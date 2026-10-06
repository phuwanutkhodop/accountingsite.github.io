# 34 — Visual identity benchmark

**Ticket:** GitHub issue #34 (Wayfinder research: visual identity benchmark) · **Date:** 5 October 2026 · **Status:** research only. No theme files changed.
**Judged against:** the locked brand brief in `docs/decisions/33-brand-feeling.md` §5. Its one rule: *bold in colour and voice, minimal in type, layout and numbers.* Palette: O1 Oxblood by day (`#7a2229` on `#f2eeea`) and O9 Night Library by night (`#1b1112`), with brass `#7d5f28` / `#c4a06a` for figures and the seal.
**Inputs:** four research notes in `research_notes/Visual identity benchmark/`:
- `premium_brand_patterns.md`
- `thai_chinese_premium_typography.md`
- `trilingual_font_candidates.md`
- `premium_photography.md`

It also uses the locked brief (#33) and the earlier typography report `docs/research/05-thai-chinese-typography.md`. Section 8 lists where this report replaces #05.
**Evidence warning:** the network proxy blocked direct visits to almost every brand, foundry and design-press site. Most brand observations therefore come from **search-result summaries**, not from inspecting the sites. Font sizes and licences are the exception: they were **measured first-hand** from the Google Fonts API and the `google/fonts` repository. Section 9 lists what #35 must check in a real browser.
> **Note, 6 October 2026:** for the builder, decision #15 (`docs/decisions/15-type-system.md`) replaces cn-font-split with HarfBuzz's subsetter, measures the figures check (§9 #11) and settles loading.

---

## 1. สรุปสำหรับเจ้าของกิจการ (ภาษาไทย)

1. แบรนด์ระดับสูง เช่น ธนาคารส่วนบุคคลของสวิส สำนักงานกฎหมายชั้นนำ และ Hermès, Aesop, Cartier ไม่ได้ดูแพงเพราะใส่ของเยอะ แต่เพราะ**ยับยั้ง** คือใช้สีประจำแบรนด์สีเดียวอย่างมีที่ทาง ใช้มุมเหลี่ยม พื้นสีกระดาษอุ่น และตัวอักษรแค่สองแบบ (หัวเรื่องแบบมีเชิง และตัวอักษรเรียบ ๆ สำหรับข้อความทั่วไป)
2. **สีแดงเลือดนกของเราหายากในวงการการเงิน** ซึ่งเกือบทุกแห่งใช้สีกรมท่า ตัวอย่างที่ใกล้ที่สุดคือธนาคาร Pictet (แดงอิฐ) และกล่องหนังแดงขลิบทองของ Cartier สีแดงจะดูหรูเมื่อเป็นแดงเข้ม ผูกกับสัญลักษณ์ชิ้นเดียว และจับคู่กับสีทอง ไม่ใช่ทาทั้งหน้า
3. **กับดักที่ต้องหลีก:** ตัวหนังสือสีทองบนภาพมืด ๆ ตอนนี้กลายเป็นเทมเพลตสำเร็จรูปที่ขายกันทั่วไปแล้ว ในโหมดกลางคืนจึงต้องใช้สีทองเหลืองกับตัวเลขและตราประทับเท่านั้น ห้ามใช้กับหัวเรื่อง
4. **ภาษาไทย:** ตัวอักษรแบบมีหัวเทียบได้กับตัวอักษรอังกฤษแบบมีเชิง ให้ความรู้สึกทางการและน่าเชื่อถือ ส่วนแอปธนาคารใหญ่ ๆ เปลี่ยนไปใช้ตัวไม่มีหัวกันหมดแล้ว การใช้ตัวมีหัวจึงทำให้เราดูต่างจากธนาคารทั่วไป และดูเป็นบริการเฉพาะบุคคลมากกว่า
5. **ภาษาจีน:** ใช้ตัวแบบซ่ง (宋体) ซึ่งเป็น "ตัวมีเชิง" ของจีน ส่วนคำภาษาอังกฤษและตัวเลขที่อยู่ในข้อความจีน ให้แสดงด้วยฟอนต์อังกฤษของเราเพื่อให้ทั้งเว็บดูเป็นชุดเดียวกัน
6. **ฟอนต์ที่แนะนำทุกตัวฟรีและใช้เชิงพาณิชย์ได้** ได้แก่ Cormorant Garamond (อังกฤษ), Trirong และ Taviraj (ไทย), Noto Serif SC (จีน) ถ้าอยากได้ฟอนต์หัวเรื่องอังกฤษแบบเสียเงิน ราคาประมาณ 600–900 ดอลลาร์สหรัฐ จ่ายครั้งเดียว แต่ยังไม่ได้ยืนยันราคาจริง
7. **ฟอนต์จีนหนักมาก:** ถ้าโหลดจาก Google หนึ่งหน้าต้องโหลดราว 400 KB ต่อความหนาหนึ่งระดับ แต่ถ้าตัวสร้างเว็บตัดเอาเฉพาะตัวอักษรที่ใช้จริง จะเหลือราว 22 KB ซึ่งเร็วกว่ามาก ควรทำแบบหลัง
8. **ภาพถ่ายที่ดูแพง** คือภาพวัสดุจริง (กระดาษ หนัง ทองเหลือง ไม้สัก) แสงจากหน้าต่าง มือที่กำลังทำงาน และภาพจริงของหุ้นส่วน **ห้ามใช้**ภาพจับมือ ตึกระฟ้า หรือกราฟลูกศรชี้ขึ้น วิธีทดสอบง่าย ๆ คือถามว่า "คู่แข่งเอาภาพนี้ไปใช้ได้ทันทีไหม" ถ้าได้ แปลว่าภาพนั้นธรรมดาเกินไป
9. **แนะนำ 3 แนวทางให้เลือกใน #35:** A "Maison" เรียบที่สุด ใช้ตัวมีเชิงทั้งหน้า · B "Atelier" หัวเรื่องมีเชิง เนื้อหาเป็นตัวเรียบอ่านง่ายบนมือถือ และสลับแถบสีชัดที่สุด · C "Haute Contrast" คอนทราสต์สูง โทนห้องสมุดยามค่ำ
10. **ข้อจำกัดและสิ่งที่ต้องตัดสินใจ:** ระบบบล็อกการเข้าเว็บแบรนด์ส่วนใหญ่ ข้อมูลหลายส่วนจึงมาจากผลค้นหา และต้องเปิดตรวจในเบราว์เซอร์จริงระหว่างทำ #35 เรื่องที่เจ้าของต้องตัดสินใจคือ งบจ้างช่างภาพ งบซื้อฟอนต์ การให้หุ้นส่วนปรากฏหน้าในเว็บ ข้อมูลประวัติจริงของสำนักงาน อักษรบนตราประทับ และวิดีโอหน้าแรก (ดูข้อ 12)

---

## 2. Bottom line

The firms and houses this brief aims at look premium by **holding back**, not by adding ornament. Five habits recur:
- one owned signature colour, anchored to one emblem;
- square geometry;
- a warm paper ground instead of white;
- a two-voice type system (an expressive serif for headlines and a quiet face for working text);
- real material or people in the photographs.

Oxblood is a genuinely open position in a category of navy and navy-with-gold. Two cases show a deep red reading as old money rather than loud: Pictet's claret-brick lion, and Cartier's red leather box with its gold garland. In both, the red is **dark, anchored to one object and paired with metal**. That is exactly the brief's oxblood-plus-brass system.

For Thai and Chinese, the established convention is "the loop is the Thai serif" and "Song is the Chinese serif". So a looped Thai serif (Trirong or Taviraj) and a Song Chinese face (Noto Serif SC) beside Cormorant Garamond is both correct and distinctive. Thai mass-market banking moved to loopless type by 2024, so looped Thai sets the firm apart from it.

Every recommended font is free (OFL). The one serious cost is Chinese font weight. A measured Chinese paragraph pulled about **406 KB from Google Fonts but only 22 KB when subset at build time**, so the builder should subset fonts when it publishes.

Photography should follow the luxury-house recipe: material still life, natural light, hands at work, documentary partner portraits. Every image gets one house grade. The two traps to design against are the navy-sans-skyline default and the newer "gold serif on a black hero" template, which matters most in night mode.

Section 11 turns this into three directions for #35: **A Maison** (all serif, paper-led, the quietest), **B Atelier** (serif headlines with a looped-sans body, the strongest band rhythm, the most legible on phones) and **C Haute Contrast** (night-library mood, duotone imagery, heavier display weights, an optional paid Latin face). The evidence is thinnest exactly where #35 needs precision: measured type sizes, how Pictet actually deploys its red, and which fonts Thai and Chinese premium sites render. Those are browser checks, listed in section 9.

---

## 3. The top tier looks expensive by owning less

### Restraint and ownership beat ornament across banks, law firms and luxury houses

Ten benchmarks were reviewed. The best-documented ones share a recognisable grammar. **Pictet** commissioned its own type family, Lardy, in both Serif and Sans cuts. It added Lardy to the logo in 2021, as part of a rebrand meant to "create one voice for all business units", and kept the lion emblem it has used since 1955 ([Pictet logo page](https://www.pictet.com/us/en/about/the-pictet-logo); [Maxibestof: Lardy Serif](https://maxibestof.one/typefaces/lardy-serif); [M.Rodzik: Pictet](https://www.mrodzik.com/pictet)). **Cartier** pairs a proprietary editorial serif, Fancy Cut, with a geometric sans, Brilliant Cut, on near-black ink and white surfaces. **Every corner radius is 0px** ([shadcn.io: Cartier](https://www.shadcn.io/design/cartier)). **Aesop** runs on two colours, a cream canvas `#fffef2` and graphite `#333333`. It uses "zero rounded corners" and twelve sans styles with "one Zapf-Humanist serif moment" ([shadcn.io: Aesop](https://www.shadcn.io/design/aesop)). Its Work & Co redesign draws layouts from the product packaging and uses "calm transitions that mirror a relaxing in-store experience" ([Work & Co: Aesop](https://work.co/clients/aesop/)).

**Hermès** goes further still: its signature orange "does not appear in the UI token set". The interface is a white stage with achromatic type, and the colour comes from the photographed objects ([shadcn.io: Hermès](https://www.shadcn.io/design/hermes)).

Three caveats apply to these sources:
- The shadcn.io pages are third-party token extractions, so their font names may be web fallbacks rather than the brands' own typefaces.
- The Brandfetch colour values cited in this report are extracted automatically, not taken from brand guidelines.
- Neither was confirmed by visiting the sites.

**Heritage as content** is the second recurring move. Pictet publishes its lion's four incarnations ([Pictet](https://www.pictet.com/us/en/about/the-pictet-logo)). C. Hoare & Co, the UK's oldest privately owned bank (founded 1672), has its own history page ([Hoare's: Our history](https://www.hoaresbank.co.uk/our-history)). Coutts' 2020 FutureBrand rebrand drew on three heritage sources: handwritten type based on the founders' letters, family-portrait photography, and "bold graphic framing devices reminiscent of old family photo albums" ([FutureBrand](https://www.futurebrand.com/news/a-new-era-for-private-banking-futurebrand-refresh-coutts-brand-positioning-and-visual-identity)). FutureBrand reports that the rebrand made people see Coutts as more "caring", "modern" and "innovative" ([FutureBrand: Coutts](https://www.futurebrand.com/our-work/coutts)). The album-frame device is a close relative of the brief's **double-rule frame**.

**Berenberg's** 2025 rebrand kept its founding-history orange and modernised its coat of arms "for digital and international applications". This is a precedent for a historic emblem, like our monogram seal, working in a digital identity ([Berenberg](https://www.berenberg.de/en/news/pressemeldung/berenberg-new-brand-identity/)).

The documented motion language is equally quiet. Only Aesop's "calm transitions" are described, which supports the brief's short rise or fade with no parallax. **No evidence was found that any of these brands offers a user-selectable dark mode.** Patek Philippe achieves a dark mood through "full-bleed dark photography" on a palette of charcoal, white, taupe and black, with "no additional chromatic accent" ([shadcn.io: Patek Philippe](https://www.shadcn.io/design/patek-philippe)). The brief's switchable Night Library is therefore a differentiator with no direct precedent to copy.

### Deep red reads as old money when it is dark, anchored and paired with metal

Very few brands in this tier own a red. Lombard Odier's extracted palette is blue plus near-black, with no burgundy ([Brandfetch: Lombard Odier](https://brandfetch.com/lombardodier.com)). Julius Baer is royal blue ([FutureBrand](https://www.futurebrand.com/our-work/juliusbaer)). Rothschild & Co is dark blue `#162A4B` with gold `#CC9F53` ([Brandfetch](https://brandfetch.com/rothschildandco.com)). Searches for claret signatures at Arbuthnot Latham, Weatherbys and C. Hoare found nothing.

Three red-family precedents stand out:
- **Pictet.** Its primary colour is a muted claret-brick, `#A04044` (auto-extracted), tied to the lion and wordmark ([Brandfetch: Pictet](https://brandfetch.com/pictet.com)).
- **Cartier.** The box has been official packaging since the 1930s, in "deep red leather, gold garland decoration". The red-and-gold pairing became so distinctive it "often eclipsed the Cartier logo in recognition" ([Lyon & Turnbull](https://www.lyonandturnbull.com/stories/the-cartier-red-box)). On the website, a much brighter red, `#d50032`, appears only as one accent token ([shadcn.io: Cartier](https://www.shadcn.io/design/cartier)). Treat these as two different reds.
- **Loro Piana.** It sets a terracotta "kummel red" inside a neutral palette of fibre colours that also includes burgundy ([Selvane](https://www.selvane.co/blogs/knowledge/the-color-intelligence-of-loro-piana)).

The lesson for oxblood is consistent. In all three, red stays quiet because:
- it sits on a neutral field;
- it attaches to one heraldic object (a lion, a box);
- it is dark and desaturated;
- it is paired with gold as a *detail* colour.

At `#7a2229`, our oxblood is darker than Pictet's red and close to the Cartier box tone (an unofficial hex of `#801B2B`, per [color-name.com](https://www.color-name.com/cartier-red.color)), so it sits firmly in the quiet register.

The brief asks for more red than these precedents use: an oxblood header bar on every page and alternating bands. **No bank or law firm with a full-width red header bar was found.** That makes the bar the brief's boldest move and its least-precedented one. It stays "luxury" only if everything else holds back. The seal and wordmark go inside the bar, rather than more red on the paper, and the reading surfaces stay paper.

### Brass rules computed for #35

Contrast ratios computed with the WCAG formula on the locked tokens refine the brief's rule that oxblood carries bands and brass carries figures. On the day oxblood bar (`#7a2229`), the light brass `#c4a06a` reaches **4.1:1**. That is enough for the seal and other graphic marks, and for large text, but not for small figures. The dark brass `#7d5f28` reaches only **1.7:1** there, so it must never sit on oxblood. On the deep bands, light brass reaches **6.7:1** by day (`#3a1316`) and **6.0:1** by night (`#4b171c`), so month grids and figure tables placed on a deep band use the light brass in both modes. On day paper, light brass falls to **2.1:1**, so only the dark brass serves for figures there. The night oxblood `#8f2a31` remains a fill only, at 2.2:1 on night paper.

### The two failure modes are the navy default and the gold-on-black template

The category default is well documented: "navy blue, a sans-serif font, a stock photo of a city skyline, and a generic tagline about 'delivering results'" ([Wolf Financial](https://wolf.financial/blog/visual-identity-design-guide-financial-brands); the attribution comes from a search summary). Another source describes "navy blue palettes, conservative serif wordmarks and reassuring imagery of handshakes or ascending charts" ([The Brand Identity](https://the-brandidentity.com/project/20something-uses-editorial-design-to-reinvent-finance-branding)).

A second, newer default matters more for this brief. Marketplace "Luxe Wealth Management" templates already ship "dark cinematic imagery, gold serif accents… dramatic full-bleed heroes featuring gold-accented serif typography layered over luxury lifestyle photography" ([Converge template](https://enter.converge.ai/marketplace/templates/luxe-wealth-management-firm-website-629)). The night palette plus brass sits one careless step from that template. The guard is a rule: **brass never sets a headline, and night headlines are warm off-white (`#efe6dc`)**.

Hermès' January 2026 site adds commissioned, hand-drawn lithograph illustrations by Linda Merad, one for each section ([Domus](https://www.domusweb.it/en/news/2026/01/07/herms-new-website.html); [Fast Company](https://www.fastcompany.com/91471305/hermes-hand-illustrated-website-is-the-ultimate-luxury)). This is the strongest counter-example to the brief's illustration ban. It is a named artist's seasonal craft statement, not an icon grid, so the ban stands for this firm.

Part of the evidence base is soft. No study measuring which visual cues raise trust for professional-services sites was found, so the "expensive" signals above are practitioner consensus plus observed practice, not tested effects.

---

## 4. Looped Thai and Song Chinese are their scripts' serifs

### Thai: the loop carries formality, and the banks have left it behind

Thai typographers state the pairing convention plainly. "The loop is to Thai letters as the serif is to Latin characters", so looped fonts go with Latin serifs and loopless ones with Latin sans. They add that the rule is flexible, not a law ([ATypI: Thai Type Pairing](https://atypi.org/presentation/thai-type-pairing/); search snippet only). Thai design press links looped forms with trust and quality, and with finance, law, publishing and luxury. It links loopless forms with tech, startups and digital media ([GIANT PRINT](https://giantprint.co.th/font-selection-branding-sme/); a popular source rather than an authority).

The market split is sharp. "By 2024, every major Thai product including KBank Plus, SCB Easy, LINE MAN, Grab Thailand, and Shopee Thailand had shipped with loopless Thai as the UI default." Meanwhile, looped Thai still "dominates traditional publishing and is prevalent in education and official contexts" ([ThaiGraph, Loopless Revolution, April 2026](https://thaigraph.com/learn/typography/loopless-revolution/)). Cadson Demak's Thong Lor project shows that the foundry best known for loopless corporate faces now worries that loopless "risked crowding out the looped forms that are so central to Thai identity". It answered with a wide, modern looped design meant "to encourage slower reading" ([GRANSHAN: Thong Lor](https://granshan.com/insights/thong-lor-and-the-return-of-the-loop-cadson-demaks-typographic-bridge-to-thai-identity)).

For this firm, a looped Thai serif is therefore both the "correct" partner for Cormorant and a positioning signal. It reads as private, official and heritage, unlike the loopless type of mass-market banking.

Premium Thai institutions invest in custom Thai faces. Cadson Demak drew a custom face for Krungsri as part of its identity refresh ([Cadson Demak: Krungsri](https://font.cadsondemak.com/foundry/krungsri-%E0%B8%98%E0%B8%99%E0%B8%B2%E0%B8%84%E0%B8%B2%E0%B8%A3%E0%B8%81%E0%B8%A3%E0%B8%B8%E0%B8%87%E0%B8%A8%E0%B8%A3%E0%B8%B5/)). Its other custom clients include AIS and Thai Beverage ([MyFonts interview](https://www.myfonts.com/pages/newsletters-cc-201103)). **Which Thai fonts SCB, KBank, Bangkok Bank, Tilleke & Gibbins, the Big Four and Bangkok's luxury hotels actually render was not verified**, because every one of those sites was blocked.

### Chinese: Song with a Latin serif, Latin glyphs from the Latin font

Chinese practice mirrors the Latin rule: "尽可能地用衬线体配衬线体" (pair serif with serif wherever possible). Song (宋体) pairs with Latin serifs because their stroke character and temperament match. The guidance also says to use a real Latin font rather than the Latin glyphs bundled in the Chinese one ([Canva.cn](https://www.canva.cn/learn/chinese-english-fonts-typesetting-question/)). The same Chinese design press advises setting **Latin about 10–15% larger than Chinese** to balance height and weight. That fits Cormorant's small x-height, though the advice comes from a blended snippet. Web practice declares the English font first in `font-family`, so Latin and numerals come from the Latin face ([Fei Ye: 思源宋体](https://blog.yfei.page/cn/2020/12/siyuansongti/); [少数派](https://sspai.com/post/38705)).

The W3C Chinese layout requirements set three rules ([W3C clreq](https://www.w3.org/TR/clreq/), snippet only):
- a gap of **at least 1/8 em** between Chinese and Latin runs;
- a line gap of 50–100% of the character frame, which is roughly CSS `line-height` 1.5–2.0;
- full-width punctuation, where the dash and ellipsis take two ems and must not break across a line.

The global luxury houses offer no ready model. No published evidence was found of bespoke Thai or Chinese companions for Hermès, Aesop, Rolex or Cartier. Monotype Hong Kong does build custom Simplified and Traditional faces for global brands ([MyFonts: Monotype HK](https://www.myfonts.com/collections/monotype-hk-foundry)). The working hypothesis, unverified, is that most global sites let Thai and Chinese text fall to system or Noto fonts and carry the premium feel through restraint alone. If so, a properly paired looped Thai serif and a Song Chinese face would already exceed the norm.

### Typesetting rules that hold across all three directions

| Rule | Thai (`:lang(th)`) | Simplified Chinese (`:lang(zh-Hans)`) | Basis |
|---|---|---|---|
| Line-height, body | 1.7–1.8 | 1.7–1.8 | Thai: at least 1.55 because of stacked marks ([r12a](https://r12a.github.io/scripts/thai/th.html), snippet). Chinese: 1.5–2.0 ([W3C clreq](https://www.w3.org/TR/clreq/)) |
| Line-height, headings | 1.25–1.35 (looser than Latin display, to stop tone marks clipping) | 1.3–1.4 | Inference, to be tested |
| Size against Cormorant | About 1.05–1.15× the Latin size for body | Equal or slightly smaller; display often smaller than the Latin | Cormorant's small x-height; the Canva.cn 10–15% rule |
| Letter-spacing | None on body (Thai has no word spaces) | At most about 0.02em | Inference; #05 §5 |
| Emphasis | Weight or oxblood colour, never italic | Weight, colour or `text-emphasis` dots, never italic | `font-synthesis: none` to stop fake bold or italic ([CSS-Tricks](https://css-tricks.com/?p=318556)) |
| Mixed-script lines | Latin font first in the stack; numerals stay in the Latin face | Same, plus a gap of at least 1/8 em around Latin runs | [W3C clreq](https://www.w3.org/TR/clreq/) |
| Alignment | Never `justify` | Justify allowed, `inter-character` | #05 §5 |

---

## 5. Free fonts cover all three scripts; Chinese payload is the real cost

### Candidates, licences and measured loading cost

The sizes below were **measured on 5 October 2026** from the Google Fonts CSS2 API, as Latin or Thai WOFF2 slices. Licences come from the `google/fonts` METADATA files. Commercial prices come from search summaries and are **unverified**, because every foundry site was blocked.

| Role | Font | Licence | Weights | Measured cost | Fit |
|---|---|---|---|---|---|
| Latin display | **Cormorant Garamond** | OFL ([METADATA](https://raw.githubusercontent.com/google/fonts/main/ofl/cormorantgaramond/METADATA.pb)) | Variable 300–700, plus italic | **36.8 KB** for the whole range; 22.8 KB for one static weight ([API](https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300..700;1,300..700&display=swap)) | The brief's chosen character; weak below about 18–20 px (inference) |
| Latin display, extras | Cormorant SC, Cormorant Upright | OFL | Static 300–700 | Small | Small caps for labels; Upright for the monogram ([README](https://raw.githubusercontent.com/CatharsisFonts/Cormorant/master/README.md)) |
| Latin display, free alternative | Gloock | OFL | 400 | 25.7 KB | Single-word heroes only |
| Latin display, paid | Canela · GT Super · Ogg · Saol · Tiempos Headline · Editorial New | Commercial | — | About US$600–900 one-off for a GT Super or Canela family; Editorial New web licence "from $30" | Unverified; may be desktop prices ([Grilli](https://www.grillitype.com/shops/gt-super); [Commercial Type](https://commercialtype.com/catalog/canela); [licenseorg](https://licenseorg.com/guide/fonts/pangram-pangram)) |
| Latin body, serif | **Newsreader** | OFL | Optical size 6–72, weight 200–800 | 128.9 KB (full variable) | Strongest text partner for fragile display hairlines |
| Latin body, serif | Source Serif 4 | OFL | Optical size 8–60, weight 200–900 | 119.5 KB | More neutral and institutional |
| Latin body, serif | EB Garamond · Crimson Pro | OFL | — | 43.3 · 47.1 KB | Lighter, but two Garamonds lack contrast of role |
| Latin UI, sans | **Hanken Grotesk** | OFL | 100–900 | 33.9 KB | Small labels and nav only. (Instrument Sans, 29.4 KB, shares a name with the retired Instrument Serif.) |
| Thai display | **Trirong** (Cadson Demak) | OFL ([DESCRIPTION](https://raw.githubusercontent.com/google/fonts/main/ofl/trirong/DESCRIPTION.en_us.html)) | 100–900, plus italic | **15.9 KB** Thai slice per weight | Narrow, tall, "thick and thin strokes", formal: the closest to Cormorant |
| Thai body, serif | **Taviraj** (Cadson Demak) | OFL ([DESCRIPTION](https://raw.githubusercontent.com/google/fonts/main/ofl/taviraj/DESCRIPTION.en_us.html)) | 100–900, plus italic | 15.7 KB | Wide and airy; readable at length |
| Thai serif, neutral | Noto Serif Thai | OFL | Variable 100–900 | 32.0 KB (variable range) | Quieter, highly legible fallback |
| Thai body or UI, looped sans | **IBM Plex Sans Thai Looped** · Sarabun · Noto Sans Thai Looped | OFL | — | 13.3 · 9.6 · 11.0 KB | Plex Looped is the corporate-grade body; Sarabun is the Government Gazette face ([METADATA](https://raw.githubusercontent.com/google/fonts/main/ofl/sarabun/METADATA.pb)) |
| Thai display, accent | Chonburi | OFL | 400 | 10.3 KB | Looped display serif; reads "poster", so use sparingly |
| Thai, paid | Cadson Demak retail (e.g. Thong Lor) · DB Fonts | Commercial; some on Adobe Fonts | — | Unverified (MyFonts lists styles from US$29, desktop) | Only if a bespoke look is wanted |
| Chinese serif | **Noto Serif SC** (= Source Han Serif) | OFL, © Adobe ([METADATA](https://raw.githubusercontent.com/google/fonts/main/ofl/notoserifsc/METADATA.pb)) | Variable 200–900 | **406 KB per weight** via Google for a 121-character page; **22 KB** (static 400) or 43 KB (variable) subset at build time | The only mature free Song with a full weight range |
| Chinese sans | Noto Sans SC | OFL | Variable 100–900 | Not measured separately | UI and body in Direction B |
| Chinese, rejected | LXGW WenKai · Zhuque Fangsong · ZCOOL XiaoWei | OFL | — | — | Too casual (its own author advises against long text), pre-release, or decorative ([WenKai README](https://raw.githubusercontent.com/lxgw/LxgwWenKai/main/README.md); [Zhuque README](https://raw.githubusercontent.com/TrionesType/zhuque/main/README.md)) |

### Thai and Latin are cheap; Chinese decides the loading strategy

Thai costs almost nothing. Two weights of Trirong plus one of Sarabun add under 50 KB of Thai glyphs. The Latin layer is about 37 KB for Cormorant, plus 34–129 KB depending on the body face. Instancing Newsreader to the weights actually used would cut its 129 KB.

Chinese is a different order of magnitude. Google serves Noto Serif SC as **101 slices totalling 3.18 MB per weight**. A realistic 121-character firm paragraph pulled 11 of those slices, **406 KB for a single weight** ([API](https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400&display=swap)). The same characters subset with `pyftsubset` came to **22 KB**. Even a site-wide subset of the 3,755 common characters weighs 679 KB static, or 1.37 MB variable.

Because the builder knows every character on the site at publish time, **subsetting at build time is the single biggest performance decision**. The Apache-2.0 tool cn-font-split runs in the browser via WASM, which fits a no-server builder ([cn-font-split README](https://raw.githubusercontent.com/KonghaYao/cn-font-split/master/README.md)). Google-hosted Noto Serif SC would remain only a fallback, for text added without a rebuild.

Four other loading rules apply to all three directions:
- Preload only the Cormorant Latin file; never preload CJK.
- Use `font-display: swap`.
- Keep at most three families per language page.
- Use one Chinese weight for body and one for headings. Light-to-medium Song (300–500) keeps the "measured" feel; heavy Song reads as a newspaper headline.

### Figures need a check before the tables are designed

The brief puts figures in tables and month grids, and lists old-style figures as allowed. **Whether Cormorant Garamond's default numerals are old-style or lining, and whether it supports tabular figures, was not verified.** Financial tables need tabular, aligned figures (`font-variant-numeric: tabular-nums`). If Cormorant lacks them, table figures should come from the body face, which also gives sturdier digits at 15–17 px than Cormorant's hairlines. This is check #11 in section 9.

---

## 6. Premium photography is material, light and real people

### The luxury recipe: materials, hands and diffused light

The best-documented premium photography comes from luxury houses, not finance. Aesop's system of "amber bottles, stone-toned palettes, restrained lighting, and ingredient-led details" feels "premium without losing realism" ([Photoroom: Aesop](https://www.photoroom.com/100-best-product-pages/beauty/aesop)). Beverley Hyde's still lifes for Aesop use "diffused" light that brings out "the rough surfaces of the props" against muted brown grounds ([visie.io](https://visie.io/media/beverley-hyde-68227)). Loro Piana's handbag campaign crops tight on zips, stitching and leather grain, and "luxury is communicated through material intelligence rather than excess" ([The Impression](https://theimpression.com/?p=11829021)). Its craft imagery shows artisans' hands working merino, with no face in frame ([Rain Magazine](https://rain-mag.com/loro-piana-record-bale-award-2024-a-new-milestone-in-merino-wool-excellence/loro-piana_record-bale-award_merino-wool-fiber-4)).

Among the banks, Lombard Odier stands out. It hired a branding chief from luxury fashion ([Management Today](https://www.managementtoday.co.uk/case-study-rebranding-swiss-bank/reputation-matters/article/1455188)). Its 2024 nature campaign won an FT PWM award for "compelling imagery and text" without showing a single banker ([Lombard Odier](https://www.lombardodier.com/fr/insights/2024/november/lombard-odier-s-nature-s-regene.html)). Law firms favour documentary portraits taken in the lawyers' own setting, art-directed for a "professional yet warm atmosphere" ([Retines](https://retines.fr/en/blog/project/corporate-portrait-for-a-law-firm-in-paris/); [Lawyers Weekly](https://www.lawyersweekly.com.au/folklaw/8774-capturing-lawyers-in-the-moment)).

This translates directly to an oxblood, brass and paper firm. The subjects are:
- paper, ledgers, fountain pens, a brass seal or stamp, archive boxes;
- teak, terrazzo and plaster details of a Bangkok shophouse;
- hands signing or turning pages;
- faces only for the real partners.

All of it should be shot in window light, with few images placed large and surrounded by deliberate emptiness.

### What reads generic, and the one-line test

The markers of stereotyped stock are consistent: "artificial, bright lighting; unnatural posing with no movement; people smiling and looking directly into the camera; and a lack of context" ([ExpertPhotography](https://expertphotography.com/types-of-stock-photos)). The handshake "does not say anything specific about the business" ([LockeDown SEO](https://lockedownseo.com/avoiding-stock-photography-cliches/)). Hinge Marketing warns that imagery that differs little from competitors' invites "confusion — and forgetting" ([Hinge](https://hingemarketing.com/blog/story/is-your-imagery-damaging-your-image), from a search snippet). A practical test for every image follows from this: **could a competitor post it unchanged?** If yes, it is generic.

### One house grade keeps a mixed library consistent

Brands keep imagery from many sources consistent with a bespoke grade. Umicore even publishes a colour-grading page in its guidelines ([Umicore](https://brand.umicore.com/en/visual-identity/photography/color-grading/)). Duotone maps image brightness to two colours. That unifies photos from different sources ([IMG.LY](https://img.ly/docs/cesdk/js/filters-and-effects/duotone-831fc5/)), but it "can strip the image of depth and meaning" ([GoSpotCheck](https://brand.gospotcheck.com/photography)).

Three treatments follow, and each maps to one direction:
- **A warm house grade** on full-colour photos: slightly warm white balance, warm-lifted shadows, muted blues and greens, and fine grain matched to the paper texture.
- **Warm-toned black and white**, for portraits from shoots in varying conditions.
- **Oxblood or night duotone**, for full-bleed heroes and to rescue weak images.

The builder's existing in-browser image pipeline can apply the grade on upload, or at render time through an SVG `feColorMatrix` filter. The grade then holds whoever uploads the image (inference; see report #07). In night mode, images need slightly reduced brightness so they do not glare against `#1b1112`.

### Video is premium when slow, silent and material

The brief allows video and sliders (M5). Video reads premium when it is a short, near-monochrome material loop: ink on paper, light moving across stone. The technical floor is:
- `autoplay muted loop playsinline` ([Swarmify](https://swarmify.com/blog/how-to-make-an-autoplaying-background-video/));
- a poster that looks like the first frame ([ProfileTree](https://profiletree.com/background-videos/));
- loading only when the section enters view;
- showing the poster only under `prefers-reduced-motion` ([specification.website](https://specification.website/spec/accessibility/reduced-motion/)).

A visible pause control is also expected (WCAG 2.2.2; unverified this session).

### Sources and costs

| Source | Cost | Use | Caution |
|---|---|---|---|
| **Commissioned Bangkok shoot** (half or full day: portraits, office, hands, still life) | **Bangkok quote unknown**; US benchmark **US$150–350 per person** for headshots ([BetterPic](https://www.betterpic.io/blog/company-headshot-photographer-pricing-2026)) | The signature library; the only route to differentiated images | Get quotes from two or three Bangkok corporate studios |
| Stocksy | US$15–125 per image, standard licence ([Photutorial](https://photutorial.com/stocksy-review)) | Texture, architecture and still-life gaps | Search material terms, not "business" |
| Adobe Stock Premium | US$96–250 or more per image (sources conflict) ([Lapse of the Shutter](https://www.lapseoftheshutter.com/adobe-stock-pricing/)) | Same | Check live prices |
| Getty Creative | About US$150–499 per image ([Lapse of the Shutter](https://www.lapseoftheshutter.com/adobe-stock-vs-getty/)) | Rarely needed | — |
| Unsplash+ | US$7–20 a month, with a US$10,000 indemnity ([Photutorial](https://photutorial.com/unsplash-review)) | Low-stakes article thumbnails | — |
| Free Unsplash | Free | Avoid for anything showing people | No model releases, no indemnity ([Pixsy](https://pixsy.com/image-licensing/unsplash-guide)) |
| Thai landmark stock | Royalty-free options exist ([Getty example](https://www.gettyimages.com/detail/photo/temple-of-the-emerald-buddha-or-wat-phra-kaew-royalty-free-image/1290084794)) | Avoid as decoration | Some are editorial-only. Buddha, royal and temple-interior imagery is culturally and legally sensitive for a commercial brand (opinion; **unverified**, check before use) |

Keep a licence register for every image: source, ID, licence, date and releases. For accessibility, alt text should be a required field with a "decorative" option that outputs `alt=""`. The W3C decision tree is the reference ([W3C WAI](https://www.w3.org/WAI/tutorials/images/decision-tree/); its wording was unverified because the page was blocked).

---

## 7. Do/don't list and pattern catalogue

### Do and don't

| Do | Don't | Why |
|---|---|---|
| Anchor oxblood to the header bar, the bands and buttons, with the seal inside the bar | Tint text, borders, icons and buttons in oxblood all at once | Pictet and Cartier anchor their red to one object |
| Keep reading surfaces warm paper `#f2eeea` with grain | Pure white, or red-washed night screens | Aesop's parchment; Patek's achromatic dark |
| Use brass only for figures, rules and the seal: dark brass on paper, light brass on oxblood and deep bands | Brass headlines; gold serif over dark photos | The "luxe wealth" template trap ([Converge](https://enter.converge.ai/marketplace/templates/luxe-wealth-management-firm-website-629)) |
| 0px corners everywhere | Rounded cards, soft shadows, glass, gradients | Aesop and Cartier run 0px; the brief bans the rest |
| One expressive serif for headlines at a measured, left-aligned size; one quiet face for working text | Light Cormorant below about 18 px; giant display words | Two-voice systems at Pictet, Aesop and Cartier |
| Looped Thai; Song Chinese; Latin and numerals in the Latin face | Loopless Thai for headings or body; Hei-only Chinese headlines; italic Thai or Chinese | The pairing conventions in section 4 |
| Figures in quiet tables and month grids with tabular digits | Giant numerals, animated counters, "500+ clients" hero stats | Brief D5 |
| Turn the firm's real history (founding year, licences, partner signatures) into content | Invented heritage ornament | Pictet, Hoare's and Coutts |
| Material still life, hands at work, documentary partner portraits, one house grade | Handshakes, skylines, smiling teams at laptops, rising arrows, chess pieces, piggy banks | The stock-cliché sources in section 6 |
| Short rise or fade, honouring reduced motion | Parallax, auto-advancing fast carousels, scroll-jacking | Aesop's "calm transitions"; brief D11 |
| Contact, including LINE OA, as an in-brand header link or a quiet fixed tab | Pop-ups, floating chat bubbles with badges | Brief M6; #33 constraint on #18 |
| Client-outcome voice with specific results ("Close every month knowing exactly where you stand.") | "Delivering results", "your trusted partner" | Category cliché ([Wolf Financial](https://wolf.financial/blog/visual-identity-design-guide-financial-brands)) |

### Pattern catalogue

Codes P1–P18 are referenced by the directions in section 11. "Precedent" names the documented source. "Brief" marks a pattern the owner already chose in #33.

| # | Pattern | Precedent | A | B | C |
|---|---|---|---|---|---|
| P1 | Oxblood header bar on every page, wordmark and seal in light brass | Brief D8 (no bank precedent found) | ● | ● | ● |
| P2 | Alternating paper / oxblood / deep bands | Brief D3 | Sparse (1–2 bands) | Full rhythm | Deep-band-led |
| P3 | Oxblood opening band | Brief D3 (also liked) | — | ● | ● (deep) |
| P4 | Signature colour anchored to one emblem (the monogram seal) | Pictet lion; Cartier box | ● | ● | ●● |
| P5 | Red plus metal detail (brass figures and seal) | Cartier's gold garland; Rothschild's gold | ● | ● | ●● |
| P6 | Zero-radius geometry, hairline rules | Aesop, Cartier | ● | ● | ● |
| P7 | Warm paper ground with grain | Aesop `#fffef2` | ●● | ● | ● (night paper) |
| P8 | Album-style double-rule frame around portraits or hero | Coutts' framing devices | ● | ● | ●● |
| P9 | Seal on the rule between sections | Brief D10 | ●● | ● | ● |
| P10 | Stitched oxblood band as section punctuation | Brief A11 / D10 | ● | ●● | ● |
| P11 | Heritage as content (founding, licences, signatures) | Pictet, Hoare's, Coutts | ●● | ● | ● |
| P12 | Material still life in a warm house grade | Aesop, Loro Piana | ●● | ● | — |
| P13 | Documentary partner portraits in situ, warm B&W | Law-firm practice | ● | ●● | ● |
| P14 | Hands, not faces, for process imagery | Loro Piana | ● | ●● | ● |
| P15 | Duotone hero in night tones, slow material video loop | IMG.LY duotone; Patek's dark photography | — | — | ●● |
| P16 | Title-left / list-right services; classic article column; key-facts box | Brief D6 / D9 | ● | ●● | ● |
| P17 | Quiet table and month grid in brass figures | Brief D5 | ● | ●● (on deep band) | ● |
| P18 | Calm rise or fade, reduced-motion aware | Aesop; brief D11 | ● | ● | ● |

● = used, ●● = emphasised, — = not used.

---

## 8. Where this report supersedes report #05

Report #05 was written for the retired Navy & Soft Linen identity, with Instrument Serif and Inter as the Latin pair. Its typesetting rules (`lang` attributes, no Thai justification, Chinese punctuation, no italics in Thai or Chinese, Arabic digits) still stand. Six things change.

First, **every pairing in #05 was built to sit beside Inter**. That is why it recommended Sarabun as the top Thai body face and Noto Sans SC for Chinese body. With Cormorant, the Thai partners move to Trirong for display and either Taviraj or IBM Plex Sans Thai Looped for body, depending on the direction. Sarabun drops to UI labels.

Second, #05 decided on **"Google Fonts, no self-hosting"** for Chinese and budgeted roughly 0.9–1.4 MB per Chinese page. This report's measurement shows a 22 KB build-time subset against 406 KB from Google for the same text. It therefore **reverses that decision**: subset at build time, with Google as the fallback.

Third, #05's warning that Noto Sans SC "has no 600 instance" no longer applies. Requested as a weight range, both Noto SC families are served variable (Sans 100–900, Serif 200–900).

Fourth, #05's floor of "never below 400 for Thai text" was set for thin loops on Soft Linen. It **still holds for Thai body text**. The font note's suggestion of Trirong 300 applies only to display sizes, and only if it passes the specimen test.

Fifth, the Thai line-heights are slightly looser here (1.7–1.8 for body, 1.25–1.35 for headings, against #05's 1.7–1.75 and 1.2–1.3), because a high-contrast looped serif clips more easily.

Sixth, #05's figure of 9.6 KB for Noto Serif Thai was a static 400 weight. The 32 KB here is the full variable range, so the two figures do not conflict.

---

## 9. Evidence limits and what #35 must check in a real browser

The proxy blocked direct visits to:
- every brand site named: Pictet, Hoare's, Lombard Odier, Coutts, Rothschild & Co, Slaughter and May, Wachtell, Cravath, Lazard, Hermès, Aesop, Loro Piana, Patek, A. Lange & Söhne and Cartier;
- every Thai and Chinese bank, law-firm and hotel site;
- the foundries: Klim, Commercial Type, Grilli, Sharp Type, Pangram Pangram, Displaay and Cadson Demak;
- the design press: Creative Review, Fonts In Use, GRANSHAN, ATypI and ThaiGraph pages;
- the standards and guidance sites: W3C, web.dev and MDN.

**First-hand evidence** covers only font file sizes, weight ranges, subsets and licences (from the Google Fonts API, `google/fonts` METADATA and the project READMEs), the Chinese subsetting measurements, and this report's contrast calculations. Everything about how brands look comes from search summaries, Brandfetch auto-extraction or shadcn.io third-party token extraction.

The notes flagged some statements as **unverified model recall**. They are kept below as hypotheses and are not used as findings: Wachtell's text-only site, Lazard's green-black wordmark, Lombard Odier's black-and-white large photography, Patek's dark presentation, Coutts' navy crown, Rothschild's gold symbol, and Pictet, Rothschild and Coutts favouring architecture over meeting shots.

| # | Check in a real browser during #35 | Why it matters |
|---|---|---|
| 1 | **Pictet live site:** where `#A04044` appears (header bar? bands? logo only?), and the computed type sizes and rules | The closest red precedent; it calibrates how much oxblood is "quiet" |
| 2 | Any private bank or law firm using a **full-width coloured header bar** | The brief's boldest move has no precedent yet |
| 3 | Aesop, Cartier, Hermès, Patek: confirm 0px radius, the canvas colours, and the real font names (not fallbacks) | The shadcn.io extractions are third-party |
| 4 | Headline sizes, letter-spacing, grid columns, header heights, button styling and CTA labels on 4–5 benchmark sites | None were measured; #35 needs real numbers for "measured size" |
| 5 | How private banks present numbers (fact tables, tabular figures, AUM) | No source found; it feeds P17 |
| 6 | Whether any benchmark reacts to `prefers-color-scheme` | The night-mode precedent is unknown |
| 7 | Rendered Thai fonts (DevTools → Computed → Rendered Fonts) on SCB/KBank Private, Krungsri, Bangkok Bank, Tilleke & Gibbins, Baker McKenzie TH, Weerawong C&P, Big Four TH, Mandarin Oriental, Capella, Rosewood, Siam Paragon, ICONSIAM | Looped or loopless, Thai versus Latin size and line-height |
| 8 | TH and ZH pages of Hermès, Aesop, Rolex, Cartier (hermes.cn, aesop.com/th, rolex.cn, cartier.cn): font, Song or Hei, line-height, whether the brand's Latin face stays on Latin words | Tests the "system fonts plus restraint" hypothesis |
| 9 | Chinese finance and law sites (Bank of Singapore, UOB Private, CICC, HSBC China, Hang Seng, KWM, Fangda): rendered fonts | Song versus Hei norms in the sector |
| 10 | Foundry web-licence prices and terms (Canela, GT Super, Ogg, Saol, Tiempos, Editorial New): flat fee or pageview tier | Needed before the owner decides on a paid font |
| 11 | **Cormorant Garamond figures:** default old-style or lining, `tnum`/`lnum` support; x-height compared with Trirong, Taviraj and Noto Serif SC, to set `size-adjust` | Tables and month grids; trilingual size matching |
| 12 | A rendered specimen of all three pairings at 320/390/720/1200 px, on Windows ClearType and iPhone; Trirong 300 at display size | No visual specimen review was possible |
| 13 | Noto Sans SC payload; cn-font-split running in the builder; real CLS when fonts swap | Direction B's Chinese body; performance budget (#30) |
| 14 | Live Stocksy and Adobe prices; quotes from two or three Bangkok corporate photographers | The sources conflict; there is no THB data |
| 15 | W3C alt decision tree wording; WCAG 2.2.2 pause rule; web.dev lazy-video guidance; GitHub file-size limits for video | Recalled only; needed for builder rules |
| 16 | The recall hypotheses listed above this table | Before any of them is quoted |
| 17 | Thai rules on commercial use of royal and religious imagery | The caution in section 6 is unsourced |

---

## 10. Conclusion

The benchmark changes the question #35 must answer. The brief's ingredients are already well precedented: oxblood, brass, paper, serif and seal. The design risk is **dosage**. Every documented luxury precedent uses less signature colour than the brief demands. So the three directions should differ mainly in *how much* oxblood the page carries, and *where*: bar only plus rare bands, full alternation, or night-led deep bands. They should not differ in which ornaments they add.

The second insight is that the trilingual requirement is an asset, not a burden. Looped Thai and Song Chinese are each script's "formal serif", and both have drifted out of mainstream digital banking. Setting them carefully beside Cormorant would give the firm a typographic register that most Thai banks and most global luxury sites appear not to attempt. That claim rests on an inference that #35 should confirm in a browser.

---

## 11. Recommendations for #35

All three directions share the same base:
- the locked palette and both modes;
- 0px corners;
- the oxblood header bar (P1);
- solid oxblood and outline buttons;
- a client-outcome voice;
- a short rise or fade, honouring reduced motion;
- build-time font subsetting;
- the `:lang()` typesetting rules in section 4.

The directions differ in type voice, oxblood dosage, photography and which signature details lead. Brass rules apply in every direction: **dark brass `#7d5f28` on paper, light brass `#c4a06a` on the oxblood bar and on deep bands, never on headlines.**

### Direction A — "Maison": the quiet library (serif throughout)

| Aspect | Specification |
|---|---|
| Idea | Closest to Aesop and Hermès restraint. The page is mostly paper; colour is an event. |
| Latin | Cormorant Garamond 300/500 plus italic for display; **Newsreader** 400 for body (17–18 px); Cormorant SC for small labels |
| Thai | Trirong 400 for display (300 only if the specimen passes); **Taviraj 400** for body; Sarabun 500 for tiny UI |
| Chinese | Noto Serif SC 300–500 for display; Noto Serif SC 400 for body (Song all the way, at 17 px or more) |
| Oxblood | Header bar, plus **one or two** deep or oxblood bands per page (for example the outcome statement and the contact). Everything else is paper. |
| Brass | Dark brass figures in quiet tables on paper; light-brass seal in the bar |
| Photography | **Material still life** (P12) in a warm full-colour house grade; few images, large, set in deliberate emptiness; partners in colour, framed |
| Signature details | **Paper grain, seal on the rule (P9), deliberate emptiness** first; double-rule frame on the hero and portraits; stitched band once, at the footer |
| Payload | Latin about 37 + 129 KB (less if Newsreader is instanced); Thai +about 32 KB; Chinese about 22–43 KB per weight subset |
| Risk | It may read too quiet against "bold". The bar and the one or two bands must carry the confidence. Song body text needs testing on Windows. |

### Direction B — "Atelier": the working ledger (serif headlines, looped-sans body)

| Aspect | Specification |
|---|---|
| Idea | The firm at work. It is the boldest colour rhythm, with the most legible body on phones, and it is practical and outcome-led. |
| Latin | Cormorant Garamond 400/500 plus italic for display and pull-quotes; **Hanken Grotesk** 400 for body and UI |
| Thai | Trirong 400 for display; **IBM Plex Sans Thai Looped** 400 for body (looped, so it stays formal); pull-quotes in Trirong 400, never Thai italics |
| Chinese | Noto Serif SC 500 for display; **Noto Sans SC** 400 for body; Noto Serif SC 400 for quotes |
| Oxblood | **Full alternation** (P2) with an oxblood opening band (P3): paper → oxblood → paper → deep, down every long page |
| Brass | **Month grid and figure tables on a deep band in light brass** (P17); dark brass on paper tables |
| Photography | **Documentary partner portraits in situ, warm black and white** (P13); hands at work (P14); one material still life per page at most |
| Signature details | **Stitched oxblood band (P10)** as section punctuation; seal on the rule; double-rule frame around portraits; grain kept subtle |
| Payload | The lightest Latin, about 37 + 34 KB; Thai about 29 KB; Chinese serif and sans subsets |
| Risk | A sans body moves closer to "modern". The serif must own every headline, quote and figure label so that sans never reads as "everywhere". |

### Direction C — "Haute Contrast": the night salon (dark-led, editorial contrast)

| Aspect | Specification |
|---|---|
| Idea | The Night Library as the defining mood: deep bands and dark imagery, with stronger stroke contrast and weight rather than larger size. Day mode keeps the same structure on paper. |
| Latin | Cormorant Garamond 600/700 for display at a measured size (or a **paid** GT Super or Canela, about US$600–900, unverified); Source Serif 4 400 for body; Hanken Grotesk 500 for UI |
| Thai | **Trirong 500–600** for display (Chonburi tested only for single words); Trirong 400 for body at 18 px or more; Sarabun 500 for UI |
| Chinese | Noto Serif SC 600 for display; Noto Serif SC 400 for body; Noto Sans SC 500 for UI |
| Oxblood | **Deep bands lead** (P2, deep-led); in night mode oxblood `#8f2a31` is fill only (2.2:1); the header bar is the main oxblood moment |
| Brass | Light brass figures on deep bands and in night mode; the **seal at its largest** (P4); brass rules framing the hero; **never brass headlines** (headlines are `#efe6dc` or `#f2e8e0`) |
| Photography | **Duotone heroes** in night tones (P15); one slow, silent material video loop with a poster frame; portraits in the duotone or the warm B&W |
| Signature details | **Double-rule frame (P8) and monogram seal (P4)** emphasised; deliberate emptiness around the hero; grain on the night paper |
| Payload | Latin about 37 + 120 + 34 KB; Thai about 32 + 10 KB; Chinese two serif weights subset; video 1–3 MB, loaded lazily |
| Risk | It sits closest to the "gold serif on a black hero" template (section 3). It succeeds only if brass stays on figures and rules, and display size stays measured. |

**Suggested method for #35**, following the round-8 lesson in #33: render all three as complete pages in real context, in both modes and all three languages, with the specimen strings from #05 §6. The owner rates them dimension by dimension, rather than choosing between thumbnails.

---

## 12. Open questions for the owner

1. **Photography budget.** Will you commission a half-day or full-day shoot in Bangkok (partner portraits, the office, hands at work, still life of paper, pens and brass)? The Bangkok price is unknown. The US benchmark is US$150–350 per person for portraits, so quotes are needed. Or should the site launch on curated stock (Stocksy at roughly US$15–125 per image) and add the shoot later? Directions B and C depend more on the shoot than A does.
2. **Faces on the site.** Are the partners willing to appear by name and photograph? Direction B is built on documentary portraits; Direction A can work with still life alone.
3. **Paid font.** Is a one-time spend of about US$600–900 (price unverified) acceptable for a commercial Latin headline face in Direction C? Or should every direction stay on free fonts? Thai and Chinese stay free either way.
4. **Heritage material.** What real material can the site use? For example: the founding year, licence numbers (CPA or tax-auditor registration), partner signatures, old documents or ledgers. The benchmark shows heritage-as-content as a strong premium signal, but only with genuine material.
5. **The seal.** Which letters and which script form the monogram seal: Latin initials, Thai, or a Chinese-style seal? The seal appears in every direction, and in Chinese culture a seal carries specific meaning.
6. ~~Years in tables and month grids.~~ **Already decided in #11:** Gregorian years on Thai pages (`5 ตุลาคม 2026`), `2026年10月5日` on Chinese pages, formatted from fixed tables in the generator. Not an open question.
7. **Homepage video.** Video is allowed. Do you want a slow material video loop on the homepage (Direction C)? It needs footage from the shoot in question 1, or licensed stock footage.
