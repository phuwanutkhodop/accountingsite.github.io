# D.A. brand seal: locked design 346

**Status:** locked by the owner, 2026-10-05. Use the geometry and colours below; never redraw the seal by eye.

**What it is:** the brand seal, not the legal company seal. It is in English only and carries no year.

**Master files:**
- SVG with exact outlines: `brand/seal/da-seal-346-{paper,oxblood,night}.svg`
- Machine-readable spec: `brand/seal/da-seal-346.json`

**The monogram:** always the full logo 153, as defined in `docs/brand/da-logo-153.md`.

## 1. What is in it (outside in)

| # | Element | Notes |
|---|---|---|
| 1 | Thick ring + thin ring | The ring pair. |
| 2 | Name on the top arc | "D.A. ACCOUNTING & CONSULTING". No "CO., LTD." (owner rule). |
| 3 | Lower arc | Flowers alternate with rose diamonds, largest at the foot and shrinking toward both ends. |
| 4 | Foot flower | One large flower at the bottom centre. |
| 5 | Pattern band | The 153 lattice in reverse: background-colour ground, diamond rings in the letter colour, rose flowers. Fine lines run inside and outside the band. |
| 6 | Top clasp | A flower that interrupts the band at the top. |
| 7 | Monogram | D A in full 153 detail, centred. |

The meanings of the lattice, the two diamond rings and the flower are the owner's, pinned in the logo spec §1. They carry over to the band: the band is the same pattern, shown as a ring around the founders' initials.

## 2. Colours (exact)

The seal uses the logo's colours. Nothing is added.

| Version | Background | Letter colour | Rose | Silver (monogram only) |
|---|---|---|---|---|
| **Paper** (main) | `#F2EEEA` | `#7A2229` | `#B07E80` | `#D4D5D8` |
| **Oxblood** | `#7A2229` | `#F6EFE8` | `#C29998` | `#85878C` |
| **Night** | `#1B1112` | `#EFE6DC` | `#BE9491` | `#85878C` |

**What takes which colour:**

| Colour | Elements |
|---|---|
| Letter colour | Both outer rings, the name, the flowers in the arc, the clasp and foot flowers, the band's diamond rings, and its edge and fine lines. |
| Rose | The diamonds in the arc and the flowers inside the band. |
| Background | The seal disc, the band's ground, and the small discs behind the clasp and foot flowers. |

## 3. Proportions (scale-proof)

**S** is the seal's diameter, measured to the outer edge of the thick ring. In the master files S = 285.2 units and the centre is at (150, 150). To draw the seal at any size, choose S and multiply.

| Measure | × S | Master units |
|---|---|---|
| Thick ring: radius / line | 0.4944 / 0.0112 | 141 / 3.2 |
| Thin ring: radius / line | 0.4716 / 0.0035 | 134.5 / 1 |
| Name: baseline radius / font size | 0.3997 / 0.0473 | 114 / 13.5 |
| Name tracking | 0.14 em | — |
| Lower arc radius | 0.4348 | 124 |
| Arc pieces | 15 over 150°, centred on the bottom | — |
| Arc flower radius at the foot | 0.0189 | 5.4 |
| Arc diamond half-height at the foot | 0.0161 | 4.6 |
| Arc grading | Size × (1 − 0.9·\|t\|), with t running from −0.5 to 0.5 along the arc: 100% at the foot, 55% at the ends | — |
| Foot flower radius (on a background disc of the same radius) | 0.0386 | 11 |
| Band inner / outer radius | 0.3015 / 0.3787 | 86 / 108 |
| Band tile width / height | 0.0842 / 0.1178 | 24 / 33.6 |
| Band edge line | 0.0035 | 1 |
| Fine lines: gap from the band / line weight | 0.0091 / 0.0018 | 2.6 / 0.5 |
| Top clasp flower: centre radius / flower radius / background disc | 0.3401 / 0.0368 / 0.0403 | 97 / 10.5 / 11.5 |
| Monogram width (logo 153) | 0.4067 | 116 |
| Monogram centre, above the seal centre | 0.0140 | 4 |

**Band pattern:**
- The tiles are laid like the logo's lattice: rows staggered by half a tile, with one tile centre on the seal centre.
- Diamond rings sit at 94% and 62% of the tile, with line weight 0.0021 S.
- The flower radius is 0.17 of the tile width (0.0143 S). The small points are 0.52 of that.

**Arc order:** flower, diamond, flower… ending on a flower at each end. The centre piece is replaced by the large foot flower.

## 4. Use

**Minimum size:** 160 px across on screen, or 30 mm in print. Below that the name can no longer be read; use the logo instead.

**Choosing a version:**
- **Paper** is the main version.
- **Oxblood** is for covers and dark panels.
- **Night** is for dark mode.

Each master file includes its own background disc, so it can sit on any surface.

**Do not:**
- stretch the seal;
- change the name, or add "CO., LTD." or a year;
- strip detail from the monogram;
- recolour the seal by hand;
- rotate the band pattern;
- change the size of the pattern.

**One-colour version (rubber stamp, embossing, foil):** not needed. The owner decided on 2026-10-05 not to make one.

## 5. Where it came from

The decision trail is in `docs/decisions/36-generated-imagery.md` §7, seal rounds 1–13:
- 244 / 270 / 271: alternating diamonds and flowers.
- 295: the name on top, the alternation along the lower half.
- 314: an inner pattern band.
- 321: the band reversed, with a flower clasp and one large foot flower.
- 339: fine double lines around the band.
- 346: the largest band pattern. **Locked.**
