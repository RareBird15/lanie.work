# What Should I Use?

Route this task to the best prompt, skill, or agent in this repository.

## Input

The user gives a short task description.

## Goal

Return a small, low-overwhelm recommendation with one primary choice.

## Rules

1. Prefer one primary prompt first.
2. Suggest at most one optional follow-up prompt.
3. Suggest a skill only if it clearly improves accuracy.
4. Suggest an agent only if it adds distinct value.
5. Do not suggest broad toolchains when one prompt is enough.
6. Respect repository policy that `tools-and-resources.md` is hand-written content.
7. Prefer plain language and low cognitive load in your response.

## Routing Priority

1. Content rewrite/cleanup tasks:

- `rewrite-in-lanie-voice.prompt.md`
- `cleanup-site-page.prompt.md`

2. Final checks:

- `final-check.prompt.md`
- `front-matter-check.prompt.md`
- `link-slug-check.prompt.md`
- `markdown-a11y-pass.prompt.md`

3. Specialized pages:

- `service-boundary-guard.prompt.md`
- `tools-resources-curator.prompt.md`
- `narrative-safety-pass.prompt.md`

4. Utility:

- `summary-diff.prompt.md`
- `publish-snippet.prompt.md`

5. Skills:

- `context-map`
- `what-context-needed`
- `commit-message-storyteller`
- `markdown-to-html`

6. Agents:

- `markdown-accessibility-assistant.agent.md`
- `prompt-builder.agent.md`

## Output format

Return only:

## Use first

- One prompt/skill/agent name with one-sentence reason.

## Optional next step

- Zero or one follow-up item with one-sentence reason.

## Why this is enough

- One short sentence explaining why no extra tools are needed right now.
