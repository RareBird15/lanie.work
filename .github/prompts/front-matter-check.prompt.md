# Front Matter Consistency Check

Check and fix front matter in the currently open Markdown file.

## Validate

1. Required keys are present and valid
2. `title`, `slug`, `date`, and `description` are coherent
3. Category and tag style is consistent with repo usage
4. Boolean fields are valid booleans
5. No accidental front matter/body mixing

## Rules

- Preserve body wording unless a front matter value clearly conflicts with content.
- Do not change slugs unless obviously broken.
- Do not invent facts.

## Output

Edit the file directly.

After editing, reply with only:

## Changed

- Front matter fixes made

## Left alone

- Fields intentionally unchanged

## Check manually

- Any metadata that needs author confirmation
