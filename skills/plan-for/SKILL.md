---
name: plan-for
description: Decide the design direction for a piece of work — lay out 2-3 candidate approaches with trade-offs, show representative current-vs-changed code side by side with old/new diagrams, and recommend one — written to a persistent HTML design doc (.plan/<stem>-design.html), without the detailed implementation plan. Use when the user asks which approach to take or how best to build something, wants design options weighed before committing, says /plan-for <what they want to do>, or after research when the approach is not yet settled. Sits between research-project and plan-todo in the research -> plan-for -> plan-todo -> update -> implement workflow.
---

# plan-for

The design-direction phase, between `research-project` and `plan-todo`. The user
invokes it with their intent and some detail (`/plan-for <what I want to do>`).
Its job is to settle **which approach** and **why** — before `plan-todo` commits
that decision to a concrete, snippet-level phased plan.

This is where the creative and decision work lives. `research-project` tells you
how the system works today; `plan-for` chooses where to take it; `plan-todo`
turns the chosen direction into mechanical steps.

Language- and stack-agnostic. Match whatever conventions and tooling the project
already uses; discover them rather than assuming.

## Workflow

1. **Ground in intent and research.** Read the user's `<what they want to do>`
   description and any `args`. If a `.project/research_*.html` exists for this
   work, read it first; if several research docs exist, pick the one whose
   Scope matches this work, and ask which one if it's still ambiguous. If no
   research has been done and the change is non-trivial, say so and recommend
   `research-project` — but you may proceed from the user's description alone
   when the work is well understood.

2. **Resolve the doc filename.**
   - Directory: `.plan/` (create it if missing).
   - If the user gave a name (via `args` or message), use
     `.plan/<name>-design.html`.
   - Otherwise derive a short, descriptive kebab-case stem from the intent
     (e.g. `.plan/rate-limiter-design.html`) and tell the user the name you
     chose.
   - If a design doc for this work already exists (same or similar name), read
     it and refine it in place rather than creating a near-duplicate or
     overwriting from scratch.

3. **Write the design doc** from the bundled [template.html](template.html).
   Include, concretely:
   - **Header** — `data-status="awaiting-approval"` on `<body>` and a
     `Source research:` link to the research doc you grounded in.
   - **Goal & scope** — what we want to achieve and what is explicitly out of
     scope. Restate the user's intent in precise terms.
   - **Constraints & context** — what bounds the solution: existing
     architecture, performance/compat requirements, deadlines, what the research
     surfaced. Cite `file:line` where it grounds a constraint.
   - **Candidate approaches** — 2-3 genuinely distinct designs. For each: how it
     works, what it touches at a high level, and its trade-offs (complexity,
     risk, blast radius, effort, reversibility). Real alternatives, not strawmen.
   - **Code impact, side by side** — for each approach (at minimum the
     recommendation), a `.compare` block: left = the current code (real excerpt
     with `file:line`), right = what it becomes under that approach. Plus a
     Mermaid old | new diagram for every scope/feature the approach changes —
     required, no exceptions. Representative, not exhaustive: enough to judge
     the direction.
   - **Recommendation** — pick one and justify it against the others. If the
     user shared a reference implementation, weigh its approach explicitly.
   - **Open decisions** — what the reviewer must still settle before planning:
     unresolved trade-offs, unknowns, questions only the user can answer.

   Escape `<` `>` `&` inside code excerpts, and confirm the HTML is well-formed
   (parse check) before reporting.

4. **Stop. Do not plan the implementation and do not code.** Report the doc path
   and a short summary of the recommended direction, ending with "open it in a
   browser to review". The next phase is `plan-todo` — but first the user
   reviews the doc and picks a direction (they may annotate it with
   `<note>...</note>`; run `plan-update` to address notes on this doc). Once a
   direction is chosen, `plan-todo` turns it into the detailed phased plan.

## Rules

- **No exhaustive edit list, no phased todo, no production code.** The code
  this doc shows is *representative* — current-vs-changed excerpts, enough to
  judge the direction by. The complete file-by-file changes and the todo list
  are `plan-todo`'s job; if you find yourself enumerating every touched file or
  writing step-by-step tasks, you have crossed into `plan-todo`.
- Present **real** alternatives with honest trade-offs. A doc with one option
  dressed up as three has failed its purpose — the point is an informed choice.
- Be specific and grounded: cite `file:line`, name actual components, and tie
  each approach to the project's real constraints.
- End by stating that nothing was planned in detail or implemented, and that the
  doc awaits a direction decision before `plan-todo`.
