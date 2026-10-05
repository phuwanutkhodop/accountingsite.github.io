# Thai and Simplified Chinese typography for a premium, serif-led EN/TH/ZH firm website

> **Method note (read first).** All direct page fetches failed during this session. Brand websites, W3C,
> Cadson Demak, GRANSHAN, ATypI, ThaiGraph, Typotheque and r12a were all blocked by the sandbox's
> network egress proxy (`EGRESS_BLOCKED` / HTTP 403). Because of that, **no brand site's CSS `font-family`
> could be inspected**, and every finding below comes from web-search result snippets. Where a snippet
> blended several pages and I could not tell which page a sentence came from, the line says
> "(snippet; exact page not confirmed)". Brand-level font observations for SCB, KBank, Bangkok Bank,
> Mandarin Oriental, Capella, Rosewood, Siam Paragon, ICONSIAM, Bank of Singapore, UOB, CICC, HSBC,
> Hang Seng, KWM, Fangda, Hermès, Aesop, Rolex and Cartier are therefore **unverified** and sit under
> Gaps, with a checklist for confirming them in a browser.

## 1. What Thai premium brands (banks, law/accounting firms, hospitality, retail) use

### Takeaway
Thai premium institutions use **custom corporate Thai typefaces**, often from Cadson Demak (Krungsri is one confirmed example). Thai banks' digital products have mostly moved to **loopless** Thai for their UI. Looped Thai remains the norm for traditional, official and long-form contexts. I could not confirm which Thai fonts specific private-banking, hotel or retail sites use.

### Cited Findings
- Cadson Demak is a Bangkok foundry founded in 2002 by Pongthorn Hiranpruek, Burin Hemthat and Anuthin Wongsunkakon. The name is a transcription of Thai words meaning "very well selected". — [GRANSHAN: Very Well Selected](https://granshan.com/insights/very-well-selected-cadson-demak-and-the-modern-thai-typeface)
- Cadson Demak's custom-font clients include AIS (one of Thailand's first custom digital typefaces), Thai Beverage (Chang), CAT Telecom, CPAC and Nokia. — [MyFonts Creative Characters interview](https://www.myfonts.com/pages/newsletters-cc-201103)
- Cadson Demak designed a custom Thai typeface for **Krungsri (Bank of Ayudhya)** as part of a refresh of the bank's corporate identity. The foundry has a dedicated Krungsri page. — [Cadson Demak foundry: Krungsri](https://font.cadsondemak.com/foundry/krungsri-%E0%B8%98%E0%B8%99%E0%B8%B2%E0%B8%84%E0%B8%B2%E0%B8%A3%E0%B8%81%E0%B8%A3%E0%B8%B8%E0%B8%87%E0%B8%A8%E0%B8%A3%E0%B8%B5/) (snippet only; whether that face is looped or loopless was not confirmed)
- "By 2024, every major Thai product including KBank Plus, SCB Easy, LINE MAN, Grab Thailand, and Shopee Thailand had shipped with loopless Thai as the UI default." — [ThaiGraph, "The Loopless Revolution: Modern Thai Type" (Narongsak Chaiwong, 16 Apr 2026)](https://thaigraph.com/learn/typography/loopless-revolution/)
- Cadson Demak "earned its initial reputation for trendsetting custom loopless fonts for business conglomerates" in its first decade, so many users see it as a proponent of loopless (headless) type. — [GRANSHAN: Very Well Selected](https://granshan.com/insights/very-well-selected-cadson-demak-and-the-modern-thai-typeface)
- Looped Thai "dominates traditional publishing and is prevalent in education and official contexts". Loopless is increasingly used in signage, advertising and contemporary print. — [ThaiGraph, Loopless Revolution](https://thaigraph.com/learn/typography/loopless-revolution/)
- Designer Ekaluck Peanpanawate's corporate projects include dtac, Nokia Sans Thai and CAT. — search snippet referencing [Anuthin Wongsunkakon (Wikipedia)](https://en.wikipedia.org/wiki/Anuthin_Wongsunkakon) / [National Fonts (Wikipedia)](https://en.wikipedia.org/wiki/National_Fonts) (snippet; exact page not confirmed)

### Inferences
- The split between a bank's app (loopless, built for small UI text) and its private-banking or heritage communication is plausible but unverified. Big Thai banks probably use loopless corporate faces throughout. A firm that uses **looped** Thai for display would therefore stand out from mass-market banking and read as closer to "heritage / official / private".
- Premium Thai institutions invest in a matched Thai+Latin family rather than relying on system fonts. For a small firm, the realistic equivalent is a carefully chosen open-source looped Thai serif (see section 2) that is sized and weighted to match Cormorant.

### Gaps
- **Not verified (egress blocked):** the Thai fonts used on SCB Private Banking, KBank Private Banking, Krungsri, Bangkok Bank Private, Tilleke & Gibbins, Baker McKenzie Thailand, Weerawong C&P, the Big Four Thailand sites, Mandarin Oriental Bangkok, Capella Bangkok, Rosewood Bangkok, Siam Paragon, ICONSIAM, and Thai luxury retail. To verify, open each Thai-language page in Chrome DevTools, go to Elements, then Computed, then "Rendered Fonts", on a Thai heading and on Thai body text. Record the font name, whether it is looped, the `font-size` and `line-height` of Thai versus the EN page, and any `letter-spacing`.
- Bangkok Bank, SCB and KBank corporate typeface names: searches returned no reliable source.
- No source was found on **PSL** or **DB Fonts** corporate work for banks or law firms. ThaiGraph has a PSL Kanda Modern page ([link](https://thaigraph.com/fonts/psl-kanda-modern/)), but its content could not be fetched.

## 2. Looped (มีหัว) vs loopless (ไม่มีหัว): formality, premium feel, and pairing with a Latin high-contrast serif

### Takeaway
Thai designers broadly agree on three points. Looped Thai reads as traditional, formal, trustworthy and "serious", and is associated with finance, law, publishing and luxury. Loopless reads as modern, neutral and digital. The working convention is **"the loop is to Thai what the serif is to Latin"**, so a looped Thai goes with a Latin serif. Typographers add that this is a convention, not a law. For a Cormorant-led site, a looped Thai with **thick-thin contrast** is the closest match. Cadson Demak's Trirong and Taviraj, Noto Serif Thai, and Maitree are the open-source candidates.

### Cited Findings
- History: for roughly seven centuries, from the Sukhothai inscriptions to the first digital fonts, the loop was Thai type's defining feature, "the anchoring element that tells the reader where a consonant begins". Loopless went "from avant-garde provocation to mainstream default over twenty years… propelled by the readability failure of looped Thai on early digital screens". — [ThaiGraph, Loopless Revolution (2026)](https://thaigraph.com/learn/typography/loopless-revolution/)
- Loopless Thai is generally considered the modern form. It originated with the Thai Naris typeface in 1863, and its overall height is shorter than looped. — [Proxima Nova Thai story (Mark Simonson / Cadson Demak)](https://www.marksimonson.com/proxima-super-nova/thai/story/)
- Pairing convention: "A prevailing notion in Thailand's typographic circles is that the loop is to Thai letters as the serif is to Latin characters". Designers "have come to take it for granted that looped fonts are to be employed with Latin serif fonts, while loop-less is complementary to Latin sans serif". However, "many Thai fonts with loops can be set side by side with Latin sans serif type without creating visual discord". Thai–Latin pairing is described as flexible overall. — [ATypI presentation "Thai Type Pairing"](https://atypi.org/presentation/thai-type-pairing/) (snippet; speaker and year not confirmed)
- Thai-language design press reports the following associations: looped fonts "สร้างความไว้วางใจและสื่อถึงคุณภาพ" (build trust and signal quality) and suit finance, law, publishing and luxury brands. Loopless feels approachable and suits tech, startups, fashion and digital media. For long-form text, looped "ช่วยพาสายตาไหล" (keeps the eye flowing) and feels more serious. For small on-screen text, loopless is often the starting point. — [GIANT PRINT: ฟอนต์มีผล](https://giantprint.co.th/font-selection-branding-sme/); [Lemon8: ฟอนต์มีหัว vs ไม่มีหัว](https://www.lemon8-app.com/@matha_math/7422189241486066192?region=us) (snippet blended these sources; they are popular-design sources, not typographer authorities)
- Loopless can also look formal if the weight is chosen well. — [Lemon8: ฟอนต์มีหัว vs ไม่มีหัว](https://www.lemon8-app.com/@matha_math/7422189241486066192?region=us) (snippet)
- Cadson Demak's **Thong Lor** ("molten gold") is a modern looped sans. It was started in 2010 by Ekaluck Phianphanawate for a client that wanted loops with a minimalist, modern look. The client switched to loopless partway through, and the project was revived later. It has a bigger-than-usual loop and a wider-than-typical width "to encourage slower reading". The team's stated concern was that while loopless was trending, it "risked crowding out the looped forms that are so central to Thai identity". — [GRANSHAN: Thong Lor and the Return of the Loop](https://granshan.com/insights/thong-lor-and-the-return-of-the-loop-cadson-demaks-typographic-bridge-to-thai-identity); [Cadson Demak: Thong Lor, Part 2](https://cadsondemak.com/medias/read/thong-lor-the-way-back-into-loop-part-2); [Fontstand: Thonglor](https://fontstand.com/fonts/thonglor)
- "Cadson Demak's fonts usually have similar structures to Latin letterforms". — [GRANSHAN: Very Well Selected](https://granshan.com/insights/very-well-selected-cadson-demak-and-the-modern-thai-typeface) (snippet)
- **Trirong** (Cadson Demak, Google Fonts) is a serif Latin + looped Thai face "characterized by thick and thin strokes", in 9 weights. The name means "tricolor flag". — [Google Fonts: Trirong](https://fonts.google.com/specimen/Trirong); [ThaiGraph: Trirong](https://thaigraph.com/fonts/trirong/); [Fonts In Use: Trirong](https://fontsinuse.com/typefaces/92160/trirong)
- **Maitree** (Cadson Demak) is a serif Latin + looped Thai face with wide proportions and a "bigger-than-usual looped terminal in Thai, and long serifs in Latin, that balance out the whole structure". — [GitHub: cadsondemak/maitree](https://github.com/cadsondemak/maitree); [RightFont: Maitree](https://rightfontapp.com/family/maitree)
- **Noto Serif Thai** is the looped serif companion to Noto Sans Thai. It is a variable-weight font under the SIL OFL. — search snippet ([Google Thai Fonts, Medium](https://poonlapv.medium.com/google-thai-fonts-f7274bea0a50)) (snippet; exact page not confirmed)
- Cadson Demak's Google Fonts families: Athiti, Chonburi, Itim, Kanit, Maitree, Mitr, Pattaya, Pridi, Prompt, Sriracha, **Taviraj**, Trirong. — [Google Thai Fonts (Medium)](https://poonlapv.medium.com/google-thai-fonts-f7274bea0a50) (snippet)
- Cadson Demak also designed Proxima Nova Thai in both looped and loopless versions. — [Proxima Nova Thai story](https://www.marksimonson.com/proxima-super-nova/thai/story/)
- An "Evolution of Thai Loopless" talk was given at BITS10 (Bangkok International Typographic Symposium). — [BITS10 program](http://bitscon.asia/program/type-talk-the-evolution-of-thai-loopless)
- Typotheque has an essay on new Thai type, "Bridging Tradition and Modernity". — [Typotheque blog](https://www.typotheque.com/blog/new-thai-type) (content not fetched)

### Inferences
- For a Cormorant Garamond-character Latin, the closest open-source Thai partners are looped serifs with stroke contrast: **Trirong** (explicitly thick-thin) and **Taviraj** (same foundry and family logic; its high-contrast character is not confirmed in this session's sources). **Noto Serif Thai** is a quieter, highly legible alternative. **Maitree** is wider and lower-key, which suits body text more than display. Thong Lor (commercial, looped sans) is an option if the firm wants a "modern heritage" Thai that pairs with a sans secondary face.
- A sensible split: **looped Thai for headings and long-form body** (premium, formal, consistent with "loop = serif"). Use loopless Thai only for small UI chrome (buttons, nav, form labels), mirroring how a Latin serif site might use a small sans for UI.
- Cormorant's extreme contrast and small x-height mean the Thai face should be chosen and tested **at the same weight step on screen**. A light Cormorant headline next to a regular-weight Thai will look mismatched. Treat this as a hypothesis to test on real pages.

### Gaps
- I could not find a direct published statement by Anuthin Wongsunkakon, DB Fonts or PSL specifically about pairing looped Thai with a *high-contrast display* Latin serif, such as Didone or Garamond display cuts. The ATypI and GRANSHAN pages that likely discuss this were blocked.
- No Type Thursday Bangkok material was retrieved.

## 3. Chinese premium finance/professional brands: Song/Ming (宋体/明体) vs Hei (黑体), and mixing with Latin serifs

### Takeaway
Chinese typographic practice mirrors the Latin rule: **Song/Ming (宋体) goes with Latin serifs, Hei (黑体) with sans**. Song carries the "elevated, literary, premium" feel, especially at display sizes, and Hei is the default for on-screen UI and body. The open Song for the web is **Noto Serif SC / Source Han Serif (思源宋体)**, with weights 200–900. Common practice is to declare the Latin font first in the CSS stack so Latin glyphs come from the Latin serif. I could not confirm which fonts HK, Singapore or Shanghai private banks and Chinese law firms use.

### Cited Findings
- Basic CJK classes used for titles, body and annotations: 明體 (serif/Ming/Song), 黑體 (sans/Hei), 圓體 (rounded), 楷體 (Kai), 仿宋體 (imitation Song). justfont offers web-embedded Hei, Ming and Fangsong. — [justfont pocketbook: basic types](https://learn.justfont.com/pocketbook/applications/basic-applications/basic-types)
- Mixing rule: "尽可能地用衬线体配衬线体，无衬线体配无衬线体" (serif with serif, sans with sans as far as possible). 宋体 "常与衬线体相搭配使用，因为两种字体无论在笔画特征，还是气质上都很相似" (Song pairs with Latin serifs because their strokes and temperament are similar). Use a real Latin font rather than the Latin glyphs bundled in the Chinese font. — [Canva.cn: 中英文字体排版](https://www.canva.cn/learn/chinese-english-fonts-typesetting-question/); see also [数英: 重新认识宋体字排版](https://www.digitaling.com/articles/987965.html) (snippet blended these sources)
- Sizing: "通常英文需比中文略大（约10%-15%），才能达到视觉粗细和高度上的平衡". In other words, Latin set about 10–15% larger than the Chinese to balance weight and height. Also watch the Latin baseline and cap height when mixing. — search-result snippet from the same result set ([Canva.cn](https://www.canva.cn/learn/chinese-english-fonts-typesetting-question/) / [symprint](https://www.symprint.com/show/news-8751.html)) (snippet; exact page not confirmed)
- Noto Serif SC = Source Han Serif (思源宋体). Noto Sans SC = Source Han Sans (思源黑体). — [Google Fonts 已支持思源宋体](https://io-oi.me/tech/noto-serif-sc-added-on-google-fonts/); [Source Han Serif (Wikipedia)](https://en.wikipedia.org/wiki/Source_Han_Serif)
- Noto Serif SC has 7 weights: 200, 300, 400, 500, 600, 700 and 900. — [io-oi.me](https://io-oi.me/tech/noto-serif-sc-added-on-google-fonts/) (snippet)
- Web practice: in `font-family`, put the English font before the Chinese font. Source Han Serif at heavy weight (900) can be used for titles. Sites mix Source Han Sans and Serif between title and body. — [Fei Ye: 在网页中使用思源宋体](https://blog.yfei.page/cn/2020/12/siyuansongti/); [简书: 博客网站字体设置](https://www.jianshu.com/p/aa7faa583136); [少数派: 思源宋体如何正确使用](https://sspai.com/post/38705) (snippet)
- Monotype Hong Kong designs Simplified and Traditional Chinese typefaces and "continues to create custom and bespoke typefaces for global brands and enterprises". — [MyFonts: Monotype HK foundry](https://www.myfonts.com/collections/monotype-hk-foundry)
- Shang Xia was founded in 2010 as a Hermès–Jiang Qiong Er collaboration, and Hermès later sold it. — [Wikipedia: Shang Xia](https://en.wikipedia.org/wiki/Shang_Xia); [CPP-Luxury](https://cpp-luxury.com/hermes-sells-shang-xia-a-brand-created-for-the-chinese-market/). (No typographic information found.)

### Inferences
- For the ZH pages, the direct analogue of Cormorant headlines is a **Song display at light/regular weight** (Noto Serif SC 300–400), with Cormorant supplying the Latin glyphs, numerals and the firm name. Song's horizontal-thin / vertical-thick contrast and triangular stroke ends (字脚) echo a high-contrast Latin serif.
- Body ZH: a Song body (Noto Serif SC 400) at ≥16–17px reads as "editorial/premium" on high-DPI screens. A Hei body (Noto Sans SC / PingFang SC) is the safer screen-legibility choice. A premium serif-led site can justify Song body on long-form pages and Hei for UI.
- Simplified Chinese is the requirement, but the HK/Singapore context means some readers will expect Traditional forms. If a TC page is ever added, use Noto Serif TC/HK and do not reuse SC files.

### Gaps
- **Not verified (egress blocked):** the actual web fonts of Bank of Singapore, UOB Private, CICC, HSBC Private Bank China, Hang Seng, King & Wood Mallesons, Fangda and Shang Xia. To verify, use DevTools "Rendered Fonts" on a Chinese H1 and body paragraph. Expectation (unverified, from general knowledge): most of these rely on system fonts such as PingFang SC or Microsoft YaHei (Hei) for body, with Song appearing mainly in imagery or campaign headlines.
- HSBC's Chinese corporate typeface could not be confirmed. A search surfaced "Seol for HSBC", but that is a **Korean** custom face ([MyFonts](https://www.myfonts.com/collections/seol-for-hsbc-font-custom)), not Chinese.
- No Type is Beautiful (字绘本) article was retrieved.
- The page weight of a full CJK webfont, and Google Fonts' subsetting by `unicode-range`, were not checked in this session. This matters for performance on a static GitHub Pages site and should be verified.

## 4. Practical rules: line-height, letter-spacing, sizes, punctuation, faux bold/italic, mixed-script lines

### Takeaway
Thai needs **more line-height than Latin**, about 1.55+ for body, because of stacked vowels and tone marks. Chinese body text wants roughly 1.5–2.0, with about 1.7 a common target. In mixed Chinese/Latin lines, leave **≥1/8 em** between Chinese and Latin runs. Chinese punctuation is full-width, and certain marks must not break across lines. Disable synthetic bold/italic for Thai and CJK with `font-synthesis: none` and load real weights. Never italicise Thai or Chinese.

### Cited Findings
- **Thai line-height:** Thai body text needs a line-height of at least 1.55, about 10–15% more than Latin, to fit stacked vowels and tone marks. Use 1.1–1.25 at display sizes. — search snippet from a result set including [ThaiGraph FAQ](https://thaigraph.com/faq/) and [r12a Thai orthography notes](https://r12a.github.io/scripts/thai/th.html) (snippet; exact page not confirmed)
- Thai stacks marks vertically: a syllable can carry a vowel above the consonant and a tone mark above that (two levels), plus marks below. "Thai tends to add more interline spacing than Latin text does". Test with text containing stacked above-vowels and tone marks. — [r12a: Thai orthography notes](https://r12a.github.io/scripts/thai/th.html) (snippet)
- Thai shaping and mark positioning rely on OpenType features in the font. — [Thai Script Shaping (Theppitak Karoonboonyanan)](https://linux.thai.net/~thep/th-otf/shaping.html); [NECTEC: Standardization and Implementations of Thai Language](https://www.nectec.or.th/it-standards/thaistd.pdf)
- Thong Lor's wider-than-typical Thai width was chosen "to encourage slower reading and reduce the chance of rereading, especially since Thai script does not have spaces between words". — [GRANSHAN: Thong Lor](https://granshan.com/insights/thong-lor-and-the-return-of-the-loop-cadson-demaks-typographic-bridge-to-thai-identity)
- **Chinese/Latin spacing:** "The spacing between Chinese and Western text within a line should be at least one-eighth of the width of a Chinese character". When there are many mixed runs, reduce spacing equally, with 1/8 em as the minimum. — [W3C clreq: Requirements for Chinese Text Layout](https://www.w3.org/TR/clreq/) (snippet)
- **Chinese line gap:** "commonly set to a value between 50% and 100% of the height of the character frame", which corresponds to a CSS `line-height` of about 1.5–2.0. — [W3C clreq](https://www.w3.org/TR/clreq/) (snippet). A leading of about 1.7 is recommended for CJK's dense information. — [Asian Absolute: CJK Typesetting in 2025](https://asianabsolute.co.uk/blog/cjk-typesetting-challenges-workflows-and-best-practices/) (snippet; exact page not confirmed)
- **Chinese punctuation:** set in a full em box, treated as a half-width glyph plus a half-width adjustable space. Certain marks, such as the dash and the ellipsis, take 2 em as one unit and must not break across lines. — [W3C clreq](https://www.w3.org/TR/clreq/); [postext issue #185 on punctuation widths and hanging](https://github.com/drnachio/postext/issues/185) (snippet)
- Chinese-context rule: use Chinese full-width punctuation in Chinese text (one character width) and Western punctuation in English (half width). — [CSDN: 中西文混合排版指南](https://blog.csdn.net/MrBaymax/article/details/78774177) (snippet)
- **Faux styles:** "Faux bolding and style can be completely unreadable or might even change the meaning" for logographic scripts. `font-synthesis: none` stops the browser synthesising bold or oblique, and the property has had broad support since about 2022 (~95% usage). — [CSS-Tricks: font-synthesis](https://css-tricks.com/?p=318556); [modern-css.com: font-synthesis](https://modern-css.com/reference/properties/font-synthesis/); [SuttaCentral: avoid faux fonts](https://discourse.suttacentral.net/t/avoid-faux-fonts/336)
- Chinese weight vocabulary: the "W" system (W3, W5…) gives stroke weight, where a lower number is lighter. — [Canva.cn](https://www.canva.cn/learn/chinese-english-fonts-typesetting-question/) (snippet)

### Inferences
These are recommendations derived from the findings above, not sourced facts.
- Use per-language CSS with `:lang(th)` and `:lang(zh-Hans)` selectors on `<html lang>`, so each script gets its own `font-family`, `line-height` and `letter-spacing`. Do not use one global stack.
  - **EN:** Cormorant display about 1.05–1.15; body about 1.5–1.6 (owned by the Latin research thread).
  - **TH:** headings about 1.25–1.35, which is higher than the snippet's 1.1–1.25 because looped faces and stacked marks clip easily at tight leading. Body about 1.7–1.8. Never set Thai `line-height` below the font's ascender+descender, or tone marks will collide with the line above.
  - **ZH:** headings about 1.3–1.4; body about 1.7–1.8.
- **Size calibration:** Cormorant has a small x-height, so at an equal `font-size` Thai and Chinese will look larger and darker. Calibrate by eye on real strings. Typically Thai body is the same as or about 5–10% above the Latin body size (Thai glyphs are small inside the em). Chinese body is often equal to or slightly below the Latin size. Display Chinese often needs a *smaller* `font-size` than Cormorant to match its visual weight. The 10–15% "Latin larger than Chinese" rule from Chinese design press points the same way. Use `font-size-adjust` cautiously and test.
- **Letter-spacing:** do not add tracking to Thai body text, because Thai has no word spaces and tracking weakens word shapes. Keep any Chinese display tracking very small and test it. Do not carry over the wide all-caps tracking used on Latin labels.
- **Emphasis:** no italics in TH or ZH. For ZH, use weight (a real loaded weight), colour (oxblood) or `text-emphasis` dots. For TH, use weight or colour. Set `font-synthesis: none` on `:lang(th)` and `:lang(zh)`, and load the actual weights used.
- **Mixed-script lines** such as "บริษัท ABC Accounting" or "税务 VAT 申报":
  - Let the Latin font come first in the stack so Latin words render in Cormorant, with the TH/ZH font next.
  - Add 1/8–1/4 em space around Latin runs in Chinese.
  - Keep numerals in the Latin face for tables, because consistent figures look premium. Check that Cormorant's old-style figures suit financial tables; tabular lining figures may be needed.
- **Thai line breaking:** browsers break Thai using dictionaries. Avoid `text-align: justify` on Thai, because it stretches unpredictably without spaces, and test `word-break` behaviour. Thai uses spaces as phrase or sentence separators, not between words.

### Gaps
- No W3C Thai Layout Requirements (thai-lreq) text could be retrieved, because w3.org was blocked. The precise W3C guidance on Thai justification, emphasis and line breaking is therefore not cited.
- No authoritative published numeric rule for the Thai-vs-Latin size ratio was found. The ratio has to be tuned per font pair.

## 5. How global luxury houses (Hermès, Aesop, Rolex, Cartier) handle Thai and Chinese sites

### Takeaway
Luxury houses commission bespoke Latin typefaces, but I found no published evidence of bespoke Thai or Chinese companions for Hermès, Aesop, Rolex or Cartier. Monotype HK does build bespoke Chinese faces for global brands. The live TH/ZH sites could not be inspected, so the actual treatment is unverified.

### Cited Findings
- Houses like Chanel, Hermès and Tiffany commission bespoke typefaces. Cartier uses a custom script, and Louis Vuitton's monogram is described as Georgia-derived, with Futura for the wordmark. — [Fontfabric: Fonts for Luxury Branding](https://www.fontfabric.com/blog/fonts-for-luxury-branding/) (snippet; the LV/Georgia claim comes from a secondary design blog and should be treated cautiously)
- Monotype publishes analyses of luxury-brand typography (fashion, beauty), but not of their CJK or Thai variants. — [Monotype: Fonts and luxury brands, fashion](https://www.monotype.com/resources/expertise/fonts-and-luxury-brands-fashion); [Monotype: Luxury and typography](https://www.monotype.com/resources/luxury-and-typography-elegance-crafted-letters)
- Monotype HK creates custom SC/TC typefaces for global brands. — [MyFonts: Monotype HK](https://www.myfonts.com/collections/monotype-hk-foundry)

### Inferences
- Many global luxury sites keep the Latin brand face for logos, numerals and Latin words, and let TH/ZH text fall to a well-chosen system or Noto font. The premium feel then comes from **restraint**: generous whitespace, small measured headings, colour, and photography. This is unverified and should be confirmed in DevTools. For this firm, that means a properly paired looped Thai serif and a Song Chinese face, with matched weights and generous leading, should already exceed the norm.

### Gaps
- **Unverified; please inspect directly.** Check the Hermès (hermes.cn, hermes.com/th), Aesop (aesop.com/th, aesop.com.cn), Rolex (rolex.cn, rolex.com/th) and Cartier (cartier.cn, cartier.com/th-th) TH/ZH pages for:
  1. the rendered font on the H1 and body;
  2. Song vs Hei, and looped vs loopless;
  3. `line-height` and `letter-spacing` compared with the EN page;
  4. whether Latin brand words stay in the brand face.

  All of these domains were blocked in this session.
