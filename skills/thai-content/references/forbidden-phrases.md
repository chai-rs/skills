# Forbidden phrase blocklist

Phrases that mark AI-generated or off-voice Thai. They must never appear **as use**
in lesson prose. The linter (`lint_thai_content.py`) parses the `## Blocklist`
section directly — this `.md` is the single source, there is no separate JSON.

## Use vs mention

A phrase may appear as **mention** when wrapped in backticks, inside a fenced code
block, or inside a `>` blockquote — e.g. when a reference file or `examples.md`
discusses the pattern itself. The linter masks those regions, so only **un-backticked**
prose occurrences are flagged.

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
