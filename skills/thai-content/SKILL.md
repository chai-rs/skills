---
name: thai-content
description: "Write and audit Thai-language system-design lesson content (.th.mdx) for scaler-client in the house voice — รุ่นพี่ที่เคยผ่านมาแล้ว เล่าให้ฟังตรง — not generic AI Thai. TRIGGER when: user asks to write, draft, translate, audit, or fix a Thai lesson or section under content/modules; user asks to check Thai MDX against the content rules. DO NOT TRIGGER for: English (.en.mdx) prose, UI strings, code identifiers, or non-lesson chat."
---

# thai-content

## Why this skill exists

Generic AI Thai imports English discourse mechanics and adds politeness/connective
padding by default. Native Thai readers feel the friction. This skill writes lessons
that read like a Thai engineer explaining to a peer — direct, confident, concrete.

The rules live in `references/`. This spine is the workflow + routing. The rules were
migrated from the project's CONTENT-GUIDE.md (now a pointer here) and merged with the
universal Thai-prose layer adapted from chakrit/kien-thai (MIT). See `references/overrides.md`.

## Fixed register

One register, no register-selection step: **scaler peer-explainer**.

- Voice: รุ่นพี่เล่าตรง — confident, not hype, gives the reader credit
- Address: คุณ (direct) / เรา (walking through it together)
- No ผม / ดิฉัน / แอด, no gender question
- ครับ/ค่ะ sparingly (~1 per 4-5 sentences) for warmth — this is judgment, NOT a lint check
- Full voice + deixis rules: `references/register.md`

## Native-Thai frames (apply when drafting and editing)

Port of kien-thai's structural frames, filtered to this one register. Walk them before
picking words — most surface AI-tells auto-resolve once the frames are right:

- `f1` topic-comment over subject-verb-object
- `f2` condition / time clauses go first (`พอ...ก็`, `ถ้า...จะ`)
- `f3` sentence boundaries via space and newline, not period → `rule-07-period`
- `f4` close clauses with particles (`ด้วย`, `แล้ว`, `ต่างหาก`)
- `f5` cohesion via zero-anaphora + demonstratives, not `มัน`/`พวกเขา`
- `f6` pacing via `ก็` where Thai wants the beat
- `f7` pivots via question or simple `แต่`, not `อย่างไรก็ตาม`

Full frame explanations + Bad/Good triplets: `references/style-rules.md` and `references/grammar.md`.

## Task — write a lesson

1. Read the `.en.mdx` twin if it exists, for **structure parity** — mirror its sections and
   order. Do NOT translate its prose; write Thai natively.
2. Open from a problem or question, not a definition (`problem-first-open`).
3. Draft frame-first (f1–f7); follow scaler lesson structure in `references/mdx-lessons.md`
   (analogy per hard concept, numbers carry context, every code block wrapped in Thai why-sentences).
4. Self-edit: run the linter, fix every `error`, adjudicate every `warn`:
   ```
   uv run --project .claude/skills/thai-content python \
     .claude/skills/thai-content/scripts/lint_thai_content.py "<file>"
   ```
5. Close with `## Key Takeaways` or `## ถ้าจำได้แค่ 3 อย่าง` (3 actionable), not a โดยสรุป relist.

## Task — audit / fix a lesson

Run the linter first as the mechanical backbone, then the judgment passes:

- Mechanical (linter): ไม้ยมก spacing, Thai periods, em-dash density, blockquote callouts,
  forbidden phrases, script leakage. Fix all `error`; adjudicate `warn`.
- Judgment (read `references/`): voice/register, frame violations, analogy presence,
  numbers-carry-context, problem-first openings, discourse-marker naturalness.

Cite each issue by its rule slug (e.g. `rule-08-yamok`, `wrong-classifier`) and quote the
offending text. The blocklist scan is use-vs-mention exempt (backticked/blockquoted = OK).

## Task — cross-check th/en parity

`warn`-only. The linter compares heading count + order and named-section presence
(Real-World, Practice Questions, Key Takeaways). Flag gaps for the author to fill in Thai —
never write or rewrite the English side.

## Routing

- Mechanical rule → the linter + its keyed reference (`rule-NN-*`).
- A case the rules don't cover → references are canonical; trace the gap before inventing a rule.
- Domain rule collides with universal Thai guidance → `references/overrides.md` decides
  (DOMAIN > UNIVERSAL).

## References

`style-rules.md` (frames + positive style) · `grammar.md` (word-level hard rules) ·
`register.md` (voice / deixis / particles) · `ai-tells.md` (AI patterns) ·
`forbidden-phrases.md` (blocklist, linter-parsed) · `code-switching.md` (ทับศัพท์ four-bucket) ·
`mdx-lessons.md` (lesson structure + MDX components + bilingual parity) ·
`overrides.md` (scaler > universal seams + attribution) · `examples.md` (before/after).
