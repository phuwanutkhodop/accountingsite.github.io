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
- Font: Instrument Serif for headings, Inter for body. No other fonts.
- Colors: Navy and Soft Linen palette only. No new colors without design discussion.
- No backend features. This is a static site — no servers, no databases.
- Read every file before editing it. Never guess what is already in a file.
- Do not write code in the first response of a new stage — ask questions first.

## File structure
```
accountingsite/
├── CLAUDE.md              ← you are here (auto-loaded briefing)
├── PROJECT-STATUS.md      ← read this first every session
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
        ├── articles.json          ← add new articles here
        ├── ARTICLES-README.txt    ← guide for adding articles
        └── article-template.html
```

## Current stage
See PROJECT-STATUS.md for the current stage. As of last update: Stage 5 complete, Stage 6 (sub-pages) is next.

## User profile
- Non-technical user. Avoid jargon. Explain in plain language.
- User communicates in English. Site has English pages; Thai version may come later.
- User owns an accounting firm.
