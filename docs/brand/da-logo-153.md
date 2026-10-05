# D.A. logo — locked design 153

**Status:** locked by the owner, 2026-10-05. The geometry and colours below are the logo; do not redraw by eye.
**Firm:** D.A. Accounting & Consulting Co., Ltd. — **D is Diamond and A is Atom: the names of the two founders** (owner, 2026-10-05).
**Master files:** `brand/logo/` (SVG, exact outlines) · machine-readable spec: `brand/logo/da-logo-153.json`.

## 1. What the elements mean (owner's definitions, pinned)

These are the owner's words and are the official meaning of each element. Quote them as written.

| # | Element | Meaning (owner, Thai) | Meaning (English) |
|---|---|---|---|
| 1 | The repeating pattern as a whole | การใช้ลวดลายที่มีความสม่ำเสมอคือการบ่งบอกความสม่ำเสมอของมาตรฐานการทำงาน | A pattern that repeats evenly stands for consistent standards of work. |
| 2 | Diamond frame, ring 1 (outer) | กรอบ Diamond ชั้นที่ 1 เป็นตัวแทนความมุ่งมั่นในการส่งมอบผลงานคุณค่าสูงให้ลูกค้า | Our commitment to delivering high-value work to clients. |
| 3 | Diamond frame, ring 2 (inner) | กรอบ Diamond ชั้นที่ 2 เป็นตัวแทนกฎระเบียบและมาตรฐานของการทำงาน เพื่อสร้างคุณภาพของงานที่สม่ำเสมอ | The rules and standards of our work, which make quality consistent. |
| 4 | Flower at the centre of each diamond | ดอกไม้ตรงกลางกรอบ Diamond เป็นตัวแทนของผลงานที่ดี ส่งมอบมูลค่าแก่ลูกค้า ผ่านคุณค่าของกรอบ Diamond ทั้ง 2 ชั้นที่บริษัทยึดมั่น | Good work that delivers value to clients, made possible by the two diamond frames the firm holds to. |

**Fact (owner):**

| Element | Meaning |
|---|---|
| The letters D and A | **Diamond** and **Atom**, the two founders. The firm carries their names. |

**Proposed by Claude for the remaining elements. Not yet confirmed by the owner:**

| Element | Proposed meaning |
|---|---|
| D and A overlapping, with the overlap opened | The two founders working as one. Where they meet, nothing is hidden. |
| Eight-point flower (4 petals + 4 small points) | In the spirit of ลายประจำยาม, the Thai guardian motif. |
| Oxblood | Seriousness and permanence: the colour of ledger bindings. |
| Silver flowers | Quiet, lasting value. |

## 2. Colours (exact)

All colours are solid. Never use transparency to make the ring colour. The ring colour already resolves the rose tint to a solid code.

| Background | Background | Letters | Diamond rings | Flowers |
|---|---|---|---|---|
| **Paper** (main) | `#F2EEEA` | `#7A2229` oxblood | `#B07E80` rose | `#D4D5D8` silver |
| **Oxblood** | `#7A2229` | `#F6EFE8` cream | `#C29998` rose | `#85878C` deep silver |
| **Night** | `#1B1112` | `#EFE6DC` cream | `#BE9491` rose | `#85878C` deep silver |

**Notes:**
- Silver was added at the owner's request. It is the only colour outside the #33 palette. Use the deep silver on cream letters so the flowers stay visible.
- For print: specify Pantone or CMYK matches from these codes with the printer, and approve a proof against a screen-calibrated reference. The codes above are the master values.

## 3. Proportions (scale-proof)

Every measure is a ratio of **H**, the cap height of the letter D. In the master files H = 190 units. To draw the logo at any size, choose H and multiply.

| Measure | × H | In master units |
|---|---|---|
| Mark width (D left edge to A right edge) | 1.6425 | 312.07 |
| Mark height (A apex to baseline) | 1.0193 | 193.67 |
| Width of D | 0.9340 | 177.46 |
| Overlap of A onto D | 0.2989 | 56.79 |
| Letter size (font size) | 1.3333 | 253.33 |
| Pattern tile width (s) | 0.2316 | 44 |
| Pattern tile height (1.4 s) | 0.3242 | 61.6 |
| Ring 1 (outer) | 94% of the tile half-width and half-height | — |
| Ring 2 (inner) | 62% of the tile half-width and half-height | — |
| Ring line weight | 0.00526 | 1.0 |
| Flower radius, main petals | 0.0394 (= 0.17 s) | 7.48 |
| Flower radius, small diagonal points | 0.0205 (= 0.52 of main) | 3.89 |
| Petal width / bulge | 0.34 / 0.55 of petal radius (small points: 0.40 / 0.55) | — |
| Pattern origin (a tile centre) | −0.1053 H, −0.1053 H from the D's top-left corner | (0, 0) |
| Name line cap size | 0.0752 | 14.28 |
| Name line baseline below the letters' baseline | 0.2316 | 44 |
| Clear space on every side | 0.25 | 47.5 |

### Construction (how to rebuild exactly)

1. Set **D** and **A** in Bodoni Moda Bold (optical size 11) at font size 1.3333 H.
2. Place the A so that its left edge sits 0.2989 H inside the right edge of the D.
3. Combine both letters into one shape with the **even-odd rule**. Where they overlap, the shape opens.
4. Fill the shape with the letter colour.
5. Inside the shape only (clipped), lay the staggered diamond lattice:
   - Tiles are s × 1.4 s.
   - Every other row is shifted by s/2.
   - Rows are spaced 0.7 s apart.
   - One tile centre sits at the pattern origin.
6. In every tile, draw:
   - ring 1 and ring 2 as lozenges, with mitred corners;
   - the eight-point flower at the centre.
7. **Name line:** "D.A. ACCOUNTING & CONSULTING" in Cormorant Garamond SemiBold capitals, tracking 0.20 em. It spans the mark's width exactly and is centred under the mark.

## 4. Use

**Versions:**

| Version | Use |
|---|---|
| **Patterned** (`da-logo-153-*.svg`, `da-lockup-153-*.svg`) | 96 px wide or larger on screen, or 25 mm or wider in print. |
| **Plain** (`da-logo-small-*.svg`) | Same shape without the pattern. Below 96 px, for favicons, and for embossing, foil or one-colour stamping. Minimum 16 px. |

**Choose the background version; never recolour by hand:**
- Paper is the main version.
- Oxblood is for the header bar and covers.
- Night is for dark mode.

**Do not:**
- stretch the logo, or change the overlap;
- rotate or rescale the pattern relative to the letters;
- change the tile size, add or remove rings, or swap the flower;
- add effects (shadows, gradients, glow);
- set the letters in another font.

## 5. Where it came from

The decision trail is in `docs/decisions/36-generated-imagery.md`, rounds 1–15:
- 45 (overlap window)
- → 102 (nested diamonds)
- → 122 (ประจำยาม flower)
- → 126 (eight-point flower, locked)
- → 153 (rose rings and silver flowers, locked)
