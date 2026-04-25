# 📋 PROJECT STATUS — Website Template Build

> **How to use this file:**
> At the start of every new chat with Claude, paste the contents of this file into your first message **and upload the files listed in the Session Kit** for the current stage. Claude will instantly know exactly where we are, what's been decided, and what to do next. At the end of each session, Claude will give you an updated version — replace this file with the new one.

---

## 🎯 CURRENT STATUS

**Stage:** Stage 4.5 — Rendering Fix — ✅ COMPLETE. Ready to begin Stage 5.
**Status:** 🟢 Homepage fully renders on the live site, all 49 visual checkpoints passed by user, palette fine-tuned based on feedback (bumped ambient blob opacity for more noticeable background motion, shifted base background from Warm Stone `#F4EFE6` to Soft Linen `#FDFAF3` with matching band re-calibration). Stage 4.5 discovered and fixed: the theme.css 77-missing-classes gap, button naming drift, ambient blob naming drift, cross-file header/footer drift between homepage and article template, absolute-path bug in article template, broken `--font-display` variable reference, 9 unstyled article-template classes, and the `/en/post/` folder naming typo that caused the `animations.js` 404. Session Kit Protocol formally adopted.
**Last Updated:** 25 April 2026
**Next Action:** 🔵 **NEW CHAT — begin Stage 5 (knowledge.html / Insights index page).** First message should paste this file, say "we're starting Stage 5," and upload the Stage 5 Session Kit (listed below). First decision of Stage 5: the marquee ticker content and placement on knowledge.html.

---

## 🗺️ THE FULL ROADMAP

Nine stages from start to finished reusable template. Status markers:
- ⬜ Not started
- 🟨 In progress
- ✅ Done

| # | Stage | Status | One-line summary |
|---|-------|--------|------------------|
| 1 | Planning & Architecture | ✅ Done | Folder structure, file responsibilities, and multi-language-ready architecture locked in |
| 2 | Design System & Theme | ✅ Done | `theme.css` and `motion.css` built — palette, typography, spacing, and full motion library all defined and heavily commented |
| 3 | Homepage (index.html) | ✅ Done | `/en/index.html` and `/core/animations.js` built — seven-section editorial layout with full motion suite, all placeholders clearly marked for user replacement |
| 4 | Article Template | ✅ Done | `/en/posts/article-template.html` built — reusable, richly-commented template with full JSON-LD structured data (both named-author and firm-authored variants), editorial typography, all body block types as copy-paste examples |
| 4.5 | Rendering Fix | ✅ Done | `theme.css` rebuilt to cover all 88 classes (grew from 15 to 107 defined classes, 587 → 1,728 lines). Article template patched for class-name alignment and path corrections. Ambient blob opacity bumped. Palette base shifted to Soft Linen with band re-calibration. 404 resolved (folder was wrongly `/en/post/`, corrected to `/en/`). All 49 visual checkpoints passed on live site. |
| 5 | Knowledge Index Page | ⬜ Ready to start | The "library view" — chronological feed of all articles with search, plus marquee ticker deployment |
| 6 | SEO & AI-Search Layer | ⬜ Not started | Meta tags, JSON-LD structured data, sitemap, robots.txt, llms.txt, hreflang tags |
| 7 | Documentation & Standing Instructions | ⬜ Not started | START-HERE.md, SITE-SETTINGS.md, site map |
| 8 | Test Run: First Real Article | ⬜ Not started | User publishes their first article hands-on to validate the workflow |
| 9 | Template Hardening | ⬜ Not started | Finalize as reusable kit for spinning up future sites quickly |

---

## ✅ DECISIONS LOG

Key decisions we've made, so we don't re-debate them later.

| Date | Decision |
|------|----------|
| 24 Apr 2026 | User is not a coder — all comments must be written in plain, human-friendly English with zero assumed HTML knowledge |
| 24 Apr 2026 | Comments stay in the final shipped files (no minification) — performance cost is negligible and readability is the priority |
| 24 Apr 2026 | Template will be reusable across many future websites, not just a single site |
| 24 Apr 2026 | Future sites will be similar professional services firms — template can be opinionated for this industry |
| 24 Apr 2026 | SEO and AI-search (AEO/GEO) optimization baked in from day one, not bolted on later |
| 24 Apr 2026 | User wants rich, lively animations and modern visual effects comparable to top-tier website builders |
| 24 Apr 2026 | User edits in HTML directly — no visual UI builder needed |
| 24 Apr 2026 | AI-safe zoning is a hard requirement — AI edits must be physically restricted to content zones |
| 24 Apr 2026 | Working rhythm: one chat per stage, fresh chat between stages, PROJECT-STATUS.md as the bridge |
| 24 Apr 2026 | No hidden files — `/core/` folder uses "read-and-understand, don't edit" model with full human-readable comments, not "do not look" model |
| 24 Apr 2026 | Multi-language ready architecture chosen (Approach 3 — hybrid shared shell with per-language folders) |
| 24 Apr 2026 | English built first. Thai and Chinese folders exist structurally but are dormant until activated |
| 24 Apr 2026 | No "coming soon" labels visible to visitors — site presents as a finished English site until other languages are ready |
| 24 Apr 2026 | Language switcher will activate only when additional languages go live — not shown in dormant state |
| 24 Apr 2026 | Editor: User will edit via GitHub's built-in browser editor (recommended for non-coders) or VS Code if upgrading later |
| 24 Apr 2026 | Domain: Not yet registered. Recommendation given to register sooner than later for SEO aging and professional email |
| 24 Apr 2026 | Folder structure locked in — see architecture section below |
| 24 Apr 2026 | **Design feel: Warm welcoming** — human, approachable, relationship-led, not corporate-cold |
| 24 Apr 2026 | **Palette: Navy & Warm Stone (base), refined in Stage 4.5** — navy `#1E3A5F`, ink `#1A1F2E`, muted gold `#B8902F`, soft navy `#4A6B8A`. **Background stones updated 25 Apr 2026**: page `#FDFAF3` (Soft Linen, near-white with hint of warm), client strip band `#F4EEE2` (warmth anchor), about band `#FFFCF5` (subtle warmer lift) |
| 24 Apr 2026 | **Typography: Instrument Serif (headings) + Inter (body)** — loaded from Google Fonts, with Noto fallbacks wired up for eventual Thai/Chinese/Japanese |
| 24 Apr 2026 | **Spacing: 4-based doubling scale** — 4/8/16/32/64/96/128 px. Generous editorial spacing, 680px article content width (~70 characters per line for comfortable reading) |
| 24 Apr 2026 | **Motion philosophy: "Editorial flourish + Ambient life"** — homepage & section pages get both directions; article pages get editorial flourish only. Every animation uses `cubic-bezier(0.16, 1, 0.3, 1)` easing |
| 24 Apr 2026 | **Reduced motion respected globally** — `prefers-reduced-motion` soft-fails all animations. Accessibility and SEO trust signal |
| 24 Apr 2026 | Component-level button glow, cursor-responsive headline, drifting background blobs, gold-line draw-ins, serif unfold on headings, staggered reveals, marquee ticker, scroll progress bar — all included in the motion library |
| 24 Apr 2026 | **Homepage structure: Option B — Editorial + Trust Layer (7 sections)** — Hero → Services → Client strip → Insights preview → About → Testimonial → Contact |
| 24 Apr 2026 | **Marquee OFF on homepage** — kept in motion library for deployment on other pages (likely Insights index) |
| 24 Apr 2026 | **Core service positioning: Tax · Legal · Onboarding · Bangkok** — firm's differentiator is offering all three pillars plus foreigner onboarding under one roof |
| 24 Apr 2026 | **Primary audience: Foreign companies expanding into Thailand** — copy and SEO aimed at foreign-inbound, not Thai-outbound |
| 24 Apr 2026 | **Hero copy direction: Blend of Warm & Specific** — headline "Thailand, made *straightforward.*" (italic word gets cursor-parallax effect); eyebrow "Tax · Legal · Onboarding · Bangkok"; sub-headline explains all three pillars plus onboarding in one sentence |
| 24 Apr 2026 | **Contact section uses direct details, no form** — email-only enquiries appropriate for a relationship-led firm. Adding a form is parked for Stage 5 review |
| 24 Apr 2026 | Homepage placeholders are realistic but clearly marked with `🟢 EDIT:` comments — firm name, client logos, insight article previews, testimonial quote, stats numbers, email/phone/address |
| 24 Apr 2026 | **Article taxonomy: NO categories (Stage 4)** — articles publish chronologically; search will do the navigation work. Cleaner template, less maintenance, preserves the option to layer categories on later. Each article DOES carry a small eyebrow label for editorial signalling but this is cosmetic, not a filterable taxonomy |
| 24 Apr 2026 | **Article byline: both variants available (Stage 4)** — named-author for opinion/analysis/case-studies (higher AEO ceiling); firm-authored for neutral explainers and how-to guides. Template ships with BOTH JSON-LD schemas built in. Editor picks one per article |
| 24 Apr 2026 | **Reading time shown on articles (Stage 4)** — hand-typed by the author (words ÷ 200, rounded). No auto-calculation — one less moving part |
| 24 Apr 2026 | **Marquee ticker deployment: Insights index page (Stage 5)** — confirmed during Stage 4. An archive/library page benefits from a small piece of ambient motion at the top. Exact ticker content to be decided at Stage 5 |
| 24 Apr 2026 | **Session Kit Protocol adopted (Stage 4.5)** — formalised rule: at the start of every new chat, user uploads PROJECT-STATUS.md PLUS every file the new stage will read from or modify. See the Session Kit Protocol section below. Addresses the drift problem that caused the .in-view/.is-revealed bug and the 15-vs-88-classes bug |
| 24 Apr 2026 | **BEM-style class naming is canonical (Stage 4.5)** — when existing code disagrees on naming (e.g. `btn-primary` vs `btn--primary`), the double-dash BEM variant wins. The homepage's naming convention is the reference |
| 24 Apr 2026 | **All internal site paths must be relative, never absolute (Stage 4.5)** — `/theme/theme.css` breaks on GitHub Pages project sites. Use `../theme/theme.css` from `/en/` pages and `../../theme/theme.css` from `/en/posts/` pages. Same rule for all CSS, JS, image, and internal link hrefs |
| 25 Apr 2026 | **Ambient blob opacity: navy 0.18, gold 0.14 (Stage 4.5 user feedback)** — original 0.12/0.10 was too subtle per user. Bumped for more noticeable "page feels alive" without competing with hero |
| 25 Apr 2026 | **Background shifted to Soft Linen (Stage 4.5 user feedback)** — base page `#FDFAF3` (was `#F4EFE6`), client strip band `#F4EEE2` (was `#E8E1D3`), about band `#FFFCF5` (was `#FAF6EF`). User wanted "brighter, more white-feeling, but keep the golden warmth." Band tones re-calibrated together so section rhythm still reads visibly against the brighter page |

---

## 🏗️ LOCKED ARCHITECTURE (Stage 1 output)

```
your-website-repo/
│
├── 📄 PROJECT-STATUS.md
├── 📄 START-HERE.md
├── 📄 SITE-SETTINGS.md
│
├── 📄 site.config.js            ← MAIN EDITING ZONE
├── 📄 index.html                ← Redirects to /en/
│
├── 📁 en/                       ← ACTIVE: English site
│   ├── index.html               ← ✅ Built Stage 3, live & rendering correctly after Stage 4.5
│   ├── knowledge.html           ← Will be built in Stage 5
│   └── posts/                   ← NOTE THE 's' — plural, not "post"
│       ├── article-template.html  ← ✅ Built Stage 4, patched in Stage 4.5
│       └── first-article.html     ← Placeholder article, Stage 8
│
├── 📁 th/                       ← DORMANT: Thai site (structure only)
├── 📁 cn/                       ← DORMANT: Chinese site (structure only)
│
├── 📁 assets/                   ← Shared: logo, images, favicon
│
├── 📁 theme/                    ← Shared design system ✅ BUILT IN STAGE 2
│   ├── theme.css                ← ✅ Rebuilt in Stage 4.5 (1,728 lines, 107-class coverage, 88-class homepage verified)
│   └── motion.css               ← ✅ Done — animations, transitions, ambient motion
│
├── 📁 core/                     ← Read-and-understand (fully commented)
│   ├── components.html
│   ├── config-loader.js
│   └── animations.js            ← ✅ Built in Stage 3 — lives at repo-root `/core/`, NOT inside `/en/`
│
└── 📁 seo/                      ← SEO & AI-search files
    ├── sitemap.xml
    ├── robots.txt
    └── llms.txt
```

**Editing zones:**
- 🟢 **Safe to edit freely:** `site.config.js`, all files in `/en/posts/`, `/th/posts/`, `/cn/posts/`
- 🟡 **Edit carefully with understanding:** `/theme/` files, page HTML files in `/en/`, `/th/`, `/cn/`
- 🔴 **Read-and-understand, don't edit:** `/core/` files — touch only if you know what you're doing

**AI permission zones:**
- AI may create/modify files **only** in `/en/posts/`, `/th/posts/`, `/cn/posts/`
- AI may append one line to `knowledge.html` files when adding a new article
- AI must **never** modify `site.config.js`, `/core/`, `/theme/`, `/assets/`, or any top-level page file without explicit user instruction

---

## 📦 SESSION KIT PROTOCOL (adopted Stage 4.5)

**The problem this solves.** PROJECT-STATUS.md is excellent at carrying *decisions* across chats, but it can't carry *code conventions* — class names, variable names, selector strings, data attributes. Those live in the files themselves. If Claude starts a new stage without reading the existing files, it's guessing at internal conventions from memory, which is how drift bugs happen. We hit this three times:

1. **Stage 3 → Stage 4 drift:** `motion.css` named the reveal class `.in-view`, but `animations.js` added `.is-revealed` — causing sections below the hero to stay invisible.
2. **Stage 2 → Stage 3 drift:** `theme.css` only defined 15 classes, but the homepage HTML used 88 — causing the layout system to be invisible.
3. **Stage 3 ↔ Stage 4 drift:** Homepage and article template used totally different naming conventions for their "shared" header and footer.

**The rule.** At the start of every new chat, the user uploads:
1. **PROJECT-STATUS.md** (always)
2. **Every file the new stage will READ FROM or MODIFY** (the Session Kit for that stage — listed below)

Claude's first action in the new chat is to read every uploaded file before writing a single line of code. The Session Kit is the payload; PROJECT-STATUS is the narrator.

**Per-stage Session Kits.**

| Stage | Session Kit (files to upload with PROJECT-STATUS.md) |
|-------|-----------------------------------------------------|
| **Stage 5** (knowledge.html) | `theme.css`, `motion.css`, `/en/index.html`, `/en/posts/article-template.html`, `/core/animations.js` |
| **Stage 6** (SEO layer) | `theme.css`, `/en/index.html`, `/en/posts/article-template.html`, `/en/knowledge.html`, any existing `seo/` files |
| **Stage 7** (docs) | All files (docs reference the whole repo). If upload limit becomes an issue, upload in priority order: PROJECT-STATUS, all `/theme/`, all `/en/`, all `/core/` |
| **Stage 8** (first article) | `/en/posts/article-template.html`, `/en/knowledge.html`, PROJECT-STATUS |
| **Stage 9** (template hardening) | All files |

**What to do if an upload silently fails.** Sometimes files with the same name (e.g. two `index.html` files from different folders) don't all come through. A file will appear in the upload list but its content won't reach Claude. If Claude reports a missing file it should have, re-upload with renamed prefixes (e.g. `en-index.html`, `root-index.html`) to force uniqueness. Claude can also read files directly from the `/mnt/user-data/uploads/` filesystem path as a fallback, but giving distinct names is safer.

---

## 🎨 LOCKED DESIGN SYSTEM (Stage 2 output, refined Stage 4.5)

### Palette — "Navy & Soft Linen" (updated 25 Apr 2026)
- **Navy** `#1E3A5F` — primary brand color, used for headings, primary buttons, footer
- **Soft Linen** `#FDFAF3` — page background, near-white with a hint of warm
- **Ink** `#1A1F2E` — body text (slightly softer than pure black)
- **Muted Gold** `#B8902F` — accent: eyebrows, underlines, hover highlights, ticker dots
- **Soft Navy** `#4A6B8A` — secondary accents and muted borders
- **Stone variants:** page `#FDFAF3` / lighter-warmer band `#FFFCF5` / darker band `#F4EEE2`

### Typography
- **Headings:** Instrument Serif (weight 400) — Google Fonts
- **Body:** Inter (weights 400, 500, 600) — Google Fonts
- **Fallbacks:** Noto Serif TC / JP / Thai (for headings), Noto Sans TC / JP / Thai (for body)
- **Scale:** xs (12px) / sm (14px) / base (16px) / md (18px) / lg (22px) / xl (28px) / 2xl (36px) / 3xl (48px) / 4xl (64px)

### Spacing
- 4-based doubling: `xs` 4px / `sm` 8px / `md` 16px / `lg` 32px / `xl` 64px / `2xl` 96px / `3xl` 128px
- Article content width: **680px** (~70 chars per line)
- Main content width: 1100px
- Wide hero width: 1400px

### Motion
- Every animation uses `cubic-bezier(0.16, 1, 0.3, 1)` easing
- Durations: fast 200ms / base 400ms / medium 700ms / slow 1100ms / ambient 20s
- Stagger step: 120ms between cascading children
- Homepage and section pages: **full motion suite** (editorial flourish + ambient life)
- Article pages: **editorial flourish only** — for reading comfort
- Reduced-motion preference fully respected
- **Ambient blob opacity (post-feedback):** navy 0.18, gold 0.14

### What's in the motion library
Class-based entrance animations (`animate-fade-up`, `animate-serif-unfold`, `animate-line-draw`), delay modifiers (`delay-1` through `delay-6`), scroll-triggered reveals (`data-animate="fade-up"` etc.), link underline draw, hover lift for cards, cursor-following gold glow on buttons, hero headline cursor parallax, drifting ambient background blobs, scroll progress bar, and marquee ticker.

### JavaScript helpers (Stage 3 output — `/core/animations.js`)
All five helpers are built, each self-contained and independently toggleable:
1. ✅ **Scroll-trigger observer** — adds `is-revealed` class to `[data-animate]` elements (threshold 0.15, rootMargin `-10%`)
2. ✅ **Cursor-position tracker for button glow** — updates `--glow-x` / `--glow-y` on `.btn--glow`
3. ✅ **Cursor parallax for hero headlines** — smooth lerp-based drift, max 14px offset, opposite-direction
4. ✅ **Scroll progress bar** — rAF-throttled width update on `#scrollProgress`
5. ✅ **Stats counter animation** — count-up from 0 to `data-target`, ease-out cubic, 1.6s

All helpers respect `prefers-reduced-motion`.

---

## 🏡 HOMEPAGE CONTENT MAP (Stage 3 output)

### Seven sections, in order:
1. **Hero** — eyebrow, headline with cursor-parallax italic, sub-headline, primary + secondary CTA, scroll cue
2. **Services** — three cards: Tax/accounting/audit, Legal/regulatory, Onboarding foreigners
3. **Client strip** — trust layer, five client-name slots, optional geography line underneath
4. **Insights preview** — two most-recent article cards with link to full Insights index
5. **About** — two-column: heading + short bio, plus three counted stats (years, clients, countries)
6. **Testimonial** — single pull-quote with attribution
7. **Contact** — heading + lede on left; email, phone, office, hours on right

### Placeholders the user replaces before going live
- Firm name, email, phone, office address
- Five client names in client strip
- Two insight article titles + excerpts + metadata
- Testimonial quote + attribution
- Three About stat numbers: 12 / 140 / 18 (adjustable via `data-target`)
- Footer tagline and copyright year

---

## 📰 ARTICLE TEMPLATE MAP (Stage 4 output, patched in Stage 4.5)

### Shell (matches homepage exactly after Stage 4.5 patch)
- Same `<header>`: firm name (`site-header__logo`), nav (`site-header__nav`), email CTA (`btn btn--glow`)
- Same `<footer>`: three columns (`site-footer__col` / `site-footer__col--brand`) plus base row (`site-footer__base`)
- Scroll progress bar at the top
- Loads `/theme/theme.css`, `/theme/motion.css`, `/core/animations.js`
- **All paths relative:** `../../theme/theme.css`, `../../core/animations.js`

### Article-specific zones, top to bottom
1. **Article header** — eyebrow + gold line draw-in, title (serif-unfold, optional italic accent), optional standfirst, meta row (date + reading time + byline, gold dot separators)
2. **Article body** — 680px reading column with house-styled typography: drop-cap opening paragraph, H2/H3 sub-headings, gold-marker lists, internal + external links (gold underline draw-in), callout box, pull quote (centred, gold hairlines), block quote with citation, image + caption, data table, closing summary
3. **Byline / author block** — TWO JSON-LD schema variants in `<head>`; TWO matching visual blocks. Editor picks one:
   - **Variant A (named author):** `@type: Person` + `jobTitle` + `worksFor`. For opinion, analysis, case-studies
   - **Variant B (firm-authored):** `@type: Organization`. For neutral explainers, how-to guides
4. **Further reading** — three hand-picked related-article cards in a responsive grid
5. **Soft contact CTA** — gentle closing invitation

### Motion rules on article pages
- ✅ Scroll progress, serif-unfold, gold line draw-in, fade-up reveals, link underline draw
- ❌ NO cursor parallax, NO drifting blobs, NO marquee ticker, NO counting-up stats

### Five colour-coded comment tiers
- 🟢 **EDIT** — safe to change
- 🔵 **STRUCTURE** — leave alone; changing breaks layout
- 🟡 **OPTIONAL** — toggle on/off by uncommenting
- 🔴 **WARNING** — removal breaks the site
- 📎 **NOTE** — background info only

---

## 🔧 STAGE 4.5 FINAL SUMMARY (what just happened, for future reference)

### What was rebuilt
- **`theme.css`** grew 587 → 1,728 lines; 15 defined classes → 107; all 88 homepage classes verified covered; both button naming conventions aliased; both footer naming conventions supported side-by-side as a safety net; responsive at 900px and 600px; balanced braces and comments; no nested-comment anti-pattern; palette base shifted to Soft Linen with matching band recalibration; ambient blob opacity bumped post-feedback
- **`article-template.html`** received four patches: header class names aligned to homepage, footer class names aligned to homepage, all paths changed from absolute to relative for GitHub Pages, inline `<style>` block fixed (bad `--font-display` variable reference) and 9 previously-unstyled classes added

### Lessons captured (rules now in effect for all future stages)
1. **Never write HTML comment syntax INSIDE another HTML comment** — the parser treats any `-->` as a close, even inside what looks like a larger block
2. **Never trust cross-session internal conventions from memory** — at the start of any stage that touches a previously-built file, READ the existing file first (this is why the Session Kit Protocol exists)
3. **Never use absolute internal paths on GitHub Pages project sites** — always relative, scaled to the file's depth
4. **Never reference a CSS variable that isn't defined** — confirm the variable name matches what's actually in `:root`
5. **Check every class used in HTML has a CSS rule somewhere** — mechanical check at the end of every stage that touches CSS or HTML
6. **File-and-folder names are case-sensitive on GitHub Pages** and easy to typo invisibly — verify path structure matches what PROJECT-STATUS expects

### Final live-site state after Stage 4.5 close-out
- All 49 visual checkpoints passed by user
- Header, hero, all seven sections, footer all rendering correctly
- Ambient blobs visible and drifting
- Cursor parallax working on italic word
- Scroll progress bar filling as user scrolls
- Stats counting up on scroll
- Hover states on buttons and links working
- Mobile responsive (stacking correctly)
- Palette base is now Soft Linen `#FDFAF3`

---

## 🅿️ PARKED ITEMS / OPEN QUESTIONS

Things we noticed but chose to handle later. Nothing gets forgotten.

- **Build step (optional):** Whether to use a small build script to avoid copy-pasting shared header/footer into every article file. Deferred. Template currently ships with header/footer hand-pasted into each page file. Revisit at Stage 7 (documentation) or Stage 9 (hardening).
- **Theme variants:** Pre-built alternate color schemes (Warm Peach / Professional Blue / Minimal Monochrome) to be built in Stage 9. Current palette can be re-skinned by changing the 5 brand color variables in theme.css.
- **Analytics slot:** Location in config for pasting Google Analytics / Plausible / Umami tracking code — add in Stage 6.
- **Domain registration:** User planning to register but hasn't yet. Needed for Stage 6 SEO config.
- **Translation workflow:** When Thai and Chinese are activated, user will need to decide on translation method. Not urgent until Phase 2.
- **Japanese as 4th language:** User has Japanese clients — could be added later. Architecture already supports it. Font stack includes Noto JP.
- **Browser language auto-detect:** Root `index.html` could auto-detect visitor's browser language and redirect accordingly. Deferred until Thai/Chinese are activated.
- **Contact form vs email-only:** Homepage launched email-only. Revisit in Stage 5 if enquiry volume suggests a form is needed.
- **Newsletter signup:** Not built into homepage or article template. Decide in Stage 5 whether Insights articles should drive email-list signups.
- **Insights preview auto-population:** The two article cards on the homepage are hand-edited. In Stage 5, consider whether a small build script should auto-pull the two most recent articles.
- **Hero imagery:** Homepage launched as pure-typography hero. Revisit only if feedback suggests it feels thin.
- **Author pages:** Named-author JSON-LD references a Person by name but doesn't link to a dedicated author page. For maximum AEO lift, each named author should eventually have their own page. Deferred to Stage 9.
- **Share image (Open Graph image):** Template has `og:image` meta tag commented out. Each article should ideally have a 1200×630 px social share image. Workflow to be documented in Stage 7.
- **Further-reading auto-population:** The three further-reading cards are hand-picked per article. If article count grows large (20+), consider a small build script.
- **Reading-time accuracy:** Currently hand-typed. If tedious at volume, a tiny JS helper could calculate it. Deferred.
- **Article-template header/footer drift protection:** When user edits header/footer on homepage (e.g. renames firm), they must also edit article-template AND every cloned article. Same parking spot as build-step question above.
- **Marquee ticker content:** Deployment confirmed for Insights index (Stage 5). Exact content still to be decided — rotating latest article titles, publication cadence signal, or topic tags drifting past. **First decision of Stage 5.**
- **Favicon:** Console logs `favicon.ico 404`. Harmless but untidy. Will be handled in Stage 6 alongside Open Graph images and touch icons.
- **Gold saturation on new lighter background:** After palette shift to Soft Linen, user confirmed acceptable. If at any future stage the gold feels washed out against the brighter background, consider bumping `--color-gold` from `#B8902F` to a shade deeper. Current state: user approved as-is.

---

## 📝 CONTEXT HANDOFF NOTES

Subtle things about the user and project that aren't formal decisions but are worth Claude remembering across chats.

- **User's coding level:** Zero coding experience. Needs plain English explanations, not developer shorthand.
- **User's priority order:** (1) Ease of self-editing with human-readable comments, (2) Rich visual/animation quality, (3) Reusability as template, (4) SEO and AI-search optimization, (5) Multi-language readiness.
- **User's communication style:** Prefers honest, direct answers — including being told when scope has grown or when an earlier plan needs adjusting. Appreciates being warned about tradeoffs upfront. Asks sharp, good questions. Don't assume, explain.
- **User's aesthetic sensibility confirmed:** Chose the confident, distinctive options over the safest ones. Also chose the bolder "near white" background option over the subtle one — willing to be bold when the payoff is clear. Don't over-apologize or over-caveat in future stages.
- **User gives concrete precise feedback:** When asked "what does the live site look like," user went through all 49 points and marked each. When asked about background colour, user picked one of three options specifically rather than saying "make it brighter." Claude should offer structured choices rather than asking vague open questions.
- **Existing assets:** User had an initial HTML file with warm peach palette. Superseded by Navy & Warm Stone in Stage 2, then refined to Navy & Soft Linen in Stage 4.5.
- **User's business context:** Professional services firm in Thailand, serving foreign and local enterprises. Client examples from UK, USA, Japan. Core offering is the full landing-and-operating stack for foreigners entering Thailand — tax/accounting/audit + legal/regulatory + practical onboarding (visas, permits, company setup, banking introductions).
- **Editor environment:** User will likely use GitHub's browser editor. Design navigation comments to work well there (no assumption of code-folding features).
- **Deployment environment:** GitHub Pages project site at `https://phuwanutkhodop.github.io/accountingsite.github.io/`. Case-sensitive file system. All internal paths must be relative.
- **Memory setting:** User has not enabled Claude's Memory feature. PROJECT-STATUS.md + Session Kit are the primary context-carrying mechanisms between chats.
- **User values ownership:** Rejected "hidden folder" approach in favor of "read-and-understand" — clear signal that user wants genuine understanding and control over the full template.
- **Working pattern that works well:** Show options visually → give honest recommendation with pros/cons → let user choose. Ask nested decisions one at a time, not all at once.
- **User will push back when the process slips:** When Claude rewrote PROJECT-STATUS.md in a condensed format instead of preserving existing structure, user immediately flagged it. Lesson: this file is the user's scaffolding system — preserve its structure literally, add new content into existing sections rather than summarizing or rewriting.
- **User asks practical "can I change it later" questions:** Answer them concretely with what's easy, what's medium, and what's hard — not just "yes, of course."
- **User thinks ahead about SEO / AEO impact:** Bring AEO reasoning into future decisions proactively.
- **User is comfortable stopping and re-chatting when context gets long (Stage 4.5):** User proactively suggested wrapping up a long chat and starting fresh. Claude should recognise this signal and produce clean handoffs rather than pushing to finish in the same chat.
- **User catches structural problems quickly (Stage 4.5):** User noticed their folder was `/en/post/index.html` instead of `/en/index.html` before Claude fully diagnosed it. Trust the user's observations — when they ask whether something is right, they've usually noticed something off.
- **User distinguishes "works" from "I like it" (Stage 4.5):** When given a visual checklist, user pre-emptively clarified that marking items as "pass" means the functionality works but doesn't preclude later design changes. Good discipline — Claude should mirror this and distinguish "shipped" from "finalized design."
- **User is willing to make palette-level changes late (Stage 4.5):** User requested a significant palette shift (near-white background) after all decisions seemed locked. This is fine — the design-token architecture was built for exactly this. Don't treat past decisions as immovable when user feedback suggests they should change.

---

## 🔄 CHANGE LOG

| Date | Change |
|------|--------|
| 24 Apr 2026 | File created. Nine-stage roadmap locked in. Stage 1 ready to begin. |
| 24 Apr 2026 | Stage 1 complete. Architecture locked, multi-language-ready structure chosen (Approach 3), `/core/` changed from hidden to fully-commented read-and-understand zone, language switcher to activate only when additional languages go live. |
| 24 Apr 2026 | Stage 2 complete. Design system locked: Navy & Warm Stone palette, Instrument Serif + Inter typography, 4-based doubling spacing scale, Editorial flourish + Ambient life motion philosophy. `theme.css` and `motion.css` written with full plain-English commenting. |
| 24 Apr 2026 | Stage 3 complete. Homepage structure locked (Option B — 7 sections). Marquee OFF on homepage. Hero copy finalized. `/en/index.html` and `/core/animations.js` built. |
| 24 Apr 2026 | PROJECT-STATUS.md restored to full original format after user flagged condensed update. Lesson captured. |
| 24 Apr 2026 | Stage 4 complete. Article taxonomy: NO categories. Byline: both variants with JSON-LD. Reading time hand-typed. Marquee ticker reserved for Stage 5. `/en/posts/article-template.html` built with five colour-coded comment tiers. |
| 24 Apr 2026 | Post-Stage-4 preview debug. Four issues: project-site URL structure (expected), duplicate root index.html (patched), nested-comment anti-pattern in `/en/index.html` (patched), class-name drift between motion.css (`.in-view`) and animations.js (`.is-revealed`) causing invisible sections. Fixed. |
| 24 Apr 2026 | Stage 4.5 started. Discovery found theme.css 15/88 class gap, button + blob + header/footer naming drift, absolute-path bug, broken CSS variable, 9 unstyled article classes. Session Kit Protocol adopted. |
| 25 Apr 2026 | Stage 4.5 completed. Folder typo `/en/post/` corrected to `/en/`, resolving 404 on animations.js. All 49 visual checkpoints passed on live site. Ambient blobs opacity bumped 0.12→0.18 navy, 0.10→0.14 gold. Palette base shifted Warm Stone→Soft Linen with matching band recalibration. User approved final state. Ready for Stage 5. |

---

## ▶️ HOW TO RESUME WORK WITH CLAUDE

When you open a new chat:

1. Start your first message with: *"Here's our project status — please catch up."*
2. Paste this entire file below that sentence.
3. **Upload the files listed in the current stage's Session Kit** (see Session Kit Protocol section above).
4. Claude will read PROJECT-STATUS and every uploaded file before doing anything else, then confirm the current stage and tell you what's next.
5. Work through that stage.
6. At the end, Claude gives you an updated version of this file.
7. Replace the old file in your GitHub repo with the new one.

### For the next chat (Stage 5 — knowledge.html)

Your first message should contain:
1. The sentence: *"Here's our project status — please catch up. We're starting Stage 5: the knowledge.html Insights index page."*
2. This entire file pasted below.
3. **Uploads (Stage 5 Session Kit):**
   - `theme.css` (current, from your repo)
   - `motion.css` (from your repo)
   - `/en/index.html` (the homepage, for pattern/reference)
   - `/en/posts/article-template.html` (for consistency reference)
   - `/core/animations.js` (for motion integration)

Claude will then walk you through the Stage 5 decisions in order, starting with the marquee ticker content and placement.
