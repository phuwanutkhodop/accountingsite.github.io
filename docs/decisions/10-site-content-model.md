# 10 — Content model and file layout of a site

**Ticket:** GitHub issue #10 (Wayfinder grilling)
**Date:** 5 October 2026
**Decided by:** the owner, in a grilling session with Claude
**Inputs:** research #3 (CMS landscape), #4 (browser publishing), #7 (images), #8 (multilingual SEO), #9 (design libraries)
**Status:** locked. **Amended 6 October 2026** after the plan review (`docs/reviews/2026-10-06-plan-review.md`): the robots claim (M15), article file names (M1, via #14), image renditions before Publish (H5).
**Amended 6 October 2026 by #31** (`docs/decisions/31-multi-site-hosting.md`): `admin/` and `library/` leave the site repo — the Admin runs from its own origin and the library has its own repo; the drafts repo is one per site; decision 8 stores a 4096 px **master** instead of the raw original.
**Amended 6 October 2026 by #21** (`docs/decisions/21-section-library-sample.md` §2-4): the colour-mode override in decision 5a is now the section **tone** `plain / tinted / bold`; the site's colour scheme is light / dark / follow-device (review M16).

---

## 1. สรุปสำหรับเจ้าของกิจการ (ภาษาไทย)

1. **แยกสองชั้น:** Admin แก้ "ต้นฉบับ" (ไฟล์ข้อมูล) เวลากด Publish จะประกอบหน้าเว็บ HTML ที่สมบูรณ์ให้ แล้วส่งขึ้นพร้อมกันใน commit เดียว Google และบอท AI จึงเห็นหน้าเว็บครบ
2. **ต้นฉบับแยกหลายไฟล์:** ตั้งค่าเว็บ · ธีม · 1 ไฟล์ต่อหน้า · 1 ไฟล์ต่อบทความ · สำเนาดีไซน์ · ดัชนีรูป
3. **สามภาษาเก็บคู่กัน** ในไฟล์เดียวของแต่ละหน้า โครงหน้าใช้ร่วมกัน และมีสวิตช์ "ซ่อน section นี้ในภาษา…"
4. **ลงบทความ:** ต้นฉบับเปลี่ยนแค่ไฟล์บทความ (และดัชนีรูปถ้ามีรูปใหม่) หน้ารวมบทความ หน้าแรก และ sitemap ให้ Admin ประกอบใหม่อัตโนมัติ
5. **ผูกดีไซน์ + ล็อกเวอร์ชัน:** หน้าคงเดิมจนเจ้าของกดอัปเกรด ห้ามลบดีไซน์ที่ยังมีหน้าใช้อยู่ ทำได้แค่ติดป้าย "เลิกใช้"
6. **ปรับเฉพาะหน้า:** ปรับในช่องที่ดีไซน์อนุญาต ถ้าเกินกว่านั้นให้เป็น "ดีไซน์เฉพาะหน้า" ที่ซ่อนจากคลัง **ไม่มีการตัดลิงก์**
7. **คลังแม่ + สำเนา:** ดีไซน์ใหม่เข้าคลังแม่ที่เดียว แต่ละเว็บเก็บสำเนาเฉพาะดีไซน์และเวอร์ชันที่ใช้อยู่ เว็บจึงยังครบในตัว
8. **ฉบับร่าง:** บันทึกในเครื่องอัตโนมัติ และกด "บันทึกร่าง" เพื่อเก็บใน **repo ส่วนตัว** แยกต่างหาก repo สาธารณะจะมีแค่สิ่งที่ Publish แล้ว
9. **รูปต้นฉบับ:** เก็บใน repo ส่วนตัว (ไฟล์ละไม่เกิน 12 MB มีแถบบอกพื้นที่) บนเว็บมีแค่ไฟล์ที่ย่อแล้ว

---

## 2. Decisions

| # | Question | Decision | Why |
|---|---|---|---|
| 1 | Source vs output | **Two layers.** The Admin edits *source* data files; on Publish it generates complete static HTML in the browser and commits source + output in **one atomic commit** (Git Data API, research #4). JavaScript only powers runtime extras (search, calculators). | Only option that gives a growing design library, trilingual consistency and full SEO/AEO. Research #8 requires static JSON-LD; JS-rendered pages are invisible to most AI crawlers and link previewers. |
| 2 | One file vs split | **Split files** (layout in §3). | Publishing an article adds one file; per-page history works via `GET /commits?path=`; small files load fast; a broken file breaks one page, not the site. |
| 3 | Per-language text | **Side-by-side in one file per page:** every text field is `{ "en": …, "th": …, "zh": … }`. Page structure is shared across languages; each section instance may carry `hiddenIn: ["th"]`. Text in each language is written freely, not forced to be a literal translation. | One structure = mechanical hreflang, visible missing translations, no structural drift. Decap/Sveltia `single_file` pattern (research #3). |
| 4 | "Article scope" rule | Reinterpreted with the owner: the rule from Stage 5 ("I don't want to update code outside knowledge scope every time I post") was about the owner's manual work. Now: **source change = the article file only** (+ `media.json` when new images are added). The Admin **regenerates dependent output automatically** in the same commit: the article page × 3 languages, the knowledge index × 3, the homepage latest-articles section × 3, sitemaps. | Keeps the owner's convenience and makes article lists and their JSON-LD static (research #8). |
| 5 | Page → preset reference | **Linked, version-pinned instances:** `"preset": "hero-split@3"`. A page keeps rendering v3 until the owner upgrades it. A minor upgrade offers "upgrade all"; a major upgrade shows each affected page side by side. Presets are deprecated, never deleted while in use. | Research #9 §3.7. Avoids both silent breakage (Figma) and libraries that never improve (Wix/Squarespace). |
| 5a | Per-page tweaks | **Two levels only.** (1) **Overrides** from the preset's whitelist (text, image, alignment, image side, colour mode light/dark/linen, item count, show/hide parts), stored on the instance and carried across upgrades. (2) Beyond the whitelist, a **page-only preset**: a real versioned preset flagged `listed: false` (hidden from the picker, tracked in the usage index, can be promoted to the library later). **No detach.** Colours and fonts are always tokens from the locked palette. | Covers small tweaks without polluting the library or losing upgradability (research #9 pitfalls 2 and 9). Frequent level-2 use signals that a preset needs another override. |
| 6 | Library storage | **Master library + pinned copies.** Every save-back goes to the master library (`library/`, in this repo for now and movable to its own repo later). Each site folder keeps copies of exactly the preset versions it uses, so the site is self-contained. | A pinned version is immutable, so copies can never drift. Keeps "1 site = 1 self-contained folder" (map) and "the library accumulates" (Principle 1). |
| 7 | Drafts | **Local autosave (IndexedDB) + a private drafts repo.** "Save draft" commits to a separate **private** repo; Publish moves the content into the public repo and clears the published drafts. The token covers both repos. | The site repo is public (verified 2026-10-05), so drafts committed there would be readable by anyone. The public repo holds only published content. |
| 8 | Image originals | **Stored in the private drafts repo** under `originals/` (max 12 MB per file, with a usage bar). The public repo holds only the WebP renditions from research #7, **and only once they are published**: until then the renditions also wait in the drafts repo *(amended — review H5)*. | Allows re-cropping, focal-point changes and larger renditions later without hunting for files; GPS data in originals stays private. Overrides research #7's "never committed" proposal. |

Decided by Claude as technical consequences of the above (owner informed):

- The source folder is named **`site/`**.
- Theme tokens live in **`site/theme.json`** (DTCG vocabulary, `$deprecated` supported) and the Admin generates `theme.css` from it. This answers research #9 open question 7.
- Every generated file carries a header comment: *generated by the Admin; do not edit directly*.
- Every source file carries a **`"schemaVersion"`** field, so a future format change can be migrated file by file. Add fields; never rename them (research #9 pitfall 7).
- **Generation reads published source only.** It never reads drafts, except for the item being published. Regenerating the homepage for a new article therefore cannot leak an unpublished homepage draft.
- **Cross-repo order:** commit to the public repo first and clear drafts second. If clearing fails, the leftover drafts are identical to the published content and harmless; the Admin detects and removes them on the next run.
- `site/`, `library/` and `admin/` are served publicly by Pages (the repo is public anyway). `admin/` carries `noindex`, so search engines do not index the Admin. *Corrected (review M15):* `robots.txt` cannot hide these folders, because crawlers read it only at the host root and this is a project site (research #8 §robots). The raw JSON under `site/` and `library/` may therefore be crawled; it holds only published content, so this is accepted. The generated `robots.txt` still ships for the custom-domain future.

---

## 3. File layout

```
① Site repo (public) — only published content
│
├── site/                         SOURCE = "the site folder" (the Admin edits only this)
│   ├── site.json                 identity / NAP, languages, header + footer menus, redirects, SEO defaults
│   ├── theme.json                design tokens → generates theme.css
│   ├── pages/<page-id>.json      slug, parent, per-language SEO fields,
│   │                             sections[] = instances { preset: "id@ver", overrides, content{field:{en,th,zh}}, hiddenIn }
│   ├── articles/<id>.json        shared meta (id, slug, dates, author, image, featured) + per-language title/excerpt/keywords/body  (named by id — amended by #14)
│   ├── presets/<id>@<ver>.json   pinned copies of the presets this site uses (incl. page-only presets) + their markup
│   └── media.json                one entry per asset: renditions, focal point, ThumbHash, alt {en,th,zh}, usage
│
├── library/                      MASTER Design Library (section types, presets with all versions, page templates, catalogue)
│
├── index.html  en/  th/  zh/     OUTPUT, generated on every Publish
├── media/  theme.css  sitemap*.xml  robots.txt  .nojekyll
│
└── admin/                        the Admin app

② Drafts repo (private)
├── drafts/                       unpublished changes; same paths as site/, only the changed files
└── originals/<media-id>.<ext>    original uploads
```

Publishing article `vat-guide` touches *(example from 5 October; addresses and file names are now as in #14: `site/articles/<id>.json`, output at `/<lang>/<listing-page>/vat-guide/`)*:

- **Source:** `site/articles/vat-guide.json` (+ `site/media.json` if images were added)
- **Output (generated):** `{en,th,zh}/posts/vat-guide.html`, `{en,th,zh}/knowledge.html`, `{en,th,zh}/index.html` (latest-articles section), sitemaps, new `media/*` renditions

---

## 4. Effects on other tickets

- **#11 Rendering strategy:** decision 1 effectively chooses "pre-render static HTML at publish time". #11 only needs to confirm the details (which generator runs where, and incremental vs. full regeneration). One open detail: building article lists means reading every article file, so #11 should decide whether to keep a generated (output-side) article index as a cache.
- **#13 Design Library governance:** decisions 5, 5a and 6 fix the reference shape (`id@version`, override whitelist, page-only presets, master + copies). #13 still owns naming, categories and the save-back UX.
- **#17 Drafts, versions and rollback:** decision 7 fixes *where* drafts live. #17 still owns the owner-facing undo and version UX.
- **#20 Token task:** the fine-grained token must select **two repositories** (the site repo and the private drafts repo) with Contents read/write; Pages read-only applies to the site repo. The setup guide gains a "create the private drafts repo" step.
- **#19 Migration:** the current hand-written pages become generated output only after they are rebuilt as `site/` source. That work belongs to #19, not here.

---

## 5. Not decided here (deliberately)

- The exact JSON schema of each file → build sessions / #13 / #14.
- The Site Structure model (page tree, slug-change redirects) → #14.
- The admin's own code layout under `admin/`, and sanitising article HTML at generation time → #16.
- Size thresholds for the private repo (originals) → the media work that follows research #7.
- Two devices editing the same draft at once → #17.
