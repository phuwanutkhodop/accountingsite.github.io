# Reviewer brief — scarce, high-value design details

## Why
We are building the Design Library of a premium, no-server website builder (static sites; English, Thai and
Simplified Chinese). The owner rejected our first presets: plain grids, rounded buttons, standard hero + cards.
**"Nobody would pay for that."** The library must contain what top professionals do that others rarely do.
Think like an economist: value comes from **scarcity and craft**. Your job is to *look* at real work and extract
the rare, distinctive, rebuildable details.

## Your material
Screenshots in `shots/<site>/` (no internet needed, do not browse):
- `sheet-desktop-a.jpg`, `sheet-desktop-b.jpg`: 1440×900 frames while scrolling down (2×2 per sheet, labelled);
- `sheet-phone.jpg`: iPhone frames while scrolling (3×2);
- the single frames `desktop-0N.jpg` (1440×900) and `phone-0N.jpg` (780×1688, 2×) — open them when you need detail;
- `signals.json`: fonts loaded, libraries (gsap, lenis, webgl…), CSS techniques found in their stylesheets.

Look at every sheet of every site you are given. Zoom into single frames for anything promising.

## Ignore (worthless to us — we already have it)
Generic hero + headline + button; card grids; rounded buttons; standard top nav; hamburger menus; cookie banners;
logo walls; testimonial carousels; icon-in-circle features; stock gradients; "modern SaaS" layouts; anything you
would see on a typical template site. Do not report a detail just because it is well executed if it is common.

## Record (only what is distinctive)
For each site, 0–5 findings. Zero is fine and honest. A finding is something a typical template does not have:
a typographic device, a grid or composition idea, a navigation idea, an image treatment, a number/data
presentation, a rule/line system, a caption/label convention, a motion idea visible across frames, a micro-detail
(index numbers, footnotes, marginalia, running heads, time stamps, coordinates, hairlines, small caps, etc.).

For each finding write:
- `site`, `id` (site-slug + n), `name` (short, specific, e.g. "Sentence-shaped filter", not "Nice hero")
- `what`: a **rebuildable** description — composition and grid (columns, alignment, what spans what),
  type (relative sizes, weight, case, tracking, serif/sans, numerals), spacing rhythm, colour discipline,
  image treatment, motion inferred from consecutive frames. Precise enough that a designer could rebuild it.
- `evidence`: frame file + crop box `[x, y, w, h]` in that frame's pixels. **Make the crop** with Python/PIL into
  `findings/crops/<id>.jpg` (keep under ~1400 px wide; JPEG q80).
- `why_valuable`: the mechanism that makes it read as expensive/authoritative (restraint, precision, editorial
  authority, material honesty, rarity, effort visibly spent…).
- `rarity`: 1 (common on good sites) … 5 (only seen here / almost never).
- `buildable`: one of `css` · `css+small-js` · `heavy-js/webgl` · `needs-bespoke-assets` (photography, custom
  font, illustration) — and how it would degrade without JavaScript.
- `fit_professional`: 1–5, fit for a premium accounting / law / advisory firm website.
- `role`: opening · services · process · people · proof · knowledge · contact · navigation · footer ·
  type-system · grid-system · motion-system · data-presentation · other.
- `three_languages`: does it survive Thai and Chinese text (no uppercase/tracking/italics in those scripts,
  longer Thai lines, no word spaces in Chinese)? yes / with care / no — one line why.

Also write one short **site-level note** per site: its typographic system (how many sizes, ratio, families),
grid, colour discipline and motion vocabulary — only where notable.

If a site did not load (bot wall, blank, error page), say so in one line and move on. **Never invent** what you
cannot see in the screenshots.

## Output
- `findings/<group>.json`: an array of finding objects (fields above) plus `site_notes` (object keyed by site).
- `findings/<group>.md`: the same, readable, sorted by rarity × fit_professional.
- Your final reply: the five strongest findings (rarity × fit) in two lines each, plus the list of sites that failed.
