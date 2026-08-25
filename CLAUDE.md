@AGENTS.md

## Claude Code Integration

`skills/deeppapernote/SKILL.md` is both the canonical workflow definition and the Claude Code skill entrypoint.
`.claude-plugin/plugin.json` identifies the plugin, but it must not restate the workflow.

- Do not fork or restate the DeepPaperNote workflow in any Claude-only file.
- All workflow logic stays in `skills/deeppapernote/SKILL.md`.

### Skill Invocation

End users running Claude Code invoke the skill with natural language or the
`/deeppapernote` slash command. Recognized trigger examples:
- `Generate a deep-reading note for this paper`
- `Write a high-quality paper reading note`
- `Organize this article into an Obsidian note`
- `/deeppapernote <paper title, DOI, arXiv ID, or local PDF path>`
