---
name: plan-for
description: Decide the design direction for a piece of work — lay out 2-3 candidate approaches with trade-offs and recommend one — and write it to a persistent design doc, without writing the detailed implementation plan or any code. Use when the user says /plan-for <what they want to do>, or after research when the approach is not yet settled. Sits between research-project and plan-todo in the research -> plan-for -> plan-todo -> update -> implement workflow.
---

# plan-for

The design-direction phase, between `research-project` and `plan-todo`. The user
invokes it with their intent and some detail (`/plan-for <what I want to do>`).
Its job is to settle **which approach** and **why** — before `plan-todo` commits
that decision to a concrete, snippet-level phased plan.

This is where the creative and decision work lives. `research-project` tells you
how the system works today; `plan-for` chooses where to take it; `plan-todo`
turns the chosen direction into mechanical steps. Keep those boundaries: do not
produce a phased todo list or code snippets here — that is `plan-todo`'s job.

Language- and stack-agnostic. Match whatever conventions and tooling the project
already uses; discover them rather than assuming.

## Workflow

1. **Ground in intent and research.** Read the user's `<what they want to do>`
   description and any `args`. If a `.project/research_*.md` exists for this
   work, read it first. If no research has been done and the change is
   non-trivial, say so and recommend `research-project` — but you may proceed
   from the user's description alone when the work is well understood.

2. **Resolve the doc filename.**
   - Directory: `.plan/` (create it if missing).
   - If the user gave a name (via `args` or message), use `.plan/<name>.md`.
   - Otherwise derive a short, descriptive kebab-case name from the intent
     (e.g. `.plan/rate-limiter-design.md`) and tell the user the name you chose.

3. **Write the design doc.** Include, concretely:
   - **Goal & scope** — what we want to achieve and what is explicitly out of
     scope. Restate the user's intent in precise terms.
   - **Constraints & context** — what bounds the solution: existing
     architecture, performance/compat requirements, deadlines, what the research
     surfaced. Cite `file:line` where it grounds a constraint.
   - **Candidate approaches** — 2-3 genuinely distinct designs. For each: how it
     works, what it touches at a high level, and its trade-offs (complexity,
     risk, blast radius, effort, reversibility). Real alternatives, not strawmen.
   - **Recommendation** — pick one and justify it against the others. If the
     user shared a reference implementation, weigh its approach explicitly.
   - **Open decisions** — what the reviewer must still settle before planning:
     unresolved trade-offs, unknowns, questions only the user can answer.

4. **Stop. Do not plan the implementation and do not code.** Report the doc path
   and a short summary of the recommended direction. The next phase is
   `plan-todo`, which takes the chosen approach and writes the detailed phased
   plan with snippets.

## Rules

- **No phased todo list, no code snippets, no production code.** This phase
  produces a direction, not an implementation plan. If you find yourself writing
  step-by-step tasks or real diffs, you have crossed into `plan-todo`.
- Present **real** alternatives with honest trade-offs. A doc with one option
  dressed up as three has failed its purpose — the point is an informed choice.
- Be specific and grounded: cite `file:line`, name actual components, and tie
  each approach to the project's real constraints.
- End by stating that nothing was planned in detail or implemented, and that the
  doc awaits a direction decision before `plan-todo`.
