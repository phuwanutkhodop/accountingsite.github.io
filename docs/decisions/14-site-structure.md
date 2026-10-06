# 14 — Site Structure model

**Ticket:** GitHub issue #14 (Wayfinder grilling)
**Date:** 6 October 2026
**Decided by:** the owner, for what visitors see (§2), and Claude, under the owner's delegation of technical choices (§3)
**Inputs:** research #2 (premium builders, §3.4), #8 (multilingual SEO/AEO); decisions #10 (content model), #11 (rendering), #12 (Admin IA), #16 (tech stack)
**Status:** locked

---

## 1. สรุปสำหรับเจ้าของกิจการ (ภาษาไทย)

1. **เมนูด้านบน:** มีเมนูย่อยหนึ่งชั้น เช่น ชี้ที่ "บริการ" แล้วรายการบริการเลื่อนลงมา บนมือถือเป็นรายการที่กดเปิดได้
2. **ส่วนท้ายเว็บ:** แบ่งหลายคอลัมน์ มีหัวข้อ เช่น บริการ · บริษัท · ติดต่อ และมีแถบล่างสุดสำหรับลิขสิทธิ์และนโยบาย
3. **ต้นไม้หน้าเว็บลึกได้ 3 ชั้น** เช่น หน้าแรก › บริการ › จดทะเบียนบริษัท
4. **ที่อยู่เว็บอ่านง่ายและสั้น** เช่น `/th/services/company-registration/` ใช้ภาษาอังกฤษตัวเล็กในทุกภาษา เพื่อให้แชร์ใน LINE ได้ไม่เพี้ยน
5. **เปลี่ยนชื่อที่อยู่ ย้ายหน้า หรือลบหน้าได้โดยลิงก์เดิมไม่เสีย** ระบบจะพาคนที่เปิดลิงก์เก่าไปหน้าใหม่อัตโนมัติ เวลาลบหน้า ระบบจะถามว่าจะให้คนที่เปิดลิงก์เก่าไปที่หน้าไหน
6. **ลิงก์ภายในเว็บไม่มีวันเสีย** เพราะระบบจำว่าลิงก์ไปที่ "หน้าไหน" ไม่ได้จำที่อยู่ ทุกหน้ามีรายการ "หน้าที่ลิงก์มาหาหน้านี้" และระบบเตือนหน้าที่ไม่มีใครลิงก์ถึง
7. **หน้าแต่ละหน้ามี 3 สถานะ:** อยู่ในเมนู · ไม่อยู่ในเมนูแต่เปิดได้ด้วยลิงก์ · ฉบับร่าง และมีสวิตช์ "ซ่อนจาก Google" แยกต่างหาก

---

## 2. Owner decisions

| # | Question | Decision | Why |
|---|---|---|---|
| 1 | Header menu | **Top-level items plus one dropdown level.** On phones the same menu becomes a list whose groups open with a tap. | Owner choice (recommended option). Squarespace's one-level folders are the most legible model in research #2. A mega menu adds design weight a firm of this size does not need. |
| 2 | Footer | **Headed columns** (for example Services · Company · Contact), at most four, plus a bottom bar for copyright and legal links. | Owner choice (recommended option). It is the norm for professional firms and gives contact details a fixed home. |

---

## 3. Technical decisions (delegated to Claude)

### 3.1 The tree and the menus are separate things

- **The page tree** is the site's structure. It decides each page's address, its breadcrumbs and its parent. The homepage is the root and cannot be moved or deleted.
- **Menus** are curated lists that point at pages. The header menu, the footer columns and the footer's bottom bar are edited in Site Structure. When a page is added at the top level, the Admin offers "add to header menu".
- This follows WordPress and Squarespace. A page can be in the tree without being in any menu, and a menu can hold links that are not pages.

### 3.2 Tree rules

- **Maximum depth: three levels below the homepage** (Home › Services › VAT registration). Deeper trees make addresses and breadcrumbs long and are not needed for a firm site. The Admin refuses a drag that would exceed it.
- **Page states** (the Squarespace three-zone model, research #2):
  - *In a menu*;
  - *Not in a menu*: published, reachable by links, listed in the sitemap;
  - *Draft*: not published (decision #10 drafts).
- **"Hide from search"** is a separate per-page switch. It adds `noindex` and removes the page from the sitemap and hreflang sets (research #8 §2.3).
- A page with children cannot be deleted until its children are moved or deleted.

### 3.3 Addresses (URLs)

- **Clean directory addresses that follow the tree:** `/<lang>/<parent-slug>/<slug>/`, generated as `…/<slug>/index.html`. The homepage is `/<lang>/`. GitHub Pages serves the folder form natively.
  - *This amends research #8's form* (`/<lang>/<file>.html`). The rule that matters there still holds: **one form everywhere**: canonical, hreflang, `og:url`, sitemap and JSON-LD all use the trailing-slash form.
- **One slug per page, shared by all three languages,** in lowercase Latin letters, digits and hyphens (research #8 §2.1). So `/en/services/`, `/th/services/` and `/zh/services/` are the same page. Thai and Chinese visitors still see their own titles, menus and breadcrumbs; only the address is in Latin. Shared Thai addresses stay readable in LINE instead of turning into `%E0%B8%…`.
- The slug is suggested from the English title and is editable. It must be 2–60 characters, unique among siblings, and must not be a reserved name: `admin`, `site`, `library`, `media`, `en`, `th`, `zh`, `assets`, `404`.
- **Changing a slug after publishing is allowed** and creates a redirect automatically (§3.4). The Admin warns first: "people who saved the old address will be forwarded". *This relaxes research #8 §4.7 ("immutable after publish"); Principle 2 on the map asks for slug changes with automatic redirects.*
- **Articles** are not pages in the tree. Each article lives under the page that lists the articles: `/<lang>/<listing-page-path>/<article-slug>/`. Taxonomy and the listing itself → #27.
- **Page identity is not the address.** Each page has a permanent `id`, assigned when it is created and never changed. Slugs, parents and addresses can change; the id does not.

### 3.4 Redirects without a server

GitHub Pages cannot send server redirects. The generator therefore writes a **redirect page** at every old address, in each language. Each redirect page contains:
- `<meta http-equiv="refresh" content="0; url=…">`, which works with JavaScript off. Google treats an instant meta refresh as a permanent redirect.
- `<link rel="canonical">` to the new absolute address, and `noindex`.
- A short script with `location.replace`, which keeps any `#anchor`.
- A visible link in the page's language, for the rare visitor who sees the page.

Rules:
- **Redirects are created automatically** when a slug changes, a page moves in the tree, or a page is deleted (§3.6). The owner can also add one by hand in Site Structure › Redirects: old address → a page, or → an outside address.
- **Chains are collapsed.** If A → B and B later → C, the generator writes A → C.
- **Loops, and a redirect sitting on an address a live page uses, are validation errors** (decision #11 §3.5).
- Redirect pages are generator-owned (`generated.json`, decision #11 §3.4), kept until the owner removes the rule, and never listed in the sitemap.
- No practical cap. Each redirect page is about 1 KB × 3 languages. The Admin warns above 500 rules.
- **A trilingual `404.html`** is generated at the site root, which is the only place Pages looks for it. It picks its language from the path (`/th/…` → Thai). It offers the homepage, search when #27 adds it, and the main menu.
- The current hand-written pages (`/en/knowledge.html`, `/en/posts/*.html` …) receive redirects through the same mechanism when #19 migrates them.

### 3.5 Menus

- **Item types:** a page (by id); a page plus a section anchor; an outside address (`https://`, optionally opening in a new tab); email; phone; LINE.
- **Labels** default to the page's menu title in each language and can be overridden per language. Like every visible text, all three languages are required to publish (decision #11).
- **Header menu:** top items, each with an optional dropdown (one level, owner decision 1). A top item can be a page or a label that only opens its dropdown. The Admin warns above 7 top items or 8 dropdown items.
- **Footer:** up to 4 columns, each with a heading and links, plus the bottom bar (owner decision 2).
- **The language switcher is automatic**, not a menu item. It links to the same page in the other languages.
- The phone menu is derived from the header menu; there is nothing to maintain twice.

### 3.6 Deleting a page

1. The Admin shows what depends on the page: menus that list it, pages and articles that link to it, and redirects that point at it.
2. It asks where visitors of the old address should go. The default is the parent page.
3. On Publish, that choice becomes a redirect (§3.4). Menu entries for the page are removed, and links to it become validation errors until each one is changed. The Admin offers "point all to the chosen page" in one click.

### 3.7 Internal links never break

- Internal links are stored **by page id**, never by address: `page:<id>` or `page:<id>#<anchor>` in rich-text link marks (decision #16 §2-6) and in preset link fields.
- The generator turns them into **relative** addresses (project rule) for each language. Renaming or moving a page therefore updates every link to it on the next Publish.
- Section anchors are stable ids stored on the section instance, so renaming a heading does not break `#anchor` links.
- **What the owner sees:**
  - every page has a "Links to this page (n)" list and a "This page links to" list;
  - Site Structure has a link map: a table of every page with its inbound links and menus;
  - pages with no inbound link and no menu are flagged as **orphans** in "Needs attention" (decision #12-5).

### 3.8 One-language pages

Already decided in #11: publishing requires all three languages. A page cannot exist in only one language. Hiding a single section in one language (`hiddenIn`) is still allowed.

### 3.9 Root and breadcrumbs

- The site root `/` stays the language chooser and the `x-default` (research #8 §2.2). The generator owns it from now on.
- Breadcrumbs come from the tree, in the page's language. `BreadcrumbList` JSON-LD is always generated (research #8). Whether breadcrumbs are visible on the page is a preset choice.

### 3.10 Where it is stored (amends decision #10 §3)

- `site/site.json` holds the **tree** as one ordered nesting of page ids, plus the **menus** and the **redirect rules**.
- Each `site/pages/<id>.json` holds the slug, SEO fields and sections. **`parent` moves out of the page file into the tree.**
- *Why:* reordering or moving a page changes one file instead of several sibling files, and the tree cannot contradict itself.

---

## 4. Effects on other tickets

- **#8 / generation checklist:** the URL form becomes `/<lang>/…/<slug>/`, and slugs can change with redirects. Everything else in the checklist stands.
- **#10:** `parent` moves into the tree in `site/site.json` (§3.10).
- **#11 validation gate:** gains depth limit, slug rules, reserved names, redirect loops, redirects that shadow live pages, and links to deleted pages.
- **#13 Design Library:** preset link fields store `page:<id>` values, not addresses.
- **#19 Migration:** existing addresses get redirects to their new form through §3.4.
- **#22 Admin prototype:** the tree panel shows the three states; Site Structure has Menus, Redirects and Link map.
- **#26 Pages editing:** the page settings panel holds the slug, the menu title per language, "hide from search" and the link lists.
- **#27 Articles:** article addresses live under their listing page (§3.3).

---

## 5. Not decided here

- How the menus and the footer look → the neutral test theme (#21) and the presets.
- Article categories, tags and search → #27.
- The exact Admin screens for Site Structure → #22 and #26.
