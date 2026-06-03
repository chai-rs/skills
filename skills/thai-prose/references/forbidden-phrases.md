# Forbidden phrase blocklist

Mechanically grep-able blocklist of phrases that mark AI-generated or off-voice Thai
prose. They must never appear **as use** (in the model's own prose). Some entries are
universal across every register; some are scaler-house bans (slang) that only matter for
the lesson register — but the linter treats the whole list uniformly, and none of these
belong in good prose anywhere, so the union is safe to enforce everywhere.

The linter (`scripts/lint_thai_content.py`) parses the `## Blocklist` section directly —
this `.md` is the single source, there is no separate JSON.

## Use vs mention

A phrase may appear as **mention** when wrapped in backticks, inside a fenced code block,
or inside a `>` blockquote — e.g. when a reference file or `examples.md` discusses the
pattern itself. The linter masks those regions, so only **un-backticked** prose
occurrences are flagged.

## Format

One forbidden phrase per list item. The forbidden token is the **first** backticked
string, before any `→`. Anything after `→` is a human-facing suggestion and is **not**
parsed as forbidden. For "both forms banned", use two separate list items.

## Blocklist

- `ในยุคปัจจุบัน`
- `ในโลกปัจจุบัน`
- `ในโลกที่`
- `เป็นที่ทราบกันดีว่า`
- `เป็นที่รู้กันว่า`
- `ปฏิเสธไม่ได้ว่า`
- `เป็นสิ่งสำคัญที่ต้องตระหนัก`
- `มีความสำคัญ` → ใช้ `สำคัญ`
- `ในเรื่องของ`
- `ในส่วนของ`
- `อย่างมหาศาล`
- `โดยสรุปแล้ว`
- `กล่าวโดยสรุป`
- `นั่นเอง!`
- `สำคัญกว่าเดิมหลายเท่า`
- `เปลี่ยนเกม`
- `555`
- `โคตร`
- `ปังมาก`
- `จัดไป`
- `แอด`

## Patterns (judgment — not literal-matched by the linter)

These carry an ellipsis or are register-scoped, so the linter can't grep them literally.
Catch them by eye in the self-edit pass.

- `การที่...นั้น` — heavy nominalized topic (Frame 1); rewrite topic-comment.
- `รีบ...เลย!` — imperative product-CTA bang. Banned in body copy; allowed once per piece
  in Marketing register only, scoped per `cta-bang` (see `register.md`).
