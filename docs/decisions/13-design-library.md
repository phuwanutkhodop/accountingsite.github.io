# 13 — Design Library governance

**Ticket:** GitHub issue #13 (Wayfinder grilling)
**Date:** 6 October 2026
**Decided by:** the owner for the three choices in §2; Claude for the technical choices in §3, under the owner's delegation
**Inputs:** research #9 (design libraries) and #2 (premium builders); decisions #10 (content model), #11 (rendering), #14 (site structure), #16 (tech stack), #33 (light and dark token sets)
**Status:** locked. **Amended 6 October 2026** after the plan review (`docs/reviews/2026-10-06-plan-review.md`, findings H4, M3, M4, M9): §3.4 step 6, §3.7, §3.10 and §3.11.
**Amended 6 October 2026 by #31** (`docs/decisions/31-multi-site-hosting.md` §3-7, §7): the master library is its own repo, `builder-library`; save-back writes the master there at once, and the pinned copy ships with Publish. Removal waits for zero use across every site.
**Amended 6 October 2026 by #15** (`docs/decisions/15-type-system.md`): `theme.json` gains `font.roles` (display, body and UI, each with Latin, Thai and Chinese families); the library check gains the font rules of #15 decision 10.
**Amended 6 October 2026 by #21** (`docs/decisions/21-section-library-sample.md` §2): presets carry scoped, token-only `css`; the generator owns the `<section>` wrapper; container queries at three shared breakpoints; `tone` (plain / tinted / bold) is universal; field kinds expand into template values; a shared base; the quality bar in §4 there.

---

## 1. สรุปสำหรับเจ้าของกิจการ (ภาษาไทย)

1. **คลังดีไซน์มี 5 ระดับ:** ธีม (สีและตัวอักษรกลาง) · แบบหน้า · ชนิด section · ดีไซน์ (preset) · ชิ้นที่วางบนหน้า
2. **"เก็บเข้าคลัง" เก็บแค่ดีไซน์:** ระบบเอาข้อความ รูป และเบอร์โทรจริงออก แล้วใส่ข้อความตัวอย่างสามภาษาแทน คลังจึงสะอาดเสมอ
3. **หน้าเว็บไม่เปลี่ยนเอง:** เมื่อดีไซน์มีรุ่นใหม่ หน้าเดิมยังใช้รุ่นเก่า ระบบแจ้งใน "ต้องดูแล" พร้อมภาพก่อนและหลัง แล้วคุณกดอัปเกรดเองทีละหน้าหรือทั้งหมด
4. **หมวดในคลังมี 10 หมวด:** เปิดหน้า · ความน่าเชื่อถือ · บริการ · ขั้นตอนการทำงาน · ทีมงาน · ผลงานและรีวิว · บทความ · คำถามที่พบบ่อย · ติดต่อและเชิญชวน · โครงหน้า
5. **ภาพตัวอย่างในคลังเป็นของจริงเสมอ:** ระบบวาดด้วยธีมปัจจุบัน ไม่ใช่รูปถ่ายเก่า จึงไม่ล้าสมัยเมื่อเปลี่ยนสี
6. **ไม่มีการลบดีไซน์ที่ยังมีหน้าใช้อยู่** ทำได้แค่ติดป้าย "เลิกใช้" ป้ายนี้ซ่อนดีไซน์จากคลัง แต่หน้าเดิมยังแสดงผลตามปกติ
7. **ดีไซน์ไม่มีสีหรือตัวอักษรตายตัว** ทุกชิ้นผูกกับธีม ดีไซน์ทุกชิ้นต้องอ่านชัดทั้งโหมดสว่างและโหมดมืด
8. **ข้อความตัวอย่างไม่มีวันขึ้นเว็บจริง** ช่องข้อความเริ่มว่างเสมอ และระบบไม่ยอมให้ Publish ถ้ายังมีข้อความตัวอย่างค้างอยู่ *(เพิ่มหลังการตรวจ 6 ต.ค.)*
9. **ดีไซน์ที่เก็บเข้าคลังจะขึ้นเว็บพร้อมการ Publish ครั้งถัดไป** ก่อนหน้านั้นเก็บเป็นฉบับร่างส่วนตัว *(เพิ่มหลังการตรวจ 6 ต.ค.)*

---

## 2. Owner decisions

| # | Question | Decision | Why |
|---|---|---|---|
| 1 | What "Save to library" saves | **Design only, always.** Real text, images, phone numbers and links are replaced by the section type's placeholders in all three languages. There is no "save with content" option. | Owner choice (recommended). Avoids research #9 pitfall 5: a client name or an old price appearing inside a "design". |
| 2 | When a preset gets a new version | **Pages keep their version until the owner upgrades.** "Needs attention" lists the pages that have a newer version available, with a before/after preview. The owner can upgrade one page or all of them. | Owner choice (recommended). Confirms decision #10-5. Nothing on the live site changes without the owner seeing it first. |
| 3 | Picker categories | **The ten intent categories:** Opening (Hero) · Trust · Services · Process · People · Proof · Knowledge · FAQ & notes · Contact & conversion · Structure. More can be added later. | Owner choice (recommended). Research #9 §3.5 mapped these to the pages a Thai accounting firm actually has. |

---

## 3. Technical decisions (delegated to Claude)

### 3.1 The five levels

Owner-facing words are the Thai labels below with the English term underneath. No "component", "block" or "pattern" anywhere (research #9 pitfall 12).

| Level | Thai label | What it stores | File |
|---|---|---|---|
| **Theme** | ธีม | Semantic tokens with **a light set and a dark set** (decision #33) in DTCG vocabulary, aliasing primitives. It is the only place colours, fonts, spacing and radii have values. | `site/theme.json` → generated `theme.css` (decision #10) |
| **Page template** | แบบหน้า | An ordered list of slots, each naming a *section type* and a default preset. It is used when creating a page ("Service page: Opening → Services → Process → FAQ → Contact"). After that the page is independent. | `library/templates/<id>.json` |
| **Section type** | ชนิด section | The content contract: the fields, their kinds (text, rich text, image, link, list of items), required or optional, and item-count limits. It also holds **placeholders in EN, TH and ZH** for every field. | `library/types/<id>.json` |
| **Preset** | ดีไซน์ | One design of a section type: the markup (strict Mustache subset, decision #16-5), token bindings, options with defaults, the override whitelist, constraints and preview settings. It is versioned. | `library/presets/<id>@<major>.<minor>.json` |
| **Instance** | ชิ้นบนหน้า | A preset placed on a page. It holds `preset: "<id>@<major>.<minor>"`, real content per language, override values, `hiddenIn` and its anchor id (decision #14). | inside `site/pages/<id>.json` |

### 3.2 What a preset record holds

These fields are additive only. A field is never renamed (research #9 pitfall 7), and each record has `schemaVersion` (decision #10).

- **Identity:** a permanent `id` (lowercase, hyphens, never reused); a `name` and a one-line `purpose` in EN, TH and ZH; the `type` it implements; one primary `category` (§2-3) plus free `tags`.
- **Version:** `major.minor`, with a changelog line per version, plus `deprecated: { reason, replacedBy }`.
  - **Minor:** the same fields and overrides; only markup or defaults change.
  - **Major:** a field or an override is added or removed.
- **Lineage:** `from: "<id>@<version>"` and the save date. This lets the library read as a family tree.
- **Markup:** a strict Mustache-subset template. It may use only the section type's fields, option values and token class names.
- **Token bindings:** each styled part names a **semantic token**. **Literal colours, font names and pixel sizes are rejected** by the library check (research #9 pitfall 4).
- **Options and overrides:** the option set with defaults, and the whitelist of options an instance may override. The base whitelist from decision #10-5a is text, image, alignment, image side, colour mode, item count and show/hide parts.
- **Constraints:** min/max items, the maximum heading length **per language**, and the image aspect ratio. The editor warns when the content would not fit.
- **Preview:** viewport width and option values for the thumbnail.

Every page instance stores its preset as `preset: "<id>@<major>.<minor>"`. This refines decision #10's `@3` example to a two-part version.

### 3.3 Rules every preset must pass (the library check)

The check runs in `node --test` for library files (decision #16-10). The Admin runs the same check before any save-back.

1. The template parses in the strict subset and uses only declared fields and options.
2. It contains no literal colours, fonts or sizes, and no inline `style` or `<script>`.
3. It renders with placeholders in **all three languages** and in **both light and dark token sets**.
4. Text and background token pairs pass **WCAG AA contrast in both sets** (decision #33 consequence). The precise accessibility bar for whole pages is #30.
5. It renders without JavaScript (decision #11-1). Interactive behaviour may only *enhance*, for example opening an FAQ answer with `<details>`.
6. Its markup is semantic and has one heading level per section role; the page `<h1>` belongs to the opening section only.

### 3.4 Save-back flow

The owner's path, inside the Admin:

1. Select a section → **"Save design to library"**.
2. The Admin decides the kind of save and shows it in plain words:
   - **Only option values were changed:** it offers **"save as a new version of <name>"** (minor) or **"save as a new design"** (a sibling). Asking this is what prevents near-duplicates (research #9 pitfall 9).
   - **The instance uses a page-only preset** (decision #10-5a): the action is called "add to library", which promotes it by setting `listed: true`.
3. **Strip step:** content is replaced by the type's placeholders in EN, TH and ZH, and the overrides become the new defaults.
4. The owner gives it a name and a one-line purpose in three languages (Thai first) and a category. A live thumbnail renders immediately.
5. The library check runs (§3.3). If it fails, the reason is shown in Thai and nothing is saved.
6. The new preset and its pinned copy are saved **as a draft in the private drafts repo** (decision #10-7), and the page points to it in its draft. They reach the public `library/` and `site/presets/` (decision #10-6) **with the next Publish**, through the validation gate like any other change. The public repo still holds only published content. **Nothing visible changes on the page.** *(Amended: the first version wrote public files at once, outside Publish — review M3.)*

**Claude sessions add presets as files** in `library/` through the same check, with tests. This is how the library grows quickly at the start (#21 builds the first set).

### 3.5 Upgrading pages (owner decision 2)

- **"Needs attention" shows:** "a newer version of <name> is available on N pages."
- **Minor upgrade:** a before/after preview, then **Upgrade this page** or **Upgrade all N pages**. Content and overrides carry over unchanged.
- **Major upgrade:** a before/after preview **for each page**. Fields that no longer exist are shown so that no content is lost silently. The owner confirms page by page.
- **Whether the owner upgrades or not:**
  - an upgrade is just an edit, so it is published like any other change and can be undone through Versions (#17);
  - not upgrading is always safe, because the pinned copy keeps rendering.

### 3.6 Deprecation and removal

- **Deprecating** hides the preset from the picker. Pages using it keep rendering, and they get a "newer design available" note pointing at `replacedBy`.
- **A preset can be removed only when nothing uses it.** At that point its pinned copy disappears from `site/presets/` on the next publish. The master copy in `library/` is kept in git history.
- The owner can deprecate. Removal is a cleanup the Admin proposes only for presets with zero use.

### 3.7 Usage index

- The usage index is **computed, not stored:** the Admin derives it from published pages, **drafts** and **page templates** whenever it loads source (decision #11 §3.7 cache). A computed index cannot drift (research #9 pitfall 3).
- **Removal waits for every use:** a preset still used by a draft or a template counts as used. When the master library serves more than one site, removal also waits for zero use across **every** site, and for every site to be readable (#31 §7). *(Amended — review M4; resolved by #31.)*
- It powers:
  - "Used on N pages" in the library, with links to those pages;
  - the upgrade notices;
  - the removal rule;
  - checks for token deprecation in the theme.

### 3.8 Previews

- Previews are **live**: the engine renders the preset with its placeholders, using the current theme and the language shown in the Admin. The render is scaled into a **sandboxed iframe** (`sandbox` with no scripts). Because they are never stored images, previews never go stale (research #9 pitfall 10).
- A preset with a colour-mode option shows light and dark side by side.
- The picker is grouped by the ten categories, filterable by tag, with a "Saved by me" view. It shows previews at the width of the device preview chosen in the top bar.

### 3.9 Page templates

- Templates offer a starting set of sections when a page is created. The page does not stay linked to its template.
- **Why:** the page's sections are already linked to their presets, so linking the page to the template as well would add a second, confusing kind of update for little benefit. Squarespace page layouts work the same way.
- New templates are saved from an existing page ("save this page's layout as a template"). This is design only, the same as presets.

### 3.10 Placeholders never reach the live site *(added — review H4)*

- When a preset is placed on a page, its content fields **start empty**. The placeholder appears only as a grey hint inside the editor field, and as the content of library previews.
- The validation gate (decision #11 §3.5) adds an **error**: a field whose value equals its placeholder in any language. Sample Thai or Chinese text therefore cannot be published by accident, even if it was pasted in.

### 3.11 Contrast is checked at Publish too *(added — review M9)*

- The library check (§3.3-4) proves contrast for each preset when it is saved. Editing the theme can still break contrast everywhere.
- The validation gate therefore also checks every text/background **token pair of the current theme**, in both light and dark sets, against WCAG AA. A failing pair is an error. #30 sets the whole-page accessibility level on top of this.

---

## 4. Effects on other tickets

- **#10:** version strings become `major.minor`; templates and section types also live in `library/`.
- **#11 validation gate:** gains "a preset referenced by a page is missing from `site/presets/`" as an error, and "the preset is deprecated" as a warning (already listed).
- **#17 Versions:** a preset upgrade is an ordinary undoable edit.
- **#21 Section sample:** builds the first section types and presets against these rules, on the neutral test theme, and swaps in a second theme to prove that the token binding works.
- **#22 Admin prototype:** the library screen, the picker, "Save design to library" and the upgrade notices.
- **#26 Pages editing:** the add-section picker, the override panel and the constraint warnings.
- **#30 Quality:** sets the whole-page accessibility level. The contrast rules in §3.3-4 and §3.11 already apply to every preset and to the theme.
- **#17 Drafts:** save-back is a draft change (§3.4 step 6); the drafts model must carry new presets and their pinned copies.

---

## 5. Not decided here

- The first section types and presets → #21.
- The neutral test theme's token values → #21.
- The exact library screens → #22 and #26.
