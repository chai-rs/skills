---
name: plan-update
description: Address inline notes/annotations the user left in a plan doc and revise the plan accordingly — without implementing yet. Use when the user says they annotated/added notes/commented on the plan, asks to revise/update the plan, or says /plan-update. The review phase of the research -> plan-for -> plan-todo -> update -> implement workflow; repeats until the plan is approved.
---

# plan-update

The review phase of the **research -> plan-for -> plan-todo -> update ->
implement** workflow. The user has opened the plan doc in their editor and added
inline notes — corrections,
rejected approaches, domain knowledge, scope cuts. Your job is to address every
note and revise the document. This loop repeats (often several times) until the
plan is approved.

This phase is why the plan lives in a shared, mutable markdown file: it lets the
user give structured feedback at precise locations instead of steering through
chat. Treat their annotations as authoritative.

Language- and stack-agnostic.

## Workflow

1. **Locate the plan.** Use the path the user gives, or the most recently
   touched file in `.plan/`. If multiple plans exist and it's ambiguous, ask
   which one.

2. **Find every note.** Read the whole doc and collect all annotations — inline
   comments, `NOTE:`/`TODO:`/`?`/`<<< >>>` markers, struck-through sections,
   anything the user added. Do not miss any; a half-addressed plan forces
   another round.

3. **Address each note.** For every annotation:
   - Apply the correction or incorporate the domain knowledge.
   - If a note rejects an approach, replace it — don't just delete the note.
   - If a note says remove a section, remove it entirely.
   - The user's notes override your earlier design choices. If a note seems
     wrong or contradictory, do it their way but flag the concern briefly.

4. **Clean up.** Remove the annotation markers once addressed, keep the doc
   coherent, and update the phased todo list so it still matches the revised
   plan.

5. **Report and stop.** List what you changed, note by note, and explicitly
   confirm you did **not** implement anything. Invite another annotation pass.
   Only move to `plan-implement` when the user approves the plan.

## Rules

- **Do not implement.** Honor "don't implement yet" — this phase only edits the
  plan document. The working tree stays untouched.
- Address *all* notes, not a subset. If one is unclear, ask rather than guess.
- Keep the doc the single source of truth: don't park decisions in chat that
  belong in the plan.
- Expect to run this loop 1-6 times. Each pass should converge, not reopen
  settled sections.
