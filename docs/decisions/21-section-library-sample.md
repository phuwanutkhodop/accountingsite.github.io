# 21 — Section library sample: the preset format, proven

**Ticket:** GitHub issue #21 (Wayfinder prototype)
**Date:** 6 October 2026
**Decided by:** Claude, under the owner's standing delegation of technical choices (map #1). The owner reviews the sample for quality (§6).
**Inputs:**
- decisions #11 (rendering), #13 (Design Library), #15 (type system), #16 (stack) and #31 (library repo);
- plan review finding **M16** (colour-mode names).

**Prototype:** [Section Library Sample](https://claude.ai/artifact/KXF9kgSGvYtTJFXS46CUQC) (private). Source: [`21-section-library-sample/prototype/`](./21-section-library-sample/prototype/).
**Status:** the **format** half is locked and resolves M16. **The quality half failed the owner's review (6 October 2026):** the nine presets are generic placeholders, "far from professional; nobody would pay for this". The ticket is reopened. Real presets will come from visual research of top professional work (§8).

---

## 1. สรุปสำหรับเจ้าของกิจการ (ภาษาไทย)

1. **โครงสร้างคลังดีไซน์ใช้งานได้จริง** ต้นแบบมี section 3 ชนิด (เปิดหน้า · บริการ · ติดต่อ) ชนิดละ 3 ดีไซน์ ทำงานได้ครบ 3 ภาษา ทั้งบนจอคอมพิวเตอร์และมือถือ
2. **ดีไซน์ชุดเดียวกันเปลี่ยนหน้าตาได้ด้วยธีมอย่างเดียว** สลับธีม A (เรียบ ไม่มีเชิง มุมมน) กับธีม B (มีเชิง มุมเหลี่ยม แบบหนังสือ) แล้ว HTML ไม่เปลี่ยนเลย
3. **ระบบตรวจดีไซน์อัตโนมัติจับข้อผิดพลาดได้จริง** ทดสอบด้วยดีไซน์ที่ตั้งใจทำผิด 9 แบบ ระบบจับได้ครบทั้ง 9 แบบ ความคมชัดของสีทุกธีม ทุกโหมดสี และทุกพื้น ผ่านเกณฑ์ทั้งหมด (ต่ำสุด 6.07:1 เกณฑ์คือ 4.5:1)
4. **ตั้งชื่อเรื่องสีให้ชัด:**
   - "โหมดสี" ของทั้งเว็บ มี สว่าง · มืด · ตามเครื่องผู้อ่าน
   - "พื้น" ของแต่ละ section มี พื้นปกติ · พื้นอ่อน · พื้นเข้ม
5. **ปัญหาหัวข้อไทยตัดกลางคำแก้ได้แล้ว** ใส่ตัวเชื่อมคำที่มองไม่เห็นระหว่าง "ตัดสิน" กับ "ใจ" แล้วคำไม่ถูกตัด ตัวแก้ไขในอนาคตจะมีปุ่ม "ให้คำนี้อยู่ด้วยกัน"
6. **สิ่งที่ขอให้คุณทำ:** เปิดหน้าตัวอย่าง แล้วบอกผมว่าดีไซน์ไหนยังดูไม่ถึงระดับมืออาชีพ และธีมทดสอบทั้งสองดูเป็นกลางพอหรือไม่
7. **ที่เก็บคลังดีไซน์ (builder-library) ยังไม่ต้องสร้างตอนนี้** ต้นแบบนี้ไม่ต้องใช้ จะสร้างตอนเริ่มเขียนดีไซน์จริงชุดแรก

---

## 2. What changes in the preset format

The record shape of #13 §3.2 holds. The prototype adds these rules; each is checked automatically.

| # | Change | Why |
|---|---|---|
| 1 | **Presets carry their own `css`.** <br>• Every selector starts with the preset's prefix class. <br>• Colours, fonts, font sizes, spacing, radii and shadows must be `var(--token)`; only `0`, `1px`, `2px` and keywords may be literal. <br>• Layout geometry may be literal: grid tracks, `ch` measures, aspect ratios. <br>• No `@media`, `@import` or `url()`. | Presets need styling, and #13's "no literal values" needed a precise, checkable form. Geometry is part of the design itself, not of the theme. |
| 2 | **The root element is `<div class="s__in <prefix>">`.** The generator writes the wrapping `<section class="s tone-…" id="…" data-preset="id@version">`. | The anchor id (#14), the tone, `hiddenIn` and the version stamp belong to the instance, so no preset can get them wrong. |
| 3 | **Responsive rules use container queries,** `@container section (min-width: …)`, at three shared breakpoints: `40rem`, `48rem`, `64rem`. Theme sizes use `cqi`. | A preset then lays out by the width it is given. The Admin's narrow panes, its device preview and the library thumbnails all render correctly without resizing a frame. A short shared list keeps presets consistent. |
| 4 | **`tone` is a universal option:** `plain`, `tinted` or `bold` (พื้นปกติ · พื้นอ่อน · พื้นเข้ม). The theme defines every colour token for each tone in each scheme. In the dark scheme, `bold` becomes a light band. **The site's colour scheme is light, dark or follow-the-device,** with a visible switch on the site. | Resolves review M16: one name for a section's ground, another for the site's scheme. It replaces "light/dark/linen" (#10) and "light/dark/band" (#33). |
| 5 | **Field kinds expand into template values:** <br>• `link` → `href`, `label`; <br>• `image` → `src`, `alt`, `w`, `h` (`srcset` with #27); <br>• `phone` → the display form plus `phoneE164` for `tel:`. <br>Options are read as `{{opt.*}}`; system strings as `{{t.*}}`. | Templates stay logic-less (#11 §3.8), and the check can list exactly which names each template may read. |
| 6 | **The generator supplies system strings** per language, such as "Phone" / "โทรศัพท์" / "电话", as `{{t.*}}`. | Labels that are not the owner's content must still be trilingual. |
| 7 | **A small shared base is part of the contract:** `.s`, `.s__in`, `.lead`, `.eyebrow`, `.actions`, `.btn`, `.btn--quiet`, plus the #15 type system. It ships with the engine; changing it is an engine release, checked against every preset. | Without it, nine presets would hold nine copies of the same button. |
| 8 | **Preset `constraints` may tighten their type:** `hero-split` requires an image; `hero-figures` requires two to four figures. | One section type serves designs with different needs. |
| 9 | **The theme token contract** (what every theme must define): <br>• colours `bg surface text muted rule accent onAccent` × 3 tones × 2 schemes; <br>• font roles and weights (#15); <br>• sizes `display-xl display-1 h2 h3 lead body ui small figure`; <br>• spaces `1–8`, `section`, `gutter`; <br>• radii `control card media`; <br>• the page measure; <br>• eyebrow case and tracking. | It is the minimum that let two themes as different as A and B restyle the same nine presets. |

## 3. What the prototype proved

| Claim | Evidence |
|---|---|
| The same HTML restyles from tokens alone | Theme A (sans, rounded, tight) and theme B (serif, square, generous) on identical markup: shapes, type, density and colour all change. |
| The library check works | **9 deliberately broken presets, 9 caught:** raw output `{{{…}}}`, a partial, an undeclared field, a literal colour, a literal font size, an unscoped selector, an odd breakpoint, an `onerror` handler, a literal font family. |
| Contrast holds everywhere | 2 themes × 2 schemes × 3 tones × 6 pairs (text, muted, accent, on-accent, on-surface) all ≥ 4.5:1; the lowest is **6.07:1**. |
| Trilingual and responsive | EN, TH and ZH at 1280 px and 390 px: no horizontal overflow and no script errors in Chromium. Thai marks are not clipped. |
| The strict template engine is enough | Nine real designs needed only variables, sections, inverted sections and dotted names. About 80 lines, pure, no DOM. |
| Thai "keep together" works | `ตัดสิน⁠ใจ` with U+2060 between the two words is no longer broken across lines (Chromium; desktop and phone). This confirms the #26 proposal. |

## 4. The quality bar for real presets

A preset enters `builder-library` only when **all** of these hold:

1. **The library check passes** (§2 rules and #13 §3.3). It runs in `node --test` and in the Admin before save-back.
2. **Contrast:** every text pair it uses is ≥ 4.5:1 in every tone it allows, in both schemes, in every library theme.
3. **Length stress:** it renders without overflow or clipping with every field at its `maxLength` in each language, at container widths 320, 390, 768 and 1280.
4. **Visual review in both test themes and both schemes,** with real-sounding content in all three languages. No sample text that reads like a template.
5. **Semantics:** only opening presets carry an `h1`; others start at `h2`. Lists are `ul` or `dl`. Every image has `alt` or the *decorative* flag. Every link has a real target.
6. **Works with JavaScript off;** no script in markup.
7. **Keyboard focus is visible** on everything it makes clickable (the shared base supplies this).
8. **Name and purpose in Thai, English and Chinese,** and one primary category (#13 §2-3).

## 5. The neutral test themes

- **Theme A "Slate"** (`test-slate`): the sans pairing of #15, cool neutral greys, a steel-blue accent, rounded controls. It is the builder's default test theme.
- **Theme B "Paper"** (`test-paper`): the serif pairing of #15, warm neutral, a deep green accent, square corners, more generous spacing. It is the second theme that proves swapping.
- Neither borrows from the firm's brand (route correction, 2026-10-06). Both are placeholders.

## 6. Owner review (pending)

Open the sample. Switch theme, colour, language and width, and report:
1. any design that does not look professional (name it);
2. whether the two test themes look neutral enough;
3. whether Thai and Chinese look as finished as English.

A complaint about a design changes that preset, not the format.

## 7. Effects on other tickets and documents

- **#13:** §3.2 gains the rules in §2 here; §3.3's check is extended by the CSS and name rules.
- **#10 decision 5a and #33:** the colour-mode names are replaced by §2-4 (M16).
- **#26:** the "keep together" mark is confirmed in Chromium; check Safari and Firefox there.
- **#22:** the Admin preview can render presets at any width directly, thanks to container queries. The library screen uses the same check report.
- **#29:** the site setting "colour scheme: light / dark / follow device" lives in Settings.
- **#31 §8:** `builder-library` is needed when the first **real** presets are written, not for this prototype. That owner step moves to the build phase.

## 8. Owner review, 6 October 2026: not commercial grade

**Owner's verdict:** the sample is far from professional. Squares, rounded buttons and standard layouts are worth nothing, because nobody would pay for them.

**The owner's direction for the real library:**
- study the work of top professional designers **by looking at it**, not from descriptions;
- skip what is standard;
- collect what is **scarce and distinctive** in the economic sense: details few sites have, which is what makes work worth paying for;
- build those into real presets.

**What stands from this ticket:**
- the format (§2);
- the library check;
- the test themes, as plumbing only.

**What does not stand:**
- the nine presets as designs;
- §4 as the whole quality bar. It is a floor, not a bar. The real bar comes from the visual research.

**Blocker:** the session's network policy refuses every design gallery, studio site and brand site tried, among them Awwwards, Behance, Dribbble, Pentagram, Aesop, Pictet and Stripe. The owner must widen the network access before the research can start.
