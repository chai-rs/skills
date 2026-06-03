"""Golden-file assertions for the linter, including MDX skip-zone negatives."""

from __future__ import annotations

from pathlib import Path

from lint_thai_content import lint, load_blocklist

FIX = Path(__file__).parent / "fixtures"
BLOCKLIST = load_blocklist()


def _rules(name: str, severity: str | None = None) -> set[str]:
    fs = lint(str(FIX / name), BLOCKLIST)
    return {f.rule for f in fs if severity is None or f.severity == severity}


def test_clean_has_no_errors():
    assert _rules("clean.th.mdx", "error") == set()


def test_dirty_flags_core_rules():
    assert {"rule-08-yamok", "rule-07-period", "forbidden-phrase"} <= _rules("dirty.th.mdx")


def test_skipzones_has_no_errors():
    # decimals, KaTeX, fenced code, <Callout>, and a §7-violating blockquote
    # must all be masked — none may produce an error finding.
    assert _rules("skipzones.th.mdx", "error") == set()


def test_blocklist_loads():
    assert "ในยุคปัจจุบัน" in BLOCKLIST
    assert "555" in BLOCKLIST
