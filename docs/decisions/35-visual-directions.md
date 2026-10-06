# 35 — Three visual directions

**Ticket:** GitHub issue #35 (Wayfinder prototype)
**Date:** 6 October 2026
**Decided by:** the owner, with Claude
**Inputs:** decision #33 (brand feeling), research #34 §11 (the three directions), the locked brand (`brand/README.md`)
**Status:** **in progress.** Round 1 published and waiting for the owner's ratings.

---

## 1. สรุปสำหรับเจ้าของกิจการ (ภาษาไทย)

1. **ทำ 2 รอบ:** รอบ 1 ทำหน้าแรกและหน้าหลังบ้านครบ 3 แนว ส่วนรอบ 2 ทำหน้าที่เหลือ (บริการ ปฏิทินภาษี บทความ ติดต่อ) เฉพาะแนวที่ชนะ
2. **สีตัวเลข:** ให้ดูเทียบทั้งทองเหลืองและแดงเลือดนก (บนพื้นเข้ม แดงเลือดนกเปลี่ยนเป็นชมพูกุหลาบของโลโก้ เพราะแดงบนพื้นเข้มอ่านไม่ออก)
3. **ชื่อบริษัทเขียนว่า D.A. มีจุดเสมอ** ทุกภาษาใช้ชื่ออังกฤษไปก่อน
4. **ลวดลาย:** รอบนี้ใช้ 4 ลายที่ล็อกไว้ เจ้าของกิจการอาจขอลายเพิ่มภายหลัง (ดูข้อ 3)

---

## 2. Owner decisions (6 October 2026)

| # | Question | Decision |
|---|---|---|
| 1 | Imagery for #35 | Use the locked brand pieces now (logo 153, seal 346, patterns 401 · 406 · 417 · 420, paper grain). **Owner note, kept for later:** four patterns may be too few and could feel repetitive, so more patterns beyond the locked four may be needed. Revisit **only when the owner raises it** once patterns are tried on the website. #36 stays open for this. |
| 2 | Figure colour (brass in #33 vs the seal, which has no brass) | **Show both in context and let the owner choose.** Brass: `#7d5f28` on paper, `#c4a06a` on dark. Oxblood: `#7a2229` on paper; on dark surfaces the logo's rose (`#BE9491` / `#C29998`), because oxblood on dark is 2.2:1. |
| 3 | How to review | **Two rounds.** Round 1: homepage + one Admin screen, all three directions, EN/TH/ZH, day/night, desktop/phone, rated dimension by dimension. Round 2: the remaining pages (services, tax calendar, article, contact) in the winning direction. |
| 4 | Firm name | **"D.A." with dots, always** (owner correction). English name on every language page until Thai and Chinese names are supplied. |

## 3. Round 1 board

D.A. Visual Directions (private artifact): https://claude.ai/artifact/CAdrbjPVRMLb44ixXLzxLM
Source: `docs/decisions/35-visual-directions/round1.html`. Assets are published from `brand/` and `brand/export/svg-compatible/` unchanged.

- **Screens:** homepage (header, hero, October filings table, services, outcome band, October 2026 month grid, insights, contact, footer) and the Admin Dashboard (#24 shell: Thai labels with English underneath, page tree with TH/EN/ZH status, "Needs attention", live preview, versions; phone = check and publish).
- **Switches:** direction A/B/C (keys 1/2/3 keep the scroll position), screen, language, mode, device, figure colour, replay motion.
- **Ratings:** 15 dimensions × A/B/C (Like / No / ★ best), figure colour, and which direction carries into round 2. Saved to the artifact's database (`ratings/round1`), so Claude reads them directly.

| | A Maison | B Atelier | C Haute Contrast |
|---|---|---|---|
| Latin | Cormorant Garamond 400 + Newsreader | Cormorant Garamond 500 + Hanken Grotesk | Cormorant Garamond 600 + Source Serif 4 |
| Thai | Trirong 400 + Taviraj | Trirong 400 + IBM Plex Sans Thai Looped | Trirong 600 / 400 |
| Chinese | Noto Serif SC 400 | Noto Serif SC 500 + Noto Sans SC | Noto Serif SC 600 / 400 |
| Oxblood | Bar, one deep band, stitched footer | Oxblood opening, full alternation | Deep bands lead |
| Imagery | Seal in a double frame on 406 quiet | 417 canvas, 401 ribbon | 420 night panel, largest seal |
| Motion | Fade | Short rise | Short rise |

**Content notes:** contact details are samples. The October dates are shown as statutory paper dates (7th, 15th) and online dates that depend on the Revenue Department's e-filing extension being in force; 13 and 23 October 2026 are public holidays, so VAT online moves to Monday 26 October. **Check these dates before any real publication.**

## 4. Browser checks from #34 §9 run this session

| # | Check | Result |
|---|---|---|
| 11 | Cormorant Garamond figures | **Old-style by default**, with `lnum` and `tnum` available. Tables use `lining-nums tabular-nums`. x-heights (share of em): Cormorant 0.386 · Newsreader 0.426 · Source Serif 4 0.475 · Hanken Grotesk 0.493 · Trirong 0.498 · Taviraj 0.470 · IBM Plex Sans Thai Looped 0.516. Thai display is scaled to 0.84 and body to 0.95 next to the Latin face. |
| 12 | Rendered specimen at desktop and 390 px | Rendered in Chromium for all three directions, EN/TH/ZH, day/night: no console errors and no sideways scrolling. Windows ClearType and iPhone were not available. |
| 1–10, 13–17 | Live brand sites, foundry prices, CLS | Not run: the proxy still blocks those sites. |

## 4b. Fixes made during the check

- Thai and Chinese headlines broke in the middle of a word at desktop width. They now break at phrase boundaries.
- The Thai menu wrapped below about 1100 px. The language switch now moves out of the bar at that width.

## 5. Next

1. The owner rates round 1 on the board.
2. Claude reads `ratings/round1`, records the result here, and builds round 2 in the winning direction.
3. When the ticket closes: record Theme #1 tokens and the font choice for #15.
