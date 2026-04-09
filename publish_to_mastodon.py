"""Publish the latest blog post from RSS to Mastodon, avoiding duplicates."""

from __future__ import annotations

import logging
import os
from typing import TYPE_CHECKING, Any, Protocol, cast

if TYPE_CHECKING:
    from collections.abc import Sequence

import feedparser  # pyright: ignore[reportMissingTypeStubs]
from mastodon import Mastodon  # pyright: ignore[reportMissingTypeStubs]

FEED_URL = "https://lanie.work/feeds/all.rss.xml"
MASTODON_BASE_URL = "https://allovertheplace.ca"
RECENT_STATUS_LIMIT = 10

logger = logging.getLogger(__name__)


class FeedEntry(Protocol):
    """A minimal RSS entry shape used by this script."""

    link: str
    title: str
    tags: Sequence[dict[str, str]]


class ParsedFeed(Protocol):
    """A minimal parsed RSS feed shape used by this script."""

    entries: Sequence[FeedEntry]


class MastodonAccount(Protocol):
    """The account data needed for loading recent statuses."""

    id: int | str


class MastodonStatus(Protocol):
    """A minimal status representation used for duplicate detection."""

    content: str


class MastodonClient(Protocol):
    """The subset of Mastodon client APIs used by this script."""

    def account_verify_credentials(self) -> MastodonAccount: ...
    def account_statuses(
        self, account_id: int | str, limit: int = RECENT_STATUS_LIMIT
    ) -> Sequence[MastodonStatus]: ...
    def status_post(self, status: str) -> object: ...


def setup_logging() -> None:
    """Configure script logging for informational CLI output."""
    logging.basicConfig(level=logging.INFO, format="%(message)s")


def get_latest_post(feed_url: str) -> tuple[str, str, list[str]] | None:
    """Return the latest `(title, url, tags)` triple from the RSS feed, if available."""
    feedparser_module: Any = feedparser
    parsed_feed = cast("ParsedFeed", feedparser_module.parse(feed_url))
    if not parsed_feed.entries:
        return None

    latest_entry = parsed_feed.entries[0]
    tags = [tag["term"].replace(" ", "") for tag in latest_entry.get("tags", [])]
    return latest_entry.title, latest_entry.link, tags


def build_mastodon_client() -> MastodonClient:
    """Create and return an authenticated Mastodon client instance."""
    mastodon_factory: Any = Mastodon
    return cast(
        "MastodonClient",
        mastodon_factory(
            access_token=os.environ["MASTODON_TOKEN"],
            api_base_url=MASTODON_BASE_URL,
        ),
    )


def is_duplicate_post(
    client: MastodonClient, post_url: str, *, recent_limit: int = RECENT_STATUS_LIMIT
) -> bool:
    """Check whether a post URL appears in the account's recent statuses."""
    account = client.account_verify_credentials()
    recent_statuses = client.account_statuses(account.id, limit=recent_limit)
    return any(post_url in status.content for status in recent_statuses)


def publish_post(
    client: MastodonClient, post_title: str, post_url: str, tags: list[str]
) -> None:
    """Publish a formatted post announcement to Mastodon."""
    hashtags = " ".join([f"#{tag}" for tag in tags])
    message = f"New post: {post_title}\n\n{post_url}\n\n{hashtags}"
    client.status_post(message.strip())


def main() -> int:
    """Publish the latest RSS entry to Mastodon when it has not been posted."""
    setup_logging()

    latest_post = get_latest_post(FEED_URL)
    if latest_post is None:
        logger.info("Feed is empty. Nothing to post.")
        return 0

    post_title, post_url, tags = latest_post
    mastodon_client = build_mastodon_client()

    if is_duplicate_post(mastodon_client, post_url):
        logger.info("Duplicate prevented: '%s' was already posted.", post_title)
        return 0

    publish_post(mastodon_client, post_title, post_url, tags)
    logger.info("Successfully posted: %s", post_title)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
