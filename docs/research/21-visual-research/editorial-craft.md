# Editorial + craft findings

Group: editorial (magazines, data-journalism, publishers) and craft (product companies known for interface and typographic craft).  
35 findings from 16 sites, sorted by rarity x fit for a professional firm (score = rarity x fit_professional, max 25). Crops are in `crops/`.

**Failed sites:** apartamentomagazine.com - newsletter modal covers every frame after the hero (desktop and phone); the-brandidentity.com - scroll never advanced - all frames show the same hero.  
**Partial captures:** rauno.me - phone capture has a single frame (desktop complete); framer.com - cookie banner overlaps lower-left of most desktop frames (content still readable).

## Ranking

| # | Score | R | Fit | Finding | Site | Role | Build | 3 languages |
|---|---|---|---|---|---|---|---|---|
| 1 | 20 | 5 | 4 | [Glyph navigation with sub-index](#teenage-engineering-1) | teenage.engineering | navigation | css | with care |
| 2 | 20 | 5 | 4 | [Second-script mission block](#teenage-engineering-2) | teenage.engineering | footer | css | yes |
| 3 | 20 | 4 | 5 | [Archive provenance stamp](#theatlantic-1) | theatlantic.com | knowledge | css | yes |
| 4 | 16 | 4 | 4 | [Index as the hero's control](#kinfolk-1) | kinfolk.com | opening | css+small-js | with care |
| 5 | 16 | 4 | 4 | [Two-register headline with a postage-stamp portrait](#kinfolk-2) | kinfolk.com | people | css | no as-is |
| 6 | 16 | 4 | 4 | [FIG-numbered line plates](#linear-1) | linear.app | process | css | yes |
| 7 | 16 | 4 | 4 | [Tick-ruler contents gauge](#press-stripe-2) | press.stripe.com | navigation | css+small-js | yes |
| 8 | 16 | 4 | 4 | [Corner-anchored contact card](#rauno-3) | rauno.me | contact | css | yes |
| 9 | 16 | 4 | 4 | [Multilingual stacked word plate](#vercel-2) | vercel.com | type-system | css | yes |
| 10 | 15 | 5 | 3 | [Book-spine shelf index](#press-stripe-1) | press.stripe.com | knowledge | heavy-js/webgl | with care |
| 11 | 15 | 3 | 5 | [Numbered claim footnotes](#apple-1) | apple.com | type-system | css | yes |
| 12 | 15 | 3 | 5 | [Footnoted two-tone claim](#stripe-2) | stripe.com | type-system | css | yes |
| 13 | 15 | 3 | 5 | [Three-voice editorial type system with column rules](#theatlantic-2) | theatlantic.com | type-system | css | with care |
| 14 | 15 | 3 | 5 | [Case proof as a marginal sidenote](#vercel-1) | vercel.com | proof | css | with care |
| 15 | 12 | 4 | 3 | [Tick strip with a window cursor](#rauno-1) | rauno.me | navigation | css+small-js | yes |
| 16 | 12 | 4 | 3 | [Zig-zag indented statement](#rauno-2) | rauno.me | type-system | css | with care |
| 17 | 12 | 4 | 3 | [Rolling live figure in the eyebrow](#stripe-1) | stripe.com | opening | css+small-js | yes |
| 18 | 12 | 4 | 3 | [Version table beside a title](#teenage-engineering-3) | teenage.engineering | data-presentation | css | yes |
| 19 | 12 | 4 | 3 | [Odometer tile counter](#theatlantic-3) | theatlantic.com | data-presentation | css | yes |
| 20 | 12 | 3 | 4 | [Freshness stamp and ageing dates](#itsnicethat-2) | itsnicethat.com | knowledge | css+small-js | with care |
| 21 | 12 | 3 | 4 | [Issue-numbered caption trio](#kinfolk-4) | kinfolk.com | knowledge | css | with care |
| 22 | 12 | 3 | 4 | [Chapter-end feature index](#linear-2) | linear.app | services | css | yes |
| 23 | 12 | 3 | 4 | [Serial number + dateline header row](#pudding-1) | pudding.cool | knowledge | css | yes |
| 24 | 12 | 3 | 4 | [Spotlit stat rule](#stripe-3) | stripe.com | proof | css | yes |
| 25 | 12 | 3 | 4 | [Exposed page-frame hairlines](#stripe-4) | stripe.com | grid-system | css | yes |
| 26 | 12 | 3 | 4 | [Age-graded timestamps](#theatlantic-4) | theatlantic.com | knowledge | css+small-js | yes |
| 27 | 9 | 3 | 3 | [Colour-keyed chapter with demo chip](#family-1) | family.co | services | css | yes |
| 28 | 9 | 3 | 3 | [Threshold readout bars](#framer-1) | framer.com | data-presentation | css | yes |
| 29 | 9 | 3 | 3 | [Sub-brand strip above the masthead](#itsnicethat-1) | itsnicethat.com | navigation | css | with care |
| 30 | 9 | 3 | 3 | [Edge-to-edge caps title on the photograph's foot](#kinfolk-3) | kinfolk.com | opening | css | with care |
| 31 | 9 | 3 | 3 | [Matted live-screenshot thumbnails](#pudding-2) | pudding.cool | knowledge | css | yes |
| 32 | 9 | 3 | 3 | [Corner micro-labels on product photography](#teenage-engineering-4) | teenage.engineering | other | css | yes |
| 33 | 8 | 4 | 2 | [Stamp-edged sticky band](#arc-1) | arc.net | other | css | yes |
| 34 | 8 | 4 | 2 | [Margin squiggle cue](#arc-2) | arc.net | navigation | css | with care |
| 35 | 8 | 2 | 4 | [Sans headline, serif standfirst, side by side](#itsnicethat-3) | itsnicethat.com | type-system | css | with care |

## Findings

<a id="teenage-engineering-1"></a>
### Glyph navigation with sub-index - teenage.engineering

`teenage-engineering-1` · score 20 (rarity 5 × fit 4) · role: navigation

![Glyph navigation with sub-index](crops/teenage-engineering-1.jpg)

- **What:** The header is a row of four items, each = a black pictogram (~44px: clover for products, bag for store, empty square for latest, tool cluster for finder) + a lowercase light label (~20px) + directly beneath the label a 3-line tiny sub-index (~10px lowercase) of what is inside ('instruments / audio / designs'; 'visit store / cart & checkout / deals'; 'newsletter / instagram / now'; 'guides & downloads / support / search'). The wordmark 'teenage engineering' sits far-left as two lowercase lines; the logo glyph far-right.
- **Evidence:** `shots/teenage.engineering/desktop-00.jpg` crop `[0, 0, 1440, 120]`
- **Why valuable:** The navigation is a printed directory - scope visible without hovering, no dropdowns; the pictograms make it an identity system, not a menu.
- **Buildable:** css + needs-bespoke-assets (pictogram set). No JS.
- **Three languages:** with care - lowercase is a Latin device; for Thai/Chinese keep the size contrast only; Thai sub-index lines are longer.

<a id="teenage-engineering-2"></a>
### Second-script mission block - teenage.engineering

`teenage-engineering-2` · score 20 (rarity 5 × fit 4) · role: footer

![Second-script mission block](crops/teenage-engineering-2.jpg)

- **What:** A narrow block of Japanese text - the company's mission statement - set solid at ~13px with tight leading, used as a permanent typographic element among Latin items: on desktop inside the header between 'finder' and the logo (~90px wide); on phone in the footer between the copyright (left) and the Stockholm address (right), all three columns top-aligned, same light grey on near-black. It is not a language switch.
- **Evidence:** `shots/teenage.engineering/phone-03.jpg` crop `[0, 990, 780, 270]`; also: desktop-00.jpg (same block in the header)
- **Why valuable:** A second script used as texture and as a statement of heritage and reach - cosmopolitan, extremely rare on Western sites.
- **Buildable:** css. No JS.
- **Three languages:** yes - made for CJK; a Thai mission block on the English site (and English on the Thai site) works the same way.

<a id="theatlantic-1"></a>
### Archive provenance stamp - theatlantic.com

`theatlantic-1` · score 20 (rarity 4 × fit 5) · role: knowledge

![Archive provenance stamp](crops/theatlantic-1.jpg)

- **What:** Older pieces resurfaced on the home page end their dek with the original year in italic parentheses - '“We need to catch up soon!” (From 2015)', '...possibility of redemption (From 2025)', '(From 2018)' - same serif and colour as the dek (AGaramond ~15px), no badge, followed by the byline in mono caps. Used inside the 'RECOMMENDED FOR YOU' and 'ARCHIVE' sections.
- **Evidence:** `shots/theatlantic.com/desktop-03.jpg` crop `[70, 120, 1300, 600]`
- **Why valuable:** Radical honesty about age: telling the reader a piece is old raises its authority (it has lasted) and reads like a bibliographic citation.
- **Buildable:** css (CMS field 'first published'; render '(From YYYY)' when older than N months). No JS.
- **Three languages:** yes - drop the italic in Thai/Chinese and keep the parentheses: (เผยแพร่ครั้งแรก 2562) / (首发于2019年); pairs well with a 'reviewed 2026' note.

<a id="kinfolk-1"></a>
### Index as the hero's control - kinfolk.com

`kinfolk-1` · score 16 (rarity 4 × fit 4) · role: opening

![Index as the hero's control](crops/kinfolk-1.jpg)

- **What:** Full-bleed hero photograph; in its lower-right third a two-column table of contents overlaid in white serif (~13px): heading 'LATEST STORIES' in caps, left column = section ('Fashion', 'Interiors', 'Music', 'Arts & Culture'...), right column = story title ('The Flow State', 'Home Tour: Sphinx Hill'...). The active row is 100% white with a small bullet hanging in the left margin; the other 7 rows sit at ~35% opacity. The image and the large caption at lower-left ('THE FLOW STATE / Mind. Body. Clothes: ...') belong to the active row - the list replaces carousel dots and arrows. On phone it collapses to 'LATEST STORIES / Fashion' plus a small circular progress control.
- **Evidence:** `shots/kinfolk.com/desktop-01.jpg` crop `[980, 520, 460, 260]`
- **Why valuable:** The carousel's controls are the content: the reader sees all eight entries and their categories at once - a contents page printed on the photograph.
- **Buildable:** css+small-js (rows are links; JS swaps image/caption and auto-advances). Without JS: first image + the index as a plain link list.
- **Three languages:** with care - two columns work for Thai/Chinese titles; 35%-opacity rows need a scrim behind them to keep contrast on any photo.

<a id="kinfolk-2"></a>
### Two-register headline with a postage-stamp portrait - kinfolk.com

`kinfolk-2` · score 16 (rarity 4 × fit 4) · role: people

![Two-register headline with a postage-stamp portrait](crops/kinfolk-2.jpg)

- **What:** Centred headline in a display serif (~60px, line-height ~1.05): line 1 is the kicker in caps ('A HELTER-SKELTER WORLD'), line 2 the sentence-case statement ('The artist Carsten Höller wants to play.') at the SAME size - only the case change separates them. ~70px below, a tiny portrait (~212x286px, ~15% of viewport width) centred, then a 13px sans caption 'Arts & Culture, Issue 61'. ~200px of white space around the group.
- **Evidence:** `shots/kinfolk.com/desktop-03.jpg` crop `[180, 40, 1080, 560]`
- **Why valuable:** Inverts the big-image/small-text habit: type carries the authority, the photo becomes an exhibit; restraint and white space signal confidence.
- **Buildable:** css. No JS.
- **Three languages:** no as-is - Thai and Chinese have no case; substitute a weight or colour change for line 1 (or keep Latin caps only on the English site).

<a id="linear-1"></a>
### FIG-numbered line plates - linear.app

`linear-1` · score 16 (rarity 4 × fit 4) · role: process

![FIG-numbered line plates](crops/linear-1.jpg)

- **What:** A three-column band on near-black (#08090A); columns separated by full-height 1px vertical hairlines (~8% white). Each cell: top-left label 'FIG 0.1' / 'FIG 0.2' / 'FIG 0.3' in ~10px mono (Berkeley Mono) at ~25% opacity; centred, a monochrome isometric line drawing (1px strokes, no fills, ~240px wide); bottom-left a ~13px title ('Purpose-built') and a 2-line grey description.
- **Evidence:** `shots/linear.app/desktop-02.jpg` crop `[0, 60, 1440, 500]`
- **Why valuable:** Borrows the figure numbering of technical manuals and patents - authority through documentation; the drawings look drafted, not decorated.
- **Buildable:** css + needs-bespoke-assets (simple isometric SVG line drawings). No JS.
- **Three languages:** yes - localise the label (รูปที่ 1.1 / 图 1.1); mono is optional.

<a id="press-stripe-2"></a>
### Tick-ruler contents gauge - press.stripe.com

`press-stripe-2` · score 16 (rarity 4 × fit 4) · role: navigation

![Tick-ruler contents gauge](crops/press-stripe-2.jpg)

- **What:** A fixed vertical ruler at the left edge (x=28px, vertically centred): 20 ticks, each 16x2px at a 13px pitch, mid-grey (~#777) on the dark ground - one tick per catalogue item, no labels. The tick of the item in view turns pure white; it visibly moves down the ruler across frames 01->02->03->04. The ruler ends with two tiny glyphs (a play triangle = the film, a broadcast icon = the podcast) marking the non-book entries. Only other chrome: logo top-left, a '?' glyph bottom-left.
- **Evidence:** `shots/press.stripe.com/desktop-02.jpg` crop `[0, 300, 140, 340]`
- **Why valuable:** A table of contents reduced to a measuring instrument - silent, exact, an honest count of the collection; it reads like a gauge, not 'UI'.
- **Buildable:** css+small-js (IntersectionObserver sets .is-current). Without JS: ticks are plain anchor links in a fixed nav, no live highlight.
- **Three languages:** yes - no text; give each tick an aria-label/tooltip in the page language.

<a id="rauno-3"></a>
### Corner-anchored contact card - rauno.me

`rauno-3` · score 16 (rarity 4 × fit 4) · role: contact

![Corner-anchored contact card](crops/rauno-3.jpg)

- **What:** A white card (~360x215px at 1440) whose five items sit on the four corners and the centre: 'Twitter' top-left, '2023' top-right, 'Email' centred, '2022' bottom-left, 'GitHub' bottom-right - all one size (~26px regular grotesque), no icons, no labels, no inner rules, on a light-grey ground. It is the last card of the horizontal slide row.
- **Evidence:** `shots/rauno.me/desktop-05.jpg` crop `[310, 220, 760, 460]`
- **Why valuable:** Corner tension makes a calm, poster-like composition out of five words; contact data treated as typography.
- **Buildable:** css (3x3 grid, items placed at corners/centre). No JS.
- **Three languages:** yes - short words; step the size down slightly for Thai labels.

<a id="vercel-2"></a>
### Multilingual stacked word plate - vercel.com

`vercel-2` · score 16 (rarity 4 × fit 4) · role: type-system

![Multilingual stacked word plate](crops/vercel-2.jpg)

- **What:** A black rounded panel styled like a passport cover: at top, two mono-caps columns (~13px Geist Mono) - 'VERCEL' left, and right the same word stacked in four languages 'PASSPORT / PASAPORTE / PASSAPORTO / パスポート' at equal line spacing; the brand triangle centred near the bottom.
- **Evidence:** `shots/vercel.com/desktop-04.jpg` crop `[720, 200, 720, 320]`
- **Why valuable:** Shows international reach through typography alone and reads like an official document - apt for identity and credentials.
- **Buildable:** css. No JS.
- **Three languages:** yes - this IS a multi-script device: 'AUDIT / ตรวจสอบบัญชี / 审计'; needs fonts with matched x-height/cap height across Latin, Thai and Chinese.

<a id="press-stripe-1"></a>
### Book-spine shelf index - press.stripe.com

`press-stripe-1` · score 15 (rarity 5 × fit 3) · role: knowledge

![Book-spine shelf index](crops/press-stripe-1.jpg)

- **What:** The home page IS the catalogue: a single centred column (~720px of 1440, i.e. 50%) of real 3D book boxes seen spine-on, spines ~60-90px tall with ~35px gaps on a near-black aubergine ground (#201819). Every spine uses three fixed slots - author flush-left (~35px inset), title centred, publisher mark flush-right - but each in that book's own typeface, colour and material (marbled paper, cloth, foil, pixel art), so the list is orderly yet every row is unique. Rendered in WebGL: across frames 00->03 the camera angle changes with scroll (first looking down onto the cover art, later showing the box undersides). The stack continues past the books into other object types (a film poster box, a red podcast 'button'). On phone the boxes are enlarged so spines crop at both viewport edges.
- **Evidence:** `shots/press.stripe.com/desktop-02.jpg` crop `[340, 0, 760, 900]`
- **Why valuable:** The list is the product - material honesty; each item visibly unique while the three-slot spine grid keeps discipline; enormous visible effort.
- **Buildable:** heavy-js/webgl (3D) + needs-bespoke-assets (cover art per item). Degrades cleanly to CSS: flat stacked spine bars (author | title | mark), fully readable without JS.
- **Three languages:** with care - horizontal spine text works for Thai and Chinese; spine height must clear Thai ascenders/descenders; Chinese titles could run vertically (writing-mode) like real CJK spines.

<a id="apple-1"></a>
### Numbered claim footnotes - apple.com

`apple-1` · score 15 (rarity 3 × fit 5) · role: type-system

![Numbered claim footnotes](crops/apple-1.jpg)

- **What:** Marketing claims carry superscript numerals inline ('The most accurate heart rate sensing in a wearable.¹', 'Love it. Lease it. Upgrade it.²'); above the footer a light-grey band holds the notes as a numbered list (12px grey, ~1.5 line-height, hanging numbers, ~1100px measure), then unnumbered disclosure paragraphs, a 1px rule, and the sitemap.
- **Evidence:** `shots/apple.com/desktop-05.jpg` crop `[200, 380, 1100, 420]`; also: desktop-02.jpg, desktop-03.jpg (superscripts in claims)
- **Why valuable:** Qualifying claims is what serious institutions do; a visible fine-print system makes bold claims credible.
- **Buildable:** css (ol + sup anchors with back-links). No JS.
- **Three languages:** yes - numerals universal; Thai footnotes need >=13px in a legible text face.

<a id="stripe-2"></a>
### Footnoted two-tone claim - stripe.com

`stripe-2` · score 15 (rarity 3 × fit 5) · role: type-system

![Footnoted two-tone claim](crops/stripe-2.jpg)

- **What:** The hero statement is ONE paragraph at ~48px light (sohne-var weight 300): sentence 1 in near-black navy, the continuation in slate grey-blue - same size and weight; the colour change replaces the headline/subhead stack. A superscript footnote numeral sits inside the headline itself ('business banking,¹ and...') pointing to small print further down. The same run-in pattern opens later sections ('Flexible solutions for every business model. Grow your...').
- **Evidence:** `shots/stripe.com/desktop-00.jpg` crop `[190, 250, 1050, 230]`
- **Why valuable:** A footnote in the biggest line on the page signals a regulated, careful institution confident enough to qualify its claims.
- **Buildable:** css. No JS.
- **Three languages:** yes - the colour change works in every script; superscript numerals are fine; Thai needs a shorter measure (~26 graphemes vs ~32ch Latin).

<a id="theatlantic-2"></a>
### Three-voice editorial type system with column rules - theatlantic.com

`theatlantic-2` · score 15 (rarity 3 × fit 5) · role: type-system

![Three-voice editorial type system with column rules](crops/theatlantic-2.jpg)

- **What:** Three families with fixed jobs: (a) Garamond serif for headlines (~22-28px) and deks (~15px); (b) a monospace in small tracked caps (~10-11px) for bylines ('ALAN EYRE') and meta; (c) the same mono in lower case, ~9px grey, for the credit line set flush-left directly under every image ('Illustration by The Atlantic. Source: Getty.'). Section heads: condensed serif caps (~22px) over a full-width ~1.5px black rule with a mono 'See All' at right. Columns are divided by 1px vertical hairlines (lead story | right rail; Recommended | Archive). Series kicker 'RADIO ATLANTIC • EPISODE 220' = sans caps + red mono number. The Popular list hangs red oldstyle serif numerals (2, 3, 4, 5) outside the headline column with hairlines between items. Red is reserved for the A mark, Subscribe, episode numbers and ranks.
- **Evidence:** `shots/theatlantic.com/desktop-00.jpg` crop `[60, 230, 1320, 660]`; also: desktop-03.jpg (section heads, column rule); desktop-04.jpg (red hanging numerals, episode kicker)
- **Why valuable:** Each voice signals a different kind of information (claim / person / source); credits under every image are a visible mark of rigour; column rules evoke the printed paper.
- **Buildable:** css. No JS.
- **Three languages:** with care - mono caps bylines are Latin-only; Thai/Chinese need a small tabular/mono-like substitute without caps or tracking; credit lines work in every script.

<a id="vercel-1"></a>
### Case proof as a marginal sidenote - vercel.com

`vercel-1` · score 15 (rarity 3 × fit 5) · role: proof

![Case proof as a marginal sidenote](crops/vercel-1.jpg)

- **What:** Each section is a triad across 1440: headline top-left (~32px, 2 lines), the client's artefact (screenshot) in the middle ~45%, and in the outer margin column (~14% width) a sidenote: the proof sentence ~15px with the first clause black and the rest grey ('Notion powers millions | of agent conversations daily on Vercel.'), then an 11px grey label 'Features' and a 4-item plain list of what the client used. The sidenote alternates sides per case (Zapier left margin, Mintlify right margin).
- **Evidence:** `shots/vercel.com/desktop-01.jpg` crop `[0, 150, 1440, 600]`; also: desktop-02.jpg, desktop-03.jpg (alternating sides)
- **Why valuable:** Proof presented like a scholarly marginal note - understated, factual, attached to evidence - instead of a testimonial card.
- **Buildable:** css (grid with a margin column; alternate with :nth-child). No JS.
- **Three languages:** with care - the ~200px margin column gets tall in Thai; give it >=240px or move it under the artefact on narrow screens.

<a id="rauno-1"></a>
### Tick strip with a window cursor - rauno.me

`rauno-1` · score 12 (rarity 4 × fit 3) · role: navigation

![Tick strip with a window cursor](crops/rauno-1.jpg)

- **What:** A small horizontal strip at top-centre (~100px wide): ~15 thin 1px vertical ticks (~12px tall) in mid-grey; the current position is an outlined 1px rectangle (~16x10px) that replaces one tick and slides along the strip as the horizontal sequence of slides advances (it moves left->right across frames 00->06).
- **Evidence:** `shots/rauno.me/desktop-02.jpg` crop `[560, 40, 320, 60]`
- **Why valuable:** A scrollbar redrawn as a measuring instrument - minimal, exact, honest about length.
- **Buildable:** css+small-js (position from scroll progress). Without JS hide it.
- **Three languages:** yes - no text.

<a id="rauno-2"></a>
### Zig-zag indented statement - rauno.me

`rauno-2` · score 12 (rarity 4 × fit 3) · role: type-system

![Zig-zag indented statement](crops/rauno-2.jpg)

- **What:** The intro sentence is set large (~38px grotesque, leading ~1.2) with alternating line indents: odd lines flush-left, even lines indented ~28px ('Rauno Freiberg / __is an Estonian / interaction / __designer / working with Vercel / __and Devouring Details'), with hand-set line breaks; the text overlaps a flat yellow disc (no transparency effects), and a 1px crosshair '+' marks the viewport centre.
- **Evidence:** `shots/rauno.me/desktop-00.jpg` crop `[180, 120, 1100, 660]`
- **Why valuable:** A typographer's hand-set rhythm that default text flow can never produce - proof that someone weighed every line break.
- **Buildable:** css (each line a span; even lines padding-left). No JS.
- **Three languages:** with care - Thai and Chinese have no word spaces; breaks must be set by hand per language (fine for one statement).

<a id="stripe-1"></a>
### Rolling live figure in the eyebrow - stripe.com

`stripe-1` · score 12 (rarity 4 × fit 3) · role: opening

![Rolling live figure in the eyebrow](crops/stripe-1.jpg)

- **What:** Above the hero headline, a ~13px eyebrow 'Global GDP running on Stripe:' in dark followed by a grey figure with 7-8 decimals ('1.7278069_%') whose last digit is caught mid-roll (odometer-style: the next digit is visibly sliding in vertically). The figure ticks continuously; it is small and grey, not a big stat.
- **Evidence:** `shots/stripe.com/desktop-00.jpg` crop `[200, 190, 300, 40]`
- **Why valuable:** A live, over-precise number whispers proof of scale and of a working system - more credible than a big rounded stat.
- **Buildable:** css+small-js (digit columns translated with tabular numerals). Without JS shows the static figure.
- **Three languages:** yes - digits universal; only the label localises. Needs a genuine live quantity (e.g. countdown to the next filing deadline).

<a id="teenage-engineering-3"></a>
### Version table beside a title - teenage.engineering

`teenage-engineering-3` · score 12 (rarity 4 × fit 3) · role: data-presentation

![Version table beside a title](crops/teenage-engineering-3.jpg)

- **What:** Title lockup 'DAILY LIFE OF MR. UPDATE' in heavy condensed caps; to its right a tear-off-calendar pictogram ('EP SERIES / UPDATE') and under it a 3-row mini table: model codes left ('EP-133', 'EP-40', 'EP-1320') in black, version numbers right-aligned in orange ('2.5', '2.5', '1.6'), hairlines between rows.
- **Evidence:** `shots/teenage.engineering/desktop-00.jpg` crop `[1032, 180, 190, 280]`
- **Why valuable:** A changelog compressed into a typographic label - exact version numbers become ornament and proof at once.
- **Buildable:** css (+ bespoke pictogram optional). No JS.
- **Three languages:** yes - codes and numbers; Thai row labels longer.

<a id="theatlantic-3"></a>
### Odometer tile counter - theatlantic.com

`theatlantic-3` · score 12 (rarity 4 × fit 3) · role: data-presentation

![Odometer tile counter](crops/theatlantic-3.jpg)

- **What:** Promo panel: condensed serif caps title 'AI WATCHDOG', below a 9-digit figure with leading zeros '000,023,910' where each digit sits in its own slightly lighter tile (~26x40px, 2px gaps) and the commas stand outside the tiles; caption 'WORKS TAKEN' in mono caps under it; then a centred serif paragraph and a mono-labelled button.
- **Evidence:** `shots/theatlantic.com/desktop-04.jpg` crop `[1040, 440, 340, 460]`
- **Why valuable:** Mechanical-counter metaphor - the number feels measured and audited rather than rounded marketing; leading zeros signal capacity and a counter still running.
- **Buildable:** css (tabular numerals, one span per digit); css+small-js if it counts up. Static without JS.
- **Three languages:** yes - Arabic numerals in all three languages; only the caption localises. Use only for real, verifiable figures.

<a id="itsnicethat-2"></a>
### Freshness stamp and ageing dates - itsnicethat.com

`itsnicethat-2` · score 12 (rarity 3 × fit 4) · role: knowledge

![Freshness stamp and ageing dates](crops/itsnicethat-2.jpg)

- **What:** Under the masthead, a full-width light-grey bar (~#F2F2F2, ~48px) reads 'The Nice Feed' (dark) + 'Refreshed 5h ago' (grey) at left and 'Explore All' with a small filled-square arrow at right. Card dates are relative while recent ('12 hours ago', 'A day ago', '7 days ago') and switch to absolute dates once older ('16 September 2026', seen in desktop-06), ~11px grey directly under each headline.
- **Evidence:** `shots/itsnicethat.com/desktop-00.jpg` crop `[180, 150, 1080, 60]`; also: desktop-06.jpg (absolute dates on older cards)
- **Why valuable:** Tells the reader the site is actively maintained - freshness is proof of diligence; flipping to absolute dates keeps old items honest.
- **Buildable:** css+small-js (relative time computed client-side; the static HTML carries the absolute date as fallback).
- **Three languages:** with care - relative phrases must be localised (2 ชั่วโมงที่แล้ว / 2小时前); Intl.RelativeTimeFormat covers all three (outside the pure engine).

<a id="kinfolk-4"></a>
### Issue-numbered caption trio - kinfolk.com

`kinfolk-4` · score 12 (rarity 3 × fit 4) · role: knowledge

![Issue-numbered caption trio](crops/kinfolk-4.jpg)

- **What:** Section header 'Inside Issue Sixty-One' (serif ~20px, the number spelled out) over a full-width 1px black rule, with 'View All' ~11px at right. Below, a horizontally scrolling row of portrait images (~150x200px at 1440, 8px gutters, last image cut by the edge). Each caption has three tiers: 9px sans 'Arts & Culture, Issue 61' / 10px sans caps title 'SUIT YOURSELF' / 10px sans sentence dek.
- **Evidence:** `shots/kinfolk.com/desktop-02.jpg` crop `[0, 100, 1440, 680]`
- **Why valuable:** Issue numbering and spelled-out numbers give a periodical voice; the three-tier caption is a disciplined small-type system.
- **Buildable:** css (overflow-x + scroll-snap). No JS.
- **Three languages:** with care - the caps tier needs a weight substitute in Thai/Chinese; spelled-out numbers have natural forms (ฉบับที่หกสิบเอ็ด / 第六十一期).

<a id="linear-2"></a>
### Chapter-end feature index - linear.app

`linear-2` · score 12 (rarity 3 × fit 4) · role: services

![Chapter-end feature index](crops/linear-2.jpg)

- **What:** At the end of each product chapter: a grey label 'Features' in the far-left column; the sub-feature links in two short columns starting right of centre, each followed by a small '+' glyph; the two columns separated by a 1px vertical hairline; generous space above and a full-width hairline after.
- **Evidence:** `shots/linear.app/desktop-05.jpg` crop `[0, 250, 1440, 200]`
- **Why valuable:** Like a 'see also' index at the end of a book chapter - shows depth without cards; the '+' promises more without shouting.
- **Buildable:** css. No JS.
- **Three languages:** yes - short labels; Thai entries are longer, let the columns wrap.

<a id="pudding-1"></a>
### Serial number + dateline header row - pudding.cool

`pudding-1` · score 12 (rarity 3 × fit 4) · role: knowledge

![Serial number + dateline header row](crops/pudding-1.jpg)

- **What:** Every story tile is topped by a one-line row: left, an outlined pill (1px #262626, fully rounded, ~44x20px) holding the serial '#225' in small mono; right, month + year in typewriter caps 'OCT 2026' (Atlas Typewriter ~12px, slight tracking) flush to the tile edge. Below: image, then a heavy semi-condensed serif title set all lowercase ('mowing experiment'), then one grey sans sentence. Serials descend continuously through the archive (#225 ... #199), so the index doubles as a publication count.
- **Evidence:** `shots/pudding.cool/desktop-00.jpg` crop `[80, 260, 880, 140]`
- **Why valuable:** Serial numbering turns a blog into a numbered series - continuity, editorial accountability, visible volume; the typewriter dateline reads like a filing stamp.
- **Buildable:** css (serial from CMS order). No JS needed.
- **Three languages:** yes - numerals are universal; month must be localised (ต.ค. 2569 with a Buddhist-era option for Thai, 2026年10月 for Chinese); caps only apply to the Latin version.

<a id="stripe-3"></a>
### Spotlit stat rule - stripe.com

`stripe-3` · score 12 (rarity 3 × fit 4) · role: proof

![Spotlit stat rule](crops/stripe-3.jpg)

- **What:** Four stats in a row inside a frame of 1px hairlines (top and bottom, full container width): large light numerals (~34px, weight 300: '135+', '$1.9T', '99.999%', '200M+') over 2-line ~12px centred captions. One stat is 'lit' at a time - numeral and caption go dark navy while the others stay slate - and a short darker gradient segment appears on the top and bottom hairlines exactly above/below that cell (a travelling highlight on the rule).
- **Evidence:** `shots/stripe.com/desktop-04.jpg` crop `[80, 180, 1280, 200]`
- **Why valuable:** Directs attention without counting-up gimmicks; the rule itself becomes the indicator - quiet and precise.
- **Buildable:** css (staggered keyframes, no JS needed) or css+small-js; without animation all four sit equal.
- **Three languages:** yes - numerals; Thai captions run longer, allow 3 lines.

<a id="stripe-4"></a>
### Exposed page-frame hairlines - stripe.com

`stripe-4` · score 12 (rarity 3 × fit 4) · role: grid-system

![Exposed page-frame hairlines](crops/stripe-4.jpg)

- **What:** The content container is drawn: 1px light-grey vertical lines run the full page height at the container edges (x~88 and x~1352 at 1440) and 1px horizontal lines span between them at section boundaries; inside sections, dashed 1px rules separate accordion rows (client stories with a square '+' button at right). Copy blocks use bold run-in leads ('Professional services. Get tailored guidance...') instead of separate headings; case metadata reads as bold figure + grey label ('160 countries', '11K+ locations').
- **Evidence:** `shots/stripe.com/desktop-06.jpg` crop `[0, 160, 1440, 740]`; also: desktop-00.jpg, desktop-04.jpg (same frame lines)
- **Why valuable:** Makes the grid visible like ledger ruling or a blueprint - engineering-grade order at almost no cost, and rare.
- **Buildable:** css (borders on the wrapper and section elements). No JS.
- **Three languages:** yes - script-independent; bold run-in leads need a real bold weight in the Thai/Chinese fonts.

<a id="theatlantic-4"></a>
### Age-graded timestamps - theatlantic.com

`theatlantic-4` · score 12 (rarity 3 × fit 4) · role: knowledge

![Age-graded timestamps](crops/theatlantic-4.jpg)

- **What:** In the Latest list the meta line under each byline (~9px mono caps, grey) shows clock time for today's items ('9:00 AM ET', '7:00 AM ET', '12:59 PM ET') and switches to full dates for older ones ('OCTOBER 5, 2026'). Rows: thumbnail left (~140x90px), serif headline ~20px, byline, time; 1px hairlines between rows.
- **Evidence:** `shots/theatlantic.com/desktop-05.jpg` crop `[400, 80, 640, 820]`
- **Why valuable:** A newsroom habit: precision about when builds trust, and the granularity itself tells you how fresh an item is.
- **Buildable:** css+small-js (or resolved at build time). No JS fallback: always the date.
- **Three languages:** yes - local formats (14:30 น. / 14:30), no caps or tracking in Thai/Chinese.

<a id="family-1"></a>
### Colour-keyed chapter with demo chip - family.co

`family-1` · score 9 (rarity 3 × fit 3) · role: services

![Colour-keyed chapter with demo chip](crops/family-1.jpg)

- **What:** Each feature chapter owns one hue: a ~12px eyebrow word in that hue ('Simple' green, 'Understandable' orange, 'Secure' blue, 'Seamless' amber), a 3-item checklist whose ticks and text share the hue, and at the end a 'demo chip' - a ~58x34px video thumbnail followed by a 2-line label ('Watching Wallets' / 'Watch the demo' in grey). Headline ~36px black, 2 lines.
- **Evidence:** `shots/family.co/desktop-04.jpg` crop `[180, 140, 560, 500]`
- **Why valuable:** Colour as wayfinding inside a long page; the demo chip offers proof at the moment of the claim, far smaller than an embedded video.
- **Buildable:** css + needs-bespoke-assets (short demo videos/thumbnails). No JS for the chip itself.
- **Three languages:** yes - colour and thumbnail are script-free; Thai labels run longer.

<a id="framer-1"></a>
### Threshold readout bars - framer.com

`framer-1` · score 9 (rarity 3 × fit 3) · role: data-presentation

![Threshold readout bars](crops/framer-1.jpg)

- **What:** A small panel 'Core Web Vitals' with an outlined green 'GOOD' badge top-right; each metric row: grey label + info glyph at left ('LCP'), value right-aligned in blue ('1.1s'), beneath it a 4px full-width dark track with a short blue fill and a 1px vertical tick marking the threshold near the right end.
- **Evidence:** `shots/framer.com/desktop-05.jpg` crop `[150, 240, 340, 260]`
- **Why valuable:** Value + threshold + verdict in one line - a dashboard grammar that reads as measured fact.
- **Buildable:** css. No JS.
- **Three languages:** yes - numbers and short labels.

<a id="itsnicethat-1"></a>
### Sub-brand strip above the masthead - itsnicethat.com

`itsnicethat-1` · score 9 (rarity 3 × fit 3) · role: navigation

![Sub-brand strip above the masthead](crops/itsnicethat-1.jpg)

- **What:** A ~60px cream band above the main masthead, split into 4 equal cells by 1px vertical hairlines. Each cell: a sub-brand wordmark in its own typeface (serif 'insights', stacked black 'ONES TO WATCH', condensed italic 'NICER TUESDAYS', script 'If You Could') over a one-line ~11px sans descriptor ('Visual Research Department', 'New Talent Showcase', 'Events', 'Creative Jobs Board'). Below: centred wordmark with the tagline 'Inspiring Creativity Since 2007'.
- **Evidence:** `shots/itsnicethat.com/desktop-00.jpg` crop `[0, 0, 1440, 140]`
- **Why valuable:** Presents the house as a family of named departments - institutional depth and scale before the first headline.
- **Buildable:** css. No JS.
- **Three languages:** with care - for a sober firm use one typeface for all cells (names differ, not fonts); Thai descriptors run ~30% longer, allow 2 lines.

<a id="kinfolk-3"></a>
### Edge-to-edge caps title on the photograph's foot - kinfolk.com

`kinfolk-3` · score 9 (rarity 3 × fit 3) · role: opening

![Edge-to-edge caps title on the photograph's foot](crops/kinfolk-3.jpg)

- **What:** Feature opener: full-bleed photo; the title in white display-serif caps sized so one line spans the full viewport minus ~34px margins ('TAKING PLAY SERIOUSLY', ~90px cap height at 1440), baseline ~40px above the image's bottom edge; the dek in small white serif at top-left. Frames 06->07: the image scrolls in from below with the title first cropped by the viewport, then fully in view - the title is anchored to the image foot, not centred in the viewport.
- **Evidence:** `shots/kinfolk.com/desktop-07.jpg` crop `[0, 0, 1440, 840]`
- **Why valuable:** Fitting a title to the full measure is a print-cover move; anchoring it to the image foot gives cinema-title gravity.
- **Buildable:** css (font-size in vw/clamp tuned per title) or small JS fit-text; without JS a fixed vw size works.
- **Three languages:** with care - caps device is Latin-only; fit-to-width itself works for Thai/Chinese but needs per-language sizing.

<a id="pudding-2"></a>
### Matted live-screenshot thumbnails - pudding.cool

`pudding-2` · score 9 (rarity 3 × fit 3) · role: knowledge

![Matted live-screenshot thumbnails](crops/pudding-2.jpg)

- **What:** Thumbnails are not photos but screenshots of the actual piece, inset on a flat saturated colour mat (passe-partout): tile ~4:3, the screenshot ~70% of tile width, centred, starting ~10% below the top edge and bleeding off the bottom edge (no bottom margin, no shadow, no rounding). The mat colour changes per story (cyan, butter yellow, lilac, magenta).
- **Evidence:** `shots/pudding.cool/desktop-04.jpg` crop `[80, 220, 1280, 480]`
- **Why valuable:** Shows the real work instead of stock imagery (material honesty); the mat unifies very different screenshots into one consistent set.
- **Buildable:** css + needs-bespoke-assets (a screenshot per report/tool). No JS.
- **Three languages:** yes - image-only; use muted mats (stone, sage, ink) for a professional palette.

<a id="teenage-engineering-4"></a>
### Corner micro-labels on product photography - teenage.engineering

`teenage-engineering-4` · score 9 (rarity 3 × fit 3) · role: other

![Corner micro-labels on product photography](crops/teenage-engineering-4.jpg)

- **What:** Full-bleed, dark-lit product photographs carry only a tiny label at lower-left ('EP-133 K.O. II', 'K.O.-SIDEKICK', 'APC-2'; ~10px light sans, ~28px from the edges) and sometimes a status line top-left ('sinus transmission completed'). Below the photo, a row of equal white cells divided by 1px hairlines, each with the item name + a blue 'buy now' at top-left and the object centred.
- **Evidence:** `shots/teenage.engineering/desktop-05.jpg` crop `[0, 0, 1440, 900]`; also: desktop-02.jpg, desktop-04.jpg, desktop-07.jpg
- **Why valuable:** Labels behave like museum or catalogue plates; the photograph is left untouched - confidence and material honesty.
- **Buildable:** css. No JS.
- **Three languages:** yes - short labels in any script.

<a id="arc-1"></a>
### Stamp-edged sticky band - arc.net

`arc-1` · score 8 (rarity 4 × fit 2) · role: other

![Stamp-edged sticky band](crops/arc-1.jpg)

- **What:** Under the nav, a ~60px band with scalloped postage-stamp edges top and bottom (semicircle teeth ~8px pitch) cut into a pale pastel-gradient strip with a soft shadow below; it stays sticky across the page and holds one serif line ('Meet Dia, the next evolution of Arc') + a dark pill CTA. The page ground is saturated blue with fine grain; press quotes run in a cream strip bounded by wavy 1px lines.
- **Evidence:** `shots/arc.net/desktop-01.jpg` crop `[0, 60, 1440, 160]`
- **Why valuable:** A die-cut edge turns a digital band into a printed ticket/stamp - tactile and memorable.
- **Buildable:** css (mask-image with repeating radial-gradient). No JS.
- **Three languages:** yes - shape only.

<a id="arc-2"></a>
### Margin squiggle cue - arc.net

`arc-2` · score 8 (rarity 4 × fit 2) · role: navigation

![Margin squiggle cue](crops/arc-2.jpg)

- **What:** At the right margin, mid-height: a 2-line mono caps label 'MORE / DETAILS' (~11px, wide tracking, white) above a hand-drawn squiggly vertical arrow (~80px tall, ~1.5px white stroke) pointing down.
- **Evidence:** `shots/arc.net/desktop-01.jpg` crop `[1302, 510, 138, 200]`
- **Why valuable:** Handwriting in the margin reads as a person annotating the page - replaces the generic scroll chevron.
- **Buildable:** css + needs-bespoke-assets (one SVG squiggle). No JS.
- **Three languages:** with care - caps/tracking are Latin-only; the arrow is universal.

<a id="itsnicethat-3"></a>
### Sans headline, serif standfirst, side by side - itsnicethat.com

`itsnicethat-3` · score 8 (rarity 2 × fit 4) · role: type-system

![Sans headline, serif standfirst, side by side](crops/itsnicethat-3.jpg)

- **What:** Feature block under the lead image: headline in a light grotesque (Labil, ~34px, regular, 4 lines) in the left ~55%; the standfirst in a book serif (Bradford, ~15px, oldstyle figures - '25 years') in a right column top-aligned with the headline; beneath it a tiny grey relative date and pale-lavender tag chips. Inverts the usual serif-headline / sans-body pairing.
- **Evidence:** `shots/itsnicethat.com/desktop-01.jpg` crop `[180, 360, 1100, 260]`
- **Why valuable:** Two voices with clear jobs - a cool sans for the claim, a warm book serif for the argument; side-by-side reads like a magazine spread, not a blog stack.
- **Buildable:** css. No JS.
- **Three languages:** with care - needs a Thai/Chinese pairing that keeps the contrast (Thai loopless sans + looped text face; Chinese Hei + Song).

## Site notes

- **press.stripe.com** - Chrome uses one family in three optical sizes (Ivar Display / Headline / Text); the catalogue itself is the type system - every spine brings its own face inside a fixed author | title | mark grid. Dark aubergine ground (#201819) with white; the mission text below switches to white paper, Ivar Text ~16px at a ~480px measure. Footer: hairline, legal small print left, italic right-aligned address. Motion: WebGL camera tilt tied to scroll + the tick ruler highlight.

- **pudding.cool** - Three families with strict roles: Gooper SemiCondensed (heavy serif, all-lowercase titles), Atlas Grotesk (deks), Atlas Typewriter (serials, dates, filter labels in caps). White ground; colour lives only in the thumbnail mats. 3 columns (~395px tiles) at 1440, single column on phone with an 'All' dropdown filter. Category filters are pictogram + mono caps label.

- **itsnicethat.com** - Labil (variable grotesque) for headlines/UI, Bradford (book serif, oldstyle figures) for decks. Masonry of natural-ratio images; each category is a pastel band with white panels of ragged height; floating bottom pill navigation (common). Relative time stamps throughout.

- **kinfolk.com** - Proprietary Kinfolk Serif in Display/Deck/Text plus Kinfolk Sans for captions. Scale roughly 60 / 20 / 13 / 9-10px. Almost everything centred or flush-left on ~34px margins; black, white and photography only; numbers spelled out ('Issue Sixty-One'); sticky black subscription bar at the bottom. GSAP + Lenis smooth scroll (feature openers scroll over full-bleed images).

- **apartamentomagazine.com** - FAILED (modal wall): a newsletter popup covers every frame after the first on desktop and phone. Only the hero is visible (italic serif kicker 'Apartamento magazine issue #37', Futura name, lowercase nav). No findings.

- **the-brandidentity.com** - FAILED (scroll did not advance): all 8 desktop and 6 phone frames show the same hero (serif lowercase client name 'fatty15' over sans caps 'PACKAGING', 'EXPLORE CASE STUDY'). No findings.

- **theatlantic.com** - AGaramond (headlines/deks) + condensed Atlantic Serif caps (section heads) + Graphik (UI) + Logic Monospace (bylines, credits, times). Red reserved for the A mark, Subscribe, episode numbers and ranking numerals. Four-column front page with 1px vertical column rules; masthead (giant red A over italic wordmark) collapses into a sticky bar with a small red A at left. The most complete editorial micro-system in this group.

- **stripe.com** - sohne-var at light weight 300 for display (~48px) with two-tone run-in paragraphs; Source Code Pro for code; light numerals for stats. Exposed container frame lines + dashed row rules. Motion vocabulary: rolling digits, stat spotlight on the rule, WebGL gradient ribbon. Hanging punctuation, text-wrap balance and subgrid present in CSS.

- **linear.app** - Inter Variable (weight ~510) + Berkeley Mono for labels; near-black #08090A with 1px low-contrast hairlines and a fine grain. Repeating chapter pattern: 2-line heading left / paragraph right / product fragments fading into the dark / feature index. Product UI is SaaS-specific; only the documentary devices transfer.

- **vercel.com** - Geist Sans (tight negative tracking at display sizes) + Geist Mono; off-white #FAFAFA, black. Case studies alternate their margin sidenote left/right. Footer is a 6-column directory with small 'New' chips. Hero right column stacks three purpose phrases (mono on phone).

- **rauno.me** - One grotesque at few, large sizes (~38px statement, ~26px card text, ~280px display words cropped by their cards) plus ~9px slide labels above each card. Light-grey ground (#EDEDED), white cards, flat yellow/orange discs. Horizontal slide track with a tick-strip position marker and a crosshair cursor. Phone capture has only one frame.

- **family.co** - Custom 'Family' display face + Inter; one hue per chapter. The famous micro-motion is not legible in stills (only a speed selector changing '~27 Secs' / '~60 Secs'). Otherwise a modern SaaS layout.

- **teenage.engineering** - House faces te-20/te-40; all-lowercase UI; black pictograms as nav; full-bleed product photography on black with plate-like corner labels; hairline-divided product cells; a Japanese text block as a permanent element. Lottie + Splitting in the stack.

- **apple.com** - SF Pro Display/Text; centred name / tagline / two CTAs per tile, tiles with ~12px gutters - familiar. The transferable craft is the footnote system.

- **framer.com** - Generic dark SaaS bento (GT Walsheim + Inter + several monos); a cookie banner covers the lower-left of most frames. One data-presentation detail recorded.

- **arc.net** - Rounded sans (Marlin Soft) for headings, serif for the sticky band, ABC Favorit Mono for labels and outlined handle chips ('@BEEBOMCO'); saturated blue with grain; scalloped and wavy edges as the signature; marquee of press quotes.
