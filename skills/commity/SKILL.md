---
name: commity
description: Create a single git commit from already-staged changes using a Conventional Commits message, then report the result. Use when the user runs /commity or asks to commit staged changes following the conventional commits spec. Does NOT push.
---

# commity

Commit **only what is already staged**, with a [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) message, then report what happened. This skill never stages, never pushes, never amends, never uses `--no-verify` or `--force`.

## Process

1. Run these in parallel to understand state:
   - `git status` — see staged vs unstaged vs untracked.
   - `git diff --staged` — the exact changes that will be committed.
   - `git log -n 10 --oneline` — match the repo's existing message style/scopes.

2. **Gate on staged content.** If `git diff --staged` is empty (nothing staged):
   - STOP. Do not run `git add`. Do not commit.
   - Show the user the current `git status` and tell them to stage files first (`git add <paths>`), then re-run `/commity`.

3. Compose a Conventional Commits message from the staged diff (see format below). Reuse scopes that already appear in `git log`. Do not invent prefixes.

4. Create the commit using a HEREDOC so the body formats correctly:
   ```bash
   git commit -m "$(cat <<'EOF'
   <type>[optional scope]: <description>

   [optional body]

   [optional footer(s)]
   EOF
   )"
   ```
   If a pre-commit hook fails, the commit did NOT happen. Fix the issue, re-stage, and create a NEW commit (never `--amend`, never `--no-verify`).

5. Report the result (see Output below).

## Conventional Commits format

`<type>[optional scope][!]: <description>`

- **type** (required): `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`, `revert`.
- **scope** (optional): noun in parens describing the area, e.g. `feat(parser):`.
- **description**: imperative, lowercase, no trailing period, ≤ ~72 chars.
- **body** (optional): blank line, then the *why*. Wrap at ~72 cols.
- **breaking change**: append `!` after type/scope AND/OR add footer `BREAKING CHANGE: <what broke>`.
- **footers** (optional): `Refs: #123`, `Reviewed-by: ...`.

`feat` → MINOR, `fix` → PATCH, `BREAKING CHANGE`/`!` → MAJOR (semver intent).

Pick `type` from what the staged diff actually does. If the diff mixes unrelated concerns, say so in your report — the user may want to split it — but still commit what is staged.

## Output

After committing, report (in Thai, per workspace preference — keep identifiers/paths in English):

- ✅ commit created
- **Hash**: short SHA (`git rev-parse --short HEAD`)
- **Message**: the full commit message
- **Branch**: current branch
- **Files**: count + names, with `+insertions / -deletions` (`git show --stat --oneline HEAD`)

If the staged set looked like it mixed concerns, add a one-line note suggesting a split next time.
