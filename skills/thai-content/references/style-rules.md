# Style rules

Positive style for scaler lessons: the native-Thai frames, sentence shape, em-dash
discipline, the discourse-marker vocabulary, and opening techniques. Migrated from
CONTENT-GUIDE §2/§3/§6/§10/§11 and merged with kien-thai's frames (MIT).

## The seven frames (structural)

Walk these before picking words. English → Calqued → Native:

- **f1 topic-comment.** `The system processes this data every 5 minutes.` → calqued
  `ระบบประมวลผลข้อมูลพวกนี้ทุกๆ 5 นาที` → native `ข้อมูลพวกนี้ ระบบจะ process ทุก 5 นาที`
- **f2 condition/time first.** `The DB times out when traffic spikes.` → native
  `พอ traffic พุ่งสูง DB ก็เริ่ม timeout`
- **f3 space not period.** see `rule-07-period`.
- **f4 closure particles** (`ด้วย`, `แล้ว`, `ต่างหาก`). `ไม่ได้มีแค่กฎ มี linter ด้วย`.
- **f5 zero-anaphora + demonstratives**, not `มัน`/`พวกเขา` at every verb head.
- **f6 pacing via `ก็`.** `พอ traffic ขึ้น DB ก็เริ่มอืด`.
- **f7 pivots via question or `แต่`**, not `อย่างไรก็ตาม`.

### `rule-06-emdash` *(mechanical · scaler-explainer · soft)*

em-dash (`—`) is allowed but ≤1 per paragraph is the target; LLM prose pivots on `—`
every sentence. Prefer Thai connectives (`คือ`, `ซึ่ง`, `โดย`, `เพราะฉะนั้น`, `อย่างเช่น`).

- **Overused**: `ทีมเล็ก — ใช้ monolith ก็พอ — ไม่ต้อง over-engineer`
- **Better**: `ทีมเล็กใช้ monolith ก็พอ ไม่ต้อง over-engineer`

Linter flags >2 per paragraph (warn). Connective budget: ≤1 `ซึ่ง` per sentence, ≤1 `โดย`
per paragraph — kien-thai's cap, complements (does not override) §6's recommendation to use them.

### `sentence-length` *(craft · scaler-explainer · soft)*

A Thai sentence should not run past ~2 lines. Split, or break with a newline instead of a
long comma chain.

### `no-bureaucratic-thai` *(craft · scaler-explainer · hard)*

No ราชการ/academic stiffness. `กระบวนการออกแบบและวางโครงสร้างของระบบซอฟต์แวร์ขนาดใหญ่` →
`การออกแบบระบบที่ต้องรองรับคนเยอะ`. Cut `ได้อย่างมีประสิทธิภาพ` or replace with `ให้ทำงานได้ดี`.

### `verbs-over-nouns` *(craft · scaler-explainer · soft)*

Prefer verbs to nominalizations. `ทำการ deploy` → `deploy`; `มีการเพิ่มขึ้นของ load` → `load เพิ่มขึ้น`.

### `discourse-markers` *(craft · scaler-explainer · stylistic)*

Sprinkle natural Thai connective particles so prose reads spoken, not flat-translated.
1–2 per paragraph; overuse drifts to blog-กวน tone (which the voice bans).

| use | markers |
|---|---|
| correct a misconception | `จริงๆ (แล้ว)`, `เอาจริงๆ`, `พูดตรงๆ` |
| "that's all it is" close | `นั่นเอง`, `นั่นแหละ`, `เท่านั้นเอง` |
| soften a definition | `ก็คือ`, `มันก็คือ` |
| invite the reader to picture it | `ลองนึกภาพ`, `ลองคิดดู` |
| check in (sparingly) | `ใช่ไหม`, `เห็นภาพไหม` |

Note: write `จริงๆ` attached (`rule-08-yamok`), never `จริง ๆ`.

### `stacked-question-open` *(craft · scaler-explainer · stylistic)*

Open from 2-3 questions the reader already has, then answer — instead of a definition.

> Caching คืออะไร? เก็บของไว้ใน memory? ทำให้เร็วขึ้น? หรือแค่ตัวแปร global ที่ดูดี?

### `english-definition-anchor` *(craft · scaler-explainer · stylistic)*

Define a technical term once in a short English line (a blockquote works), then unpack in Thai.
Source term stays English; understanding lands in Thai.

> "Idempotency: calling an operation multiple times has the same effect as calling it once."
>
> แปลเป็นภาษาคนคือ กดจ่ายเงินซ้ำ 3 ครั้งเพราะเน็ตค้าง เงินต้องตัดครั้งเดียว

### `personal-experience-frame` *(craft · scaler-explainer · stylistic)*

Open a perspective from real experience (`จากคนที่เคย deploy พังมาก่อน`) to earn the
รุ่นพี่-ผ่านมาแล้ว credibility — sparingly, not every lesson.
