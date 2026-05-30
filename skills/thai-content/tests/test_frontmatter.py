"""SKILL.md frontmatter must be strict-parseable YAML.

The skills CLI parses name/description with a strict YAML parser. A bare
colon-space inside an unquoted scalar (e.g. `TRIGGER when: ...`) is illegal YAML
and silently breaks skill discovery. This guards against that class of bug.
Ported from chakrit/kien-thai (MIT)."""

from __future__ import annotations

from pathlib import Path

import yaml

SKILL_MD = Path(__file__).resolve().parent.parent / "SKILL.md"


def _frontmatter(text: str) -> str:
    assert text.startswith("---\n"), "SKILL.md must open with a `---` frontmatter fence"
    return text[4:text.index("\n---", 4)]


def test_skill_md_exists():
    assert SKILL_MD.exists(), SKILL_MD


def test_frontmatter_is_strict_yaml():
    data = yaml.safe_load(_frontmatter(SKILL_MD.read_text("utf-8")))
    assert isinstance(data, dict), "frontmatter must parse to a mapping"
    for key in ("name", "description"):
        assert data.get(key), f"frontmatter missing non-empty `{key}`"
