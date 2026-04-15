"""Configuration file for Lanie's Pelican site."""

THEME = "themes/reflex"
THEME_COLOR = "dark"
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

AUTHOR = "Lanie"
SITENAME = "Lanie: Faith, Tech & Advocacy"
SITETITLE = "Lanie"
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
)

# --- Social widget (Icon Links) ---
SOCIAL = (
    ("mastodon", "https://allovertheplace.ca/@RareBird15"),
    ("linkedin", "https://www.linkedin.com/in/laniecarmelo/"),
    ("reddit", "https://www.reddit.com/user/Laniebird91/"),
)

# --- URL Settings (Clean URLs) ---
ARTICLE_URL = "{category}/{slug}/"
ARTICLE_SAVE_AS = "{category}/{slug}/index.html"
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"
CATEGORY_URL = "category/{slug}/"
CATEGORY_SAVE_AS = "category/{slug}/index.html"

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
        "markdown.extensions.toc": {"title": ""},
        "markdown.extensions.admonition": {},
    },
    "output_format": "html5",
}

DISPLAY_CATEGORIES_ON_MENU = True
MAIN_MENU = True
COPYRIGHT_YEAR = 2026

# Reflex specific settings
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

PLUGINS = [
    # "pelican.plugins.seo",
    "pelican.plugins.sitemap",
    "pelican.plugins.yaml_metadata",
    "pelican.plugins.share_post",
    "pelican.plugins.related_posts",
    # "pelican.plugins.readtime",
    "pelican.plugins.search",  # The new addition
    "pelican.plugins.neighbors",
    "pelican.plugins.statistics",
]

# Set once: Sitemaps help search engines crawl your site
SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.5, "indexes": 0.5, "pages": 0.5},
    "changefreqs": {"articles": "monthly", "indexes": "daily", "pages": "monthly"},
}

# Stork Search Configuration
STORK_INPUT_OPTIONS = {
    "base_directory": "content",
    "url_prefix": SITEURL,
    "html_selector": "main",
}

CC_LICENSE = {
    "name": "Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License",
    "version": "4.0",
    "slug": "by-nc-sa",
}

MINIFY = {
    "host": "localhost",
    "port": 8000,
    "webpath": "/",
    "cachepath": "./cache",
    "css_min": True,
    "js_min": True,
    "html_min": True,
    "inline_css_min": True,
    "inline_js_min": True,
}
