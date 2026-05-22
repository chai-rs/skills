# Attribution

This repository curates skills and subagents from several upstream sources.
Each item below was imported at HEAD of the upstream `main` branch on
2026-05-22. Refer to the upstream repo for the canonical version, license,
and ongoing maintenance.

## Sources

| Skill / agent (here) | Upstream repo | Upstream path |
|---|---|---|
| skills/caveman, diagnose, edit-article, git-guardrails-claude-code, grill-me, grill-with-docs, handoff, improve-codebase-architecture, migrate-to-shoehorn, obsidian-vault, prototype, review, scaffold-exercises, setup-matt-pocock-skills, setup-pre-commit, tdd, to-issues, to-prd, triage, write-a-skill, writing-beats, writing-fragments, writing-shape, zoom-out | [mattpocock/skills](https://github.com/mattpocock/skills) | `skills/{engineering,productivity,misc,personal,in-progress}/<name>/` |
| skills/karpathy-guidelines | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | `skills/karpathy-guidelines/` |
| skills/impeccable, agents/impeccable-asset-producer.md | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | `.claude/skills/impeccable/`, `skill/agents/impeccable-asset-producer.md` |
| skills/golang-* (42 skills) | [samber/cc-skills-golang](https://github.com/samber/cc-skills-golang) | `skills/golang-*/` |
| skills/coding-guidelines, core-*, domain-*, m01..m15, meta-cognition-parallel, rust-*, unsafe-checker (38 skills) | [actionbook/rust-skills](https://github.com/actionbook/rust-skills) | `skills/<name>/` |
| skills/debug-mantra, post-mortem, scrutinize, management-talk | [thananon/9arm-skills](https://github.com/thananon/9arm-skills) | `skills/{engineering,productivity}/<name>/` |

## Originals authored in this repo

- `commands/plan-todo.md`
- `commands/plan-update.md`
- `commands/plan-implement.md`
- `commands/research-codebase.md`

## Refreshing from upstream

To pull the latest version of any skill, re-clone the upstream repo and
copy the relevant folder. There is no automatic sync — this is a snapshot
curated by hand.

## Licensing

Each upstream repository has its own LICENSE file. By including their work
here, this repository is bound by the terms of each respective upstream
license. If you redistribute or modify any included skill, consult the
upstream LICENSE first.
