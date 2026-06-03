# Style rules

Positive style rules. Apply these when drafting.

This file is the union of two sources: the universal Thai-prose base (kien-thai,
all-registers, MIT) and the scaler-domain specialization (thai-content,
scaler-explainer register, migrated from CONTENT-GUIDE §2/§3/§6/§10/§11). It
covers the native-Thai frames, sentence shape and rhythm, the discourse-marker
vocabulary, em-dash discipline, opening techniques, verbs/nouns, openers and
closings, concreteness, voice, ทับศัพท์ judgment, translation craft, and structure.

Rule headers carry a tag: `*(... · all-registers · ...)*` marks a universal rule
that applies in every register; `*(... · scaler-explainer · ...)*` marks a rule
specialized to the scaler peer-explainer register. Where the universal and scaler
guidance collide, do **not** resolve it here — `overrides.md` is the authority
(SCALER > UNIVERSAL); both sides are preserved with their tags. Any `rule-NN-*`
slug is emitted by `scripts/lint_thai_content.py` and must survive verbatim.

Inline-code Thai examples may exceed the 90-column rule when the example itself is
longer than that — they're treated as atomic, like URLs.

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

## Sentence shape and rhythm

### `mixed-sentence-length` *(style · all-registers · soft)*

A 6-word sentence next to a 35-word one is normal Thai prose. Test your draft:
if every sentence is ~20 words, break some.

Good rhythm — long body, then a short snap at the end (personal-blog register,
where fragment snaps with `.` are allowed):

> พอ traffic เข้ามาเยอะขึ้น cache layer ที่เคยพอก็เริ่มไม่พอ
> และตอนนั้นเองที่ปัญหา hot key เริ่มโผล่ ปวดหัวมาก.

In particle-free registers (explainer, news, marketing-body), drop the
fragment and end the paragraph at the natural snap (`...hot key เริ่มโผล่.`).

### `sentence-length` *(craft · scaler-explainer · soft)*

A Thai sentence should not run past ~2 lines. Split, or break with a newline instead of a
long comma chain.

### `connective-budget` *(style · all-registers · soft)*

In a 100-word paragraph: at most one ซึ่ง, one โดย, one ดังนั้น. Drop "however"
in roughly half its English occurrences. Test every connective: would a Thai
reader notice it missing? If no, delete. See `chueung-stacking`, `doi-sprawl`,
`yangrai-kotam-overuse`, `formal-connective-stack` for the audit-time bans on
each.

### `topic-comment-fronting` *(style · all-registers · soft)*

Thai prefers `topic → comment` over English's SVO. When the English would calque a passive ("X is done by Y"), front the patient as topic and use active voice.

- English: `The fact that the human brain grew larger created a problem during childbirth.`
- Calqued: `ความจริงที่ว่าสมองมนุษย์ใหญ่ขึ้นทำให้เกิดปัญหาในการคลอด`
- Crafted: `สมองที่ใหญ่ขึ้น คือต้นเหตุของปัญหาในการคลอด`

### `conceptual-seam-break` *(style · all-registers · soft)*

If your draft has more than ~25 Thai words without a break, look for a seam. Skilled translators routinely produce 2–3 Thai sentences from one English sentence.

### `topic-pronoun-drop` *(style · all-registers · soft)*

Drop pronominal subjects after the topic is established. Re-state only when
control changes. A paragraph beginning `เราเรียนรู้จากความผิดพลาด...` can run
several sentences before *เรา* needs to reappear. See Frame 5
(`f5/zero-anaphora`); audit catch `pronoun-spam`.

### `ko-pacing-particle` *(style · all-registers · soft)*

Use ก็ as a pacing particle, not a connective. `พอ traffic ขึ้น DB ก็เริ่มอืด`
— feels native. AI tends to drop ก็ entirely or use it wrong. See Frame 6
(`f6/ko-pacing`, `f6/ko-resumptive`).

### `mai-yamok-reduplication` *(style · all-registers · soft)*

Use ๆ (mai-yamok) for casual reduplication. `เรื่อย ๆ`, `ใหม่ ๆ`, `บ่อย ๆ` — natural Thai signal.

**ไม้ยมก spacing** (canonical rule: `mai-yamok-spacing` in `grammar.md`; scaler override
`rule-08-yamok`; `overrides.md` is authority). Two rules for the space before ๆ (vetted
2026-05-13, see
[`notes/chrome-session-2026-05-13.md`](../../../notes/chrome-session-2026-05-13.md) §3):

1. **`ต่าง ๆ` always takes the space.** Near-universal across edited
   Thai — government, tech-blog, even amateur personal-blog tend to
   space this one as a stock phrase. If audit ever sees `ต่างๆ`, flag it.
2. **Other reduplications follow register.** Personal blog / marketing-
   warm / casual-explainer / dev-blog: drop the space (`สั้นๆ`,
   `ง่ายๆ`, `อะไรๆ`, `เด็กๆ`, `เตี้ยๆ`). Government / academic /
   formal-explainer / institutional: keep the space (`สั้น ๆ`,
   `ง่าย ๆ`). Tech-news (Register-4 Blognone-style) is mixed within
   publication — pick one and stay consistent within a piece.

Evidence: Pantip Blueplanet (settembre) and GotoKnow plain-diary
(Vicharn Panich) drop the space on non-`ต่าง ๆ` reduplications
(7/7 samples). Bank of Thailand keeps the space (2/2). Blognone
homepage mixes within publication (4 no-space casual + 6 spaced
`ต่าง ๆ` instances). Small-N (~20 samples); phrase as default,
not hard check.

Scaler note: scaler-explainer register writes `จริงๆ` attached
(see `rule-08-yamok`), never `จริง ๆ`.

### `baeb-hedger` *(style · scoped · soft)*

Use แบบ as a hedger / approximator. `แบบว่า`, `แบบเร็ว ๆ`, `แบบที่เคยทำ` — natural in dev/casual register; rare in AI output. Scope: dev/casual register.

## Mechanics

### `rule-06-emdash` *(mechanical · scaler-explainer · soft)*

em-dash (`—`) is allowed but ≤1 per paragraph is the target; LLM prose pivots on `—`
every sentence. Prefer Thai connectives (`คือ`, `ซึ่ง`, `โดย`, `เพราะฉะนั้น`, `อย่างเช่น`).

- **Overused**: `ทีมเล็ก — ใช้ monolith ก็พอ — ไม่ต้อง over-engineer`
- **Better**: `ทีมเล็กใช้ monolith ก็พอ ไม่ต้อง over-engineer`

Linter flags >2 per paragraph (warn). Connective budget: ≤1 `ซึ่ง` per sentence, ≤1 `โดย`
per paragraph — kien-thai's cap, complements (does not override) §6's recommendation to use them.

## Verbs and nouns

### `verb-over-nominal` *(style · all-registers · soft)*

Verbs over noun forms when an action is the point. Prefer `แปลหนังสือ` to
`ทำการแปลหนังสือ` to `การทำการแปลหนังสือ`. Reserve การ-/ความ- for genuinely
abstract topics or for headings. Audit catches: `tham-kan-padding`,
`kan-nominalization`.

### `verbs-over-nouns` *(craft · scaler-explainer · soft)*

Prefer verbs to nominalizations. `ทำการ deploy` → `deploy`; `มีการเพิ่มขึ้นของ load` → `load เพิ่มขึ้น`.

### `bare-adjective` *(style · all-registers · soft)*

Adjectives directly, not มีความ + adjective. `โค้ดนี้ซับซ้อน` not
`โค้ดนี้มีความซับซ้อน`. Audit catch: `mi-khwam-padding`.

### `active-voice-default` *(style · all-registers · soft)*

Active voice unless the patient is genuinely the topic. Only use ถูก- when the
action is genuinely adversative (ถูกวิจารณ์, ถูกแฮก, ถูกปฏิเสธ) or when no
agent is recoverable. Audit catch: `non-adversative-thuk`.

### `no-bureaucratic-thai` *(craft · scaler-explainer · hard)*

No ราชการ/academic stiffness. `กระบวนการออกแบบและวางโครงสร้างของระบบซอฟต์แวร์ขนาดใหญ่` →
`การออกแบบระบบที่ต้องรองรับคนเยอะ`. Cut `ได้อย่างมีประสิทธิภาพ` or replace with `ให้ทำงานได้ดี`.

## Openers and closings

### `concrete-opener` *(style · all-registers · soft)*

Open with one of: a fact, a confession, a symptom the reader recognizes, a
rhetorical question, a concrete number. Never a panorama (`ในยุคปัจจุบัน...`).
Audit catches: `panorama-opener`, `assert-consensus-opener`.

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

### `inline-def-parenthetical` *(style · all-registers · soft)*

Inline parenthetical for definitions, not footnotes. `Kubernetes (หรือเรียกสั้น ๆ ว่า K8s)` — common pattern.

### `question-heading` *(style · all-registers · soft)*

Question-headings when the body answers them, declarative when the body elaborates. Avoid noun-phrase-only headings for explainers.

- Good: `รวบหนี้…ช่วยให้การเงินดีขึ้นได้อย่างไร?` / `แล้วทำไมถึงต้องเปลี่ยน?` /
  `เคสที่ pricing พัง`

### `no-recap-close` *(style · all-registers · soft)*

Close without recap. Real Thai writing ends with: a forward-looking line, a
reframed question, a quiet handoff (`เท่านี้ก่อน`, `ลองเอาไปเล่นดู`), or just
stops. `โดยสรุป` is grammatically fine but reads lower-quality in modern Thai.

- **Bad**: `โดยสรุปแล้ว Kubernetes เป็นเครื่องมือที่มีประโยชน์อย่างยิ่งในการ...`
- **Good (war-story)**: `เท่านี้ก่อนนะครับ ใครเคยเจอเคสแปลก ๆ มาคุยกันได้`
- **Good (explainer)**: `เพื่อให้คุณมีชีวิตทางการเงินที่ดีขึ้น`
- **Good (synthesis)**: reframe the original question — don't summarize.

### `advisory-close` *(style · all-registers · soft)*

Advisory closings beat imperative CTAs. Use `ควร` + responsibility framing (`กู้เท่าที่จำเป็นและชำระคืนไหว`) over `รีบสมัครเลย!`.

## Concreteness

### `numeric-anchor` *(style · all-registers · soft)*

Numbers and named examples carry the prose. `p99 ลดจาก 800ms เหลือ ~120ms`, `งบ 4 ส่วน: ใช้/ลงทุน/ออม/ฉุกเฉิน`, `50 pods` — anchor abstract claims.

### `uneven-list` *(style · all-registers · soft)*

Uneven, specific lists beat symmetric tricolons. Replace `รวดเร็ว ปลอดภัย และมีประสิทธิภาพ` with `เร็วขึ้นชัด ๆ จาก 800ms เหลือ ~120ms และ memory ไม่บวมเหมือนเดิม`.

### `ying-proportional` *(style · all-registers · soft)*

`ยิ่ง X เท่าไหร่ ยิ่ง Y เท่านั้น` for proportional claims — Thai-native intensification, replaces empty `อย่างมาก`.

### `nee-khue-pivot` *(style · all-registers · soft)*

`นี่คือเหตุผลที่...` as a clean pivot from problem to concept. Beats `ดังนั้นในวันนี้เราจะมาแนะนำ...`.

## Voice and personality

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

### `phom-default` *(style · scoped · soft)*

First-person ผม is the default for personal tech writing; เรา for team/collective. Drop both only in pure reference docs and news register. Scope: personal tech writing and team/collective contexts.

### `parenthetical-aside` *(style · all-registers · soft)*

Conversational asides in parentheses or dashes. `(เพื่อความง่ายขอใช้เป็น 80M)`, `(ใครเคยเจอแบบนี้บ้าง)`. Signals human authorship strongly.

### `rhetorical-question` *(style · all-registers · soft)*

Rhetorical questions to advance arguments. `แล้วถ้าโหลดเพิ่มอีกสิบเท่าล่ะ?` is a normal Thai connective, not a gimmick.

### `haha-particle` *(style · scoped · soft)*

Allow `555` or `5555+` once per long post in personal blog register. Forbidden in news register and most explainer/tech-doc contexts. Scope: personal blog only.

### `voice-over-politeness` *(style · all-registers · soft)*

Author voice over Thai politeness defaults. Don't add ครับ/ค่ะ to confident essayists when translating. Don't pad with อาจจะ when the source asserts.

## ทับศัพท์ — four-bucket judgment guide

Every foreign term goes into one of four buckets. Pick once per term per document,
commit.

### Bucket 1 — translate to Thai

When a settled Thai equivalent exists and is recognizable.

- *justice* → ความยุติธรรม
- *freedom* → เสรีภาพ
- *cooperation* → ความร่วมมือ
- *capitalism* → ทุนนิยม
- *productivity* → ผลิตภาพ

### Bucket 2 — transliterate (Thai script)

For proper nouns, neologisms with no clean Thai equivalent, or technical terms whose
English form would jar in running prose.

- *algorithm* → อัลกอริทึม
- *blockchain* → บล็อกเชน
- เซิร์ฟเวอร์, ซอฟต์แวร์, ดาต้า, แอป
- Common transliterated brands: เฟซบุ๊ก, กูเกิล (less common in modern body text —
  Latin script wins)

### Bucket 3 — keep in Latin script

For:

- Brand names that are visual identities: Facebook, Google, Apple
- Industry-specific acronyms: GDP, CEO, AI, API, DCA, IPO
- Technical terms developers use in English: deploy, scale, container, payload,
  latency, throughput, query, index, cluster, pipeline
- Famous titles cited as titles: *The Wealth of Nations*
- Terms whose discussion centers on the term itself
  (`คำว่า meritocracy แปลตรงตัวได้ลำบาก`)

### Bucket 4 — coin-and-gloss

For important author concepts that recur.

- First mention: Thai coinage + (English in parentheses + brief gloss).
- Example: `ระเบียบในจินตนาการ (imagined order — ระเบียบที่คนเชื่อร่วมกันว่ามีอยู่จริง)`
- Subsequent mentions: Thai only.

### Heuristics

- Term appears > 5 times and is the author's coinage → Bucket 4.
- Term has a Royal Institute–approved Thai compound → Bucket 1.
- Term is < 3 syllables and visually punchy in Latin (CEO, AI) → Bucket 3.
- Term is a place / person / brand → Bucket 2 on first appearance with Latin in parens;
  Bucket 3 only if the brand is visually distinctive.
- **Never mix buckets for the same term within a document.**

### `code-mix-noun-binding` *(style · all-registers · soft)*

Code-mix at the noun, not the verb. `deploy โค้ด`, `scale ระบบ`, `query ตาราง` — verb
in English, object in Thai is fine. Reverse (`ทำการ deployment ของ code`) reads
bureaucratic.

## Translation craft (English → Thai)

### `italics-via-particle` *(style · all-registers · soft)*

Render English emphatic italics with word-order or particles, not with bold/italic Thai. Thai typography rarely italicizes for emphasis. Use:

- Final particle: `...แน่นอน`, `...ก็จริง`
- Foregrounding: putting the emphasized item in topic slot
- Lexical replacement: `แท้จริง`, `จริง ๆ`, `เสียด้วยซ้ำ`

### `idiom-localize` *(style · all-registers · soft)*

Localize idioms; preserve metaphors. "It's raining cats and dogs" → `ฝนตกหนักมาก` (meaning, not idiom). But authorial extended metaphors get a calque-coined term, kept consistent throughout. For bare-verb calques (e.g. "burst" → ระเบิด, "drop" → ทิ้ง, "cap" → ปิดฝา), see `verb-calque` in grammar.md — Thai often uses a different verb for the same action.

### `date-trailing` *(style · all-registers · soft)*

Numeric placement. English: `in 2019 the law was passed.` In Thai narrative, dates often trail: `กฎหมายฉบับนี้ประกาศใช้เมื่อปี 2019`.

### `foreign-name-format` *(style · all-registers · soft)*

Foreign names. First mention: Thai transliteration + parenthesized original — `ไมเคิล แซนเดล (Michael Sandel)`. Subsequent: Thai only. Famous-enough names skip the parenthetical (`แฮรารี`).

### `term-establish-once` *(style · all-registers · soft)*

Don't translate the same technical term twice in the same paragraph. First mention establishes the Thai/transliterated form; later mentions don't gloss again.

### `source-fidelity` *(style · all-registers · soft)*

Don't add anything the source doesn't have. No added ครับ/ค่ะ on confident essayists. No hedging อาจจะ where the source asserts. If the source omits a transition, omit it. Fidelity to voice, not tour-guiding.

### `heading-noun-only` *(style · all-registers · soft)*

Headings: shorter than the English, often noun-only.

- English: `How Imagined Orders Shape Cooperation`
- Thai: `ระเบียบในจินตนาการกับความร่วมมือ`
- Not: `วิธีที่ระเบียบในจินตนาการหล่อหลอมความร่วมมือ`

Thai chapter titles favor noun-noun juxtaposition with `กับ` / `และ` / colon.

## Structure

### `prose-before-bullets` *(style · all-registers · soft)*

Commit to prose paragraphs of 2–4 sentences before bulleting. Bullets earn their place when items are parallel-shaped or the list is 4+.

### `numbered-section-heading` *(style · all-registers · soft)*

Numbered sections (1. / 2. / 3.) are fine and common in bank explainers. Pair each with a short heading; don't bullet inside without prose context.

### `disclaimer-as-voice` *(style · scoped · soft)*

Disclaimers absorbed into voice, not bolted on. ttb's `กู้เท่าที่จำเป็น` reads as ethics, not ad. Krungsri's `ทั้งนี้ ผู้ลงทุนควร...` is one sentence, then the piece ends. Scope: bank/finance and regulated-content registers.
