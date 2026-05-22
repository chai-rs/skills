---
description: Deep-read the given folder, understand it thoroughly, and write a detailed report to research.md.
---

Read the target folder in depth. Understand how it works, what it does, and any specificities — architectural patterns, framework conventions, build tooling, deployment shape, public API surface, hot paths, known traps. Cover whatever stack is in front of you (TypeScript, Go, Rust, Python, Java, mixed monorepo, etc.) — do not assume a particular language.

When you have a complete picture, write a detailed report to `research.md` in the project root. The report should include:

- **Summary** — one paragraph: what this codebase does and who uses it.
- **Architecture** — top-level structure, key modules, how data flows.
- **Tech stack** — languages, frameworks, build tools, runtime targets.
- **Entry points** — where execution starts (`main`, server bootstrap, CLI handler, etc.).
- **Conventions** — naming, error handling, logging, testing patterns.
- **Notable specificities** — anything non-standard, surprising, or worth flagging to a new contributor.
- **Open questions** — anything you couldn't fully resolve from the code alone.
