# Surface Thai grammar

Word- and character-level Thai rules. Hard rules, this register. The first two are
mechanical and linter-enforced; the rest are judgment rules ported from kien-thai (MIT)
that the guide had no equivalent for.

### `rule-07-period` *(mechanical · scaler-explainer · hard)*

Thai clauses do not close with a full stop. Sentence boundaries are carried by spaces
and paragraph breaks. A `.` after a Thai word reads like an AI translation.

- **Bad**: `ทีมเล็กใช้ monolith ก็พอ. ไม่ต้อง over-engineer.`
- **Good**: `ทีมเล็กใช้ monolith ก็พอ ไม่ต้อง over-engineer`

Exceptions (the linter masks these): decimals (`2.5 วินาที`), `99.9%`, URLs/domains
(`api.eddict.io`), code (`service.method()`), abbreviations (`etc.`), and lines that are
pure English. Linter: `rule-07-period` (error).

### `rule-08-yamok` *(mechanical · scaler-explainer · hard)*

ไม้ยมก (`ๆ`) attaches to the repeated word — never a space before it.

- **Bad**: `ทำซ้ำ ๆ หลาย ๆ ครั้ง` · `service ใหม่ ๆ`
- **Good**: `ทำซ้ำๆ หลายๆ ครั้ง` · `service ใหม่ๆ`

This is a deliberate scaler override of kien-thai's universal `mai-yamok-spacing` (which
keeps `ต่าง ๆ` spaced). See `overrides.md`. Linter: `rule-08-yamok` (error).

### `wrong-classifier` *(judgment · scaler-explainer · hard)*

Each Thai noun takes an established classifier; AI defaults to `ใบ` or drops it. Common
technical-noun classifiers:

- `เครื่อง` — server, machine, node, instance (hardware sense)
- `ตัว` — variable, function, service, parameter, instance (logical sense)
- `อัน` — generic small/abstract object (token, item, record)
- `ถัง` — bucket, queue tank
- `รายการ` — list item, transaction, entry
- `บรรทัด` — line of code/text

- **Bad**: `server หนึ่งใบ` · `เพิ่ม read replica อีกหนึ่งใบ`
- **Good**: `server หนึ่งเครื่อง` · `เพิ่ม read replica อีกหนึ่งเครื่อง`

If unsure, omit the count (`เพิ่ม replica`) rather than pick a wrong classifier.

### `missing-cha-modal` *(judgment · scaler-explainer · hard)*

Thai marks future/hypothetical/modal clauses with `จะ`. AI omits it when the English source
has no explicit future marker, leaving a clause that reads as bare description.

- **Bad**: `วิธีนี้คุม average rate ได้`
- **Good**: `วิธีนี้จะคุม average rate ได้`

### `verb-calque` *(judgment · scaler-explainer · hard)*

Translating an English verb literally where Thai uses a different verb. Watch idiomatic-physical
verbs (burst, drop, spin up, throttle).

- **Bad**: `ถ้า queue เต็มก็ทิ้ง` (calque of "drop")
- **Good**: `ถ้า queue เต็มก็โดน reject`

### `capability-modal` *(judgment · scaler-explainer · soft)*

"can / is able to" is the frame `สามารถ + V + ได้`. In this register `V + ได้` alone is fine;
reach for the full frame only for emphasis.

- **Acceptable**: `ระบบ query ได้ผ่าน API`
- **Emphatic**: `ระบบสามารถ query ได้ผ่าน API`

### `time-period` *(judgment · scaler-explainer · hard)*

For time periods (eras, decades) Thai uses `ใน` (during), not `ของ` (possession).

- **Bad**: `ระบบที่ใหญ่ที่สุดของยุค cloud`
- **Good**: `ระบบที่ใหญ่ที่สุดในยุค cloud`
