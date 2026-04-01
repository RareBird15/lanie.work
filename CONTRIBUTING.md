# Contributing Guidelines

Thank you for your interest in contributing to my digital garden!

Because this site serves as a live accessibility testing ground and my personal workspace, contributions that improve
screen reader navigation, semantic structure, or workflow automation are always deeply appreciated.

## Getting Started

### Prerequisites

- Python (version 3.10 or higher)
- `uv` (Fast Python package installer and resolver)
- Git

### Setup

1. Clone the repository: `git clone https://github.com/RareBird15/lanie.work.git`
2. Navigate to the directory: `cd lanie.work`
3. Install dependencies and set up pre-commit hooks (if configured): `uv pip install pre-commit && pre-commit install`
4. Start the local development server: `uv run make serve`

## Development Workflow

### Running Locally

```bash
# Start the local development server with live reload
uv run make serve

# Build the static site for production
uv run make html

# Run linters manually (if pre-commit is installed)
pre-commit run --all-files

# Clean generated files
uv run make clean
```

### Pre-commit Hooks

This project uses `pre-commit` to maintain code quality and prevent accessibility regressions. Hooks run automatically
before each commit and include:

- Trailing whitespace removal
- End-of-file fixing
- YAML syntax checking
- Markdown linting (with custom rules to allow Pelican templating)

To skip hooks in an emergency (not recommended):

```bash
git commit --no-verify
```

## Code & Content Style

### Markdown

- **Headers:** Use ATX-style headers (`#` syntax) strictly sequentially. Do not skip heading levels (e.g., jumping from
  `##` to `####`), as this disrupts screen reader navigation.
- **Line Length:** Keep line length under 120 characters (prose-wrap preferred) to make raw files readable.
- **Lists:** Use dashes (`-`) or asterisks (`*`) for unordered lists. Keep list items concise to respect cognitive load.
- **Code Blocks:** Always specify a language for fenced code blocks (e.g., `bash`, `python`, `c`).

### Frontmatter (YAML)

- Use Title Case for keys (e.g., `Title`, `Date`, `Category`).
- Do not put a space before the colon (use `Key: Value`, not `Key : Value`).
- Always include a `Summary` for `content/writing/` posts so the automated Pelican index renders correctly.

### Accessibility Standards

This site is built around a **Persistent Text** and **Keyboard-First** interaction model.

- **Alt Text:** All images must have descriptive alt text. Avoid phrases like "Image of" or "Picture of"—screen readers
  announce this automatically.
- **Semantic HTML:** Rely on native HTML5 landmarks (nav, main, footer) provided by the Flex theme.
- **Link Clarity:** Never use "Click here" or "Read more." Link text must describe its destination independently of the
  surrounding text.
- **Sensory Agnostic:** Do not provide instructions that rely on spatial relationships (e.g., "click the button on the
  right") or color alone.
- **Testing:** If making structural changes, test with NVDA (or another screen reader) and ensure the site remains fully
  operable via keyboard.

## Submitting Changes

1. Create a new branch for your changes (`git checkout -b feature/your-feature-name`).
2. Make your changes with clear, descriptive commits.
3. Ensure the site builds successfully (`uv run make html`).
4. Push your branch and create a Pull Request.

## Questions?

Feel free to open an issue for any questions or concerns! If you are proposing a major structural change, please open an
issue first to discuss whether it aligns with the site's low-cognitive-load philosophy.
