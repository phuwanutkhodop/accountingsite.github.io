# Rarity numbers: what the measurements show (#21, step 1)

**Made:** 07 October 2026 by `tools/rarity.py` from the `signals.json` of every capture in the private `builder-research` repo. Run it again with `python tools/rarity.py <path to builder-research>`.

**What it is for:** the reviewers scored each finding's rarity by eye (1–5). This file adds the part that can be counted: which typefaces, CSS techniques and script libraries the top sites use, compared with the ordinary baseline (paid accounting templates, Big-4 Thailand, a Thai accounting firm, our current site).

## In short

1. **Type is the clearest measured gap.** 74 of 85 top sites (87%) load a licensed typeface or one made for the brand. 7 of 8 baseline sites use free fonts only.
2. **Smooth scrolling is a template trait, not a premium one.** 4 of the 4 Framer templates load Lenis smooth scrolling. Only 1 of 18 finance, law and consulting sites do (13 of 89 top sites overall; 10 of those 13 are design studios or award winners).
3. **The CSS counts are weak.** They show what a stylesheet *contains*, not what the page *uses*, and the capture could not read the CSS of 4 of the 8 baseline sites. Treat the CSS table as a hint, not proof; section 5 says how to fix it.

## Which sites count

- **Used:** 89 top sites and 8 baseline sites.
- **Left out (12):** `a16z.com` (did not load); `aesop.com` ("Just a moment..." page instead of the site); `awwwards.com_websites_sites_of_the_year` (did not load); `cleary.com` (did not load); `jacquemus.com` ("Our website is currently undergoing brie" page instead of the site); `loropiana.com_en` ("Access Denied" page instead of the site); `lusion.co` (did not load); `mckinsey.com` ("Access Denied" page instead of the site); `mucho.ag` (did not load); `rosewoodhotels.com_en_bangkok` (same brand as another capture); `rothschildandco.com_en` ("Just a moment..." page instead of the site); `ledgerhouse.framer.website` ("Site Not Found | Framer" page instead of the site).
- **CSS not readable** (under 10 KB of stylesheets captured; the site puts its CSS inside the page): top: `andwalsh.com`, `arc.net`, `buildinamsterdam.com`, `family.co`, `framer.com`, `igloo.inc`, `rolex.com`, `scb.co.th_en_personal-banking.html`, `sequoiacap.com`, `tekt.com.au`, `the-brandidentity.com`; baseline: `accora.framer.website`, `accura.framer.website`, `ashworth.framer.website`, `auditly.framer.website`. These sites still count for typefaces and libraries, but not in the CSS table.

## 1. Typefaces

Each site is put in one class by the text faces it loaded (icon fonts ignored):
- **own face:** a face made for the brand (it carries the brand's name, or is publicly the brand's own; listed in the appendix);
- **licensed:** at least one face that is not free (bought from a foundry, or an unnamed custom alias);
- **free only:** Google Fonts or other open-licence faces only.

| Group | Sites with fonts | Own face | Licensed | Free only | Own + licensed |
|---|---|---|---|---|---|
| **All top sites** | 85 | 23 (27%) | 51 (60%) | 11 (13%) | 87% |
| finance / law / consulting | 18 | 5 (28%) | 9 (50%) | 4 (22%) | 78% |
| luxury | 10 | 4 (40%) | 4 (40%) | 2 (20%) | 80% |
| editorial / craft | 17 | 6 (35%) | 10 (59%) | 1 (6%) | 94% |
| Thai | 6 | 2 (33%) | 3 (50%) | 1 (17%) | 83% |
| design studios | 20 | 4 (20%) | 15 (75%) | 1 (5%) | 95% |
| award winners | 14 | 2 (14%) | 10 (71%) | 2 (14%) | 86% |
| **Baseline (ordinary)** | 8 | 1 (12%) | 0 (0%) | 7 (88%) | 12% |

Top sites with free faces only: `centerviewpartners.com`, `hermes.com_us_en`, `hoaresbank.co.uk`, `maisonlesgrandschenes.com`, `patek.com_en_home`, `pwpartners.com`, `ragged-edge.com`, `raycast.com`, `tilleke.com`, `unanima.uk`, `wlrk.com`.

*Observation (judgement, not measured):* free fonts do not make a site cheap on their own; the sites above use free faces only. The baseline's problem is free faces **plus** the template habits in `baseline.md`. A licensed face is a visible sign that money was spent, and the builder already supports any self-hosted face (decision #15).

## 2. CSS techniques

Share of the 78 top sites whose CSS was readable, against the 4 readable baseline sites (ey.com_en_th, kpmg.com_th_en_home.html, phuwanutkhodop.github.io_accountingsite.github.io_en, sa-accounttax.com). Bands: common ≥ 50%, uncommon 20–49%, rare < 20%.

| Technique | Top sites | Baseline | Band |
|---|---|---|---|
| sticky positioning | 77% (60) | 3 of 4 | common |
| multi-column text | 74% (58) | 4 of 4 | common |
| clip-path shapes/reveals | 64% (50) | 2 of 4 | common |
| backdrop blur | 60% (47) | 0 of 4 | common |
| 3D transforms | 56% (44) | 2 of 4 | common |
| CSS masks | 46% (36) | 3 of 4 | uncommon · loose pattern |
| blend modes | 38% (30) | 0 of 4 | uncommon |
| variable-font axes | 31% (24) | 0 of 4 | uncommon |
| custom cursor (cursor:none) | 31% (24) | 1 of 4 | uncommon |
| oldstyle/tabular numerals | 29% (23) | 0 of 4 | uncommon |
| text-wrap balance/pretty | 28% (22) | 0 of 4 | uncommon |
| container queries | 13% (10) | 2 of 4 | rare |
| gradient text | 13% (10) | 1 of 4 | rare |
| marquee keyframes | 12% (9) | 1 of 4 | rare |
| subgrid | 10% (8) | 0 of 4 | rare |
| drop caps (initial-letter / first-letter) | 9% (7) | 0 of 4 | rare |
| grain/noise texture | 9% (7) | 0 of 4 | rare · loose pattern |
| text stroke / outline type | 5% (4) | 1 of 4 | rare |
| hanging punctuation | 5% (4) | 0 of 4 | rare |
| view transitions | 4% (3) | 0 of 4 | rare |
| small caps | 4% (3) | 0 of 4 | rare |
| scroll-driven animation | 3% (2) | 0 of 4 | rare |
| writing-mode vertical text | 3% (2) | 0 of 4 | rare |
| shape-outside text wrap | 0% (0) | 0 of 4 | rare |

Large sites ship large stylesheets that contain rules they never show on the page (Bottega Veneta and KKR load over 4 MB of CSS), so a "yes" here means "available", not "seen".

**By group** (share of readable sites in each group):

| Technique | finance / law / consulting (17) | luxury (9) | editorial / craft (13) | Thai (7) | design studios (19) | award winners (13) |
|---|---|---|---|---|---|---|
| scroll-driven animation | 6% | 0% | 8% | 0% | 0% | 0% |
| view transitions | 0% | 0% | 15% | 0% | 5% | 0% |
| blend modes | 18% | 44% | 46% | 29% | 79% | 0% |
| clip-path shapes/reveals | 41% | 67% | 92% | 57% | 74% | 54% |
| CSS masks | 29% | 44% | 62% | 86% | 58% | 15% |
| backdrop blur | 41% | 67% | 77% | 57% | 63% | 62% |
| text stroke / outline type | 0% | 11% | 23% | 0% | 0% | 0% |
| variable-font axes | 18% | 0% | 31% | 29% | 47% | 46% |
| drop caps (initial-letter / first-letter) | 24% | 11% | 0% | 14% | 5% | 0% |
| multi-column text | 82% | 89% | 85% | 86% | 53% | 69% |
| hanging punctuation | 6% | 11% | 15% | 0% | 0% | 0% |
| text-wrap balance/pretty | 18% | 11% | 46% | 14% | 37% | 31% |
| subgrid | 6% | 11% | 31% | 0% | 5% | 8% |
| container queries | 18% | 33% | 23% | 0% | 5% | 0% |
| sticky positioning | 71% | 89% | 85% | 71% | 74% | 77% |
| 3D transforms | 71% | 56% | 54% | 57% | 58% | 38% |
| custom cursor (cursor:none) | 29% | 44% | 23% | 14% | 53% | 8% |
| grain/noise texture | 6% | 11% | 8% | 29% | 11% | 0% |
| oldstyle/tabular numerals | 18% | 22% | 69% | 0% | 26% | 31% |
| small caps | 6% | 0% | 8% | 0% | 5% | 0% |
| gradient text | 6% | 11% | 31% | 0% | 16% | 8% |
| marquee keyframes | 6% | 0% | 23% | 0% | 16% | 15% |
| writing-mode vertical text | 0% | 0% | 0% | 0% | 11% | 0% |
| shape-outside text wrap | 0% | 0% | 0% | 0% | 0% | 0% |

## 3. Script libraries

Share of all 89 top sites against all 8 baseline sites.

| Library | Top sites | Baseline | Note |
|---|---|---|---|
| three.js / WebGL | 34% (30) | 1 of 8 | loose pattern |
| gsap | 26% (23) | 0 of 8 | |
| barba | 17% (15) | 0 of 8 | |
| lenis | 15% (13) | 4 of 8 | |
| splitting | 13% (12) | 3 of 8 | loose pattern |
| lottie | 12% (11) | 0 of 8 | |
| swup | 4% (4) | 0 of 8 | |
| webflow | 3% (3) | 0 of 8 | |
| framer | 2% (2) | 4 of 8 | |
| locomotive-scroll | 1% (1) | 0 of 8 | |
| rive | 1% (1) | 0 of 8 | |

**By group:**

| Library | finance / law / consulting (18) | luxury (10) | editorial / craft (17) | Thai (8) | design studios (21) | award winners (15) | baseline (8) |
|---|---|---|---|---|---|---|---|
| gsap | 22% | 30% | 12% | 12% | 29% | 47% | 0% |
| lenis | 6% | 10% | 6% | 0% | 19% | 40% | 50% |
| barba | 6% | 50% | 24% | 0% | 10% | 20% | 0% |
| lottie | 17% | 10% | 6% | 12% | 14% | 13% | 0% |
| three.js / WebGL | 6% | 60% | 35% | 50% | 38% | 33% | 12% |

## 4. What this means for the presets

Measured:
- Own or licensed type: 87% of top sites, against 12% of the baseline.
- Smooth scrolling: 4 of 4 paid templates, 1 of 18 finance, law and consulting sites.

Judgement *(ข้อคิดเห็น)*, for the owner board and the preset quality bar:
- **Type carries the premium signal more than effects do.** When the owner judges presets, show them set in a serious licensed face as well as in the free test-theme faces, so a weak preset cannot pass, and a good one cannot fail, because of the face alone.
- **No smooth scrolling and no scroll-jacking in presets.** The firms we want to resemble almost never use it (1 of 18); the paid templates all do.
- **Animation libraries are not what sets the firms apart.** GSAP loads on 4 of 18 finance, law and consulting sites and on 13 of 36 studio and award sites. Studios use motion to show off their own craft. A firm's presets should not depend on it, and must read fully without it.
- The CSS table is too weak to rank craft details such as numerals, small caps or multi-column text. The reviewers' rarity scores remain the main guide for those until the measurement is fixed (section 5).

## 5. Limits, and how to make the numbers trustworthy

- **Presence, not use.** `capture.cjs` tests stylesheet *text* with a pattern, so a rule that is never applied still counts. Fix: measure on the rendered page (for example, how many visible elements use tabular figures, sticky positioning or small caps).
- **Inline CSS is missed.** Only separate stylesheet files are read, so Framer and CSS-in-JS sites look empty. Fix: also read `<style>` blocks and `document.styleSheets`.
- **Loose patterns:** *grain/noise texture* matches the words "noise" or "grain" anywhere in the CSS; *CSS masks* also matches vendor icon and image masks; *three.js / WebGL* matches the word "webgl" in any script (feature checks, maps, analytics); *splitting* matches the word "splitting" in any script.
- **Small baseline:** only 4 baseline sites have readable CSS, and none of them is a paid template.
- Fonts list only faces loaded near the top of the page (first 12).

Both fixes need the signal step to run again over the same sites in a real browser. No new screenshots are needed. This is a separate step and waits for the owner's OK.

## Appendix: per-site classification

| Site | Group | Type class | Faces (icons removed) | CSS readable | Libraries |
|---|---|---|---|---|---|
| `bain.com` | finance / law / consulting | licensed | Tiempos, Graphik, graphik, graphiklight | yes | gsap, barba |
| `bcg.com` | finance / law / consulting | own | Henderson BCG | yes | gsap, splitting, lottie |
| `centerviewpartners.com` | finance / law / consulting | free | Nunito Sans | yes | – |
| `coutts.com` | finance / law / consulting | own | Coutts Siena / Coutts Forme | yes | – |
| `cravath.com` | finance / law / consulting | licensed | Bembo, Franklin Gothic ITC | yes | – |
| `evercore.com` | finance / law / consulting | licensed | IBM Plex Sans, Giorgio Sans | yes | – |
| `freshfields.com` | finance / law / consulting | own | Freshfields Headline / Text | yes | – |
| `hoaresbank.co.uk` | finance / law / consulting | free | Trirong, Lato | yes | – |
| `juliusbaer.com_en` | finance / law / consulting | licensed | VerlagSSmforBaerVar | yes | splitting |
| `kkr.com` | finance / law / consulting | licensed | Ghost, Ghost Bold, Ghost Medium, Ghost Light | yes | – |
| `lazard.com` | finance / law / consulting | licensed | Helvetica Neue LT W02_51488892, VC Garamond | yes | – |
| `lombardodier.com` | finance / law / consulting | own | Lombard Odier | yes | – |
| `pictet.com` | finance / law / consulting | licensed | Lardy Serif, Lardy Sans | yes | gsap, three.js / WebGL |
| `pjtpartners.com` | finance / law / consulting | own | pjtSans | yes | – |
| `pwpartners.com` | finance / law / consulting | free | Work Sans | yes | – |
| `sequoiacap.com` | finance / law / consulting | licensed | Rosart Regular, Pitch Sans Regular, Unica77 Web Regular, Inter | no | lenis, framer, lottie |
| `slaughterandmay.com` | finance / law / consulting | licensed | Open Sans, Feature Deck | yes | gsap, lottie |
| `wlrk.com` | finance / law / consulting | free | Playfair Display | yes | – |
| `aman.com` | luxury | licensed | Lyon Display Web, Lyon Text Web, WhitneySSm | yes | – |
| `bottegaveneta.com_en-us` | luxury | own | Bottega Veneta | yes | three.js / WebGL, barba |
| `byredo.com` | luxury | own | byredoSans | yes | barba |
| `cartier.com_en-us` | luxury | own | Brilliant Cut / Fancy Cut | yes | three.js / WebGL |
| `hermes.com_us_en` | luxury | free | Manrope, EBGaramond, Overpass Mono | yes | gsap, three.js / WebGL, splitting |
| `lemaire.fr` | luxury | licensed | BrownStd, GaramondPremrPro | yes | three.js / WebGL, barba |
| `patek.com_en_home` | luxury | free | lora, openSans | yes | gsap, lenis, splitting, lottie |
| `rolex.com` | luxury | own | RolexFont | no | – |
| `rosewoodhotels.com_en_default` | luxury | licensed | Engravers Gothic Bold, Austin Light Web, Austin Light Web Italic, Swiss 721 Black Condensed | yes | three.js / WebGL, barba, splitting |
| `therow.com` | luxury | licensed | Basic Commercial | yes | gsap, three.js / WebGL, barba |
| `apartamentomagazine.com` | editorial / craft | licensed | futura-pt | yes | three.js / WebGL |
| `apple.com` | editorial / craft | own | SF Pro | yes | three.js / WebGL |
| `arc.net` | editorial / craft | licensed | Marlin, Inter, InterVariable, ABC Favorit Mono, Marlin Soft SQ | no | barba |
| `family.co` | editorial / craft | own | Family | no | – |
| `framer.com` | editorial / craft | licensed | GT Walsheim Medium, Input Mono Regular, Inter, Inter Variable, JetBrains Mono | no | framer |
| `itsnicethat.com` | editorial / craft | licensed | Bradford, LabilVariable, Labil | yes | – |
| `kinfolk.com` | editorial / craft | own | Kinfolk Serif / Sans | yes | gsap, lenis, barba, swup |
| `linear.app` | editorial / craft | licensed | Inter Variable, Berkeley Mono | yes | – |
| `press.stripe.com` | editorial / craft | licensed | Ivar Display, Ivar Headline, Ivar Text | yes | three.js / WebGL |
| `pudding.cool` | editorial / craft | licensed | Atlas Grotesk, Atlas Typewriter, Gooper SemiCondensed | yes | – |
| `rauno.me` | editorial / craft | licensed | X | yes | – |
| `raycast.com` | editorial / craft | free | Inter, JetBrains Mono, GeistMono | yes | gsap, three.js / WebGL |
| `stripe.com` | editorial / craft | licensed | sohne-var, SourceCodePro | yes | three.js / WebGL |
| `teenage.engineering` | editorial / craft | own | te-20 / te-40 | yes | splitting, lottie |
| `the-brandidentity.com` | editorial / craft | licensed | Times Now, NB International Pro | no | barba, webflow |
| `theatlantic.com` | editorial / craft | own | Atlantic Serif | yes | webflow |
| `vercel.com` | editorial / craft | own | Geist | yes | three.js / WebGL, barba |
| `cadsondemak.com` | Thai | licensed | Graphik TH, Graphik Thai Loop | yes | – |
| `capellahotels.com_en_capella-bangkok` | Thai | licensed | Goudy Light, Goudy Regular, Calibre | yes | three.js / WebGL |
| `farmgroup.co.th` | Thai | own | Farm Sans | yes | swup |
| `mandarinoriental.com_en_bangkok_chao-phraya-river` | Thai | licensed | Futura PT, Futura PT Medium, AvenirNext LT Pro, AvenirNext LT Pro Bold, MO Exceptional | yes | three.js / WebGL |
| `pwc.com_th_en.html` | Thai | own | PwC Charter / Helvetica | yes | three.js / WebGL |
| `scb.co.th_en_personal-banking.html` | Thai | unknown | – | no | gsap, three.js / WebGL |
| `tilleke.com` | Thai | free | Poppins, Source Sans Pro, Roboto | yes | lottie |
| `wcp.co.th` | Thai | unknown | – | yes | – |
| `andwalsh.com` | design studios | licensed | Maison | no | – |
| `area17.com` | design studios | licensed | SuisseIntl | yes | gsap, three.js / WebGL, swup |
| `basicagency.com` | design studios | licensed | SctoGroteskA | yes | – |
| `buildinamsterdam.com` | design studios | licensed | RecklessNeue-Book, NHaasGroteskTXPro, NHaasGroteskDSPro | no | – |
| `collins1.com` | design studios | licensed | Portrait Text, Graphik | yes | lottie |
| `dixonbaxi.com` | design studios | licensed | Aeonik Fono, Iskry | yes | lenis, lottie |
| `dogstudio.co` | design studios | licensed | Heebo, GT Sectra Display, Gilroy | yes | three.js / WebGL |
| `fantasy.co` | design studios | licensed | sans | yes | gsap, lenis, three.js / WebGL |
| `heystudio.es` | design studios | unknown | – | yes | three.js / WebGL |
| `instrument.com` | design studios | own | Instrument Serif / Sans | yes | gsap, three.js / WebGL, splitting |
| `koto.studio` | design studios | own | GT Kotoheim | yes | gsap, three.js / WebGL, splitting, rive |
| `locomotive.ca_en` | design studios | own | LocomotiveNew | yes | three.js / WebGL, barba |
| `manualcreative.com` | design studios | licensed | ABCOracle-797018b588059137, ABCOtto-478c268553af3f8b | yes | – |
| `obys.agency` | design studios | own | Obys | yes | three.js / WebGL |
| `order.design` | design studios | licensed | Pitch Sans | yes | – |
| `pentagram.com` | design studios | licensed | Plain | yes | gsap, barba |
| `ragged-edge.com` | design studios | free | Open Sans, Roboto, Cagliostro | yes | – |
| `spin.co.uk` | design studios | licensed | gerstner | yes | lenis |
| `studiofreight.com` | design studios | licensed | jjannon-regular, publico-text-mono-roman, publico-text-mono-semibold | yes | gsap, lenis |
| `superunion.com` | design studios | licensed | Sequel Sans | yes | lottie |
| `wolffolins.com` | design studios | licensed | Monument-Grotesk, Untitled-Serif, WO | yes | – |
| `archives.surfersjournal.com` | award winners | licensed | Plain, Practice | yes | gsap, lenis |
| `boc.studio` | award winners | licensed | ppMori | yes | gsap, lenis, three.js / WebGL, splitting |
| `eladiodieste.com` | award winners | licensed | font | yes | gsap, lenis, splitting |
| `exemplarfromsweden.com` | award winners | own | Exemplar | yes | – |
| `igloo.inc` | award winners | unknown | – | no | three.js / WebGL |
| `jakobsencopenhagen.com` | award winners | licensed | ABC Arizona Flare, ABC Arizona Sans | yes | lenis |
| `lambert-lambert.com` | award winners | licensed | System-Medium, Zurich-Black | yes | – |
| `maisonlesgrandschenes.com` | award winners | free | eb-garamond | yes | – |
| `mejuma-tuscany.com` | award winners | licensed | Made Mirage, Roxale Story 400, Golos Text | yes | gsap, lenis, locomotive-scroll, barba, splitting, webflow, lottie |
| `palaraiffeisen.ch` | award winners | licensed | APK Systema Regular, APK-Narrative-Regular, APK-Narrative-Medium | yes | gsap, three.js / WebGL |
| `redcollar.co` | award winners | own | RedCollar | yes | – |
| `sort-office.com` | award winners | licensed | custom_115681 | yes | three.js / WebGL, barba, lottie |
| `tekt.com.au` | award winners | licensed | af Another Sans, Herbik | no | gsap, swup |
| `terrenohotel.com_en` | award winners | licensed | PP Monument Extended, Tiempos Text, WT Central Avenue, Blitz Script | yes | three.js / WebGL |
| `unanima.uk` | award winners | free | DM Mono, Lora, Mona Sans | yes | gsap, lenis, barba, splitting |
| `accora.framer.website` | baseline | free | Geist, Hedvig Letters Serif, Cabinet Grotesk | no | lenis, framer |
| `accura.framer.website` | baseline | free | Inter | no | lenis, framer |
| `ashworth.framer.website` | baseline | free | Cormorant SC, Playfair Display, Inter, Manrope | no | lenis, framer |
| `auditly.framer.website` | baseline | free | Apfel Grotezk | no | lenis, framer |
| `ey.com_en_th` | baseline | own | EYInterstate | yes | three.js / WebGL, splitting |
| `kpmg.com_th_en_home.html` | baseline | free | OpenSans--Regular, OpenSans--SemiBold, OpenSans_Condensed--Bold | yes | splitting |
| `phuwanutkhodop.github.io_accountingsite.github.io_en` | baseline | free | Instrument Serif, Inter | yes | – |
| `sa-accounttax.com` | baseline | free | Prompt | yes | splitting |
