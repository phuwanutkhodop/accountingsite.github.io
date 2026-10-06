# Plan review — 6 October 2026

**Asked by:** the owner: "check what slipped or is weak in the work the earlier AI did"
**Scope:**
- the builder plan: map #1, research #2–#9, decisions #10, #11, #12 and #24;
- today's decisions #16, #14 and #13, to check they fit the earlier work.
**Method:**
- two independent checks:
  - a document-consistency audit;
  - a fact-check against primary sources (GitHub docs source, browser-compat-data 8.1.4, the WHATWG specs, Google);
- every high finding was then re-checked by hand against the files.
**Status:** **applied, 6 October 2026** (owner: "แก้เลย"). Every finding is either fixed in the documents or attached to the ticket that owns it; see §4.

---

## 1. สรุปสำหรับเจ้าของกิจการ (ภาษาไทย)

1. **โครงหลักแข็งแรงและถูกต้อง** ข้อเท็จจริงสำคัญได้รับการยืนยันจากแหล่งทางการแล้ว:
   - สร้างหน้าเว็บเสร็จตอนกด Publish
   - ส่งขึ้น GitHub ในครั้งเดียว
   - สิทธิ์ของโทเคน
   - โทเคนเดียวดูแลได้ทั้งที่เก็บสาธารณะและที่เก็บส่วนตัว
   - การเรียก GitHub จากเบราว์เซอร์ได้
2. **พบจุดอ่อน 6 ข้อที่ต้องแก้ก่อนเริ่มเขียนโปรแกรม** ส่วนใหญ่เป็นเรื่องฉบับร่าง การย้อนเวอร์ชัน และความปลอดภัยของโทเคน (§2)
3. **จุดอ่อนหลายข้อมาจากงานของผมเองวันนี้** (#13 #14 #16) ไม่ใช่เฉพาะงานของ AI รุ่นก่อน
4. **เอกสารบางฉบับยังพูดถึงของเก่า** เช่น สีเดิม ไฟล์บทความเดิม และตั๋วที่รองานแบรนด์ที่พักไว้แล้ว ซึ่งจะทำให้ AI session ถัดไปเข้าใจผิด

---

## 2. High — fix before any build session

| # | Finding | Evidence | Fix | Owner | From |
|---|---|---|---|---|---|
| H1 | **The token's threat model is out of date, and the Admin shares its origin with everything else on `phuwanutkhodop.github.io`.** Decision #10 later gave the token access to a private repo holding drafts and original photos, which may carry GPS data. Every project site of the account is one origin (verified). Third-party script on public pages (#18 widgets, #29 analytics), or an SVG upload, could read the Admin's IndexedDB and its encrypted "remember me" store, and could poison the cached source that Publish trusts. | 04:163 assumes "website integrity" only; 04:168; 07:141 lets SVG pass through; 10:37; 11:99 | Rewrite the threat model. #31 decides the origin: a custom domain or subdomain for the Admin or the site, and when. Hard rules for #18, #27 and #29: no third-party script on any page of the Admin's origin unless it is isolated; SVG uploads are sanitised or refused; cached source is re-hashed against its git SHA when read. | #31 (+ #18 #27 #29) | earlier |
| H2 | **Whole-site rollback restores the entire repo tree,** including `admin/`, `library/` and any workflow file. A rollback silently downgrades the Admin and deletes presets saved since. It fails outright if the rollback crosses a workflow file, because the token has no Workflows permission. | 04:92 (H5); 11:132 | Rollback restores **only `site/` and the paths in `generated.json`**, through a normal Publish (regenerate, then diff). It is never a raw tree copy. | #17 | earlier |
| H3 | **Drafts and the shared `site.json` collide.** Today's #14 put the tree, the menus and the redirects in one file. Drafts are whole changed files, and Publish reads published source plus only the item being published. Publishing page A could therefore leak unpublished page B's menu or tree edits, or lose A's place in the tree. | 14:113; 10:45; 10:73 | #17 must define item-level drafts for `site.json`: each draft records its own tree, menu and redirect changes as operations, and those are merged at Publish. | #17 | **today (#14)** |
| H4 | **Placeholder text can pass the "all three languages" gate.** Section types carry EN/TH/ZH placeholders (today's #13), and the gate only blocks *empty* fields. Thai or Chinese sample text could go live unread. | 13:43; 11:74 | Fields start **empty**, with the placeholder shown only as a hint. The gate adds the error "value equals its placeholder". | #13 amend, #26 | **today (#13)** |
| H5 | **Where images wait before Publish is contradictory.** Research #7 commits renditions at upload time, and #11 relies on that. Decision #10 says the public repo holds only published content. Uploading early makes draft images public. Uploading loose blobs instead risks garbage collection while a draft waits weeks for translation. | 07:46; 11:121; 10:36, 10:67 | Renditions live in the **private drafts repo** until Publish, which copies them into `media/`. Uploads are throttled because of GitHub's write limits (80 per minute and 500 per hour, verified), and an interrupted batch can resume. | #27, #17 | earlier |
| H6 | **The Admin cannot read the token's expiry date.** Research #4 planned to read the `github-authentication-token-expiration` header. GitHub's CORS `Access-Control-Expose-Headers` does not include it (verified in the GitHub docs source), so a browser page never sees it. | 04 §4.4; GitHub docs, CORS page | The setup guide asks the owner to enter the expiry date when pasting the token. Any `401` means "renew your key", with the renewal flow from 04 §4.4. | #20, #25 | earlier |

## 3. Medium and low

| # | Finding | Fix | Owner | From |
|---|---|---|---|---|
| M1 | Articles have no permanent id; their file name is the slug. Today's #14 allows slug changes but defines automatic redirects and the `page:<id>` link form only for pages. | Add article ids, an `article:<id>` link form, and redirects for articles and for the children of a moved page. | #14 amend, #27 | **today** |
| M2 | The strict CSP was never tested on the **live preview**. Unpublished theme CSS, focal-point `style=`, YouTube frames and web fonts may all be blocked. | A preview spike in #22 before #23. If something needs loosening, record exactly what (for example `style-src blob:`) and why. | #16 note, #22 | **today** |
| M3 | Saving to the library writes public files (`library/`, `site/presets/`) immediately, outside Publish. | Save-back goes to the drafts repo and ships with the next Publish. | #13 amend | **today** |
| M4 | The usage index ignores drafts, page templates and other sites, so a preset could be removed while something still needs it. | The index includes drafts and templates. Removal across sites waits for #31. | #13 amend, #31 | **today** |
| M5 | The root `404.html` is served at any depth, so its relative links break. | A documented exception: the 404 page uses `<base href>` or site-absolute paths. | #14 amend | **today** |
| M6 | Root redirect vs `x-default`: an instant meta refresh is a permanent redirect (verified), so `x-default` would point at a redirect. | The root becomes a real chooser with no instant refresh, or `x-default` points to `/en/`. | #29 | earlier |
| M7 | Font loading has three positions that contradict each other: Google Fonts (05), never Google on `/zh/` (08, 11), and browser-side subsetting (34, parked). No subsetting tool is in #16's vendor list. | Reconcile in #15 and add the tool to the vendor set. | #15 | earlier |
| M8 | "All three languages required" conflicts with research #8's "switch a language off", and migrating the English-only test site could publish nothing. | **Proposed:** a language can be switched off per site, and every *switched-on* language must be complete. The firm's real site stays EN+TH+ZH as locked on the map. | #32, #19 | earlier |
| M9 | Contrast is checked only when a design is saved, never when the theme changes. | The publish gate also checks token contrast pairs. | #30 | **today (#13)** |
| M10 | The "is it live?" check can wait forever when GitHub cancels a superseded Pages build. | Accept "built at our commit **or a newer one**". | #20, #28 | earlier |
| M11 | Blob-SHA pitfalls: the length must be counted in UTF-8 bytes (Thai and Chinese text), and the repo has no `* text=auto eol=lf`, so a Windows clone shows phantom changes. | Hash UTF-8 bytes and write LF only. Add `* text=auto eol=lf` alongside the brand rules. | #20 | earlier |
| M12 | **`.nojekyll` is missing.** GitHub's Jekyll skips folders such as `vendor`, so `admin/vendor/` would silently not be served. | Add `.nojekyll` before the first Admin code ships. | #20 | today (#16) |
| M13 | The drafts repo grows with every original photo: git keeps all history, and GitHub recommends repos under 1 GB. | A size budget and a warning for the drafts repo; consider not keeping originals forever. | #27, #31 | earlier |
| M14 | More ways to lose the token: GitHub's public revocation API, automatic revocation on leak, and push protection blocking a publish. | Clear Thai error screens for each. | #25, #28 | earlier |
| M15 | `robots.txt` cannot hide `site/`, `library/` or `admin/` on a project site, because crawlers read it only at the host root (research #8 already says so). | Fix the claim in #10. Rely on `noindex` for HTML and accept that the JSON is crawlable. | doc fix | earlier |
| M16 | The visitor-facing day/night switch comes from the parked brand track (#33). Colour-mode names differ: "light/dark/band" vs "light/dark/linen". | The builder supports light, dark and "follow device" as a site setting; each site chooses later. #21 fixes the names. | #21 | earlier |
| L1 | Stale text that would mislead a session: PROJECT-STATUS line 24 (#15/#19/#21 "wait on #35"); line 275 (`articles.json` locked as source of truth); CLAUDE.md lines 65 and 74. | Edit. | doc fix | earlier |
| L2 | **#23 can never close.** It is blocked by the parked #35 and still lists "visual identity" in the spec. **#20** describes a test branch that Pages cannot serve, and omits the two-repo token. | Edit both issue bodies. | issues | earlier |
| L3 | The rich-text link whitelist has no `page:`, `article:`, `tel:` or `#anchor` links, and the gate demands alt text even for decorative images. | Extend the whitelist; add a "decorative" flag. | #16 amend, #27 | today |
| L4 | The policy on squashing git history has no owner. | Assign to #17. | #17 | earlier |

## 4. Outcome (applied 6 October 2026)

**Owner decision taken during the review (M8):** publishing requires every **switched-on** language. A site may switch a language off. The firm's real site keeps EN + TH + ZH. Recorded in decision #11.

**Fixed in the documents now:**
- **Decision records:**
  - #13: H4, M3, M4, M9;
  - #14: M1, M5, M6, plus the H3 consequence;
  - #16: M2 noted, M11, M12, L3;
  - #11: M8, L3, H5;
  - #10: M15, M1, H5.
- **Research #4:** dated correction notes for H1 and H6.
- **Status files:** PROJECT-STATUS and CLAUDE.md (L1).
- **Issue bodies:** #23 and #20 rewritten (L2, H6, M10, M11, M12).

**Attached to the owner tickets** (one comment each; each finding is resolved when that ticket closes):

| Ticket | Findings |
|---|---|
| #17 | H2, H3, M3, M4, L4 |
| #31 | H1, M4, M13 |
| #27 | H5, H1 (SVG), M1, L3, M13 |
| #22 | M2 (CSP preview test first) |
| #15 | M7 |
| #19 | M8 |
| #32 | M8, H4 |
| #18 | H1 (no third-party script) |
| #29 | H1, M15, M6 |
| #25 | H6, M14 |
| #28 | M10, H2, M14 |
| #21 | M16 |

#23 must confirm every row above is closed before the final specification is written.
