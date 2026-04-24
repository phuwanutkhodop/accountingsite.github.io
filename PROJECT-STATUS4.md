# 📋 PROJECT STATUS — Website Template Build

> **How to use this file:**  
> At the start of every new chat with Claude, paste the contents of this file into your first message. Claude will instantly know exactly where we are, what's been decided, and what to do next. At the end of each session, Claude will give you an updated version — replace this file with the new one.

---

## 🎯 CURRENT STATUS

**Stage:** Stage 4 — Article Template (article-template.html)  
**Status:** ✅ Complete  
**Last Updated:** 24 April 2026  
**Next Action:** Start a fresh chat for Stage 5 (Knowledge Index Page). Paste this file into the first message. Claude will begin by confirming the two carry-over decisions already made at the end of Stage 4: (a) the Insights index is a chronological feed with search (no category filters, decided in Stage 4), and (b) the marquee ticker will deploy on the Insights index (confirmed in Stage 4). Stage 5 itself will produce `/en/knowledge.html` — the "library view" that lists every published article, plus the small search/filter UI needed to make a category-less feed navigable as it grows.

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
| 24 Apr 2026 | **Palette: Navy & Warm Stone (Option D)** — navy `#1E3A5F`, warm stone `#F4EFE6`, ink `#1A1F2E`, muted gold `#B8902F`, soft navy `#4A6B8A` |
| 24 Apr 2026 | **Typography: Instrument Serif (headings) + Inter (body)** — loaded from Google Fonts, with Noto fallbacks wired up for eventual Thai/Chinese/Japanese |
| 24 Apr 2026 | **Spacing: 4-based doubling scale** — 4/8/16/32/64/96/128 px. Generous editorial spacing, 680px article content width (~70 characters per line for comfortable reading) |
| 24 Apr 2026 | **Motion philosophy: "Editorial flourish + Ambient life"** — homepage & section pages get both directions; article pages get editorial flourish only (no marquee/drifting distractions while reading). Every animation uses `cubic-bezier(0.16, 1, 0.3, 1)` easing for consistency |
| 24 Apr 2026 | **Reduced motion respected globally** — `prefers-reduced-motion` soft-fails all animations to simple fades or removes them entirely. Accessibility and SEO trust signal |
| 24 Apr 2026 | Component-level button glow, cursor-responsive headline, drifting background blobs, gold-line draw-ins, serif unfold on headings, staggered reveals, marquee ticker, scroll progress bar — all included in the motion library |
| 24 Apr 2026 | **Homepage structure: Option B — Editorial + Trust Layer (7 sections)** — Hero → Services → Client strip → Insights preview → About → Testimonial → Contact. Option A (5 sections) felt thin against the rich motion system; Option C (8 sections with marquee) risked competing with the hero |
| 24 Apr 2026 | **Marquee OFF on homepage** — kept in motion library for deployment on other pages (likely Insights index). On the warm editorial palette, marquee near the hero would fight the headline for attention |
| 24 Apr 2026 | **Core service positioning: Tax · Legal · Onboarding · Bangkok** — firm's differentiator is offering all three pillars plus foreigner onboarding under one roof, where most Bangkok firms pitch only one |
| 24 Apr 2026 | **Primary audience: Foreign companies expanding into Thailand** — copy and SEO aimed at foreign-inbound, not Thai-outbound |
| 24 Apr 2026 | **Hero copy direction: Blend of Warm & Specific** — headline "Thailand, made *straightforward.*" (italic word gets cursor-parallax effect); eyebrow "Tax · Legal · Onboarding · Bangkok"; sub-headline explains all three pillars plus onboarding in one sentence. Combines the warmth of Draft 1 with the SEO-specificity of Draft 2 |
| 24 Apr 2026 | **Contact section uses direct details, no form** — email-only enquiries appropriate for a relationship-led firm. Adding a form is parked for Stage 5 review |
| 24 Apr 2026 | Homepage placeholders are realistic but clearly marked with `🟢 EDIT:` comments — firm name, client logos, insight article previews, testimonial quote, stats numbers, email/phone/address. User swaps each in piece by piece without breaking anything |
| 24 Apr 2026 | **Article taxonomy: NO categories (Stage 4)** — articles publish chronologically; search will do the navigation work. Cleaner template, less maintenance, preserves the option to layer categories on later if article volume ever justifies it. Each article DOES carry a small eyebrow label (e.g. "Insight", "Guide", "Analysis") for editorial signalling but this is cosmetic, not a filterable taxonomy |
| 24 Apr 2026 | **Article byline: both variants available (Stage 4)** — named-author for opinion/analysis/case-studies (higher AEO ceiling for thought-leadership content); firm-authored for neutral explainers and how-to guides. Template ships with BOTH JSON-LD schemas built in (Variant A = `@type: Person` with `jobTitle` and `worksFor`; Variant B = `@type: Organization`). Editor picks one per article by choosing which block to leave active and which to delete/comment out. This gives maximum AEO upside (AI search engines cite content with named, credentialed authors more often) without forcing every post to carry a named byline |
| 24 Apr 2026 | **Reading time shown on articles (Stage 4)** — hand-typed by the author (words ÷ 200, rounded). No auto-calculation — one less moving part for a non-coder. Sits next to publication date in the meta row |
| 24 Apr 2026 | **Marquee ticker deployment: Insights index page (Stage 5)** — confirmed during Stage 4. An archive/library page benefits from a small piece of ambient motion at the top because the page itself is mostly static lists; on the homepage it would have fought the hero. Exact ticker content to be decided at Stage 5 (rotating article categories, latest teasers, or publication cadence) |

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
│   ├── index.html               ← ✅ Built in Stage 3
│   ├── knowledge.html           ← Will be built in Stage 5
│   └── posts/
│       ├── article-template.html  ← ✅ Built in Stage 4
│       └── first-article.html     ← Placeholder article, Stage 8
│
├── 📁 th/                       ← DORMANT: Thai site (structure only)
├── 📁 cn/                       ← DORMANT: Chinese site (structure only)
│
├── 📁 assets/                   ← Shared: logo, images, favicon
│
├── 📁 theme/                    ← Shared design system ✅ BUILT IN STAGE 2
│   ├── theme.css                ← ✅ Done — palette, fonts, spacing, buttons
│   └── motion.css               ← ✅ Done — animations, transitions, ambient motion
│
├── 📁 core/                     ← Read-and-understand (fully commented)
│   ├── components.html
│   ├── config-loader.js
│   └── animations.js            ← ✅ Built in Stage 3 (scroll triggers, cursor glow, parallax, progress bar, counters)
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

## 🎨 LOCKED DESIGN SYSTEM (Stage 2 output)

### Palette — "Navy & Warm Stone"
- **Navy** `#1E3A5F` — primary brand color, used for headings, primary buttons, footer
- **Warm Stone** `#F4EFE6` — page background, never pure white
- **Ink** `#1A1F2E` — body text (slightly softer than pure black)
- **Muted Gold** `#B8902F` — accent: eyebrows, underlines, hover highlights, ticker dots
- **Soft Navy** `#4A6B8A` — secondary accents and muted borders

### Typography
- **Headings:** Instrument Serif (weight 400) — Google Fonts
- **Body:** Inter (weights 400, 500, 600) — Google Fonts
- **Fallbacks:** Noto Serif TC / JP / Thai (for headings), Noto Sans TC / JP / Thai (for body) — Asian language readiness baked in
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
- Article pages: **editorial flourish only** (no marquee, no drifting blobs) — for reading comfort
- Reduced-motion preference fully respected

### What's in the motion library
Class-based entrance animations (`animate-fade-up`, `animate-serif-unfold`, `animate-line-draw`), delay modifiers (`delay-1` through `delay-6`), scroll-triggered reveals (`data-animate="fade-up"` etc.), link underline draw, hover lift for cards, cursor-following gold glow on buttons, hero headline cursor parallax, drifting ambient background blobs, scroll progress bar, and marquee ticker.

### JavaScript helpers (Stage 3 output — `/core/animations.js`)
All five helpers now built, each self-contained and independently toggleable:
1. ✅ **Scroll-trigger observer** — adds `is-revealed` class to `[data-animate]` elements as they enter the viewport (threshold 0.15, rootMargin `-10%`)
2. ✅ **Cursor-position tracker for button glow** — updates `--glow-x` / `--glow-y` custom properties on `.btn--glow` elements
3. ✅ **Cursor parallax for hero headlines** — smooth lerp-based drift on `[data-cursor-parallax]` elements, max 14px offset, opposite-direction movement
4. ✅ **Scroll progress bar width updater** — updates `#scrollProgress` width on scroll, rAF-throttled
5. ✅ **Stats counter animation** — count-up from 0 to `data-target` on `[data-counter]` elements, ease-out cubic, 1.6s duration
All helpers respect `prefers-reduced-motion` (reveals become instant, parallax + glow disable entirely, counter shows final number immediately).

---

## 🏡 HOMEPAGE CONTENT MAP (Stage 3 output)

Written here so future stages and future translations (Thai / Chinese) know exactly what the English homepage contains.

### Seven sections, in order:
1. **Hero** — eyebrow, headline with cursor-parallax italic, sub-headline, primary + secondary CTA, scroll cue
2. **Services** — three cards: Tax/accounting/audit, Legal/regulatory, Onboarding foreigners
3. **Client strip** — trust layer, five client-name slots, optional geography line underneath
4. **Insights preview** — two most-recent article cards with link to full Insights index
5. **About** — two-column: heading + short bio, plus three counted stats (years, clients, countries)
6. **Testimonial** — single pull-quote with attribution (name, role, company, country)
7. **Contact** — heading + lede on left; email, phone, office, hours on right

### Placeholders the user needs to replace before going live
- Firm name (`Your Firm Name`) — appears in header, footer, testimonial footer
- Email (`hello@yourfirm.com`) — header CTA, contact section, footer
- Phone (`+66 (0) 2 000 0000`) — contact section, footer
- Office address — contact section, footer
- Five client names in client strip (currently "Client Name" × 5)
- Two insight article titles + excerpts + metadata (currently plausible placeholders)
- One testimonial quote + attribution (currently plausible placeholder)
- Three About-section stat numbers: 12 (years), 140 (clients), 18 (countries) — all adjustable via `data-target` attribute
- Footer tagline and copyright year

---

## 📰 ARTICLE TEMPLATE MAP (Stage 4 output)

Written here so future stages and future translations know exactly what the article template contains.

### Shell (matches homepage)
- Same `<header>`: logo/firm name, nav (Services / Insights / About / Contact), email CTA
- Same `<footer>`: firm name, tagline, email/phone/location, copyright year
- Scroll progress bar at the top (gold line driven by `/core/animations.js`)
- Loads `/theme/theme.css`, `/theme/motion.css`, `/core/animations.js`

### Article-specific zones, top to bottom
1. **Article header** — eyebrow (topic cue, e.g. "Insight", "Guide") with gold draw-in line, title (serif-unfold animation, optional italic accent word), optional standfirst/deck (italic lead paragraph), meta row (publication date + reading time + byline, divided by gold dots)
2. **Article body** — 680px reading column with rich house-styled typography: paragraphs (first-letter drop-cap on the opening paragraph), H2 and H3 sub-headings, bulleted + numbered lists with gold markers, internal + external links (gold underline draw-in on hover), callout box, pull quote (centred, gold hairlines top & bottom), block quote with citation, image + caption, data table, closing summary section
3. **Byline / author block** — TWO JSON-LD schema variants pre-wired in `<head>`; TWO matching visual blocks at the end of `<article>`. Editor picks one per article:
   - **Variant A (named author):** `@type: Person` + `jobTitle` + `worksFor`. For opinion, analysis, case-studies, thought-leadership
   - **Variant B (firm-authored):** `@type: Organization`. For neutral explainers, how-to guides, FAQs
4. **Further reading** — three hand-picked related-article cards in a responsive grid. Chosen editorially per article since articles don't have categories to auto-match against
5. **Soft contact CTA** — gentle closing invitation ("Have a question this article didn't answer?") with email button. Softer tone than homepage contact because readers who reach the end of an article are already warm

### Motion rules on article pages (editorial flourish only)
- ✅ Scroll progress bar, serif-unfold on title, gold line draw-in, fade-up reveals on content blocks, link underline draw
- ❌ NO cursor parallax, NO drifting blobs, NO marquee ticker, NO counting-up stats — all reserved for homepage / insights index

### Comment system inside the template
Five colour codes used throughout the file to guide the editor:
- 🟢 **EDIT** — safe to change; this is your content
- 🔵 **STRUCTURE** — leave alone; changing it may break the layout
- 🟡 **OPTIONAL** — a feature you can turn on/off by uncommenting
- 🔴 **WARNING** — do not remove; breaks the site
- 📎 **NOTE** — background info for understanding, not action

### Placeholders the user replaces per article
- Page `<title>`, meta description, canonical URL, Open Graph tags (all in `<head>`)
- JSON-LD fields: `headline`, `description`, `url`, `datePublished`, `dateModified`, and author details
- Eyebrow label, H1 title, standfirst (or delete), meta row (date + reading time + byline)
- Entire article body (example content must be deleted and replaced)
- Author block: name, role, bio OR firm bio
- Three further-reading card links
- `/assets/example-article-image.jpg` — swap for the article's hero image or delete the `<figure>` if no image

---

## 🅿️ PARKED ITEMS / OPEN QUESTIONS

Things we noticed but chose to handle later. Nothing gets forgotten.

- **Build step (optional):** Whether to use a small build script to avoid copy-pasting shared header/footer into every article file. **Decision STILL deferred after Stage 4** — template currently ships with header/footer hand-pasted into each page file, which works fine while the site is small. Revisit at Stage 7 (documentation) or Stage 9 (hardening) once there are more articles to gauge the maintenance cost.
- **Theme variants:** Pre-built alternate color schemes (Warm Peach / Professional Blue / Minimal Monochrome) to be built in Stage 9 during template hardening. Note: current Navy & Warm Stone palette could easily be re-skinned by changing the 5 brand color variables in `theme.css`.
- **Analytics slot:** Location in config for pasting Google Analytics / Plausible / Umami tracking code — to be added in Stage 6.
- **Domain registration:** User planning to register but hasn't yet. Will need to be filled into SEO config once registered. Relevant for Stage 6.
- **Translation workflow:** When Thai and Chinese are activated, user will need to decide on translation method (human translator / AI-assisted / hybrid). Not urgent until Phase 2.
- **Japanese as 4th language:** User has Japanese clients — Japanese could be added later as a 4th language. Architecture already supports adding more languages. Font stack already includes Noto JP.
- **Browser language auto-detect:** Root `index.html` could auto-detect visitor's browser language and redirect accordingly. Decision deferred until Thai/Chinese are activated.
- **Contact form vs email-only:** Homepage launched email-only. If enquiry volume or user feedback suggests a form is needed, revisit in Stage 5.
- **Newsletter signup:** Not built into homepage or article template. Decide in Stage 5 whether Insights articles should drive email-list signups, and if so where the signup UI lives (likely bottom of Insights index, not every article).
- **Insights preview auto-population:** The two article cards on the homepage are currently hand-edited. When Stage 5 builds the Insights system, consider whether a small build script should auto-pull the two most recent articles into the homepage preview.
- **Hero imagery:** Homepage launched as pure-typography hero. Revisit only if feedback suggests it feels thin.
- **Author pages (NEW, Stage 4):** Named-author JSON-LD currently references a `Person` by name but doesn't link to a dedicated author page. For maximum AEO lift each named author should eventually have their own page at `/en/authors/[name].html` with bio, credentials, and list of their articles. Deferred to Stage 9 (template hardening) — not blocking for launch. Google and Perplexity read the JSON-LD regardless.
- **Share image (Open Graph image) (NEW, Stage 4):** Template has the `og:image` meta tag commented out. When the user starts publishing articles, each should ideally have a 1200×630 px social share image. Workflow for producing these (simple template in Canva/Figma) to be documented in Stage 7.
- **Further-reading auto-population (NEW, Stage 4):** The three further-reading cards are hand-picked per article. If article count grows large (20+ articles), consider a small build script to suggest candidates. Not urgent.
- **Reading-time accuracy (NEW, Stage 4):** Currently hand-typed. If the user finds this tedious at volume, a tiny JS helper could calculate it from word count on page load. Deferred — first gauge whether hand-typing is actually annoying in practice.
- **Article-template header/footer drift (NEW, Stage 4):** When user edits the header/footer on homepage (e.g. renames firm), they must also edit the article-template AND every cloned article. This is the same concern as the build-step question above — same parking spot, same decision point (Stage 7 or 9).
- **Marquee ticker content (NEW, Stage 4 → Stage 5):** Deployment confirmed for Insights index. Exact content still to be decided — options include: rotating latest article titles, publication cadence signal ("new insight every fortnight"), or topic tags drifting past. First decision of Stage 5.

---

## 📝 CONTEXT HANDOFF NOTES

Subtle things about the user and project that aren't formal decisions but are worth Claude remembering across chats.

- **User's coding level:** Zero coding experience. Needs plain English explanations, not developer shorthand.
- **User's priority order:** (1) Ease of self-editing with human-readable comments, (2) Rich visual/animation quality, (3) Reusability as template, (4) SEO and AI-search optimization, (5) Multi-language readiness.
- **User's communication style:** Prefers honest, direct answers — including being told when scope has grown or when an earlier plan needs adjusting. Appreciates being warned about tradeoffs upfront. Asks sharp, good questions (e.g., asking to see the "professional" set alongside the "warm" set before committing to a palette; asking whether choosing B now locks them in forever) — don't assume, explain.
- **User's aesthetic sensibility confirmed:** Chose the confident, distinctive options over the safest ones (Instrument Serif over safer Fraunces; 2+3 motion combo over minimal motion; Option B homepage over safer Option A). Willing to be bolder where it improves quality. Don't over-apologize or over-caveat in future stages.
- **Existing assets:** User has an initial HTML file with warm peach palette, professional services / Thailand business theme. Warm peach has been superseded by Navy & Warm Stone palette.
- **User's business context:** Professional services firm in Thailand, serving foreign and local enterprises. Client examples from UK, USA, Japan. Core offering is the full landing-and-operating stack for foreigners entering Thailand — tax/accounting/audit + legal/regulatory + practical onboarding (visas, permits, company setup, banking introductions).
- **Editor environment:** User will likely use GitHub's browser editor. Design navigation comments to work well there (no assumption of code-folding features).
- **Memory setting:** User has not enabled Claude's Memory feature. PROJECT-STATUS.md is the primary context-carrying mechanism between chats.
- **User values ownership:** Rejected "hidden folder" approach in favor of "read-and-understand" — clear signal that user wants genuine understanding and control over the full template, not convenient opacity.
- **Working pattern that works well:** Show options visually → give honest recommendation with pros/cons → let user choose. Ask nested decisions one at a time, not all at once. Repeat for each major decision (homepage structure → marquee → hero copy). User explicitly appreciates this rhythm.
- **User will push back when the process slips:** When Claude rewrote PROJECT-STATUS.md in a condensed format instead of preserving the existing structure, user immediately flagged it: *"in project status file you cut manything please use the same format and keep the information safe not delting things but update from it."* Lesson: this file is the user's scaffolding system — preserve its structure literally, add new content into existing sections rather than summarizing or rewriting.
- **User asks practical "can I change it later" questions:** When offered structural options, user asked whether they could change the homepage structure later. Answer them concretely with what's easy, what's medium, and what's hard — not just "yes, of course." Build future deliverables with this in mind (clear section markers, commented-out optional blocks, zero hidden coupling).
- **User thinks ahead about SEO / AEO impact (NEW, Stage 4):** When asked about bylines, user paused and explicitly said *"i think about how this will effect the SEO and AEO"* rather than picking the simpler option. Signal: the user takes AEO seriously as a real strategic lever, not a nice-to-have. Bring AEO reasoning into future decisions proactively (Stage 5 search UI, Stage 6 schema-org structured data, Stage 7 llms.txt, Stage 9 author pages) — they'll appreciate the upfront reasoning and will make better decisions for it.

---

## 🔄 CHANGE LOG

Every time this file is updated, a one-line note is added here so you can see how the plan has evolved.

| Date | Change |
|------|--------|
| 24 Apr 2026 | File created. Nine-stage roadmap locked in. Stage 1 ready to begin. |
| 24 Apr 2026 | Stage 1 complete. Architecture locked, multi-language-ready structure chosen (Approach 3), `/core/` changed from hidden to fully-commented read-and-understand zone, language switcher to activate only when additional languages go live. Ready for Stage 2. |
| 24 Apr 2026 | Stage 2 complete. Design system locked: Navy & Warm Stone palette, Instrument Serif + Inter typography, 4-based doubling spacing scale, Editorial flourish + Ambient life motion philosophy. `theme.css` and `motion.css` written with full plain-English commenting. Ready for Stage 3. |
| 24 Apr 2026 | Stage 3 complete. Homepage structure locked (Option B — 7 sections, Editorial + Trust Layer). Marquee OFF on homepage. Hero copy finalized (blend of Warm & Specific — "Thailand, made straightforward"). `/en/index.html` built with realistic-but-marked placeholders; `/core/animations.js` built with all five motion helpers respecting prefers-reduced-motion. New homepage content map section added to this file. Ready for Stage 4. |
| 24 Apr 2026 | PROJECT-STATUS.md restored to full original format after user flagged that the prior update had condensed/dropped sections. Lesson captured in handoff notes: preserve this file's structure literally across sessions; add into existing sections rather than rewriting. |
| 24 Apr 2026 | Stage 4 complete. Article taxonomy decision: NO categories — chronological feed with search. Byline decision: both variants available per article with full JSON-LD for both (named-author `@type: Person`, firm-authored `@type: Organization`). Reading time: shown, hand-typed. Marquee ticker confirmed for Stage 5 deployment on Insights index. `/en/posts/article-template.html` built — richly commented, five colour-coded comment tiers (🟢🔵🟡🔴📎), kitchen-sink example body showing every block type (drop-cap paragraph, H2/H3, lists, callout, pull quote, block quote, image+caption, table), soft contact CTA, further-reading grid. New "Article Template Map" section added to this file. Ready for Stage 5. |

---

## ▶️ HOW TO RESUME WORK WITH CLAUDE

When you open a new chat:

1. Start your first message with: *"Here's our project status — please catch up."*
2. Paste this entire file below that sentence.
3. Claude will read it, confirm the current stage, and tell you what's next.
4. Work through that stage.
5. At the end, Claude gives you an updated version of this file.
6. Replace the old file in your GitHub repo with the new one.

That's the whole system. Simple, no tools, no accounts, no subscriptions.
