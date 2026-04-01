"""Configuration file for Lanie's Pelican site."""

AUTHOR = "Lanie"
SITENAME = "Lanie: Faith, Tech & Advocacy"
SITESUBTITLE = (
    "Working at the intersection of faith, technology, and disability advocacy."
)
SITEURL = ""  # Leave blank for local development
SITELOGO = "/images/avatar-simple.svg"

PATH = "content"
TIMEZONE = "America/Chicago"
DEFAULT_LANG = "en"

# --- Feed settings ---
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# --- Blogroll (Text Links) ---
LINKS = (
    ("GitHub", "https://github.com/RareBird15"),
    ("Code::Stats", "https://codestats.net/users/RareBird15"),
    ("Email", "mailto:lanie.rarebird15@gmail.com"),
)

# --- Social widget (Icon Links) ---
SOCIAL = (
    ("mastodon", "https://allovertheplace.ca/@RareBird15"),
    ("linkedin", "https://www.linkedin.com/in/laniecarmelo/"),
    ("reddit", "https://www.reddit.com/user/Laniebird91/"),
)

# --- URL Settings (Clean URLs) ---
ARTICLE_URL = "writing/{slug}/"
ARTICLE_SAVE_AS = "writing/{slug}/index.html"
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"
CATEGORY_URL = "{slug}/"
CATEGORY_SAVE_AS = "{slug}/index.html"

# These ensure the Archives/Tags/Categories pages also use Clean URLs
ARCHIVES_SAVE_AS = "archives/index.html"
CATEGORIES_SAVE_AS = "categories/index.html"
TAGS_SAVE_AS = "tags/index.html"

DEFAULT_PAGINATION = False
RELATIVE_URLS = True  # Better for testing locally in WSL

# --- Markdown Extensions ---
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.meta": {},
        "markdown.extensions.extra": {},
        "markdown.extensions.toc": {"title": "Table of Contents"},
        "markdown.extensions.admonition": {},
    },
    "output_format": "html5",
}

# --- Theme and UI ---
THEME = "themes/Flex"
DISPLAY_CATEGORIES_ON_MENU = True
MAIN_MENU = True
COPYRIGHT_YEAR = 2026

# Flex specific settings
BROWSER_COLOR = "#333333"
ROBOTS = "index, follow"

# This maps the top navigation bar to your clean URLs
MENUITEMS = (
    ("Archives", "/archives/"),
    ("Categories", "/categories/"),
    ("Tags", "/tags/"),
)

# Save the 'blog' index elsewhere if you want a static home page
INDEX_SAVE_AS = "writing/index.html"
