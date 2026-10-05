# 03 — Git-backed CMS landscape: can anything be our `/admin/`?

**Ticket:** GitHub issue #3 (Wayfinder research)
**Date:** 5 October 2026
**Author:** research agent (Claude), for the site owner and the Wayfinder planning track
**Status:** research complete; recommendation at section 4

> **Destination being measured against:** a browser-only Admin served from `/admin/` on this GitHub Pages site, that logs in with a *fine-grained GitHub personal access token* (no OAuth proxy, no worker, no cloud account), edits pages *visually, section by section*, handles three languages (EN / TH / ZH), handles images, and grows a design/preset library over time.

---

## 1. สรุปสำหรับเจ้าของกิจการ (ภาษาไทย)

1. เราสำรวจระบบจัดการเนื้อหาแบบ "เก็บไว้ใน GitHub" ที่มีอยู่แล้ว 7 ตัวหลัก + อีกหลายตัวที่พบระหว่างทาง เพื่อดูว่ามีตัวไหน "หยิบมาใช้ได้เลย" หรือไม่
2. เงื่อนไขสำคัญของเราคือ ต้องทำงานในเบราว์เซอร์ล้วน ๆ บน GitHub Pages ไม่มีเซิร์ฟเวอร์ ไม่ต้องสมัครบริการคลาวด์ และล็อกอินด้วย "โทเค็น" จาก GitHub โดยตรง
3. ผลคือ **มีเพียงตัวเดียว (Sveltia CMS) ที่ผ่านเงื่อนไข "ไม่มีเซิร์ฟเวอร์ + ล็อกอินด้วยโทเค็น"** ตัวอื่น ๆ ต้องมีเซิร์ฟเวอร์ตัวกลาง ต้องสมัครคลาวด์ หรือเป็นโปรแกรมติดตั้งบนคอมพิวเตอร์
4. แต่ Sveltia (และทุกตัวที่เหลือ) เป็นแบบ "กรอกฟอร์ม" — ไม่มีตัวไหนให้แก้หน้าเว็บแบบเห็นภาพทีละส่วน (section) อย่างที่เราต้องการ และไม่มีตัวไหนมี "คลังแบบสำเร็จรูป (preset library)" ที่เราจะต่อยอดได้ง่าย
5. เรื่องสามภาษา Sveltia ทำได้ดีที่สุดในกลุ่ม (สลับภาษาข้างกัน, แปลด้วยคลิกเดียว) แต่เป็นการแปล "ข้อมูลในไฟล์" ไม่ใช่การแก้หน้า HTML ที่เราออกแบบไว้
6. Sveltia ยังอยู่ในสถานะ "เบต้า" ดูแลโดยนักพัฒนาหลักคนเดียว แม้จะอัปเดตถี่มาก (ออกเวอร์ชันใหม่แทบทุกวัน) ซึ่งเป็นทั้งข้อดีและความเสี่ยง
7. **ข้อเสนอ: สร้าง Admin ของเราเองแบบบางเบา (BUILD)** โดย "ยืม" วิธีคิดและรูปแบบจากโครงการเหล่านี้ เช่น วิธีล็อกอินด้วยโทเค็นของ Sveltia วิธีบันทึกไฟล์ขึ้น GitHub และหน้าตาการสลับภาษา
8. ข้อดีของการสร้างเอง: ตรงกับความต้องการ 100%, ไม่ผูกกับใคร, ไม่มีค่าใช้จ่ายรายเดือน, เข้ากับกฎของโปรเจกต์ (ไม่มี backend, ไม่มีฟอนต์/สีใหม่)
9. ข้อเสีย: เราต้องดูแลเอง, ต้องระวังเรื่องความปลอดภัยของโทเค็น, และฟีเจอร์ขั้นสูง (เช่น ขั้นตอนตรวจก่อนเผยแพร่) จะไม่มีในช่วงแรก
10. ทางเลือกสำรองที่ไม่เสียอะไร: ติดตั้ง Sveltia ไว้ที่โฟลเดอร์แยก (เช่น `/admin-articles/`) สำหรับแก้ "บทความ" อย่างเดียว ระหว่างที่ Admin ของเรายังสร้างไม่เสร็จ — เรื่องนี้เปิดเป็นคำถามให้ตั๋วอื่นตัดสิน

---

## 2. Comparison table

Legend: ✅ yes · ❌ no · ◑ partial · ? could not verify from this environment (see §7)

| Candidate | Truly zero-backend on GitHub Pages? | Token (PAT) login? | Editing model | i18n model | Media | Preset-library extensibility | Licence | Health (as of 5 Oct 2026) | Needs a build? |
|---|---|---|---|---|---|---|---|---|---|
| **Sveltia CMS** | ✅ static files + GitHub API | ✅ "Use Personal Access Token" option | Forms + rich-text (Lexical); no visual page editing; no custom preview templates | ✅ strongest: multi-structure, side-by-side locales, one-click translation, `duplicate`, RTL, per-locale slugs | ✅ asset library, WebP/SVG optimiser, stock photos | ◑ custom widgets "partial"; config-driven only | MIT | Beta; v0.228.0 on 2026-10-04; 42 open issues; one lead maintainer | ❌ single `<script>` from unpkg |
| **Decap CMS** (ex-Netlify CMS) | ❌ "GitHub requires a server for authentication" | ❌ (open feature request #7545, Jul 2025) | Forms + optional React preview pane; custom widgets | ✅ `multiple_folders` / `multiple_files` / `single_file`; field `i18n: true/duplicate` | ✅ media library (+ Cloudinary/Uploadcare) | ◑ custom widgets/previews in React | MIT | Active; releases 2026-09-22; 567 open issues; "non-funded" OSS; new paid Decap Turbo | ❌ single `<script>` from unpkg |
| **Static CMS** | ❌ (Decap fork, same auth model) | ❌ | Forms | as Decap | as Decap | ◑ | MIT | **Archived 2024-09-09** | ❌ |
| **Pages CMS** | ❌ Next.js app + PostgreSQL + GitHub App | ❌ GitHub App auth | Forms | ❌ none documented | ✅ media management | ❌ | MIT | Active; v2.1.8 on 2026-06-08; repo moved to `pagescms/pagescms` | n/a (hosted or self-host server) |
| **TinaCMS** | ❌ needs TinaCloud or a self-hosted "API function" + database adapter | ❌ | ✅ visual (side-by-side) editing — **React only** (`useTina`) | ◑ directory-based or field-based patterns (guide, not a feature) | ✅ | ◑ React components as templates | Apache-2.0 | Active; tinacms@3.14.2 on 2026-10-01 | ✅ Node/Vite build; React app |
| **Keystatic** | ❌ "API routes… need to happen on the server"; Keystatic Cloud still needs the app's routes | ❌ GitHub App / Cloud | Forms + rich document field | ❌ none built in | ✅ images | ◑ React/TypeScript schema | MIT | Active commits 2026-10-01; marked "experimental"; no GitHub releases | ✅ Next.js/Astro/Remix app |
| **Publii** | n/a — desktop (Electron) app, not a browser admin | ◑ pushes to GitHub Pages with a token from the desktop | WYSIWYG posts, theme-driven | ◑ (desktop themes; not evaluated) | ✅ local | ❌ | GPL-3.0 | Active; v0.47.9 on 2026-07-23 | n/a |
| Prose.io | ❌ needs Gatekeeper OAuth server | ❌ | Markdown editor | ❌ | ◑ | ❌ | BSD-3 | Last commit 2024-02-21; "looking for new maintainers" | ❌ |
| Outstatic | ❌ Next.js + GitHub OAuth app + API routes | ❌ | Forms + Tiptap editor | ❌ | ✅ | ◑ | FSL-1.1-ALv2 (source-available, becomes Apache after 2 yrs) | Active | ✅ |
| Front Matter CMS | n/a — VS Code extension | n/a | Forms in VS Code | ◑ UI languages only | ✅ | ❌ | MIT | Maintained "for personal use"; big features need sponsorship | n/a |
| JekyllPad / GitCMS | ◑ hosted, client-side claims — **proprietary** services | ❌ GitHub OAuth | Markdown/WYSIWYG | ❌ | ✅ | ❌ | Proprietary | Commercial | n/a |

**Bottom line of the table:** exactly one project (Sveltia) meets the hard constraint "zero backend + token login". **Zero** projects offer visual, section-based editing of hand-authored static HTML pages, and none has a preset/design-library concept we could extend without forking.

---

## 3. Per-candidate notes

### 3.1 Sveltia CMS — https://github.com/sveltia/sveltia-cms

- **What it is.** "A leading Git-based headless CMS for Jamstack sites. It's open source, free, and a complete modern rewrite of Netlify CMS" — README, https://github.com/sveltia/sveltia-cms/blob/main/README.md. Describes itself as "the de facto successor to Netlify/Decap CMS" with 355 upstream issues solved (805 incl. duplicates) — same URL.
- **Zero backend?** Yes. Installation is a single script tag in `/admin/index.html`: `<script src="https://unpkg.com/@sveltia/cms/dist/sveltia-cms.js"></script>`; it "doesn't interact with the framework that builds your site" and manages content "directly via an API" — README at tag v0.98.0, https://raw.githubusercontent.com/sveltia/sveltia-cms/v0.98.0/README.md. Works with GitHub, GitLab, Gitea, Forgejo; "Does not support Azure, Bitbucket, and Git Gateway backends" — same URL.
- **Token login.** The README (v0.98.0) documents signing in "with a personal access token instead of OAuth" by clicking the small arrow next to Sign In and choosing "Use Personal Access Token"; the token is kept in local storage; the project advises it is "better to set up an OAuth client if your CMS instance is used by non-technical users" — https://raw.githubusercontent.com/sveltia/sveltia-cms/v0.98.0/README.md. The current docs page for this is https://sveltiacms.app/en/docs/backends/github (search snippet: "You can use a personal access token for authentication if you or a small team of developers are the only users… this method doesn't require setting up an OAuth app or updating the CMS configuration"; "click the 'Sign In with Token' button… the token is stored in the browser's local storage"). *Not fetched directly — see §7.* Optional OAuth path: Sveltia CMS Authenticator, a Cloudflare Workers script, MIT — https://github.com/sveltia/sveltia-cms-auth. A GitHub Discussion confirms people run it on GitHub Pages without Netlify — https://github.com/sveltia/sveltia-cms/discussions/218.
- **Editing model.** Forms per collection/field; rich-text editor "built on Lexical" with rich/raw Markdown modes; custom editor components with "current limitations on preview/multiline". **Not supported:** editorial workflow, open authoring, nested collections, custom widgets (partial), custom preview templates — https://raw.githubusercontent.com/sveltia/sveltia-cms/v0.98.0/README.md. No drag-and-drop/section/page-builder mode exists; no open issue proposes one among the top issues — https://github.com/sveltia/sveltia-cms/issues.
- **i18n.** Multiple locales shown with human-readable names; "Integrates translation services to allow translation of text fields from another locale with one click"; RTL support; localisable slugs (Hugo `translationKey`); `i18n: duplicate` for List/Object widgets; `multiple_folders_i18n_root` structure; UI follows browser language — https://raw.githubusercontent.com/sveltia/sveltia-cms/v0.98.0/README.md. Google Cloud Translation / OpenAI integration also listed there.
- **Media.** Asset library; "Built-in image optimizer for WebP and SVG" with configurable max dimensions; stock photos (Pexels, Pixabay, Unsplash); per-collection media folders; SVG/PDF preview; Cloudinary/Uploadcare "unimplemented" — same URL.
- **Licence / health.** MIT (org listing, https://github.com/orgs/sveltia/repositories). Status "currently in beta and version 1.0 (GA) is expected to ship in late 2025" (v0.98.0 README) — as of 5 Oct 2026 the latest tag is **v0.228.0 (2026-10-04)**, with v0.227.4 and v0.227.3 in the two preceding days (https://github.com/sveltia/sveltia-cms/releases.atom) — i.e. still 0.x, still pre-GA, extremely high release cadence. 42 open issues; a "1.0 RC" milestone contains "Implement Sveltia CMS Additions (user management & roles)" (#918) — https://github.com/sveltia/sveltia-cms/issues, https://github.com/sveltia/sveltia-cms/issues/918. "Created and actively maintained by an experienced UX engineer @kyoshino" — one lead maintainer (v0.98.0 README). Bundle "less than 500 KB when minified and brotlied" — same README.
- **Fit verdict.** The *only* candidate matching "no backend + token login on GitHub Pages". Misses "visual section editing" and "preset library" entirely; it edits Markdown/YAML/JSON *data*, not our hand-built HTML pages.

### 3.2 Decap CMS — https://github.com/decaporg/decap-cms

- **Zero backend?** No for GitHub. Official docs: "Because GitHub requires a server for authentication, Netlify facilitates basic GitHub authentication" — https://raw.githubusercontent.com/decaporg/decap-website/main/content/docs/github-backend.md (source of https://decapcms.org/docs/github-backend/). Alternatives are a self-run OAuth server from a long community list (Node, Go, PHP, Cloudflare Pages, AWS Lambda, Firebase, etc.) — https://raw.githubusercontent.com/decaporg/decap-website/main/content/docs/external-oauth-clients.md — or the new paid **Decap Turbo**: "hosted auth & user management… no auth server or OAuth app for you to run", free plan 1 site/1 seat, Pro from €19/month, "in public preview" with a trial "free until 15 October 2026" — https://raw.githubusercontent.com/decaporg/decap-website/main/content/docs/turbo-overview.md and https://raw.githubusercontent.com/decaporg/decap-website/main/content/turbo/_index.md.
- **Token login.** Not supported. Feature request "Support authentication with user-provided GitHub API token (without server-side auth proxy)" is **open** since 16 Jul 2025 with no maintainer response visible — https://github.com/decaporg/decap-cms/issues/7545.
- **Editing model.** Forms with widgets; a React-based custom preview pane; custom widgets — repo README (https://github.com/decaporg/decap-cms). Not a visual/section editor.
- **i18n.** Three structures (`multiple_folders`, `multiple_files`, `single_file`), `locales` + `default_locale`, field-level `i18n: true` / `duplicate` / omitted; limits: "File collections support only `structure: single_file`", "List widgets only support `i18n: true`" — https://raw.githubusercontent.com/decaporg/decap-website/main/content/docs/i18n.md.
- **Install.** Single script from `https://unpkg.com/decap-cms@^3.0.0/dist/decap-cms.js`, no build — https://raw.githubusercontent.com/decaporg/decap-website/main/content/docs/install-decap-cms.md.
- **Licence / health.** MIT; 19.4k stars; 567 open issues (https://github.com/decaporg/decap-cms). Releases on 2026-09-22 (`decap-server@3.11.3`, etc.) — https://github.com/decaporg/decap-cms/releases.atom. Maintainer in Feb 2025: "Decap is basically married to Netlify Identity… a non-funded open-source project"; on 19 Aug 2026 they reported Netlify had reversed the Identity deprecation — https://github.com/decaporg/decap-cms/discussions/7419; Netlify's original notice: https://www.netlify.com/changelog/deprecation-netlify-identity. History of the 2023 revival: https://github.com/decaporg/decap-cms/discussions/6503.
- **Fit verdict.** Fails the hard constraint (OAuth server or paid Turbo). Bundle ~3× Sveltia's.

### 3.3 Static CMS — https://github.com/StaticJsCMS/static-cms

- **Archived** 2024-09-09: "Static CMS has been archived… Decap CMS has been revitalized… there are better options" — repo README; last commits 2024-09-09 (https://github.com/StaticJsCMS/static-cms/commits.atom); final release v4.3.0 (https://github.com/StaticJsCMS/static-cms/releases). MIT. **Not a candidate.**

### 3.4 Pages CMS — https://github.com/pagescms/pagescms (moved from `pages-cms/pages-cms`, see https://github.com/pages-cms)

- **Zero backend?** No. Stack: Next.js, PostgreSQL, Drizzle ORM, GitHub App auth; self-hosting needs Postgres, a GitHub App and env vars (`DATABASE_URL`, `BETTER_AUTH_SECRET`, `CRYPTO_KEY`); "The easiest way to get started is the hosted version at app.pagescms.org" — https://raw.githubusercontent.com/pages-cms/pages-cms/main/README.md and https://github.com/pagescms/pagescms.
- **Editing / i18n / media.** Form-based collections; media management is a headline feature; no i18n feature documented in the README — same URLs. Visual editing: none.
- **Licence / health.** MIT; 4.1k stars; 50 open issues; v2.1.8 on 2026-06-08 — https://github.com/pagescms/pagescms/releases.atom.
- **Fit verdict.** Good UX but requires a server + database + GitHub App. Fails the constraint.

### 3.5 TinaCMS — https://github.com/tinacms/tinacms

- **Zero backend?** No. Self-hosting "requires a single API function to act as the backend service" deployable to "any Node.js serverless environment, such as Vercel or Netlify", with three modules: Auth Provider, Database Adapter ("MongoDB, Postgres, etc."), Git Provider; the alternative is TinaCloud ("Managed hosting alternative") — https://raw.githubusercontent.com/tinacms/docs/main/content/docs/self-hosted/overview.mdx.
- **Visual editing.** Yes — the only candidate with true side-by-side visual editing — but it "currently requires React" via the `useTina` hook; "We are currently working on adding support for other frameworks such as vue" — https://raw.githubusercontent.com/tinacms/docs/main/content/docs/contextual-editing/overview.mdx. Our site is plain HTML/JS with no React.
- **i18n.** A guide describing directory-based and field-based patterns (`{"title": {"en": "Hello", "fr": "Bonjour"}}`), not a dedicated feature — https://raw.githubusercontent.com/tinacms/docs/main/content/docs/guides/internationalization.mdx.
- **Licence / health.** Apache-2.0 (https://github.com/tinacms/tinacms/blob/main/LICENSE); tinacms@3.14.2 on 2026-10-01 (https://github.com/tinacms/tinacms/releases.atom); CLI targets Node 22/24 (https://github.com/tinacms/tinacms/releases).
- **Fit verdict.** Closest to "visual editing", furthest from "zero backend + no build".

### 3.6 Keystatic — https://github.com/Thinkmill/keystatic

- **Zero backend?** No. GitHub mode needs a GitHub App and "Make sure the host can run Node.js for Keystatic's API routes", with `KEYSTATIC_GITHUB_CLIENT_ID/SECRET` secrets — https://raw.githubusercontent.com/Thinkmill/keystatic/main/docs/src/content/pages/github-mode.mdoc. Maintainer (Dec 2023): "The API routes in the Keystatic Admin UI are doing some reads/writes on the file system (or GitHub repo), which need to happen on the server" — https://github.com/Thinkmill/keystatic/discussions/826. Keystatic Cloud removes the GitHub App setup (free up to 3 users; Pro from $10/month) but is a cloud service — https://raw.githubusercontent.com/Thinkmill/keystatic/main/docs/src/content/pages/cloud.mdoc.
- **Editing / i18n.** Forms + document field; frameworks Astro/Next.js/Remix; "It can save data locally, directly to Github, or both" — https://raw.githubusercontent.com/Thinkmill/keystatic/main/docs/src/content/pages/introduction.mdoc. No i18n feature documented.
- **Licence / health.** MIT; 2.4k stars; 167 open issues; "experimental" (https://github.com/Thinkmill/keystatic); commits 2026-10-01 (https://github.com/Thinkmill/keystatic/commits.atom); no GitHub releases (https://github.com/Thinkmill/keystatic/releases).
- **Fit verdict.** Fails the constraint; also requires a Node framework we do not use.

### 3.7 Publii — https://github.com/GetPublii/Publii

- "A desktop-based CMS for Windows, Mac and Linux"; deploys to "Netlify, Amazon S3, GitHub Pages and Google Cloud or SFTP"; GPL-3.0; v0.47.9 — https://raw.githubusercontent.com/GetPublii/Publii/master/README.md; v0.47.9 on 2026-07-23 — https://github.com/GetPublii/Publii/releases.atom. No browser admin exists. An unanswered discussion shows token-permission friction for fine-grained tokens on GitLab — https://github.com/GetPublii/Publii/discussions/2574.
- **Fit verdict.** Different category (desktop generator with its own themes). It would replace our hand-built site, not administer it.

### 3.8 Others found

- **Prose.io** — "A Content Editor for GitHub", BSD-3, 4.8k stars, "currently looking for new maintainers", last commit 2024-02-21 — https://github.com/prose/prose, https://github.com/prose/prose/commits.atom. Auth via the Gatekeeper OAuth server (MIT) — https://github.com/prose/gatekeeper. Stale; needs a server.
- **Outstatic** — Next.js dashboard, GitHub OAuth app + API routes — https://github.com/avitorio/outstatic; licence FSL-1.1-ALv2 (source-available, converts to Apache-2.0 two years after each release) — https://github.com/avitorio/outstatic/blob/canary/license.md. Fails constraint; licence less permissive.
- **Front Matter CMS** — VS Code extension, MIT, "No browser-hosted version exists"; maintainer says major features depend on sponsorship — https://github.com/estruyf/vscode-front-matter. Not a web admin.
- **JekyllPad** and **GitCMS** — proprietary hosted editors that sign in with GitHub OAuth; JekyllPad advertises "100% client-side" but is a commercial service with a free beta tier — https://docs.astro.build/en/guides/cms/jekyllpad/, https://docs.astro.build/en/guides/cms/gitcms/. Not forkable; not a base.
- **Mattrbld** — a browser-based git CMS we could not reach from this environment (https://mattrbld.com/ blocked; no public GitHub org found). Flagged for manual check in §6, not evaluated.
- **Decap Turbo** (hosted auth for Decap, see 3.2) and **Keystatic Cloud** (3.6) are cloud services, excluded by the destination.

### 3.9 Building blocks (not CMSs) relevant to "visual section editing"

- **Puck** — "The visual editor for React", MIT, 13.4k stars, v0.23.0 on 2026-08-10 (adds a "Dictionary API for translating the editor UI") — https://github.com/puckeditor/puck, https://github.com/puckeditor/puck/releases.atom. Requires React.
- **GrapesJS** — "Free and Open source Web Builder Framework", BSD-3-Clause, 26.3k stars, framework-agnostic, outputs HTML/CSS/JSON, v0.23.6 on 2026-08-26 — https://github.com/GrapesJS/grapesjs, https://github.com/GrapesJS/grapesjs/releases.atom. A free-form HTML/CSS builder — powerful, but it is the opposite of our locked design system (it lets editors invent new styles/colours).

---

## 4. Recommendation: BUY / BORROW / BUILD

### Verdict: **BUILD a thin Admin, BORROWING patterns (and optionally Sveltia's ready-made PAT flow as a stop-gap for articles).**

**Why not BUY (adopt a CMS as-is)?** The destination has two hard gates — (a) zero backend + PAT login, (b) visual section editing of our hand-authored HTML — and no project passes both. Sveltia passes (a) and fails (b); Tina passes (b) in React only and fails (a); everything else fails (a).

**Why not use one as the BASE and extend?**
- Sveltia is a Svelte application bundled into one 500 KB script; adding a section-based visual editor means forking a fast-moving 0.x codebase (three releases in two days, https://github.com/sveltia/sveltia-cms/releases.atom) maintained by one person. We would inherit a merge burden far larger than our own thin admin. Its explicit non-goals (no custom preview templates, partial custom widgets — https://raw.githubusercontent.com/sveltia/sveltia-cms/v0.98.0/README.md) are precisely the extension points we would need.
- Decap has the extension points (custom widgets, React previews) but no token login and a maintainer statement that the project is unfunded (https://github.com/decaporg/decap-cms/discussions/7419); the PAT request has sat open since July 2025 (https://github.com/decaporg/decap-cms/issues/7545). Building a PAT backend into Decap is possible (it is MIT), but we would then own a fork of a 1.5 MB React bundle to get form editing we do not want.

### Top-2 candidates and their limitations spelled out

**#1 Sveltia CMS (closest fit)**
1. Forms-only; no section/page-builder mode; no way to show *our* page as the live preview (custom preview templates unsupported) — https://raw.githubusercontent.com/sveltia/sveltia-cms/v0.98.0/README.md.
2. Edits Markdown/YAML/JSON files, not the `<section>` blocks inside `en/index.html`; using it would force us to move all page copy into data files and render it client-side (feasible — `core/article-loader.js` already does this for articles — but it is a site refactor, not an admin install).
3. No preset/design library concept; every new section type = a config change by a developer.
4. Beta (0.x) with one lead maintainer; roadmap still has "1.0 RC" items open (https://github.com/sveltia/sveltia-cms/issues/918).
5. PAT login is positioned for developers; the project itself recommends OAuth for non-technical users — https://raw.githubusercontent.com/sveltia/sveltia-cms/v0.98.0/README.md.
6. We could not read the live docs site from this environment (§7) — the PAT instructions must be re-verified by a human at https://sveltiacms.app/en/docs/backends/github before anyone relies on them.

**#2 Decap CMS (runner-up)**
1. Requires an OAuth server, Netlify, or paid Decap Turbo for GitHub login — https://raw.githubusercontent.com/decaporg/decap-website/main/content/docs/github-backend.md. This alone breaks the destination.
2. Forms-only; preview pane requires writing React components.
3. i18n has structural limits (file collections only `single_file`; list widgets only `i18n: true`) — https://raw.githubusercontent.com/decaporg/decap-website/main/content/docs/i18n.md.
4. ~1.5 MB bundle vs Sveltia's <500 KB (Sveltia README comparison, same URL as above).
5. 567 open issues and self-described lack of funding — https://github.com/decaporg/decap-cms, https://github.com/decaporg/decap-cms/discussions/7419.

### What we gain / lose either way

| | BUILD thin Admin | Adopt Sveltia as-is |
|---|---|---|
| Matches destination | Fully (we define it) | Login yes; editing model no; presets no |
| Visual section editing | Yes, by design | No |
| Trilingual | Our own locale model; must design it (borrow Sveltia's UX) | Excellent, ready today — for data files |
| Media | We must write upload/optimise ourselves (Contents API) | Ready: library, WebP/SVG optimiser, stock photos |
| Preset library | Native concept | Not a concept |
| Maintenance | Ours, forever; small surface area | Upstream handles bugs/security; but 0.x churn and config drift |
| Security | We own token storage/XSS hygiene | Same model (token in localStorage), but battle-tested by more users |
| Missing for a long time | Editorial workflow, multi-user roles, conflict handling, rate-limit handling, offline drafts | Editorial workflow (also missing in Sveltia); visual editing |
| Project rules (static only, relative paths, fonts/colours locked) | Trivially satisfied | Satisfied for hosting; admin UI uses its own look |

---

## 5. If BUILD — what to borrow from these projects

**From Sveltia (login + i18n UX):**
- The *PAT sign-in flow*: a secondary "Sign in with token" affordance, token kept in `localStorage`, clear wording that the token must have Contents read/write on this one repository only — https://raw.githubusercontent.com/sveltia/sveltia-cms/v0.98.0/README.md. GitHub's REST "Create or update file contents" endpoint requires the fine-grained permission `contents: write` — https://docs.github.com/en/rest/repos/contents (permission requirement surfaced via the `X-Accepted-GitHub-Permissions` header documented there). Fine-grained tokens are scoped per repository and expire — https://github.blog/security/application-security/introducing-fine-grained-personal-access-tokens-for-github/.
- The *side-by-side locale pane* and the two field behaviours `translate` vs `duplicate` (a phone number is duplicated; a headline is translated) — Sveltia README and Decap i18n doc (https://raw.githubusercontent.com/decaporg/decap-website/main/content/docs/i18n.md). Map directly to EN/TH/ZH.
- "Human-readable language names, not ISO codes" in the UI, and auto-detecting the editor's browser language — Sveltia README.
- Browser-side image optimisation to WebP with a max-dimension setting before commit — Sveltia README. Keeps the repo small, needs no server.
- Mobile-first admin ergonomics (floating action buttons, large targets) — Sveltia README. The owner may edit from a phone.

**From Decap (schema & structure ideas):**
- A declarative `config` that describes collections/fields — the mental model editors already know (https://raw.githubusercontent.com/decaporg/decap-website/main/content/docs/configure-decap-cms.md). For us: a *section schema* (hero, services grid, CTA, FAQ…) where each preset = schema + default copy per locale + a render template.
- The three i18n file layouts; for a JSON-driven site `single_file` (all locales in one file per page) is the simplest to commit atomically — https://raw.githubusercontent.com/decaporg/decap-website/main/content/docs/i18n.md.
- Why GitHub needs a server for OAuth, and why the PAT route is the only fully-static one — https://raw.githubusercontent.com/decaporg/decap-website/main/content/docs/github-backend.md, https://github.com/decaporg/decap-cms/issues/7545.

**From Tina (visual-editing interaction):**
- The "website and editor window sit side-by-side, showing your changes in real-time" pattern — https://raw.githubusercontent.com/tinacms/docs/main/content/docs/contextual-editing/overview.mdx. For a static site this can be an `<iframe>` of the real page with `postMessage` updates; no React needed.

**From Puck / GrapesJS (section builder shape):**
- Puck's model — components defined by *us*, editor outputs plain JSON, editor UI itself is translatable (Dictionary API) — https://github.com/puckeditor/puck/releases.atom. We would not import Puck (React), but copy the data shape: `{sections: [{type, props, locales}]}`.
- GrapesJS shows the anti-pattern for us: free-form styling invites brand drift; our builder should offer *presets only*, never colour/font pickers (CLAUDE.md rules).

**From Pages CMS / Keystatic:** the plain-language empty states and "repo-is-the-database" messaging; nothing technical to reuse (server-bound).

**Fallback worth noting:** because Sveltia is a single `<script>` with PAT login, it can coexist at a *different* path (e.g. `/admin-articles/`) to edit `en/posts/articles.json` and Markdown immediately, at zero cost, while our Admin is built — decision deferred to §6.

---

## 6. Open questions for other tickets

1. **Verify Sveltia PAT instructions by hand** at https://sveltiacms.app/en/docs/backends/github (blocked for this agent). Record exact token permissions it asks for.
2. **Interim article editor?** Should we install Sveltia at `/admin-articles/` now for `articles.json`/Markdown only, or avoid two admins? (Owner decision; UX ticket.)
3. **Content storage shape for pages.** Keep page copy inside HTML (admin edits HTML DOM and commits the file) vs. move copy to per-page JSON (`single_file` i18n layout) rendered by `core/*.js`? Affects SEO (Stage 7) — JSON-rendered text is still indexable but changes the crawl model already used for articles.
4. **Token security model.** localStorage vs sessionStorage; auto-expiry; what happens if the owner's token leaks (fine-grained tokens are repo-scoped and expiring — https://github.blog/security/application-security/introducing-fine-grained-personal-access-tokens-for-github/). Needs a short threat-model ticket.
5. **Conflict & rate-limit handling.** Contents API updates need the file's current `sha`; concurrent edits must be detected (https://docs.github.com/en/rest/repos/contents). Decap Turbo's existence shows rate limits bite real editors (https://raw.githubusercontent.com/decaporg/decap-website/main/content/docs/turbo-overview.md).
6. **Image size limits via Contents API** (base64 upload) and whether to optimise to WebP client-side first (Sveltia does) — needs a spike against https://docs.github.com/en/rest/repos/contents.
7. **Deployment latency.** GitHub Pages rebuilds after each commit; the admin needs a "published / building" indicator — Decap infers this from commit statuses (https://raw.githubusercontent.com/decaporg/decap-website/main/content/docs/github-backend.md).
8. **Mattrbld** — unreachable here; someone should check whether it is a browser-only git CMS with token auth and what licence it carries.
9. **Thai/Chinese typography in the admin** — Instrument Serif/Inter are Latin fonts (CLAUDE.md); the admin and the TH/ZH pages need a fallback stack decision without adding "new fonts" in the design sense.

---

## 7. Method and verification notes

- Research window: 5 Oct 2026. Repo health read from GitHub Atom feeds (`/releases.atom`, `/commits.atom`), which carry ISO timestamps; human-readable pages omit years.
- The research sandbox blocked these official sites: decapcms.org, sveltiacms.app, pagescms.org, tina.io, keystatic.com, getpublii.com, docs.github.com, docs.astro.build, netlify.com, mattrbld.com, jekyllpad.com. Where possible the *source files* of those docs were read from their GitHub repos instead (decaporg/decap-website, tinacms/docs, Thinkmill/keystatic, sveltia/sveltia-cms at tag v0.98.0). Claims marked "search snippet" come from search-engine excerpts of the blocked page and should be re-verified (open question 1).
- GitHub API access in this session was limited to this repository, so star/issue counts come from rendered GitHub pages and are approximate.
