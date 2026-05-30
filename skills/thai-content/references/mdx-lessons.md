# MDX lessons (structure + components)

Domain rules for scaler lesson MDX. Migrated from CONTENT-GUIDE Lesson Structure, Callout
Conventions, Worked-Example, Frontmatter, MDX Components, and bilingual parallelism.

Files live at `content/modules/<NN>-<module-slug>/<NN>-<lesson-slug>.<lang>.mdx`, paired
`.th.mdx` + `.en.mdx`, with a module `meta.json` listing `pages` in order.

### `mdx-frontmatter` *(domain · scaler-explainer · hard)*

Every file opens with YAML frontmatter: `title` (in the file's language) and `locked`
(`false` free / `true` paid).

### `problem-first-open` *(domain · scaler-explainer · hard)*

Open each lesson/section from a problem or question, not a definition. The reader doesn't
care about the definition until they see it's about them. See `style-rules.md`
`stacked-question-open`.

### `lesson-structure` *(domain · scaler-explainer · hard)*

Narrative and technical content alternate — not code block after code block. Every code
block, number, or diagram gets a Thai sentence before and after explaining *why*, not just
*what*. One analogy per hard concept (not every paragraph); if the analogy breaks down, say so.

### `numbers-carry-context` *(domain · scaler-explainer · hard)*

A bare number means nothing. `34,722 QPS` needs `MySQL single node รับได้ ~5,000 QPS เลยต้อง
shard อย่างน้อย 7 เครื่อง`.

### `worked-example` *(domain · scaler-explainer · hard)*

Worked examples are a story that walks one step at a time, not a formula dump. Start from a
known number, derive the next, and after each result say what it tells you (see
`numbers-carry-context`).

### `callout-component` *(domain · scaler-explainer · hard)*

Use the JSX `<Callout>` component, never a markdown `> 💡` blockquote (the linter errors on
blockquote-as-callout). Four kinds:

- `type="idea"` title `"Tips"` — non-obvious insight
- `type="warning"` — a mistake that actually costs you
- `type="info"` — extra context / cross-reference
- no `type` — a real-world data point (title `"Fun Fact"`)

Max 3 per section; callouts support the narrative, they don't replace it.

### `lesson-takeaways` *(domain · scaler-explainer · hard)*

Close with `## Key Takeaways` or `## ถ้าจำได้แค่ 3 อย่าง` — pick one and stay consistent within
a module (the linter warns on mixed headings). 3 actionable lines, **bold**-led, not a relist
of every subheading (see `ai-tells.md` `relist-recap`).

### `lesson-handoff` *(domain · scaler-explainer · soft)*

If the lesson connects forward, close with `<LessonHandoff>` linking the next lesson. Other
registered components: `<ScreamText>` (thesis statement), `<ProcessFlow>`, `<Mermaid>`, and
sketch components — check `components/content/` before inventing one.

### `th-en-parallel` *(domain · scaler-explainer · hard)*

`.th.mdx` and `.en.mdx` keep parallel structure — same sections, same order. If EN has
Real-World or Practice Questions, TH has them too. The linter cross-checks heading count/order
and named-section presence (warn). When writing TH, read the EN twin for structure — never
translate its prose.
