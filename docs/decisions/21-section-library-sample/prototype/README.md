# PROTOTYPE — #21 section library sample (throwaway)

Kept as the record of decision #21 (`../../21-section-library-sample.md`). **Not builder code**: the real engine and the
first real presets are written fresh in the Admin repo and `builder-library` (decision #31), following the decision.

| File | What it is |
|---|---|
| `engine/template.mjs` | Strict Mustache subset (decision #16-5), pure |
| `library.mjs` | 3 section types, 9 presets in the stored record shape, system strings, sample content (EN/TH/ZH) |
| `themes.mjs` | Test theme A "Slate" and B "Paper": every colour, font, size, space and radius |
| `build.mjs` | Library check, contrast check, generated theme CSS, rendering; writes `out/library/*.json` |
| `page.mjs` | Writes `out/sample.html` (published as an Artifact) |
| `negtest.mjs` | Feeds 9 deliberately broken presets to the check |
| `shot.cjs` | Playwright screenshots at 1280 and 390 px |

Run (Node 22): needs `../../15-type-system/prototype` built first (its `out/fonts.css`); adjust the path in `build.mjs`,
then `node page.mjs`.
