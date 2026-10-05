# Trilingual (EN / TH / ZH-Hans) web font candidates for a luxury-refined accounting & advisory site

Research date: 2026-10-05. Method note: most foundry websites (Klim, Commercial Type, Pangram Pangram, Cadson Demak, Sharp Type, Grilli, Displaay, Adobe Fonts, MyFonts, fonts.google.com specimen pages, GitHub web UI) were **blocked by this session's network proxy**, so foundry prices below come from search-engine summaries and are flagged as unverified. What *could* be reached directly — the Google Fonts CSS2 API (`fonts.googleapis.com`), the `google/fonts` repository on raw.githubusercontent.com, and font project READMEs — was measured first-hand: file sizes, subsets, weight ranges, licences. Those numbers are primary measurements taken on 2026-10-05 with a desktop Chrome user-agent (WOFF2).

---

## Q1. Latin display serifs in the Cormorant character (free and commercial)

### Takeaway
The free Cormorant family is the best fit for the owner's choice and is very cheap to load: about 35–37 KB for the whole 300–700 variable range (Latin subset). Free alternatives with a similar fine, high-contrast character are Gloock and, further away, Bodoni Moda or Playfair, which the owner turned down. Commercial "luxury house" display serifs (Canela, GT Super, Ogg, Saol, Tiempos Headline, Editorial New) cost roughly US$30–900+. Their web licence terms could not be checked first-hand.

### Cited Findings
**Cormorant family (free, OFL)**
- Cormorant is "a free display type family" by Christian Thalmann (Catharsis Fonts). It has 45 font files: 9 styles (Roman, Italic, Infant, Infant Italic, Garamond, Garamond Italic, Upright Cursive, Small Caps, Unicase) × 5 weights (Light, Regular, Medium, Semibold, Bold). The libre release was funded by Google Fonts. The designer says he drew most glyphs from scratch, inspired by Claude Garamont. — [Cormorant README](https://raw.githubusercontent.com/CatharsisFonts/Cormorant/master/README.md)
- Google Fonts lists Cormorant Garamond and Cormorant as licence "OFL", designer Christian Thalmann, added 2017-01-18. — [google/fonts METADATA: cormorantgaramond](https://raw.githubusercontent.com/google/fonts/main/ofl/cormorantgaramond/METADATA.pb); [cormorant](https://raw.githubusercontent.com/google/fonts/main/ofl/cormorant/METADATA.pb)
- Measured via the Google Fonts API (2026-10-05):
  - Cormorant Garamond is served as a variable font, `font-weight: 300 700`, roman and italic. Subsets: cyrillic, cyrillic-ext, latin, latin-ext, vietnamese. The Latin slice of the 300–700 variable font is **36.8 KB**. A single static weight (500) is **22.8 KB**.
  - Cormorant (the original cut) var 300–700: 34.5 KB. Cormorant Infant var 300–700: 34.8 KB.
  - Cormorant Upright comes only as static weights 300–700, with latin, latin-ext and vietnamese subsets (no Cyrillic).
  - Cormorant SC comes as static 300–700.
  — [Google Fonts CSS2 API, Cormorant Garamond](https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300..700;1,300..700&display=swap)

**Free alternatives (all OFL on Google Fonts; Latin-slice sizes measured 2026-10-05)**
- **Gloock**: designer Duarte Pinto, OFL, added 2023-01-06, one weight (400). Latin slice 25.7 KB. — [METADATA](https://raw.githubusercontent.com/google/fonts/main/ofl/gloock/METADATA.pb); [API](https://fonts.googleapis.com/css2?family=Gloock)
- **Bodoni Moda**: opsz 6–96 plus wght 400–900 variable, Latin 45.2 KB. The owner already rejected it. — [API](https://fonts.googleapis.com/css2?family=Bodoni+Moda:opsz,wght@6..96,400..900)
- **Playfair Display**: wght 400–900 variable, Latin 37.5 KB. The owner already rejected it. — [API](https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400..900)
- **Fraunces**: opsz 9–144 plus wght 100–900 variable. Latin subset only. Not measured further; it is probably too soft for this brand (inference). — [API](https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,100..900)
- **Libre Caslon Display**: available (Latin and latin-ext). The request `Libre Caslon Text:wght@400..700` returned HTTP 400, which means it is not offered as a variable range; static styles only. — [API](https://fonts.googleapis.com/css2?family=Libre+Caslon+Display)
- **EB Garamond**: wght 400–800 variable, Latin 43.3 KB; covers Greek and Cyrillic. — [API](https://fonts.googleapis.com/css2?family=EB+Garamond:wght@400..800)

**Commercial options (prices UNVERIFIED: from search-engine summaries, foundry sites blocked; the figures may be desktop rather than web prices)**
- **Canela** (Commercial Type, Miguel Reyes, 2016): a search summary says US$800 for the collection, with individual styles from US$50, as a one-time fee. It is also rentable on Fontstand. — [Commercial Type catalog: Canela](https://commercialtype.com/catalog/canela) (blocked; figure from search summary); [Fontstand: Canela](https://fontstand.com/fonts/canela)
  - Note: "CS Canela" on Fontspring (from US$20) is a **different, unrelated font** from Craft Supply Co. Do not confuse the two. — [Fontspring CS Canela](https://fontspring.com/fonts/craft-supply-co/cs-canela)
- **GT Super** (Grilli Type): a search summary gives US$900 for the full family (20 styles) or US$600 per sub-family (10 styles), as a one-time fee. Whether that covers web use was not verified. — [Grilli Type shop: GT Super](https://www.grillitype.com/shops/gt-super); [Grilli Type information](https://www.grillitype.com/information)
- **Ogg** (Sharp Type): MyFonts listing "from $49.99" per style and $299.99 for a 10-font family. This is probably a desktop licence; web is priced separately. — [MyFonts Ogg Display](https://www.myfonts.com/collections/ogg-display-font-monotype-imaging/)
- **Saol** (Schick Toikka): the foundry's buy page exists. A third-party snippet quoted "Saol Text from $109.91". Saol Display web pricing was not verified. — [Schick Toikka: Buy Saol](https://www.schick-toikka.com/saol/buy)
- **Tiempos Headline** (Klim): Klim sells web licences per font with tiers. Klim changed its EULAs and pricing; the blog post exists but could not be read. — [Klim: Changes to EULAs and new pricing](https://klim.co.nz/blog/changes-to-eulas-new-pricing/); [Klim web font licence](https://klim.co.nz/licences/web-fonts/)
- **Editorial New** (Pangram Pangram): trial fonts are for personal use only. Paid Web licences are "from $30 per font family", sold separately from Desktop ($30) and App ($60). — [licenseorg.com guide: Pangram Pangram](https://licenseorg.com/guide/fonts/pangram-pangram) (secondary source)
- **Reckless** (Displaay): no reliable price found. A search engine returned "Reckless by Ana's Fonts" on MyFonts at US$12–16. That is a **different font** and should not be cited for Displaay's Reckless. — [MyFonts "Reckless Font" (wrong foundry)](https://www.myfonts.com/collections/reckless-font-ana-s-fonts/)
- **Romie** and **Freight Display**: no price found. See Gaps.

### Inferences
- Cormorant Garamond is the right "house" display face: it is free, self-hostable, has a variable 300–700 weight range plus italics, and the whole range costs under 40 KB. Cormorant Upright and Cormorant SC give a small-caps and upright-cursive layer (for monograms and eyebrow labels) at no cost.
- Cormorant is a *display* family. Its delicate hairlines and small x-height compared with its cap height make it weak below about 18–20 px. Headline-only use is the safe choice ("measured size" fits this). This is an inference from type-design knowledge, not measured.
- None of the commercial options adds Thai or Chinese. They would only change the Latin headline. For a one-office firm, Canela or GT Super at about US$600–900 one-time is the "premium" upgrade path. It is optional, not necessary.

### Gaps
- No commercial *web* licence price could be confirmed on a foundry page (proxy blocked). This covers Canela, GT Super, Ogg, Saol, Tiempos Headline, Editorial New, Romie, Reckless, Freight Display, Söhne and Neue Haas Grotesk. Freight is believed to be on Adobe Fonts (subscription, which includes web use), but this could not be verified here.
- Whether each foundry prices web use by pageviews (Klim and Commercial Type have historically done so) or by company size was not verified for 2025–26.

---

## Q2. Latin body and UI faces to pair with Cormorant

### Takeaway
For serif body text, the best-engineered free options are **Newsreader** (Production Type) and **Source Serif 4**. Both have optical sizes, so they keep their colour at 16–18 px. They are heavier downloads as full variable fonts (about 120–130 KB, Latin). **EB Garamond** and **Crimson Pro** are lighter (about 43–47 KB) and closer in Garamond spirit. For a small UI sans (Inter is retired), **Hanken Grotesk**, **Instrument Sans** and **Manrope** are all OFL and 24–34 KB.

### Cited Findings (all OFL on Google Fonts; Latin-subset WOFF2 measured 2026-10-05)
| Face | Axes served | Latin KB | Source |
|---|---|---|---|
| Newsreader (Production Type, OFL, added 2020-07-01) | opsz 6–72, wght 200–800 | 128.9 | [METADATA](https://raw.githubusercontent.com/google/fonts/main/ofl/newsreader/METADATA.pb); [API](https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,200..800) |
| Source Serif 4 | opsz 8–60, wght 200–900 | 119.5 | [API](https://fonts.googleapis.com/css2?family=Source+Serif+4:opsz,wght@8..60,200..900) |
| Literata | opsz 7–72, wght 200–900 | 107.5 | [API](https://fonts.googleapis.com/css2?family=Literata:opsz,wght@7..72,200..900) |
| Crimson Pro | wght 200–900 | 47.1 | [API](https://fonts.googleapis.com/css2?family=Crimson+Pro:wght@200..900) |
| EB Garamond | wght 400–800 | 43.3 | [API](https://fonts.googleapis.com/css2?family=EB+Garamond:wght@400..800) |
| Hanken Grotesk (Alfredo Marco Pradil, Hanken Design Co.; OFL; added 2022-11-16) | wght 100–900 | 33.9 | [METADATA](https://raw.githubusercontent.com/google/fonts/main/ofl/hankengrotesk/METADATA.pb); [API](https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@100..900) |
| Instrument Sans | wght 400–700 | 29.4 | [API](https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400..700) |
| Manrope | wght 200–800 | 24.3 | [API](https://fonts.googleapis.com/css2?family=Manrope:wght@200..800) |

- Söhne (Klim) and Neue Haas Grotesk / Neue Haas Unica (commercial): no price could be verified (see Q1 Gaps).

### Inferences
- **Newsreader** is the strongest serif body partner. It is a sturdy text design with optical sizing and contrasts well with Cormorant's fragile display hairlines. **Source Serif 4** is the more neutral, "institutional" choice.
- Both full variable fonts are heavy. Self-hosting a pinned opsz/wght instance range would cut the size substantially; not measured. A static instance would also do it.
- EB Garamond + Cormorant is *too* similar (two Garamonds) and lacks contrast of role. Use it only if the owner wants an all-Garamond, book-like voice.
- Instrument Sans is distinct from the retired *Instrument Serif*, but it shares the "Instrument" family name. Confirm the owner is happy with it before shortlisting; otherwise use Hanken Grotesk.

### Gaps
- No x-height or cap-height metric comparison was run between Cormorant and the body faces. This is recommended at implementation, for example with fontTools `OS/2.sxHeight`, to set `size-adjust`.

---

## Q3. Thai faces to pair with a high-contrast Latin serif

### Takeaway
The best free Thai serif partners are by **Cadson Demak** and are OFL on Google Fonts: **Trirong** (narrow, tall, high-contrast looped; formal) and **Taviraj** (wide, airy looped "farangses" style; formal). Each has 9 weights with italics, and each Thai subset is only about 16 KB per weight. **Noto Serif Thai** is a variable alternative (100–900, about 32 KB Thai). For a looped body or UI sans: **Sarabun** (the national font TH Sarabun New under OFL, about 10 KB), **IBM Plex Sans Thai Looped**, **Noto Sans Thai Looped**. All the Google Fonts Thai families measured also include Latin glyphs. Commercial Cadson Demak and DB fonts exist, but their prices could not be verified.

### Cited Findings
- **Trirong**: © 2015 Cadson Demak, OFL. "A serif Latin and looped Thai typeface… characterized by thick and thin strokes, and its narrow and tall structure echoes that of traditional Thai typefaces… works well in formal contexts." The description warns that similar glyphs (ก ถ ภ ฤ ฦ, ฎ/ฏ) can be confused in very short texts. Weights 100–900 with italics (18 styles). — [Trirong DESCRIPTION](https://raw.githubusercontent.com/google/fonts/main/ofl/trirong/DESCRIPTION.en_us.html); [METADATA](https://raw.githubusercontent.com/google/fonts/main/ofl/trirong/METADATA.pb)
- **Taviraj**: © 2015 Cadson Demak, OFL. "A serif Latin and looped Thai typeface that has a wide structure that ensures readability and legibility. It is well-suited for formal usage… thick and thin strokes… rounded and airy looped terminals." It has 9 weights with italics and is in the traditional "farangses" (French) Thai genre. — [Taviraj DESCRIPTION](https://raw.githubusercontent.com/google/fonts/main/ofl/taviraj/DESCRIPTION.en_us.html)
- **Chonburi**: Cadson Demak, OFL. A "Thai + Latin typeface for display usage, with a formal looped + serif design"; one weight. — [Chonburi DESCRIPTION](https://raw.githubusercontent.com/google/fonts/main/ofl/chonburi/DESCRIPTION.en_us.html)
- **Charm**: Cadson Demak, OFL. "A handwritten Thai and Latin family… created using a flat tip pen… works well for Thai religious texts." Weights 400 and 700. Accent use only. — [Charm DESCRIPTION](https://raw.githubusercontent.com/google/fonts/main/ofl/charm/DESCRIPTION.en_us.html)
- **Pridi**: Cadson Demak, OFL, weights 200–700 (6 static weights). — [Pridi METADATA](https://raw.githubusercontent.com/google/fonts/main/ofl/pridi/METADATA.pb)
- **Sarabun**: "is the 'TH Sarabun New' font, made available under the Open Font License". It is used in the Government Gazette of Thailand. Designer Suppakit Chalermlarp. Weights 100–800 with italics. — [Sarabun DESCRIPTION/METADATA](https://raw.githubusercontent.com/google/fonts/main/ofl/sarabun/METADATA.pb)
- **IBM Plex Sans Thai Looped**: Mike Abbink and Bold Monday, OFL, added 2021-06-18, weights 100–700. — [METADATA](https://raw.githubusercontent.com/google/fonts/main/ofl/ibmplexsansthailooped/METADATA.pb)
- **Anuphan**: Cadson Demak, OFL, added 2023-02-23, variable 100–700. — [METADATA](https://raw.githubusercontent.com/google/fonts/main/ofl/anuphan/METADATA.pb)
- **Noto Serif Thai** and **Noto Sans Thai Looped**: Google, OFL, added 2020-11-19. — [Noto Serif Thai METADATA](https://raw.githubusercontent.com/google/fonts/main/ofl/notoserifthai/METADATA.pb); [Noto Sans Thai Looped METADATA](https://raw.githubusercontent.com/google/fonts/main/ofl/notosansthailooped/METADATA.pb)
- Measured Google Fonts WOFF2 sizes, one weight unless stated (2026-10-05). Every family below serves `thai`, `latin` and `latin-ext` subsets, so all include Latin. — [Google Fonts CSS2 API](https://fonts.googleapis.com/css2?family=Trirong:wght@400)

| Family | Weights served | Thai slice KB | Latin slice KB |
|---|---|---|---|
| Trirong 400 (300 is about the same) | 100–900 static + italics | 15.9 | 20.2 |
| Taviraj 400 | 100–900 static + italics | 15.7 | 22.0 |
| Noto Serif Thai | variable 100–900 | 32.0 | 35.3 |
| Pridi 400 | 200–700 static | 14.3 | 20.5 |
| Chonburi | 400 | 10.3 | 18.3 |
| Charm 400 | 400, 700 | 16.4 | 19.5 |
| Sarabun 400 | 100–800 static + italics | 9.6 | 11.1 |
| IBM Plex Sans Thai Looped 400 | 100–700 static | 13.3 | 17.4 |
| Noto Sans Thai Looped 400 | 100–900 static | 11.0 | 10.4 |
| Noto Sans Thai (loopless) | variable 100–900 | 26.3 | 30.0 |
| Anuphan | variable 100–700 | 18.5 | 34.2 |

- **Commercial Thai**:
  - Cadson Demak "fonts appear throughout Thailand", with text and display families covering Thai and Latin. They are rentable monthly on Fontstand. A MyFonts example lists individual styles from US$29 and an 8-style family at US$199 (desktop pricing; web not verified). — [Fontstand: Cadson Demak](https://fontstand.com/news/new-releases/cadson-demak/); [MyFonts: Cadson Demak "Due"](https://myfonts.com/fonts/cadson-demak/due)
  - Some Cadson Demak families (e.g. Pracharath, Preuksa, Than) are on Adobe Fonts, which allows website use under subscription. — [Adobe Fonts: Pracharath](https://fonts.adobe.com/fonts/pracharath); [Preuksa](https://fonts.adobe.com/fonts/preuksa); [Than](https://fonts.adobe.com/fonts/than)
  - DB Fonts (DearBook, founded 1999 by Prinya Rojarayanont): no web licence prices found.

### Inferences
- **Trirong** is the closest Thai match to Cormorant's high-contrast, tall, formal feel. Use it for Thai headlines, and also for body at 18 px or more. **Taviraj** is wider and easier to read at length, so it suits Thai body text best when the brand wants serif "all the way down".
- Both are the same foundry and era, and Taviraj's Latin is a transitional serif. On a Thai page, set Latin words in Cormorant or the Latin body face rather than the Thai font's own Latin, so the Latin voice stays consistent. Do this by ordering the font stack, or with `unicode-range` on self-hosted files.
- Thai needs a larger optical size than Cormorant. Thai looped faces carry vowels and tone marks above and below, so the Thai line needs more line-height (about 1.7–1.9 for body) and usually a size bump of about 1.05–1.15× against a small-x-height Latin. This is a rule-of-thumb inference, not measured.
- Thai is cheap on the web: a full Thai page with two weights of Trirong plus one Sarabun weight is under 50 KB of Thai glyphs.

### Gaps
- No verified price was found for any commercial Cadson Demak retail serif, DB font web licence, or the remaining SIPA/DIP national fonts (the 13 "TH … PSK" fonts). Their exact licence wording for web embedding was not retrieved. Only Sarabun's OFL status is confirmed.
- No visual quality comparison (specimen review) was possible. fonts.google.com specimen pages were blocked.

---

## Q4. Simplified Chinese faces, file sizes and web loading on a static GitHub Pages site

### Takeaway
**Noto Serif SC** (Source Han Serif, © Adobe, OFL, variable 200–900) is the only mature free Song/Ming serif with a full weight range. It is the default Chinese serif. **Noto Sans SC** (variable 100–900) is the sans partner. **LXGW WenKai** is too casual and calligraphic for long text; even its author says it suits "medium-length" text better than long body text. **Zhuque Fangsong** is OFL but still pre-release.

Payload is the real cost. Through Google Fonts, a short Chinese page (121 unique characters) pulled **11 of 101 slices = about 406 KB for ONE weight**. A self-hosted subset of exactly those characters is **22 KB** (static 400) or **43 KB** (full 200–900 variable). A site-wide "common 3,755 characters" (GB2312 level-1) subset is **679 KB** static 400, or **1.37 MB** variable. For a static site whose builder knows every page's text, build-time subsetting is far cheaper than Google's slicing.

### Cited Findings
- Noto Serif SC: Google Fonts METADATA gives licence OFL and copyright "(c) 2017-2024 Adobe". It is "a modulated ('serif') design for languages in mainland China that use the Simplified Chinese variant of the Han ideograms" and "has multiple weights". — [METADATA](https://raw.githubusercontent.com/google/fonts/main/ofl/notoserifsc/METADATA.pb); [DESCRIPTION](https://raw.githubusercontent.com/google/fonts/main/ofl/notoserifsc/DESCRIPTION.en_us.html)
- Measured with fontTools on 2026-10-05, using the Google Fonts source file `NotoSerifSC[wght].ttf`: 25.1 MB TTF, 31,058 glyphs, 30,928 mapped code points, `wght` axis 200–900. — [google/fonts ofl/notoserifsc](https://raw.githubusercontent.com/google/fonts/main/ofl/notoserifsc/NotoSerifSC%5Bwght%5D.ttf)
- The Google Fonts API serves Noto Serif SC and Noto Sans SC as **101 `@font-face` blocks per style**, split by unicode-range. Requested as a range, they come back variable (`font-weight: 200 900` for Serif; `100 900` for Sans). For Noto Serif SC 400, the 101 slices total **3.18 MB**: smallest 1.5 KB, median 34 KB, largest 54 KB. — [API: Noto Serif SC 400](https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400&display=swap)
- Measured page simulation: a 121-unique-character Simplified Chinese paragraph (firm intro, service list, navigation and footer words) matched **11 slices = 406 KB** for Noto Serif SC 400 via Google Fonts. Each extra weight (e.g. a 600 heading) would add a similar amount for the characters it uses. — measured against [API: Noto Serif SC 400](https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400&display=swap)
- Google's slices were built with machine learning on which characters are used together, so a browser downloads only the slices a page needs. — [AIGA Eye on Design: Google wants to make web fonts accessible all over the world](https://eyeondesign.aiga.org/google-wants-to-make-web-fonts-accessible-all-over-the-world/)
- Self-hosted subsetting, measured with `pyftsubset` and `fontTools varLib.instancer` (WOFF2 output):
  - same 121 characters, variable 200–900: **43 KB**
  - same 121 characters, static 400: **22 KB**
  - GB2312 level-1 (3,755 hanzi + ASCII + CJK punctuation), variable: **1,372 KB**
  - GB2312 level-1, static 400: **679 KB**
  — measured from [NotoSerifSC[wght].ttf](https://raw.githubusercontent.com/google/fonts/main/ofl/notoserifsc/NotoSerifSC%5Bwght%5D.ttf)
- **cn-font-split** (KonghaYao) is Apache-2.0 licensed. It is a Rust/WASM CJK font subsetter that outputs WOFF2 chunks plus `unicode-range` CSS; runs in the browser, WASI, Linux/macOS/Windows; usable from JS (Node, Bun, Deno) and Python. It has a Vite plugin, `vite-plugin-font`. — [cn-font-split README](https://raw.githubusercontent.com/KonghaYao/cn-font-split/master/README.md); [npm vite-plugin-font](https://npmjs.com/package/vite-plugin-font); [jsDelivr cn-font-split](https://www.jsdelivr.com/package/npm/cn-font-split)
- **LXGW WenKai** (霞鹜文楷):
  - OFL 1.1, derived from Fontworks' Klee One (a Japanese textbook-style face "兼有仿宋和楷体的特点", i.e. with traits of both fangsong and kai).
  - Three weights. The author notes it "可能并不太适合大段正文排版" (may not suit long body text) and is better for medium-length texts such as poetry or notes.
  - Variants: WenKai Lite (fewer characters, for embedding) and WenKai GB (G-source glyph shapes).
  — [LXGW WenKai README](https://raw.githubusercontent.com/lxgw/LxgwWenKai/main/README.md)
  - On Google Fonts only the **TC** (Traditional) version exists ("LXGW WenKai TC": OFL, added 2024-05-16, weights 300/400/700). The requests "LXGW WenKai" and "LXGW WenKai SC" returned HTTP 400. — [METADATA lxgwwenkaitc](https://raw.githubusercontent.com/google/fonts/main/ofl/lxgwwenkaitc/METADATA.pb)
- **Zhuque Fangsong** (朱雀仿宋), TrionesType:
  - OFL 1.1, © 2025. A fangsong revival of the 1932 "南宋" metal type. The Latin glyphs currently borrow Alegreya.
  - The team asks people not to widely redistribute modified versions **before the official release**, so it is still pre-release.
  - Not on Google Fonts (API returned 400).
  — [Zhuque README](https://raw.githubusercontent.com/TrionesType/zhuque/main/README.md)
- Not on the Google Fonts API (HTTP 400): "Source Han Serif SC". It ships via Adobe or GitHub instead; Noto Serif SC is the same design. Also absent: "Noto Serif Simplified Chinese". ZCOOL XiaoWei and Ma Shan Zheng are on Google Fonts (about 92 slices each), but they are decorative display faces. — [API probe](https://fonts.googleapis.com/css2?family=ZCOOL+XiaoWei)

### Inferences
- **GitHub Pages impact**: self-hosting a full CJK font is not a storage problem. The site-wide GB2312-L1 subset is 0.7–1.4 MB per family, well within GitHub Pages limits. But making visitors download it is a performance problem. The best design for a static builder is:
  1. **Build-time per-site subsetting.** At publish, the builder collects every Chinese character used on the site and subsets Noto Serif SC (and Noto Sans SC, if used) to that set. A small firm site with a few hundred distinct hanzi would likely total about 40–150 KB per weight. This is an estimate from the 121-character = 22 KB measurement, scaled linearly; unverified.
  2. Optionally slice that subset with cn-font-split, so pages fetch only the chunks they use.
  3. **Fallback**: use Google Fonts' hosted Noto Serif SC (about 400 KB per weight per page) for articles added without a rebuild.
- Use **one** Chinese weight for body (400) and **one** for headings (500 or 600). Since Cormorant headlines are light, a Noto Serif SC 300–500 headline weight keeps the luxury "measured" feel; heavy Song weights look like newspaper headlines.
- A static instance (400) halves the size compared with the variable font. If only two weights are used, two static subsets (about 2 × 22 KB for a typical page) beat one variable subset (43 KB) only marginally. The variable font is simpler for the builder.

### Gaps
- Noto Sans SC payload was not separately measured. It is expected to be similar in scale but somewhat smaller than the serif, since a sans has simpler outlines; unverified.
- The Source Han Serif GitHub release sizes and the Adobe Fonts route could not be checked (GitHub API and adobe.com blocked).
- No real-browser measurement of render time or CLS was made.
- No free, mature alternative to Noto Serif SC for a refined Song/Ming serif was found. LXGW Neo ZhiSong (霞鹜新致宋) exists, but its licence and quality were not verified.

---

## Q5. Fallback stacks, :lang(), font-display and preloading

### Takeaway
Scope fonts per language with `:lang(th)` and `:lang(zh-Hans)` selectors, built on a `lang` attribute on `<html>` and on inline spans. Use `font-display: swap` (what Google Fonts emits with `&display=swap`). Preload only the Latin display WOFF2. Let `unicode-range` decide Thai and CJK downloads. System fallbacks below are from general knowledge and are **unverified** in this session.

### Cited Findings
- Google Fonts CSS2 accepts `display=swap` and emits per-subset `@font-face` rules with `unicode-range`. The browser downloads a file only when the page contains characters in that range. This was confirmed by the measured CSS for every family above (e.g. Trirong returns separate `thai`, `latin`, `latin-ext` and `vietnamese` blocks). — [API: Trirong](https://fonts.googleapis.com/css2?family=Trirong:wght@400&display=swap); [AIGA Eye on Design](https://eyeondesign.aiga.org/google-wants-to-make-web-fonts-accessible-all-over-the-world/)
- cn-font-split's ecosystem includes `cn-font-metrics` for reducing Cumulative Layout Shift (CLS) when fonts swap, and `cn-font-replacer` for dynamic loading. — search summary of [cn-font-split docs](https://docsearch.algolia.com/mcp/docs/repo/konghayao/cn-font-split) (secondary)

### Inferences
- Suggested CSS skeleton (illustrative; family names only):
  ```css
  :root { --display: "Cormorant Garamond", "Cormorant", Georgia, serif;
          --body: "Newsreader", "Source Serif 4", Georgia, serif; }
  :lang(th) { --display: "Cormorant Garamond", "Trirong", "Leelawadee UI", "Thonburi", serif;
              --body: "Newsreader", "Taviraj", "Sarabun", "Leelawadee UI", "Thonburi", serif;
              line-height: 1.8; }
  :lang(zh-Hans) { --display: "Cormorant Garamond", "Noto Serif SC", "Songti SC", "SimSun", serif;
                   --body: "Newsreader", "Noto Serif SC", "Songti SC", "SimSun", serif;
                   line-height: 1.8; letter-spacing: .02em; }
  ```
  Putting the Latin face first in each stack keeps English words and numerals in the brand Latin font. The Thai and Chinese faces then cover only the glyphs the Latin font lacks. For Chinese, use `"Microsoft YaHei"`/`"PingFang SC"` as fallbacks only for the *sans* stack. These system font names are standard knowledge but unverified in this session.
- `font-display: swap` for body; consider `optional` for the large CJK files on slow networks.
- `<link rel="preload" as="font" type="font/woff2" crossorigin>` only for Cormorant's Latin file (about 37 KB). Never preload CJK chunks; with unicode-range the browser picks the needed ones.
- Use `size-adjust` / `ascent-override` on the fallback `@font-face` to reduce layout shift. Thai needs a larger `ascent-override` because of stacked marks.

### Gaps
- No primary MDN or web.dev pages were fetched in this session for `:lang()`, `size-adjust`, cache partitioning (cross-site CDN cache no longer shared) or `font-display` behaviour. Treat those points as unverified.

---

## Q6. Three recommended trilingual pairings

### Takeaway
All three keep **Cormorant Garamond** (or a paid luxury upgrade in C) as the Latin voice. They differ in body treatment and contrast:
- **A "Maison"**: all serif, free.
- **B "Atelier"**: serif display + quiet sans body, free, most readable on phones.
- **C "Haute contrast"**: a stronger, optionally commercial display serif, with Trirong and heavier Song weights.

Total licence cost: A = US$0, B = US$0, C = US$0 (free variant) or about US$600–900 one-time (unverified) if a commercial Latin display is bought.

### Cited Findings (component facts as sourced above)
- All free components are OFL: Cormorant, Newsreader, Source Serif 4, Hanken Grotesk, Trirong, Taviraj, Sarabun, IBM Plex Sans Thai Looped, Noto Serif SC, Noto Sans SC. — see Q1–Q4 METADATA links, e.g. [Cormorant Garamond](https://raw.githubusercontent.com/google/fonts/main/ofl/cormorantgaramond/METADATA.pb), [Trirong](https://raw.githubusercontent.com/google/fonts/main/ofl/trirong/METADATA.pb), [Noto Serif SC](https://raw.githubusercontent.com/google/fonts/main/ofl/notoserifsc/METADATA.pb)
- Commercial C upgrade prices come from search summaries: GT Super US$600–900 ([Grilli shop](https://www.grillitype.com/shops/gt-super)); Canela about US$800 collection ([Commercial Type](https://commercialtype.com/catalog/canela)). Both are unverified and may be desktop-only.

### Inferences — the three pairings

**A — "Maison" (fine luxury, serif throughout). Licence: US$0, all OFL, self-hostable.**
| Role | Latin | Thai | Simplified Chinese |
|---|---|---|---|
| Display | Cormorant Garamond 300/500 + italic | Trirong 300/400 | Noto Serif SC 300–500 |
| Body | Newsreader (opsz) 400, 17–18 px | Taviraj 300/400 | Noto Serif SC 400 |
| Small UI / labels | Cormorant SC or Hanken Grotesk 500 at small sizes | Sarabun 500 | Noto Sans SC 500 (optional) |

- Rationale: closest to the owner's taste and the most "luxury house". Trirong's tall, contrasted forms echo Cormorant. Taviraj's wide loops keep Thai body readable. Song-style Chinese matches the serif voice.
- Indicative font payload per page (one display + one body weight): Latin about 37 + about 129 KB (Newsreader full variable; less if instanced); Thai page about 16 + 16 KB of Thai on top; Chinese page about 22–43 KB per weight if subset at build, or about 400 KB per weight via Google Fonts.

**B — "Atelier" (serif headlines, quiet sans body; most legible on mobile). Licence: US$0.**
| Role | Latin | Thai | Simplified Chinese |
|---|---|---|---|
| Display | Cormorant Garamond 400/500 + italic | Trirong 400 | Noto Serif SC 500 |
| Body | Hanken Grotesk 400 (or Instrument Sans) | IBM Plex Sans Thai Looped 400 (or Sarabun) | Noto Sans SC 400 |
| Accent | Cormorant italic for pull-quotes | Taviraj italic for quotes | Noto Serif SC 400 for quotes |

- Rationale: meets "not sans everywhere", because every headline and quote is serif, while body and UI are a calm looped sans that stays clear at 15–16 px on phones. It is the lightest Latin payload: about 37 + 34 KB.
- Thai body keeps the **looped** form (formal and trustworthy for an accounting firm) rather than a loopless "modern" Thai.

**C — "Haute contrast" (stronger, more editorial contrast). Licence: US$0 free variant; about US$600–900 one-time if a commercial display face is chosen (unverified).**
| Role | Latin | Thai | Simplified Chinese |
|---|---|---|---|
| Display | Free: Cormorant Garamond 600/700 at large sizes, or Gloock for single-word heroes. Paid: GT Super Display or Canela | Chonburi (display) or Trirong 600 | Noto Serif SC 600–700 |
| Body | Source Serif 4 (opsz) 400 | Trirong 400 at 18 px+ | Noto Serif SC 400 |
| UI | Hanken Grotesk 500 | Sarabun 500 | Noto Sans SC 500 |

- Rationale: more drama for hero sections and reports; the Thai and Chinese headline weights are heavier to hold up next to a bolder Latin. Risk: Chonburi and heavy Song weights read "poster" rather than "measured", so use them sparingly. The commercial route only upgrades the Latin headline; Thai and Chinese stay free.

**Across all three**
- Build-time subsetting for Chinese, possibly also Thai and Latin, is the single biggest performance decision. Measured: 22 KB vs 406 KB for the same Chinese paragraph.
- Keep the total family count per language page at three or fewer (display, body, optional UI) to keep requests and payload down.

### Gaps
- No visual specimen test of the pairings was possible (specimen sites blocked). The owner should review a rendered test page before locking the choice.
- Commercial prices need checking directly on the foundry sites before any purchase decision. Check also whether a one-office website licence is a flat fee or a pageview tier.
