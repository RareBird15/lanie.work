"""Stub file for jinja-lsp variable resolution.

Pelican injects these variables into Jinja2 templates at build time.
jinja-lsp cannot see them because they come from the framework, not from
pelicanconf.py. Declaring them here lets jinja-lsp resolve them and stops
the "Variable '...' is used but has not been set" warnings.

This file is NOT imported at runtime — it exists only for static analysis.
"""

# --- Pelican framework-injected globals ---
THEME_STATIC_DIR: str = ""
DEFAULT_LANG: str = ""
JINJA_ENVIRONMENT: dict = {}
ROBOTS: str = ""

# --- Site configuration (also in pelicanconf.py) ---
SITEURL: str = ""
SITENAME: str = ""
SITETITLE: str = ""
SITESUBTITLE: str = ""
SITELOGO: str = ""
AUTHOR: str = ""
LINKS: tuple = ()
SOCIAL: tuple = ()
PLUGINS: list = []

# --- Theme feature flags ---
DISPLAY_PAGES_ON_MENU: bool = True
DISPLAY_CATEGORIES_ON_MENU: bool = True
LINKS_IN_NEW_TAB: object = False  # str | bool
PAGES_SORT_ATTRIBUTE: str = ""
DISABLE_URL_HASH: bool = False
USE_GOOGLE_FONTS: bool = True
USE_LESS: bool = False
ARTICLE_HIDE_TRANSLATION: bool = False
SERIES_TEXT: str = ""
GOOGLE_ADSENSE: dict = {}

# --- Isso comment plugin ---
ISSO_URL: str = ""
ISSO_EMBED_JS_PATH: str = ""
ISSO_OPTIONS: dict = {}

# --- Template context objects ---
# Articles
articles: list = []
article: object = None
drafts: list = []
hidden_articles: list = []

# Pages
pages: list = []
page: object = None
hidden_pages: list = []
draft_pages: list = []

# Taxonomy
categories: list = []
category: object = None
tags: list = []
tag: object = None
authors: list = []
author: object = None

# Pagination
articles_page: object = None
articles_previous_page: object = None
articles_next_page: object = None
