# 20 — Token and browser-only publish: proved end to end

**Ticket:** GitHub issue #20 (Wayfinder task)
**Date:** 6 October 2026
**Done by:** the owner, who created the repo and the key and ran the test, with Claude, who built the test page and checked the result
**Inputs:**
- research #4 (publishing), including its §5 draft guide;
- decisions #10, #11 §3.3–3.6 and #17;
- plan review findings H6, M10, M11 and M12.

**Status:** done. Every step passed on the first real run.
**Follow-up (#31, `docs/decisions/31-multi-site-hosting.md` §8):** the key later also covers `builder-library` and each new site's two repos. It never covers the Admin, which lives under a separate GitHub organization.

---

## 1. สรุปสำหรับเจ้าของกิจการ (ภาษาไทย)

1. **ระบบที่ออกแบบไว้ทำงานได้จริง** การทดสอบครั้งแรกผ่านครบ 11 ขั้น บน Edge ในเครื่อง Windows ของคุณ
2. **เบราว์เซอร์ Publish ขึ้นเว็บเองได้ โดยไม่มีเซิร์ฟเวอร์** หน้าเว็บขึ้นจริงภายใน 34 วินาทีหลังกด
3. **GitHub ปฏิเสธการเขียนทับงานที่ล้าสมัย** ข้อนี้คือสิ่งที่ป้องกันงานหายเมื่อแก้จากสองเครื่อง
4. **ที่เก็บส่วนตัวสำหรับฉบับร่างใช้งานได้** เขียน อ่าน และลบได้ครบ
5. **ไฟล์ทดสอบถูกลบออกเองแล้ว** เว็บกลับมาเหมือนเดิมทุกไฟล์
6. **กุญแจของคุณหมดอายุวันที่ 7 ตุลาคม 2027** ระบบจะเตือนล่วงหน้า 14 วัน กุญแจต้องอยู่ในโปรแกรมเก็บรหัสผ่านเท่านั้น
7. **หน้าทดสอบถูกลบออกจากเว็บแล้ว** เพราะใช้ครั้งเดียว

---

## 2. What was set up (the owner)

| Item | Value |
|---|---|
| Private drafts repo | `phuwanutkhodop/accountingsite-drafts`, private, initialised with a README so that `main` exists |
| Fine-grained token | Name "D.A. Website Admin key". Repositories: **only** `accountingsite.github.io` and `accountingsite-drafts`. Permissions: **Contents: read and write**, **Pages: read-only**, Metadata: read-only (automatic). Nothing else. |
| Expiry | **7 October 2027.** The owner entered it, because the browser cannot read it (H6). |
| Browser | Microsoft Edge 154 on Windows |

## 3. Results (run `21d83794b47c`, 2026-10-06 17:43 UTC)

| # | Step | Result | Time |
|---|---|---|---|
| 1 | Identity: `GET /user` | ✓ `phuwanutkhodop`. The rate-limit header is readable; **the token-expiry header is not** (H6 confirmed). | 0.7 s |
| 2 | Site repo and Pages read | ✓ public; `main`; Pages source `main` `/` | 1.3 s |
| 3 | Drafts repo | ✓ private; `main` | 0.7 s |
| 4 | Recursive tree read | ✓ 334 entries, not truncated | 1.9 s |
| 5 | Local blob SHA against git | ✓ Matches for an existing file and for Thai and Chinese text. The string-length method would have been wrong (M11). | 1.5 s |
| 6 | Two files in one commit, fast-forward only | ✓ `c67912b` | 3.1 s |
| 7 | Stale ref update | ✓ **Refused with HTTP 422.** This is the concurrency guard in #11 §3.6 and #17 §3.6. | 1.6 s |
| 8 | Wait until live (content check) | ✓ **Live after 34 s.** Pages build status still read "building" at that moment, which confirms the M10 rule: trust the served content, not the build status. | 32 s |
| 9 | Remove the test files | ✓ `0a92fd7`. The site tree is now identical to before the test (verified with git). | 4.8 s |
| 10 | Drafts repo: write, read back, delete | ✓ | 7.6 s |
| 11 | `X-GitHub-Api-Version` header from the browser | ✓ **Allowed.** GitHub's documented CORS list is out of date here. | 0.6 s |

**Timing of one small publish:** about 3 s of API calls, then about 30–35 s until GitHub Pages serves the new files. This matches research #4's figure of about 40 s.

## 4. What this settles

- **The publish architecture in research #4 and decisions #10, #11 and #17 works as designed** with the exact permissions above. No GitHub Actions are needed.
- **One token covers both repos,** as decision #10 requires.
- **Hashing:** git blob length counts UTF-8 bytes, which is now proven in a real browser against real git. Every text file is written with LF; `* text=auto eol=lf` is in `.gitattributes` (M11 closed).
- **`.nojekyll` is in place** (M12 closed). The Pages build after adding it succeeded and the site is unchanged.
- **The Admin may send `X-GitHub-Api-Version: 2022-11-28`.** It should, so that a future default API version cannot change behaviour silently. Decision #16 §4.1 is updated.
- **"Is it live?" check:** compare served content against the commit, as step 8 did; build status alone lags (M10 confirmed).
- **Token expiry:** the Admin asks for the date at setup (H6 confirmed). This key's date is 7 October 2027.
- **Lesson for the owner guide:** create the drafts repo **before** opening the token page. A repo created afterwards does not appear in the selector until that page is reloaded. This is what happened during setup.

## 5. Owner guide: the publishing key (verified on 6 October 2026)

This replaces the draft in research #4 §5. It becomes part of the illustrated guide in the Admin's onboarding (#25).

1. **Create the drafts repo first:**
   - open https://github.com/new;
   - name it `accountingsite-drafts`;
   - choose **Private**;
   - tick **Add a README file**;
   - click **Create repository**.
2. **Open the pre-filled token form** (fills in name, description, 365 days, Contents write, Pages read):
   `https://github.com/settings/personal-access-tokens/new?name=D.A.+Website+Admin+key&description=Used+only+by+/admin/+on+the+firm+website&expires_in=365&contents=write&pages=read`
   If you made the repo after opening this page, reload it.
3. **Resource owner:** `phuwanutkhodop`.
4. **Repository access:** choose **Only select repositories**, then pick `accountingsite.github.io` and `accountingsite-drafts`. Type `drafts` in the search box if the list is long.
5. **Permissions:**
   - Contents: **Read and write**;
   - Pages: **Read-only**;
   - Metadata: **Read-only** (set automatically);
   - everything else: **No access**.
6. **Generate the token, then copy it.** GitHub shows it **once**. Store it in a password manager. Never paste it in chat, LINE or email.
7. **Note the expiry date.** The Admin will ask for it.
8. **If it leaks:**
   - go to GitHub → Settings → Developer settings → Fine-grained tokens and **Delete** it;
   - make a new one with these steps.

   The website stays online meanwhile.

## 6. Clean-up

- The test page `admin/proof/` was removed after the run, so it is no longer served on the Admin's origin. It remains in git history at commit `14890d7` if it is ever needed again.
- The two test commits (`c67912b`, `0a92fd7`) stay in public history. Public history is never rewritten (#17 §3.8). The Admin's version list will not show them, because they carry `Builder-Proof`, not `Builder-Publish`.
