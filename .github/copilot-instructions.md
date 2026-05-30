# Copilot instructions for lanie.work

This repository is Lanie's personal website and public home base. It is not a corporate portfolio, academic publication,
or generic professional brand site.

## Voice and tone

When editing Markdown content, preserve Lanie's natural voice.

Prefer writing that is:

- plainspoken
- informal but clear
- direct
- human
- specific
- scannable
- accessible to tired readers and screen reader users

Contractions are fine and usually preferred.

Prefer natural contractions in narrative prose when they improve flow and sound more like Lanie (for example: "wasn't"
instead of "was not"). Keep uncontracted forms only when emphasis, cadence, or precision clearly benefits from it.

Do not make the writing sound corporate, academic, detached, or over-polished.

Avoid em dashes unless the existing text already uses them naturally.

Prefer "this sounds like Lanie, but clearer and easier to follow" over "this sounds more professional."

Avoid awkward synonym swaps done only to prevent repetition. Use the phrase that sounds most natural in plain speech,
even if a nearby sentence uses a related word.

Preferred wording examples:

- Prefer "wasn't" over "was not" when no extra emphasis is needed.
- Prefer "I'm" over "I am" in personal narrative sentences.
- Prefer "this helps explain" over more absolute phrasing when discussing uncertainty.
- Prefer "useful" over stiffer alternatives like "utilized" or "leveraged."

## Editing priorities

When editing site content, prioritize:

1. Accuracy
2. Clarity
3. Accessibility
4. Trust and boundaries
5. Preserving Lanie's voice

Do not polish for formality by default.

Suggest more formal wording only when it improves clarity, safety, legal/affiliate disclosure, boundaries, or trust.

## Content rules

Do not invent facts, services, experience, diagnoses, tools, or current usage.

If something sounds outdated or inconsistent, flag it instead of silently changing it.

When describing services, keep clear boundaries:

- Lanie provides accessibility, usability, and product feedback.
- Do not imply she provides legal compliance audits, WCAG certification, VPATs, ACRs, or full regression QA.
- Do not make her sound like a full-time agency or corporate consultant.

When describing accessibility, focus on lived experience, practical barriers, screen reader use, keyboard access,
cognitive load, fatigue, information persistence, and overlapping disabilities.

## Markdown style

Use simple Markdown.

Keep paragraphs short.

Use headings and bullets when they make the page easier to scan.

Avoid complex tables unless they genuinely help.

Keep link text descriptive.

Do not use visual-only language.

Do not add emojis to site content.

## Code and tooling

This is a Hugo site.

Preserve front matter.

Do not change slugs unless asked.

Do not break existing internal links.

Prefer small, focused edits over large rewrites.

### Hugo & Congo Technical Context

- **Single Config File**: The site uses a single `hugo.yaml` file for all settings. Reject suggestions involving
  `config.toml`, `hugo.toml`, or separate files in `config/_default/`.
- **Congo Theme Structure**: The site uses the Congo theme via Hugo modules.
- **Taxonomies**: Congo handles tags via `showTaxonomies: true` under `params.article`. It does not use `showTags`.
- **Front Matter Format**: Use YAML front matter arrays for tags and categories (e.g., `tags: ["tech", "gaming"]`).
  Never use Pelican-style comma-separated strings.
- **Congo Shortcodes**: When embedding media or components, prefer Congo-native shortcodes:
  - Use `{{< icon "name" >}}` for icons.
  - Use `{{< alert >}}content{{< /alert >}}` for callouts.
  - Use `{{< figure src="img.jpg" >}}` for images rather than standard Markdown syntax to ensure proper styling.

## How to respond to rewrite and cleanup requests

When Lanie asks for a rewrite, cleanup, or voice pass on a Markdown file, prefer editing the open file directly instead
of pasting a full rewritten page into chat.

After making edits, give a short summary.

Do not provide a full replacement file unless Lanie specifically asks for one.

The goal is to make changes easy to review with VS Code diffs.

Before finishing any rewrite or cleanup pass, do a short final voice check for:

1. natural contractions in places where uncontracted phrasing sounds stiff
2. less formal alternatives for corporate or academic wording
3. awkward phrase substitutions that sound less human than the original wording
