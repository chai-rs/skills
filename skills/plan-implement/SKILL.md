---
name: plan-implement
description: Execute an approved HTML plan doc (.plan/<stem>-plan.html) end to end — implement every phase and task, satisfy each phase's Verify acceptance criteria, mark tasks checked in the plan as you go, log deviations, and run the project's checks continuously. Use when the user approves the plan and says implement it, or says /plan-implement. Final phase of the research -> plan-for -> plan-todo -> update -> implement workflow.
---

# plan-implement

Final phase of the **research -> plan-for -> plan-todo -> update -> implement**
workflow. The plan is approved; the creative work is done. Implementation
should be mechanical: build exactly what the plan specifies, track progress in
the plan doc, and keep the project green.

Language- and stack-agnostic — use whatever build/test/lint tooling the project
already has.

## Workflow

1. **Load the plan.** Use the plan the user named; otherwise the most recently
   touched `.plan/*-plan.html` — a `*-design.html` has no todo list; it is an
   input, not an implementation target. If several qualify, ask. If none
   exists, do not implement from the chat request — recommend `plan-todo`
   first.
   - **Approval gate:** if the doc's `data-status` is not `approved`, or any
     `<note>` element remains, it was not finalized in review — stop and route
     back to `plan-update`; do not treat annotation text as spec.
   - **Resume/reconcile:** if any tasks are already `checked` (resumed
     session), reconcile against the working tree before continuing: a checked
     box is done only if its change is actually present. Trust the code,
     correct the boxes, and resume from the first genuinely-incomplete task.

2. **Discover the project's checks.** Identify how this project builds, type-
   checks, lints, and tests (e.g. its makefile/task runner, CI config, package
   scripts, or the conventions in CLAUDE.md). You'll run these continuously.
   If the project has no automated checks, say so and pick the lightest
   verification available (run the touched script, a smoke test, a syntax
   check) — that becomes the completion gate in step 4.

3. **Implement task by task, in order.**
   - Do everything in the plan — do not cherry-pick or silently skip tasks.
   - As you finish each task, **mark it `checked` in the plan doc** so the doc
     reflects real progress.
   - A phase may be checked off only after its `Verify:` block passes; paste
     the verification output in your report.
   - Run the relevant checks frequently (after each meaningful change, not just
     at the end) so regressions surface early. Fix issues as they appear.
   - **Do not stop** until every task and phase is complete — unless you hit a
     genuine blocker or a decision the plan doesn't cover, in which case stop
     and ask rather than guessing.

4. **Final verification.** Run the full check suite (or the stated fallback)
   and confirm it passes. Paste the relevant output. Re-read your diff against
   the plan to confirm it matches. When every phase passes, set
   `data-status="done"` (and the badge text). Per the completion bar, the task
   is not "done" until checks pass and the diff matches the plan.

## Code quality directives

- Match the project's existing conventions, types, and style. Do not loosen
  typing or introduce escape-hatch types to make things compile.
- **Do not add unnecessary comments or doc blocks.** Write self-explanatory
  code; comment only where the project's conventions call for it.
- Keep changes scoped to the plan. If you discover work the plan missed, note
  it and ask — don't expand scope unilaterally.

## Rules

- The plan doc is the live progress tracker — keep it accurate as you go, not
  only at the end.
- If a plan snippet is mechanically wrong against the current tree (typo,
  drifted signature, stale import) and a small fix makes checks pass, apply
  the fix AND log it as a row in the plan's Deviations section with the
  reason. A different approach or new scope is not a mechanical fix — stop and
  ask.
- Honor any interface/signature constraints the plan marked as fixed.
- **Never commit or push** unless the user explicitly asks. A clean tree and
  passing tests are not permission to commit.
- If the user reverts and re-scopes mid-implementation, follow the new scope
  and update the plan doc to match rather than patching around it.
