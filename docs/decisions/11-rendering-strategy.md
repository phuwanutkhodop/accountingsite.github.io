# 11 — Rendering strategy

**Ticket:** GitHub issue #11 (Wayfinder grilling)
**Date:** 5 October 2026
**Decided by:** the owner, in a grilling session with Claude. The owner delegated every technical choice to Claude ("I am not a coder or engineer — think these through rigorously"). Those choices are recorded in §3 with their reasons.
**Inputs:** decision #10 (content model), research #4 (browser publishing), #8 (multilingual SEO/AEO), #9 (design libraries)
**Status:** locked. **Amended 6 October 2026** after the plan review (`docs/reviews/2026-10-06-plan-review.md`): owner decision 2 refined by the owner (M8); §3.5 alt-text rule (L3); §3.10 image note (H5).

---

## 1. สรุปสำหรับเจ้าของกิจการ (ภาษาไทย)

1. **หน้าเว็บสร้างเสร็จตอนกด Publish:** ข้อความ เมนู รายการบทความ และข้อมูลสำหรับ Google และ AI อยู่ในไฟล์ HTML ครบตั้งแต่ต้น ถ้าปิด JavaScript เว็บก็ยังอ่านได้ครบ JavaScript ใช้แค่ส่วนเสริม เช่นกล่องค้นหา เครื่องคิดเลข ภาพเคลื่อนไหว และปุ่มส่งฟอร์ม
2. **ทุกครั้งที่กด Publish ระบบสร้างเว็บใหม่ทั้งหมด แต่ส่งขึ้นเฉพาะไฟล์ที่เปลี่ยนจริง** ก่อนยืนยัน คุณจะเห็นรายการว่าหน้าไหนจะเปลี่ยน
3. **ตรวจก่อนส่ง:** ถ้ามีลิงก์เสีย ช่องว่าง หรือข้อมูลไม่ครบ ปุ่ม Publish จะกดไม่ได้ และระบบบอกเป็นภาษาไทยว่าต้องแก้ตรงไหน
4. **ไม่มีเว็บพังครึ่ง ๆ:** ถ้าเกิดปัญหากลางทาง จะไม่มีอะไรถูกส่งขึ้น เว็บเดิมยังอยู่ครบ
5. **ภาษาที่เปิดใช้ต้องครบทุกภาษาก่อน Publish:** ถ้าภาษาที่เปิดใช้ภาษาใดยังว่าง จะ Publish หน้านั้นไม่ได้ งานจะเก็บเป็นฉบับร่างระหว่างรอแปล ปิดบางภาษาของเว็บได้ (เช่นเว็บทดสอบที่มีแค่อังกฤษ) แต่เว็บจริงของบริษัทเปิดครบสามภาษา *(เจ้าของปรับ 6 ต.ค. 2026)*
6. **วันที่บนหน้าภาษาไทยใช้ปีคริสต์ศักราช** เช่น 5 ตุลาคม 2026
7. **พรีวิวตรงกับของจริงทุกตัวอักษร** เพราะใช้เครื่องสร้างหน้าตัวเดียวกัน
8. **ปลอดภัยต่อของเดิม:** ระบบไม่แตะไฟล์ที่ตัวเองไม่ได้สร้าง หน้าเว็บที่เขียนด้วยมือในปัจจุบันจึงอยู่ครบจนกว่าจะย้ายเข้าระบบ (ตั๋ว #19)

---

## 2. Owner decisions

| # | Question | Decision | Why |
|---|---|---|---|
| 1 | Where pages are rendered | **Pre-rendered at publish time** (confirms decision #10 §2-1). Everything a person or a bot reads is in the HTML file: all text, navigation, article lists, language links, images, and all JSON-LD. **JavaScript may only add extras:** on-site search, calculators (extension slot), animations, the marquee, form submission. **Every generated page must be fully readable and navigable with JavaScript off.** | Most AI crawlers and link-preview fetchers (LINE, Facebook) do not run JavaScript (research #8 §AEO). |
| 2 | Missing translations | **Publishing requires every switched-on language** *(refined by the owner, 6 October 2026 — review M8; was "all three languages")*. A site can switch a language off in Settings (research #8 §4.5): a switched-off language generates nothing and appears nowhere, including hreflang. The firm's real site keeps EN + TH + ZH switched on, as locked on the map. An item (page or article) whose required text fields are empty in any switched-on language cannot be published. Publish is disabled, with a list of the missing fields by language. Work waits as a draft. Deliberate `hiddenIn` on a section (decision #10) is still allowed: hiding a section on purpose is not the same as a missing translation. | The owner wants every published item complete in all three languages. This also keeps the hreflang matrix complete on every page, with no special cases. |
| 3 | Year format on Thai pages | **Gregorian (ค.ศ.)**: `5 ตุลาคม 2026`. EN: `5 October 2026`. ZH: `2026年10月5日`. Machine-readable dates are ISO 8601 in `<time datetime>`, in JSON-LD and in sitemaps. | Owner choice. Answers research #8 open question 6.5. |

---

## 3. Technical decisions (delegated to Claude)

### 3.1 The generator is a pure function

- **Input:** a snapshot of *published* source (`site/` plus the pinned presets). Drafts are never read, except the item being published (decision #10).
- **Output:** a map of `path → file content`.
- **Inside it there is no clock, no network, no randomness and no browser- or locale-dependent API.** The same input always gives byte-identical output.
- The same module runs in three places: the Admin's live preview, the Publish step, and Node, for automated tests (golden-file tests: fixed source in, expected HTML out).
- **Preview is therefore exactly what gets published.**

### 3.2 Determinism rules

These rules exist so that a page whose content has not changed produces an identical file, which keeps "what changed" lists and history honest.

- UTF-8 without BOM, LF line endings, one final newline.
- Stable ordering everywhere: object keys in JSON-LD, lists, sitemap entries, attributes.
- **No publish time and no commit SHA inside pages.** This overrides research #4 §2.4 L3, which proposed a per-page build `<meta>`. The "is it live yet?" marker moves to one small file, `build.json`, written on every publish.
- `dateModified`, sitemap `<lastmod>` and visible "updated" dates come from **content dates stored in the source**. The Admin sets them when the content itself changes; they are never derived from publish time.
- **Dates and numbers are formatted from fixed tables in the generator, not with `Intl`.** `Intl` output varies across browsers and versions, and `th-TH` defaults to the Buddhist calendar, which would silently contradict owner decision 3.

### 3.3 Full regeneration, minimal commit

1. Generate the whole site in memory (estimated 1–2 s for ~700 output files).
2. Read the current tree in one call (`GET /git/trees/{sha}?recursive=1`).
3. Compute each generated file's git blob SHA-1 locally (`blob <len>\0<bytes>`, SubtleCrypto) and compare it with the tree.
4. Send **only paths whose SHA differs**: text inline in `POST /git/trees`, binaries as blobs (concurrency ≤ 5), using research #4's one-commit sequence.

Incremental "regenerate only dependent pages" is rejected: one missed dependency leaves a page silently stale. Full regeneration cannot miss one.

### 3.4 Ownership manifest — never touch what the generator did not make

- Each publish writes **`generated.json`**, listing every output path with its blob SHA.
- **Deletions** apply only to paths in the previous manifest that are no longer produced (for example a page that was removed).
- **Collision guard:** if a new output path already exists in the repo but is not in the manifest, Publish is **blocked**. This protects the current hand-written pages, `CNAME`, `admin/` and anything else made outside the generator. Migration (#19) hands paths over explicitly.
- **Hand-edit detection:** if a path in the manifest no longer has the SHA recorded there, someone edited generated output by hand. The Admin shows this and overwrites only after the owner confirms.

### 3.5 Validation gate (runs before every publish)

**Errors block Publish.** Each is shown in plain Thai, linked to the field to fix:

- a required field is empty in any of the three languages (owner decision 2)
- an internal link points to a page that will not exist
- a duplicate slug within one language
- an absolute internal path (project rule: relative only)
- hreflang pairs that are not reciprocal, or a canonical that is not self-referencing (research #8)
- JSON-LD that does not parse, or lacks the fields required for its type
- an image without alt text in any switched-on language, unless the image is flagged **decorative** (empty `alt`, research #7) *(amended — review L3)*
- a page without `<title>` or meta description
- leftover placeholders such as `example.com`, `Your Firm Name` or `hello@yourfirm.com`

**Warnings inform but do not block:**

- title or description length outside recommended ranges
- a large page weight
- a preset version marked deprecated

### 3.6 Atomic and safe under concurrency

- Nothing is sent until every file has been generated and validated.
- Only the final `PATCH /git/refs/heads/main` with `force: false` makes anything visible (research #4).
- If another device published in between, the update is rejected. The Admin re-reads, regenerates, re-diffs, and shows the change list again if it differs.
- Dangling objects from an interrupted publish are harmless.

### 3.7 Reading source efficiently (answers decision #10 §4 open detail)

- **No separate article index is kept as source.** The Admin keeps a local IndexedDB cache of source files keyed by git blob SHA.
- One recursive tree call shows which source files changed, and only those are downloaded. A new device downloads everything once: ~300 requests for a large site, well inside the 5,000/hour limit.
- On the **output** side, a per-language article list is generated as a runtime extra for on-site search, if search is in v1 (taxonomy and search are still unspecified on the map).

### 3.8 Templates are logic-less

- Preset markup uses a **logic-less, Mustache-compatible subset**: variables, sections/loops and conditionals only, with no arbitrary code.
- **Every value is HTML-escaped by default.**
- Rich text (article bodies) enters only through one dedicated slot that is sanitised against a whitelist. The sanitiser is owned by #16.
- Consequence: a preset from the library cannot run script or break page structure. This is the main defence against XSS in the Admin's own origin (research #4 §security). Presets also stay portable JSON.
- The concrete library, or a small in-house engine with that syntax, is chosen in #16.

### 3.9 Output format

- Readable, not minified. Pages compresses responses; readable files keep history diffs and rollback reviews understandable.
- Each file carries a header comment: *generated by the Admin; do not edit directly* (decision #10).
- `<html lang>` is `en`, `th` or `zh-Hans`, matching the hreflang codes in research #8.
- Per-language font loading follows #15. `/zh/` pages must not depend on Google Fonts for first render (research #8 checklist).

### 3.10 Scale limits (checked, not a concern)

- The recursive tree read truncates at 100,000 entries or 7 MB; this site will have a few thousand files at most.
- Write limits (80 content-creating requests per minute, 500 per hour) matter only for binaries. *Amended (review H5):* image renditions are **not** in the public repo before Publish. They wait in the private drafts repo, and Publish copies them into `media/`. Uploads to the drafts repo are throttled and can resume after an interruption (#27).
- Revisit only if output exceeds ~5,000 files.

---

## 4. Effects on other tickets

- **#12 Admin IA:** the Publish screen holds the change list (§3.3) and the validation report (§3.5). The editor shows each item's per-language completeness.
- **#13 Design Library governance:** presets must be logic-less templates (§3.8).
- **#14 Site Structure:** the link and slug checks in §3.5 run against the page tree and redirects defined there.
- **#16 Tech stack:** the generator must run unchanged in the browser and in Node (§3.1). #16 also chooses the template engine and the rich-text sanitiser (§3.8).
- **#17 Drafts, versions, rollback:** decision 2 means untranslated work lives as drafts, so drafts UX matters more. Whole-site rollback restores `generated.json` along with the files, which keeps them consistent.
- **#19 Migration:** existing pages are protected by the collision guard (§3.4) until migration explicitly hands each path to the generator. `core/article-loader.js` runtime rendering and JSON-LD injection are retired page by page as pages move.
- **#20 Token task:** the end-to-end proof should include the tree read, the local blob-SHA diff and a fast-forward-only ref update.
- **Map, "Not yet specified":** "how untranslated pages behave" is now answered (publishing requires all three). Who writes TH/ZH and whether machine-assist is offered remain open.

---

## 5. Not decided here (deliberately)

- Template engine library and HTML sanitiser → #16.
- What the Publish and "what changed" screens look like → #12 / #17.
- On-site search and article taxonomy → still on the map's "Not yet specified".
- Who translates, machine-assist, and flagging a translation that is out of date after the source language changes → translation workflow (map, "Not yet specified").
