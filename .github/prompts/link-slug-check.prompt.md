# Internal Link and Slug Safety Pass

Check the currently open Markdown page for internal link and slug safety.

Make direct edits only when confidence is high.

## Validate

1. Internal links match expected site paths
2. Link text is descriptive
3. No obvious broken or stale internal references
4. Slug references align with existing content naming

## Rules

- Preserve front matter.
- Do not change page slug unless explicitly asked.
- Do not guess missing routes.
- If uncertain, leave unchanged and report.

## Output

Edit the file directly.

After editing, reply with only:

## Changed

- Internal link fixes made

## Left alone

- Links intentionally unchanged

## Check manually

- Links/slugs requiring manual verification
