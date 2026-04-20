"""Master script to publish the latest Pelican post to social media."""

from __future__ import annotations

import logging
import os
from pathlib import Path
from typing import TYPE_CHECKING, Any, Final, Protocol, cast

import requests
from dotenv import load_dotenv

if TYPE_CHECKING:
    from collections.abc import Sequence

import feedparser
from mastodon import Mastodon

# Load local .env
ROOT_DIR: Final = Path(__file__).resolve().parent.parent
ENV_FILE: Final = ROOT_DIR / '.env'
load_dotenv(dotenv_path=ENV_FILE, override=True)

# Constants
FEED_URL: Final = 'https://lanie.work/feeds/all.rss.xml'
MASTODON_BASE_URL: Final = 'https://allovertheplace.ca'
RECENT_STATUS_LIMIT: Final = 10

logger = logging.getLogger(__name__)

# --- Protocols ---


class FeedEntry(Protocol):
    link: str
    title: str
    tags: Sequence[dict[str, str]]


class ParsedFeed(Protocol):
    entries: Sequence[FeedEntry]


def get_required_env(name: str) -> str | None:
    """Return a normalized env value, or None if missing/blank."""
    value = os.environ.get(name)
    if value is None:
        return None
    value = value.strip()
    return value or None


# --- Platform Handlers ---


def publish_to_linkedin(title: str, url: str, tags: list[str]) -> bool:
    """Announce post on LinkedIn Personal Profile."""
    token = get_required_env('LI_PERSONAL_TOKEN')
    urn = get_required_env('LI_PERSON_URN')
    missing = [
        name
        for name, value in (
            ('LI_PERSONAL_TOKEN', token),
            ('LI_PERSON_URN', urn),
        )
        if not value
    ]
    if missing:
        logger.error('LinkedIn: Missing environment variables: %s', ', '.join(missing))
        return False

    endpoint = 'https://api.linkedin.com/v2/ugcPosts'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'X-Restli-Protocol-Version': '2.0.0',
    }

    # Format tags into hashtags
    hashtags = ' '.join([f'#{tag}' for tag in tags])
    message = f'New Blog Post: {title}\n\n{hashtags}'

    payload = {
        'author': urn,
        'lifecycleState': 'PUBLISHED',
        'specificContent': {
            'com.linkedin.ugc.ShareContent': {
                'shareCommentary': {'text': message},
                'shareMediaCategory': 'ARTICLE',
                'media': [
                    {'status': 'READY', 'originalUrl': url, 'title': {'text': title}}
                ],
            }
        },
        'visibility': {'com.linkedin.ugc.MemberNetworkVisibility': 'PUBLIC'},
    }

    try:
        response = requests.post(endpoint, headers=headers, json=payload, timeout=10)
    except Exception:
        logger.exception('LinkedIn Exception')
        return False
    else:
        if response.status_code == 201:
            logger.info("LinkedIn: Successfully posted '%s'", title)
            return True
        if response.status_code == 422 and 'DUPLICATE_POST' in response.text:
            logger.info("LinkedIn: Duplicate prevented for '%s'", title)
            return True
        logger.error('LinkedIn Error (%s): %s', response.status_code, response.text)
        return False


def publish_to_mastodon(title: str, url: str, tags: list[str]) -> bool:
    """Announce post on Mastodon with duplicate detection."""
    try:
        # Check if token exists before initializing
        m_token = get_required_env('MASTODON_TOKEN')
        if not m_token:
            logger.error('Mastodon: Missing MASTODON_TOKEN')
            return False

        client = cast(
            'Any',
            Mastodon(
                access_token=m_token,
                api_base_url=MASTODON_BASE_URL,
            ),
        )

        # Duplicate check
        account = client.account_verify_credentials()
        recent = client.account_statuses(account.id, limit=RECENT_STATUS_LIMIT)
        if any(url in status.content for status in recent):
            logger.info("Mastodon: Duplicate prevented for '%s'", title)
            return True

        hashtags = ' '.join([f'#{tag}' for tag in tags])
        message = f'New post: {title}\n\n{url}\n\n{hashtags}'
        client.status_post(message.strip())
        logger.info("Mastodon: Successfully posted '%s'", title)
    except Exception:
        logger.exception('Mastodon Error')
        return False
    else:
        return True


def publish_to_facebook(title: str, url: str) -> bool:
    """Announce post on Facebook Page via Graph API."""
    page_id = get_required_env('FB_PAGE_ID')
    access_token = get_required_env('FB_ACCESS_TOKEN')
    missing = [
        name
        for name, value in (
            ('FB_PAGE_ID', page_id),
            ('FB_ACCESS_TOKEN', access_token),
        )
        if not value
    ]
    if missing:
        logger.error('Facebook: Missing environment variables: %s', ', '.join(missing))
        return False

    endpoint = f'https://graph.facebook.com/v21.0/{page_id}/feed'

    payload = {
        'message': f'New Blog Post: {title}',
        'link': url,
        'access_token': access_token,
    }

    try:
        response = requests.post(endpoint, data=payload, timeout=10)
    except Exception:
        logger.exception('Facebook Exception')
        return False
    else:
        if response.ok:
            logger.info("Facebook: Successfully posted '%s'", title)
            return True
        logger.error('Facebook Error (%s): %s', response.status_code, response.text)
        return False


# --- Main Logic ---


def main() -> int:
    logging.basicConfig(level=logging.INFO, format='%(message)s')

    # 1. Get Latest Post
    feedparser_module: Any = feedparser
    parsed_feed = cast('ParsedFeed', feedparser_module.parse(FEED_URL))
    if not parsed_feed.entries:
        logger.info('Feed is empty.')
        return 0

    latest = parsed_feed.entries[0]
    title, url = latest.title, latest.link

    # Process tags: replaces spaces to make valid hashtags
    tags = [tag['term'].replace(' ', '') for tag in latest.tags]

    # 2. Distribute
    m_success = publish_to_mastodon(title, url, tags)
    f_success = publish_to_facebook(title, url)
    l_success = publish_to_linkedin(title, url, tags)

    # Return 0 only if all enabled platforms succeed
    return 0 if (m_success and f_success and l_success) else 1


if __name__ == '__main__':
    import sys

    sys.exit(main())
