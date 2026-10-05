# 24 — Admin shell and navigation (12a)

**Ticket:** GitHub issue #24 (Wayfinder grilling, sub-ticket of #12)
**Date:** 5 October 2026
**Decided by:** the owner, in a grilling session with Claude
**Inputs:** decision #12 (frame), research #2 (premium builders)
**Status:** **in progress.** Round 1 below is locked. Dashboard detail, empty/error/loading states and keyboard shortcuts are still open.

---

## 1. สรุปสำหรับเจ้าของกิจการ (ภาษาไทย)

1. **ชื่อเมนูเป็นภาษาไทย มีคำอังกฤษตัวเล็กใต้** เช่น "หน้าเว็บ / Pages"
2. **หน้าแก้ไขแบ่ง 4 ช่อง:** เมนูหดเหลือไอคอน · ต้นไม้หน้าเว็บ · หน้าเว็บจริง (คลิกเพื่อแก้) · ช่องตั้งค่าของ section ที่เลือก
3. **บนมือถือ:** ดู Dashboard และรายการ "ต้องดูแล" · แก้คำผิด · เปลี่ยนรูป · กด Publish ได้ ส่วนการสร้างหน้าและจัดโครงเว็บทำบนคอมพิวเตอร์หรือแท็บเล็ต
4. **หน้าตาของ Admin รอการเลือกอัตลักษณ์ใหม่** (#33 → #34 → #35) เพราะเจ้าของเลิกใช้ชุดสี Navy & Soft Linen และฟอนต์เดิมแล้ว

---

## 2. Locked decisions (round 1)

| # | Question | Decision | Why |
|---|---|---|---|
| 1 | Menu labels | **Thai label with a small English word underneath** (แดชบอร์ด / Dashboard · หน้าเว็บ / Pages · บทความ / Articles · โครงสร้างเว็บ / Site Structure · คลังดีไซน์ / Design Library · รูปและไฟล์ / Media · SEO / Search & sharing · เวอร์ชัน / Versions · ตั้งค่า / Settings). The English toggle switches the whole Admin to English. | Owner choice. Thai-first, but matches WordPress habits and English help material. |
| 2 | Edit layout | **Four zones:** (1) left menu collapses to an icon rail while editing; (2) page tree; (3) the real page in the centre, click to edit; (4) a right panel with the selected section's settings (layout, colour mode, image, show/hide, per-language status). The top bar keeps the site name, TH/EN/ZH, device preview and Publish with a change count. | Owner choice (Webflow/Framer pattern). Gives the page the most space while the tree stays visible (decision #12-4). |
| 3 | Phone use | **Check, fix small things, publish.** On a phone: Dashboard and "Needs attention", edit text, swap an image, approve a Publish. Building pages, adding sections and arranging the tree are desktop/tablet only, and the phone says so plainly instead of showing a cramped editor. | Owner choice. Dragging trees and sections on a small screen is error-prone; urgent fixes still work anywhere. |
| 4 | Admin look | **Deferred to the new visual identity.** The owner retired Navy & Soft Linen and Instrument Serif + Inter for both the website and the Admin. The Admin's look is decided by the direction chosen in #35, which includes an Admin screen. | Owner instruction: "change the whole theme, don't refer to the old one." |

---

## 3. Still open in this ticket

- Dashboard detail: order and wording of "Needs attention", what the live preview shows, shortcuts.
- Empty, loading and error states (Thai wording, tone).
- Keyboard shortcuts.
- Tablet layout (whether the four zones fit, or the settings panel becomes a drawer).
