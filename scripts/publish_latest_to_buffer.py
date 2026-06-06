"""Publish the latest Hugo RSS post to Buffer.

This script:
- Reads the latest post from a local Hugo RSS feed
- Queues the post in Buffer for configured channels
- Avoids queueing the same URL to the same channel twice
- Handles Facebook's required post type metadata

Required environment variables:
- BUFFER_API_KEY
- BUFFER_CHANNEL_IDS

Optional environment variables:
- BUFFER_FACEBOOK_CHANNEL_IDS
- BUFFER_STATE_FILE
- BLOG_FEED_FILE
"""

from __future__ import annotations

import json
import logging
import os
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Final, Protocol, cast

import feedparser
import requests
from dotenv import load_dotenv

ROOT_DIR: Final = Path(__file__).resolve().parent.parent
ENV_FILE: Final = ROOT_DIR / ".env"

BUFFER_API_URL: Final = "https://api.buffer.com"

DEFAULT_FEED_FILE: Final = ROOT_DIR / "public" / "index.xml"
DEFAULT_STATE_FILE: Final = ROOT_DIR / "data" / "buffer-published.json"

logger = logging.getLogger(__name__)


class MissingEnvironmentVariableError(RuntimeError):
    """Raised when a required environment variable is missing."""

    def __init__(self, name: str) -> None:
        """Build a message naming the missing environment variable."""
        super().__init__(f"Missing required environment variable: {name}")


class EmptyBufferChannelIdsError(RuntimeError):
    """Raised when BUFFER_CHANNEL_IDS is configured but empty."""

    def __init__(self) -> None:
        """Build a message for an empty configured channel ID list."""
        super().__init__("BUFFER_CHANNEL_IDS is set, but no channel IDs were found.")


class BufferHttpError(RuntimeError):
    """Raised when Buffer returns a non-2xx HTTP response."""

    def __init__(self, status_code: int, body: str) -> None:
        """Build a message including HTTP status and response body."""
        super().__init__(f"Buffer HTTP error {status_code}: {body}")


class BufferGraphQLError(RuntimeError):
    """Raised when Buffer returns GraphQL errors."""

    def __init__(self, errors: object) -> None:
        """Build a message including the GraphQL errors payload."""
        super().__init__(f"Buffer GraphQL error: {errors}")


class InvalidPublishStateError(TypeError):
    """Raised when the publish state file is not a JSON object."""

    def __init__(self, state_file: Path) -> None:
        """Build a message naming the invalid state file path."""
        super().__init__(f"State file is not a JSON object: {state_file}")


class FeedFileNotFoundError(FileNotFoundError):
    """Raised when the RSS feed file cannot be found."""

    def __init__(self, feed_file: Path) -> None:
        """Build a message with recovery guidance for missing feed files."""
        super().__init__(
            f"Feed file not found: {feed_file}\n"
            "Run Hugo first, or set BLOG_FEED_FILE to the correct feed path."
        )


class EmptyFeedError(RuntimeError):
    """Raised when the RSS feed has no entries."""

    def __init__(self, feed_file: Path) -> None:
        """Build a message naming the feed file with no entries."""
        super().__init__(f"Feed has no entries: {feed_file}")


class FeedEntry(Protocol):
    """Small subset of feedparser entry fields we use."""

    link: str
    title: str


class ParsedFeed(Protocol):
    """Small subset of feedparser parsed feed fields we use."""

    entries: list[FeedEntry]


def load_environment() -> None:
    """Load local .env values when running outside GitHub Actions."""
    load_dotenv(dotenv_path=ENV_FILE, override=True)


def get_env(name: str) -> str | None:
    """Return a normalized environment variable, or None if missing."""
    value = os.environ.get(name)

    if value is None:
        return None

    value = value.strip()
    return value or None


def require_env(name: str) -> str:
    """Return a required environment variable or raise a clear error."""
    value = get_env(name)

    if value is None:
        raise MissingEnvironmentVariableError(name)

    return value


def get_feed_file() -> Path:
    """Return the local RSS feed file path."""
    raw_path = get_env("BLOG_FEED_FILE")

    if raw_path is None:
        return DEFAULT_FEED_FILE

    return Path(raw_path).expanduser().resolve()


def get_state_file() -> Path:
    """Return the publish state file path."""
    raw_path = get_env("BUFFER_STATE_FILE")

    if raw_path is None:
        return DEFAULT_STATE_FILE

    return Path(raw_path).expanduser().resolve()


def get_channel_ids() -> list[str]:
    """Read comma-separated Buffer channel IDs from BUFFER_CHANNEL_IDS."""
    raw_channel_ids = require_env("BUFFER_CHANNEL_IDS")

    channel_ids = [
        channel_id.strip()
        for channel_id in raw_channel_ids.split(",")
        if channel_id.strip()
    ]

    if not channel_ids:
        raise EmptyBufferChannelIdsError

    return channel_ids


def get_facebook_channel_ids() -> set[str]:
    """Read comma-separated Facebook Buffer channel IDs."""
    raw_channel_ids = get_env("BUFFER_FACEBOOK_CHANNEL_IDS")

    if raw_channel_ids is None:
        return set()

    return {
        channel_id.strip()
        for channel_id in raw_channel_ids.split(",")
        if channel_id.strip()
    }


def buffer_graphql(query: str, variables: dict[str, Any]) -> dict[str, Any]:
    """Send a GraphQL request to Buffer."""
    token = require_env("BUFFER_API_KEY")

    response = requests.post(
        BUFFER_API_URL,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
        json={
            "query": query,
            "variables": variables,
        },
        timeout=20,
    )

    if not response.ok:
        raise BufferHttpError(response.status_code, response.text)

    data = response.json()

    if "errors" in data:
        raise BufferGraphQLError(data["errors"])

    return cast("dict[str, Any]", data["data"])


def load_publish_state(state_file: Path) -> dict[str, Any]:
    """Load the local publish state file."""
    if not state_file.exists():
        return {"published": {}}

    with state_file.open("r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, dict):
        raise InvalidPublishStateError(state_file)

    if "published" not in data:
        data["published"] = {}

    return data


def save_publish_state(state_file: Path, state: dict[str, Any]) -> None:
    """Save the local publish state file."""
    state_file.parent.mkdir(parents=True, exist_ok=True)

    with state_file.open("w", encoding="utf-8") as file:
        json.dump(state, file, indent=2, sort_keys=True)
        file.write("\n")


def already_published(
    state: dict[str, Any],
    post_url: str,
    channel_id: str,
) -> bool:
    """Return True if this URL was already queued for this channel."""
    published = state.get("published", {})
    post_record = published.get(post_url, {})
    channel_record = post_record.get(channel_id)

    return bool(channel_record)


def mark_published(
    state: dict[str, Any],
    post_url: str,
    channel_id: str,
    buffer_post_id: str,
) -> None:
    """Record that this URL was queued for this channel."""
    published = state.setdefault("published", {})
    post_record = published.setdefault(post_url, {})

    post_record[channel_id] = {
        "buffer_post_id": buffer_post_id,
        "queued_at": datetime.now(UTC).isoformat(),
    }


def get_latest_post_from_feed(feed_file: Path) -> tuple[str, str, list[str]]:
    """Read the latest post title, URL, and tags from the local RSS feed."""
    if not feed_file.exists():
        raise FeedFileNotFoundError(feed_file)

    parsed_feed = cast("ParsedFeed", feedparser.parse(str(feed_file)))

    if not parsed_feed.entries:
        raise EmptyFeedError(feed_file)

    latest = parsed_feed.entries[0]
    title = latest.title.strip()
    url = latest.link.strip()

    raw_tags = getattr(latest, "tags", [])
    tags = [
        tag["term"].replace(" ", "")
        for tag in raw_tags
        if isinstance(tag, dict) and tag.get("term")
    ]

    return title, url, tags


def format_social_post(title: str, url: str, tags: list[str]) -> str:
    """Create the text that Buffer will queue."""
    unique_tags = list(dict.fromkeys(tag for tag in tags if tag))
    hashtags = " ".join(f"#{tag}" for tag in unique_tags)

    parts = [
        f"New post: {title}",
        url,
    ]

    if hashtags:
        parts.append(hashtags)

    return "\n\n".join(parts).strip()


def queue_buffer_post(channel_id: str, text: str) -> str | None:
    """Queue one post for one Buffer channel and return its Buffer post ID."""
    mutation = """
    mutation CreatePost($input: CreatePostInput!) {
      createPost(input: $input) {
        ... on PostActionSuccess {
          post {
            id
            text
            status
            dueAt
          }
        }
        ... on MutationError {
          message
        }
      }
    }
    """

    post_input: dict[str, Any] = {
        "channelId": channel_id,
        "text": text,
        "schedulingType": "automatic",
        "mode": "addToQueue",
        "assets": [],
    }

    if channel_id in get_facebook_channel_ids():
        post_input["metadata"] = {
            "facebook": {
                "type": "post",
            }
        }

    variables = {
        "input": post_input,
    }

    data = buffer_graphql(mutation, variables)
    result = data["createPost"]

    if "post" in result:
        return cast("str", result["post"]["id"])

    logger.error(
        "Buffer returned an error for channel %s: %s",
        channel_id,
        result.get("message", "Unknown error"),
    )
    return None


def publish_latest_post() -> bool:
    """Publish the latest feed post to all configured Buffer channels."""
    feed_file = get_feed_file()
    state_file = get_state_file()

    title, url, tags = get_latest_post_from_feed(feed_file)
    channel_ids = get_channel_ids()
    state = load_publish_state(state_file)
    text = format_social_post(title, url, tags)

    logger.info("Latest post: %s", title)
    logger.info("URL: %s", url)
    logger.info("Channels configured: %s", len(channel_ids))

    any_failures = False
    state_changed = False

    for channel_id in channel_ids:
        if already_published(state, url, channel_id):
            logger.info("Already queued for channel %s. Skipping.", channel_id)
            continue

        try:
            buffer_post_id = queue_buffer_post(channel_id, text)
        except Exception:
            logger.exception("Failed to queue Buffer post for channel %s", channel_id)
            any_failures = True
            continue

        if buffer_post_id is None:
            any_failures = True
            continue

        logger.info(
            "Queued Buffer post %s for channel %s",
            buffer_post_id,
            channel_id,
        )

        mark_published(state, url, channel_id, buffer_post_id)
        state_changed = True

    if state_changed:
        save_publish_state(state_file, state)
        logger.info("Updated publish state: %s", state_file)

    return not any_failures


def main() -> int:
    """Run the publisher."""
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    load_environment()

    success = publish_latest_post()

    if success:
        logger.info("Publish script completed successfully.")
        return 0

    logger.error("Publish script completed with one or more failures.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
