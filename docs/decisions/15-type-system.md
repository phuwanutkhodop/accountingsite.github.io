# 15 — The builder's trilingual type system

**Ticket:** GitHub issue #15 (Wayfinder prototype)
**Date:** 6 October 2026
**Decided by:** Claude, under the owner's standing delegation of technical choices (map #1). The owner checks the specimen on their own Windows PC and iPhone (§7).
**Inputs:**
- research #5 (Thai and Chinese typography), #8 (multilingual SEO), #34 §4–5 (fonts, measured costs);
- decisions #11, #13, #16 and #31;
- plan review finding **M7** (three contradicting font-loading positions).

**Prototype:** [Builder Type Specimen](https://claude.ai/artifact/GHqZLEnpmiRVAau4KWdQnX) (private). Its source is in [`15-type-system/prototype/`](./15-type-system/prototype/).
**Status:** locked. Line-height values may be tuned after the owner's device check (§7); the model and the recipe do not depend on it. Resolves M7.

---

## 1. สรุปสำหรับเจ้าของกิจการ (ภาษาไทย)

1. **ทุกธีมใช้ระบบตัวอักษรเดียวกัน** ฟอนต์มี 3 บทบาท คือ หัวข้อ เนื้อความ และปุ่มกับตาราง แต่ละบทบาทมีฟอนต์อังกฤษ ไทย และจีน ที่เลือกให้เข้าคู่กัน
2. **ขนาดอักษรสามภาษาเข้ากันเอง** ระบบปรับให้ตัวอักษรทุกฟอนต์สูงเท่ากัน รวมถึงฟอนต์สำรองในเครื่องผู้อ่าน เปลี่ยนธีมแล้วหน้าเว็บไม่ล้นหรือเล็กลงผิดปกติ
3. **ฟอนต์ไม่โหลดจาก Google** ทุกหน้าใช้ฟอนต์จากเว็บของเราเอง ผู้อ่านในจีนจึงเห็นฟอนต์ครบ และข้อมูลผู้อ่านไม่ถูกส่งไปที่ Google
4. **ตอนกด Publish ระบบตัดฟอนต์ให้เหลือเฉพาะตัวอักษรที่เว็บใช้จริง** หน้าจีนของตัวอย่างใช้ฟอนต์จีน 58 KB ต่อ 1 น้ำหนัก ถ้าโหลดจาก Google จะหนัก 692 KB การตัดใช้เวลาไม่ถึงครึ่งวินาที
5. **ตัวเลขในตารางเรียงตรงหลักเสมอ** และระบบตรวจเองว่าฟอนต์ที่ใช้ทำได้
6. **ภาษาไทยและจีนไม่ใช้ตัวเอียง** เน้นคำด้วยตัวหนาแทน
7. **รับเฉพาะฟอนต์ที่ใช้ฟรีได้ถูกต้องตามสัญญาอนุญาต** ฟอนต์ที่สงวนชื่อไว้ เช่น IBM Plex จะไม่รับเข้าคลัง
8. **สิ่งที่ขอให้คุณทำ:** เปิดหน้าตัวอย่างบน Windows (Edge) และบน iPhone แล้วบอกผมว่าสระและวรรณยุกต์ไทยชนกันหรือถูกตัดหรือไม่ และแบบ "ปรับขนาดให้เท่ากัน" เปิดหรือปิดอ่านสบายกว่า

---

## 2. Decisions

| # | Question | Decision | Why |
|---|---|---|---|
| 1 | Font slots | **Three roles × three scripts.** Roles: `display` (headings), `body` (running text), `ui` (buttons, navigation, labels, tables). Each role names one Latin, one Thai and one Chinese family, plus its weights. Stored in `site/theme.json` as `font.roles.<role>.<latin\|thai\|cjk> = { "font": "<library font id>", "weights": [400, 600] }`. A role may reuse another role's Chinese family with no weights of its own. | Every preset binds to roles, never to font names (#13). A theme swaps fonts without touching presets. Three roles are what the specimen needed; a fourth (monospace) can be added later without a format change. |
| 2 | Stacks | **One stack per role for every language:** Latin family, then Thai, then Chinese, then system fallbacks per script, then the generic family. Each web face carries a `unicode-range` for its script, so each script uses its own font and the browser downloads only the scripts a page contains. **Chinese adds one alias first:** `<Chinese family> Punct`, the same font limited to `“ ” ‘ ’ — … ·`, so these shared characters take the full-width Chinese form on `/zh/` and stay Latin elsewhere. | Latin first keeps Latin words and figures in the Latin face on every page (#34 §4). `unicode-range` makes language-specific stacks unnecessary. Without the alias, Chinese quotes and dashes render half-width from the Latin font (seen in the specimen). |
| 3 | Size matching | **`font-size-adjust: ex-height 0.5` on every page.** Every face, including system fallbacks, is scaled so its x-height is half the font size. Type-scale tokens are defined in these normalised terms. | Faces differ widely: x-height is 0.386 for Cormorant, 0.426 for Newsreader, about 0.5 for the Thai faces and 0.51 for Noto Serif SC (measured). Without normalising, swapping a theme's font changes every size on the site, and Windows' Thai fallbacks render tiny. Thai and Chinese faces are normalised through their own Latin x-height, which their designers already balanced against their script. Supported by the #16 baseline: Chrome 127+, Safari 17+, Firefox. |
| 4 | Per-language rules | **Line height:** body 1.6 (EN) · 1.8 (TH) · 1.8 (ZH); headings 1.15 · 1.4 · 1.35; Thai buttons and table cells at least 1.5. **Heading tracking:** −0.01em in Latin only, 0 in Thai and Chinese. **Chinese:** `text-autospace: normal`, which adds the W3C ⅛-em gap between Chinese and Latin where the browser supports it. **Alignment:** start-aligned everywhere, never justified. **Emphasis:** weight, never italic, in Thai and Chinese; Latin italic only when the theme ships an italic face. `font-synthesis: none`, so no fake bold or italic. | Thai stacked marks need room (#5, #34). With line guides on, the 1.4 Thai heading keeps `ปั๊มน้ำ ผู้ถือหุ้น ฎีกา` inside its line at 52 px, in the web fonts and in the fallbacks. Justifying Thai breaks spacing, and one alignment rule is simpler. |
| 5 | Figures | **Lining figures by default in every language.** Tables use `tabular-nums lining-nums`. Old-style figures are a theme option for Latin running text only. | Cormorant's default old-style "5" dropped below the line inside Thai headings (specimen, fixed). Fee tables must align (#34 §5). |
| 6 | Loading (resolves M7) | **Self-hosted on every page; Google Fonts never at runtime.** Fonts are written into the site's output at Publish (`fonts/<family>-<weight>-<key>.woff`), with `font-display: swap`. Published pages need only `font-src 'self'`. | One rule replaces three. It covers #8 (China cannot reach Google), visitor privacy (no visitor addresses go to Google, which helps #29), the strict policy of #16, and deterministic output (#11). |
| 7 | Subsetting | **At Publish, each face is cut to its guard set plus the characters the site uses in that script:** <br>• Latin guard: Basic Latin, Latin-1, general punctuation, € and minus; <br>• Thai guard: the whole Thai block, the zero-width characters and the dotted circle; <br>• Chinese guard: none, only the characters used. <br>Format: **WOFF 1.0**. File names are keyed by the **inputs** (the master's SHA, the sorted characters, the axis values), so unchanged inputs keep the same file and nothing is committed again, whichever browser compressed it. | Measured on the specimen, per weight: Chinese 58 KB against **692 KB** from Google's slices; Thai about 13–18 KB; Latin 17–31 KB. A full trilingual set is ~120 KB on an English page, 100–200 KB on a Thai page and 160–240 KB on a Chinese page. |
| 8 | Subsetting tool | **HarfBuzz's own subsetter:** `harfbuzz-subset.wasm` from harfbuzzjs 1.6.3 (MIT). It is a standalone WebAssembly file of 667 KB, with no JavaScript glue and no imports. It is vendored as a file through `tools/vendor/` and loaded only at Publish. A WOFF writer of about 60 lines sits beside it in `services/`, using the browser's `CompressionStream`. **The subsetter must add the numeral features** (`tnum pnum lnum onum zero case frac numr dnom sups subs ordn`) to HarfBuzz's default list, which drops them. Without this, Cormorant's tabular figures silently disappear (found in the prototype). | HarfBuzz is the industry-standard subsetter that Google Fonts itself uses. It can also pin variable axes, so masters can be variable fonts. **Proven** in Node 22 and in Chromium 141 under #16's exact policy: 110 ms from the 24 MB Chinese master. cn-font-split (#34) is 6 MB and built for slicing whole fonts. WOFF2 is rejected for v1: the only browser encoder found (wawoff2) needs `new Function`, which the policy forbids. A policy-clean WOFF2 encoder would save about 22% and can be added later. |
| 9 | Font masters | Masters live in **`builder-library/fonts/<id>/`** (#31): the font file, its licence text, and `font.json` (family, scripts, weights or axes, measured x-height, whether digits are tabular by default, numeral features, licence). **Chinese masters are pre-trimmed to GB 2312** (6,763 characters plus punctuation), keeping the variable axis: Noto Serif SC drops from 24 MB to 4.9 MB, Noto Sans SC from 17 MB to 3.5 MB. The Admin caches masters per device. Only Claude sessions add fonts, through `tools/fonts/ --check`. | A phone may publish (#24), so a 24 MB first download is too much. GB 2312 covers everyday Simplified Chinese. A character outside it falls back to the system font, and the gate warns. |
| 10 | Library check for fonts | A font enters the library only if: <br>• its licence is OFL or Apache-2.0; <br>• it has **no Reserved Font Name** that its family name uses; <br>• it covers its script; <br>• a font for the `ui` role gives tabular lining digits, by default or through `tnum` + `lnum`. <br>The check reads and records these facts; nobody types them by hand. | Subsetting changes the font. Under the OFL, a changed font may not keep a reserved name, so IBM Plex ("Plex") is excluded and the specimen uses Noto Sans Thai Looped instead. Noto Sans SC reserves "Source", which its name does not use, so it is allowed. Hanken Grotesk has no `tnum` but tabular digits by default (measured); Noto Serif SC has neither, so it cannot carry tables. |
| 11 | Weight budget per page | **Chinese at most 2 weights per page** (regular and one strong, shared by all roles). Thai at most 3. Latin at most 4 files. The gate warns above these. | One Chinese weight costs as much as all of a page's Thai. Sharing the Chinese weights brought the serif Chinese page from 341 KB to 242 KB. |
| 12 | Admin preview | The preview uses the full cached masters, never subsets. Fonts reach it either from bytes (`new FontFace(name, bytes)`, which needs **no policy change**, proven) or as `data:` URLs in a sandboxed frame, which needs `font-src data:` (proven in the main document). `blob:` font URLs are refused by the policy (proven). #22's preview test picks the route. | Subsetting on every keystroke would be wasted work. Both routes keep `unsafe-inline` and `unsafe-eval` forbidden. |

## 3. The stacks the generator emits

```css
/* per role; [L] [T] [C] are the theme's families for that role */
--font-<role>: "[L]", "[T]", "[C]", <fallback>;
:lang(zh) { --font-<role>: "[C] Punct", "[L]", "[T]", "[C]", <fallback>; }

/* fallback (serif roles) */
Georgia, "Times New Roman", "Noto Serif Thai", Ayuthaya, Tahoma,
"Noto Serif CJK SC", "Source Han Serif SC", "Songti SC", STSong, SimSun, serif
/* fallback (sans roles) */
"Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans Thai Looped", "Noto Sans Thai", Thonburi,
"Leelawadee UI", Tahoma, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei",
"Noto Sans CJK SC", "Source Han Sans SC", sans-serif
```

Each `@font-face` carries `unicode-range` for its script: Latin `U+20-7E, U+A0-17F, U+2010-2027, U+2030-203A, U+2044, U+20AC, U+2190-2193, U+2212` · Thai `U+E00-E7F, U+200B-200D, U+25CC` · Chinese `U+3000-303F, U+3400-4DBF, U+4E00-9FFF, U+FF00-FFEF` · Chinese punctuation alias `U+B7, U+2014, U+2018-2019, U+201C-201D, U+2026`.

## 4. Measurements (6 October 2026)

| Face (subset for the specimen) | WOFF | WOFF2 (for comparison) |
|---|---|---|
| Cormorant Garamond 600 (Latin, with numeral features) | 27.9 KB | ~22 KB |
| Newsreader 400 / 600 | 29.3 / 31.3 KB | ~25 KB |
| Hanken Grotesk 400–700 | 16.8–18.2 KB | ~13 KB |
| Trirong 500 · Taviraj 400 / 600 | 18.4 · 18.4 / 18.7 KB | ~15 KB |
| Noto Sans Thai Looped 400–600 | 12.4–13.1 KB | — |
| Noto Serif SC 400 / 600 (271 characters used) | 58.3 / 58.9 KB | ~46 KB |
| Noto Sans SC 400 / 600 | 46.5 / 47 KB | ~37 KB |
| Chinese punctuation alias | 2.5 KB | — |
| **Google Fonts, Noto Serif SC 400, same Chinese text** | **692 KB** (18 of 101 slices) | |

Subsetting time per face: 2–50 ms in Node 22; 110 ms in Chromium from the 24 MB Chinese master.

## 5. Findings for other tickets

- **#26 (editing):** with `text-wrap: balance`, Thai headings can break inside a compound word (the specimen showed `ตัดสิน | ใจ`). The heading editor should offer "keep these words together", which inserts U+2060 WORD JOINER. Browser behaviour still needs testing there.
- **#22 (preview, M2):** a sandboxed `srcdoc` preview frame inherits the Admin's policy, so its inline `<style>` is refused (seen in this prototype's test). Stylesheet delivery to the preview has to be solved first; fonts then follow the same route (§2-12).
- **Instanced variable fonts keep the default instance's name** in their `name` table (for example "Noto Serif SC ExtraLight" for weight 400). Pages are unaffected, because CSS names each face itself. Renaming can come with the font tools.

## 6. What this supersedes

- **Research #5:** Google Fonts loading, and the candidate list as a decision. The fonts there are now only candidates for themes.
- **Research #34 §5:** cn-font-split is replaced by HarfBuzz.
- **Decision #11 §3.10:** "`/zh/` must not depend on Google Fonts" is now true of every page.
- **Review M7:** resolved by decisions 6–9 here.

## 7. Owner check (pending)

On the owner's Windows PC (Edge) and iPhone (Safari), open the specimen and report:
1. Do Thai vowels and tone marks collide or get clipped, in large headings or in running text?
2. Is "ปรับขนาดให้เท่ากัน" (size matching) easier to read on or off, especially on Thai pages?
3. Does anything look wrong in "ฟอนต์สำรอง" (fallback fonts)?

A problem changes token values in decision 4, not the model.

## 8. Effects on other tickets

- **#11:** the gate gains three warnings: a character missing from a font's master; more font files per page than decision 11 allows; and a theme `ui` font without tabular digits (an error).
- **#13:** `theme.json` gains `font.roles` (decision 1). The library check gains the font rules (decision 10).
- **#16:** the vendor set gains `harfbuzz-subset.wasm` (MIT); `services/` gains `fonts.js`. Policy: published pages `font-src 'self'`; Admin as in decision 12.
- **#21:** the neutral test theme uses this model. Suggestion: the sans pairing as theme 1 and the serif pairing as theme 2, which proves a font swap.
- **#29:** no Google Fonts means no font-related transfer of visitor data to disclose.
- **#30:** the performance report shows font bytes per page (§4 gives the expected range).
- **#31:** font masters live in `builder-library/fonts/`.
