# AI tells

Patterns that read as machine-written. Migrated from CONTENT-GUIDE §9 + kien-thai's ai-tells
and the surviving craft rules (MIT). Most are judgment-tier; the grep-able phrase tells live
in `forbidden-phrases.md` (linter).

### `bullet-pattern-repetition` *(ai-tell · scaler-explainer · hard)*

A 5+ item bullet/numbered list where every item opens with the same structure.

- **Tell**: `1. AI Agent คือ... 2. Inference cost คือ... 3. ส่วนประกอบที่... 4. Interview เริ่ม...`
- **Fix**: vary structure, or fold into narrative prose.

### `definition-then-simplify` *(ai-tell · scaler-explainer · hard)*

`X คือ <formal def> พูดให้เข้าใจง่าย X ก็คือ <plain>`. If you can say it plainly, start there.

### `relist-recap` *(ai-tell · scaler-explainer · hard)*

A closing `Key Takeaways` / `โดยสรุปแล้ว` that just re-lists every subheading. Takeaways must
be 3 *actionable* lines that add something, not a table of contents. The recap phrasings
(`โดยสรุปแล้ว`, `กล่าวโดยสรุป`) are in `forbidden-phrases.md`.

### `hyperbole` *(ai-tell · scaler-explainer · hard)*

`สำคัญกว่าเดิมหลายเท่า`, `ช็อก`, `เปลี่ยนเกม`. Lowers credibility. In `forbidden-phrases.md`.

### `empty-intensifier` *(craft · scaler-explainer · soft)*

Intensifiers that add no information: `อย่างมาก`, `เป็นอย่างยิ่ง`, `อย่างมหาศาล`. Cut, or
replace with a concrete number.

### `concrete-cases` *(craft · scaler-explainer · soft)*

Real-world examples should say *what happened and why*, not just name-drop. `Netflix ใช้แบบนี้`
→ `Netflix เจอ thundering herd ตอน cache หมดอายุพร้อมกัน เลยใส่ jitter ใน TTL`.

### `positive-capability` *(craft · scaler-explainer · soft)*

State what the system does, not vague reassurance. `ระบบนี้ช่วยให้ดีขึ้น` → `ระบบนี้ตัด p99
latency จาก 2s เหลือ 200ms`.
