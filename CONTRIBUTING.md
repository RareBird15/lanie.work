# Contributing Guidelines

Thank you for your interest in contributing to this site.

Because this site serves as a live accessibility testing ground and public workspace, contributions that improve screen
reader navigation, semantic structure, documentation, or workflow automation are especially welcome.

## Getting Started

### Prerequisites

- Hugo
- Python 3.14 or newer
- `uv`
- Git
- `pre-commit`, if working with repository hooks

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/RareBird15/lanie.work.git
   ```

2. Navigate to the project directory:

   ```bash
   cd lanie.work
   ```

3. Install Python helper dependencies:

   ```bash
   uv sync
   ```

4. Install pre-commit hooks, if needed:

   ```bash
   uv run pre-commit install
   ```

5. Start the local Hugo server:

   ```bash
   hugo server
   ```

## Development Workflow

### Running Locally

```bash
# Start the local development server
hugo server

# Build the static site for production
hugo

# Run Python helper scripts
uv run ./scripts/get_buffer_org_ids.py

# Run pre-commit checks manually
uv run pre-commit run --all-files
```

## Buffer Publishing Workflow

The site uses Buffer for social publishing instead of calling each social platform directly.

The publishing helper script:

1. Reads the generated Hugo RSS feed.
2. Finds the latest post.
3. Queues it to configured Buffer channels.
4. Records the queued post in `data/buffer-published.json`.
5. Skips posts that were already queued.

Before testing the publish script, build the site:

```bash
hugo
uv run ./scripts/publish_latest_to_buffer.py
```

Required environment variables:

```bash
BUFFER_API_KEY=your_buffer_api_key
BUFFER_CHANNEL_IDS=comma,separated,buffer,channel,ids
BUFFER_FACEBOOK_CHANNEL_IDS=comma,separated,facebook,channel,ids
```

Do not commit API keys or secrets.

## Pre-commit Hooks

This project uses `pre-commit` to maintain code quality and reduce accessibility regressions.

Hooks may include:

- Trailing whitespace removal
- End-of-file fixing
- YAML/TOML syntax checks
- Markdown linting
- Python linting or formatting checks

To run hooks manually:

```bash
uv run pre-commit run --all-files
```

To skip hooks in an emergency:

```bash
git commit --no-verify
```

Skipping hooks is not recommended.

## Code and Content Style

### Markdown

- Use ATX-style headers (`#` syntax).
- Keep heading levels sequential. Do not jump from `##` to `####`.
- Keep paragraphs short and scannable.
- Use dashes (`-`) for unordered lists.
- Always specify a language for fenced code blocks.
- Use descriptive link text.

### Hugo Front Matter

Use TOML front matter unless there is a specific reason to use another format.

Example:

```toml
+++
title = "Your Article Title"
date = 2026-05-21
description = "A short summary for previews."
draft = false
tags = ["accessibility", "technology"]
categories = ["Technology"]
+++
```

Guidelines:

- Use lowercase TOML keys.
- Include a clear `title`.
- Include a useful `description` for posts.
- Set `draft = true` for unfinished work.
- Use meaningful tags and categories.

### Python

Python scripts in this repository are helper tools, not the site generator.

Guidelines:

- Keep scripts small and readable.
- Prefer clear error messages.
- Do not hard-code API keys or secrets.
- Read secrets from environment variables.
- Avoid platform-specific API integrations when Buffer can handle the publishing layer.

## Accessibility Standards

This site is built around a persistent-text and keyboard-first interaction model.

### Alt Text

All meaningful images must have descriptive alt text.

Avoid phrases like:

- “Image of”
- “Picture of”
- “Graphic of”

Screen readers already announce images.

### Semantic Structure

Use semantic HTML and Hugo templates that preserve logical document structure.

Important checks:

- One clear page title.
- Logical heading order.
- Descriptive navigation.
- Descriptive link text.
- No keyboard traps.

### Link Clarity

Avoid vague link text such as:

- “Click here”
- “Read more”
- “Learn more”

Use link text that describes the destination independently.

### Sensory-Agnostic Instructions

Do not write instructions that rely only on:

- Color
- Shape
- Visual position
- Sound
- Mouse movement

Instead of:

```text
Click the button on the right.
```

Use:

```text
Select the Save button.
```

### Testing

For structural or layout changes, test that:

1. The site can be navigated by keyboard.
2. Headings form a logical outline.
3. Links make sense out of context.
4. Images have appropriate alt text.
5. Forms have labels and useful error messages.

Screen reader testing with NVDA, JAWS, VoiceOver, or another screen reader is appreciated when possible.

## Submitting Changes

1. Create a new branch:

   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make changes with clear, descriptive commits.

3. Build the site:

   ```bash
   hugo
   ```

4. Run checks:

   ```bash
   uv run pre-commit run --all-files
   ```

5. Push your branch and create a pull request.

## Questions

Open an issue for questions or concerns.

For major structural changes, please open an issue first to discuss whether the change fits the site's accessibility,
low-cognitive-load, and maintainability goals.
