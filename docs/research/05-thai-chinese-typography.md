# 05 — Thai & Simplified-Chinese typography for the Navy & Soft Linen site

**Ticket:** Wayfinder research issue #5 · **Date:** 2026-10-05 · **Status:** research only — no theme files changed.
**Locked Latin pair (do not change):** Instrument Serif (headings) + Inter (body).

Measurements marked **[measured]** were taken on 2026-10-05 by downloading the live CSS from `fonts.googleapis.com` and reading `Content-Length` of every WOFF2 slice on `fonts.gstatic.com` (Chrome user-agent, so WOFF2 + `unicode-range` were served). Other facts are cited inline.

---

## 1) สรุปสั้น ๆ ภาษาไทย (10 บรรทัด)

1. เว็บไซต์ของเราใช้ฟอนต์ภาษาอังกฤษ 2 ตัวที่ล็อกไว้แล้ว คือ Instrument Serif (หัวข้อ) และ Inter (เนื้อหา) แต่ทั้งสองตัว**ไม่มีตัวอักษรไทยและจีน** จึงต้องมีฟอนต์ "คู่หู" สำหรับสองภาษานี้
2. สำหรับภาษาไทย แนะนำคู่หลักคือ **Trirong** (หัวข้อ — ตัวมีหัว เส้นหนาบางเหมือน Instrument Serif) + **Sarabun** (เนื้อหา — ตัวมีหัว อ่านง่าย เป็นฟอนต์ที่ราชการไทยใช้) ทั้งคู่ฟรี ใช้เชิงพาณิชย์ได้ (สัญญาอนุญาต OFL)
3. ตัวเลือกสำรองคือ **Taviraj + IBM Plex Sans Thai Looped** (ทางการ นุ่มกว่า) และ **Noto Serif Thai + Noto Sans Thai Looped** (ปลอดภัยสุด แต่บุคลิกน้อยกว่า)
4. ไม่ควรใช้ Kanit, Prompt, Mitr, Chakra Petch, Bai Jamjuree, Charm, Srisakdi, Niramit, K2D ในเว็บสำนักงานบัญชี — เป็นฟอนต์แนวโฆษณา/แฟชั่น หรือตัวไม่มีหัวแบบวัยรุ่น ไม่เหมาะกับความน่าเชื่อถือแบบวิชาชีพ
5. สำหรับภาษาจีน แนะนำ **Noto Serif SC** (หัวข้อ — ตัวซ่ง/明朝 คู่กับ serif อังกฤษ) + **Noto Sans SC** (เนื้อหา — ตัวเฮย/黑体 คู่กับ Inter) ฟรี OFL เช่นกัน
6. ฟอนต์จีนมีขนาดใหญ่มาก (ไฟล์เต็ม 2–3 MB ต่อน้ำหนัก) แต่ Google Fonts หั่นเป็นชิ้นเล็ก ๆ 101 ชิ้น เบราว์เซอร์ดาวน์โหลดเฉพาะชิ้นที่หน้านั้นใช้จริง — หน้าทดสอบที่มีตัวอักษรจีน ~200 ตัว โหลดจริงประมาณ 400–515 KB ต่อน้ำหนัก (วัดจริง)
7. ฟอนต์ไทยเล็กมาก ชิ้นภาษาไทยเพียง 7–16 KB ต่อน้ำหนัก — ไม่ต้องกังวลเรื่องขนาด
8. ภาษาไทยต้องตั้งระยะบรรทัดสูงกว่าภาษาอังกฤษ (เนื้อหาอย่างน้อย 1.6–1.75) เพราะมีสระบนและวรรณยุกต์ซ้อนกัน และต้องใส่ `lang="th"` ให้เบราว์เซอร์ตัดคำไทยถูกต้อง
9. ภาษาจีนก็ต้องการระยะบรรทัดกว้าง (1.7–1.8) ห้ามใช้ตัวเอียง และต้องใส่ `lang="zh-Hans"` เพื่อให้ได้รูปอักษรแบบจีนตัวย่อ ไม่ใช่แบบญี่ปุ่น
10. **คำถามสำคัญถึงเจ้าของกิจการ:** ลูกค้าจีนของเราส่วนใหญ่มาจากจีนแผ่นดินใหญ่ (ใช้ตัวย่อ 简体) หรือไต้หวัน/ฮ่องกง (ใช้ตัวเต็ม 繁體)? คำตอบนี้กำหนดว่าเราจะทำเวอร์ชันจีนแบบไหน

---

## 2) Candidate pairings

### 2.0 How the Latin pair "reads", so the Thai/Chinese partners can match it

| Property | Instrument Serif (headings) | Inter (body) |
|---|---|---|
| Classification | High-contrast, condensed-ish transitional/Didone-flavoured display serif; single weight (Regular + Italic) | Neutral grotesque/humanist-leaning sans, large x-height, open apertures, weights 400/500/600 in theme |
| Tone | Editorial, quiet, "old-money" professional — fits Navy & Soft Linen | Clean, trustworthy, UI-grade |
| What a partner must match | Visible thick/thin contrast; narrow-to-normal width; light overall colour on the page (we use weight 400 for headings) | Even stroke, generous x-height/loop-height, calm rhythm, 400–600 weights |

The theme currently lists `'Noto Serif TC','Noto Serif JP','Noto Serif Thai'` and `'Noto Sans TC','Noto Sans JP','Noto Sans Thai'` as fallbacks in `theme/theme.css` lines 130–131. Those names are **not loaded** by the `@import` on line 52 (only Instrument Serif + Inter are), so today Thai/Chinese text silently falls to system fonts. Also note TC/JP are listed although the target is Simplified Chinese; see §7.

### 2.1 Thai — triage of the required candidate list

Thai type has two families of letterform: **looped (มีหัว)** — the traditional form with small loops/"heads", used in books, official documents and body text — and **loopless (ไม่มีหัว)** — a modern simplification that resembles Latin sans letters, popular in advertising, branding and display. Cadson Demak's own descriptions on Google Fonts put it this way: "formal loopless Thai typefaces have more simple forms than the conservative looped Thai designs" (Kanit/Prompt descriptions) and "formal looped Thai typefaces have delicate details so it is not proper to extend to so many weights" (Trirong README). Loopless faces also raise confusability (ก ถ ภ ฤ ฦ, ฎ ฏ, บ ป, ข ช), which Cadson Demak flags on every loopless family. For a conservative accounting firm, **looped is the right default for body text**; a loopless face is acceptable only as a deliberate "modern" accent.

Facts below (designer, category, weights, description quotes) come from the `METADATA.pb` / `DESCRIPTION.en_us.html` files in the google/fonts repository (https://github.com/google/fonts/tree/main/ofl/) and the Cadson Demak GitHub READMEs.

| Font | Looped? | Google Fonts category / weights | Designer | Verdict for a conservative professional firm |
|---|---|---|---|---|
| **Noto Serif Thai** | Looped, modulated ("serif") | SERIF, variable wght 100–900, wdth 62.5–100 | Google | **Yes — heading or body.** Neutral, well-engineered, matches Noto Serif SC metrics if we want one "Noto" system. Less character than Trirong. |
| **Noto Sans Thai** | **Loopless** | SANS, variable wght 100–900, wdth 62.5–100 | Google | Caution. Google's own description: "mainly suitable for headlines, packaging and advertising". Not for body text here. |
| **Noto Sans Thai Looped** | Looped, unmodulated | SANS, variable wght 100–900, wdth 62.5–100 | Google | **Yes — body.** Google: "suitable for all texts". The safe body choice beside Inter. |
| **Sarabun** | Looped humanist sans | SANS (DISPLAY tag), 100–800 + italics | Suppakit Chalermlarp | **Yes — body (top pick).** It is TH Sarabun New under OFL — the font "used in the Government Gazette of Thailand"; the de-facto standard for Thai official/professional documents. Instantly signals formality to Thai readers. |
| **IBM Plex Sans Thai** | **Loopless** | SANS, 100–700 | Mike Abbink, Bold Monday (Thai by Mark Frömberg/Ben Mitchell) | Acceptable modern body; Plex and Inter share a neutral grotesque DNA. Loopless → second to the Looped cut. |
| **IBM Plex Sans Thai Looped** | Looped | SANS, 100–700 | same | **Yes — body.** Corporate, engineered, sits beside Inter very naturally; better loop-height/x-height match to Inter than Sarabun (Sarabun runs small on the body). |
| **Anuphan** | **Loopless** (a loopless Plex Thai drawn from Plex Latin) | SANS, variable wght 100–700 | Mint Tantisuwanna / Cadson Demak | Acceptable modern UI/nav face; same caveat as Noto Sans Thai for long reading. |
| **Taviraj** | Looped, thick/thin | SERIF (DISPLAY), 100–900 + italics | Cadson Demak | **Yes — heading (alt).** "wide structure… well-suited for formal usage… rounded and airy looped terminals". Softer, wider than Trirong. |
| **Trirong** | Looped, thick/thin | SERIF (DISPLAY), 100–900 + italics | Cadson Demak | **Yes — heading (top pick).** "narrow and tall structure echoes traditional Thai typefaces… Transitional serif Latin works well in formal contexts". Its narrow proportion and stroke contrast are the closest Thai analogue of Instrument Serif. |
| **Pridi** | Looped | SERIF slab (DISPLAY), 200–700 | Cadson Demak | Possible for pull-quotes only. Slab Latin + "informal" per README; too chunky beside Instrument Serif's hairlines. |
| **Bai Jamjuree** | Looped but "rounded rectangle silhouettes" (Eurostile-inspired) | SANS, 200–700 + italics | Cadson Demak (Rapee Suveeranont, Virot Chiraphadhanakul) | **No.** Square/techno headline face; "unorthodox detail" — wrong tone. |
| **Kanit** | Loopless geometric | SANS, 100–900 + italics | Cadson Demak | **No** for this brand. Ubiquitous in Thai startup/ad branding; "contemporary and futuristic". Clashes with a serif-led editorial system. |
| **Prompt** | Loopless geometric | SANS, 100–900 + italics | Cadson Demak | **No** — same reasoning as Kanit (wide, airy, poster-like). |
| **Mitr** | Loopless, rounded terminals | SANS, 200–700 | Cadson Demak | **No** — "friendly… casual usage such as celebration cards". |
| **Athiti** | Loopless, calligraphic | SANS, 200–700 | Cadson Demak | **No** — "informal sans"; handwriting trace. |
| **Chakra Petch** | Looped, square sans with tapered corners | SANS (DISPLAY), 300–700 + italics | Cadson Demak | **No** — techno/gaming look. |
| **K2D** | Looped, "modern appearance" | SANS (DISPLAY), 100–800 + italics | Cadson Demak | **No** — display/UI; rounded playful. |
| **Niramit** | Looped with "decorative details" | SANS, 200–700 + italics | Cadson Demak | **No** — decorative. |
| **Krub** | Looped, metal-type flavour | SANS, 200–700 + italics | Cadson Demak | Marginal. Interesting "less dusty traditional" body alternative, but its Latin is quirky and it has no weight ≥700. Keep as a wildcard for the specimen only if time allows. |
| **Thasadith** | Humanist sans, rounded corners | SANS (DISPLAY), 400/700 + italics | Cadson Demak | **No** — rounded corners read soft/casual; only two weights. |
| **Charm** | Handwritten (flat-tip pen) | HANDWRITING, 400/700 | Cadson Demak | **No** — "works well for Thai religious texts". |
| **Srisakdi** | Handwritten, Rattanakosin-era | DISPLAY, 400/700 | Cadson Demak | **No** — retrospective display. |

Sources: google/fonts METADATA & descriptions (https://github.com/google/fonts); Trirong README (https://github.com/cadsondemak/trirong); Taviraj README (https://github.com/cadsondemak/taviraj); Pridi README (https://github.com/cadsondemak/pridi); Bai Jamjuree README (https://github.com/cadsondemak/bai-jamjuree); Kanit (https://github.com/cadsondemak/kanit); Prompt (https://github.com/cadsondemak/prompt); Mitr (https://github.com/cadsondemak/mitr); Sarabun specimen (https://fonts.google.com/specimen/Sarabun); ThaiGraph Sarabun page on its government-document role (https://thaigraph.com/fonts/sarabun/); ThaiGraph loopless category (https://thaigraph.com/fonts/categories/loopless/); Wikipedia "National Fonts" (https://en.wikipedia.org/wiki/National_Fonts).

### 2.2 Thai pairings (recommended order)

**Pairing TH-A (recommended): Trirong (headings) + Sarabun (body)**
- *Why it sits beside Instrument Serif:* Trirong is the only free Thai serif whose **narrow, tall structure and thick/thin modulation** echo Instrument Serif's condensed, high-contrast display feel. Use weight 400 (and Trirong 500 if 400 looks too light next to Instrument Serif at small heading sizes — Thai hairlines thin out faster than Latin). Trirong's own Latin is a transitional serif, but we will never show it: `unicode-range` keeps Trirong for U+0E01–0E5B only, so Instrument Serif still sets any Latin inside a Thai heading.
- *Why Sarabun beside Inter:* both are neutral, even-stroked, humanist-leaning sans faces. Sarabun's looped forms carry the "official document" cue Thai readers expect from an accounting firm (it is literally the Government Gazette face). Weights 400/500/600 exist to mirror Inter's.
- *Watch-outs:* Sarabun's loop-height/x-height is **smaller** than Inter's; Thai body set in Sarabun at the same `font-size` as Inter looks ~8–10 % smaller. Use `size-adjust` on the Sarabun `@font-face` (≈108–110 %, confirm in the specimen) or bump `--text-base` on `:lang(th)`. Sarabun 100–300 are too thin on Soft Linen backgrounds; never go below 400 for text.
- *Size [measured]:* Thai slice 9.6 KB (Sarabun 400), 16 KB (Trirong 400). Trivial.

**Pairing TH-B (alternate, softer): Taviraj (headings) + IBM Plex Sans Thai Looped (body)**
- Taviraj is wider and airier than Trirong; it pairs well with Instrument Serif's *italic* and reads a touch friendlier — good if the owner finds Trirong too austere. Still formal per Cadson Demak.
- IBM Plex Sans Thai Looped is a true corporate-grade companion to Inter: engineered terminals, large loop-height, 400/500/600 available; it keeps Thai and Latin body text at near-identical visual size without `size-adjust`. Its one drawback is that Plex Thai is slightly "wider/colder" than Sarabun and lacks the governmental association.
- *Size [measured]:* Taviraj 400 Thai slice 15.7 KB; Plex Looped 400 Thai slice 13.3 KB.

**Pairing TH-C (safe/uniform): Noto Serif Thai (headings) + Noto Sans Thai Looped (body)**
- One design system, variable fonts (weight 100–900, width 62.5–100 — the condensed widths let us tune Noto Serif Thai to Instrument Serif's narrowness), and shared vertical metrics with Noto Serif/Sans SC if we go Noto for Chinese too. Lowest design risk, lowest personality; Noto Serif Thai's contrast is gentler than Instrument Serif's, so headings may look slightly heavier than Latin headings.
- *Size [measured]:* Noto Serif Thai 400 Thai slice 9.6 KB; Noto Sans Thai 400 Thai slice 8.9 KB (Looped variant comparable).

**Explicitly not recommended as a pairing:** anything loopless for body (Noto Sans Thai, Anuphan, Plex Sans Thai, Kanit, Prompt). If the owner wants a modern accent later, Anuphan 500 for **navigation/buttons only** is the least-bad loopless option because its skeleton is Plex (close to Inter).

### 2.3 Chinese — triage of the required candidate list

Facts from google/fonts metadata and project READMEs unless noted.

| Font | Style | Script | License / where | Verdict |
|---|---|---|---|---|
| **Noto Serif SC** | Song/Ming (宋体) — modulated; same design as Adobe **Source Han Serif** (思源宋体) | Simplified (also covers kana, Hangul, Latin, Cyrillic, Greek) | OFL; Google Fonts; variable wght 200–900 | **Yes — headings.** The natural Chinese analogue of a Latin serif: horizontal hairlines + heavy verticals = stroke contrast like Instrument Serif. |
| **Noto Sans SC** | Hei (黑体) — unmodulated; same design as Adobe **Source Han Sans** (思源黑体) | Simplified | OFL; Google Fonts; variable wght 100–900 | **Yes — body.** Neutral grotesque, open counters, metrically coordinated with Noto Serif SC. The Chinese Inter. |
| Source Han Serif / Source Han Sans | Identical designs to Noto Serif/Sans CJK (Adobe builds) | SC/TC/JP/KR | OFL; GitHub (adobe-fonts) | Same fonts, different packaging; use the Noto builds because Google Fonts slices them for us. |
| **Noto Serif TC / Noto Sans TC** | Same families, Traditional glyph forms | Traditional (Taiwan standard) | OFL; Google Fonts (108 slices per weight [measured]) | Only if §7 question resolves to Taiwan/HK. |
| **Chiron Sung HK / Chiron Hei HK** | Source Han Serif/Sans re-cut with Hong Kong/"modern stroke" glyph forms | **Traditional (HK)** | OFL-1.1; GitHub (chiron-fonts); added to Google Fonts 2025-05 (118/122 slices [measured]) | Good choice **only for a Traditional/HK audience**; irrelevant for Simplified. Keep in the TC contingency list. |
| **LXGW WenKai (霞鹜文楷)** | Kai/楷 (regular-script, brush-like) derived from Fontworks Klee One | SC (GitHub) / TC (Google Fonts "LXGW WenKai TC", 300/400/700) | OFL-1.1; README warns some corporate legal teams won't accept OFL without a "license certificate" | **No for headings/body.** Handwritten/literary tone; unsuited to an accounting firm. Could label a single pull-quote at most. |
| **ZCOOL XiaoWei (站酷小薇)** | Display, brush-flavoured "logo-ready" face, 1 weight, no Latin pairing | SC | OFL; Google Fonts (92 slices, 3.2 MB full [measured]) | **No.** Logo/display face; "intended to help fill the dearth of logo-ready Chinese display fonts". |
| **Ma Shan Zheng (马善政)** | Calligraphic brush script, 1 weight | SC | OFL; Google Fonts | **No.** Festive "yinglian" couplet style. |
| **Huiwen-mincho (匯文明朝體)** | Ming/Song, Japanese-mincho-flavoured, derived from Source Han Serif + Japanese glyphs | Mixed SC/TC/JP shapes | OFL (derivative of Source Han Serif); GitHub only, not on Google Fonts; glyph forms lean Japanese | **No** — regional glyph shapes would look "off" to mainland readers; and no CDN slicing. |
| Other free SC options worth knowing | **Smiley Sans (得意黑)** — oblique display sans, OFL, trendy; **Alibaba PuHuiTi 3.0** — free commercial Hei, but *not* OFL (Alibaba's own license), no Google Fonts; **HarmonyOS Sans SC** — Huawei license, not OFL | SC | — | None beats Noto for a conservative firm; listed so the choice is seen to be deliberate. |

### 2.4 Chinese pairings (recommended order)

**Pairing ZH-A (recommended): Noto Serif SC (headings) + Noto Sans SC (body)**
- This is the conventional Song-for-headings / Hei-for-body split that Chinese editorial design uses, and it maps one-to-one onto serif-heading / sans-body in the Latin system. Beside Instrument Serif, use **Noto Serif SC 400–500** (Chinese serif at 400 looks lighter than Latin at 400 because hairlines are very thin; test 500). Beside Inter 400/500/600 use **Noto Sans SC 400/500/700** (Noto Sans SC has no 600 static instance on the CDN; 700 is the bold).
- Vertical alignment: CJK glyphs fill the em-box; Noto SC's ascender/descender are taller than Inter's, so mixed Chinese + Latin lines (e.g. "增值税 VAT 7%") need `line-height` set on the container, not on spans, to avoid line-box jumps.
- *Size [measured, per weight]:* full chinese-simplified coverage = 101 slices, **2,353 KB** (Sans 400), **2,403 KB** (Sans 700), **3,107 KB** (Serif 400). Real pages download only slices they use: a 241-distinct-character sample page (an accounting-firm homepage, 203 distinct Han characters) hit **14 slices = 400 KB (Sans 400)** and **14 slices = 515 KB (Serif 400)**.

**Pairing ZH-B (lighter contrast): Noto Serif SC (headings, 400) + Noto Serif SC (body, 400)**
- An all-Song page is common for law/accounting/finance brochures in Chinese and looks very "paper-like" against Soft Linen; it avoids loading a second CJK family (saves ~400 KB) but body Song at 16 px on low-DPI Windows renders thin and grey. Only viable if we set body to ≥17 px and test on Windows ClearType.

**Pairing ZH-C (sans-only, performance first): Noto Sans SC 500 (headings) + Noto Sans SC 400 (body)**
- Cheapest (one family), robust on every screen, but loses the serif-heading rhythm that defines the Latin design. Acceptable as a *fallback-only* strategy: let headings fall back to system Song (`SimSun`/`Songti SC`) and ship only Noto Sans SC.

**If the audience turns out Traditional (see §7):** replace with Noto Serif TC + Noto Sans TC (Taiwan standard forms) or Chiron Sung HK + Chiron Hei HK (Hong Kong forms). Same loading recipe; slice counts 108/118–122.

---

## 3) Loading recipe and size budget

### 3.1 Strategy

1. **Keep Google Fonts for everything** (consistent with the locked decision to load Instrument Serif + Inter from Google). Google Fonts already serves Thai families with a dedicated `thai` subset and CJK families pre-sliced into ~101–122 `unicode-range` slices (its ML-derived slicing — see https://github.com/black7375/font-range and the google/fonts Noto guidance issue https://github.com/google/fonts/issues/1684). The browser downloads only slices whose characters appear on the page. Self-hosting CJK would require us to run `pyftsubset` (https://fonttools.readthedocs.io/en/latest/subset/) to a 3,500-character set (~300–500 KB per weight per https://changethisfile.com/blog/font-subsetting-guide and https://github.com/CodePlayer/webfont-noto, whose "slim" builds are 0.31–3.68 MB) and keep that pipeline alive — more work for no gain on a static GitHub Pages site. **Decision: Google Fonts, no self-hosting.**
2. **Replace the single `@import`** in `theme/theme.css` with one `<link>` per language page (or a per-language `@import`) so the English pages never pay for Thai/Chinese CSS. `@import` also delays font discovery; `<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>` + `<link rel="stylesheet">` in `<head>` is faster.
3. **Request only needed weights.** Headings use weight 400 only (Instrument Serif has no bold). Body uses 400/500/600 (Inter). So:
   - Thai page: `Trirong:wght@400;500` + `Sarabun:wght@400;500;600` (+ Instrument Serif + Inter).
   - Chinese page: `Noto+Serif+SC:wght@400;500` + `Noto+Sans+SC:wght@400;500;700` (+ Instrument Serif + Inter).
4. **`display=swap` for body, and for headings too.** FOIT on CJK is catastrophic (3-second blank headings while a 500 KB slice set downloads); swapping from system Hei/Song to Noto is low-shift because both are full-em-box designs. For Thai, swapping Leelawadee UI/Thonburi → Sarabun causes a small loop-height jump; mitigate with `size-adjust`/`ascent-override` on a local fallback `@font-face` (see §4.3).
5. **Do not preload CJK slices** — we cannot know which slices a page needs; let the CSS drive it. Preloading the Thai slice *is* reasonable (one ~10–16 KB file per weight), but only after measuring; Google's slice URLs are stable but not guaranteed.
6. **Reading-order budget for a Chinese page:** keep each page's distinct Han character count low (reuse vocabulary, avoid rare characters in headings) — every new rare character can pull in another 20–40 KB slice.

### 3.2 Size budget table [measured 2026-10-05, WOFF2 via fonts.gstatic.com]

| Family (weight) | Slices served | Full family download | Thai slice only | Realistic first-page download |
|---|---|---|---|---|
| Noto Sans Thai 400 | 3 (thai, latin, latin-ext) | 24 KB | 8.9 KB | ~9 KB (Latin served by Inter) |
| Noto Serif Thai 400 | 3 | 28 KB | 9.6 KB | ~10 KB |
| Sarabun 400 | 4 (+vietnamese) | 35 KB | 9.6 KB | ~10 KB |
| Anuphan 400 | 4 | 35 KB | 7.3 KB | ~7 KB |
| IBM Plex Sans Thai Looped 400 | 4 (+cyrillic) | 38 KB | 13.3 KB | ~13 KB |
| Pridi 400 | 4 | 64 KB | 14.3 KB | ~14 KB |
| Trirong 400 | 4 | 67 KB | 15.9 KB | ~16 KB |
| Taviraj 400 | 4 | 71 KB | 15.7 KB | ~16 KB |
| **Thai page total (TH-A, 2 heading + 3 body weights)** | — | — | — | **≈ 60–65 KB** on top of the Latin fonts |
| Noto Sans SC 400 | 101 | 2,353 KB | n/a | **400 KB** (14 slices, 203 distinct Han chars) |
| Noto Sans SC 700 | 101 | 2,403 KB | n/a | ≈ 400 KB |
| Noto Serif SC 400 | 101 | 3,107 KB | n/a | **515 KB** (14 slices) |
| Noto Sans/Serif TC 400 | 108 | not measured | n/a | similar order |
| Chiron Hei HK / Sung HK 400 | 122 / 118 | not measured | n/a | similar order |
| ZCOOL XiaoWei 400 | 92 | 3,192 KB | n/a | rejected |
| LXGW WenKai TC 400 | 115 | 4,526 KB | n/a | rejected |
| **Chinese page total (ZH-A, Serif 400 + Sans 400/500)** | — | — | — | **≈ 1.2–1.4 MB first visit**, then cached; ≈ 0.9 MB if we drop Sans 500 |

Reference points from the field: "Noto Sans SC … ~22,000 glyphs … ~16 MB TTF, ~6 MB WOFF2; top-3000 subset 300–500 KB" (https://changethisfile.com/blog/font-subsetting-guide); Noto Sans CJK JP full files "about 13 MB" each (https://github.com/notofonts/noto-cjk/issues/229 thread; https://en.wikipedia.org/wiki/Noto_fonts). Google Fonts' CJK slicing is described at https://github.com/black7375/font-range and in https://github.com/vercel/next.js/discussions/47309.

**Budget recommendation:** Thai ≤ 80 KB of extra font per page (easily met). Chinese ≤ 1.0 MB extra on first view: ship **Noto Serif SC 400 + Noto Sans SC 400 only** at launch (≈ 0.9 MB on the sample page), add Sans 500/700 only if the design needs them. Numerals/Latin inside Chinese text are served by Inter, which keeps the CJK fonts out of the critical path for prices and dates.

### 3.3 Recipe (for the prototype ticket — not applied here)

```html
<!-- th/index.html -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet"
  href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter:wght@400;500;600&family=Trirong:wght@400;500&family=Sarabun:wght@400;500;600&display=swap">
```
```css
/* theme/theme.css additions — order matters: Latin font first, script font second */
:lang(th)      { --font-heading: 'Instrument Serif', 'Trirong', 'Noto Serif Thai', 'Leelawadee UI', 'Thonburi', Georgia, serif;
                 --font-body:    'Inter', 'Sarabun', 'Noto Sans Thai Looped', 'Leelawadee UI', 'Thonburi', 'Tahoma', system-ui, sans-serif; }
:lang(zh-Hans) { --font-heading: 'Instrument Serif', 'Noto Serif SC', 'Source Han Serif SC', 'Songti SC', 'SimSun', serif;
                 --font-body:    'Inter', 'Noto Sans SC', 'Source Han Sans SC', 'PingFang SC', 'Microsoft YaHei', 'Hiragino Sans GB', system-ui, sans-serif; }
```
Because Instrument Serif and Inter contain no Thai/Han glyphs, the browser falls through to the second family for those code points only — this is the standard "Latin first, script second" ordering (see https://chenhuijing.com/blog/chinese-web-typography/ and https://chenhuijing.com/blog/font-face-fun-times/). All paths stay relative; Google Fonts URLs are external resources and allowed by the project rules (the current theme already uses them).

---

## 4) Fallback stacks

### 4.1 Thai system fonts
| Platform | Default Thai UI/body font | Other Thai fonts present | Looped? |
|---|---|---|---|
| Windows 8.1 / 10 / 11 | **Leelawadee UI** (UI font; Regular/Semilight/Bold); Tahoma also covers Thai | Leelawadee, Cordia New, Angsana New, Browallia New, the *UPC family (Dillenia, Eucrosia, Freesia, Iris, Jasmine, Kodchiang, Lily), Microsoft Sans Serif | Leelawadee UI: loopless-ish modern; Tahoma: looped; Angsana New: looped serif (the old "official document" face) |
| macOS | **Thonburi** (system Thai) | Ayuthaya, Krungthep, Sathu, Silom, Sukhumvit Set | Thonburi: looped; Sukhumvit Set: loopless |
| iOS / iPadOS | **Thonburi** | Sukhumvit Set | looped |
| Android | **Noto Sans Thai** (loopless) | (Noto Sans Thai Looped not guaranteed) | loopless |
| ChromeOS / Linux | Noto Sans Thai | Garuda, Loma, Waree, Norasi (TLWG) | mixed |

Sources: Designil "รวม System Font ฟอนต์ไทยและอังกฤษบน Mac, Windows, iOS, Android" (https://www.designil.com/thai-default-fonts/); jeffmcneill thai-font-collection list of Apple/Microsoft Thai fonts (https://github.com/jeffmcneill/thai-font-collection/blob/master/apple-and-microsoft-thai-fonts.md); Microsoft Leelawadee UI font page (https://learn.microsoft.com/en-us/typography/font-list/leelawadee-ui); Readium default Thai stack `"Thonburi","Leelawadee UI","Cordia New",Roboto,Noto,"Noto Sans Thai"` (https://readium.org/css/docs/CSS09-default_fonts.html); ThaiGraph on Sukhumvit Set (https://thaigraph.com/fonts/sukhumvit-set/).

**Thai stacks:**
```css
/* headings */ 'Instrument Serif', 'Trirong', 'Noto Serif Thai', 'Angsana New', 'Thonburi', 'Leelawadee UI', Georgia, serif;
/* body     */ 'Inter', 'Sarabun', 'Noto Sans Thai Looped', 'Thonburi', 'Leelawadee UI', 'Tahoma', 'Noto Sans Thai', system-ui, sans-serif;
```
Thonburi is placed before Leelawadee UI so macOS/iOS get a looped face; on Windows, Thonburi is absent and Leelawadee UI is used. Android ends at Noto Sans Thai (loopless) — acceptable during the swap window only.

### 4.2 Simplified Chinese system fonts
| Platform | Default SC font | Serif available |
|---|---|---|
| Windows 7–11 | **Microsoft YaHei** (微软雅黑); Windows 10/11 also **DengXian** (等线) | **SimSun** (宋体), NSimSun; KaiTi, FangSong |
| macOS 10.11+ / iOS 9+ | **PingFang SC** (苹方) | **Songti SC** (宋体-简); older: Heiti SC, STHeiti, STSong |
| Android | Noto Sans CJK SC / "Source Han Sans" (varies by OEM; Chinese OEMs ship MiSans, HarmonyOS Sans, OPPO Sans) | none guaranteed |
| Linux / ChromeOS | Noto Sans CJK SC, WenQuanYi Micro Hei | Noto Serif CJK SC (if installed) |

Sources: Chen Hui Jing, "Chinese language on the web" (https://chenhuijing.com/blog/chinese-web-typography/) and talk slides (https://huijing.github.io/slides/18-pitercss-2017/); W3C clreq (https://www.w3.org/TR/clreq/); SymbolFYI CJK guide (https://symbolfyi.com/guides/cjk-web-typography/).

**SC stacks:**
```css
/* headings */ 'Instrument Serif', 'Noto Serif SC', 'Source Han Serif SC', 'Songti SC', 'SimSun', 'Noto Serif CJK SC', serif;
/* body     */ 'Inter', 'Noto Sans SC', 'Source Han Sans SC', 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', 'Noto Sans CJK SC', system-ui, sans-serif;
```
Traditional contingency: swap `SC`→`TC`, `Songti SC`→`Songti TC`/`PMingLiU`, `PingFang SC`→`PingFang TC`, `Microsoft YaHei`→`Microsoft JhengHei`.

### 4.3 FOUT control
- `font-display: swap` everywhere (already `display=swap` in the current import).
- Optional metric-matching for Thai body to reduce the swap jump:
  ```css
  @font-face { font-family: 'Sarabun-fallback'; src: local('Leelawadee UI'), local('Thonburi');
               size-adjust: 92%; ascent-override: 105%; descent-override: 40%; line-gap-override: 0%; }
  ```
  Exact percentages must be derived in the prototype (compare `OS/2` metrics of Sarabun vs Leelawadee UI/Thonburi); values above are placeholders, not measured.
- Never use `font-display: block`/`optional` for CJK headings: `optional` would show system Song forever on first visit; `block` hides headings for up to 3 s.
- Keep `-webkit-font-smoothing: antialiased` (theme line 247) — it helps thin Noto Serif SC hairlines on macOS; on Windows nothing can be done in CSS, so test Noto Serif SC 400 vs 500 on a ClearType screen.

---

## 5) Typesetting rules the theme must respect

### 5.1 Thai
1. **`lang="th"` on `<html>`** (or on any Thai block). Browsers break Thai lines with a dictionary (ICU "dictionary code… loads the appropriate dictionary… for Thai, Khmer, Chinese, Japanese" — https://unicode-org.github.io/icu/userguide/boundaryanalysis/break-rules.html; Chrome/Safari/Firefox all do this). Thai has no inter-word spaces; without a correct `lang`, break quality drops and hyphenation/`text-transform` misbehave. W3C Thai layout requirements: "when Thai text is wrapped at the end of a line you should not split a word… requires… a dictionary" (https://www.w3.org/International/sealreq/thai/; https://r12a.github.io/scripts/tutorial/summaries/thai).
2. **Do not insert `<wbr>` or U+200B everywhere.** Browser dictionary breaking is good for ordinary prose. Use U+200B/`<wbr>` only inside headings and buttons where a wrong break would be embarrassing (e.g. after proper nouns, between compound words). `Intl.Segmenter('th', {granularity:'word'})` is available in Chrome 87+, Safari 14.1+, Firefox 125+ and can pre-segment headings client-side if needed (polyfill: https://www.npmjs.com/package/intl-segmenter-polyfill); projects such as pretext use it "only for word boundaries inside Thai, Lao, Khmer and Myanmar runs" (https://github.com/chenglou/pretext/pull/340). This is optional enhancement, not launch scope.
3. **Spaces are phrase/sentence separators, not word separators.** Never apply `word-spacing` tricks, never `text-align: justify` on Thai body (browsers justify by stretching the rare spaces → huge gaps). Keep ragged-left… i.e. `text-align: start`.
4. **Line-height.** Thai stacks up to three marks above and one below the base line (e.g. ที่, ปั้น, ฐ์). Body: **≥ 1.6, recommend 1.7–1.75** for Sarabun 16–17 px (field guidance "at least 1.55 — about 10–15 % more than Latin"; https://thaigraph.com/faq/, https://monisaenterprise.com/blog/dos-donts-fonts-that-break-arabic-and-thai-layouts/). Headings: 1.2–1.3 (not the 1.1 used for Latin display) and **padding-top ≥ 0.15 em** on heading boxes, because tone marks over tall vowels (e.g. ปี้) exceed the ascender and get clipped by `overflow: hidden` or tight line boxes.
5. **Size.** Thai looped fonts have a smaller "x-height" (ความสูงตัวอักษร) than Latin; Sarabun at 16 px reads like Inter at ~14.5 px. Set `:lang(th) { --text-base: 1.0625rem }` or use `size-adjust`. Minimum body 16 px; captions never below 14 px.
6. **No letter-spacing** on Thai (breaks mark positioning); no `text-transform`; no `font-style: italic` synthesis — Trirong/Taviraj/Sarabun have real italics, Thai italic is acceptable but unusual in formal text, so avoid.
7. **Numerals and dates.** Use Arabic digits (0–9) set in Inter; Thai digits (๐–๙) only in ceremonial contexts. Buddhist-era years (พ.ศ.) are the Thai business norm — content decision, not type.
8. **Weights.** Never below 400 for Thai text; loops disappear at 300 on Soft Linen. Bold Thai ≥ 600.
9. **Looped vs loopless.** Body and headings: looped (formality, legibility, confusable-glyph safety). Loopless only as a possible UI accent, decided in the specimen review.

### 5.2 Simplified Chinese
1. **`lang="zh-Hans"`** (not `zh-CN` alone, not bare `zh`). Fonts and browsers select Simplified glyph forms by language tag; without it a Han character may be drawn with Japanese or Traditional shapes by the fallback font. Use `zh-Hant-TW` / `zh-Hant-HK` if §7 goes Traditional.
2. **Line-height 1.7–1.8 for body**, 1.3–1.4 for headings (Chinese body "typically 1.5–2.0em, 1.7em commonly used", https://chenhuijing.com/blog/chinese-web-typography/; W3C clreq https://www.w3.org/TR/clreq/; Bobby Tung, "Best Practices for Chinese Layout", https://bobtung.medium.com/best-practice-in-chinese-layout-f933aff1728f).
3. **Minimum body size 16 px; prefer 17–18 px** — Han glyphs have far more strokes than Latin letters.
4. **Punctuation.** Simplified Chinese uses full-width punctuation sitting bottom-left (，。、；：), Traditional centres it — one more reason the glyph set must match the audience (https://chenhuijing.com/blog/chinese-web-typography/). Use proper Chinese punctuation in copy (，。！？「」/“ ”, —). Enable `text-spacing-trim: space-first` and `hanging-punctuation: allow-end` where supported (progressive enhancement; clreq "Chinese Layout Gap Analysis" https://www.w3.org/TR/clreq-gap/).
5. **Mixed Chinese/Latin.** Put a thin gap between Han and Latin/digits ("增值税 7%"): browsers now support `text-autospace: normal` (Chromium 2025+); until universal, write a normal space in copy. Numbers and Latin inside Chinese paragraphs should render in Inter (our stack order guarantees this) — this is standard practice because Noto's Latin is wider than Inter.
6. **No italics in Chinese.** Oblique Han is a Western import and reads as an error in formal text; use weight (Noto Sans SC 500/700) or colour for emphasis. The theme's `<em>`/blockquote italic rules must be neutralised under `:lang(zh)`.
7. **`text-align: justify` is fine and traditional for Chinese** (every character is a break opportunity), but keep `text-justify: inter-character`; avoid `letter-spacing` above 0.02 em.
8. **Line breaking.** `word-break: normal; line-break: strict` to forbid lines starting with closing punctuation; `overflow-wrap: anywhere` only for URLs/e-mails.
9. **Bold is weight 700 on the CDN**, not 600: map `--weight-semibold` to 700 under `:lang(zh)`.
10. **Numerals/dates.** Keep Western digits in Inter; Chinese year format "2026年10月5日" mixes Han + digits — test the baseline alignment in the specimen.

---

## 6) Specimen plan for the prototype ticket

**Goal:** one static page per language (`th/specimen.html`, `zh/specimen.html`, relative paths only), Navy on Soft Linen, showing each pairing side by side with the Latin pair so the owner can choose in 10 minutes. No theme changes until a pairing is approved.

**Text to set (same content in each pairing column):**
- H1 (one line): "บริการบัญชีและภาษีสำหรับธุรกิจของคุณ" / "专业会计与税务服务"
- H2 with stacked marks and tall vowels: "ที่ปรึกษาด้านภาษีที่คุณไว้วางใจได้" (contains ที่ ปึ ไว้) / "增值税与预扣税申报（ภ.พ.30 · ภ.ง.ด.53）"
- Stat line (Instrument Serif numerals beside script): "15 ปี ประสบการณ์" / "服务客户 200+ 家"
- Body paragraph ≈ 90 words (Thai) / ≈ 180 characters (Chinese) using real service copy (monthly bookkeeping, VAT, WHT, SSO, audit coordination, BOI, work permits) — reuse the sample texts in this ticket's scratch files.
- Mixed-script line: "ยื่น ภ.พ.30 ภายในวันที่ 15 ของเดือนถัดไป (e-Filing: 23rd)" / "每月 15 日前申报 VAT（e-Filing 可延至 23 日）"
- Button/nav labels: "ติดต่อเรา · บริการ · บทความ · นโยบายความเป็นส่วนตัว" / "联系我们 · 服务 · 知识库 · 隐私政策"
- Confusable-glyph row (Thai only): "ก ถ ภ ฤ ฦ | ฎ ฏ | บ ป | ข ช | ด ต | พ ฟ ผ ฝ" at 14 px and 16 px.
- Rare-character stress line (Chinese only): "簽署 / 签署 · 審計 / 审计 · 餘額 / 余额" to visualise Simplified vs Traditional for the owner (§7).

**Sizes** (theme scale, already defined in `theme.css`): headings at `--text-3xl`, `--text-2xl`, `--text-xl`; body at 16, 17, 18 px (Thai) and 16, 17, 18 px (Chinese); caption 14 px. Show each at line-height 1.5 / 1.65 / 1.8 (Thai) and 1.6 / 1.75 / 1.9 (Chinese) in a small matrix.

**Widths:** 320 px (small phone), 390 px (modern phone), 720 px (article measure), 1200 px (desktop container). Record where Thai dictionary breaking produces an ugly break in H1/H2 and whether Chinese punctuation hangs correctly.

**Pairings to render:**
- Thai columns: TH-A Trirong + Sarabun · TH-B Taviraj + Plex Sans Thai Looped · TH-C Noto Serif Thai + Noto Sans Thai Looped · (optional wildcard) Trirong + Krub.
- Chinese columns: ZH-A Noto Serif SC + Noto Sans SC · ZH-B Serif-only · ZH-C Sans-only; plus one TC column (Noto Serif TC + Noto Sans TC) for the owner's decision.

**Measurements to capture in the prototype:** DevTools Network → total font bytes per page (expect ≈ 60 KB Thai, ≈ 0.9–1.4 MB Chinese), CLS from font swap, and screenshots on Windows (ClearType) and iPhone. Also compute real `size-adjust` values for Sarabun vs Leelawadee UI/Thonburi.

**Owner review questions to put on the specimen page:** (a) which Thai heading face feels right for the firm; (b) is the Chinese audience mainland or Taiwan/HK; (c) is a 1 MB Chinese page acceptable, or should Chinese headings fall back to system Song (ZH-C).

---

## 7) Open questions

1. **Simplified or Traditional Chinese?** Mainland China, Singapore and Malaysia read Simplified; Taiwan, Hong Kong and Macau read Traditional, and "Hong Kong audiences notice and react negatively to content that uses Simplified characters" (https://translationservices.hk/traditional-vs-simplified-chinesewhich-version-should-your-business-use-for-hong-kong-china-taiwan/; https://www.smartling.com/blog/traditional-vs-simplified-chinese; https://www.ecinnovations.com/blog/simplified-vs-traditional-chinese-which-one-to-choose-for-localization/). Mainland investors dominate Chinese FDI into Thailand in recent years, but Taiwanese manufacturers and Hong Kong holding structures are a large share of accounting clients. **Owner must confirm the client mix.** If both matter, plan `zh-Hans` first and a `zh-Hant` page later; fonts and stacks are listed above for both.
2. **Which Chinese variant of the firm's name/address is official** (Simplified vs Traditional spelling of Thai place names)? Needed before the specimen text is final.
3. **Does the owner accept ≈ 1 MB of Chinese font on first visit**, or prefer ZH-C (system Song headings, Noto Sans SC body only)?
4. **Thai heading austerity:** Trirong (narrow, formal) vs Taviraj (wider, friendlier) is a taste call; the specimen decides.
5. **Thai digits/era:** confirm Arabic digits + พ.ศ. years for Thai pages (content rule, affects numerals in Instrument Serif).
6. **Current theme stacks list `Noto Serif TC`/`JP`, `Noto Sans TC`/`JP`** (theme.css lines 130–131) although the target is Simplified Chinese and nothing is loading them. The prototype ticket should replace them with the `:lang()` scoped stacks above — flagged here, not changed.
7. **Loopless accent (Anuphan) for navigation?** Default recommendation is no; keep as a reversible option after the owner sees TH-A.
8. **Noto Sans SC has no 600 instance on Google Fonts** — decide whether `--weight-semibold` maps to 500 or 700 for Chinese UI labels.
9. **Fallback-metric overrides** (`size-adjust`, `ascent-override`) need real measurement in the prototype; values in §4.3 are placeholders.

---

### Appendix A — Sources consulted
- google/fonts repository metadata & descriptions for every Thai/Chinese family above — https://github.com/google/fonts/tree/main/ofl/
- Google Fonts CSS API (live slice counts and WOFF2 sizes, measured) — https://fonts.googleapis.com/css2 and https://fonts.gstatic.com
- Cadson Demak READMEs: Trirong https://github.com/cadsondemak/trirong · Taviraj https://github.com/cadsondemak/taviraj · Pridi https://github.com/cadsondemak/pridi · Bai Jamjuree https://github.com/cadsondemak/bai-jamjuree · Kanit https://github.com/cadsondemak/kanit · Prompt https://github.com/cadsondemak/prompt · Mitr https://github.com/cadsondemak/mitr · Cadson Demak feature https://maekan.com/story/type-of-graphic-cadson-demak/
- Anuphan specimen https://fonts.google.com/specimen/Anuphan · Sarabun specimen https://fonts.google.com/specimen/Sarabun · IBM Plex Sans Thai Looped https://fonts.adobe.com/fonts/ibm-plex-sans-thai-looped · ThaiGraph: https://thaigraph.com/fonts/ , /fonts/sarabun/ , /fonts/anuphan/ , /fonts/ibm-plex-sans-thai/ , /fonts/trirong/ , /fonts/categories/loopless/ , /faq/
- Thai script layout: W3C https://www.w3.org/International/sealreq/thai/ · r12a https://r12a.github.io/scripts/tutorial/summaries/thai · Microsoft line/word breaking https://learn.microsoft.com/en-us/globalization/fonts-layout/line-and-word-breaking · ICU boundary analysis https://unicode-org.github.io/icu/userguide/boundaryanalysis/ and break rules https://unicode-org.github.io/icu/userguide/boundaryanalysis/break-rules.html · Intl.Segmenter usage https://github.com/chenglou/pretext/pull/340 · polyfill https://www.npmjs.com/package/intl-segmenter-polyfill · Thai layout do's & don'ts https://monisaenterprise.com/blog/dos-donts-fonts-that-break-arabic-and-thai-layouts/ · National Fonts https://en.wikipedia.org/wiki/National_Fonts
- Thai system fonts: https://www.designil.com/thai-default-fonts/ · https://github.com/jeffmcneill/thai-font-collection/blob/master/apple-and-microsoft-thai-fonts.md · https://learn.microsoft.com/en-us/typography/font-list/leelawadee-ui · https://readium.org/css/docs/CSS09-default_fonts.html
- Chinese layout & fonts: W3C clreq https://www.w3.org/TR/clreq/ · clreq gap analysis https://www.w3.org/TR/clreq-gap/ · Chen Hui Jing https://chenhuijing.com/blog/chinese-web-typography/ and https://chenhuijing.com/blog/font-face-fun-times/ · Bobby Tung https://bobtung.medium.com/best-practice-in-chinese-layout-f933aff1728f · SymbolFYI https://symbolfyi.com/guides/cjk-web-typography/
- CJK font sizes & subsetting: https://changethisfile.com/blog/font-subsetting-guide · https://github.com/CodePlayer/webfont-noto · https://fonttools.readthedocs.io/en/latest/subset/ · https://github.com/black7375/font-range · https://github.com/google/fonts/issues/1684 · https://en.wikipedia.org/wiki/Noto_fonts · https://en.wikipedia.org/wiki/Source_Han_Sans
- Other Chinese fonts: Chiron Sung HK https://github.com/chiron-fonts/chiron-sung-hk · Chiron Hei HK https://github.com/chiron-fonts/chiron-hei-hk (OFL-1.1) · LXGW WenKai https://github.com/lxgw/LxgwWenKai · List of CJK fonts https://en.wikipedia.org/wiki/List_of_CJK_fonts
- Simplified vs Traditional audience: https://www.smartling.com/blog/traditional-vs-simplified-chinese · https://translationservices.hk/traditional-vs-simplified-chinesewhich-version-should-your-business-use-for-hong-kong-china-taiwan/ · https://www.ecinnovations.com/blog/simplified-vs-traditional-chinese-which-one-to-choose-for-localization/ · https://www.ics-translate.com/blog/simplified-vs-traditional-chinese
