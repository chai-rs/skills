---
name: thai-prose
description: "Write, edit, translate, or audit Thai-language prose so it reads like a real Thai writer — not generic over-formal, over-polite, calqued AI Thai. Covers BOTH general prose across every register (marketing, landing pages, docs, READMEs, blog posts, explainers, news, announcements, emails) AND scaler-client system-design lessons (.th.mdx) in the house voice (รุ่นพี่ที่เคยผ่านมาแล้ว เล่าให้ฟังตรง). TRIGGER when: user asks for any non-trivial Thai prose output (paragraph or longer); user asks to translate English into Thai; user asks to edit, rewrite, or review existing Thai prose; user asks to write, draft, translate, audit, or fix a Thai lesson or section under content/modules; user asks to check Thai MDX against the content rules; conversation is in Thai and the user asks for a prose deliverable. DO NOT TRIGGER for: single-word or single-phrase translations, button labels, code identifiers, short UI strings, code comments, English (.en.mdx) prose, or conversational Thai chat replies that aren't deliverable prose."
---

# thai-prose

## Why this skill exists

AI-produced Thai imports English's discourse mechanics whole-cloth and adds
politeness/connective padding by default. Native readers feel the friction — re-reading,
skimming, abandoning. Surface-level rules ("don't use ทั้งนี้") treat symptoms; the seven
frames below are the structural cause. Many granular rules in `references/ai-tells.md`
(mechanical), `references/grammar.md` (surface), and `references/craft.md` (taste) auto-resolve
once the frames are right.

This skill carries two layers. A **universal** layer handles Thai prose in any register. A
**scaler lesson** layer specializes the Explainer register into the fixed house voice for
`.th.mdx` content and backs it with a deterministic linter. `references/overrides.md` is the
authority where the two collide (SCALER > UNIVERSAL, for lesson content).

## Router — pick the path first

Before anything else, decide which path the task is on:

- **Path B — scaler lesson.** The task is to write / draft / translate / audit / fix a
  `.th.mdx` lesson or section under `content/modules`, or to check lesson MDX against the
  rules. → Skip register selection; use the fixed **scaler peer-explainer** register, the
  lesson structure in `references/mdx-lessons.md`, and the linter. Jump to **Path B** below.
- **Path A — general Thai prose.** Anything else: marketing copy, landing pages, docs,
  READMEs, blog posts, explainers, news, announcements, emails, translations. → Run the
  universal flow: select a register, set deixis and voice, draft frame-first. The linter does
  not apply. Jump to **Path A** below.

Both paths apply the seven frames and person deixis below.

## The seven native-Thai frames (apply on both paths)

### `f1` *(frame · all-registers · structural)*

**Frame 1 — Topic-comment over subject-verb-object.** English defaults to SVO. Thai often
fronts the topic (whatever the sentence is *about*) and then comments on it. When the English
source has a heavy subject ("the fact that X is..."), calquing it into Thai produces
`การที่...นั้น...` chains that no Thai reader produces unprompted.

- English (SVO): `The system processes this data every five minutes.`
- Calqued: `ระบบประมวลผลข้อมูลพวกนี้ทุก ๆ 5 นาที`
- Topicalized: `ข้อมูลพวกนี้ ระบบจะ process ทุก 5 นาที`

Heuristic: if the English subject is heavy, abstract, or really the patient of the verb,
front it as topic in Thai. Covers `non-adversative-thuk` (ถูก-passive) and
`garn-thi-tham-hai` (การที่...ทำให้).

### `f2` *(frame · all-registers · structural)*

**Frame 2 — Condition, time, and frame go first.** English puts conditions and time-frames
after the main clause: "X happens when Y" / "X if Y". Thai prefers the inverse: condition
first, main clause after.

- English: `The DB starts timing out when traffic spikes.`
- Calqued: `DB จะเริ่ม timeout เมื่อ traffic พุ่งสูง`
- Native: `พอ traffic พุ่งสูง DB ก็เริ่ม timeout`

Common openers for fronted conditions/times: `พอ...ก็...`, `ถ้า...จะ...`, `เมื่อ...`, `ตอน...`,
`หาก...`. Covers `tirai-frame-closure`, `frame-scoped-ko`, and `whenever-calque` — conditional
frames require paired closure/linker (see `grammar.md`, `ai-tells.md`).

### `f3` *(frame · all-registers · structural)*

**Frame 3 — Sentence boundaries via space and paragraph, not period.** English uses a period
after every sentence. Modern Thai web writing uses periods sparingly. Boundaries are carried
by spaces and paragraph breaks; periods are reserved for end-of-paragraph snap or genuinely
terminal statements.

- AI density: `ระบบทำงานเร็วขึ้น. ใช้ memory น้อยลง. ทีมพอใจมาก.`
- Native: `ระบบทำงานเร็วขึ้น ใช้ memory น้อยลง ทีมพอใจมาก`

Heuristic: drop mid-paragraph periods; let space carry the boundary. The Royal Institute's
*หลักเกณฑ์การเว้นวรรค* formalizes a two-tier space system (clause-internal vs sentence boundary);
treat it as visual rhythm — short single space within a clause, paragraph break at sentence
boundaries. Covers `mid-paragraph-period` (`ai-tells.md`) and, on Path B, the linter's
`rule-07-period`.

### `f4` *(frame · all-registers · structural)*

**Frame 4 — Closure via sentence-final particles.** Thai uses a small inventory to wrap
clauses cleanly: `ด้วย` (also/too), `แล้ว` (completion, transition), `ไป` (movement away/done),
`อยู่` (ongoing state), `เลย` (intensification or "right then"), `ก็แล้วกัน` (decision), `อยู่ดี`
(still / nonetheless), `ต่างหาก` (contrastive correction — "actually X, not Y").

Note on `แล้ว` variants (Olsson 2013 on Thai iamitive): bare `แล้ว` (`f4/laeo-completion`) marks
completion / "by now"; `X แล้ว ก็ Y` adds sequence + pacing (Frame 6); `เสร็จแล้ว`
(`f4/set-laeo-perfective`) is perfective-completion. When AI omits these, Thai sentences feel
dangling — like the writer trailed off.

- Dangling: `repo นี้ไม่ได้มากับกฎอย่างเดียว มี eval harness ผูกกับ claude และ codex`
- Closed: `repo นี้ไม่ได้มากับกฎอย่างเดียว มี eval harness ผูกกับ claude และ codex ด้วย`

**ด้วย additive closure** (`f4/duai-additive`): watch `ไม่ได้...อย่างเดียว`, `ไม่ใช่แค่...`,
`ไม่เพียงแต่...` — they almost always need a closure particle to finish the implicit "also Y".

**ต่างหาก closure** (`f4/targhak-closure`): contrastive-correction frames
(`ไม่ได้ X อยู่ที่/เป็น/คือ Y`) take `ต่างหาก`.

- Dangling: `ปัญหาส่วนใหญ่ไม่ได้อยู่ที่ยอดขาย อยู่ที่ต้นทุน`
- Closed: `ปัญหาส่วนใหญ่ไม่ได้อยู่ที่ยอดขาย อยู่ที่ต้นทุนต่างหาก`

Covers `dangling-additive-frame` and `seam-connective-missing`.

### `f5` *(frame · all-registers · structural)*

**Frame 5 — Cohesion via zero anaphora and demonstratives.** English needs explicit pronouns;
Thai has three strategies AI underuses:

1. **Zero anaphora** (`f5/zero-anaphora`) — once the topic is established, drop the subject;
   re-state only when control changes.
2. **Demonstratives over pronouns** — `นี่ / นั่น / โน่น`; reference the noun by demonstrative +
   classifier (`คนนี้`, `เคสนั้น`, `ปัญหานั้น`). AI overuses `มัน`, `เขา`, `พวกเขา` because they map to
   English `it / he / they`.
3. **Demonstrative as inter-clause bridge** (`f5/demo-bridge`) — `ตรงนี้แหละที่...`,
   `นี่คือเหตุผลที่...`, `ส่วนนี้...`. Especially valuable for problem→solution pivots (Frame 7).

   - Dangling: `ของค้างก็กลายเป็นต้นทุนเงียบ ระบบนี้ช่วย...`
   - Bridged: `ของค้างก็กลายเป็นต้นทุนเงียบ ตรงนี้แหละที่ระบบช่วยได้`

- Calqued: `bun ได้ปล่อย feature ต่าง ๆ ออกมามากมาย มันปรับปรุงเรื่องของ performance จากการ build มันลดการใช้งาน memory ในขณะ runtime และมันยังปรับปรุงแนวทางการทดสอบอีกด้วย`
- Native: `bun ได้ปล่อย feature ต่าง ๆ ออกมามากมาย ทั้งการปรับปรุงเรื่องของ performance จากการ build และลดการใช้งาน memory ในขณะ runtime รวมทั้งยังได้ปรับปรุงแนวทางการทดสอบอีกด้วย`

**Caveat — zero anaphora has limits.** Aggressive subject-drop creates subjectless robot-prose
when the referent isn't recoverable. If a clause starts with a connective (`เพราะ...`,
`ดังนั้น...`, `ส่วน...`) and immediately presents a verb without a topic, restore reference via a
demonstrative bridge or topic-comment restructure rather than reaching for `มัน` (banned by
`dummy-man`).

- Robot: `เพราะรับประกัน output rate`
- Native (bridge): `เพราะแบบนี้ output rate จะคงที่`
- Native (restored topic): `algorithm นี้รับประกัน output rate`

### `f6` *(frame · all-registers · structural)*

**Frame 6 — Pacing via ก็.** `ก็` marks expectation, sequence, mild concession, and
"as-expected" causation. English has no equivalent, so AI drops it, and Thai prose without ก็
reads choppy.

- Without ก็: `พอ traffic ขึ้น DB เริ่มอืด`
- With ก็: `พอ traffic ขึ้น DB ก็เริ่มอืด`

**ก็ as pacing particle** (`f6/ko-pacing`): `พอ X ก็ Y`, `X แล้ว ก็ Y`, `ถ้า X ก็ Y`, `เลย...ก็...`,
`X ไม่ทัน ก็เลย Y`. Standalone `แล้ว` also bridges sequenced clauses:

- Choppy: `ถ่ายรูปบิลจากตลาด ระบบอ่านรายการให้เอง`
- Bridged: `ถ่ายรูปบิลแล้วระบบจะอ่านรายการให้เอง`

**ก็ as topic-resumptive bridge** (`f6/ko-resumptive`; Takahashi 2023):

- Clipped: `ในรายการนี้ ไม่มีคอลัมนิสต์ดังคนไหน เป็นความตั้งใจ`
- Bridged: `ในรายการนี้ ไม่มีคอลัมนิสต์ดังคนไหน ก็เป็นความตั้งใจ`

Use ก็ as breath/rhythm, not as a connective replacement.

### `f7` *(frame · all-registers · structural)*

**Frame 7 — Pivots via question, demonstrative, or simple แต่.** Thai pivots via:

1. **Rhetorical question** (`f7/question-pivot`) — `แล้วถ้า X ล่ะ?`, `นั่นแปลว่ายังไง?`.
2. **Demonstrative bridge** (`f7/demo-pivot`) — `ตรงนี้แหละ...`, `นี่คือเหตุผลที่...`.
3. **Simple `แต่`** (`f7/tae-pivot`) — replaces `อย่างไรก็ตาม` in roughly half its occurrences.

- AI pivot: `อย่างไรก็ตาม การใช้งานในระดับ production มีข้อจำกัด`
- Native pivot: `แต่พอเอาขึ้น production จริง ก็มีอะไรให้ปวดหัวอีก`
- Question pivot: `แล้วถ้าโหลดเพิ่มอีกสิบเท่าล่ะ? ตรงนี้แหละที่เริ่มน่าสนใจ`

**Problem-list to solution pivot** (`f7/problem-solution-pivot`): after listing 2–3 pain-points,
insert a pivot before the solution instead of bullet-list cadence.

- Bullet-cadence: `ของหมดก็เสียยอดขาย ของค้างก็กลายเป็นต้นทุนเงียบ ระบบนี้ช่วย...`
- Pivoted (question): `ของหมดก็เสียยอดขาย ของค้างก็กลายเป็นต้นทุนเงียบ — แล้วทำไงให้คุมของได้แม่น?`

Heuristic: every "however" you'd write, ask whether a question or just `แต่` would do better.
Drop one in two.

## Person deixis (apply before drafting any piece with a reader)

Identify three roles before drafting: **1st** (speaker), **2nd** (addressee), **3rd** (product
/ concept / third party). Most critical for Marketing.

The single rule AI breaks most: **never substitute the audience's demographic noun**
(`เจ้าของร้าน`, `ผู้ใช้`, `นักลงทุน`, `ผู้ประกอบการ`) for `คุณ` in body copy. Demographic nouns frame
headers and categories; `คุณ` is the active 2nd-person referent.

- Bad: `เครื่องมือนี้ทำให้เจ้าของร้านเห็นภาพจริงของร้านตัวเอง`
- Good: `ระบบนี้ช่วยให้คุณเห็นภาพจริงของร้านได้ทันที`

Once a deixis frame is established for a stretch — including the **implicit-2nd-person** frame
where no pronoun is named — hold it (`deixis-continuity` in `register.md`). Don't slip an
indefinite-someone (`ใคร`, `คน`, `ใครๆ`) into an implicit-2nd-person passage; promote it to a
modifier (`โดยไม่รู้ตัว`) instead. Full per-register deixis defaults, brand mood / gender /
formality voice attributes, and the scaler `เรา`/`คุณ` pattern live in `references/register.md`.

## Stylistic conventions (apply on top of the frames)

Surface-level voice fine-tuning lives in `references/style-rules.md` (positive rules: sentence
shape, verbs over nouns, openers/closings, concreteness, voice, ทับศัพท์, translation craft),
`references/craft.md` (soft taste rules), and `references/code-switching.md` (Thai/English
ทับศัพท์ four-bucket — most relevant on Path B but applies anywhere English terms appear).

## Editing discipline — scope every fix to its full unit (apply on both paths)

Every fix is wrong until it is consistent with everything around it. A token-level edit that
ignores its context produces two recurring failures — both are defects, not acceptable
partial work:

1. **Sentence-level coherence (`edit-sentence-coherence`).** After changing any token, **re-read
   the entire sentence end to end** and confirm the edit agrees with what precedes and follows
   it: subject/topic, verb, classifier, connective, particle, and closure. Fixing a fragment in
   isolation often leaves a dangling subject, a doubled connective, a particle that no longer
   matches the new clause, or a verb that no longer agrees with its restored topic. The unit you
   must leave coherent is the **whole sentence**, not the span you touched.

   - Half-fixed: `เพราะ RPS มาจากพฤติกรรมของ user มันเลยคาดเดายาก` — restored the topic in clause 1
     but left `มัน` in clause 2 of the same sentence.
   - Coherent: `เพราะ RPS มาจากพฤติกรรมของ user เลยคาดเดายาก`

2. **Sibling propagation (`edit-sibling-consistency`).** When the pattern you fixed recurs in
   **parallel siblings**, fix **all of them or none** — never leave a half-fixed list. Siblings
   include: items in the same bullet/numbered list, rows or columns of the same table,
   coordinated clauses joined by `และ / หรือ / แต่`, repeated sub-headings of the same shape, and
   the recurring stem of a `X คือ ...` / `ใช้ X เมื่อ ...` parallel series. Before moving on,
   scan the whole enclosing block (the full `<list>`, the full table, the full coordinated
   sentence) for the same construct and apply the identical fix so the series stays parallel.

   - Half-fixed list: bullet 1 `เลือก eventual consistency` (dropped `ผม`) but bullet 2 still
     reads `ผมใช้ strong consistency` — the list is now mixed.
   - Consistent: both bullets drop the banned pronoun the same way.

**Workflow:** locate every occurrence first (the linter's per-line findings and a manual scan of
the enclosing structure), fix the whole set in one pass, then re-read each touched **sentence**
and each touched **list/table/clause-series** as a unit before declaring done. On Path B, a
re-run of the linter is necessary but **not sufficient** — it catches mechanical siblings (e.g.
every `ๆ`-spacing hit) but not judgment siblings (`มัน`, `ผม`, calqued connectives), which you
must sweep by reading.

---

## Path A — general Thai prose (write / edit / translate)

1. **Identify register, voice, and person deixis.** ASK if any are unclear — wrong register is
   worse than rough prose. Six register families (full guide in `references/register.md`):

   - **News / reference** — no first-person, no particles, active voice.
   - **Explainer** — bank/tech long-form, no particles, problem-first, `เรา`/`คุณ` address.
     (The scaler lesson voice on Path B is a fixed preset of this register.)
   - **Marketing (family)** — SaaS-SME / B2B-formal / fintech-warm / retail-tech sub-registers;
     person deixis required.
   - **Personal blog / dev war-story** — first-person `ผม` *or* `ดิฉัน` per gender, ครับ/ค่ะ at
     openings and sign-offs only. **ASK gender if not stated.**
   - **Academic long-form** — no particles, longer sentences acceptable, synthesis closings.
   - **Official / minutes** — government/ministerial/policy/legal. No particles, no
     first-person, explicit subjects, formal vocab swap.

   Voice attributes (gender, brand mood, formality) are orthogonal to register — pick both.

2. **Draft frame-first.** Walk the seven frames (topic fronted? conditions leading? no period
   spam? clauses closed? cohesion via zero anaphora? ก็ where Thai wants the beat? pivots via
   question or `แต่`?).

3. **Self-edit pass.** Scan for AI tells, and scope every fix per **Editing discipline** above
   (whole-sentence coherence + sibling propagation):
   - `forbidden-phrases.md` blocklist.
   - Connective budget: ≤1 ซึ่ง / ≤1 โดย / ≤1 ดังนั้น per ~100 words (`connective-budget`).
   - Period audit: drop mid-paragraph periods (`mid-paragraph-period`).
   - Closure audit: `ไม่ได้...อย่างเดียว` / `ไม่ใช่แค่...` need a closure particle
     (`dangling-additive-frame`).
   - Sentence-length variance (`mixed-sentence-length`).
   - ครับ/ค่ะ usage matches register (`khrap-kha-in-body`).
   - ถูก- passive genuinely adversative or agentless (`non-adversative-thuk`).

4. **Closing.** Don't recap (`no-recap-close`). End with a forward-looking line, a reframed
   question, a quiet handoff (`เท่านี้ก่อน`, `ลองเอาไปเล่นดู`), or just stop. Never
   `โดยสรุปแล้ว...` then re-state the body.

**When editing Thai prose:** apply the passes in reverse — hunt for frame violations and AI
tells, propose specific line edits with the *why*, and scope each fix per **Editing discipline**
(re-read the whole sentence; fix all parallel siblings). See `references/examples.md`.

**When translating English → Thai** (where AI fails hardest — it preserves English shape):
reorder to topic-comment (f1); move condition/time clauses front (f2); drop English-style
mid-paragraph periods (f3); add closure particles where the sentence dangles (f4); drop
pronouns once topic is set, use demonstratives where English uses pronouns (f5); insert ก็ where
Thai wants the beat (f6); convert "however/moreover" to questions or simple `แต่` (f7); localize
idioms; don't add politeness the source doesn't have; apply the ทับศัพท์ four-bucket guide
(`references/code-switching.md`, `style-rules.md`).

---

## Path B — scaler lesson (.th.mdx)

**Fixed register — no selection step: scaler peer-explainer.**

- Voice: รุ่นพี่เล่าตรง — confident, not hype, gives the reader credit
- Address: คุณ (direct) / เรา (walking through it together)
- No ผม / ดิฉัน / แอด, no gender question
- ครับ/ค่ะ sparingly (~1 per 4–5 sentences) for warmth — judgment, NOT a lint check
- Full voice + deixis + particle rules: `references/register.md` (scaler preset section)

### Write a lesson

1. Read the `.en.mdx` twin if it exists, for **structure parity** — mirror its sections and
   order. Do NOT translate its prose; write Thai natively.
2. Open from a problem or question, not a definition (`problem-first-open`).
3. Draft frame-first (f1–f7); follow scaler lesson structure in `references/mdx-lessons.md`
   (analogy per hard concept, numbers carry context, every code block wrapped in Thai
   why-sentences, `<Callout>` not blockquote callouts).
4. Self-edit: run the linter, fix every `error`, adjudicate every `warn`:
   ```
   uv run --project .claude/skills/thai-prose python \
     .claude/skills/thai-prose/scripts/lint_thai_content.py "<file>"
   ```
5. Close with `## Key Takeaways` or `## ถ้าจำได้แค่ 3 อย่าง` (3 actionable), not a โดยสรุป relist.

### Audit / fix a lesson

Run the linter first as the mechanical backbone, then the judgment passes. Scope every fix per
**Editing discipline** above — whole-sentence coherence + sibling propagation. The linter
catches mechanical siblings but not judgment siblings, so after fixing, **re-read each touched
sentence and each touched list/table/clause-series as a unit**:

- Mechanical (linter): ไม้ยมก spacing, Thai periods, em-dash density, blockquote callouts,
  forbidden phrases, script leakage. Fix all `error`; adjudicate `warn`.
- Judgment (read `references/`): voice/register, frame violations, analogy presence,
  numbers-carry-context, problem-first openings, discourse-marker naturalness. These recur in
  parallel siblings (list items, table rows, repeated `X คือ ...` stems) — sweep the whole
  enclosing block, not just the first hit.

Cite each issue by its rule slug (e.g. `rule-08-yamok`, `wrong-classifier`) and quote the
offending text. The blocklist scan is use-vs-mention exempt (backticked/blockquoted = OK).

### Cross-check th/en parity

`warn`-only. The linter compares heading count + order and named-section presence (Real-World,
Practice Questions, Key Takeaways). Flag gaps for the author to fill in Thai — never write or
rewrite the English side.

---

## Routing (when rules collide or run out)

- Mechanical rule (Path B) → the linter + its keyed reference (`rule-NN-*`).
- A case the rules don't cover → references are canonical; trace the gap before inventing a rule.
- Universal guidance collides with the scaler lesson layer → `references/overrides.md` decides
  (SCALER > UNIVERSAL, for lesson content). Outside lesson content, the universal rule stands.

## References

`style-rules.md` (frames + positive style) · `grammar.md` (word-level hard rules) ·
`register.md` (6 register families + scaler preset + deixis + voice + particles) ·
`ai-tells.md` (mechanical AI patterns) · `forbidden-phrases.md` (blocklist, linter-parsed) ·
`craft.md` (soft taste) · `code-switching.md` (ทับศัพท์ four-bucket) ·
`mdx-lessons.md` (Path B lesson structure + MDX components + bilingual parity) ·
`overrides.md` (scaler > universal seams + attribution) · `examples.md` (register-tagged
before/after) · `exemplars.md` (full-length native models).

Scholarly provenance (Iwasaki & Ingkaphirom, Smyth, Prasithrathsint, Takahashi, Olsson, Thai
Discourse Treebank, Singnoi, Royal Institute, Marcel Barang) lives in the kien-thai corpus —
not in this bundle.
