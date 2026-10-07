# Baseline: what money already buys

**Sites reviewed:** 4 paid Framer templates for accounting firms: accora, accura, ashworth, auditly. ledgerhouse returned
*Framer "Site Not Found"*, so there was nothing to review. Also sa-accounttax.com (a Thai SME accounting firm), KPMG Thailand,
EY Thailand, and our own current hand-made site.

This file does the opposite of the brief. It lists the habits that make these sites look ordinary, so the Design
Library can avoid them on purpose. Crops: `findings/crops/baseline-1.jpg` … `baseline-9.jpg`.

---

## 1. The ten patterns that define "ordinary"

### 1. The hero formula
A tracked uppercase **eyebrow with dot separators** sits above a **2-line headline of 56–84px**. **One word is recoloured or
italicised** in the accent. Below come a 1–2 line grey subhead (14–20px) and a **filled pill button next to a ghost button**,
usually centred.
- Accora: `ACCOUNTING • TAX • ADVISORY` / "Finance that moves you forward", Hedvig Letters Serif 68px.
- Auditly: Google chip "4.8 ★ 376 vote" / "Clear **Numbers**. Confident Decisions", Apfel Grotezk Bold 82px, "Numbers" in green #017931.
- Ours: `TAX · LEGAL · ONBOARDING · BANGKOK` / "Thailand, made *straightforward.*", Instrument Serif 64px, gold italic accent.
- The same accent-word trick appears again further down the page: Accora's "goes beyond the **numbers**" in yellow, and our "is *always free.*" in gold italic.
- Crop: `baseline-1` (Accora, Auditly, ours stacked: the same formula three times).

### 2. The section formula
Each section has a **centred H2 of 40–56px**, then a **centred grey 1–2 line subhead**, then a **3-up or 3×2 card grid**
in a 1120–1280px container. Each card has an icon at the top left, a 20–24px title, two lines of text and "Learn more". Ashworth's
six teal cards even print each title twice, which is template residue. Our own "Three pillars" uses the same grid,
with a 32px gold dash in place of the icon.
- Crop: `baseline-4` (Ashworth teal service cards over our three pillars).

### 3. The number trio
**Three big numbers with "+" suffixes and a small grey label underneath** count up on scroll:
- "10+ Years / 150+ / 1,000+" (Ashworth)
- "$50M+ / 120+ / 98%" on a pastel green panel with 40px radius (Auditly)
- "15+ years / 500+ businesses" (Accora)
- "12 / 137 / 18" (ours; the phone capture shows 136 and 17 because it caught the count mid-way)

None of these can be checked, and the count-up animation is the same everywhere.
- Crop: `baseline-2`.

### 4. Fake or placeholder proof
- **Logo strips of invented companies**: PIONEER Construction, MONTERRA Home Goods, Evergreen Landscapes, NORTHFIELD Coffee Co.
  (Ashworth), and AlphaWave, Codecraft, Boltshift (Accora). Ours shows "CLIENT NAME" five times.
- A **Google star chip** in the hero.
- **Testimonials signed with a first name and initial** ("Andrea T., Startup Founder at SpotX"), shown as 3 or 6 equal cards
  or one card with a stock headshot and a "40%" stat.

### 5. Stock and fake-UI imagery
- **Smiling, diverse professionals at a laptop**: Accora, Auditly, EY.
- **Cut-out portraits on flat colour** inside a 40px-radius frame: Auditly's green hero and yellow CTA.
- **Floating fake dashboard widgets** pasted on photos: "Revenue Growth $2.4M ↑18%" and a bar-chart card (Accora).
  Ashworth uses a **tilted greyscale dashboard collage**; Accura a **phone in a hand with a neon-green glow**.
- **AI-made still lifes of calculator, coffee and paperwork** for blog thumbnails (Ashworth).
- The Big-4 versions are **abstract purple and blue 3D glass and "data" renders** and **network globes** (KPMG), and a sunset
  metaphor and award-night photos (EY).
- The Thai SME version is **Facebook-ad banners with the text baked into the image** (SA Accounting).
- Ours has **no images at all**, only two blurred colour blobs in the hero corners.
- Crops: `baseline-3` (Accora's fake widgets), `baseline-8` (Ashworth's dashboard collage, Accura's phone-in-hand),
  `baseline-7` (KPMG and EY hero renders), `baseline-6` (SA Accounting banner).

### 6. Rounded everything
- **Pill buttons** (radius = half the height, 40–56px tall) everywhere, including KPMG's blue pills for its service list.
- **Cards and panels with 12–40px radius**, soft drop shadows, and in Ashworth's case neumorphic grey tiles.
- Full-width panels are inset 80px with 40px corners.
- EY and our site are the exceptions, with small-radius rectangles.

### 7. One neutral ground plus one loud accent, and gradient "atmosphere"
- **The pairs.** Cream #F8F3ED + yellow #FFE502 (Accora). Grey #EDEDED + green #017931 + yellow #E9AD0F (Auditly). White +
  teal #3C7880 (Ashworth). Black + neon green (Accura). KPMG purple-blue, EY yellow on charcoal, SA all-orange. Ours: cream
  #FDFAF3 + navy + gold.
- **Dark and light bands alternate** down the page.
- **Gradient atmosphere:** blurred blobs (ours), radial glow (Accura) and a warm orange gradient CTA (Accora).

### 8. The fixed section order
Nav (logo left, 4 links, pill CTA right) → hero → logo strip → numbers → services → "why us" checklist → industries →
testimonials → pricing (3 tiers, middle one highlighted) → FAQ accordion of five "+" rows → **"Ready to …?" CTA band** → 4-column dark
footer with round social icons.
- Ours runs in the same order without pricing or FAQ: hero → pillars → client-name strip → insights → about → numbers → centred quote →
  contact → navy footer.
- Crop: `baseline-5` (Auditly's FAQ beside its "Ready To Start?" card).

### 9. The motion kit
- **Lenis smooth scroll** on every Framer template.
- **Fade or blur-up word reveals**: Accora was caught mid-blur on "smarter decisions".
- **Cards that stack and fan on scroll** (Accora, crop `baseline-9`).
- **Count-up numbers** and **logo marquees**.
- **Carousels with arrows, dots and a pause button** (EY, KPMG).
- **A "SCROLL" cue with a short line** (ours, Tilleke).

Nothing moves in a way that carries meaning. It is all entrance decoration.

### 10. Generic copy
- **The same vocabulary everywhere:** *clarity, confidence, numbers, decisions, growth, forward*.
- **Title Case Every Word** (Auditly: "We Take Care Of Your Books — So You Can Focus On Growth").
- **Stock section names:** "Why Choose Accora", "What Clients Say", "Frequently Asked Questions", "Ready to get your finances under
  control?", "Trusted by businesses like yours", "Everything your business needs".
- **SaaS phrases on a firm's site:** "No credit card required" (Accura), "Get Started".
- **No names, no licence numbers, no named partners.** Only Auditly ($199 / $399 / $699 a month) and SA Accounting (2,500 THB a month)
  publish fees.

**Type habits across all of them:** one display face plus one grotesk, with 3–4 sizes and a display-to-body ratio of about 4–5 : 1.
The display face is either a soft serif at regular weight with tight tracking (Hedvig, Playfair Bold, Instrument Serif) or a heavy
geometric grotesk (Apfel Grotezk, Inter 500). Body text is Inter, Geist or Manrope at 14–18px. Ashworth sets its body at roughly
1.0 line-height, which is too tight to read comfortably.

**Template residue on show:** a "Made in Framer" badge and "Get for free" button on every Framer frame; "Edit template" in Auditly's
nav; "Ledger & Laurel" left in an Ashworth testimonial; Accura's desktop nav squeezed beside its logo on phone and cut off at the right edge.

---

## 2. What is genuinely good in them

- **Auditly: published prices and a real-objections FAQ.** Three monthly tiers with what each includes, and questions like "Can you
  replace my current accountant?" and "Is my data secure?". For an accounting buyer, a stated fee is persuasive. The direct phone
  number in the nav is also right for this market.
- **Accora: disciplined colour and a good process strip.** One serif at 68px with correct optical spacing on a warm cream ground,
  and a single accent (yellow #FFE502) used with discipline. The process strip in the phone frames (Discover · Plan · Execute · Support,
  with thin bar ticks) is compact and readable.
- **EY: an audience router.** "Explore insights and services for your C-suite role" offers a grid of boxed chips (CISO, CMO, CTO, CRO,
  Tax leader, GCO, Board executive, CSO…) and organises content by *who is reading*. It also features a Thailand-specific publication
  ("Thailand International and Corporate Tax Snapshots 2026"), which is real local substance.
- **KPMG: dated, local insight cards.** "TFRS 17 first reporting insights", "ASPAC Pillar Two", "M&A Trends in Thailand Q2/2026"
  carry a coloured title bar and a date. "Request for proposal" is a first-class action.
- **SA Accounting: what Thai SME buyers look for.** Its taste is rough (orange banners, text inside images, centred Thai paragraphs, a
  cookie bar over everything), but it shows exactly what this market wants to see:
  - prices up front (2,500 THB a month for bookkeeping, 8,000 THB for company registration)
  - the founder's credential (ex-Revenue Department auditor, 17 years)
  - phone and LINE ID in the hero
  - a decent loopless Thai webfont (Prompt) at 16px / 1.5
- **Ours:**
  - Restraint: no stock photos, fake dashboards or invented logos.
  - Copy with a specific voice ("Twelve months in, our Thai entity runs the way our London office does").
  - A contact block set as labelled rows with hairlines (EMAIL / PHONE / OFFICE / HOURS).
  - A gold reading-progress bar, a consistent small type scale, and a phone layout that simply works.

---

## 3. Our own site, frankly

**Against the paid templates: on par for finish, calmer, and better written, but thinner.**
- It has no template residue, no fake widgets and better copy than all four.
- But it has **no visual material at all**: zero images, no proof assets, and placeholders ("Your Firm Name", "CLIENT NAME" ×5) that
  make it read as unfinished.
- Its **structure is the same formula** as the templates (patterns 1, 2, 3, 8 above). The gold italic accent word is the same device as
  Accora's yellow "numbers" and Auditly's green "Numbers." The hero's blurred corner blobs are the stock-gradient habit.

**Against top work (Capella, Rosewood, Cadson Demak in the Thai group): about two steps below.** It has the restraint but not the system
or the material.
1. **No grid tension.** Everything is centred or sits in the left two-thirds, so the right ~35% of a 1440 screen is empty in several
   sections. For example, the numbers float right of an empty left half, and "All articles" hangs alone at the far right.
2. **Body text is small** (~14px on desktop), and there is **one visual voice** throughout.
3. **No signature device:** no image system, no numbering, no captions, and no rule system beyond 32px gold dashes.

**Readiness for Thai and Chinese: weak.**
- Instrument Serif is a very condensed Latin face with no Thai or Chinese partner of similar width. The stack falls back to Noto Serif
  Thai and Noto Serif TC/JP, which will look far wider and heavier.
- The italic accent and the tracked-caps eyebrows have no Thai or Chinese equivalent.

This palette and font pairing are retired in CLAUDE.md anyway.

**Where it stands:** at the top of the "good template" band. Its taste is better than the $20–129 templates, but it is built from the
same parts in the same order. A buyer would not see anything they could not get from a template.

---

## 4. Crops

| id | shows |
|---|---|
| baseline-1 | The hero formula three times: Accora, Auditly, ours (eyebrow, 2-line headline, accent word, pill or ghost CTAs) |
| baseline-2 | Number trios: Ashworth (with invented logo strip), Auditly green panel, ours |
| baseline-3 | Fake UI widgets on stock photos (Accora "Revenue Growth $2.4M", bar-chart card) |
| baseline-4 | 3-up service cards: Ashworth teal with duplicated titles; our three pillars with gold dash |
| baseline-5 | FAQ accordion + "Ready To Start?" CTA card (Auditly) |
| baseline-6 | Thai SME hero: text baked into an orange banner image (SA Accounting) |
| baseline-7 | Big-4 heroes: KPMG abstract purple glass render; EY carousel hero |
| baseline-8 | "Numbers" imagery: Ashworth tilted greyscale dashboard collage; Accura phone-in-hand with neon glow |
| baseline-9 | Accora stat cards stacking and fanning on scroll (two consecutive frames) |
