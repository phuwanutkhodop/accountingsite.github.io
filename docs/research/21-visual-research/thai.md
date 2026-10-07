# Thai group: Thai and Bangkok premium sites

Sites: cadsondemak.com, tilleke.com, rosewoodhotels.com/en/bangkok, capellahotels.com/en/capella-bangkok, mandarinoriental.com/en/bangkok/chao-phraya-river, pwc.com/th/en, wcp.co.th. 13 findings, sorted by rarity × fit. Crops are in `findings/crops/<id>.jpg`. The Thai typesetting notes come after the findings.

**Failed:** wcp.co.th (domain now hosts an unrelated Thai classified-ads forum; re-capture identical); farmgroup.co.th, scb.co.th (excluded by instruction: being re-captured).  
**Partial:** rosewoodhotels.com_en_bangkok, capellahotels.com_en_capella-bangkok, mandarinoriental.com_en_bangkok_chao-phraya-river: desktop hero image/video did not render in the capture.

## Findings

| # | id | name | rarity | fit | score | role | buildable |
|---|---|---|---|---|---|---|---|
| 1 | cadsondemak-3 | Thai and Latin cut as one voice (matched companion type) | 4 | 5 | 20 | type-system | needs-bespoke-assets |
| 2 | cadsondemak-2 | Type-as-cover article cards | 4 | 4 | 16 | knowledge | css |
| 3 | cadsondemak-4 | Language offered as an 'Edition' | 4 | 4 | 16 | navigation | css |
| 4 | cadsondemak-1 | Rotating multi-script greeting with a script index | 5 | 3 | 15 | opening | css+small-js |
| 5 | capella-1 | Indented body column that survives on phone | 3 | 5 | 15 | grid-system | css |
| 6 | rosewood-bkk-1 | Engraved wide caps + light condensed serif (two-voice system) | 3 | 4 | 12 | type-system | needs-bespoke-assets |
| 7 | pwc-1 | Pivot-phrase headline | 3 | 4 | 12 | opening | css. |
| 8 | capella-2 | Awards as a captioned register | 2 | 5 | 10 | proof | css. |
| 9 | rosewood-bkk-2 | Centre-stage carousel with clipped wings | 3 | 3 | 9 | services | css+small-js |
| 10 | rosewood-bkk-3 | CTA band fused to the image + numeric slide counter | 3 | 3 | 9 | navigation | css |
| 11 | capella-3 | Warm blush fade under the sticky header | 3 | 3 | 9 | navigation | css |
| 12 | pwc-2 | Brand slab composited into the photograph | 3 | 3 | 9 | other | needs-bespoke-assets |
| 13 | tilleke-1 | Footprint map in one flat brand colour | 2 | 4 | 8 | proof | needs-bespoke-assets |

### 1. Thai and Latin cut as one voice (matched companion type)  ·  `cadsondemak-3`  ·  rarity 4 × fit 5

![cadsondemak-3](crops/cadsondemak-3.jpg)

- **Site:** cadsondemak.com  ·  **Role:** type-system
- **What:** All titles and UI use Graphik TH, the Thai companion of Graphik, with 'Graphik Thai Loop' loaded as a second family. Measured on the title 'Keychron Keycap กับภาษาไทย…' (~28px semibold, white on black): Latin cap height 20px, Latin x-height 15px, Thai consonant body 17px. Thai sits between x-height and cap height (1.13 x the x-height, 0.85 x the cap height) with the same stroke weight and terminals, so a mixed line reads as one colour. Two-line Thai titles use a 42px line pitch (1.5), so the vowels and tone marks above clear the line above. In display graphics, loopless bold carries the main phrase and looped light Thai is the counter-voice: 'ฟอนต์ฟรี' is loopless bold orange over 'ฟรีฟอนต์' looped light white, and 'ระหว่าง SEASON 5 บรรทัด' mixes looped light Thai with small Latin caps.
- **Evidence:** `shots/cadsondemak.com/desktop-01.jpg` [940, 100, 420, 160]; also `shots/cadsondemak.com/desktop-02.jpg` [836, 560, 514, 340]
- **Why valuable:** Mixed Thai/English lines usually look like two fonts fighting. Here they share weight, size and rhythm, which is the clearest sign of Thai-native craft. Using looped and loopless as a deliberate contrast (formal against modern) is a lever only Thai typography has.
- **Buildable:** needs-bespoke-assets (font choice). Free families built the same way: IBM Plex Sans Thai + IBM Plex Sans Thai Looped with IBM Plex Sans/Serif, or Noto Sans Thai / Noto Sans Thai Looped / Noto Serif Thai with Noto Sans/Serif. Pure CSS once self-hosted.
- **Three languages:** yes: this is the multi-script recipe itself. For Chinese, pick the CJK family that matches the Latin weight and keep CJK and Thai body line-height at 1.6 or more.

### 2. Type-as-cover article cards  ·  `cadsondemak-2`  ·  rarity 4 × fit 4

![cadsondemak-2](crops/cadsondemak-2.jpg)

- **Site:** cadsondemak.com  ·  **Role:** knowledge
- **What:** Article grid of 3 columns (cards ~408x510px, 18px gap, 16px radius). Each card's 'image' is typography: the article's key word in giant letterforms cropped by the card edge, for example 'บรี ไทย' at ~190px white on red, 'น้ำเสียงใหม่ คนเดิม' stacked as outline, fill, outline in blue, Thai keycaps on black, and a cropped serif 'สร้าง' overlapping itself. Card text block at the top left: category label (12px bold: 'Type', 'Thought'), title 28px semibold in mixed Thai/Latin, then a right-aligned byline 'Article by **Name**' (13px, regular plus bold). Grounds are flat colours (red, black, cream, pale grey). No photographs.
- **Evidence:** `shots/cadsondemak.com/desktop-01.jpg` [90, 60, 1270, 530]
- **Why valuable:** Replaces stock photos with imagery made from the content itself. Every cover is unique but follows one system. Costs nothing to produce and is clearly authored.
- **Buildable:** css (oversized text, overflow:hidden, -webkit-text-stroke for the outline echo, colour tokens per category). Needs no JS and degrades to plain text.
- **Three languages:** yes: Thai words and Chinese characters both crop well at display size. Use a loopless bold Thai face for outlined text, because outlines on thin looped Thai break up.

### 3. Language offered as an 'Edition'  ·  `cadsondemak-4`  ·  rarity 4 × fit 4

![cadsondemak-4](crops/cadsondemak-4.jpg)

- **Site:** cadsondemak.com  ·  **Role:** navigation
- **What:** Bottom-left of the footer, below a 1px full-width rule: 'Explore more content in **English Edition**'. The words are 13px grey; the link is bold white and underlined. The other language is offered as a parallel edition of a publication, not as a flag or an 'EN | TH' toggle.
- **Evidence:** `shots/cadsondemak.com/desktop-03.jpg` [60, 820, 760, 60]
- **Why valuable:** Treats each language as an edited edition, which implies the content was written for that reader rather than machine-translated. It frames the switch in publishing language.
- **Buildable:** css (a plain link). No JS.
- **Three languages:** yes: 'อ่านฉบับภาษาไทย' and '中文版' work naturally.

### 4. Rotating multi-script greeting with a script index  ·  `cadsondemak-1`  ·  rarity 5 × fit 3

![cadsondemak-1](crops/cadsondemak-1.jpg)

- **Site:** cadsondemak.com  ·  **Role:** opening
- **What:** Full-width hero band under a 4px dashed black rule (a 'perforation'). One word, the greeting, is set in a heavy sans at roughly 20vw (cap height ~270px at 1440) and deliberately cropped by both viewport edges ('Welcome' runs off the right). Under it, one row of the scripts the studio covers (Latin, Bahasa & Tagalog, Vietnamese, Thai, Lao, Khmer, Burmese) in a ~36px light sans spread across the width; the script now on show is set bold italic ('Latin' bold while 'Welcome' shows). Each step swaps the greeting word, the bold item in the index and the ground colour: desktop frame = cyan with a yellow wedge, phone frame = magenta with a green wedge showing the Lao greeting with 'Lao' bolded. On phone the index turns 90 degrees into a vertical column at the left edge, so the greeting keeps the full width. Above the band, the site title in hairline condensed caps (~190px) also bleeds off both edges.
- **Evidence:** `shots/cadsondemak.com/desktop-00.jpg` [0, 260, 1440, 640]; also `shots/cadsondemak.com/phone-00.jpg` [0, 420, 780, 760]
- **Why valuable:** Shows that the site speaks several languages as the opening gesture instead of hiding it in a flag dropdown. The bolded index turns an animation into something you can read, like a table of contents. Huge cropped type shows confidence.
- **Buildable:** css+small-js (swap every ~3s, stop when the user prefers reduced motion). Without JS: the first greeting plus the full index, still complete.
- **Three languages:** yes: made for it. A quiet firm version could cycle 'Welcome / ยินดีต้อนรับ / 欢迎' on a muted ground, with the index 'English · ไทย · 中文' doubling as the language switch. Give Thai a line box of 1.3 or more so the vowels above the line are not cut off when cropped.

### 5. Indented body column that survives on phone  ·  `capella-1`  ·  rarity 3 × fit 5

![capella-1](crops/capella-1.jpg)

- **Site:** capellahotels.com_en_capella-bangkok  ·  **Role:** grid-system
- **What:** Desktop: section title in Goudy Light caps (~50px, slight tracking) at x=150. Lede in Goudy ~30px grey #6F6F6F in the left half. Body in Calibre 15px/20px grey #777 in a narrow 340px column starting at x~820, the right half, followed by a small underlined caps link 'RESORT PROGRAMMING'. The image below breaks out to x=37, further left than the text margin. Phone: the lede stays on the heading margin (~35 CSS px) while the body and link are indented ~50 CSS px further, so the two-column relationship survives as an indent instead of collapsing to one left edge. The image again starts left of the text margin and bleeds off the right edge.
- **Evidence:** `shots/capellahotels.com_en_capella-bangkok/phone-01.jpg` [0, 90, 780, 900]; also `shots/capellahotels.com_en_capella-bangkok/desktop-01.jpg` [0, 150, 1440, 500]
- **Why valuable:** Keeps book-like hanging structure on small screens, where almost every template collapses to a single flush edge. Costs one CSS rule.
- **Buildable:** css (margin-inline-start on body blocks at narrow widths; a 12-column grid offset on desktop). No JS.
- **Three languages:** yes: an indent works in every script, and it suits longer Thai lines well.

### 6. Engraved wide caps + light condensed serif (two-voice system)  ·  `rosewood-bkk-1`  ·  rarity 3 × fit 4

![rosewood-bkk-1](crops/rosewood-bkk-1.jpg)

- **Site:** rosewoodhotels.com_en_bangkok  ·  **Role:** type-system
- **Duplicate of:** luxury.json rosewood-1 (same Rosewood design system, seen on rosewoodhotels.com/en/default)
- **What:** Labels, section kickers and venue names are in Engravers Gothic: wide, flat-sided, heavy caps at ~13px with ~0.3em tracking ('DINING', 'SALTWATER POOL', 'NAN BEI'). Headings are in Austin Light, a light, narrow, high-contrast serif, at ~44px/1.1 in sentence case. Body is the same light serif at ~18px. The main nav is also in that serif, sentence case, ~15px, which is unusual (nav is rarely serif or lower case). Buttons use the wide caps at 10px, tracked, in square black blocks (Reserve 103x46, no radius) or with a 1px hairline outline. Ground is warm off-white #FAFBF5; one accent, deep green #023C2D, is used only for Reserve.
- **Evidence:** `shots/rosewoodhotels.com_en_bangkok/desktop-03.jpg` [30, 390, 400, 340]; also `shots/rosewoodhotels.com_en_bangkok/desktop-07.jpg` [480, 700, 480, 140]
- **Why valuable:** Wide engraved caps call up stationery and engraving (letterheads, banknotes), the authority of a private bank. Tiny-and-wide against large-and-narrow gives strong hierarchy from only two families.
- **Buildable:** needs-bespoke-assets (licensed fonts). A CSS substitute is any wide grotesk at 600 weight with 0.25em tracking plus a light condensed serif.
- **Three languages:** with care: the tracked-caps voice has no Thai or Chinese equivalent. Map it to a smaller, bolder loopless Thai with no tracking, and to CJK with at most 0.1em letter-spacing.

### 7. Pivot-phrase headline  ·  `pwc-1`  ·  rarity 3 × fit 4

![pwc-1](crops/pwc-1.jpg)

- **Site:** pwc.com_th_en.html  ·  **Role:** opening
- **What:** The hero is one sentence over a photo, split into three lines. Lead clause in ITC Charter 32px regular, white. The pivot 'so you can' in Charter bold at ~84px with tight leading (~0.9). Continuation back at 32px regular. Left-aligned at x=30. Ratio ~2.6:1. Then an outlined white square-cornered button 'Learn more >' (148x52).
- **Evidence:** `shots/pwc.com_th_en.html/desktop-00.jpg` [0, 130, 720, 300]
- **Why valuable:** Emphasis by scale inside one sentence, rather than a coloured or italic accent word, gives a spoken rhythm and a quotable promise.
- **Buildable:** css. No JS.
- **Three languages:** with care: word order differs, so the pivot must be written per language (e.g. 'เพื่อให้คุณ', '让您'). The big Thai line needs line-height 1.25 or more, never 0.9, or the marks above clip.

### 8. Awards as a captioned register  ·  `capella-2`  ·  rarity 2 × fit 5

![capella-2](crops/capella-2.jpg)

- **Site:** capellahotels.com_en_capella-bangkok  ·  **Role:** proof
- **What:** 3-column grid (columns ~420px from x=80) of award marks in their own colours, about 160px tall. Under each: a 2-line Goudy Light caps title (~24px) naming the award and year, then one 15px grey (#888) Calibre line stating exactly what was won ('Capella Bangkok – No.2', 'Three MICHELIN Keys – An extraordinary stay', 'Côte by Mauro Colagreco'). Rows ~120px apart, with no cards, borders or shadows. A second register, 'Health & Sustainability', repeats the pattern.
- **Evidence:** `shots/capellahotels.com_en_capella-bangkok/desktop-06.jpg` [60, 150, 1260, 680]
- **Why valuable:** Specific, checkable claims (rank, category, year) are what make proof believable. It reads like a register or catalogue, not a logo wall.
- **Buildable:** css. No JS.
- **Three languages:** yes: but the titles must carry hierarchy through size and weight, not caps, in Thai and Chinese. For a firm, entries could read 'Chambers Asia-Pacific 2026 — Band 2, Tax' or 'TFAC registration no. …'.

### 9. Centre-stage carousel with clipped wings  ·  `rosewood-bkk-2`  ·  rarity 3 × fit 3

![rosewood-bkk-2](crops/rosewood-bkk-2.jpg)

- **Site:** rosewoodhotels.com_en_bangkok  ·  **Role:** services
- **Duplicate of:** luxury.json rosewood-3 (same Rosewood design system, seen on rosewoodhotels.com/en/default)
- **What:** The active slide sits dead centre (portrait image 450x590). The neighbouring slides are cut by the viewport edges, with only ~200px of each showing, and the gutters between are ~290px of empty ground (templates use ~24px). The active image is ~15% taller than its neighbours (590 against 510). Only the active slide carries text: a wide-caps label, 2 lines of serif body and an underlined 'Discover'. The neighbours show only their wide-caps label ('NAIL BAR', 'FITNESS STUDIO').
- **Evidence:** `shots/rosewoodhotels.com_en_bangkok/desktop-07.jpg` [0, 100, 1440, 740]
- **Why valuable:** Generous empty space reads as luxury. It turns a carousel into a gallery wall that shows one thing at a time.
- **Buildable:** css+small-js (scroll-snap to centre plus a class on the active slide). Without JS: a horizontal scroll-snap strip that still works.
- **Three languages:** yes

### 10. CTA band fused to the image + numeric slide counter  ·  `rosewood-bkk-3`  ·  rarity 3 × fit 3

![rosewood-bkk-3](crops/rosewood-bkk-3.jpg)

- **Site:** rosewoodhotels.com_en_bangkok  ·  **Role:** navigation
- **Duplicate of:** luxury.json rosewood-2 (same Rosewood design system, seen on rosewoodhotels.com/en/default)
- **What:** Full-bleed promo image (1440x395, darkened ~30%) with a centred wide-caps headline (~40px) and 3 lines of serif body. Directly under it, with no gap, a full-width black band 64px tall holds one tiny caps label 'SHOP NOW' (10px, 0.3em tracking); the whole band is the button. 40px below, pagination is set as type: '1 —— 3' (wide-caps numerals ~11px with a 24px hairline between), centred. The same counter is used on the dining carousel ('1 —— 2').
- **Evidence:** `shots/rosewoodhotels.com_en_bangkok/desktop-06.jpg` [0, 100, 1440, 540]
- **Why valuable:** The button becomes part of the structure, like a plinth under the picture, instead of a pill. The counter shows how many there are, like page numbers in a book.
- **Buildable:** css (the counter needs a little JS for the live number; without JS it shows a static total).
- **Three languages:** yes: numerals work everywhere. Set the Thai label without tracking.

### 11. Warm blush fade under the sticky header  ·  `capella-3`  ·  rarity 3 × fit 3

![capella-3](crops/capella-3.jpg)

- **Site:** capellahotels.com_en_capella-bangkok  ·  **Role:** navigation
- **What:** The fixed white header (two rows, 70px + 43px, with a 1px light-grey rule between) ends in a ~40px strip that fades from blush #F8EAE1 to transparent, not a grey drop shadow. Content scrolls under it. It is present in every frame.
- **Evidence:** `shots/capellahotels.com_en_capella-bangkok/desktop-02.jpg` [0, 0, 1440, 200]
- **Why valuable:** A shadow tinted with the brand's warm neutral feels like paper and light rather than software chrome. Tiny effort, rarely done.
- **Buildable:** css (a gradient pseudo-element on the sticky header).
- **Three languages:** yes

### 12. Brand slab composited into the photograph  ·  `pwc-2`  ·  rarity 3 × fit 3

![pwc-2](crops/pwc-2.jpg)

- **Site:** pwc.com_th_en.html  ·  **Role:** other
- **What:** The orange (#FE611C) parallelogram (skewed ~30 degrees, ~1:5) appears in every photo, in the hero and in the 16:9 card thumbnails. It sits in the middle ground: it passes behind the people and foreground objects (the hologram table and the people overlap it) and in front of the background, at the same angle every time, sometimes as two offset slabs.
- **Evidence:** `shots/pwc.com_th_en.html/desktop-01.jpg` [40, 0, 1360, 200]; also `shots/pwc.com_th_en.html/desktop-00.jpg` [380, 420, 1060, 260]
- **Why valuable:** One brand gesture built into the photograph makes generic stock look commissioned and owned.
- **Buildable:** needs-bespoke-assets (compositing per photo). A CSS overlay with clip-path is possible but loses the 'behind the subject' depth.
- **Three languages:** yes

### 13. Footprint map in one flat brand colour  ·  `tilleke-1`  ·  rarity 2 × fit 4

![tilleke-1](crops/tilleke-1.jpg)

- **Site:** tilleke.com  ·  **Role:** proof
- **What:** A two-column band on navy #002043. Left (x150-640): section label (28px red rule + small caps), Poppins SemiBold H2 ~50px on two lines, a red text link with an arrow, then a 2x2 stat grid (numerals ~60px regular, labels Source Sans 16px; the rows are separated by 50px white hairlines aligned to each stat). Right (~55%): Southeast Asia drawn as flat red #ED2726 shapes with no basemap or labels, and white pins on the office cities. The map is cut by the top of the band and bleeds off the right edge. The numbers count up: desktop caught 163+/89/41/5 mid-count and phone shows 174+/95/43/6.
- **Evidence:** `shots/tilleke.com/desktop-01.jpg` [140, 90, 1300, 540]
- **Why valuable:** Turns the presence claim ('6 offices') into a single, owned graphic shape in the brand colour, plainer and stronger than a pin map.
- **Buildable:** needs-bespoke-assets (one SVG map) + css. The count-up is small JS; without JS the final numbers show.
- **Three languages:** yes

## Thai typesetting: what the screenshots show

**Caveat.** Screenshots come from a headless Linux machine. Any Thai text a site does not serve as a webfont is drawn in that machine's fallback font (Loma, a looped monoline sans). On a Mac it would be Thonburi/Sukhumvit, and on Windows Leelawadee UI/Tahoma. Judgements of PwC's Thai therefore describe the fallback problem, not PwC's intent.

**Coverage.** Thai text was visible on only 2 of the 7 assigned sites (PwC, Cadson Demak), plus the forum at wcp.co.th and sa-accounttax.com in the baseline. The luxury Bangkok hotels show no Thai at all on their /en pages.

**Measured proportions** (pixel heights in the 1440-wide frames):

| site | font | Latin cap | Latin x | Thai body | Thai ÷ x | Thai ÷ cap | line pitch |
|---|---|---|---|---|---|---|---|
| cadsondemak.com | Graphik TH semibold ~28px | 20 | 15 | 17 | 1.13 | 0.85 | 42px = 1.5 (2-line title) |
| pwc.com_th_en.html | Charter 32px + Thai fallback (Loma) | 23 | 17 | 19 | 1.12 | 0.83 | 45px = 1.4 headings; body ~17px on ~30px = ~1.75 |
| sa-accounttax.com (baseline) | Prompt 16px body (loopless) | – | – | – | – | – | 24px = 1.5 |

At the same font-size, Thai consonants come out about 1.12× the Latin x-height in both pairs. Size is therefore not the problem. Style is: stroke contrast, loops, terminals and digits.

**Rules for the builder** (each comes from evidence above):

1. Every theme declares its own Thai family and its own CJK family, self-hosted. Never let Thai fall back. PwC shows looped monoline Thai next to a bracketed serif, with serif digits ('2569') inside Thai lines.
2. Choose Thai type by its partner. A Thai face designed with the Latin face (Graphik TH; free: IBM Plex Sans Thai with IBM Plex, Noto Sans/Serif Thai with Noto) keeps weight and terminals in step. In both measured pairs the size ratio was already right at the same font-size (Thai body ~1.12x the Latin x-height), so the mismatch to fix is style, not size.
3. Loopless Thai for display, UI and modern voices (every premium Thai example here). Looped Thai for long reading and formal documents. Offer both per theme, and allow loop against loopless as a deliberate contrast, as Cadson does.
4. Thai line-height: headings 1.4-1.5 and body 1.6-1.8. Never use the 0.9-1.1 display leading that Latin themes use, or the vowels and tone marks above clip (risk on 'so you can'-style pivots and cropped display type).
5. Line breaks: the browser's dictionary splits compounds and idioms ('ของผู้ | บริโภค', 'ความ | ท้าทาย', 'ผู้ | จัดการ', 'หัว | เลี้ยวหัวต่อ', 'สภาพปกติ | ใหม่', 'ผู้ | คว้าโอกาส'; SA: 'เหมาะสม | ที่สุด', 'ไม่ | ต้อง'). For headings, give authors a 'keep together' phrase mark (a nowrap span) and/or explicit break points (<wbr>/ZWSP), and use text-wrap: balance. Test word-break: keep-all per browser before relying on it.
6. Never centre long Thai paragraphs. SA Accounting centres them and gets ragged edges on both sides plus orphans like '17 | ปี'.
7. Underlines: skip-ink breaks the underline around below-base vowels and descenders (ุ ู ฏ ฎ) in PwC's Thai link titles, so it looks chopped. For Thai links use text-underline-offset of 0.3em or more, a hairline under the block, or colour alone.
8. No caps, tracking or italic in Thai or Chinese. Remap the 'tracked caps label' voice (Rosewood, Capella, our own eyebrow) to small bold Thai with letter-spacing 0. Remap the 'italic accent word' (our site's gold italic) to colour or weight. Oblique Thai looks broken.
9. Thai titles ran 3-4 lines where English ran 2 in the same card width (PwC). Cards must allow variable title height, or clamp Thai at 3 lines rather than 2.
10. Digits: Thai copy uses Buddhist-era years (2569) and Arabic digits. Make sure the Thai face's digits match the Latin face's. Thai numerals (๐-๙) appeared nowhere.

**Evidence crops for these notes:**

- `thai-ts-1`: PwC desktop-01 [40,215,920,130]: Charter Latin title beside a Thai title in fallback Loma; 'ผู้ | บริโภค' split; Charter digits '2569' inside the Thai line.  
  ![thai-ts-1](crops/thai-ts-1.jpg)
- `thai-ts-2`: PwC desktop-07 [40,120,840,420]: underlined Thai link titles with skip-ink gaps; body ~17px at ~30px pitch; 'ความ | ท้าทาย' and 'ผู้ | จัดการ' splits.  
  ![thai-ts-2](crops/thai-ts-2.jpg)
- `thai-ts-3`: sa-accounttax desktop-01 [100,70,620,290] + [0,650,1440,130]: Prompt loopless body 16px/24px; centred Thai paragraphs with orphans.  
  ![thai-ts-3](crops/thai-ts-3.jpg)
- `thai-ts-4`: PwC desktop-04 [735,455,660,300]: 4-line Thai card titles; 'หัว | เลี้ยวหัวต่อ' and 'ผู้ | คว้าโอกาส' splits; Charter and Loma mixed in one title.  
  ![thai-ts-4](crops/thai-ts-4.jpg)

## Site notes

- **cadsondemak.com**: Thai type foundry's magazine, and the only assigned site that is Thai-first. One family, Graphik TH (loopless) plus Graphik Thai Loop (looped), across all sizes: 12px bold labels, 28px semibold titles, ~36px light index, and huge display type. Flat saturated grounds (cyan, red, magenta, black, cream) with no photography; typography is the image. Thin 'perforation' dashed rule, custom cursor, video slider with '1 / 10' and a 470px progress track. A cookie banner covers part of each frame. Captured late (arrived after the first pass); 4 findings.
- **rosewoodhotels.com_en_bangkok**: All 3 findings confirm, on the Bangkok property, the same Rosewood system the luxury group recorded from rosewoodhotels.com/en/default (luxury.json rosewood-1/2/3). Treat them as duplicates when merging. Two families: Engravers Gothic (wide caps) and Austin Light/Italic (light condensed serif). About 4 sizes (10-11 / 15 / 18 / 44px). Off-white #FAFBF5, black and one deep green #023C2D; square buttons only, no radius anywhere. Desktop hero video did not render (empty cream frame with a 'Discover' button). Phone: full-width deep-green 'Reserve' bar fixed at the bottom. No Thai text on the English page.
- **capellahotels.com_en_capella-bangkok**: Goudy Light (caps headings ~50px, lede ~30px in grey) and Calibre (body 15px grey, nav small tracked caps). Text uses only two greys (#6F6F6F lede, #777 body). Wide asymmetric spacing: title at x=150, body column at x=820. Desktop hero did not render (white frame). The phone hero shows the star mark and wordmark centred on a full-bleed photo with an underlined 'WATCH VIDEO'. No contact sheet existed, so I built my own from the single frames. No Thai text.
- **pwc.com_th_en.html**: Headings in PwC ITC Charter (serif), UI in PwC Helvetica Neue, one orange accent. The /en page mixes Thai and English article titles in the same card styles. No Thai webfont is served, so Thai renders in the device fallback (Loma on our capture machine). This is the main evidence for the Thai typesetting notes below: font mismatch, compound words split across lines, broken underlines, and Thai titles running 3-4 lines where English runs 2. Otherwise a corporate card feed with 'Load more' and 'View all'.
- **tilleke.com**: English page only, with no Thai text visible. Poppins SemiBold headings, Source Sans Pro body 16px, navy #002043 + red #ED2726. The hero uses the wordmark itself as the headline (~90px) and a site search as the main action. Section labels are a short red rule + small caps (common). The rest is a standard corporate template (slider dots, cards, 'TOP' button).
- **mandarinoriental.com_en_bangkok_chao-phraya-river**: 0 findings. Futura PT caps headings (~36px 'STAY', 'DINE') with an inline 'View All >' beside them, AvenirNext body, black two-tier nav, pale-sage pill buttons, carousels with dots, FAQ accordion, black footer. The hero image did not load (grey placeholder gradient) and room images were still showing spinners. A standard hotel template. No Thai text.
- **wcp.co.th**: Did not load as intended. The domain now serves an unrelated Thai classified-ads forum ('WGAME'), and the re-capture is identical. Not reviewed. Thai there is 13px in the device fallback.
