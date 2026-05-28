---
name: commity-push
description: Create a single git commit from already-staged changes using a Conventional Commits message, then push to the remote and report the result. Use when the user runs /commity-push or asks to commit staged changes and push following the conventional commits spec. Use commity (no push) when the user only wants to commit.
---

# commity-push

Commit **only what is already staged** with a [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) message, then **push** to the remote, then report. Never stages, never amends, never uses `--no-verify`, never `--force`.

## Process

1. Run these in parallel to understand state:
   - `git status` — staged vs unstaged vs untracked.
   - `git diff --staged` — exact changes to commit.
   - `git log -n 10 --oneline` — match existing message style/scopes.
   - `git rev-parse --abbrev-ref HEAD` — current branch.

2. **Gate on staged content.** If `git diff --staged` is empty:
   - STOP. Do not run `git add`, do not commit, do not push.
   - Show `git status` and tell the user to stage files first, then re-run `/commity-push`.

3. Compose a Conventional Commits message from the staged diff (format below). Reuse scopes from `git log`; do not invent prefixes.

4. Commit via HEREDOC:
   ```bash
   git commit -m "$(cat <<'EOF'
   <type>[optional scope]: <description>

   [optional body]

   [optional footer(s)]
   EOF
   )"
   ```
   If a pre-commit hook fails, the commit did NOT happen. Fix, re-stage, create a NEW commit (never `--amend`, never `--no-verify`).

5. **Push** (only after the commit succeeds):
   - Detect upstream: `git rev-parse --abbrev-ref --symbolic-full-name @{u}` (non-zero exit = no upstream).
   - No upstream → `git push -u origin <current-branch>`.
   - Has upstream → `git push`.
   - NEVER `--force` / `--force-with-lease`. NEVER `--no-verify`.
   - If the branch is `main`/`master`, a normal (non-force) push is fine; still never force.
   - If push is rejected (non-fast-forward), STOP and report — do not force or reset. Tell the user to pull/rebase first.

6. Report the result (see Output below).

## Conventional Commits format

`<type>[optional scope][!]: <description>`

- **type** (required): `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`, `revert`.
- **scope** (optional): area noun in parens, e.g. `fix(auth):`.
- **description**: imperative, lowercase, no trailing period, ≤ ~72 chars.
- **body** (optional): blank line then the *why*, wrapped ~72 cols.
- **breaking change**: `!` after type/scope AND/OR footer `BREAKING CHANGE: <what>`.

Pick `type` from what the staged diff does. If it mixes unrelated concerns, note it in the report.

## Output

After commit + push, report (in Thai, per workspace preference — keep identifiers/paths in English):

- ✅ commit + push done
- **Hash**: short SHA
- **Message**: full commit message
- **Branch**: current branch
- **Files**: count + names with `+ins / -del` (`git show --stat --oneline HEAD`)
- **Remote**: target remote/branch, and whether upstream was newly set (`-u`)
- **Pushed range**: e.g. `abc123..def456` from the push output

If the push failed or was rejected, report the exact reason and the safe next step (pull/rebase) — do not attempt force or reset.
