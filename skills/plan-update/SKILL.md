---
name: plan-update
description: Address <note> annotations the user left in a .plan/ design or plan doc (or a .project/ research doc) and revise the document accordingly — without implementing yet. Use when the user says they annotated/added notes/commented on a doc, asks to revise/update the plan or design, or says /plan-update. The review phase of the research -> plan-for -> plan-todo -> update -> implement workflow; repeats until the plan is approved.
---

# plan-update

The review phase of the **research -> plan-for -> plan-todo -> update ->
implement** workflow. The user has opened the doc (in a browser to read, in
their editor to annotate) and added `<note>...</note>` elements — corrections,
rejected approaches, domain knowledge, scope cuts. Your job is to address every
note and revise the document. This loop repeats (often several times) until the
plan is approved.

This phase is why the docs live in shared, mutable HTML files: the user gives
structured feedback at precise locations instead of steering through chat.
Treat their annotations as authoritative. plan-update owns annotation handling
for all three doc types: research (`.project/research_*.html`), design
(`.plan/<stem>-design.html`), and plan (`.plan/<stem>-plan.html`).

Language- and stack-agnostic.

## Workflow

1. **Locate the doc.** Use the path the user gives, or the most recently
   touched `.plan/*.html` or `.project/research_*.html`. If more than one was
   recently edited (design vs plan vs research), ask which one rather than
   guessing by mtime. If neither directory has a doc, don't invent one — say
   there's nothing to update and recommend `plan-todo` / `plan-for` /
   `research-project` first.

2. **Find every note.** Collect every `<note>` element in the doc — that is
   the one annotation marker. If a full read turns up zero `<note>` elements,
   do not edit and do not assume approval — report that the doc looks
   unannotated and ask whether they meant a different file or are approving
   as-is.

3. **Address each note.** For every annotation:
   - Apply the correction or incorporate the domain knowledge.
   - If a note rejects an approach, replace it — don't just delete the note.
   - If a note says remove a section, remove it entirely.
   - The user's notes override your earlier design choices. If a note
     contradicts a constraint that research or the design doc grounded (a
     cited `file:line` invariant), do it their way — but record the accepted
     trade-off in the doc's Risks section, not only in chat, and note it in
     your report.
   - When revising a design doc that a sibling plan doc already builds on,
     flag that the plan needs re-planning — don't silently leave them
     inconsistent.

4. **Clean up.** Remove each `<note>` element once addressed, keep the doc
   coherent and well-formed (parse check), and update the phased todo, the
   `Verify:` blocks, and the old | new diagrams so they still match the
   revised plan. Keep code blocks on the doc's highlighting convention:
   `class="language-<lang>"` for code, `class="language-diff"` (`+`/`-`
   lines, GitHub-style) for modifications. Keep `.compare` figures on the
   `class="old"` / `class="new"` convention (red/green labels).

5. **Report and stop.** List what you changed, note by note, and explicitly
   confirm you did **not** implement anything. Invite another annotation pass.
   When the user approves the plan, set `<body data-status="approved">` (and
   the badge text) — `plan-implement` requires it — and only then move to
   `plan-implement`.

## Rules

- **Do not implement.** Honor "don't implement yet" — this phase only edits
  the doc. The working tree stays untouched.
- Address *all* notes, not a subset. If a note is unclear, or two notes are
  mutually exclusive (can't both be honored), ask rather than guess — name the
  specific notes and ask which wins before revising.
- If the plan already has `checked` tasks (a prior `plan-implement` run), do
  not reset them. Where a note changes an already-implemented section, keep
  the marks accurate and call out that the shipped code needs rework.
- Keep the doc the single source of truth: don't park decisions in chat that
  belong in the doc.
- Expect to run this loop 1-6 times. Each pass should converge, not reopen
  settled sections.
