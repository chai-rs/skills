# Overrides: SCALER > UNIVERSAL

Where scaler's house rules deliberately diverge from kien-thai's universal Thai guidance. On
any collision, the scaler rule wins. Most "conflicts" are register mismatches — scaler maps to
kien-thai's R1 *Explainer* register, so kien-thai's personal-blog (R3) allowances simply don't
apply here.

| seam | kien-thai (universal) | scaler (this skill) |
|---|---|---|
| ไม้ยมก spacing | `ต่าง ๆ` always spaced | NEVER a space before ๆ, incl. `ต่างๆ` — `rule-08-yamok`. Verified against real lessons (already `ต่างๆ`, no space) |
| sentence-final period | R3 allows a fragment-snap `.` | no `.` closing a Thai clause — `rule-07-period` |
| first person | R3 requires ผม/ดิฉัน | คุณ/เรา only; ban ผม/ดิฉัน/แอด (`register.md` `pronouns`) |
| 555 / slang | R3 allows 555 ×1/post | hard-ban (`forbidden-phrases.md`, error) |
| ครับ/ค่ะ in body | R1 Explainer = zero | sparing allowed (`register.md` `particle-frequency`); NOT a lint check — politeness is not an AI-tell |
| recap close | bans summaries outright | `## Key Takeaways` prescribed (`mdx-lessons.md`); only the relist form + โดยสรุปแล้ว phrasings banned |
| ซึ่ง / โดย connectives | caps their use | `rule-06-emdash` recommends them as em-dash replacements; kien-thai's budget kept as a warn-tier complement, not an override |

## Provenance

Universal Thai-prose rules, the forbidden-phrases blocklist, the rule-header schema, and the
pytest patterns are adapted from [chakrit/kien-thai](https://github.com/chakrit/kien-thai)
(MIT © 2026 Chakrit Wichian). This skill is private/internal to scaler-client and not
distributed. Governing principle borrowed from kien-thai: rules without provenance rot — don't
grow the skill faster than the evidence, and default-suspect the English-trained reflex to cut
load-bearing Thai particles (`จะ`, `ให้`, politeness).
