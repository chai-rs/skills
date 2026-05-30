# thai-content

A private Claude skill for writing and auditing Thai system-design lesson content
(`*.th.mdx`) for scaler-client, in the house voice: รุ่นพี่ที่เคยผ่านมาแล้ว เล่าให้ฟังตรง.

## Layout

- `SKILL.md` — spine: fixed register, native-Thai frames, three task flows, routing
- `references/` — canonical rules (migrated from CONTENT-GUIDE.md, merged with kien-thai)
- `scripts/lint_thai_content.py` — deterministic linter (stdlib, MDX-aware, two tiers)
- `tests/` — pytest: frontmatter guard, slug consistency, linter golden fixtures

## Run

```sh
# from the skill dir
uv run pytest -q
uv run python scripts/lint_thai_content.py "../../../content/modules/**/*.th.mdx"
```

The skill is a self-contained uv project; its `.venv`/`uv.lock` live under the git-excluded
`.claude/`. Runtime deps: none (linter is stdlib). Dev deps: pytest, pyyaml.

## Governance

- **politeness is NOT an AI-tell.** ครับ/ค่ะ and load-bearing particles (`จะ`, `ให้`) are baseline
  Thai. The linter never flags them; only `register.md` adjudicates cadence. Default-suspect the
  English-trained reflex to cut them.
- **rules without provenance rot.** Don't grow the skill faster than the evidence. A new rule
  needs a real example that motivated it.
- The linter owns mechanical rules (two tiers: `error` auto-fixable, `warn` adjudicated). The
  agent owns judgment rules by reading `references/`.

## Attribution

The universal Thai-prose layer — the forbidden-phrases blocklist, word-level grammar rules, the
rule-header schema, and the pytest patterns — is adapted from
[chakrit/kien-thai](https://github.com/chakrit/kien-thai), MIT © 2026 Chakrit Wichian. This skill
is private and not distributed.
