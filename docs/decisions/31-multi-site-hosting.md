# 31 — Multi-site hosting and the security origin

**Ticket:** GitHub issue #31 (Wayfinder research, decided by Claude)
**Date:** 6 October 2026
**Decided by:** Claude, under the owner's standing delegation of technical choices (map #1, "Working preference"). The owner's part is three short setup steps, at the times listed in §8.
**Inputs:**
- research #4 (publishing and token security);
- decisions #10 (file layout), #12 (two Admin levels), #13 (library), #16 (tech stack), #17 (drafts) and #20 (publish proof);
- plan review findings **H1, M4 and M13** (`docs/reviews/2026-10-06-plan-review.md`).

**Status:** locked. Resolves H1, M4 and M13.

---

## 1. สรุปสำหรับเจ้าของกิจการ (ภาษาไทย)

1. **ปัญหา:** ทุกเว็บที่อยู่ใต้ `phuwanutkhodop.github.io` ถือเป็น "บ้านเลขที่เดียวกัน" ในสายตาเบราว์เซอร์ อะไรที่รันบนเว็บหนึ่ง (สคริปต์วัดสถิติ, widget, ไฟล์ SVG) อ่านของในเบราว์เซอร์ของอีกเว็บได้ รวมถึงกุญแจ Publish ถ้า Admin อยู่บ้านเดียวกัน
2. **ทางแก้: Admin ย้ายไปอยู่ "บ้านของตัวเอง"** ที่ไม่มีอะไรอื่นอยู่เลย ใช้ "องค์กร" (organization) ฟรีบน GitHub ซึ่งได้ที่อยู่ใหม่ `https://<ชื่อองค์กร>.github.io/admin/` ไม่ต้องซื้อโดเมน ไม่มีค่าใช้จ่าย
3. **Admin เดียวดูแลทุกเว็บ** (หน้า "เว็บไซต์ของฉัน" ตามที่คุณเลือกไว้ใน #12) ไม่ต้องมี Admin ซ้ำในทุกเว็บ
4. **กุญแจ Publish ดอกเดียว** ครอบคลุมทุกเว็บ เพิ่มเว็บใหม่ = เพิ่มชื่อที่เก็บเข้าไปในกุญแจเดิม ปีละครั้งต่ออายุดอกเดียว
5. **กุญแจแตะโค้ดของ Admin ไม่ได้** เพราะ Admin อยู่คนละเจ้าของ ถึงกุญแจหลุด ก็ฝังโปรแกรมแอบแฝงใน Admin ไม่ได้
6. **แต่ละเว็บ = ที่เก็บสาธารณะ 1 + ที่เก็บส่วนตัว 1** (ฉบับร่างและรูปต้นฉบับ) ย้าย สำรอง หรือเลิกเว็บใดก็ทำได้ทีละเว็บ
7. **คลังดีไซน์กลางอยู่ในที่เก็บของมันเอง** ทุกเว็บดึงไปใช้ได้ ดีไซน์ที่ยังมีเว็บใดใช้อยู่ ลบไม่ได้
8. **รูปต้นฉบับ:** เก็บเป็น "ต้นแบบคุณภาพสูง" ขนาดไม่เกิน 4096 px และลบพิกัด GPS ออก แทนไฟล์ดิบจากกล้อง ไฟล์ดิบยังอยู่ในมือถือหรือ OneDrive ของคุณ ระบบมีแถบบอกพื้นที่ และเตือนก่อนเต็ม **ถ้าคุณต้องการเก็บไฟล์ดิบไว้ในระบบด้วย บอกได้ครับ**
9. **เว็บสาธารณะใส่สคริปต์วัดสถิติได้ในอนาคต** (#29) เพราะไม่มีความลับอยู่บนบ้านนั้นแล้ว
10. **สิ่งที่คุณต้องทำ (ทีละขั้น พร้อมคู่มือ ตอนถึงเวลา):** (ก) ก่อนเริ่มคลังดีไซน์ (#21) สร้างที่เก็บคลังดีไซน์และเพิ่มเข้ากุญแจ (ข) ก่อนเริ่มโปรแกรม Admin (#22) สร้างองค์กรฟรีบน GitHub (ค) เมื่อจะเพิ่มเว็บที่สอง สร้างที่เก็บ 2 ที่และเพิ่มเข้ากุญแจ **วันนี้ยังไม่ต้องทำอะไร**

---

## 2. The problem in one paragraph

Browser storage is shared per **origin** (scheme + host + port). Every Pages site of an account without its own domain is served from one host, so `phuwanutkhodop.github.io/<any-repo>/` is **one origin**. If the Admin lives there, any script that ever runs on any page of that host can read the Admin's IndexedDB, its encrypted "remember me" store and the token while it is in memory. That includes analytics (#29), widgets (#18), an uploaded SVG opened directly, or another project site. The token now also reaches private drafts and photo originals (#10). A custom domain on a *project* repo gives that repo its own origin. A custom domain on the *user* site does the opposite: every project site without its own domain moves under it (verified, §9).

## 3. Decisions

| # | Question | Decision | Why |
|---|---|---|---|
| 1 | Where the Admin runs | **One Admin for all sites, on an origin that serves nothing else:** a free GitHub organization `<admin-org>` (suggested `phuwanutkhodop-admin`), repo `<admin-org>/<admin-org>.github.io`, Admin at `https://<admin-org>.github.io/admin/`. It is born there: **no Admin code is ever committed to a site repo.** | A different owner is the only way to get a separate origin without buying a domain (§9). One Admin matches the two levels of #12 (My Sites + per-site Admin), is updated in one place, and is one origin to protect. Free, available today. |
| 2 | Why not "one site per account until a domain exists" | Rejected. | It forbids analytics and widgets on the public site for as long as the Admin shares its origin, and it blocks the second site that #12 promises from day one. The move would have to happen later anyway, with the Admin's local data left behind. |
| 3 | Why not a custom domain for the Admin now | **Optional later**, not required. `admin.<firm-domain>` can be pointed at the Admin repo when the firm has a domain. | Buying and naming the domain is part of the later firm-website effort. The organization gives the same isolation now at no cost. |
| 4 | The token | **One fine-grained token, resource owner `phuwanutkhodop`, "Only select repositories":** every site repo, every site's drafts repo, and the library repo. Contents read/write, Pages read, Metadata read. **It never covers the Admin repo, and cannot**, because a fine-grained token reaches one owner only (§9). | One key to store, paste and renew a year. Keeping the Admin's code out of the token's reach means a stolen token cannot plant code in the Admin to catch the next token. One key per site would give little isolation (the owner is one person on one device) for N times the renewals. |
| 5 | Drafts repos | **One private drafts repo per site**, named `<site-repo-name>-drafts` (the existing `accountingsite-drafts` already follows this). Same inner layout as #10 and #17. | A site stays self-contained: back up, move or retire one site without touching another. Each site gets its own size budget (§6). |
| 6 | Master Design Library | **Its own public repo, `phuwanutkhodop/builder-library`**, with Pages switched off. It holds `library/` (#13) and `sites.json`, the list of sites for My Sites. Each site keeps pinned copies in `site/presets/` (#10-6), so a site renders without the library. | The token must write it (owner save-back), so it cannot live in the Admin repo. It must not live in one site's repo once there are several. Public is fine: presets are design only (#13-1). |
| 7 | Save-back with a separate library | **The master copy is written to `builder-library` when the owner saves**, after the library check. It touches no site. The page's draft references it, and the pinned copy is written into the site with the next Publish. | Supersedes #13 §3.4 step 6's route through the drafts repo. That route existed to keep public *site* files changing only at Publish (M3), which still holds. Saving at once makes a new design usable on every site immediately (Principle 1). |
| 8 | Where public sites live | **Unchanged:** `phuwanutkhodop.github.io/<repo>/` until a site gets its own domain. Public sites may share an origin with each other. | They hold no secrets. A domain is a brand and SEO choice for the firm-website effort, no longer a security need. |
| 9 | Builder code and docs | Admin code, `tests/` and `tools/vendor/` live in the Admin repo, in exactly the layout of #16 §3. Docs, decisions, the map and the brand stay in this repo, which remains the test-bed site. | #16 already kept `admin/` self-contained with relative imports for this move. |

## 4. The repositories

```
Organization <admin-org>  (the Admin's own origin; nothing else is ever published here)
└── <admin-org>.github.io        public · Pages on
    ├── index.html               static link to ./admin/ (no script)
    ├── admin/                   the Admin, exactly #16 §3: app/ engine/ services/ styles/ vendor/
    ├── tests/   tools/vendor/   package.json
    └── (token: NO access — different owner)

User phuwanutkhodop  (everything the token touches)
├── builder-library              public · Pages off · library/ + sites.json
├── <site>                        public · Pages on   · site/ + generated output + media/   (#10 ①, minus admin/ and library/)
├── <site>-drafts                 private             · drafts/ + originals/ + labels.json  (#10 ②, #17)
└── … one <site> + <site>-drafts pair per site.  Site #1 = accountingsite.github.io + accountingsite-drafts
```

`sites.json` entry: `{ "id", "name": {en,th,zh}, "repo", "draftsRepo", "url", "addedAt" }`. The Admin reads it for My Sites.

## 5. Security rules (resolves H1)

### 5.1 Threat model (replaces research #4 §4.1)

- **What a leaked token exposes:** the integrity of every site; their unpublished drafts and image masters; the library. It does **not** expose the Admin's code, the owner's other repos, or the account.
- **How it could leak, and the control for each:**
  - **Script on the Admin's origin** → the origin serves only the Admin's own vendored code (rule A1) under the strict policy of #16-8.
  - **Device access** → sessionStorage by default; "remember me" only as ciphertext (research #4 §4.3).
  - **A bad library update** → vendored, pinned and reproducible (#16-3), added only by Claude sessions.
  - **The shared github.io origin** → closed by design: no token ever exists on a site's origin.
- **Recovery:** delete the key on GitHub, make a new one (#20 §5), and restore any damaged site through Versions (#17).
- **The #20 proof** pasted the key into a one-time page on `phuwanutkhodop.github.io`, now removed. This site's pages load no third-party script (checked: only `core/animations.js` and `core/article-loader.js`), and the account's other repos are private, with no known Pages site. No realistic exposure; the key stays valid.

### 5.2 Hard rules

| Rule | Applies to |
|---|---|
| **A1 — The Admin's origin is the Admin only.** No third-party script, no uploads, no generated site pages, no SVG. The only HTML files in the Admin repo are `index.html` and `admin/index.html`; golden test files use another extension (`.golden`). A test enforces this. | #22 onward |
| **A2 — Origin lock.** The Admin accepts and uses a token only when `location.origin` is its own origin (or `http://localhost:<port>` for development). A copy served anywhere else refuses the key. | #22, #25 |
| **A3 — Previews are opaque.** Generated pages are previewed only in `sandbox` iframes **without `allow-same-origin`**, so even a preview with scripts has no access to the Admin's storage. | #22, #28 |
| **A4 — Cache integrity.** Source cached in IndexedDB is re-hashed against its git blob SHA when read, and refetched on mismatch. | #22 (#11 §3.7 cache) |
| **S1 — Public sites hold no secrets** in browser storage. Third-party script on a public site is now a privacy and consent question for #29, and a vetted-widget question for #18, not a token question. Each such script still needs a decision and a `noscript`-safe page (#11-1). | #18, #29 |
| **S2 — SVG uploads are refused in the Admin in v1.** SVG can carry script; on a site's origin that means defacement or phishing under the firm's name. Logos and icons in SVG are added by Claude sessions after review. A sanitiser may come later. | #27 |
| **S3 — Sites with their own domain** are added to the Admin's `connect-src` by an Admin release, so the "is it live?" check (#20, M10) can read them. GitHub Pages answers cross-origin reads with `Access-Control-Allow-Origin: *` (§9). | #28 |

## 6. Size of each drafts repo (resolves M13)

- **Masters, not raw originals.** On upload the image pipeline (research #7) also writes a **master**: long edge at most **4096 px**, WebP quality 90, all metadata (including GPS) removed, typically 1–2.5 MB. The master feeds every rendition (largest 2400 px) with room to re-crop. The raw camera file stays with the owner (phone, OneDrive). This amends #10-8, which stored raw originals up to 12 MB.
- **Budget, read from `GET /repos/{owner}/{repo}` → `size`** (Metadata read; GitHub updates it with some delay):
  - shown on the site's Media screen as "พื้นที่ร่างและต้นแบบรูป 420 MB จาก 1 GB";
  - **600 MB:** yellow, with a note;
  - **850 MB:** red, and new image uploads pause with a Thai explanation and the roll-over offer below.
  - GitHub recommends repos under 1 GB.
- **"Kept forever?"** Masters of images in use are kept. A deleted image's master leaves the current files at once, but git history keeps it until the next **roll-over**:
  1. the owner creates `<site>-drafts-2` (private) and adds it to the key;
  2. the Admin copies only the current files (drafts, masters still in use, `labels.json`), throttled and resumable like uploads (H5);
  3. it updates `sites.json`;
  4. the owner archives the old repo after the Admin shows the copy is complete.
  This replaces history rewriting, which #17 §3.8 forbids in v1.
- **Rough capacity:** about 2.5 MB per image, counting the master and the renditions that wait in drafts before Publish (H5). That is roughly 340 images per site before red. A roll-over shrinks it back to the images in use.

## 7. The library across sites (resolves M4)

- **The usage index** (#13 §3.7) is computed across **every site in `sites.json`**: published pages, drafts and page templates.
- **Removal from the master** is offered only when every site reports zero use **and every site could be read**. If a site cannot be read (for example, it is missing from the key), removal waits.
- **Deprecation** stays possible at any time. Pinned copies keep every site rendering whatever happens to the master.
- **Page-only presets** (#10-5a) carry `site: "<id>"` and appear only in that site's picker.

## 8. Sites over time

**Owner steps, each with a step-by-step guide at the time:**

| When | Step | Takes |
|---|---|---|
| Before #21 (first presets) | Create the public repo `builder-library`, then add it to the existing key. Editing a fine-grained key's repository list is the expected path; if GitHub offers no edit, make a new key with the same settings (#20 §5). | ~3 min |
| Before #22 (first Admin code) | Create the free organization `<admin-org>`, then install the Claude GitHub app on it so sessions can push the Admin. Claude creates the repo and its Pages setting, or guides the owner. | ~5 min |
| Adding a site (#25 designs the screen) | Create `<site>` (public) and `<site>-drafts` (private, with a README), switch Pages on for `<site>`, add both to the key. The Admin then writes the `sites.json` entry and the empty `site/` source. | ~5 min |

**Backing up, moving and retiring a site** (repo-level meaning; #30 designs the screens):

- **Back up:** a site is its two repos. The pinned presets make it complete without the library. A full backup is a download of both. #30 adds a one-click export of their current files.
- **Move:** transfer or rename both repos and update `sites.json` and the key. The github.io address follows the repo name and owner, so **a live site moves only after it has its own domain**; otherwise its address changes.
- **Retire:** remove the entry from `sites.json`. The repos stay until the owner archives or deletes them on GitHub, because the key has no Administration permission and cannot delete anything.

## 9. Evidence

| Fact | Source |
|---|---|
| Each fine-grained token reaches resources of **one** user or organization | [GitHub Docs: managing personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) |
| A custom domain on the user site also serves project sites under it | [GitHub Docs: about custom domains](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/about-custom-domains-and-github-pages); [GitHub blog, 2013](https://github.blog/news-insights/product-news/new-github-pages-domain-github-io) |
| A custom domain on a project repo gives it its own origin; github.io addresses redirect to it | plan review H1 (verified there) |
| Organization sites at `https://<org>.github.io`, from a repo named `<org>.github.io`; Pages is available for public repos on GitHub Free for organizations | [GitHub Docs: what is GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages) |
| GitHub Pages sends `Access-Control-Allow-Origin: *` | [GitHub community discussion 22399](https://github.com/orgs/community/discussions/22399) |
| `github.io` is on the Public Suffix List, so each `<name>.github.io` is its own site | [publicsuffix.org list](https://publicsuffix.org/list/public_suffix_list.dat) |
| The account's other repos are all private | repo list on 6 Oct 2026 |

Docs pages were read through search results; docs.github.com itself was blocked by this session's network policy. The first owner step (§8) re-confirms the organization and key behaviour in practice.

## 10. Effects on other documents and tickets

- **Map #1:** "Admin lives at `/admin/` on the published site" becomes "Admin at `/admin/` on its own origin, one Admin for all sites".
- **#10:** layout ① loses `admin/` and `library/`; decision 8 now stores masters (§6). The library is its own repo (decision 6 here).
- **#13:** §3.4 step 6 per decision 7 here; §3.7 removal across sites per §7.
- **#16:** the §3 layout is the Admin repo's root. `connect-src` adds `https://phuwanutkhodop.github.io` for the live check, plus site domains later (S3).
- **#17:** the "library design" item is now only the page's reference and pinned copy; the master is saved at once.
- **#20:** the key's repository list grows as in §8. The guide gains the library and add-a-site steps.
- **Research #4 §4.1:** replaced by §5.1 here.
- **#18, #29:** S1. **#27:** S2, masters and the budget. **#22:** A1–A4 and the Admin repo. **#25:** the add-site flow, `sites.json` and the budget warnings. **#28:** A3 and S3. **#30:** backup, move and retire as in §8. **#21:** presets go to `builder-library`.

## 11. Not decided here

- The organization's exact name: the owner picks it when creating it (suggested `phuwanutkhodop-admin`).
- The screens for My Sites, add-site and the budget bar → #25 and #27.
- Custom domains for the sites and for the Admin → the firm-website effort.
- A sanitiser for SVG uploads → later, if ever needed.
