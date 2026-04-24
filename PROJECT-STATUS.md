# 📋 PROJECT STATUS — Website Template Build

> **How to use this file:**  
> At the start of every new chat with Claude, paste the contents of this file into your first message. Claude will instantly know exactly where we are, what's been decided, and what to do next. At the end of each session, Claude will give you an updated version — replace this file with the new one.

---

## 🎯 CURRENT STATUS

**Stage:** Stage 2 — Design System & Theme  
**Status:** ✅ Complete  
**Last Updated:** 24 April 2026  
**Next Action:** Start a fresh chat for Stage 3 (Homepage). Paste this file into the first message. Claude will begin by asking about homepage content priorities — specifically, which sections the homepage should include (hero + services + insights + about + contact, or a different mix), whether you want the marquee ticker on the homepage or off, and roughly what copy/text should go in the hero so the final build feels real rather than generic.

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
| 3 | Homepage (index.html) | ⬜ Ready to start | Rebuild homepage with config block, heavy comments, and full animation suite |
| 4 | Article Template | ⬜ Not started | Reusable template for knowledge-sharing articles |
| 5 | Knowledge Index Page | ⬜ Not started | The "library view" listing all articles |
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
│   ├── index.html
│   ├── knowledge.html
│   └── posts/
│       ├── article-template.html
│       └── first-article.html
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
│   └── animations.js            ← Will be written in Stage 3 (scroll triggers, cursor glow, counters, parallax)
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

### What still needs JavaScript (coming in Stage 3)
The CSS is complete, but four interactive behaviors need small JS helpers, which will live in `/core/animations.js`:
1. Scroll-trigger observer (to add `in-view` class to `[data-animate]` elements as they enter the viewport)
2. Cursor-position tracker for button glow (updates `--x` and `--y` on mouse move)
3. Cursor parallax for hero headlines (updates transform on mouse move)
4. Scroll progress bar width updater
5. Stats counter animation (counting up from 0 to target value)

---

## 🅿️ PARKED ITEMS / OPEN QUESTIONS

Things we noticed but chose to handle later. Nothing gets forgotten.

- **Build step (optional):** Whether to use a small build script to avoid copy-pasting shared header/footer into every article file. Decision deferred until Stage 4.
- **Theme variants:** Pre-built alternate color schemes (Warm Peach / Professional Blue / Minimal Monochrome) to be built in Stage 9 during template hardening. Note: current Navy & Warm Stone palette could easily be re-skinned by changing the 5 brand color variables in `theme.css`.
- **Analytics slot:** Location in config for pasting Google Analytics / Plausible / Umami tracking code — to be added in Stage 6.
- **Domain registration:** User planning to register but hasn't yet. Will need to be filled into SEO config once registered. Relevant for Stage 6.
- **Translation workflow:** When Thai and Chinese are activated, user will need to decide on translation method (human translator / AI-assisted / hybrid). Not urgent until Phase 2.
- **Japanese as 4th language:** User has Japanese clients — Japanese could be added later as a 4th language. Architecture already supports adding more languages. Font stack already includes Noto JP.
- **Browser language auto-detect:** Root `index.html` could auto-detect visitor's browser language and redirect accordingly. Decision deferred until Thai/Chinese are activated.
- **Marquee ticker per-page toggle:** Whether the ticker shows on every page or only on specific pages — to be decided per-page in Stages 3–5 as pages are built.
- **Hero imagery:** Whether the homepage hero has a background image, an illustration, or is pure typography. Will be decided when we build the homepage in Stage 3.

---

## 📝 CONTEXT HANDOFF NOTES

Subtle things about the user and project that aren't formal decisions but are worth Claude remembering across chats.

- **User's coding level:** Zero coding experience. Needs plain English explanations, not developer shorthand.
- **User's priority order:** (1) Ease of self-editing with human-readable comments, (2) Rich visual/animation quality, (3) Reusability as template, (4) SEO and AI-search optimization, (5) Multi-language readiness.
- **User's communication style:** Prefers honest, direct answers — including being told when scope has grown or when an earlier plan needs adjusting. Appreciates being warned about tradeoffs upfront. Asks sharp, good questions (e.g., asking to see the "professional" set alongside the "warm" set before committing to a palette) — don't assume, explain.
- **User's aesthetic sensibility confirmed:** Chose the confident, distinctive options over the safest ones (Instrument Serif over safer Fraunces; 2+3 motion combo over minimal motion). Willing to be bolder where it improves quality. Don't over-apologize or over-caveat in future stages.
- **Existing assets:** User has an initial HTML file with warm peach palette, professional services / Thailand business theme. Warm peach has been superseded by Navy & Warm Stone palette.
- **User's business context:** Professional services firm in Thailand, serving foreign and local enterprises. Client examples from UK, USA, Japan.
- **Editor environment:** User will likely use GitHub's browser editor. Design navigation comments to work well there (no assumption of code-folding features).
- **Memory setting:** User has not enabled Claude's Memory feature. PROJECT-STATUS.md is the primary context-carrying mechanism between chats.
- **User values ownership:** Rejected "hidden folder" approach in favor of "read-and-understand" — clear signal that user wants genuine understanding and control over the full template, not convenient opacity.
- **Stage 2 working pattern that worked well:** Show options visually → give honest recommendation with pros/cons → let user choose. Repeat for each nested decision (feel → palette → typography → motion). User appreciated being asked to compare "professional" palette set alongside the "warm" set before committing. Use this same pattern in Stage 3.

---

## 🔄 CHANGE LOG

Every time this file is updated, a one-line note is added here so you can see how the plan has evolved.

| Date | Change |
|------|--------|
| 24 Apr 2026 | File created. Nine-stage roadmap locked in. Stage 1 ready to begin. |
| 24 Apr 2026 | Stage 1 complete. Architecture locked, multi-language-ready structure chosen (Approach 3), `/core/` changed from hidden to fully-commented read-and-understand zone, language switcher to activate only when additional languages go live. Ready for Stage 2. |
| 24 Apr 2026 | Stage 2 complete. Design system locked: Navy & Warm Stone palette, Instrument Serif + Inter typography, 4-based doubling spacing scale, Editorial flourish + Ambient life motion philosophy. `theme.css` and `motion.css` written with full plain-English commenting. Ready for Stage 3. |

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
