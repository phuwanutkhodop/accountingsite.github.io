# 33 — Brand feeling

**Ticket:** GitHub issue #33 (Wayfinder grilling)
**Date:** 5 October 2026
**Decided by:** the owner, in a grilling session with Claude
**Status:** **in progress.** Term 1 ("minimal premium, not modern"): **colour locked (O1 light + O9 dark, switchable)**; fine-detail picks pending. Term 2 ("bold & confident") not started.

---

## 1. สรุปสำหรับเจ้าของกิจการ (ภาษาไทย)

1. **เลิกใช้อัตลักษณ์เดิมทั้งชุด** ทั้งเว็บและ Admin (สี Navy & Soft Linen และฟอนต์ Instrument Serif + Inter)
2. **ความรู้สึกที่ต้องการ:** เรียบ หรู แต่ไม่ "โมเดิร์น" และกล้า มั่นใจ
3. **โลกที่ใกล้ที่สุด:** แบรนด์หรูระดับ luxury house (เช่น Hermès, Aesop)
4. **ความหรูมาจาก:** พื้นที่ว่างและความยับยั้ง + รายละเอียดประณีตและผิววัสดุ
5. **ห้ามใช้:** การ์ดมุมมนกับเงานุ่ม · ไล่สี กระจก แสงเรือง · ตัวไม่มีเชิงทั้งเว็บ · ภาพการ์ตูนและไอคอนเรียงแถว
6. **สีที่เลือก:** Oxblood Library — **โหมดสว่างใช้ O1 (แดงเลือดนกต้นฉบับ) โหมดมืดใช้ O9 (ห้องสมุดยามค่ำ) และสลับไปมาได้**

---

## 2. Decisions so far

| # | Question | Decision |
|---|---|---|
| 1 | Scope of the change | **Website and Admin, fully new.** Navy & Soft Linen and Instrument Serif + Inter are retired. The old site stays only as the content and structure test bed. |
| 2 | What is open | **Everything:** colours, fonts, spacing, buttons, cards, motion. |
| 3 | Feeling | **Minimal and premium, but not "modern"** + **bold and confident.** Each term is defined separately, one at a time (owner request). |
| 4 | Process | Define the feeling here → benchmark research (#34) → three complete directions (#35) → owner picks. |
| 5 | "Not modern" rules out | Rounded cards and soft shadows · gradients, glass and glow · sans-serif everywhere · illustrations and icon grids · plus "something else" the owner has not yet named. |
| 6 | Reference world | **Luxury house** (Hermès, Aesop, high-end watchmakers): warm, crafted, editorial, a sense of material and care. |
| 7 | Where "premium" comes from | **Space and restraint + fine detail and material.** The owner asked for "fine detail and material" to be defined in depth. |
| 8 | Colour | Owner rejected abstract colour moods: colour must be answered as **complete colour sets that fit the concept**. Round 2 shows six sets in context. |
| 9 | Colour family | **B2 Oxblood Library** (owner, round 2). Owner asked for more variations within it → round 3. |
| 10 | Colour, final | **Two modes, switchable:** light = **O1 Oxblood** (original B2), dark = **O9 Night Library** (owner, round 3). |

---

## 3. Round 2 board

Material & Colour Board (private artifact): https://claude.ai/artifact/AM3Hw44F3BtdrVuxYx8Svg

- **Part A:** twelve fine-detail techniques (A1 hairline rules · A2 letter-spaced capitals · A3 double-rule frame · A4 old-style aligned figures · A5 editorial initial · A6 paper grain · A7 blind emboss · A8 monogram seal · A9 Roman section numbers · A10 margin notes · A11 material field with stitch line · A12 deliberate emptiness).
- **Part B:** six colour sets with six roles each (paper, ink, muted, hairline, signature, deep), shown on the same page: B1 Saddle & Parchment · B2 Oxblood Library · B3 Forest & Brass · B4 Ink & Bone · B5 Celadon & Stone · B6 Lacquer & Gold Leaf.

Fonts on the board are stand-ins; fonts are chosen in #35.

---

## 3b. Round 3 board

Oxblood Variations (private artifact): https://claude.ai/artifact/NSoC9wSWwFsg7QDKSh5Lz8

Nine variations, one axis at a time, each with a WCAG contrast check:

- **The red:** O1 Oxblood (original) · O2 Cordovan (browner) · O3 Bordeaux (purpler) · O4 Seal-paste Cinnabar (brighter, Chinese seal red)
- **The paper:** O5 on cream · O6 on stone grey
- **Partner colour:** O7 + brass · O8 + library green
- **Dark-first:** O9 Night Library. Oxblood is too dark for text on dark paper (2.2:1), so it is used only as fills there.

All light variations pass AA for body text, muted text and button text. O7's brass figures pass for large text only (4.3:1).

## 3c. Locked palette (round 3)

| Role | Light — O1 Oxblood | Dark — O9 Night Library |
|---|---|---|
| Paper (page background) | `#f2eeea` | `#1b1112` |
| Ink (body text) | `#1e1a1a` | `#efe6dc` |
| Muted text | `#675e5c` | `#b9aaa0` |
| Hairline | `#d6ccc4` | `#4a3232` |
| Oxblood (buttons, rules) | `#7a2229` | `#8f2a31` |
| Text on oxblood | `#f6efe8` | `#f6efe8` |
| Figures & seal | `#7a2229` | `#c4a06a` (brass) |
| Deep band | `#3a1316` | `#4b171c` |
| Text on deep band | `#f2e8e0` | `#f2e8e0` |

Contrast (WCAG): light ink 14.9, muted 5.5, oxblood text 8.7, button 8.8, band 13.5. Dark ink 15.0, muted 8.2, button 7.2, brass figures 7.6, band 12.1. **Dark-mode rule:** oxblood (2.2:1 on dark paper) is never a text colour, only a fill.

**Consequences for the builder (Claude, technical):**

- Light/dark is a **theme-level feature**: `theme.json` carries two token sets per site and the generator emits both. Every preset in the Design Library must render correctly in both modes and pass contrast in both (#13 governance, #30 checks).
- A preset's "colour mode" override (decision #10: light / dark / band) is relative to the active mode, so a "deep band" section stays a contrasting band in either mode.
- The Admin uses the same pair (#24, decision 4).
- The mode switch needs no server: the visitor's choice is remembered in their browser; pages must render correctly with JavaScript off (decision #11) using the device setting.

## 4. Still open

- Fine-detail picks from round 2 Part A (A1–A12).
- What "something else" on the "not modern" list is.
- Term 2: "bold and confident", defined the same way, on top of term 1.
- How "minimal" and "bold" coexist.
- Default mode for a first-time visitor, and whether the brand detail colour (figures, seal) should differ between modes. Round 4 preview, Oxblood Day & Night: https://claude.ai/artifact/SrYLgdiHfgFyCmFwHUAzyL. Options: A oxblood day / brass night (as chosen) · B brass both (`#7d5f28` day, AA 5.1) · C oxblood both (rose-oxblood `#c98288` night, 6.2).
