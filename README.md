# lanie.work

[![CI](https://github.com/RareBird15/lanie.work/actions/workflows/pelican-gh-pages.yml/badge.svg)](https://github.com/RareBird15/lanie.work/actions/workflows/pelican-gh-pages.yml)

Homepage and resource hub for Lanie Carmelo: Christian, accessibility tester, neurodivergent programmer, and disability
advocate. This site documents my access needs, technical workflows, and personal essays.

## 🌟 Features

- **Accessible Design:** Built with low cognitive load in mind. Tested extensively with NVDA.
- **Python-Powered:** Generated statically using **Pelican** and managed with **`uv`**.
- **Automated Indexing:** Articles and essays are automatically organized without manual curation.
- **Keyboard-Centric:** Designed for screen reader and keyboard navigation from the ground up.

## 📝 Writing Workflow (Automated)

You no longer need to manually update a `writing.md` list. Pelican handles the routing and index generation
automatically.

To add a new essay or article:

1. Create a new markdown file in the `content/writing/` folder.
2. Add the standard Pelican YAML frontmatter (fenced by `---`):

   ```yaml
   ---
   Title: Your Article Title
   Date: YYYY-MM-DD
   Category: Writing
   Slug: your-custom-slug
   Summary: A short description for the index page.
   ---
   ```

3. Write your content below the frontmatter.
4. Commit and push. The CI/CD pipeline will automatically build and publish the new article to the `/writing/` index.

## 🚀 Quick Start

### Prerequisites

- Python (3.10+)
- `uv` (Fast Python package installer and resolver)
- Git

### Local Development Setup

```bash
# Clone the repository
git clone [https://github.com/RareBird15/lanie.work.git](https://github.com/RareBird15/lanie.work.git)
cd lanie.work

# Build the site
uv run make html

# Start the local development server (live preview)
uv run make serve
```

Visit `http://localhost:8000` to view the site locally.

## 🛠️ Project Structure

This project uses a clean separation of static pages and chronological writing.

```text
lanie.work/
├── pelicanconf.py           # Main Pelican configuration
├── publishconf.py           # Production build settings
├── content/
│   ├── pages/               # Static navigation pages (About, Work, Accessibility Notes)
│   └── writing/             # Chronological essays and articles
├── themes/
│   └── Flex/                # Accessible, responsive theme
├── .github/
│   └── workflows/
│       └── pelican-gh-pages.yml # CI/CD deployment pipeline
├── .markdownlint.json       # Minimal markdown linting rules
└── README.md                # Project overview
```

## 📐 Content Guidelines

### Markdown & Formatting

- Use **ATX-style headers** (`#` syntax) for logical screen reader navigation.
- Keep line length to 120 characters (Prose-wrap preferred).
- Always include descriptive `alt` text for images.
- Specify a language for fenced code blocks (e.g., `bash`, `python`, `c`).

### Accessibility Philosophy

- **Text over Audio:** Provide persistent text for all critical information.
- **Low Cognitive Load:** Use clear bullet points and avoid "walls of text."
- **No Spatial Reliance:** Avoid directions or instructions that require mental mapping or visual-only placement.

## 🤝 Contributing

Contributions are welcome! Please read `CONTRIBUTING.md` for details on our code of conduct and the process for
submitting pull requests.

## 🔗 Links

- **Website:** [lanie.work](https://lanie.work)
- **Mastodon:** [@RareBird15@allovertheplace.ca](https://allovertheplace.ca/@RareBird15)
- **GitHub:** [RareBird15](https://github.com/RareBird15)
- **LinkedIn:** [laniecarmelo](https://www.linkedin.com/in/laniecarmelo/)
- **Code::Stats:** [RareBird15](https://codestats.net/users/RareBird15)

## 🙏 Acknowledgments

Powered by [Pelican](https://getpelican.com/), styled with the [Flex](https://github.com/alexandrevicenzi/Flex) theme,
and hosted on [GitHub Pages](https://pages.github.com/).
