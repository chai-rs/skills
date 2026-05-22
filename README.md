# vibe-skills

Personal collection of Claude Code skills, slash commands, and subagents.
The repo doubles as a **Claude Code plugin marketplace** and as an
**openskills**-compatible skills source.

## Layout

```
vibe-skills/
├── .claude-plugin/
│   ├── plugin.json          # plugin manifest (repo is the plugin)
│   └── marketplace.json     # marketplace listing this one plugin
├── skills/                  # SKILL.md files, one folder per skill
│   └── hello-vibe/SKILL.md
├── commands/                # /<name> slash commands
│   └── vibe-status.md
└── agents/                  # custom subagents
    └── vibe-reviewer.md
```

## Install — Claude Code (official)

```sh
/plugin marketplace add chai-rs/skills
/plugin install vibe-skills@vibe-skills
```

After install, skills/commands/agents become available under the plugin
namespace.

## Install — openskills (community, universal)

```sh
npx openskills install gh:chai-rs/skills
```

openskills will discover every `skills/*/SKILL.md` at the repo root and
write them into `.claude/skills/` (or `.agent/skills/`, depending on
your config). Skills installed this way also work in Cursor, Codex CLI,
Aider, and any agent that reads `AGENTS.md`.

## Add a new skill

1. Create `skills/<your-skill>/SKILL.md` with YAML frontmatter:
   ```yaml
   ---
   name: your-skill
   description: One sentence on when Claude should use this skill.
   ---
   ```
2. Body is plain markdown — instructions, examples, references.
3. Optional frontmatter fields: `allowed-tools`, `disable-model-invocation`,
   `user-invocable`, `model`, `arguments`, `argument-hint`, `paths`.
   See [Claude Code skills docs](https://code.claude.com/docs/en/skills).

## Add a new slash command

Drop a markdown file in `commands/<name>.md`. The filename becomes the
slash command. Use `$ARGUMENTS` to capture user input.

## Add a new subagent

Drop a markdown file in `agents/<name>.md` with frontmatter:

```yaml
---
name: your-agent
description: When the agent should be invoked.
tools: Read, Grep, Bash
---
```

The body is the system prompt for that subagent.

## Local development

Iterate without publishing by running Claude Code from inside this repo
with `--plugin-dir`:

```sh
claude --plugin-dir /Users/0xanonydxck/dev/vibe-skills
```
