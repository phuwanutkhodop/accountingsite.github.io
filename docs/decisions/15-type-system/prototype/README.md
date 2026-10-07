# PROTOTYPE — #15 type specimen (throwaway)

Kept as the record of decision #15 (`../../15-type-system.md`). **Not Admin code**: the real subsetter is
written fresh in the Admin repo (decision #31) following the decision, not copied from here.

| File | What it is |
|---|---|
| `fontsubset.mjs` | HarfBuzz WASM subsetter + WOFF 1.0 writer (the shape of a future `services/fonts.js`) |
| `content.mjs` | Specimen copy in EN / TH / ZH |
| `build.mjs` | Subsets every face as Publish would; writes `../out/` fonts, `fonts.css`, sizes |
| `render.mjs` | Writes `../out/specimen.html` (fonts inlined as data URIs, published as an Artifact) |
| `gcompare.mjs` | Measures what Google Fonts' slices cost for the same Chinese text |
| `trim.mjs` | Measures Chinese masters trimmed to GB 2312 |
| `csp-test/` | Runs the subsetter in Chromium under decision #16's exact policy |

Run (Node 22): put the font files from `google/fonts` in `../dl/`, then
`npm install && node build.mjs && node render.mjs`.
