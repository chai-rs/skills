---
description: Execute the active plan end-to-end — mark tasks done as you go, never stop until every phase is complete.
---

Implement every task and phase in the plan document. As soon as a task is finished, mark it completed in the plan. Do not stop until every phase is complete.

Working rules:

- Do not add unnecessary comments or docstrings — only document non-obvious behavior.
- Avoid type-system escape hatches:
  - TypeScript: no `any`, no `unknown` unless narrowed at the boundary, no `as` casts to bypass errors.
  - Go: no empty `interface{}` / `any` outside of well-justified generics; prefer concrete types.
  - Python: no `typing.Any` for new code; type with `Protocol` / `TypedDict` / generics instead.
  - Rust: no `unsafe` unless required; prefer safe abstractions, justify `.unwrap()` / `.expect()` in tests only.
  - Other languages: avoid the equivalent escape hatch unless explicitly required.
- After each task, run the project's typecheck / lint / build (`tsc`, `go vet ./... && go build ./...`, `cargo check`, `mypy`, etc.) and fix any error before moving on.
- After each phase, run the relevant test suite (`pnpm test`, `go test ./...`, `cargo test`, `pytest`, etc.).
- If the plan changes mid-flight (compiler reveals a missing step), update the plan document first, then continue.
