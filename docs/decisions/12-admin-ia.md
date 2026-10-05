# 12 — Admin information architecture (umbrella)

**Ticket:** GitHub issue #12 (Wayfinder grilling), split into sub-tickets 12a–12g
**Date:** 5 October 2026
**Decided by:** the owner, in a grilling session with Claude
**Inputs:** research #2 (premium builders), #9 (design libraries), decisions #10, #11
**Status:** **partly locked** — the frame below is locked; each sub-ticket fills in one area. #12 closes when 12a–12g are closed and this file is merged into one IA.

---

## 1. สรุปสำหรับเจ้าของกิจการ (ภาษาไทย)

1. **มี 2 ระดับตั้งแต่วันแรก:** ระดับระบบ ("เว็บไซต์ของฉัน" — รายการเว็บทั้งหมด) และระดับเว็บไซต์ (Admin ของเว็บหนึ่งเว็บ)
2. **เมนูซ้าย 9 หัวข้อแบบ WordPress:** Dashboard · Pages · Articles · Site Structure · Design Library · Media · SEO · Versions · Settings
3. **หน้าแรกของแต่ละเว็บ (Dashboard):** เห็นเว็บจริงแบบสด ๆ ด้านหนึ่ง อีกด้านเป็นรายการ "ต้องดูแล" (แปลยังไม่ครบ · มีการแก้ที่ยังไม่ Publish · ลิงก์เสีย · Publish ล่าสุดเมื่อไหร่) พร้อมปุ่ม Publish และทางลัด "เพิ่ม Section" / "เขียนบทความ"
4. **ต้นไม้หน้าเว็บ (page tree) เห็นตลอด** ข้างตัวแก้ไข ลากเพื่อเรียงลำดับได้โดยไม่ต้องออกจากหน้าแก้ไข
5. **ต้องมีใน v1:** Versions พร้อมดูตัวอย่างและกู้คืนคลิกเดียว · หน้า Publish แสดงว่าอะไรเปลี่ยน แยกตามภาษี · ตารางแปล TH/EN/ZH เคียงกันพร้อมป้ายขาด · พรีวิวมือถือ/แท็บเล็ต/เดสก์ท็อป · และส่วนเสริมคุณภาพอีกชุดที่ Claude เสนอ (ตั๋ว 12g)
6. **ตั๋วใหญ่เกินไป จึงแตกเป็น 7 ตั๋วย่อย** เพื่อออกแบบให้ละเอียดขึ้น

---

## 2. Locked decisions

| # | Question | Decision | Why |
|---|---|---|---|
| 1 | Levels | **Two levels from day one.** *System level* = a "My Sites" screen (list of sites; add, switch, back up). *Site level* = the Admin of one site. Opening the Admin lands on My Sites; entering a site lands on its Dashboard. | Owner choice. Data model is already 1 site = 1 self-contained folder (map, decision #10), so no model change; the cost is one more screen set (ticket 12b). |
| 2 | Site-level menu | **9 areas, WordPress-style:** Dashboard · Pages · Articles · Site Structure · Design Library · Media · SEO · Versions · Settings. | Owner choice. Each area has one obvious job; matches the mental model of WordPress, which the owner knows. |
| 3 | Always-on controls | Language switch, device preview (phone / tablet / desktop) and **Publish** sit in the top bar on every site-level screen. | Research #2 must-haves 4–5. |
| 4 | Page ↔ site | **Page tree always visible** beside the editor; drag in the tree to reorder or re-parent. A full Site Structure screen adds menus, redirects and the link map (ticket #14). | Owner choice. Rearranging never requires leaving the editor. |
| 5 | Dashboard (first screen of a site) | **Live preview of the homepage + a "Needs attention" list** (untranslated items, unpublished changes, broken links, last publish time) + one Publish button + "Add section" and "Write article" shortcuts. | Owner choice (recommended option). Turns the first screen into a to-do list. |
| 6 | v1 must-haves | Versions with preview and one-click restore · Publish screen listing changes by language · TH/EN/ZH side-by-side translation table with missing badges · device preview · plus the quality/safety set in 12g (owner: "plus others you see fit for commercial grade"). | Owner choice; research #2 §4. |
| 7 | Process | #12 is split into sub-tickets 12a–12g. | Owner request: "this is big, divide into sub-tickets for deeper design". |

---

## 3. Sub-tickets

| Ticket | Scope |
|---|---|
| **12a** Shell and navigation | Top bar, left menu, page-tree panel, Dashboard layout, Thai/English toggle, empty/error/loading states, keyboard shortcuts |
| **12b** System level — My Sites | Site list, add/switch/remove, per-site backup entry point, first-run, token connection per site |
| **12c** Pages and section editing | Add-section picker, editing text/images, overrides, translation table, page-only presets |
| **12d** Articles and Media | Word-like editor, upload and resize, media library, alt text, budget bar |
| **12e** Publish, Versions and Preview | "What changed" screen, validation-gate messages, version list and restore, device preview behaviour |
| **12f** SEO, Settings and onboarding | Four SEO fields with Google preview, languages, integrations placeholder, GitHub connection, onboarding |
| **12g** Quality and safety extras | Unsaved indicator and undo/redo, global search, activity log, link checker, accessibility and speed report, whole-site backup/export |

12a goes first; 12b–12g are blocked by it. Existing tickets #18 and #22 stay blocked by #12 as a whole.

---

## 4. Not decided here

Everything inside a sub-ticket's scope. Technical choices remain Claude's, recorded in each sub-ticket's record.
