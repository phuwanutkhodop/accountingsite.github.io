# 📋 PROJECT STATUS — Website Template Build

> **How to use this file:**  
> At the start of every new chat with Claude, paste the contents of this file into your first message. Claude will instantly know exactly where we are, what's been decided, and what to do next. At the end of each session, Claude will give you an updated version — replace this file with the new one.

---

## 🎯 CURRENT STATUS

**Stage:** Stage 1 — Planning & Architecture  
**Status:** ✅ Complete  
**Last Updated:** 24 April 2026  
**Next Action:** Start a fresh chat for Stage 2 (Design System & Theme). Paste this file into the first message. Claude will begin by asking about overall design feel preferences (premium calm / energetic modern / minimal sharp / warm welcoming) and whether to keep the warm peach palette or explore alternatives.

---

## 🗺️ THE FULL ROADMAP

Nine stages from start to finished reusable template. Status markers:
- ⬜ Not started
- 🟨 In progress
- ✅ Done

| # | Stage | Status | One-line summary |
|---|-------|--------|------------------|
| 1 | Planning & Architecture | ✅ Done | Folder structure, file responsibilities, and multi-language-ready architecture locked in |
| 2 | Design System & Theme | ⬜ Ready to start | Build shared colors, fonts, spacing, and animation library |
| 3 | Homepage (index.html) | ⬜ Not started | Rebuild homepage with config block, heavy comments, and full animation suite |
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
├── 📁 theme/                    ← Shared design system
│   ├── theme.css
│   └── motion.css
│
├── 📁 core/                     ← Read-and-understand (fully commented)
│   ├── components.html
│   ├── config-loader.js
│   └── animations.js
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

## 🅿️ PARKED ITEMS / OPEN QUESTIONS

Things we noticed but chose to handle later. Nothing gets forgotten.

- **Build step (optional):** Whether to use a small build script to avoid copy-pasting shared header/footer into every article file. Decision deferred until Stage 4.
- **Theme variants:** Pre-built alternate color schemes (Warm Peach / Professional Blue / Minimal Monochrome) to be built in Stage 9 during template hardening.
- **Analytics slot:** Location in config for pasting Google Analytics / Plausible / Umami tracking code — to be added in Stage 6.
- **Domain registration:** User planning to register but hasn't yet. Will need to be filled into SEO config once registered. Relevant for Stage 6.
- **Translation workflow:** When Thai and Chinese are activated, user will need to decide on translation method (human translator / AI-assisted / hybrid). Not urgent until Phase 2.
- **Japanese as 4th language:** User has Japanese clients — Japanese could be added later as a 4th language. Architecture already supports adding more languages.
- **Browser language auto-detect:** Root `index.html` could auto-detect visitor's browser language and redirect accordingly. Decision deferred until Thai/Chinese are activated.

---

## 📝 CONTEXT HANDOFF NOTES

Subtle things about the user and project that aren't formal decisions but are worth Claude remembering across chats.

- **User's coding level:** Zero coding experience. Needs plain English explanations, not developer shorthand.
- **User's priority order:** (1) Ease of self-editing with human-readable comments, (2) Rich visual/animation quality, (3) Reusability as template, (4) SEO and AI-search optimization, (5) Multi-language readiness.
- **User's communication style:** Prefers honest, direct answers — including being told when scope has grown or when an earlier plan needs adjusting. Appreciates being warned about tradeoffs upfront. Asks sharp, good questions (e.g., comparing SEO impact of two approaches) — don't assume, explain.
- **Existing assets:** User has an initial HTML file with warm peach palette, professional services / Thailand business theme. Will be replaced by new template architecture but design sensibility can carry forward.
- **User's business context:** Professional services firm in Thailand, serving foreign and local enterprises. Client examples from UK, USA, Japan.
- **Editor environment:** User will likely use GitHub's browser editor. Design navigation comments to work well there (no assumption of code-folding features).
- **Memory setting:** User has not enabled Claude's Memory feature. PROJECT-STATUS.md is the primary context-carrying mechanism between chats.
- **User values ownership:** Rejected "hidden folder" approach in favor of "read-and-understand" — clear signal that user wants genuine understanding and control over the full template, not convenient opacity.

---

## 🔄 CHANGE LOG

Every time this file is updated, a one-line note is added here so you can see how the plan has evolved.

| Date | Change |
|------|--------|
| 24 Apr 2026 | File created. Nine-stage roadmap locked in. Stage 1 ready to begin. |
| 24 Apr 2026 | Stage 1 complete. Architecture locked, multi-language-ready structure chosen (Approach 3), `/core/` changed from hidden to fully-commented read-and-understand zone, language switcher to activate only when additional languages go live. Ready for Stage 2. |

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
