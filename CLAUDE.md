# CLAUDE.md — Project Briefing (Auto-loaded every session)

## What this project is
An accounting firm website built as a static site hosted on GitHub Pages.
Live URL: https://phuwanutkhodop.github.io/accountingsite.github.io/en/
GitHub repo: https://github.com/phuwanutkhodop/accountingsite.github.io

## Local folder on this computer
C:\Users\User\OneDrive\Accdocsystem\accountingsite

## First thing to do every session
READ PROJECT-STATUS.md before doing anything else. It tells you:
- What stage we are on
- What was last completed
- What comes next
- What decisions are locked and must not be changed

## How to send changes to GitHub (after editing files)
Run these three commands in order:
1. git add .
2. git commit -m "brief description of what changed"
3. git push

## Key rules (never break these)
- All file paths must be relative (use ./ and ../) — never absolute paths like /en/...
- **Builder first, firm brand later (owner route correction, 2026-10-06).** The Site Builder is built and tested on a
  neutral test theme; it must stay theme-agnostic. The firm's identity (brand track #33–#36, #35 parked) is applied
  in the later firm-website effort. Do not start new brand or side-track work without the owner's explicit OK.
  Navy & Soft Linen and Instrument Serif + Inter stay retired; leave the existing hand-written pages as they are.
- **The D.A. brand is locked (owner, 2026-10-05):** logo 153, brand seal 346, and patterns 401 · 406 · 417 · 420.
  - Start at `brand/README.md`. It indexes the master files, the specs in `docs/brand/`, and the colours.
  - `brand/` holds the **original masters and is read-only**. Never edit, redraw, recolour or replace a file there.
  - Need a new size or format? Use `tools/brand/` and write the output elsewhere.
  - Ready-made PNG, PDF and compatible SVG files for Canva, PowerPoint, Word, Illustrator, Figma and print are in
    `brand/export/`. `brand/export/README.md` says which file to use where.
  - Before any commit that touches `brand/` or `tools/brand/`, run `python tools/brand/build.py --check`.
  - D A is always the full logo 153. The seal has no "CO., LTD." and no year.
- No backend features. This is a static site — no servers, no databases.
- **Builder code (decision #16, `docs/decisions/16-tech-stack.md`):** plain ES modules with no build step; Admin UI in
  Preact + htm; third-party code only from `admin/vendor/` (rebuilt with `tools/vendor/`), never from a CDN at runtime;
  `admin/engine/` stays pure (no DOM, fetch, Intl, clock or randomness) and runs unchanged in Node.
- Read every file before editing it. Never guess what is already in a file.
- Do not write code in the first response of a new stage — ask questions first.

## File structure
```
accountingsite/
├── CLAUDE.md              ← you are here (auto-loaded briefing)
├── PROJECT-STATUS.md      ← read this first every session
├── brand/               ← LOCKED brand masters (read-only) · start at brand/README.md
├── tools/brand/         ← exact toolchain that rebuilds brand/ byte for byte
├── docs/brand/          ← brand specs: logo 153, seal 346, patterns
├── core/
│   ├── animations.js
│   └── article-loader.js
├── theme/
│   ├── theme.css
│   └── motion.css
└── en/
    ├── index.html         ← homepage
    ├── knowledge.html     ← articles index
    ├── privacy.html
    ├── terms.html
    └── posts/
        ├── articles.json          ← current hand-written site only; the builder replaces it (#19)
        ├── ARTICLES-README.txt    ← guide for adding articles
        └── article-template.html
```

## Current stage
**The project pivoted on 2026-10-05.** Before building more pages, the owner wants a
**Site Builder** — a no-server, WordPress-premium-grade website builder that runs in the
browser and publishes to GitHub Pages. The real firm website will be built *with* that
builder afterwards. The existing site becomes the builder's content-and-structure test bed, on a neutral test theme (route correction, 2026-10-06).

The plan for the builder lives on the GitHub issue tracker as a **Wayfinder map**:
https://github.com/phuwanutkhodop/accountingsite.github.io/issues/1
Every session on the builder: read the map first (including its route-correction note), pick
the next unblocked **builder-core** ticket, resolve one ticket per session. See PROJECT-STATUS.md → "Site Builder effort".

## User profile
- Non-technical user. Avoid jargon. Explain in plain language.
- User communicates in English. Site has English pages; Thai version may come later.
- User owns an accounting firm.
