---
name: research-project
description: Deeply explore a codebase, folder, feature, or system and write findings to a persistent HTML research doc (.project/research_<timestamp>.html, with diagrams of the current system) before any planning or coding. Use when the user wants to understand how something works, asks you to research/investigate/study a part of the project, or says /research-project. First phase of the research -> plan-for -> plan-todo -> update -> implement workflow.
---

# research-project

Phase 1 of the workflow: **research -> plan-for -> plan-todo -> update ->
implement**. The goal is a written, reviewable understanding of the target
*before* anyone chooses an approach, writes a plan, or writes code. The worst
failure mode this prevents: implementations that work in isolation but break
the surrounding system.

Language- and stack-agnostic. Do not assume any specific language, framework,
or tooling — discover it.

## Workflow

1. **Scope the target.** Read the user's request (and any `args`). Identify
   exactly what to research: a folder, a feature, a subsystem, a bug, an
   integration. If ambiguous, ask one clarifying question, then proceed.

2. **Explore deeply, not superficially.** Read the actual code, configs,
   tests, and docs — do not skim. Trace real call paths and data flow across
   files, not just the entry point. Note specificities, edge cases, invariants,
   and intricacies. Spend the effort here; this is the point of the phase.
   - For broad exploration (more than ~3 searches), launch the `Explore` agent.
   - Read whole files for anything load-bearing — excerpts hide context.

3. **Write findings to a persistent doc — do not just summarize in chat.**
   - Directory: `.project/` (create it if missing).
   - Filename: `research_<YYYYMMDDHHmmss>.html` using the current local time.
   - Write it from the bundled [template.html](template.html) — same family as
     the `.plan/` docs: `data-status` header, `<note>` annotation, escaped and
     syntax-highlighted code excerpts (`class="language-<lang>"` on the
     `<code>` element). Confirm the HTML is well-formed (parse check) before
     reporting.
   - The file is the review surface; chat summaries are not.

4. **Stop and hand off for review.** Report the doc path and a 2-3 sentence
   summary, ending with "open it in a browser to review". Do **not** start
   planning or editing code. The user reviews and corrects your understanding
   first — they annotate with `<note>...</note>` and `plan-update` revises the
   doc.

## What the research doc must contain

- **Scope** — what was researched, and what was explicitly out of scope.
- **How it works** — the mechanism, in depth: components, responsibilities,
  control/data flow, key types/functions with `file:line` references.
- **Diagrams** — Mermaid diagram(s) of the current system for every researched
  scope: components and control/data flow. Current state only — the old | new
  compare starts at `plan-for`.
- **Specificities & intricacies** — non-obvious behavior, invariants, edge
  cases, assumptions the code relies on.
- **Touch points** — what depends on this and what it depends on; the blast
  radius of a change here.
- **Open questions / risks** — things to confirm with the user, unknowns,
  suspected fragility.

Use precise `file:line` references throughout so claims are verifiable.

## Rules

- Only state things you verified by reading. Mark inferences as "likely" and
  unverified general knowledge as such. Never fabricate names or APIs.
- Discover the project's conventions and tooling; do not assume them.
- Do not choose an approach, write a plan, or edit code in this phase. When
  research is approved, the next phase is `plan-for`.
