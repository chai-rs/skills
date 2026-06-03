# thai-prose

A private Claude skill for writing, editing, translating, and auditing **Thai-language
prose** — and, as a specialized path, scaler-client's system-design lesson content
(`*.th.mdx`) in the house voice: รุ่นพี่ที่เคยผ่านมาแล้ว เล่าให้ฟังตรง.

It is the union of two earlier skills:

- **kien-thai** — universal Thai prose across all register families (news, explainer,
  marketing, blog, academic, official), countering AI's over-formal/calqued Thai.
- **thai-content** — the scaler lesson layer: fixed peer-explainer register, MDX lesson
  structure, and a deterministic linter for `.th.mdx`.

## How it routes

`SKILL.md` is the spine. A top-level router picks the path by task:

- **`.th.mdx` lesson under `content/modules`** → fixed *scaler peer-explainer* register,
  lesson structure (`references/mdx-lessons.md`), and the linter. No register-selection step.
- **Any other Thai prose** → universal flow: pick one of the register families
  (`references/register.md`), set person deixis and voice, draft frame-first. The linter
  does not apply.

`references/overrides.md` is the authority when the scaler layer and the universal layer
collide (SCALER > UNIVERSAL, for lesson content).

## Layout

- `SKILL.md` — spine: superset trigger, router, 7 native-Thai frames, person deixis, workflows
- `references/` — canonical rules (universal layer + scaler domain layer)
- `scripts/lint_thai_content.py` — deterministic linter (stdlib, MDX-aware, two tiers)
- `tests/` — pytest: frontmatter guard, slug consistency, linter golden fixtures

## Run

```sh
# from the skill dir
uv run pytest -q
uv run python scripts/lint_thai_content.py "../../../content/modules/**/*.th.mdx"
```

The skill is a self-contained uv project; its `.venv`/`uv.lock` live under the
git-excluded `.claude/`. Runtime deps: none (linter is stdlib). Dev deps: pytest, pyyaml.

## Governance

- **politeness is NOT an AI-tell.** ครับ/ค่ะ and load-bearing particles (`จะ`, `ให้`) are
  baseline Thai. The linter never flags them; only `register.md` adjudicates cadence.
  Default-suspect the English-trained reflex to cut them.
- **rules without provenance rot.** A new rule needs a real example that motivated it.
- The linter owns mechanical rules (two tiers: `error` auto-fixable, `warn` adjudicated).
  The agent owns judgment rules by reading `references/`.

## Attribution

The universal Thai-prose layer — the forbidden-phrases blocklist, word-level grammar
rules, the rule-header schema, and the pytest patterns — is adapted from
[chakrit/kien-thai](https://github.com/chakrit/kien-thai), MIT © 2026 Chakrit Wichian.
This skill is private and not distributed.
