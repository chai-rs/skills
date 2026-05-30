#!/usr/bin/env python3
"""Thai-content linter for scaler-client lesson MDX.

Mechanical checks keyed to thai-content reference rule slugs. MDX-aware: masks
frontmatter, code fences, KaTeX, inline code, JSX tags, and blockquotes before
running prose checks, so the linter never flags code samples, math, or
use-vs-mention quotes.

Usage:
    uv run python scripts/lint_thai_content.py "content/modules/**/*.th.mdx"

Exit code 1 if any `error` finding; `warn` findings print but do not fail.
"""

from __future__ import annotations

import glob
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

THAI = r"฀-๿"
YAMOK = "ๆ"  # ๆ
SKILL_DIR = Path(__file__).resolve().parent.parent
CALLOUT_EMOJI = "💡⚠️📝ℹ️🔥✅❗️"


@dataclass
class Finding:
    path: str
    line: int
    rule: str
    severity: str
    msg: str


# --- MDX masking: blank protected spans, preserve offsets -------------------

_MASKS = [
    re.compile(r"\A---\n.*?\n---\n", re.S),       # YAML frontmatter
    re.compile(r"^```.*?^```", re.S | re.M),      # code / ```mermaid fences
    re.compile(r"\$\$.*?\$\$", re.S),             # KaTeX block
    re.compile(r"\$[^$\n]+\$"),                   # KaTeX inline
    re.compile(r"`[^`]*`"),                       # inline code
    re.compile(r"<[A-Za-z][^>]*>"),               # JSX opening/self-closing tags
    re.compile(r"^>.*$", re.M),                   # blockquote (use-vs-mention exempt)
]


def _blank(m: re.Match) -> str:
    return re.sub(r"\S", " ", m.group(0))


def mask(text: str) -> str:
    for rx in _MASKS:
        text = rx.sub(_blank, text)
    return text


def _line(text: str, idx: int) -> int:
    return text.count("\n", 0, idx) + 1


def _paragraphs(masked: str):
    pos = 0
    for block in re.split(r"\n[ \t]*\n", masked):
        yield pos, block
        pos += len(block) + 2


# --- blocklist (single source: references/forbidden-phrases.md) -------------

def load_blocklist() -> list[str]:
    md = (SKILL_DIR / "references" / "forbidden-phrases.md").read_text("utf-8")
    section = md.split("## Blocklist", 1)[-1]
    out: list[str] = []
    for line in section.splitlines():
        line = line.strip()
        if not line.startswith("- "):
            continue
        head = line.split("→", 1)[0]  # forbidden token sits before the arrow
        m = re.search(r"`([^`]+)`", head)
        if m:
            out.append(m.group(1))
    return out


# --- ERROR checks -----------------------------------------------------------

_YAMOK_RE = re.compile(r"\s" + YAMOK)
_PERIOD_RE = re.compile(r"[" + THAI + r"][\"')\]]*[ \t]*\.(?=\s|$)", re.M)
_BLOCKQUOTE_CALLOUT_RE = re.compile(r"^>\s*[" + CALLOUT_EMOJI + r"]", re.M)
_TRAILING_THAI_RE = re.compile(r"[" + THAI + r".]+$")

# Thai abbreviations legitimately end in '.', like English etc./e.g.
_THAI_ABBREV = {
    "น.", "ชม.", "วิ.", "กม.", "ซม.", "มม.", "กก.", "บ.", "ดร.",
    "จ.", "อ.", "ต.", "ม.", "พ.ศ.", "ค.ศ.", "น.ส.", "ฯพณฯ",
    # month abbreviations
    "ม.ค.", "ก.พ.", "มี.ค.", "เม.ย.", "พ.ค.", "มิ.ย.",
    "ก.ค.", "ส.ค.", "ก.ย.", "ต.ค.", "พ.ย.", "ธ.ค.",
}


def check_yamok(masked: str, raw: str, path: str):
    for m in _YAMOK_RE.finditer(masked):
        yield Finding(path, _line(raw, m.start()), "rule-08-yamok", "error",
                      "space before ๆ — attach the ไม้ยมก to the repeated word")


def check_period(masked: str, raw: str, path: str):
    for m in _PERIOD_RE.finditer(masked):
        token = _TRAILING_THAI_RE.search(raw[:m.end()])
        if token and token.group(0) in _THAI_ABBREV:
            continue
        yield Finding(path, _line(raw, m.start()), "rule-07-period", "error",
                      "Thai clause ends with '.' — use a space or newline instead")


def check_blockquote_callout(masked: str, raw: str, path: str):
    for m in _BLOCKQUOTE_CALLOUT_RE.finditer(raw):
        yield Finding(path, _line(raw, m.start()), "callout-component", "error",
                      "markdown blockquote used as a callout — use <Callout type=...>")


def check_blocklist(masked: str, raw: str, path: str, blocklist: list[str]):
    for phrase in blocklist:
        for m in re.finditer(re.escape(phrase), masked):
            yield Finding(path, _line(raw, m.start()), "forbidden-phrase", "error",
                          f"AI-tell / banned phrase: {phrase}")


# --- WARN checks ------------------------------------------------------------

_OTHER_SCRIPT_RE = re.compile(
    r"[一-鿿가-힯؀-ۿЀ-ӿऀ-ॿ"
    r"\U0001f000-\U0001faff]"
)


def check_emdash_density(masked: str, raw: str, path: str):
    for pos, block in _paragraphs(masked):
        if block.count("—") > 2:
            yield Finding(path, _line(raw, pos), "rule-06-emdash", "warn",
                          ">2 em-dashes in one paragraph — prefer Thai connectives (§6)")


def check_callout_count(masked: str, raw: str, path: str):
    sections = re.split(r"^##\s", raw, flags=re.M)
    for i, sec in enumerate(sections):
        if sec.count("<Callout") > 3:
            yield Finding(path, 1, "callout-count", "warn",
                          f"section {i} has >3 <Callout> — callouts are supporting, not primary")


def check_script_leakage(masked: str, raw: str, path: str):
    for m in _OTHER_SCRIPT_RE.finditer(masked):
        yield Finding(path, _line(raw, m.start()), "script-leakage", "warn",
                      f"non-Thai/Latin character: {m.group(0)!r} (only Thai + English allowed)")


_HEADING_RE = re.compile(r"^(#{2,3})\s+(.*)$", re.M)
_NAMED_SECTIONS = ("Real-World", "Practice Questions", "Key Takeaways")


def check_parity(path: str):
    if not path.endswith(".th.mdx"):
        return
    en = Path(path.replace(".th.mdx", ".en.mdx"))
    if not en.exists():
        return
    th_text = Path(path).read_text("utf-8")
    en_text = en.read_text("utf-8")
    th_h = [m.group(2).strip() for m in _HEADING_RE.finditer(th_text)]
    en_h = [m.group(2).strip() for m in _HEADING_RE.finditer(en_text)]
    if len(th_h) != len(en_h):
        yield Finding(path, 1, "th-en-parity", "warn",
                      f"heading count differs from EN twin: th={len(th_h)} en={len(en_h)}")
    for name in _NAMED_SECTIONS:
        in_en = any(name.lower() in h.lower() for h in en_h)
        in_th = any(name.lower() in h.lower() for h in th_h)
        if in_en and not in_th:
            yield Finding(path, 1, "th-en-parity", "warn",
                          f"EN has a '{name}' section but TH does not")


_PER_FILE = [
    check_yamok, check_period, check_blockquote_callout,
    check_emdash_density, check_callout_count, check_script_leakage,
]


def lint(path: str, blocklist: list[str]) -> list[Finding]:
    raw = Path(path).read_text("utf-8")
    masked = mask(raw)
    findings: list[Finding] = []
    for check in _PER_FILE:
        findings.extend(check(masked, raw, path))
    findings.extend(check_blocklist(masked, raw, path, blocklist))
    findings.extend(check_parity(path))
    return findings


# --- module-scoped checks ---------------------------------------------------

_TAKEAWAY_HEADINGS = ("Key Takeaways", "ถ้าจำได้แค่ 3 อย่าง")


def lint_module(module_dir: Path) -> list[Finding]:
    findings: list[Finding] = []
    meta = module_dir / "meta.json"
    if meta.exists():
        pages = json.loads(meta.read_text("utf-8")).get("pages", [])
        for slug in pages:
            if not (module_dir / f"{slug}.th.mdx").exists():
                findings.append(Finding(str(meta), 1, "meta-pages", "warn",
                                        f"meta.json lists '{slug}' but {slug}.th.mdx is missing"))
    used = set()
    for f in module_dir.glob("*.th.mdx"):
        text = f.read_text("utf-8")
        for h in _TAKEAWAY_HEADINGS:
            if re.search(r"^##\s+" + re.escape(h), text, re.M):
                used.add(h)
    if len(used) > 1:
        findings.append(Finding(str(module_dir), 1, "key-takeaways", "warn",
                                f"module mixes takeaway headings {sorted(used)} — pick one"))
    return findings


def main(argv: list[str]) -> int:
    patterns = argv or ["content/modules/**/*.th.mdx"]
    paths = sorted({p for pat in patterns for p in glob.glob(pat, recursive=True)})
    blocklist = load_blocklist()
    findings: list[Finding] = []
    for p in paths:
        findings.extend(lint(p, blocklist))
    for module_dir in sorted({Path(p).parent for p in paths}):
        if (module_dir / "meta.json").exists():
            findings.extend(lint_module(module_dir))
    findings.sort(key=lambda f: (f.path, f.line, f.severity))
    for f in findings:
        print(f"{f.severity.upper():5} {f.path}:{f.line} [{f.rule}] {f.msg}")
    errors = sum(1 for f in findings if f.severity == "error")
    warns = sum(1 for f in findings if f.severity == "warn")
    print(f"\n{len(paths)} file(s) · {errors} error · {warns} warn")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
