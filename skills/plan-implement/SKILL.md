---
name: plan-implement
description: Execute an approved plan doc end to end — implement every phase and task, mark items complete in the plan as you go, and run the project's checks continuously. Use when the user approves the plan and says implement it, or says /plan-implement. Final phase of the research -> plan-for -> plan-todo -> update -> implement workflow.
---

# plan-implement

Final phase of the **research -> plan-for -> plan-todo -> update -> implement**
workflow. The plan is
approved; the creative work is done. Implementation should be mechanical: build
exactly what the plan specifies, track progress in the plan doc, and keep the
project green. Only run this once the user has explicitly approved the plan.

Language- and stack-agnostic — use whatever build/test/lint tooling the project
already has.

## Workflow

1. **Load the plan.** Read the approved `.plan/<name>.md` (ask which one if
   ambiguous). The plan and its phased todo list are the source of truth for
   scope and progress.

2. **Discover the project's checks.** Identify how this project builds, type-
   checks, lints, and tests (e.g. its makefile/task runner, CI config, package
   scripts, or the conventions in CLAUDE.md). You'll run these continuously.

3. **Implement task by task, in order.**
   - Do everything in the plan — do not cherry-pick or silently skip tasks.
   - As you finish each task or phase, **mark it complete in the plan doc**
     (check the box / strike it through) so the doc reflects real progress.
   - Run the relevant checks frequently (after each meaningful change, not just
     at the end) so regressions surface early. Fix issues as they appear.
   - **Do not stop** until every task and phase is complete — unless you hit a
     genuine blocker or a decision the plan doesn't cover, in which case stop
     and ask rather than guessing.

4. **Final verification.** Run the full check suite — build, typecheck, lint,
   tests — and confirm it passes. Paste the relevant output. Re-read your diff
   against the plan to confirm it matches. Per the completion bar, the task is
   not "done" until checks pass and the diff matches the plan.

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
- Honor any interface/signature constraints the plan marked as fixed.
- **Never commit or push** unless the user explicitly asks. A clean tree and
  passing tests are not permission to commit.
- If the user reverts and re-scopes mid-implementation, follow the new scope
  and update the plan doc to match rather than patching around it.
