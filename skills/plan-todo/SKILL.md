---
name: plan-todo
description: Write a detailed, reviewable implementation plan (with code snippets and a phased todo list) to a persistent plan doc — without writing any production code. Use after the design direction is chosen, when the user asks for a plan doc, or says /plan-todo. The planning phase of the research -> plan-for -> plan-todo -> update -> implement workflow.
---

# plan-todo

The planning phase of the **research -> plan-for -> plan-todo -> update ->
implement** workflow. Produce a detailed `plan.md`-style document that a reviewer
can read, annotate, and approve *before* implementation. The design direction is
already decided (in `plan-for`); this phase turns it into concrete, mechanical
steps so that implementation becomes boring.

Language- and stack-agnostic. Match whatever conventions and tooling the
project already uses; discover them rather than assuming.

## Workflow

1. **Ground in the chosen direction.** Read the `plan-for` design doc in
   `.plan/` if one exists, and any `.project/research_*.md` for the work. The
   approach should already be settled — if it is not and the change is
   non-trivial, recommend `plan-for` (to choose a direction) or
   `research-project` (to understand the system) first.

2. **Resolve the plan filename.**
   - Directory: `.plan/` (create it if missing).
   - If the user gave a name (via `args` or message), use `.plan/<name>.md`.
   - Otherwise derive a short, descriptive kebab-case name from the task
     context (e.g. `.plan/add-rate-limiter.md`) and tell the user the name
     you chose.

3. **Write the plan doc.** Include, concretely:
   - **Goal & scope** — what we're building and what's explicitly out of scope.
   - **Approach** — the chosen design from `plan-for`, summarized so the plan
     stands on its own. Do not reopen the decision or re-litigate alternatives
     here; if no `plan-for` doc exists, briefly state the approach you're
     planning to and follow any reference implementation the user shared.
   - **Changes** — actual code snippets and the **file paths** they touch.
     Show real diffs/snippets, not vague descriptions.
   - **Risks / open questions** — anything the reviewer should weigh in on.

4. **Append a phased todo list.** A checklist of phases and individual tasks
   that fully covers the plan. This becomes the progress tracker during
   implementation. Each item should be concrete and independently checkable.

5. **Stop. Do not implement.** Report the plan path and a short summary. The
   next phase is `plan-update` (the user annotates the doc) and only then
   `plan-implement`. The phase before this one is `plan-for`, which chose the
   direction this plan implements.

## Rules

- **Do not write production code in this phase.** The plan contains snippets;
  the working tree stays untouched.
- Prefer the markdown plan doc over built-in plan mode — it is persistent,
  annotatable, and survives context compaction.
- Be specific: real file paths, real snippets, real task breakdown. A plan
  the reviewer cannot annotate precisely has failed its purpose.
- End by explicitly noting that nothing was implemented and the plan awaits
  review/annotation.
