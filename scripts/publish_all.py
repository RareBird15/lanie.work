"""Master script to publish the latest Pelican post to Mastodon and Facebook."""

from __future__ import annotations

import logging
import os
from typing import TYPE_CHECKING, Any, Final, Protocol, cast

import requests
from dotenv import load_dotenv

if TYPE_CHECKING:
    from collections.abc import Sequence

import feedparser  # pyright: ignore[reportMissingTypeStubs]
from mastodon import Mastodon  # pyright: ignore[reportMissingTypeStubs]

# Load local .env
load_dotenv()

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


# --- Platform Handlers ---


def publish_to_mastodon(title: str, url: str, tags: list[str]) -> bool:
    """Announce post on Mastodon with duplicate detection."""
    try:
        client = cast(
            'Any',
            Mastodon(
                access_token=os.environ['MASTODON_TOKEN'],
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
    page_id = os.environ['FB_PAGE_ID']
    access_token = os.environ['FB_ACCESS_TOKEN']
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
    tags = [tag['term'].replace(' ', '') for tag in latest.tags]

    # 2. Distribute
    m_success = publish_to_mastodon(title, url, tags)
    f_success = publish_to_facebook(title, url)

    return 0 if (m_success and f_success) else 1


if __name__ == '__main__':
    import sys

    sys.exit(main())
