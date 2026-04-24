# 📋 PROJECT STATUS — Website Template Build

> **How to use this file:**  
> At the start of every new chat with Claude, paste the contents of this file into your first message. Claude will instantly know exactly where we are, what's been decided, and what to do next. At the end of each session, Claude will give you an updated version — replace this file with the new one.

---

## 🎯 CURRENT STATUS

**Stage:** Stage 1 — Planning & Architecture  
**Status:** Ready to begin  
**Last Updated:** 24 April 2026  
**Next Action:** Claude to present the proposed folder structure and config file layout. User to review and approve before any code is written.

---

## 🗺️ THE FULL ROADMAP

Nine stages from start to finished reusable template. Status markers:
- ⬜ Not started
- 🟨 In progress
- ✅ Done

| # | Stage | Status | One-line summary |
|---|-------|--------|------------------|
| 1 | Planning & Architecture | 🟨 In progress | Agree on folder structure, file responsibilities, and config schema |
| 2 | Design System & Theme | ⬜ Not started | Build the shared colors, fonts, spacing, and animation library |
| 3 | Homepage (index.html) | ⬜ Not started | Rebuild homepage with config block, heavy comments, and full animation suite |
| 4 | Article Template | ⬜ Not started | Reusable template for knowledge-sharing articles |
| 5 | Knowledge Index Page | ⬜ Not started | The "library view" listing all articles |
| 6 | SEO & AI-Search Layer | ⬜ Not started | Meta tags, JSON-LD structured data, sitemap, robots.txt, llms.txt |
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
| 24 Apr 2026 | SEO and AI-search (AEO/GEO) optimization baked in from day one, not bolted on later |
| 24 Apr 2026 | User wants rich, lively animations and modern visual effects comparable to top-tier website builders |
| 24 Apr 2026 | User edits in HTML directly — no visual UI builder needed |
| 24 Apr 2026 | AI-safe zoning is a hard requirement — AI edits must be physically restricted to content zones |
| 24 Apr 2026 | Working rhythm: one chat per stage, fresh chat between stages, PROJECT-STATUS.md as the bridge |

---

## 🅿️ PARKED ITEMS / OPEN QUESTIONS

Things we noticed but chose to handle later. Nothing gets forgotten.

- **Build step (optional):** Whether to use a small build script to avoid copy-pasting shared header/footer into every article file. Decision deferred until Stage 4.
- **Theme variants:** Pre-built alternate color schemes (Warm Peach / Professional Blue / Minimal Monochrome) to be built in Stage 9 during template hardening.
- **Analytics slot:** Location in config for pasting Google Analytics / Plausible / Umami tracking code — to be added in Stage 6.
- **Domain setup:** User hasn't confirmed whether a domain is registered yet. Relevant for Stage 6 SEO setup.
- **Future site types:** User hasn't specified whether future sites built from this template will all be professional services or span different industries. Affects Stage 9 flexibility design.

---

## 📝 CONTEXT HANDOFF NOTES

Subtle things about the user and project that aren't formal decisions but are worth Claude remembering across chats.

- **User's coding level:** Zero coding experience. Needs plain English explanations, not developer shorthand.
- **User's priority order:** (1) Ease of self-editing with human-readable comments, (2) Rich visual/animation quality, (3) Reusability as template, (4) SEO and AI-search optimization.
- **User's communication style:** Prefers honest, direct answers — including being told when scope has grown or when an earlier plan needs adjusting. Appreciates being warned about tradeoffs upfront.
- **Existing assets:** User already has an initial HTML file (warm peach palette, professional services / Thailand business theme). Current file structure uses one large commented HTML file — being replaced by the new template architecture.
- **User's business context:** Professional services firm in Thailand, serving foreign and local enterprises (clients mentioned include UK, USA, Japan).
- **Editor environment:** Unknown — not yet confirmed whether user edits in VS Code, Notepad, or another tool. Relevant for how navigation comments are structured.
- **Memory setting:** User has not enabled Claude's Memory feature. PROJECT-STATUS.md is the primary context-carrying mechanism between chats.

---

## 🔄 CHANGE LOG

Every time this file is updated, a one-line note is added here so you can see how the plan has evolved.

| Date | Change |
|------|--------|
| 24 Apr 2026 | File created. Nine-stage roadmap locked in. Stage 1 ready to begin. |

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
