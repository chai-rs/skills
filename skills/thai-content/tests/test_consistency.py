r"""Slug consistency for the thai-content reference files.

Each rule has a heading `### \`<slug>\` *(<type> · <scope> · <strictness>)*`.
Slugs must be unique across all skill files. Rule-citation cross-refs
(`rule-NN-...`) and frame refs (`f1`..`f7`) must resolve.

Adapted from chakrit/kien-thai (MIT): the cross-ref matcher is restricted to
`rule-NN` and `fN` forms so it does NOT false-positive on the many hyphenated
technical terms (e.g. `read-replica`, `load-balancer`) that legitimately appear
backticked in system-design content."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL_FILES = [ROOT / "SKILL.md"] + sorted((ROOT / "references").glob("*.md"))

SLUG_DEFN_RE = re.compile(r"^###\s+`([a-z0-9][a-z0-9/_-]*)`\s+\*\([^)]+\)\*\s*$", re.M)
SLUG_REF_RE = re.compile(r"`(f[1-7](?:/[a-z][a-z0-9-]*)?|rule-\d+[a-z0-9-]*)`")
FRAME_UMBRELLA = {f"f{n}" for n in range(1, 8)}


def _definitions() -> dict[str, list[Path]]:
    slugs: dict[str, list[Path]] = {}
    for f in SKILL_FILES:
        for m in SLUG_DEFN_RE.finditer(f.read_text("utf-8")):
            slugs.setdefault(m.group(1), []).append(f)
    return slugs


def test_skill_files_exist():
    assert (ROOT / "SKILL.md").exists()
    assert SKILL_FILES


def test_slug_uniqueness():
    dups = {s: [p.name for p in paths] for s, paths in _definitions().items() if len(paths) > 1}
    assert not dups, f"duplicate slug definitions: {dups}"


def test_rule_and_frame_refs_resolve():
    defined = set(_definitions()) | FRAME_UMBRELLA
    missing: list[str] = []
    for f in SKILL_FILES:
        for line_no, line in enumerate(f.read_text("utf-8").splitlines(), start=1):
            if SLUG_DEFN_RE.match(line):
                continue
            for m in SLUG_REF_RE.finditer(line):
                if m.group(1) not in defined:
                    missing.append(f"{f.name}:{line_no}: `{m.group(1)}`")
    assert not missing, "orphan rule/frame cross-refs:\n  " + "\n  ".join(missing)
