# Research #4 — Publishing from the browser to GitHub Pages: token scopes, APIs, limits

**Ticket:** https://github.com/phuwanutkhodop/accountingsite.github.io/issues/4 (`wayfinder:research`)
**Date:** 5 October 2026
**Scope:** How a static Admin page served at `/admin/` on this GitHub Pages site can publish a multi-file website into the same repository using only a fine-grained personal access token (PAT), with no server and (ideally) no GitHub Actions.

> **How this was verified.** The network sandbox used for this research blocks `docs.github.com` and `github.blog`, so every GitHub Docs claim below was read from the *source* of the official documentation (the `github/docs` repository on `raw.githubusercontent.com`, branch `main`, fetched 5 Oct 2026) and from GitHub's official OpenAPI description (`github/rest-api-description`, `descriptions/api.github.com/api.github.com.json`, same date). Links point to the public `docs.github.com` page that is rendered from each source file; the source path is given in brackets so a reviewer can re-check either. Live behaviour (CORS headers, deployment records) was confirmed by calling `api.github.com` against this repository.

---

## 1. สรุปสั้นสำหรับเจ้าของกิจการ (ภาษาไทย)

1. หน้า Admin ที่อยู่บนเว็บของเรา (`/admin/`) สามารถ "กดปุ่มเดียวแล้วเผยแพร่เว็บ" ได้จริง โดยคุยกับ GitHub ตรง ๆ จากเบราว์เซอร์ ไม่ต้องมีเซิร์ฟเวอร์ของเราเอง และไม่จำเป็นต้องใช้ GitHub Actions
2. กุญแจที่ใช้คือ "โทเคน" (fine-grained personal access token) ซึ่งเราตั้งให้เปิดได้ **เฉพาะ repo เว็บไซต์นี้ repo เดียว** และให้สิทธิ์แค่ **อ่าน/เขียนไฟล์ (Contents: Read and write)** กับ **อ่านสถานะ Pages (Pages: Read-only)** เท่านั้น — ถึงโทเคนหลุด คนร้ายก็ทำได้แค่แก้ไฟล์เว็บนี้ ไม่ถึงบัญชี GitHub หรือ repo อื่น
3. การเผยแพร่หลายไฟล์พร้อมกัน (เช่น แก้ 5 หน้า + รูป 3 รูป) จะถูกรวมเป็น "1 commit" เดียวเสมอ ทำให้เว็บไม่มีช่วงที่ไฟล์ครึ่งเก่าครึ่งใหม่ และย้อนกลับเวอร์ชันก่อนได้ทั้งชุด
4. ทุกครั้งที่เผยแพร่ GitHub จะเก็บประวัติไว้ให้อัตโนมัติ หน้า Admin จึงทำปุ่ม "ย้อนกลับไปเวอร์ชันเมื่อวาน" ได้โดยไม่ต้องเก็บสำเนาเอง
5. หลังกดเผยแพร่ GitHub ใช้เวลาทำเว็บให้ขึ้นจริงปกติไม่กี่สิบวินาที ถึงราว 1–2 นาที (เอกสารบอกว่าอาจถึง 10 นาที) หน้า Admin จะเช็กสถานะให้และบอกเมื่อ "ขึ้นแล้ว"
6. ข้อจำกัดที่ต้องรู้: ไฟล์เดียวห้ามเกิน 100 MB (รูปเว็บปกติไม่ถึงอยู่แล้ว), ทั้งเว็บไม่ควรเกิน 1 GB, ปริมาณคนเข้าชมมีเพดานแบบนุ่ม 100 GB/เดือน และสร้างเว็บใหม่ได้ราว 10 ครั้ง/ชั่วโมง — เพียงพอมากสำหรับเว็บสำนักงานบัญชี
7. โทเคนเป็นเหมือนรหัสผ่าน: เราแนะนำให้เบราว์เซอร์ **ไม่จำโทเคนถาวร** (จำแค่ตอนเปิดแท็บ Admin) แล้ววางใหม่จากโปรแกรมจัดการรหัสผ่านเมื่อจะเผยแพร่ หรือเลือกโหมด "จำไว้ในเครื่องนี้" ก็ได้ถ้ายอมรับความเสี่ยงบนคอมเครื่องนั้น
8. โทเคนมีวันหมดอายุ (เลือกได้สูงสุด 366 วัน หรือ "ไม่หมดอายุ" สำหรับบัญชีส่วนตัว) ถ้าหมดอายุ หน้า Admin จะขึ้นข้อความชัด ๆ ให้ไปสร้างใบใหม่ ใช้เวลา 2 นาที ไม่มีอะไรเสียหาย
9. GitHub Pages ห้ามใช้ทำ e-commerce / SaaS เป็นหลัก แต่เว็บประชาสัมพันธ์สำนักงานบัญชีอยู่ในข่ายที่อนุญาต และต้องไม่ใส่ข้อมูลลับของลูกค้าลงเว็บเพราะ repo และเว็บเป็นสาธารณะ
10. ข้อควรระวังสำคัญที่สุด: หน้า Admin ต้องเขียนให้ปลอดช่องโหว่สคริปต์ (XSS) เพราะโทเคนอยู่ในเบราว์เซอร์ — เรื่องนี้จะคุมตอนออกแบบ Admin (ตั๋วถัดไป)

---

## 2. Recommended publish architecture

### 2.1 Decision summary

| Decision | Recommendation | Why |
|---|---|---|
| Token type | **Fine-grained PAT**, resource owner = the user's own account, repository access = *Only select repositories* → this repo | Scoped to one repo and specific permissions; GitHub recommends fine-grained over classic. [[1]](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) |
| Minimum permissions | **Contents: Read and write** + **Pages: Read-only**. Metadata: Read-only is added automatically. Nothing else. | Contents covers every read/write endpoint the Admin needs (see §2.3). Pages read covers `GET /pages` and `GET /pages/builds/latest` for "is it live?". [[2]](https://docs.github.com/en/rest/authentication/permissions-required-for-fine-grained-personal-access-tokens) |
| Multi-file write | **Git Data API** (blobs → tree → commit → update ref), one commit per publish | The Contents API writes one file per request and GitHub explicitly says concurrent Contents writes conflict; Git Data produces one atomic commit. [[3]](https://docs.github.com/en/rest/repos/contents#create-or-update-file-contents) [[4]](https://docs.github.com/en/rest/guides/using-the-rest-api-to-interact-with-your-git-database) |
| Single-file write (e.g. one JSON setting) | Contents API `PUT` is acceptable | Simpler; one file = one commit anyway. [[3]](https://docs.github.com/en/rest/repos/contents#create-or-update-file-contents) |
| Deploy mechanism | Keep **"Deploy from a branch"** (`main`, `/ (root)`) — already configured on this repo | No Actions workflow file to maintain; GitHub runs its own `pages build and deployment` run after each push. [[5]](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site) |
| "Live" detection | Poll `GET /repos/{o}/{r}/pages/builds/latest` until `status == "built"` and `commit == <our sha>`; then fetch the live URL with a cache-buster | Pages read-only permission suffices; verified live that each deploy also creates a Deployments-API record with `state: success`. [[6]](https://docs.github.com/en/rest/pages/pages) |
| Rollback | `GET /commits?path=...` or `GET /commits` for history; restore by creating a new commit whose tree is the old commit's tree (never force-push) | Keeps history linear and auditable; Contents read permission is enough to read history. [[7]](https://docs.github.com/en/rest/commits/commits) |
| Token storage | Default **sessionStorage** (per-tab, gone on close) with an opt-in "remember on this device" that stores in **localStorage**; never embed in page source | See §4. |
| GitHub Actions | **Not required.** Optional later for image optimisation / sitemap generation | See §2.6. |

### 2.2 Pre-flight (once per Admin session)

| # | Call | Purpose | Permission |
|---|---|---|---|
| P1 | `GET https://api.github.com/user` — header `Authorization: Bearer <token>`, `Accept: application/vnd.github+json`, `X-GitHub-Api-Version: 2022-11-28` | Validate token, show "signed in as …". Also read the `github-authentication-token-expiration` response header (observed live) to warn before expiry. | (any valid token) |
| P2 | `GET /repos/{owner}/{repo}` | Confirm the token can see the repo; read `default_branch`, `has_pages`. | Metadata read (automatic) [[2]](https://docs.github.com/en/rest/authentication/permissions-required-for-fine-grained-personal-access-tokens) |
| P3 | `GET /repos/{owner}/{repo}/pages` | Read `html_url`, `build_type` (`legacy` = deploy-from-branch, `workflow` = Actions), `source.branch`/`source.path`, current `status`. | Pages read [[6]](https://docs.github.com/en/rest/pages/pages) |
| P4 | `GET /rate_limit` (optional) | Show remaining quota; does **not** count against primary limit. | none [[8]](https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api) |

If P1 returns `401` → token invalid/expired/revoked → show the renewal screen (§4.4). If P2/P3 return `403`/`404` → token lacks repo access or permission → show "token needs Contents + Pages on this repo".

### 2.3 Publish sequence (Git Data API — one atomic commit)

All endpoints are under `https://api.github.com/repos/{owner}/{repo}`. Permission column is from GitHub's fine-grained permission map. [[2]](https://docs.github.com/en/rest/authentication/permissions-required-for-fine-grained-personal-access-tokens)

| # | Method + endpoint | Purpose | Permission |
|---|---|---|---|
| 1 | `GET /git/ref/heads/main` | Get the current branch head commit SHA (`object.sha`). This is the **parent** and the basis for conflict detection. | Contents read |
| 2 | `GET /git/commits/{head_sha}` | Read the head commit's `tree.sha` (used as `base_tree`). | Contents read |
| 3 | For **each changed binary file** (images, PDFs, fonts): `POST /git/blobs` body `{ "content": "<base64>", "encoding": "base64" }` → returns `sha`. Run these **sequentially or with low concurrency (≤ 3–5)** to respect secondary limits. | Upload binary content; text files can be sent inline in step 4 instead. | Contents write |
| 4 | `POST /git/trees` body `{ "base_tree": "<tree sha from 2>", "tree": [ { "path": "en/index.html", "mode": "100644", "type": "blob", "content": "<utf-8 text>" }, { "path": "assets/img/hero.webp", "mode": "100644", "type": "blob", "sha": "<blob sha from 3>" }, { "path": "en/old-page.html", "mode": "100644", "type": "blob", "sha": null } ] }` | Build the new tree in **one request**: text files inline via `content`, binaries by blob `sha`, deletions by `sha: null`. Returns new tree `sha`. GitHub returns an error if you delete a path that does not exist. [[9]](https://docs.github.com/en/rest/git/trees#create-a-tree) | Contents write |
| 5 | `POST /git/commits` body `{ "message": "Publish: <summary>", "tree": "<new tree sha>", "parents": ["<head sha from 1>"] }` | Create the commit object. Author/committer default to the token owner. [[10]](https://docs.github.com/en/rest/git/commits#create-a-commit) | Contents write |
| 6 | `PATCH /git/refs/heads/main` body `{ "sha": "<new commit sha>", "force": false }` | Move `main` to the new commit. With `force: false` GitHub only allows a fast-forward, so if someone pushed in between, this fails instead of overwriting — restart from step 1. [[11]](https://docs.github.com/en/rest/git/refs#update-a-reference) | Contents write |

Only step 6 makes anything visible; steps 3–5 create dangling objects if the Admin stops midway, which is harmless. This is the exact sequence GitHub's own guide describes for "commit a change via the REST API". [[4]](https://docs.github.com/en/rest/guides/using-the-rest-api-to-interact-with-your-git-database)

**Request budget per publish:** 2 reads + (number of binary files) + 3 writes. A publish touching 20 pages and 10 images is ~15 requests — trivially inside the 5,000/hour primary limit and the 80 content-creating requests/minute secondary limit (§3).

**Why not the Contents API for multi-file?** `PUT /contents/{path}` creates **one commit per file**, requires the existing file's blob `sha` for every update, and GitHub documents that running it in parallel with `DELETE /contents/{path}` "will conflict and you will receive errors. You must use these endpoints serially instead." [[3]](https://docs.github.com/en/rest/repos/contents#create-or-update-file-contents) That means N files → N sequential round-trips → N Pages builds → a window where the live site is half old, half new. It also burns the soft limit of 10 Pages builds per hour very quickly (§3).

### 2.4 "Is it live yet?" sequence

| # | Call | Purpose | Permission |
|---|---|---|---|
| L1 | `GET /pages/builds/latest` — poll every ~5 s, back off to 15 s after 1 min, give up after ~12 min | Response has `status` (`building` → `built`, or `errored` with `error.message`), `commit` (the SHA that was built), `duration`. Success = `status == "built" && commit == <our commit sha>`. The `page.status` enum in the OpenAPI schema is `built | building | errored`. [[6]](https://docs.github.com/en/rest/pages/pages) | Pages read |
| L2 (alternative) | `GET /deployments?environment=github-pages&sha=<our sha>` then `GET /deployments/{id}/statuses` | Verified live on this repo: each Pages publish creates a deployment in environment `github-pages`, and its latest status has `state: "success"` and `environment_url` = the live site URL. Needs **Deployments: Read-only**, so only use if you want this instead of Pages read. [[12]](https://docs.github.com/en/rest/deployments/deployments) | Deployments read |
| L3 | `fetch("https://<owner>.github.io/<repo>/en/index.html?v=<commit sha>", { cache: "no-store" })` and compare a marker (e.g. a `<meta name="x-build" content="<sha>">` the Admin writes into every page) | Confirms the CDN is actually serving the new bytes. GitHub Pages responses carry `Cache-Control: max-age=600` (10 min) per community observation, so a plain reload may show stale content; the query string bypasses that. [[13]](https://dev.to/jangwook_kim_e31e7291ad98/your-last-deploy-reset-every-cache-validator-on-the-site-4dd3) | none (public URL) |

Expected latency: this repo's last two `pages build and deployment` runs took **40 s and 42 s** end-to-end (observed via `GET /actions/runs`, 1 May and 25 May 2026). GitHub's documented upper bound is "up to 10 minutes", and deployments time out after 10 minutes. [[14]](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits) [[15]](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site)

Two gotchas from the docs: (a) a branch publish only happens when the pusher has **admin permission and a verified email** — true for the owner's own PAT; (b) commits made by a GitHub Actions workflow using `GITHUB_TOKEN` do **not** trigger a Pages build. [[5]](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)

### 2.5 History and rollback sequence

| # | Call | Purpose | Permission |
|---|---|---|---|
| H1 | `GET /commits?sha=main&per_page=50` | Site-wide version list (message, author, date, sha). Paginate with `page`. | Contents read [[7]](https://docs.github.com/en/rest/commits/commits) |
| H2 | `GET /commits?path=en/about.html&per_page=20` | Per-page history ("versions of the About page"). `path` filters to commits touching that file. | Contents read [[7]](https://docs.github.com/en/rest/commits/commits) |
| H3 | `GET /commits/{sha}` | What changed in one publish: `files[]` with `status`, `additions`, `deletions`, `patch`. Up to 300 files inline, paginated to 3,000. | Contents read [[7]](https://docs.github.com/en/rest/commits/commits) |
| H4 | `GET /contents/{path}?ref=<old sha>` with `Accept: application/vnd.github.raw+json` | Preview / fetch an old version of one file (raw media type needed for files > 1 MB; endpoint supports up to 100 MB that way). | Contents read [[3]](https://docs.github.com/en/rest/repos/contents#get-repository-content) |
| H5 | **Rollback whole site:** `GET /git/commits/{old sha}` → take its `tree.sha` → `POST /git/commits { tree: <old tree>, parents: [<current head>], message: "Rollback to <date>" }` → `PATCH /git/refs/heads/main { sha, force: false }` | Produces a *new* forward commit that reproduces the old state; history is preserved and Pages rebuilds normally. Never use `force: true`. | Contents write [[11]](https://docs.github.com/en/rest/git/refs#update-a-reference) |
| H6 | **Rollback one file:** `GET /contents/{path}?ref=<old sha>` → include that content in a normal publish (§2.3). | Partial restore. | Contents read+write |

### 2.6 Can GitHub Actions be avoided entirely?

**Yes, for publishing.** With "Deploy from a branch", GitHub itself runs an internal `pages build and deployment` workflow (`dynamic/pages/pages-build-deployment` on this repo); the docs state the site "will always be deployed with a GitHub Actions workflow run" even when you did not write one. [[5]](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site) You do not create, maintain or pay for it (Actions minutes are free on public repositories). [[16]](https://docs.github.com/en/billing/concepts/product-billing/github-actions)

Two consequences of this choice:

* **Jekyll runs by default** on branch publishes. Files/folders starting with `_` are dropped unless you add an empty **`.nojekyll`** file at the publishing root. This repo does **not** currently have one — the Admin should write it on first publish so Jekyll never eats a `_fonts/` or `_data/` folder, and so the build skips straight to deploy. [[15]](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site) [[5]](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)
* **Build quota**: 10 builds/hour soft limit applies to branch publishes; it does *not* apply to custom Actions workflows. [[14]](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits) One commit per publish keeps us well under it.

**When a custom Actions workflow becomes worth it (later tickets):**

| Need | Browser-only? | Actions useful? |
|---|---|---|
| Resize/convert images to WebP, strip EXIF | Yes — Canvas/`OffscreenCanvas` + `createImageBitmap` in the browser before upload. Keeps repo small. | Optional fallback for very large originals. |
| `sitemap.xml`, `robots.txt`, RSS | Yes — Admin knows every page; generate client-side and include in the same commit. | Only if content is also edited outside the Admin. |
| Minify HTML/CSS/JS | Yes (small libs) — but may not be worth it on a static brochure site. | Convenient but not needed. |
| Scheduled publish ("go live at 09:00") | **No** — a browser cannot act while closed. | Yes: a scheduled workflow that moves a ref. |
| Link checking, HTML validation on every publish | Partly. | Yes, as a non-blocking report. |
| Thai/Chinese font subsetting | Hard in browser. | Yes. |

If a workflow is ever added, the token needs **Workflows: write** to touch `.github/workflows/*` — the permission map shows `PUT /contents/{path}` and `PATCH /git/refs/{ref}` require it when workflow files are involved. [[2]](https://docs.github.com/en/rest/authentication/permissions-required-for-fine-grained-personal-access-tokens) Do **not** grant it by default.

### 2.7 CORS from a `github.io` origin

GitHub states: "The REST API supports cross-origin resource sharing (CORS) for AJAX requests from any origin." The documented preflight allows `Authorization, Content-Type, If-Match, If-Modified-Since, If-None-Match, If-Unmodified-Since, X-Requested-With` headers and methods `GET, POST, PATCH, PUT, DELETE`, with `Access-Control-Max-Age: 86400`. [[17]](https://docs.github.com/en/rest/using-the-rest-api/using-cors-and-jsonp-to-make-cross-origin-requests)

Verified live (5 Oct 2026) with `Origin: https://phuwanutkhodop.github.io`: the response carried `Access-Control-Allow-Origin: *` and `Access-Control-Expose-Headers: ETag, Link, Location, Retry-After, X-GitHub-OTP, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Used, X-RateLimit-Resource, X-RateLimit-Reset, …`, so the Admin can read rate-limit and `Retry-After` headers from JavaScript. Practical notes:

* Use `Authorization: Bearer <token>`; this header is in the allowed list so the browser preflight succeeds.
* The optional `X-GitHub-Api-Version` header is **not** in the documented allow-list; the live preflight on the generic doc shows only the headers above. Either omit it (the API defaults to `2022-11-28`, visible in `X-Github-Api-Version-Selected`) or test the preflight in the prototype ticket before relying on it.
* User site vs project site does not matter for CORS: both are `https://<owner>.github.io` origins (a project site's path is irrelevant to the origin). The only difference is that a user site must live in a repo named `<owner>.github.io` and there can be only one per account. [[18]](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages)

---

## 3. Limits table

| Limit | Value | Impact on the Admin | Source |
|---|---|---|---|
| Fine-grained PAT max lifetime | Any number of days 1–366, or **no expiration** for a personal resource owner; org/enterprise owners may cap it (org default policy 366 days) | Offer "1 year" as default; show the expiry date in the Admin | [[1]](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) [[19]](https://docs.github.com/en/organizations/managing-programmatic-access-to-your-organization/setting-a-personal-access-token-policy-for-your-organization) [[20]](https://github.blog/changelog/2024-10-18-new-pat-rotation-policies-preview-and-optional-expiration-for-fine-grained-pats/) |
| Fine-grained PATs per account | 50 | Irrelevant | [[1]](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) |
| Token auto-revocation | Expired tokens are revoked; tokens pushed to a public repo are revoked automatically; tokens **unused for one year** are revoked | Never commit the token into the site; "no expiration" still dies after 1 year idle | [[21]](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/token-expiration-and-revocation) |
| Primary REST rate limit (PAT) | 5,000 requests/hour (shared with apps acting for the user) | A publish uses ~5–30 requests | [[8]](https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api) |
| Unauthenticated | 60 requests/hour per IP | Only relevant for the public-site cache-bust fetch (not api.github.com) | [[8]](https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api) |
| Secondary limits | ≤ 100 concurrent requests; ≤ 900 points/min (GET = 1, POST/PUT/PATCH/DELETE = 5); ≤ 80 content-generating requests/min and ≤ 500/hour; ≤ 90 s CPU per 60 s | Upload blobs with concurrency ≤ 5; 80 writes/min ≈ 75 blobs + tree + commit + ref per minute max | [[8]](https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api) |
| On 403/429 | Honour `retry-after` (seconds) or `x-ratelimit-reset` (epoch); else wait ≥ 60 s with exponential backoff | Admin must implement this, not hammer | [[8]](https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api) |
| Hard per-file size in a repo | 100 MiB blocked; Git warns ≥ 50 MiB; web-UI upload ≤ 25 MiB | Admin should refuse files > 25 MB and warn > 5 MB | [[22]](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github) |
| `GET /git/blobs/{sha}` | "supports blobs up to 100 megabytes" | Reading back any site asset is fine | [[23]](https://docs.github.com/en/rest/git/blobs) |
| `GET /contents/{path}` | JSON response for files ≤ 1 MB; 1–100 MB needs `application/vnd.github.raw+json` (or `.object`) media type | Use raw media type when previewing old versions | [[3]](https://docs.github.com/en/rest/repos/contents#get-repository-content) [[24]](https://github.blog/changelog/2022-05-03-increased-file-size-limit-when-retrieving-file-contents-via-rest-api/) |
| `PUT /contents/{path}` / `POST /git/blobs` upload size | No explicit number in the official docs; the 100 MiB repository block applies. Community reports of 422 errors on ~50 MB+ uploads | Keep assets small; images for a brochure site are < 1 MB each | [[25]](https://github.com/orgs/community/discussions/155856) |
| Base64 overhead | Base64 encodes 3 bytes as 4 characters → request body ≈ 1.33 × file size (+ JSON quoting) | A 5 MB image is a ~6.7 MB request; still fine | (arithmetic; both `POST /git/blobs` and `PUT /contents` accept `base64` encoding [[23]](https://docs.github.com/en/rest/git/blobs) [[3]](https://docs.github.com/en/rest/repos/contents#create-or-update-file-contents)) |
| `GET /git/trees/{sha}?recursive=1` | 100,000 entries / 7 MB max | Irrelevant at our scale | [[9]](https://docs.github.com/en/rest/git/trees) |
| `GET /commits/{sha}` file list | 300 files inline, paginated up to 3,000 | A "what changed" view works for any realistic publish | [[7]](https://docs.github.com/en/rest/commits/commits) |
| Pages: repo size | Recommended ≤ 1 GB | Store optimised images only | [[14]](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits) |
| Pages: published site size | ≤ 1 GB (hard) | Same | [[14]](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits) |
| Pages: bandwidth | *Soft* 100 GB/month | Fine for an accounting firm; add a CDN only if exceeded | [[14]](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits) |
| Pages: builds | *Soft* 10 builds/hour (branch deploys only; not for custom Actions workflows) | One commit per publish; debounce "Publish" button | [[14]](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits) |
| Pages: deploy timeout | 10 minutes | Give up polling at ~12 min and show the error | [[14]](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits) |
| Pages: propagation | "up to 10 minutes" documented; ~40 s observed on this repo | Show a progress state, not a spinner | [[15]](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site) |
| Pages: build requests via API | One concurrent build per repo and per requester; extra requests are queued | Rarely needed (push already triggers a build) | [[6]](https://docs.github.com/en/rest/pages/pages) |
| Pages: acceptable use | Not for sites "primarily directed at … commercial transactions" or SaaS; no sensitive transactions (passwords, card numbers); sites are public even from private repos | Brochure/knowledge site is fine; the Admin's token must never be in the repo | [[14]](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits) [[5]](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site) |
| User site vs project site | One user site per account (`<owner>.github.io` repo); one project site per repo at `<owner>.github.io/<repo>` | This site is a project site; nothing in the API differs | [[18]](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages) |

---

## 4. Token storage in the browser — risk analysis and recommendation

### 4.1 Threat model for a single-owner tool

> **Update, 6 October 2026 (plan review H1, `docs/reviews/2026-10-06-plan-review.md`):** this threat model is out of date.
> - Decision #10 later gave the same token access to a **private drafts repo** holding unpublished drafts and original photos, which may carry GPS data. A leak now exposes private material, not only "website integrity".
> - The shared origin (point 2 below) is no longer hypothetical: #18 widgets, #29 analytics and SVG uploads could all put third-party code on the Admin's origin.
> - **#31 owns the fix:** the origin and custom-domain plan, plus hard rules for #18, #27 and #29.

The token grants **write to one public website repository** and nothing else (no account access, no other repos, no org). Worst realistic outcome of a leak: an attacker defaces or deletes the firm's website until the owner revokes the token and rolls back (§2.5 H5 — history makes this a 2-minute recovery). There is no customer data in the repo (it must stay that way; Pages is public). So the asset is "website integrity", not "financial data".

The three ways the token can leak from a browser-only Admin:

1. **XSS in the Admin page itself** — any script running on `https://phuwanutkhodop.github.io` can read *every* storage mechanism (localStorage, sessionStorage, IndexedDB, in-memory variables). OWASP: "A single Cross Site Scripting can be used to steal all the data in these objects." [[26]](https://cheatsheetseries.owasp.org/cheatsheets/HTML5_Security_Cheat_Sheet.html) The Admin renders owner-written content and loads third-party libraries, so this is the primary risk and must be addressed by design (CSP, no `innerHTML` of untrusted strings, pinned CDN hashes), not by storage choice.
2. **Shared origin** — storage is per *origin*, and the whole `phuwanutkhodop.github.io` host (every project site under this account) is **one origin**. OWASP warns: "every object is shared within an origin … Avoid hosting multiple applications on the same origin." [[26]](https://cheatsheetseries.owasp.org/cheatsheets/HTML5_Security_Cheat_Sheet.html) Any other Pages project published under the same account could read the token. Mitigation: keep this the only project site on the account, or move the Admin to its own origin (custom domain) later.
3. **Device access** — anyone who can open the owner's browser profile (shared PC, malware, stolen laptop) can read localStorage/IndexedDB. OWASP: "do not assume IndexedDB provides confidentiality … Avoid storing session tokens, credentials, or other secrets there." [[26]](https://cheatsheetseries.owasp.org/cheatsheets/HTML5_Security_Cheat_Sheet.html)

### 4.2 Options compared

| Option | Survives reload | Survives tab close / browser restart | Readable by XSS | Readable from disk | Notes |
|---|---|---|---|---|---|
| In-memory JS variable only | No | No | Yes (while open) | No | Owner re-pastes the token every visit. Safest, most annoying. |
| **sessionStorage** | Yes | **No** (per tab; destroyed on tab close) | Yes | Short-lived | MDN: "Closing the browser tab destroys all sessionStorage data." OWASP: prefer it "if persistent storage is not needed." [[27]](https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API) [[26]](https://cheatsheetseries.owasp.org/cheatsheets/HTML5_Security_Cheat_Sheet.html) |
| localStorage | Yes | Yes | Yes | Yes | Shared by all tabs of the origin; persists until cleared. [[27]](https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API) |
| IndexedDB (plain) | Yes | Yes | Yes | Yes | No security advantage over localStorage. [[26]](https://cheatsheetseries.owasp.org/cheatsheets/HTML5_Security_Cheat_Sheet.html) |
| IndexedDB + token encrypted with a key derived from a **WebAuthn `prf`** assertion (passkey / Touch ID / Windows Hello) | Yes | Yes (ciphertext) | Only *after* the owner authenticates in that tab; ciphertext alone is useless | Ciphertext only | The W3C spec's own motivating example: "PRF outputs could be used as symmetric keys to encrypt user data. Such encrypted data would be inaccessible without the ability to get assertions from the associated credential." Requires a platform authenticator with `hmac-secret`; support varies by browser/OS and is **not verified in this ticket**. [[28]](https://w3c.github.io/webauthn/#prf-extension) [[29]](https://developer.mozilla.org/en-US/docs/Web/API/Web_Authentication_API/WebAuthn_extensions) |
| Password-derived key (owner types a passphrase; PBKDF2/Argon2 → AES-GCM via WebCrypto; ciphertext in localStorage) | Yes | Yes (ciphertext) | Only after the owner unlocks in that tab | Ciphertext only | Works everywhere today; the passphrase is a second thing to remember; a weak passphrase is brute-forceable offline. |
| httpOnly cookie / BFF | — | — | No | — | **Not available**: needs a server; out of scope by the "static only" rule. |

Key insight: *no* client-side option survives XSS while the Admin is open and unlocked, because the token must be in memory to be used. The storage decision only changes exposure **while the Admin is closed** and **to disk/device access**.

### 4.3 Recommendation

1. **Default: sessionStorage.** The owner pastes the token (from a password manager) when opening the Admin; it survives reloads during the editing session and vanishes when the tab closes. This matches OWASP's "use sessionStorage instead of localStorage if persistent storage is not needed" and keeps nothing on disk between sessions. [[26]](https://cheatsheetseries.owasp.org/cheatsheets/HTML5_Security_Cheat_Sheet.html)
2. **Opt-in "Remember on this device" → encrypted at rest.** If the owner ticks it, store the token in localStorage/IndexedDB **only as AES-GCM ciphertext**, with the key derived from a WebAuthn `prf` assertion where available (passkey unlock = Touch ID/Windows Hello) and falling back to a passphrase-derived key. Never store plaintext in localStorage. Decide the exact mechanism in the Admin-security prototype ticket (open question §6.1).
3. **Hard rules regardless of storage:** never put the token in the URL, page source, repo, or logs; send it only to `https://api.github.com`; clear it from memory on "Sign out"; show the token's expiry date and the last-used timestamp; one-click **Revoke** link to `https://github.com/settings/personal-access-tokens`.
4. **Reduce blast radius by construction:** the token is repo-scoped with only Contents + Pages (§2.1); the repo contains no secrets (Pages is public anyway); rollback is one click (§2.5), so a defacement is a nuisance, not a disaster.
5. **XSS hygiene is the real control:** strict `Content-Security-Policy` meta tag on `/admin/` (`default-src 'self'; connect-src 'self' https://api.github.com https://phuwanutkhodop.github.io; script-src 'self' <hashes>`), no inline event handlers, sanitise any HTML preview, pin third-party scripts with `integrity=` hashes. Those belong to the Admin design ticket.

### 4.4 Expiry behaviour and renewal UX

* On expiry GitHub **revokes** the token; it "can no longer be used to authenticate … It is not possible to restore an expired or revoked token." Every API call returns `401`. [[21]](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/token-expiration-and-revocation)
* **Correction, 6 October 2026 (plan review H6):** a browser page **cannot** read the header described in the next point. GitHub's CORS `Access-Control-Expose-Headers` lists only ETag, Link, the rate-limit headers, X-OAuth-Scopes, X-Accepted-OAuth-Scopes and X-Poll-Interval. The Admin therefore asks the owner for the expiry date when the token is pasted, and treats any `401` as "renew your key" (#20, #25).
* The API tells you the date in advance: the live response header `github-authentication-token-expiration: 2026-10-05 09:13:19 UTC` was observed in this research. Admin should read it on P1 and show "Token expires in N days" from 14 days out.
* GitHub emails the account when a token is about to expire (stated in GitHub's 2021 changelog; the exact lead time is not documented in the pages read for this ticket). [[30]](https://github.blog/changelog/2021-07-26-expiration-options-for-personal-access-tokens/)
* Renewal UX: on any `401` → clear stored token → show a screen that (a) explains "your publishing key has expired — nothing is lost", (b) deep-links to the pre-filled token form (§5 step 3 URL), (c) has a paste box, (d) re-runs P1–P3 and resumes the pending publish from the draft held in the browser. GitHub also offers **Regenerate** on an existing fine-grained token in the token's settings page, which keeps the same name/permissions and issues a new secret.
* Choose the lifetime deliberately: **366 days** (max) gives one planned renewal a year; "No expiration" is allowed for a personal account but is still revoked after **one year without use**, and GitHub recommends setting an expiration. [[1]](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) [[21]](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/token-expiration-and-revocation) [[31]](https://docs.github.com/en/rest/authentication/keeping-your-api-credentials-secure)

---

## 5. DRAFT — Owner guide: creating the publishing key (fine-grained token)

*Plain-language draft for the Site Operations Manual. Every click is named. Screens are described as of the GitHub documentation read on 5 Oct 2026; GitHub may rename things — if a label differs slightly, pick the closest.* Source for the steps: [[1]](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)

**What you are making:** a "publishing key" that lets the Admin page save files into your website's GitHub repository — and nothing else. It is like a key that opens one cupboard, not the whole office.

**Before you start:** sign in to GitHub at https://github.com with the account `phuwanutkhodop`, and make sure your email is verified (GitHub requires this).

**Step 1 — Open the token page**
1. Click your **profile picture** (top-right corner).
2. Click **Settings**.
3. Scroll the left sidebar to the very bottom and click **Developer settings**.
4. In the left sidebar, under **Personal access tokens**, click **Fine-grained tokens**.
5. Click the green **Generate new token** button.

**Step 2 — Name and lifetime**
6. **Token name:** type `Website Admin publishing key`.
7. **Expiration:** choose **Custom** and set a date **one year from today** (the maximum is 366 days). The Admin page will remind you 14 days before it ends. *(Alternative: "No expiration" is allowed for personal accounts, but GitHub recommends an expiry and will anyway disable a key not used for a year.)*
8. **Description (optional):** `Used only by /admin/ on the firm website. Contents + Pages read.`

**Step 3 — Which repository**
9. **Resource owner:** leave as **phuwanutkhodop** (your own account).
10. **Repository access:** choose **Only select repositories**.
11. In the **Select repositories** dropdown, tick **accountingsite.github.io** only. (If the Admin later moves to another repo, make a new key for that repo.)

**Step 4 — Permissions (the important part)**
12. Expand **Repository permissions**.
13. Find **Contents** → set the dropdown to **Read and write**.
14. Find **Pages** → set the dropdown to **Read-only**.
15. Notice **Metadata** has become **Read-only** automatically (GitHub adds it; you cannot remove it — this is normal).
16. Leave **everything else** at **No access**. In particular do **not** tick Actions, Administration, Workflows, Secrets or any Account permissions.
17. At the top of the Permissions section the summary should read something like **"3 permissions"** (Contents, Metadata, Pages).

**Step 5 — Generate and copy**
18. Click **Generate token** at the bottom.
19. GitHub shows the key **once**. It starts with `github_pat_`. Click the **copy** icon next to it.
20. Paste it immediately into your password manager (recommended) under "Website Admin publishing key", and then into the Admin page's **Publishing key** box. If you close the page without copying, nothing is broken — just delete that token and make a new one.

**Shortcut for step 2–4 (optional):** this link opens the form with name, 365-day expiry, Contents = write and Pages = read already filled in; you still choose the repository and press Generate:
`https://github.com/settings/personal-access-tokens/new?name=Website+Admin+publishing+key&description=Used+only+by+/admin/+on+the+firm+website&expires_in=365&contents=write&pages=read`
(GitHub documents these URL parameters: `name`, `description`, `expires_in` 1–366 or `none`, and `<permission>=read|write`.) [[1]](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#pre-filling-fine-grained-personal-access-token-details-using-url-parameters)

**If something goes wrong later**
* "Publishing key expired or invalid" in the Admin → go to **Settings → Developer settings → Fine-grained tokens**, click the key, click **Regenerate token** (or just make a new one with these steps), paste the new value into the Admin.
* You think the key leaked → same page → **Delete** the token. The website stays online; the Admin simply cannot publish until you make a new key. Then use the Admin's **History → Restore** if anything was changed.

---

## 6. Open questions for other tickets

1. **Encrypted "remember me" mechanism** (Admin security prototype): verify WebAuthn `prf` support on the owner's actual devices (Windows Hello / Chrome; iPhone Safari) and decide prf-vs-passphrase fallback. Browser-compat data could not be fetched in this sandbox. [[28]](https://w3c.github.io/webauthn/#prf-extension)
2. **CORS preflight for `X-GitHub-Api-Version`**: the documented allow-list omits it; confirm in the prototype whether sending it triggers a preflight failure, or simply omit it (default version `2022-11-28` was observed).
3. **Shared-origin exposure**: all project sites under `phuwanutkhodop.github.io` share one origin with the Admin. Decide: keep this the only Pages project on the account, or plan a custom domain (and what that does to the "relative paths only" rule and the EN/TH/ZH URL design).
4. **`.nojekyll` and first-publish bootstrap**: should the Admin add `.nojekyll` (and a `<meta name="x-build">` marker in every page for live-detection) on its first publish? Interacts with the sitemap/SEO ticket.
5. **Image pipeline in the browser** (Design Library / media ticket): target formats (WebP/AVIF), max dimensions, size caps (suggest refuse > 25 MB, warn > 2 MB), EXIF stripping — all doable client-side before `POST /git/blobs`.
6. **Draft safety**: where unsaved page edits live before publish (IndexedDB is fine for *content*, not for the token), and conflict handling when `PATCH /git/refs` fails the fast-forward check (someone edited via GitHub web UI).
7. **Second editor / staff access**: fine-grained PATs are personal. If staff ever publish, each needs their own token *and* collaborator access to the repo; GitHub notes fine-grained PATs cannot yet be used by outside collaborators on some flows. Decide whether this is in scope for v1 (map says single-owner).
8. **Actions later**: scheduled publishing and font subsetting are the only identified needs that cannot run in the browser; park until a real need appears. Granting `Workflows: write` to the token is **not** planned.
9. **Acceptable-use check**: confirm the firm site stays informational (no payment collection on the Pages origin) so it remains inside GitHub Pages terms. [[14]](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits)

---

## Sources

1. Managing your personal access tokens — https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens [source: `content/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens.md`]
2. Permissions required for fine-grained personal access tokens — https://docs.github.com/en/rest/authentication/permissions-required-for-fine-grained-personal-access-tokens [source data: `src/github-apps/data/fpt-2022-11-28/fine-grained-pat-permissions.json`]
3. REST API: Repository contents (get / create-or-update / delete) — https://docs.github.com/en/rest/repos/contents [source: OpenAPI `paths./repos/{owner}/{repo}/contents/{path}`]
4. Using the REST API to interact with your Git database — https://docs.github.com/en/rest/guides/using-the-rest-api-to-interact-with-your-git-database
5. Configuring a publishing source for your GitHub Pages site — https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site
6. REST API: GitHub Pages (site, builds, deployments) — https://docs.github.com/en/rest/pages/pages [source: OpenAPI `paths./repos/{owner}/{repo}/pages*`, schemas `page`, `page-build`, `pages-deployment-status`]
7. REST API: Commits — https://docs.github.com/en/rest/commits/commits
8. Rate limits for the REST API — https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api [source incl. `data/reusables/rest-api/primary-rate-limit-authenticated-users.md`, `secondary-rate-limit-rest-graphql.md`]
9. REST API: Git trees — https://docs.github.com/en/rest/git/trees
10. REST API: Git commits — https://docs.github.com/en/rest/git/commits
11. REST API: Git references — https://docs.github.com/en/rest/git/refs
12. REST API: Deployments — https://docs.github.com/en/rest/deployments/deployments (live check: `GET /repos/phuwanutkhodop/accountingsite.github.io/deployments` → environment `github-pages`, status `success`, `environment_url` = site)
13. Community observation of GitHub Pages `Cache-Control: max-age=600` and per-deploy ETag reset — https://dev.to/jangwook_kim_e31e7291ad98/your-last-deploy-reset-every-cache-validator-on-the-site-4dd3 (non-official)
14. GitHub Pages limits — https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits
15. Creating a GitHub Pages site (Jekyll default, `.nojekyll`, "up to 10 minutes") — https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site [and `data/reusables/pages/twenty-minutes-to-publish.md`]
16. GitHub Actions billing (free for public repositories) — https://docs.github.com/en/billing/concepts/product-billing/github-actions
17. Using CORS and JSONP to make cross-origin requests — https://docs.github.com/en/rest/using-the-rest-api/using-cors-and-jsonp-to-make-cross-origin-requests (live check 5 Oct 2026: `Access-Control-Allow-Origin: *` with `Origin: https://phuwanutkhodop.github.io`)
18. What is GitHub Pages? (user/organization vs project sites) — https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages
19. Setting a personal access token policy for your organization (366-day default) — https://docs.github.com/en/organizations/managing-programmatic-access-to-your-organization/setting-a-personal-access-token-policy-for-your-organization
20. GitHub Changelog, 18 Oct 2024: PAT rotation policies and optional expiration for fine-grained PATs — https://github.blog/changelog/2024-10-18-new-pat-rotation-policies-preview-and-optional-expiration-for-fine-grained-pats/ (seen via search snippet; domain blocked in sandbox)
21. Token expiration and revocation — https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/token-expiration-and-revocation
22. About large files on GitHub (100 MiB block, 50 MiB warning, 25 MiB browser upload) — https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github [values: `data/variables/large_files.yml`]
23. REST API: Git blobs — https://docs.github.com/en/rest/git/blobs
24. GitHub Changelog, 3 May 2022: increased file size limit when retrieving file contents via REST API — https://github.blog/changelog/2022-05-03-increased-file-size-limit-when-retrieving-file-contents-via-rest-api/ (seen via search snippet)
25. Community discussion #155856 on REST upload size (non-official, anecdotal 422s above ~50 MB) — https://github.com/orgs/community/discussions/155856
26. OWASP HTML5 Security Cheat Sheet (Local Storage, Client-side databases) — https://cheatsheetseries.owasp.org/cheatsheets/HTML5_Security_Cheat_Sheet.html [source read: `OWASP/CheatSheetSeries/master/cheatsheets/HTML5_Security_Cheat_Sheet.md`]
27. MDN: Web Storage API (sessionStorage vs localStorage scoping) — https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API [source read: `mdn/content` `files/en-us/web/api/web_storage_api/index.md`]
28. W3C Web Authentication Level 3, §Pseudo-random function extension (prf) — https://w3c.github.io/webauthn/#prf-extension [source read: `w3c/webauthn/main/index.bs`]
29. MDN: WebAuthn extensions (`prf`) — https://developer.mozilla.org/en-US/docs/Web/API/Web_Authentication_API/WebAuthn_extensions [source read: `mdn/content`]
30. GitHub Changelog, 26 Jul 2021: expiration options for personal access tokens (email before expiry) — https://github.blog/changelog/2021-07-26-expiration-options-for-personal-access-tokens/ (seen via search snippet)
31. Keeping your API credentials secure — https://docs.github.com/en/rest/authentication/keeping-your-api-credentials-secure
