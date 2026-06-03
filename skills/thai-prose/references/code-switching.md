# Code-switching (Thai/English)

How to mix Thai and English. Thai is the structural language; English carries technical terms.
Migrated from CONTENT-GUIDE §1/§5 + kien-thai's four-bucket ทับศัพท์ and code-mix-at-noun (MIT).

### `thai-structure-english-terms` *(domain · scaler-explainer · hard)*

Thai carries grammar, connectives, and explanation. English carries technical terms that Thai
devs actually use.

- **Bad**: `เมื่อ traffic increase 10x, database ก็ cannot handle ต้อง add read replica เข้ามา to distribute load`
- **Good**: `พอ traffic เพิ่มขึ้น 10 เท่า database เดิมเริ่มรับไม่ไหว ต้องเพิ่ม read replica เข้ามาเพื่อกระจาย load`

English for: real dev terms (database, cache, deploy, scale, latency, throughput, QPS), proper
nouns (Redis, Kafka, Kubernetes), and terms that get worse when translated (trade-off, bottleneck,
overhead). Thai for: words devs already say in Thai (`ออกแบบ` not design, `เลือก` not choose),
all connectives/explanation, and every summary sentence.

### `code-mix-at-noun` *(domain · scaler-explainer · hard)*

Code-mix at the noun, not the verb. Keep a Thai verb and attach the English noun.

- **Bad**: `ทำการ deployment ของ code`
- **Good**: `deploy โค้ด` / `deploy code`

### `four-bucket-translit` *(domain · scaler-explainer · hard)*

Every technical term falls in one bucket. Pick one and **never mix buckets for the same term
within a document**:

1. **Keep English** — most dev terms: `cache`, `deploy`, `load balancer`, `replica`
2. **Transliterate** — terms with a settled Thai spelling in common speech: `เซิร์ฟเวอร์`
   (usually keep `server`), `คิว` (queue, sometimes)
3. **Translate** — words with a real Thai equivalent devs use: `ออกแบบ`, `เลือก`, `แก้ปัญหา`
4. **Translate + gloss once** — introduce a concept in Thai with the English in parentheses
   the first time: `การจำลองข้อมูล (replication)`, then use the English thereafter

Don't transliterate a word that has a normal Thai word (`important` → `สำคัญ`, not `อิมพอร์แทนต์`).
Don't translate a term devs only say in English (`cache` stays `cache`, not `หน่วยความจำแคช`).
