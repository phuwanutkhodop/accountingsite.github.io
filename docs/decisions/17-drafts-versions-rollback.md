# 17 — Drafts, versions and rollback

**Ticket:** GitHub issue #17 (Wayfinder grilling)
**Date:** 6 October 2026
**Decided by:** the owner (§2) and Claude (§3, technical choices delegated by the owner)
**Inputs:**
- decision #10, decisions 7–8 (drafts and originals in a private repo);
- decision #11 §3.3–3.6 (publish mechanics);
- decisions #13 and #14;
- research #2 §3.8 and research #4 §2.5 (history API);
- plan review findings H2, H3, M3, M4 and L4 (`docs/reviews/2026-10-06-plan-review.md`).

**Status:** locked. **Amended 6 October 2026 by #31** (`docs/decisions/31-multi-site-hosting.md`): one drafts repo per site; the master of a saved design goes straight to `builder-library`.

---

## 1. สรุปสำหรับเจ้าของกิจการ (ภาษาไทย)

1. **งานบันทึกอัตโนมัติ ไม่ต้องกดเซฟ** งานเก็บในเครื่องทันทีที่พิมพ์ และขึ้นคลาวด์ส่วนตัวอย่างน้อยทุกนาที บนแถบด้านบนมีป้ายบอกสถานะ: "บันทึกแล้ว ✓" · "กำลังบันทึก…" · "ออฟไลน์ เก็บในเครื่องแล้ว"
2. **เปิดงานต่อจากเครื่องไหนก็ได้** งานที่ยังไม่ Publish อยู่ในที่เก็บส่วนตัว คนภายนอกมองไม่เห็น
3. **กด Publish แล้วเห็นรายการงานที่แก้ทั้งหมด** งานที่พร้อมถูกติ๊กไว้ให้ เอาออกได้ ส่วนงานที่แปลยังไม่ครบจะไม่ถูกติ๊ก และบอกเหตุผล ถ้างานหนึ่งต้องขึ้นพร้อมอีกงาน ระบบติ๊กให้คู่กันเอง เช่น บทความที่ลิงก์ไปหน้าใหม่
4. **ทุกครั้งที่ Publish คือหนึ่งเวอร์ชัน** เก็บไว้ตลอดไป ตั้งชื่อเวอร์ชันได้ เช่น "ก่อนปรับราคา 2027"
5. **ย้อนได้ทั้งรายหน้าและทั้งเว็บ** ดูภาพก่อนยืนยันทุกครั้ง การย้อนเป็นการ Publish ครั้งใหม่ จึงย้อนการย้อนได้อีก
6. **การย้อนแตะเฉพาะเนื้อหาเว็บ** ตัวโปรแกรม Admin และคลังดีไซน์ไม่ถูกย้อนไปด้วย
7. **แก้หน้าเดียวกันจากสองเครื่องจนขัดกัน ระบบแสดงทั้งสองแบบให้คุณเลือก** ไม่มีงานหายโดยไม่รู้ตัว
8. **ข้อจำกัด:** ตั้งเวลา Publish ล่วงหน้าไม่ได้ เพราะระบบไม่มีเซิร์ฟเวอร์ คุณต้องกด Publish เองเมื่อถึงเวลา

---

## 2. Owner decisions

| # | Question | Decision | Why |
|---|---|---|---|
| 1 | How unpublished work is saved | **Automatically, Google-Docs style.** There is no Save button, and a status pill shows the state. | Owner choice (recommended). Work survives a crashed browser or a lost laptop. |
| 2 | What Publish publishes | **Every ready item, ticked by default; the owner can untick any of them.** Items that fail the gate (for example a missing translation) start unticked, with the reason shown. | Owner choice (recommended). It matches the top bar's change count (#24). |
| 3 | Restore | **Both per item (page or article) and whole site,** always with a preview first. | Owner choice (recommended). Research #2: Squarespace's lack of history is the most repeated owner complaint. |
| 4 | The same item edited on two devices | **Show both versions side by side; the owner chooses.** Nothing is overwritten silently. | Owner choice (recommended). |

---

## 3. Technical decisions (delegated to Claude)

### 3.1 Where work lives

| Layer | What | When it is written | Survives |
|---|---|---|---|
| **Browser** (IndexedDB) | The current state of every item being edited | About 1 s after typing stops | Closing the tab or a browser crash, on that device |
| **Drafts repo** (private, decision #10) | One draft file per changed item | Automatically: after 15 s idle, when leaving the item, when the tab is hidden, and before Publish. **At most once a minute.** | Everything, on any device |
| **Site repo** (public) | Published source plus generated output | Only on Publish | — |

- **Sync cost:** one sync is at most 3 API writes (tree with inline content, commit, ref). A once-a-minute cap stays far below GitHub's 500 writes per hour, which leaves room for image uploads (#27).
- **Offline or expired token:** edits stay in the browser and the pill says so. Sync resumes on its own after reconnecting or renewing the key (#25).

### 3.2 What an "item" is, and the draft file (resolves review H3)

A draft is **one item**: the unit that can be ticked in the Publish list. The kinds are:

| Item | Source it changes |
|---|---|
| a page | `site/pages/<id>.json`, **plus its own operations on the tree** (added, moved, deleted, its menu entry) |
| an article | `site/articles/<id>.json` |
| **Site structure** | Reordering pages, menu edits not tied to one page, and manual redirects: operations on `site/site.json` |
| Theme | `site/theme.json` |
| Settings | the identity and language fields of `site/site.json` |
| a media asset | rendition files waiting under `drafts/media/<id>/` (review H5), plus its `site/media.json` entry |
| a library design | the page's reference to a newly saved preset and its pinned copy; the master is already in `builder-library` (review M3, #13 §3.4, #31 §3-7) |

The draft file is `drafts/<kind>/<id>.json` in the private repo:

```json
{
  "schemaVersion": 1,
  "kind": "page",
  "id": "services",
  "base": "<git blob SHA of the published source this draft started from, or null if new>",
  "content": { "…": "the whole new source of the item" },
  "ops": [ { "op": "tree.move", "page": "services", "parent": "home", "index": 2 } ],
  "needs": [ "media:7f3a" ],
  "device": "<random id of the browser that saved it>",
  "savedAt": "2026-10-06T14:32:05Z"
}
```

- **`site.json` is never copied whole into a draft.** Each draft records **operations**, and Publish applies only the operations of the ticked items, in the order they were made. Publishing page A therefore cannot leak page B's unpublished menu change (review H3).
- **`needs` lists dependencies,** for example a new page linked from an article, an image, or a new design. In the Publish list, ticking an item ticks what it needs, and unticking a needed item unticks what depends on it. A note explains the pairing.
- **The usage index (#13 §3.7) reads drafts too** (review M4), so a design used only by a draft is never removed.

### 3.3 Publish

1. The Publish list shows every item that has a draft. Ready items are ticked; items that fail the gate are unticked, with the reason (owner decision 2).
2. **Conflict check:** for each ticked item, if the published source no longer matches the draft's `base`, another device published that item meanwhile. The side-by-side choice from §3.6 opens first.
3. The candidate source is the published source, plus the ticked drafts' content, plus their operations applied to `site.json`, plus any waiting renditions moved into `media/`. It goes through generation, the validation gate and the diff (decision #11 §3.1–3.5).
4. One commit; the ref update is fast-forward only (#11 §3.6).
5. Then the published drafts are deleted from the drafts repo, second, as in #10. Leftovers are detected and cleaned on the next run.

**Publish commit message.** The owner never reads git. The Admin reads these trailers:

```
Publish: 3 items — Services, VAT guide, Site structure

Builder-Publish: 1
Items: page:services article:vat-guide structure
Languages: en th zh
Restore-Of: <commit sha>        (restores only)
```

### 3.4 Versions

- **A version is one Publish commit.** Commits without `Builder-Publish`, such as Admin code updates or library work by Claude sessions, are not shown as versions.
- **The list** shows the date and time (Gregorian, Thai wording), the items with their Thai names, the languages, and an optional **name**.
- **Names are stored privately** in `labels.json` in the drafts repo, so any version can be named or renamed at any time without touching published history. Example: "ก่อนปรับราคา 2027".
- **Per-item history** lists the commits that touched that item's source file (`GET /commits?path=site/pages/<id>.json`, research #4 H2). Files are named by id (#14), so history survives slug changes.
- **Retention:** forever (§3.8).

### 3.5 Restore (resolves review H2)

**Restore never copies an old repo tree.** It turns old *source* into ordinary drafts, and those go through Publish like any other change:

| | Per item | Whole site |
|---|---|---|
| **What becomes a draft** | That item's source at the chosen version, plus its tree position | Every item whose source differs between the chosen version's `site/` and today's, including deletions and structure |
| **Untouched** | `admin/`, `library/` and any workflow file | the same |
| **Theme** | stays current | restored too, as it was then |

- **Preview** shows the result as it will look now, which is what Publish will produce. It can also show "as it looked then" from that version's own generated files.
- **Designs:** a restored item pins its old preset version. If that pinned copy was removed from `site/presets/`, it comes back from git history automatically.
- **Images** from the old version are put back by referencing their **existing git blobs** in the new tree. Nothing is re-uploaded.
- **Addresses:** if a restored page's old address now holds a redirect (#14 §3.4), the restore removes that redirect rule. Otherwise the gate would block it.
- **Unpublished drafts:** if the item already has one, the owner is asked whether to replace it.
- **A restore is a new version** with `Restore-Of:`, so it can itself be undone.
- `generated.json` is always regenerated, never copied (decision #11 §3.4).

### 3.6 Two devices (owner decision 4)

- Every device remembers the drafts-repo blob SHA of each draft it last read.
- **When saving a draft:** if that SHA has changed, another device saved since. The Admin does not overwrite. It shows both versions side by side, with time and device ("แก้จากอีกเครื่องเมื่อ 14:32"). The owner keeps one, or copies parts from the other and keeps that. There is no automatic text merge in v1.
- **When opening an item** that another device changed more recently, the newer draft loads with a notice.
- **After working offline:** if the cloud draft is unchanged, the local copy is pushed; otherwise the same comparison opens.
- **Fast-forward-only ref updates** on both repos turn races into a re-read and retry (#11 §3.6).

### 3.7 Other states

- **Discard draft:** asks for confirmation, then deletes the draft file. An *Undo* lasts for the session. Older discarded drafts remain in the private repo's history and are not offered in the UI in v1.
- **Unpublish** (take a page offline without deleting it): the page returns to the *Draft* state (#14 §3.2). On Publish its files are removed through `generated.json`, and, like a deletion, the owner chooses where its address redirects.
- **Scheduled publishing is not possible** without a server, so it is not in v1. It is stated to the owner (§1-8).

### 3.8 Git history policy (resolves review L4)

- **The public repo's history is never rewritten:** no squash, no force-push. Versions are permanent, and every rollback depends on them.
- **The drafts repo is not rewritten in v1 either.** Its size is watched with the budget and warning from #31 §6 (review M13). When it is full, a **roll-over** to a fresh drafts repo replaces rewriting (#31 §6).

---

## 4. Effects on other tickets

- **#13:** save-back is a *library design* draft (§3.2). The usage index reads drafts (M3 and M4 resolved).
- **#14:** `site.json` changes are item operations (§3.2). H3 is resolved.
- **#20:** the end-to-end proof includes a draft sync to the private repo and the fast-forward retry.
- **#24:** the top bar shows the save-status pill and the count of items with drafts.
- **#25:** a device id per browser; offline and expired-key behaviour (§3.1).
- **#27:** waiting renditions live under `drafts/media/<id>/` and are moved on Publish.
- **#28:** the Publish list with ticks and dependencies, the version list with names, restore previews, and the side-by-side comparison screen.
- **#30:** undo/redo inside the editor is separate from versions.

---

## 5. Not decided here

- The exact look of the Publish list, the version list and the comparison screen → #28.
- Compacting the drafts repo, if it is ever needed → a later maintenance ticket.
