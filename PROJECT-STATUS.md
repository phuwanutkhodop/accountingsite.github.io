# PROJECT-STATUS.md

**Last updated:** Saturday, 25 April 2026
**Last session:** Stage 5 complete — Knowledge index page + AEO/SEO foundations
**Next session:** Stage 6 — Sub-pages (discovery + design + build)

---

## TL;DR — Where the project is right now

The site has a working homepage, a brand-new Insights index page (`knowledge.html`), an article template, and a manifest-driven publishing workflow. Adding a new article is a two-step process: write the article HTML and add ~7 lines to `articles.json`. The homepage Insights preview, the knowledge page grid, and the marquee ticker on knowledge.html all update themselves from that single manifest. SEO/AEO foundations are baked into both the homepage and knowledge.html (full meta tags, Open Graph, Twitter Card, JSON-LD structured data with schema.org `CollectionPage` + `ItemList`). Article cards carry microdata. Five drift bugs caught and fixed during Stage 5 are documented below.

The site is **not yet ready to launch.** Three things are missing: sub-pages (About, Services, Contact, etc. — Stage 6), a sitewide SEO sweep with sitemap and robots.txt (Stage 7), and a customization guide for the user (Stage 8). After those, the user writes the first real article (Stage 9) and prepares for launch (Stage 10).

---

## The 10-stage roadmap

| Stage | What it is | Status |
|---|---|---|
| 1 | Project setup | ✅ Complete |
| 2 | Style system + design tokens | ✅ Complete |
| 3 | Homepage | ✅ Complete |
| 4 | Article template | ✅ Complete |
| 4.5 | Stabilization sweep *(added in-flight)* | ✅ Complete |
| **5** | **Knowledge index page + AEO/SEO foundations** | ✅ **Just completed** |
| 6 | **Sub-pages** (discovery + design + build) *(new)* | 📍 Next |
| 7 | Sitewide SEO/AEO sweep *(renumbered, expanded)* | Pending |
| 8 | Customization Guide & Site Operations Manual *(new)* | Pending |
| 9 | First real article *(renumbered)* | Pending |
| 10 | Launch prep & template hardening *(renumbered)* | Pending |

**Stages added across the project so far:** 4.5 (Stage 4 follow-up), 6 (sub-pages discussion), 8 (customization guide). Each was added when a real need emerged in conversation, not at project start. This responsiveness is a feature, not a problem.

---

## Stage 5 — what was actually built

### New files created

| File | Purpose | Lines |
|---|---|---|
| `/en/knowledge.html` | The Insights index page | 352 |
| `/en/posts/articles.json` | The article manifest (3 placeholders) | ~38 |
| `/en/posts/ARTICLES-README.txt` | Plain-language guide for editing articles.json | ~135 |
| `/core/article-loader.js` | Reads manifest, renders cards, injects JSON-LD, powers search | 628 |

### Files patched

| File | What changed |
|---|---|
| `/en/index.html` | SEO/AEO meta added to head; Insights section converted to auto-loading container; all 17 absolute `/en/` paths converted to relative; stagger drift fixed (`data-animate-delay` → `data-delay`); `data-seo-context="homepage"` added to body; article-loader.js script tag added |
| `/core/animations.js` | Stagger drift fix (now reads `data-delay` canonically, accepts legacy `data-animate-delay` for back-compat); rescan hook added so dynamically-rendered cards still get scroll-reveal |
| `/theme/theme.css` | Section 18 added: knowledge page layout, marquee, search, featured card. Section 19 added: `.section--cta` modifier. 1,728 → 2,164 lines (+436 with comments). 192 brace pairs balanced. |

### Files explicitly NOT touched

| File | Why |
|---|---|
| `/theme/motion.css` | Stage 5 needed nothing here — the marquee animation already existed |
| `/en/posts/article-template.html` | Signed off in Stage 4. Touching working code mid-stage to add small consistency wins violates scope discipline. Migration parked for Stage 10. |

---

## Stage 5 — the architectural decisions made

### 1. Manifest-driven publishing (the headline decision)

The user's hard constraint: "I don't want to update code outside knowledge scope every time I post." Three options were compared (hand-edited, manifest, build-step). Manifest chosen because it's the only approach that gives true zero-code-touching publishing without requiring tooling overhead.

**Workflow now:**
1. Write article HTML in `/en/posts/`
2. Add ~7 lines to `/en/posts/articles.json`
3. Push

Homepage Insights preview, knowledge.html grid, marquee, search index, and JSON-LD structured data all auto-update.

### 2. AEO/SEO folded into Stage 5 (not deferred to Stage 7)

User priority surfaced mid-stage: "make AEO and SEO great." Original plan deferred SEO/AEO entirely to Stage 6. Decision made to bake the foundational SEO/AEO layer into Stage 5 directly, because every page that exists is much cheaper to build SEO-correct than to retrofit. Stage 7 still exists, now scoped as the sitewide sweep (sitemap, robots, hreflang, canonical strategy across all pages).

**What Stage 5 shipped for SEO/AEO:**
- Full `<title>`, `<meta description>`, canonical URL on knowledge.html and homepage
- Open Graph + Twitter Card on both pages
- Static JSON-LD shells (`WebSite` on homepage, `CollectionPage` on knowledge.html)
- Runtime JSON-LD injection by article-loader.js — adds full `ItemList` of articles with author, date, URL, section, keywords as schema.org `Article` entities
- Microdata (`itemscope`, `itemtype`, `itemprop`) on every rendered article card
- Two new optional manifest fields: `author` and `keywords`
- Identity meta tags (`site-url`, `firm-name`) so the loader can build absolute URLs

### 3. Featured slot behavior

If any article has `"featured": true` in the manifest, that one is featured. Otherwise the newest is auto-promoted (silent fallback). The featured article is excluded from the grid below to avoid duplication.

### 4. Empty manifest behavior

Option A chosen: if manifest is empty (`[ ]`), the entire article-related sections (marquee, featured, grid, even homepage Insights preview) hide silently. Page still renders header + heading + CTA + footer. No placeholder text, no "coming soon" message, nothing that looks unfinished.

### 5. Sub-pages deferred to dedicated stage (Stage 6)

User chose to make sub-pages their own focused stage rather than fold them into Stage 5 as side-effect templates. Stage 6's first session will be discovery — what sub-pages the firm needs, what content goes on each, how each differs in tone. No code in Stage 6's first session.

### 6. Customization guide deferred to dedicated stage (Stage 8)

User chose to make the customization manual its own stage too. Slotted at Stage 8 (after SEO sweep, before first article) because it benefits from maximum context — the entire site exists in final shape by Stage 8, and the manual can describe what's actually there.

### 7. Stage 6 must produce SEO handoff for Stage 7

User explicitly requested smooth transition. Each sub-page session in Stage 6 must produce a "Stage-7-ready SEO inventory" alongside the page itself: page URL, title, meta description, primary keyword target, structured-data type, internal links, hreflang considerations. By the time Stage 7 begins, it inherits a clean inventory and just executes the sweep.

---

## Drift bugs caught and fixed during Stage 5

The Session Kit Protocol (read every file before writing) paid off five times this session. Each is documented here so future sessions are aware:

### 1. Cormorant Garamond vs. Instrument Serif (caught and fixed)

While writing knowledge.html I initially specified Cormorant Garamond as the serif font import. Theme.css canonically uses Instrument Serif. Would have rendered as a fallback font on the live site. **Fixed before shipping** — knowledge.html now imports Instrument Serif matching the homepage.

### 2. Stagger system had three conflicting conventions (fixed)

- `motion.css` declared `[data-delay="N"]` (CSS attribute selector with `transition-delay`)
- `animations.js` read `data-animate-delay` and added a `delay-N` *class*
- `motion.css` ALSO had `.delay-N` *classes* but they applied `animation-delay`, which doesn't fire on transitions
- `index.html` used `data-animate-delay`

Net result: cards on the homepage were never actually staggering. Two cards revealing simultaneously looked acceptable so the bug was invisible. With knowledge.html shipping a longer card grid, the missing stagger would have been visible.

**Fixed:** animations.js now reads either attribute and writes `data-delay` (the working convention). All homepage cards converted to `data-delay`. Knowledge.html uses `data-delay` from day one. Backward compatibility preserved.

### 3. Absolute paths on the homepage (fixed)

All 17 internal links on the homepage used absolute `/en/...` paths. PROJECT-STATUS line 82 has noted relative paths as canonical for GitHub Pages project sites. The "Insights" link from the homepage would have 404'd on most GitHub Pages deployments once knowledge.html shipped.

**Fixed:** all 17 absolute paths converted to relative. Homepage's nav now actually works on day one of Stage 5 deploy.

### 4. Two parallel card systems (`.insight-card` vs. `.fr-card`) — documented, parked

Homepage uses `.insight-card` (BEM, in theme.css, comprehensive). Article template uses `.fr-card` (custom, inline-only, references nonexistent `--font-display` variable). For Stage 5, the manifest-loaded cards use `.insight-card` consistently — the right primitive everywhere. Article template's `.fr-card` retirement parked for Stage 10.

### 5. Article template's `.article-cta` inline styling vs. shared `.section--cta` — partial fix, parked

Stage 5 added `.section--cta` to theme.css for knowledge.html's CTA. Article template still uses its old inline `.article-cta` styles. Migration to shared `.section--cta` parked for Stage 10. Zero impact on live site (different selectors, no conflict).

---

## The full file architecture as of end of Stage 5

```
repo-root/
├── /core/
│   ├── animations.js          PATCHED: stagger fix + rescan hook
│   └── article-loader.js      NEW: manifest loader + JSON-LD injector
│
├── /theme/
│   ├── theme.css              EXTENDED: +Section 18, +Section 19 (now 2,164 lines)
│   └── motion.css             UNTOUCHED
│
└── /en/
    ├── index.html             PATCHED: SEO head, auto-loading Insights, relative paths, stagger fix
    ├── knowledge.html         NEW
    └── /posts/
        ├── articles.json      NEW: manifest with 3 placeholder articles
        ├── ARTICLES-README.txt NEW: plain-language editing guide
        └── article-template.html  UNTOUCHED
```

---

## The Session Kit Protocol — UPDATED

The Session Kit is what you upload to a fresh AI session so they have everything they need to continue without losing context. It's why drift bugs got caught this session.

### Stage 6 Session Kit

When starting the next session (Stage 6 — sub-pages discovery), upload these files **one at a time** to prevent silent upload failures:

1. `PROJECT-STATUS.md` (this file)
2. `/theme/theme.css` (the foundation)
3. `/theme/motion.css` (the motion system)
4. `/en/index.html` (homepage — Stage 5 patched version)
5. `/en/knowledge.html` (the new index page)
6. `/en/posts/article-template.html` (the article template)
7. `/en/posts/articles.json` (the manifest)
8. `/en/posts/ARTICLES-README.txt` (the manifest editor guide)
9. `/core/animations.js` (Stage 5 patched version)
10. `/core/article-loader.js` (the loader)

That's 10 files. The first session of Stage 6 is **discovery only** — no code is written. The AI's first response should be:

> Discovery questions about which sub-pages the firm needs, what content goes on each, what tone they should have, what the firm's positioning is, how each sub-page connects to others.

The AI should NOT begin writing About.html or Services.html in the first Stage 6 session, no matter how clear the user's instructions seem. Sub-pages are where the firm's identity gets articulated; rushing them produces generic professional-services-firm pages.

### Stage 6 may split into sub-sessions

After the discovery session, the AI may propose:
- One sub-session per page (one for About, one for Services, one for Contact, etc.)
- Or one design-pattern session followed by individual page-build sessions
- Or one combined session if scope is small

Whichever shape Stage 6 takes, **each sub-page session must produce a Stage-7-ready SEO inventory** before that page is considered complete. The inventory has six fields:

1. Page URL
2. Page title (`<title>` value)
3. Meta description
4. Primary keyword target
5. Structured-data type (e.g. `AboutPage`, `Service`, `ContactPage`)
6. Internal links from this page

This handoff is the bridge to Stage 7. By the time Stage 7 starts, it inherits an inventory and just executes the sweep.

---

## Parked items (carried forward — none block Stage 6)

These are real but non-urgent. They are documented so they don't get lost across sessions.

### Pre-launch fixes (must address before launching the site)

- **`example.com` placeholders** in canonical URLs, Open Graph URLs, JSON-LD URLs across `index.html` and `knowledge.html`. Replace with real domain. Quick find-and-replace once the domain is known.
- **`Your Firm Name` placeholders** in `<meta name="firm-name">`, JSON-LD `Organization` entries, and HTML `🟢 EDIT: firm name` markers. Replace once the real firm name is known.
- **`hello@yourfirm.com` placeholders** in CTAs and contact links. Replace with real email.
- **Privacy and Terms pages referenced but not yet existing.** Footer links to `./privacy.html` and `./terms.html` will 404 until those pages are built. Either build them in Stage 6 or remove the footer links until they exist.

### Stage 6 dependencies (will be addressed in Stage 6)

- Sub-pages: About, Services, Contact, possibly Team, possibly individual case studies. Scope to be decided in Stage 6's discovery session.

### Stage 7 dependencies (will be addressed in Stage 7)

- `sitemap.xml` — must enumerate every page that exists by end of Stage 6.
- `robots.txt` — currently nonexistent.
- `hreflang` declarations — for future Thai/Chinese versions; declare even before those exist so search engines know the structure.
- Sitewide internal-linking review.
- Per-page canonical URL audit.

### Stage 10 cleanup items (template hardening)

- **Article template `.fr-card` system** — currently inline-only, references nonexistent `--font-display` variable, is a parallel system to `.insight-card`. Migrate to use `.insight-card` directly, retire `.fr-card`.
- **Article template `.article-cta` inline styling** — migrate to shared `.section--cta` from theme.css.
- **Article template's 9 `--font-display` references** — should all be `--font-heading`. Stage 4.5 patched some, missed others. Closing CTA `<h2>` and `.fr-card h3` are silently falling back to sans-serif.
- **`.delay-N` class definitions in motion.css** (lines 239-244) — now dead code after Stage 5's stagger fix uses `[data-delay="N"]` attribute selectors instead. Safe to remove during Stage 10 cleanup, or leave as harmless legacy.

---

## Locked architectural decisions (do not change without discussion)

These have been made. Future sessions should treat them as fixed unless the user explicitly raises them:

- **Manifest-driven publishing.** Single source of truth = `/en/posts/articles.json`.
- **`.insight-card`** is the canonical card primitive. New card types should be modifiers (`.insight-card--featured`, etc.), not parallel systems.
- **BEM naming** (`block`, `block__element`, `block--modifier`) is canonical. No camelCase, no hyphenated-flat names.
- **All paths relative** (`./` for current directory, `../` to go up). No `/en/...` absolute paths anywhere.
- **`data-delay="N"`** is the canonical stagger attribute. `data-animate-delay` is legacy-tolerated but should not be used in new code.
- **Comment-tier system:** 🟢 SAFE / 🟡 CARE / 🔴 STRUCTURE / 🔵 ALSO STRUCTURE / 📎 NOTE. Used consistently across HTML, CSS, JS.
- **Palette is Navy & Soft Linen.** `--color-stone` `#FDFAF3`, navy primary, gold accent. No new accent colors without design discussion.
- **Instrument Serif** for headings, **Inter** for body. No new font families without design discussion.
- **Ambient blob opacities** are 0.18 (navy) and 0.14 (gold) — defined in theme.css Section 17 (the BEM `--navy`/`--gold` variants). The legacy `-a`/`-b` definitions in motion.css are unused.
- **Marquee duration** is 35s linear loop. Slowing or speeding requires design discussion.
- **Reduced-motion** is fully respected — marquee `display:none`s, parallax disables, counters become instant. Do not weaken this.
- **No backend-dependent features.** Static site only. Forms that need server actions, comment systems, dynamic search beyond client-side filtering — all parked indefinitely or addressed via third-party services.

---

## How to read this document if you're a fresh AI

If you're starting Stage 6 (or any future stage) with this document in your context:

1. **Read this whole file before doing anything.** Especially "Locked architectural decisions" and "Parked items."
2. **Do not write code in your first response.** Stage 6 specifically is a discovery conversation. Confirm with the user what they want before opening any files.
3. **Read every file in the Session Kit before writing any code.** This is the Session Kit Protocol that Stage 4.5 codified after drift bugs cost three sessions of debugging. It paid off five times in Stage 5 alone.
4. **If you spot drift bugs in the existing code, surface them as observations, not unilateral fixes.** Let the user decide whether to scope-creep into a fix or park it.
5. **Stay scoped.** Each stage has a defined deliverable. If a question outside the current stage's scope comes up, capture it as a Parked Item rather than addressing it inline.
6. **Update this document at the end of every session.** Add what was built, what drift was caught, what's now parked, what's now locked.

---

## End of PROJECT-STATUS.md
