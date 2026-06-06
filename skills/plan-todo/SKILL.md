---
name: plan-todo
description: Write a detailed, reviewable implementation plan (real code snippets, side-by-side old/new diagrams, per-phase acceptance criteria, and a phased todo) to a persistent HTML plan doc (.plan/<stem>-plan.html) — without writing any production code. Use after the design direction is chosen, when the user asks for a plan doc, or says /plan-todo. The planning phase of the research -> plan-for -> plan-todo -> update -> implement workflow.
---

# plan-todo

The planning phase of the **research -> plan-for -> plan-todo -> update ->
implement** workflow. Produce a detailed HTML plan document that a reviewer can
read in a browser, annotate, and approve *before* implementation. The design
direction is already decided (in `plan-for`); this phase turns it into concrete,
mechanical steps so that implementation becomes boring.

Language- and stack-agnostic. Match whatever conventions and tooling the
project already uses; discover them rather than assuming.

## Workflow

1. **Ground in the chosen direction.** Read the `plan-for` design doc
   (`.plan/<stem>-design.html`) if one exists, and the research doc its
   `Source research:` link names. If several research docs exist and no design
   doc links one, pick the one whose Scope matches this work; ask if ambiguous.
   If the approach is not settled and the change is non-trivial, recommend
   `plan-for` (to choose a direction) or `research-project` (to understand the
   system) first.

2. **Resolve the plan filename.**
   - Directory: `.plan/` (create it if missing).
   - If a design doc `.plan/<stem>-design.html` exists for this work, name the
     plan `.plan/<stem>-plan.html` so the two are siblings.
   - Otherwise use the user-given name, or derive a short descriptive
     kebab-case stem from the task context, with a `-plan.html` suffix
     (e.g. `.plan/add-rate-limiter-plan.html`), and tell the user the name you
     chose.
   - Never overwrite a `*-design.html`. If the resolved name collides with any
     existing `.plan/` file, pick a distinct name or ask.

3. **Write the plan doc** from the bundled [template.html](template.html). If a
   plan already exists at the resolved path, read it first; if it contains
   `checked` tasks or `<note>` elements, stop and ask how to proceed rather
   than overwriting. Include, concretely:
   - **Header** — `data-status="awaiting-approval"` on `<body>`, plus
     `Design doc:` and `Source research:` links. `plan-update` flips the status
     on approval; `plan-implement` refuses to run without it.
   - **Goal** and **Scope** — what we're building, and what's explicitly out
     of scope.
   - **Approach** — the chosen design from `plan-for`, summarized so the plan
     stands on its own. Do not reopen the decision or re-litigate alternatives
     here; if no design doc exists, briefly state the approach you're planning
     to and follow any reference implementation the user shared.
   - **Diagrams** — a side-by-side old | new Mermaid diagram for *every*
     scope/feature/change in the plan. Required, no exceptions. In every
     `.compare` block, mark the before figure with `class="old"` and the
     after figure with `class="new"` — the template colors their labels
     red/green so the two sides are identifiable at a glance.
   - **Changes** — actual code snippets and the **file paths** they touch,
     with `<` `>` `&` escaped. Real diffs/snippets, not vague descriptions.
     Syntax-highlight new code with `class="language-<lang>"` on the `<code>`
     element; show modifications to existing code as GitHub-style diffs
     (`class="language-diff"`, `+`/`-` line prefixes).
   - **Risks / open decisions** — anything the reviewer should weigh in on.
   - **Todo** — phases and individually checkable tasks
     (`<input type="checkbox">`) that fully cover the plan, each phase with a
     `Verify:` acceptance-criteria block that defines "done" for that phase.
     This becomes the progress tracker during implementation.
   - **Deviations** — an empty section `plan-implement` appends to.

4. **Validate and stop. Do not implement.** Confirm the HTML is well-formed
   (parse check) before reporting. Report the plan path and a short summary,
   ending with "open it in a browser to review". The next phase is
   `plan-update` (the user annotates the doc with `<note>...</note>`) and only
   then `plan-implement`. The phase before this one is `plan-for`, which chose
   the direction this plan implements.

## Rules

- **Do not write production code in this phase.** The plan contains snippets;
  the working tree stays untouched.
- Prefer the HTML plan doc over built-in plan mode — it is persistent,
  annotatable, and survives context compaction.
- Be specific: real file paths, real snippets, real task breakdown. A plan
  the reviewer cannot annotate precisely has failed its purpose.
- End by explicitly noting that nothing was implemented and the plan awaits
  review/annotation.
