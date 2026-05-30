# Examples (before → tells → after)

Worked before/after pairs for editing. Format: the AI-shaped **Before**, the **Tells** it
trips (by slug), and the **After**. Anchored on scaler's reference voice — LearnAlgorithm's
*what-is-math* (Thai structure + English terms, problem-first, natural particles); the
anti-voice is DataRockie's blog tone (แอด/555/emoji), which the house voice bans.

> Note: this skill has no curated native-Thai corpus yet. These are illustrative, not corpus
> exemplars. Seed real ones from published lessons as they pass the linter; do not lift
> Claude-authored lesson output as a native anchor.

## 1 — bureaucratic open → problem-first

**Before**
> System Design คือกระบวนการออกแบบและวางโครงสร้างของระบบซอฟต์แวร์ขนาดใหญ่ โดยเฉพาะระบบที่ต้องจัดการข้อมูลจำนวนมาก

**Tells**: `no-bureaucratic-thai`, `problem-first-open`, `sentence-length`.

**After**
> พอระบบมี user หลักล้าน database เครื่องเดียวเริ่มรับไม่ไหว System Design คือการตอบคำถามว่าจะวางระบบยังไงให้มันไม่ล้มตอนคนเยอะ

## 2 — period spam + dangling clauses → space + ก็

**Before**
> ระบบทำงานเร็วขึ้น. ใช้ memory น้อยลง. ทีมพอใจมาก.

**Tells**: `rule-07-period`, frame `f3`, frame `f6`.

**After**
> ระบบทำงานเร็วขึ้น ใช้ memory น้อยลง ทีมก็พอใจ

## 3 — calqued connectives → native pivot

**Before**
> อย่างไรก็ตาม การใช้งานในระดับ production มีข้อจำกัดที่ต้องพิจารณา

**Tells**: frame `f7`, `empty-intensifier`.

**After**
> แต่พอเอาขึ้น production จริง ก็มีข้อจำกัดให้ปวดหัวอีกชุดนึง

## 4 — wrong code-mix → mix at the noun

**Before**
> เราจะทำการ deployment ของ service ใหม่ ๆ ในยุคปัจจุบัน

**Tells**: `code-mix-at-noun`, `rule-08-yamok`, forbidden `ในยุคปัจจุบัน`, `verbs-over-nouns`.

**After**
> เรา deploy service ใหม่ๆ ได้บ่อยขึ้น
