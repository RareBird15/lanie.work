# lanie.work

[![Deploy](https://github.com/RareBird15/lanie.work/actions/workflows/deploy.yml/badge.svg)](https://github.com/RareBird15/lanie.work/actions/workflows/deploy.yml)

Homepage and resource hub for Lanie Carmelo: Christian, accessibility tester, neurodivergent programmer, and disability
advocate. This site documents my access needs, technical workflows, personal essays, faith reflections, and advocacy
work.

## Features

- **Accessible design:** Built with low cognitive load, keyboard navigation, and screen reader usability in mind.
- **Static site:** Built with [Hugo](https://gohugo.io/) for fast, reliable static publishing.
- **Automated deployment:** Deployed through GitHub Actions and Cloudflare Pages.
- **Social publishing helper:** Python helper scripts can queue new posts to Buffer-connected social channels.
- **Contact form:** A Cloudflare Worker handles contact form submissions with Turnstile spam protection.

## Writing Workflow

To add a new essay or article:

1. Create a new Markdown file in the appropriate Hugo content folder.
2. Add YAML front matter.
3. Write the post content below the front matter.
4. Build and preview locally.
5. Commit and push.

Example post front matter:

```yaml
---
title: Your Article Title
date: 2026-05-21
description: A short description for summaries and previews.
draft: false
tags:
  - accessibility
  - technology
categories:
  - Technology
---
```

## Quick Start

### Prerequisites

- [Hugo](https://gohugo.io/)
- Python 3.14 or newer
- [uv](https://docs.astral.sh/uv/)
- Git

### Local Development Setup

```bash
# Clone the repository
git clone https://github.com/RareBird15/lanie.work.git
cd lanie.work

# Install Python helper dependencies
uv sync

# Start Hugo's local development server
hugo server
```

Visit the local URL printed by Hugo to view the site.

### Production Build

```bash
hugo
```

This generates the static site in:

```text
public/
```

## Buffer Publishing Scripts

This repository includes Python helper scripts for Buffer-based social publishing.

The main publish script reads the generated Hugo RSS feed, finds the latest post, queues it to Buffer, and records what
has already been queued so rebuilds do not repeatedly queue the same post.

Required environment variables:

```bash
BUFFER_API_KEY=your_buffer_api_key
BUFFER_CHANNEL_IDS=comma,separated,buffer,channel,ids
BUFFER_FACEBOOK_CHANNEL_IDS=comma,separated,facebook,channel,ids
```

Useful scripts:

```bash
# List Buffer organizations and channels
uv run ./scripts/get_buffer_org_ids.py

# Queue a harmless test post
uv run ./scripts/test_buffer_post.py

# Queue the latest generated RSS post to Buffer
uv run ./scripts/publish_latest_to_buffer.py
```

Before running the publish script, build the site so the RSS feed exists:

```bash
hugo
uv run ./scripts/publish_latest_to_buffer.py
```

The publish state is stored in:

```text
data/buffer-published.json
```

## Project Structure

```text
lanie.work/
├── content/                         # Hugo content files
├── data/                            # Data files, including Buffer publish state
├── layouts/                         # Hugo layout overrides, if any
├── public/                          # Generated site output
├── scripts/                         # Python helper scripts
├── static/                          # Static assets
├── themes/                          # Legacy theme submodules, if any
├── services/form-handler/           # Cloudflare Worker code
├── .github/
│   └── workflows/                   # CI/CD workflows
├── pyproject.toml                   # Python helper dependencies
├── requirements.txt                 # Compiled Python requirements, if needed
└── README.md                        # Project overview
```

## Content Guidelines

### Markdown and Formatting

- Use ATX-style headers (`#` syntax) for logical screen reader navigation.
- Do not skip heading levels.
- Keep paragraphs short and scannable.
- Always include descriptive `alt` text for images.
- Specify a language for fenced code blocks, such as `bash`, `python`, `toml`, or `text`.
- Use descriptive link text. Avoid vague links like “click here” or “read more.”

### Accessibility Philosophy

- **Text over audio:** Provide persistent text for all critical information.
- **Low cognitive load:** Use clear structure, short sections, and plain language where possible.
- **Keyboard-first:** Pages and interactive elements should work without a mouse.
- **No spatial reliance:** Avoid instructions that depend on visual placement, color alone, or layout alone.

### Accessibility Baseline

These are baseline decisions to preserve when making future design or content updates:

- **Navigation:** Mobile menu uses compact spacing and always-visible underlines so links are easier to identify.
- **Links in content:** In-body links use visible underlines with stronger thickness and contrast for readability.
- **Table of contents:** TOC stays expanded on desktop and defaults collapsed on smaller screens.
- **Blog browsing:** Blog is a top-level page that aggregates recent posts with pagination.
- **Contact fallback:** If the form or Turnstile fails (or JavaScript is disabled), contact fallback is
  [lanie@lanie.work](mailto:lanie@lanie.work).

When changing styles or navigation structure, re-check these behaviors to avoid regressions.

## Contributing

Contributions are welcome, especially improvements to accessibility, semantic structure, documentation, and workflow
automation.

Please read `CONTRIBUTING.md` before submitting changes.

## Links

- **Website:** [lanie.work](https://lanie.work)
- **Mastodon:** [@RareBird15@allovertheplace.ca](https://allovertheplace.ca/@RareBird15)
- **GitHub:** [RareBird15](https://github.com/RareBird15)
- **LinkedIn:** [laniecarmelo](https://www.linkedin.com/in/laniecarmelo/)
- **Code::Stats:** [RareBird15](https://codestats.net/users/RareBird15)

## Acknowledgments

Built with [Hugo](https://gohugo.io/), hosted on [Cloudflare Pages](https://pages.cloudflare.com/), and supported by
small Python helper scripts managed with [uv](https://docs.astral.sh/uv/).
