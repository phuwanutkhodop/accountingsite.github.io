# 12 — Admin information architecture (umbrella)

**Ticket:** GitHub issue #12 (Wayfinder grilling), split into sub-tickets 12a–12g (#24–#30)
**Date:** 5 October 2026
**Decided by:** the owner, in a grilling session with Claude
**Inputs:** research #2 (premium builders), #9 (design libraries), decisions #10, #11
**Status:** **partly locked** — the frame below is locked; each sub-ticket fills in one area. #12 closes when 12a–12g are closed and this file is merged into one IA.
**Revised:** 5 October 2026, after a review pass (§5) approved by the owner.

---

## 1. สรุปสำหรับเจ้าของกิจการ (ภาษาไทย)

1. **มี 2 ระดับตั้งแต่วันแรก:** ระดับระบบ ("เว็บไซต์ของฉัน" — รายการเว็บทั้งหมด) และระดับเว็บไซต์ (Admin ของเว็บหนึ่งเว็บ) — เปิด Admin แล้ว**เข้าเว็บที่ใช้ล่าสุดทันที** กดชื่อเว็บบนแถบด้านบนเพื่อไปหน้า "เว็บไซต์ของฉัน"
2. **เมนูซ้าย 9 หัวข้อแบบ WordPress:** Dashboard · Pages · Articles · Site Structure · Design Library · Media · SEO · Versions · Settings
3. **หน้าแรกของแต่ละเว็บ (Dashboard):** เห็นเว็บจริงแบบสด ๆ ด้านหนึ่ง อีกด้านเป็นรายการ "ต้องดูแล" (แปลยังไม่ครบ · มีการแก้ที่ยังไม่ Publish · ลิงก์เสีย · Publish ล่าสุดเมื่อไหร่) พร้อมปุ่ม Publish และทางลัด "เพิ่ม Section" / "เขียนบทความ"
4. **ต้นไม้หน้าเว็บ (page tree) เห็นตลอด** ข้างตัวแก้ไข ลากเพื่อเรียงลำดับได้โดยไม่ต้องออกจากหน้าแก้ไข
5. **ต้องมีใน v1:** Versions พร้อมดูตัวอย่างและกู้คืนคลิกเดียว · หน้า Publish แสดงว่าอะไรเปลี่ยน แยกตามภาษา · ตารางแปล TH/EN/ZH เคียงกันพร้อมป้ายขาด · พรีวิวมือถือ/แท็บเล็ต/เดสก์ท็อป · และส่วนเสริมคุณภาพอีกชุดที่ Claude เสนอ (ตั๋ว 12g)
6. **ตั๋วใหญ่เกินไป จึงแตกเป็น 7 ตั๋วย่อย** เพื่อออกแบบให้ละเอียดขึ้น
7. **เพิ่ม 2 ตั๋วใหม่:** วิธีโฮสต์หลายเว็บ (#31 — Claude ตัดสิน) และขั้นตอนการแปล (#32 — ถามเจ้าของ)
8. **เมนู SEO = ภาพรวมทั้งเว็บ** ส่วนช่อง SEO ของแต่ละหน้าแก้ได้ในหน้าแก้ไขด้วย ข้อมูลชุดเดียวกัน

---

## 2. Locked decisions

| # | Question | Decision | Why |
|---|---|---|---|
| 1 | Levels | **Two levels from day one.** *System level* = a "My Sites" screen (list of sites; add, switch, back up). *Site level* = the Admin of one site. **Opening the Admin goes straight to the last-used site's Dashboard**; the site name in the top bar opens My Sites. My Sites is the first screen only when no site has been opened yet. | Owner choice (both the two levels and the landing rule). The *folder* model is ready (1 site = 1 folder, decision #10), but GitHub Pages serves one site per repo, so hosting, token scope, drafts repo and library location for several sites are **not** settled — ticket #31. *(Settled by #31: one Admin on its own origin for all sites; a public repo and a private drafts repo per site; one key.)* |
| 2 | Site-level menu | **9 areas, WordPress-style:** Dashboard · Pages · Articles · Site Structure · Design Library · Media · SEO · Versions · Settings. | Owner choice. Each area has one obvious job; matches the mental model of WordPress, which the owner knows. |
| 3 | Always-on controls | Language switch, device preview (phone / tablet / desktop) and **Publish** sit in the top bar on every site-level screen. | Research #2 must-haves 4–5. |
| 4 | Page ↔ site | **Page tree always visible** beside the editor; drag in the tree to reorder or re-parent. A full Site Structure screen adds menus, redirects and the link map (ticket #14). | Owner choice. Rearranging never requires leaving the editor. |
| 5 | Dashboard (first screen of a site) | **Live preview of the homepage + a "Needs attention" list** (untranslated items, unpublished changes, broken links, last publish time) + one Publish button + "Add section" and "Write article" shortcuts. | Owner choice (recommended option). Turns the first screen into a to-do list. |
| 6 | v1 must-haves | Versions with preview and one-click restore · Publish screen listing changes by language · TH/EN/ZH side-by-side translation table with missing badges · device preview · plus the quality/safety set in 12g (owner: "plus others you see fit for commercial grade"). | Owner choice; research #2 §4. |
| 7 | SEO area vs page editor | **One set of SEO data, two views:** the SEO area is a site-wide table (every page × language, problems flagged, editable inline); the page editor shows the same four fields for the page being edited. | Avoids two places that disagree; the overview is what makes problems visible. |
| 8 | Process | #12 is split into sub-tickets 12a–12g, plus two new map tickets #31 and #32. | Owner request: "this is big, divide into sub-tickets for deeper design"; review pass §5. |

---

## 3. Sub-tickets

| Ticket | Scope |
|---|---|
| **12a (#24)** Shell and navigation | Top bar, left menu with Thai labels, page-tree panel, Dashboard layout, Thai/English toggle, empty/error/loading states, keyboard shortcuts, Admin on phone/tablet |
| **12b (#25)** System level — My Sites | Site list, add/switch/remove, per-site token and passcode question, backup entry point, **sole owner of first-run and onboarding** |
| **12c (#26)** Pages and section editing | Add-section picker, editing text/images, overrides, translation table (missing + out-of-date badges), page-only presets |
| **12d (#27)** Articles and Media | Word-like editor, upload and resize, media library, alt text, budget bar, article taxonomy, on-site search |
| **12e (#28)** Publish, Versions and Preview | "What changed" screen, validation-gate messages, version list and restore, device preview behaviour |
| **12f (#29)** SEO and Settings | Site-wide SEO table + Google preview, identity, languages, palette/font pack, GitHub connection, integrations panel, analytics and consent |
| **12g (#30)** Quality and safety extras | Unsaved indicator and undo/redo, global search, activity log, link checker, accessibility and speed report, whole-site backup/export |

### Blocking edges

| Ticket | Blocked by |
|---|---|
| #24 (12a) | — |
| #25 (12b) | #24, **#31** |
| #26 (12c) | #24, **#13**, **#32** |
| #27 (12d) | #24 |
| #28 (12e) | #24, **#17** |
| #29 (12f) | #24, **#18** |
| #30 (12g) | #24 |
| #18 | **#24** (was #12 — changed to break a cycle: #12 → #29 → #18 → #12) |
| #22 | #12 (unchanged) |
| #23 | adds #31, #32 |

Edges are written in each ticket's body. The GitHub tools available in this session cannot create GitHub's native "blocked by" links; they can be added by hand in the issue sidebar or by a session that has the `gh` CLI.

### Boundaries with existing tickets

- #26 designs the *screens*; #13 decides what a preset *is* and the save-back rules; #32 decides the translation rules.
- #28 designs the *screens*; #17 decides how drafts, history and restore *work*.
- #29 hosts the integrations panel; #18 decides what is in it.
- Site Structure and Design Library areas have no sub-ticket: #14 and #13 own them, and #22 prototypes them.

---

## 4. Not decided here

Everything inside a sub-ticket's scope. Technical choices remain Claude's, recorded in each sub-ticket's record.

---

## 5. Review pass (5 October 2026)

A second review of the first draft found seven weak points; the owner approved all fixes.

1. **"No model change" for two levels was overconfident.** One Pages site = one repo, so several sites raise hosting, token, drafts-repo and library questions → new ticket #31, blocks #25.
2. **Sub-tickets overlapped existing tickets with no edges** (#26/#13, #28/#17, #29/#18; onboarding in both #25 and #29) → edges and boundaries in §3; onboarding moved to #25.
3. **The landing screen was decided without asking** → owner chose "last-used site directly".
4. **Unowned fog:** translation workflow → new ticket #32; Admin passcode → #25; Admin on phone → #24; taxonomy and on-site search → #27; analytics/consent → #29; accessibility, performance, backup → #30.
5. **SEO in two places** → decision 7.
6. Thai summary typo ("ภาษี" → "ภาษา").
7. Map did not point fog items at their tickets → map updated.
