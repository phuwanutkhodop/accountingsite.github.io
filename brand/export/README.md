# D.A. brand: export pack (ready-to-use files)

**Ready-to-use files for every program, made from the locked masters in `brand/`.** The masters remain the originals; everything here is derived from them.

## Which file to use

| Use in… | ใช้ใน… | Take | Folder |
|---|---|---|---|
| Canva, PowerPoint, Word, Google Slides, LINE, Facebook, Photoshop | Canva, PowerPoint, Word, สไลด์, LINE, Facebook, Photoshop | **PNG** | `png/` |
| Illustrator, Affinity, InDesign, print shop | Illustrator, งานพิมพ์ร้านพิมพ์ | **PDF** (vector: never blurs at any size) | `pdf/` |
| Figma, Inkscape, or any program that imports SVG | Figma, Inkscape, โปรแกรมที่รับ SVG | **compatible SVG** | `svg-compatible/` |
| Website | เว็บไซต์ | the **masters** in `brand/logo`, `brand/seal`, `brand/pattern` (smallest files) | `../` |

## The PNG files

| What | Files | Notes |
|---|---|---|
| **Logo, lockup, small logo** | `png/logo/` | <ul><li>Three versions: paper, oxblood and night.</li><li>Each is `-transparent` (no background) or `-background` (on its brand colour).</li><li>Two sizes: 1000 px and 4000 px wide.</li></ul> |
| **Seal** | `png/seal/` | <ul><li>1000 and 4000 px.</li><li>See-through outside the circle.</li></ul> |
| **Pattern tiles** | `png/pattern/*-tile-WxHpx.png` | <ul><li>One repeat. Every tile is a whole number of pixels, so repeating it leaves no seam.</li><li>Use the tile in programs that can repeat an image.</li></ul> |
| **Pattern swatches** | `png/pattern/*-swatch-3000px.png` | <ul><li>Ready-tiled squares, 3000 × 3000 px.</li><li>For programs that cannot repeat an image, such as Canva and PowerPoint.</li></ul> |

## The PDF files

- **Size:** each page is exactly the artwork's size, at 1 unit = 0.75 pt.
- **Logo, lockup, small logo:** the logo is 82.6 mm wide at 100%. These are vector, so scale freely.
- **Seal:** included.
- **Pattern tiles:** these are vector tiles. In Illustrator, drag one into the *Swatches* panel to make a repeating pattern.
- **Printing D A patterns:** keep the D A at least 25 mm wide (see `docs/brand/da-patterns.md`).

## The compatible SVG files

They draw the same as the masters, but use only basic SVG:
- no references (`<use>`);
- no pattern fills (`<pattern>`);
- no CSS styles;
- no even-odd rule.

Many programs ignore the even-odd rule. Ignoring it would fill the opening where D and A overlap, and let the seal band spill out of its ring. Here those shapes are worked out exactly in advance instead.

## How these files were made and checked

- **Made with:** `tools/brand/export_pack.py` and `export_pack.js` (see `tools/brand/README.md`).
- **Checked with:** `tools/brand/verify_export.py`, on 2026-10-05: 510 of 510 checks passed. These include:
  - a second, non-browser program draws every compatible SVG the same as the PNG;
  - a second PDF program draws every PDF the same as the PNG;
  - every PDF is pure vector, with no pictures inside, at exactly the artwork size and scale;
  - the pattern tiles repeat without seams;
  - the background colours are exact, and there are no white hairlines at the edges.
- **Fingerprints:** `MANIFEST.sha256` holds a SHA-256 for every file here. Verify with `sha256sum -c MANIFEST.sha256`, run inside this folder.

**Colours for print (CMYK or Pantone):** not defined yet. Agree them with the printer on the first print job, against the screen colours in `docs/brand/da-logo-153.md` §2.
