# Start Here: Prompt, Skill, and Agent Map

This file is a quick chooser for low-energy days.

Use this rule:

- Start with the smallest tool that can do the job.
- Use one prompt first.
- Add a skill or agent only if needed.

## Daily Drivers (Use First)

1. `cleanup-site-page.prompt.md`

- Use for most page cleanup and polish work.

2. `rewrite-in-lanie-voice.prompt.md`

- Use for targeted rewrite passes in Lanie voice.

3. `final-check.prompt.md`

- Use right before publishing.

4. `markdown-accessibility-assistant.agent.md`

- Use when you want a stronger markdown a11y pass.

5. `prompt-builder.agent.md`

- Use when writing or improving prompts/instructions.

## If This, Use This

### I am writing or rewriting content

- Rewrite selected text: `rewrite-in-lanie-voice.prompt.md`
- Clean up a full page: `cleanup-site-page.prompt.md`
- New page scaffold: `new-page-scaffold-hugo-lanie-voice.prompt.md`

### I need safety, consistency, and checks

- Final quality pass: `final-check.prompt.md`
- Front matter check: `front-matter-check.prompt.md`
- Internal link/slug check: `link-slug-check.prompt.md`
- Markdown a11y check: `markdown-a11y-pass.prompt.md`

### This is a high-stakes personal narrative page

- `narrative-safety-pass.prompt.md`
- Then run: `final-check.prompt.md`

### This is a services/scope page

- `service-boundary-guard.prompt.md`
- Then run: `cleanup-site-page.prompt.md`

### This is Tools and Resources

- `tools-resources-curator.prompt.md`
- Keep hand-written style. Do not convert to generated index format.

### I want a clean summary after edits

- `summary-diff.prompt.md`

### I need short publish text

- `publish-snippet.prompt.md`

## Skills (Use When Needed)

- `context-map`
- Use before multi-file changes to map relevant files.

- `what-context-needed`
- Use when you are not sure what files the agent should read first.

- `commit-message-storyteller`
- Use to draft commit messages that explain why.

- `markdown-to-html`
- Use only when you explicitly need markdown-to-html conversion work.

## Agents (Use When Needed)

- `markdown-accessibility-assistant.agent.md`
- For deep markdown accessibility cleanup.

- `prompt-builder.agent.md`
- For creating/refining prompt files and instruction quality.

## Low-Energy Fallback

If you feel foggy, use this order:

1. Run `what-should-i-use.prompt.md` with one sentence about the task.
2. Run the single recommended prompt.
3. If needed, run one follow-up check prompt.

## Decision Rule

When two prompts seem similar, pick the narrower one.

Example:

- Need only front matter fixes: use `front-matter-check.prompt.md`.
- Need broad cleanup: use `cleanup-site-page.prompt.md`.
