# Handoff — 7 October 2026: from the cloud session to a local session

> **Parked, 7 Oct 2026 (owner):** the builder core comes first. This #21 design work waits until the owner reopens
> it. Its latest state and the open questions are in `PROJECT-STATUS.md` ("#21 is parked here").

**Read this after `PROJECT-STATUS.md`.** It holds everything the next chat needs to continue the builder work exactly
where the cloud session stopped. The owner is moving to a local Claude Code session because of the cloud budget.

---

## 1. Where everything is

| What | Where | Note |
|---|---|---|
| All code and docs of this work | branch `claude/house-number-security-multisite-hw1z56` | **Not merged yet.** PR [phuwanutkhodop/accountingsite.github.io#46](https://github.com/phuwanutkhodop/accountingsite.github.io/pull/46) covers it. Merge it, or check out this branch, before continuing. |
| Decision #31 (hosting, security origin) | `docs/decisions/31-multi-site-hosting.md` | closed |
| Decision #15 (trilingual type system) | `docs/decisions/15-type-system.md` + `15-type-system/prototype/` | closed; owner device check pending |
| Decision #21 (preset format) | `docs/decisions/21-section-library-sample.md` + `21-section-library-sample/prototype/` | **reopened**: the format stands, the designs failed (§8) |
| Visual research: findings text | `docs/research/21-visual-research/` | 114 findings + baseline, no images |
| Visual research: **all images** (1,623 screenshots, 127 crops, tools) | private repo **`phuwanutkhodop/builder-research`** | screenshots of other companies' sites: **never** put them in this public repo |
| #15 specimen (owner check) | https://claude.ai/artifact/GHqZLEnpmiRVAau4KWdQnX | private |
| #21 sample (rejected designs) | https://claude.ai/artifact/KXF9kgSGvYtTJFXS46CUQC | private; kept only as the "what not to do" reference |

## 2. What happened in the cloud session

1. **#31 closed:**
   - the Admin runs on its own origin (a free GitHub organization, `https://<admin-org>.github.io/admin/`);
   - one publishing key covers every site repo, each private `<site>-drafts` repo and `builder-library`;
   - hard security rules A1–A4 and S1–S3 went to tickets #18, #22, #25, #27, #28 and #29.
2. **#15 closed:**
   - fonts are set by role: 3 roles × Latin/Thai/Chinese, normalised to one x-height;
   - no Google Fonts: every face is subset at Publish with HarfBuzz WASM (proven under the strict CSP).
3. **#21: the format was proven, then the owner rejected the designs.** Their words: *"far from professional; nobody would pay for this."* The owner ordered:
   - research of top professional work **by looking at it**;
   - collect only **scarce, distinctive, high-value** details;
   - build those into real presets.
4. **The network was opened** (environment set to Full) and 97 top sites plus 9 baseline sites were captured. Four reviewer agents looked at every frame of their groups.

## 3. The research: state and next steps

**Done** (per-group files in `docs/research/21-visual-research/` and in `builder-research/findings/`):

| Group | Sites reviewed | Findings | Strongest (rarity × fit) |
|---|---|---|---|
| finance / law / consulting | 16 | 45 | Pictet line-drawing timeline (world events below the line, the firm's own above); Evercore "(values in millions)" unit captions; Lazard dated transactions ledger with "Undisclosed" allowed; PWP service diagrams instead of icons; Slaughter and May expanding matter tiles |
| luxury | 8 | 21 | Rolex "Reduce motion / Contrast" switches in the footer; Lemaire exposed index header (whole menu as columns); Aman gazetteer footer with status notes; Aman old-style figures in prose and lining in lists; Rolex signature sign-off before the footer |
| editorial / craft | 14 | 35 | teenage.engineering permanent second-script mission block; The Atlantic "(From 2015)" provenance stamp; teenage.engineering glyph navigation with sub-index; Vercel multilingual stacked word plate; Linear "FIG 0.1" numbered line plates |
| Thai | 7 | 13 | Cadson Demak Thai and Latin cut as one voice; type-as-cover article cards; language offered as an "Edition"; rotating multi-script greeting with a script index; Capella indented body column that survives on phone |
| baseline | 9 | — | the 10 patterns that define "ordinary" (`baseline.md`): the hero formula, the centred section and 3 cards, count-up number trios, fake proof, stock imagery, rounded everything, one loud accent, a fixed section order, decorative motion, generic copy |

**Cross-group pattern worth a preset family:** the "statement register". Top finance sites present figures and work the
way financial statements do: figure · unit · label · note · "as at" date, and dated registers of work. It is the
natural signature for an accounting firm.

**Open choice put to the owner. Answered 7 Oct 2026: option 1.** Done the same day: 35 sites triaged, the best 12
reviewed. Results and the synthesis of all findings are in `builder-research/findings/` (`studio-award.*`, `synthesis.md`).
1. *Economical (recommended):* one reviewer for the best 12 studio and award sites, then synthesise.
2. *Complete:* review all ~34 studio and award sites.
3. *Stop:* synthesise from the 114 findings.

**After that choice, the remaining steps:**
1. **Rarity numbers:** count each technique across all `signals.json` and compare top sites with the baseline.
   **Done 7 Oct 2026 (local session):** `docs/research/21-visual-research/rarity.md`. Own or licensed type on 87% of top
   sites against 1 of 8 baseline sites; Lenis smooth scrolling on all 4 paid templates against 1 of 18 finance, law and
   consulting sites. The CSS counts are weak (presence, not use; inline CSS missed); its §5 says how to fix the capture.
2. **Board for the owner** (owner's method: many options, each in real context). **Published 7 Oct 2026:**
   https://claude.ai/artifact/52fmRo9YhVoCp4mbSfjMNY. The picks are in its database (`picks`); the source is in `builder-research/board/`.
   - group the findings by role (opening, navigation, proof/data, process, people, knowledge, contact, footer, type system);
   - show each finding with its crop, then the owner picks;
   - publish it as a private artifact, with the images taken from `builder-research`.
3. **Build real presets** from the owner's picks:
   - follow the #21 format (§2), which still stands;
   - meet a new quality bar derived from the research. The §4 list is only the floor;
   - presets go into `builder-library` (owner step: create that repo first, as in #31 §8).
4. Close #21 only when the owner accepts the new presets as commercial grade.

## 4. Lessons from the capture work

- **Smooth-scroll sites** (Lenis, Locomotive) report a one-screen page. `capture.cjs` therefore keeps scrolling by wheel anyway; this is fixed.
- **Some sites block automated browsers:** Aesop, Hermès, Loro Piana, McKinsey and Rothschild sometimes do. Check every capture for a bot wall before reviewing it.
- **Never wait with `pgrep -f "capture.cjs"`:** it matches its own command line and never ends.
- **Reviewers share `findings/crops/`,** so each must prefix crop names with its group or site.
- **Cost:** each reviewer agent used about 200–300k tokens. Keep reviewer batches small and say how many there will be up front.

## 5. Pending owner actions (unchanged)

- **#15:** open the specimen on Windows (Edge) and iPhone. Check whether Thai marks clip, and whether size matching reads better on or off.
- **Before #22:** create the free GitHub organization for the Admin.
- **Before writing real presets:** create the public `builder-library` repo and add it to the publishing key.

## 6. Moving to local (owner, Windows)

1. Install **Git**, **Node.js 22 LTS** and **Claude Code**.
2. Clone both repos:
   - `git clone https://github.com/phuwanutkhodop/accountingsite.github.io`
   - `git clone https://github.com/phuwanutkhodop/builder-research`
3. In `accountingsite.github.io`: `git checkout claude/house-number-security-multisite-hw1z56`, or merge PR #46 first.
4. Either start a new chat there and say: *"read PROJECT-STATUS.md and docs/handoff/2026-10-07-cloud-to-local.md, then continue"*,
   or continue this exact conversation with `claude --teleport <session-id>` (claude.ai/code → the session menu → Open in → Terminal).
5. Cloud and local sessions draw from the same plan limits; moving does not change the cost of the work itself.
