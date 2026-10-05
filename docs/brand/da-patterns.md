# D.A. brand patterns: locked set 401 · 406 · 417 · 420

**Status:** locked by the owner, 2026-10-05.

**Master files:** `brand/pattern/`
- One seamless repeat tile per pattern and version: `da-pattern-{401,406,417,420}-{paper,oxblood,night,quiet}.svg`.
- Tile sizes: `brand/pattern/da-patterns.json`.

**Related specs:** these patterns are built from the logo (`docs/brand/da-logo-153.md`). The meanings of the lattice, the two diamond rings and the flower are the owner's, pinned in that spec §1.

## 1. The set

| # | Pattern | Suggested role (proposal; owner to confirm) |
|---|---|---|
| **401** | The 153 lattice as a fabric: the inside of D A, laid out flat. | Strong accent areas: website header and footer bars, slide covers, dividers. |
| **406** | Flowers only on the lattice points, with tiny rose diamonds between. | The everyday background. Its quiet version suits web pages and documents; full strength suits letterhead bands and covers. |
| **417** | D A monogram canvas: D A in half-drop, rose flowers between. | Brand canvas for social posts, slide title backgrounds and folders. |
| **420** | D A inside the two diamond rings (the 153 tile, with the monogram in place of the flower). | Feature images, such as social covers and slide section breaks. |

## 2. Colours

Every version uses the locked palette. Nothing is added.

| Version | Background | Letter colour | Rose | Silver |
|---|---|---|---|---|
| **Paper** | `#F2EEEA` | `#7A2229` | `#B07E80` | `#D4D5D8` |
| **Oxblood** | `#7A2229` | `#F6EFE8` | `#C29998` | `#85878C` |
| **Night** | `#1B1112` | `#EFE6DC` | `#BE9491` | `#85878C` |
| **Quiet** | The paper version drawn at **14%** over paper `#F2EEEA`. Use it behind text. | | | |

**Note on 401:** its ground is the letter colour, exactly as inside D A. On the oxblood and night versions, the letters are cream, so 401's ground there is cream too. This is how the owner saw and locked it.

## 3. Geometry (master units = px at 100%)

Each tile is a half-drop: one motif sits at the tile centre, and its neighbours sit on the four corners. Tiles join without a seam.

| # | Tile (w × h) | What is in it |
|---|---|---|
| 401 | 36 × 50.4 (s × 1.4 s, s = 36) | <ul><li>Ground: letter colour.</li><li>Two diamond rings at 94% and 62% of the tile, in rose, line 0.8.</li><li>The 153 flower in silver: radius 0.17 s (6.12); small points 0.52 of that.</li></ul> |
| 406 | 36 × 50.4 | <ul><li>Ground: background.</li><li>The 153 flower in the letter colour: radius 0.2 s (7.2), at the lattice points.</li><li>Rose diamonds, half-width 1.6 and half-height 2.4, at the quarter points between flowers.</li></ul> |
| 417 | 200 × 150 | <ul><li>Ground: background.</li><li>D A, the full logo 153, 92 wide, at the lattice points.</li><li>Rose 153 flowers, radius 9, at the edge midpoints.</li></ul> |
| 420 | 220 × 180 | <ul><li>Ground: background.</li><li>D A, the full logo 153, 96 wide, at the lattice points.</li><li>Around each D A, a diamond ring in the letter colour (half 110 × 90, line 0.8).</li><li>Inside that, a ring in rose (half 100 × 82, line 0.6).</li></ul> |

## 4. Use

**Scale:**
- Scale a tile evenly. Never stretch it.
- **D A patterns (417, 420):** D A must stay at least 96 px wide on screen, or 25 mm in print. That is the logo's rule for the patterned monogram.

  | Pattern | On screen | In print |
  |---|---|---|
  | 417 | At least 105% | Tile at least 54 mm wide |
  | 420 | At least 100% | Tile at least 57 mm wide |

- **401 and 406:** free to scale. Keep the flowers readable: at least 75% on screen.

**Text:**
- Put text only on the quiet version, or on a solid panel laid over the pattern.
- Never set text directly on a full-strength pattern.

**Edges:**
- The edge of an area cuts through a row of motifs.
- Where that looks busy, shift the pattern by half a tile, so the edge falls between motifs.
- On the web: `background-position: 50% 50%`, or an offset of half the tile.

**Do not:**
- recolour by hand;
- rotate a pattern;
- mix two patterns in one area;
- put a pattern behind the logo or the seal without a clear panel;
- strip detail from D A.

**Web example:**
```css
.band { background: url(../brand/pattern/da-pattern-406-quiet.svg) 50% 50% / 36px 50.4px repeat; }
```

## 5. Where it came from

The decision trail is in `docs/decisions/36-generated-imagery.md` §8:
- The owner's brief: website, documents and letterheads, social and slides. Business cards come later.
- Pattern round 1 (401–420): from the 153 lattice, new motifs, and with D A.
- The owner locked 401, 406, 417 and 420.
