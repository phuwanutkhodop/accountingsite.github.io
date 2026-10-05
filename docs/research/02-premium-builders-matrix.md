# 02 — Premium Builders: Feature & UX Inventory

**Ticket:** GitHub issue #2 (Wayfinder research)
**Date:** 2026-10-05
**Scope:** Elementor Pro · Divi 5 · Bricks · Webflow · Squarespace (Fluid Engine) · Wix Studio · Framer
**Purpose:** Inventory what commercial-grade builders do across 11 capability areas, what professionals praise and criticize, and what that implies for our browser-only, GitHub-Pages-publishing builder with curated sections, a growing Design Library, and a trilingual (EN/TH/ZH) site with a Thai-first admin.

---

## 0. Method and evidence note (read this first)

- Research was done with web search. Every factual claim below carries a URL. Where a claim is about a vendor's documented behaviour, the URL is either the vendor's own help/blog page or a specialist agency write-up of that page.
- **Limitation:** from this research environment, vendor help centres (Squarespace, Webflow, Framer, Wix, Elegant Themes, Bricks Academy, Elementor) and most review sites could not be opened directly; the network policy blocked page fetches. The claims therefore rest on search-engine summaries of those pages, cross-checked across multiple independent sources where possible. Items that rest on general product knowledge rather than a retrieved source are marked **[verify]** and should be confirmed in a follow-up ticket before being treated as a hard design input.
- Coverage is deepest for Squarespace, Webflow, Framer and Wix Studio (10+ sources each) and thinner for Divi 5, Bricks and Elementor (2–3 sources each), which is acceptable because those three are WordPress plugins and are the least similar to our no-server model.

---

## 1. สรุปสำหรับเจ้าของกิจการ (ภาษาไทย, 10 บรรทัด)

1. เราสำรวจเครื่องมือสร้างเว็บระดับพรีเมียม 7 ตัว เพื่อดูว่า "ของดี" ที่มืออาชีพชอบคืออะไร และอะไรที่คนบ่นซ้ำ ๆ
2. สิ่งที่ทุกตัวมีเหมือนกัน: หน้าเว็บประกอบจาก "ส่วน" (section) ที่เลือกจากคลังพร้อมภาพตัวอย่าง แล้วแก้ข้อความ/รูปได้ โดยไม่ต้องจัดวางเองตั้งแต่ศูนย์
3. สิ่งที่ทำให้เว็บดู "แพง" คือ ระบบสี/ฟอนต์กลาง: เลือกชุดสี 5 สีกับคู่ฟอนต์ 1 ชุด แล้วทั้งเว็บเปลี่ยนตามอัตโนมัติ (Squarespace ทำแบบนี้ได้ดีที่สุดสำหรับคนไม่ใช่ช่าง)
4. สิ่งที่คนบ่นมากที่สุดคือ "แก้แล้วขึ้นเว็บจริงทันที ย้อนกลับไม่ได้" — Squarespace ไม่มีประวัติเวอร์ชันของทั้งเว็บ ขณะที่ Webflow/Framer/Wix มี และมี "ดูก่อนเผยแพร่"
5. เครื่องมือที่ให้อิสระสูง (ลากวางได้ทุกพิกเซล) ทำให้มือใหม่งง มือถือเพี้ยน และต้องแก้สองรอบ — ตรงกับที่เราตัดสินใจไว้แล้วว่าจะไม่ทำแบบนั้น
6. เรื่องหลายภาษา: ทุกตัวที่ทำได้ดีใช้ URL แบบ /th/ /en/ /zh/ แยกกัน มีปุ่มสลับภาษา มีมุมมอง "ต้นฉบับ–คำแปล" เคียงกัน และบอกได้ว่าหน้าไหนยังแปลไม่ครบ
7. SEO ที่จำเป็นมีแค่ไม่กี่อย่าง: ชื่อหน้า/คำอธิบายพร้อมตัวอย่างว่าจะโชว์ใน Google อย่างไร, รูปตอนแชร์ลง Facebook/LINE, ซ่อนหน้าจาก Google, และ redirect เมื่อเปลี่ยนที่อยู่หน้า
8. การเผยแพร่ที่ดีคือ ปุ่มเดียว แสดง "มีอะไรเปลี่ยน" ก่อนกดยืนยัน และย้อนกลับได้ — Framer และ Webflow ทำได้ดี Squarespace ไม่มี
9. การเริ่มต้นใช้งานที่ดี (Squarespace Blueprint) ถามแค่ 5 อย่าง: ชื่อกิจการ → บุคลิกแบรนด์ → เลือกส่วนหน้าแรก → เลือกหน้า → เลือกชุดสีและฟอนต์ แล้วได้เว็บเกือบเสร็จ
10. ข้อเสนอ: เราควรเอาแบบ Squarespace (ส่วนสำเร็จรูป + สีฟอนต์กลาง + เริ่มต้น 5 ขั้น) แต่เติมสิ่งที่ Squarespace ขาดคือ ประวัติเวอร์ชัน, ดูก่อนเผยแพร่, และหลายภาษาในตัว — ซึ่งทำได้ง่ายเพราะเราเก็บทุกอย่างใน GitHub อยู่แล้ว

---

## 2. Capability matrix

Legend: ●● strong / best-in-class · ● present, adequate · ◐ partial or add-on · ○ weak or absent · [v] = verify

| Capability area | Elementor Pro | Divi 5 | Bricks | Webflow | Squarespace 7.1 / Fluid Engine | Wix Studio | Framer |
|---|---|---|---|---|---|---|---|
| **Editing model** | Free-form widgets in containers, on-canvas | Free-form modules, infinite nesting, flex/grid | Class-based, structure panel, developer-first | Free canvas + CSS classes, Flexbox/Grid, components | **Curated sections** stacked vertically; blocks on a 24-col grid inside sections | Sections + responsive canvas, grids, breakpoints | Figma-like free canvas, stacks, breakpoints |
| **Design-system controls** | Global Colors + Global Fonts in Site Settings ● | Design Variables + Option Group Presets ●● | Global classes + CSS variables ●● (pro) | Variables with collections + modes, Components with variants ●● | 5-colour palette → 10 auto section themes; Font Packs ●● (for non-tech) | Site Styles: 6 text styles, categorised palette, max 25 colours ● | Color Styles (light/dark), Text Styles with breakpoints ● |
| **Template / kit library & growth** | Website Kits library, full-kit import ●● | Layout library (2,000+ layouts), Divi Cloud [v] ● | Remote/community templates, fewer prebuilt ◐ | Marketplace, Shared Libraries, Relume (1,000+ sections) ●● | Section picker + Saved Sections (250/account) + Site Themes ● | Sections/Wireframes picker, Saved Assets, design libraries across sites, AI Creator ●● | Marketplace plugins with 500–1,000+ sections, Remix templates ● |
| **Site structure (pages, menus, redirects)** | WP pages/menus; redirects via plugin ◐ | WP ◐ | WP ◐ | Pages panel, folders, 301 redirects with wildcards ●● | Pages panel: Main Nav / Footer Nav / Not Linked; URL Mappings (≈2,500 lines) ● | Pages & menus; URL Redirect Manager with group redirects ● | Pages panel; Redirects with wildcards, drag-to-prioritise (paid) ● |
| **Multilingual** | Plugin (WPML/Polylang/TranslatePress) ◐ | Plugin ◐ | Plugin ◐ | Native Localization: /xx/ subdirectories, hreflang, MT, localized slugs (Advanced), $9–29/locale/mo ●● | **No native** — Weglot or duplicate pages ○ | Wix Multilingual: duplicate pages per language, side-by-side dashboard, hreflang, 3,000 free MT words ● | Native: list-view Localization panel, AI translate, localized paths; $20/extra locale ● |
| **Media library** | WP Media Library ● | WP ● | WP ● | Assets panel: folders, alt text at asset level, 4 MB image cap ●● | Asset Library: folders, bulk upload, no alt-text prompt on upload ◐ | Media Manager: folders, filters, image editor; alt text only in editor, not in manager ◐ | Assets panel (styles + media) ● |
| **SEO tooling** | Via Yoast/Rank Math ◐ | Via plugin ◐ | Via plugin ◐ | Per-page title/description with preview, OG fields, sitemap toggle ●● | Per-page SEO tab, "Hide page from search results", per-page social image, auto sitemap ● | Default meta patterns, SEO panel, "Let search engines index" toggle, nofollow in Advanced ●● | Page Settings → SEO: title, description, social image, slug; auto sitemap/robots/canonical ● |
| **Drafts / versioning / backups** | WP revisions + Save Draft ● | WP revisions ● | WP revisions ● | Auto backup every 50th autosave, named manual backup (⇧⌘S), preview + restore ●● | **No site-level version history**; Ctrl+Z only within session ○ | Site History: every save/publish, who/when, restore; Release Candidate filter ●● | Version History: 5-min snapshots (4 h), hourly (24 h), daily after; copy elements from old version ● |
| **Preview** | Responsive preview + "Preview changes" | Responsive views | Responsive views | Staging site on webflow.io + Edit mode | Device toggle in editor; private/password site | Preview mode; test site / release candidate | Preview button; Staging tab (Pro) |
| **Publishing flow** | Publish / Update per page; maintenance mode [v] | Per page (WP) | Per page (WP) | Designer → Staging → Production with **publish summary of changes** ●● | **Edits go live immediately**; only Private/Password workaround ○ | Save vs Publish; Site History ● | Publish button lists changed pages/components/CMS items + who changed; Staging & "Deploy Latest" ●● |
| **Onboarding** | Kit chooser; setup wizard [v] ● | Quick Sites / AI starter [v] ● | None (dev tool) ○ | Template or blank; steep curve ◐ | **Blueprint AI: 5 steps** (name/personality → homepage sections → pages → palette → fonts) ●● | Template or AI; responsive AI ● | Blank canvas + Wireframer AI prompt or preset ● |
| **Client-safe editing mode** | Role Manager (content-only) [v] ◐ | ◐ | ○ | Edit mode (replacing legacy Editor; retiring Aug 2026) ● | Single mode; contributor roles ◐ | "Edit Content" mode: text/images only, design locked; permissions per page ●● | CMS editing; no granular roles ○ |

---

## 3. Per-area deep dive

### 3.1 Page / section editing model

**What the best do**

- **Squarespace 7.1 (Fluid Engine).** Pages are a vertical stack of sections. Clicking "Add Section" opens a picker of pre-designed sections by intent (e.g. about, gallery, form, footer); users can also save any section with a heart icon and re-insert it from a "Saved" tab. Inside a section, blocks sit on a grid and can be freely positioned; the editor is grid-based and needs almost no code. Sources: [SQSPThemes](https://www.sqspthemes.com/blog/squarespace-fluid-engine), [Beyondspace on saved sections](https://beyondspace.studio/blog/squarespace-saved-sections-new-account-wide-feature), [Ecommerce-Platforms Fluid Engine review](https://ecommerce-platforms.com/articles/squarespace-fluid-engine-review).
- Squarespace's 2024–25 "Design Intelligence" adds a **Layout Switcher** (wand icon on a section) that swaps the arrangement of an existing section's content among curated layouts, and an **AI Writer** at any text cursor. Source: [ilovecreatives — What's new with Squarespace 2025](https://ilovecreatives.com/squarespace-online-course-resources-toolbox/whats-new-with-squarespace-2025).
- **Wix Studio.** "Add Elements → Sections/Wireframes → category" shows pre-designed and wireframe sections; an "AI Creator" entry generates a section from a prompt; any element or section can be right-clicked → "Save as Asset" into a library that is shared across all Studio sites in the account. Sources: [Wix support — adding and managing sections](https://support.wix.com/en/article/studio-editor-adding-and-managing-sections), [Wix support — saving and reusing design assets](https://support.wix.com/en/article/studio-editor-saving-and-reusing-design-assets), [Wix — AI sections](https://support.wix.com/en/article/wix-editor-generating-page-sections-with-ai).
- **Webflow.** True CSS-class editing on canvas with Flexbox/Grid controls; Components with Variants, Slots and property overrides; a separate Edit mode for marketers. Sources: [DXP Scorecard — Webflow](https://www.dxpscorecard.com/platform/webflow), [The CSS Agency — top Webflow features](https://www.thecssagency.com/blog/top-10-webflow-features).
- **Framer.** Figma-like canvas with stacks and breakpoints; publish from the same screen. Source: [Waida Studio — What is Framer](https://waidastudio.com/learn/framer).
- **Divi 5.** Nested modules with infinite nesting; every element is a flex/grid container; up to 7 custom breakpoints. Source: [Elegant Themes — Divi 5 exclusive features](https://www.elegantthemes.com/blog/divi-resources/divi-5-exclusive-features-so-far).
- **Bricks.** Class-based styling with a structure panel; "you're expected to build layouts, not assemble pre-made pieces". Source: [FatLab — Bricks review](https://fatlabwebsupport.com/blog/wordpress-development/bricks-builder-review/).

**Praised**

- Section-stacked editing is consistently called the easiest for beginners; Squarespace reviewers credit it with "fewer cookie-cutter websites" while needing almost no code ([Ecommerce-Platforms](https://ecommerce-platforms.com/articles/squarespace-fluid-engine-review)).
- Bricks professionals report ~40% faster builds once they have an internal library of header/footer/hero variants re-skinned via variables ([FatLab](https://fatlabwebsupport.com/blog/wordpress-development/bricks-builder-review/)).

**Criticized**

- Free positioning breaks mobile: Fluid Engine "requires users to go to the mobile editor to readjust text and images, resulting in a lot of extra work having to tweak each section" and some designers "would not recommend it and won't be using it for client websites" ([Ecommerce-Platforms](https://ecommerce-platforms.com/articles/squarespace-fluid-engine-review), [Squarespace Forum — "Fluid engine is trash"](https://forum.squarespace.com/topic/224619-fluid-engine-is-trash/), [Jessica Miller — When to use Fluid Engine](https://www.jessicamiller.work/blog/squarespace-fluid-engine)).
- Too many options overwhelm beginners ([Ecommerce-Platforms](https://ecommerce-platforms.com/articles/squarespace-fluid-engine-review)).
- Wix Studio editor reported as "horrendously slow", with selection boxes offset from content and an undo that "doesn't work" ([Wix Studio forum](https://forum.wixstudio.com/t/my-wix-studio-is-extremely-slow-and-laggy-despite-powerful-hardware/65844), [r/WIX](https://redlib.hbubli.cc/r/WIX/comments/1gru769/wix_studio_is_poorly_optimized)).
- Webflow and Framer have steep learning curves for non-developers ([G2 Webflow reviews](https://g2.com/products/webflow/reviews), [Experte — Framer review](https://www.experte.com/website-builder/framer)).
- Divi 5's redesigned panels make "the first few weeks feel slower" for existing users ([Ravenous Raven — Divi 5 review](https://ravenousravendesign.com/wordpress/divi-theme/divi-5-review-expert/)).

### 3.2 Design-system controls (tokens, global styles, colours, typography)

**What the best do**

- **Squarespace** is the reference for non-technical owners. Site Styles → Colors: pick **5 palette colours** via "Designer Palette", "From Image", "From Color" or "Custom"; Squarespace auto-generates **10 section themes** (Lightest 1/2, Light 1/2, Bright, Dark 1/2, Darkest 1/2 and so on) and applies darker colours to links/buttons on light backgrounds using built-in contrast rules; each section picks one theme, so pages alternate light/dark bands yet stay cohesive. Fonts: pick a **Font Pack** (curated pairing) with "Switch", then Heading / Paragraph / Button / Miscellaneous groups, and "Assign Styles" under Global Text Styles. Changes are site-wide. Sources: [Paige Brunton — style editor PT1](https://www.paigebrunton.com/blog/customize-squarespace-style-editor), [PT2](https://www.paigebrunton.com/blog/squarespace-site-styles-editor), [SEOSpace — fonts](https://www.seospace.co/blog/change-fonts-and-styles-squarespace).
- **Webflow Variables**: colour, size, font-family, number/percentage; grouped in **collections** with **modes** (e.g. light/dark); bound by clicking the purple dot on a swatch or size field; function like CSS custom properties. **Shared Libraries** push components, variables, variable modes and assets to every site in a Workspace. Sources: [Webflow — variables](https://webflow.com/webflow-way/design-systems/variables), [Digidop — variables guide](https://digidop.com/blog/webflow-variables-guide), [Webflow — Shared Libraries](https://webflow.com/blog/shared-libraries), [Webflow update — assets & variable modes in libraries](https://webflow.com/updates/shared-library-assets-and-variable-modes).
- **Framer**: Color Styles with a light and an optional dark value; Text Styles with breakpoint overrides; both live in the Assets panel and propagate through components and effects. Sources: [Framer Academy — light/dark](https://Framer.com/academy/lessons/light-dark-mode), [Framer — light and dark mode update](https://www.framer.com/updates/light-and-dark-mode), [Framer developers — styles](https://www.framer.com/developers/styles).
- **Wix Studio** Site Styles: six text styles (H1–H3 + 3 paragraph), a categorised palette, max 25 site colours; changing a colour instantly updates every element using it. Limitation: covers only colour and typography, not spacing or layout. Sources: [Wix — site colors](https://support.wix.com/en/article/studio-editor-working-with-site-colors), [Temperstack — Wix themes](https://www.temperstack.com/learn/wix/customize-colors-fonts-themes/).
- **Divi 5**: Design Variables (colours, fonts, spacing, text) defined once and reused; **Option Group Presets** apply across any element type whereas Element Presets are per module. Source: [Elegant Themes — Divi 5 features](https://www.elegantthemes.com/blog/divi-resources/divi-5-exclusive-features-so-far), [WP Marmite — Divi 5](https://wpmarmite.com/en/divi-5/).
- **Elementor Pro**: Global Colors and Global Fonts in Site Settings; importing a kit "deploys the global colors, fonts, and Theme Builder templates at once". Source: [Dreamgrow — Elementor review](https://www.dreamgrow.com/elementor-review/), [Pixelnet — Elementor Pro review](https://www.pixelnet.in/blog/honest-elementor-pro-review/).
- **Bricks**: global classes + CSS variables; Editor V4 adds a class-based styling system. Sources: [Crocoblock — Bricks review](https://crocoblock.com/blog/wordpress-bricks-builder-review/), [WPTuts — global classes](https://wptuts.co.uk/mastering-bricks-builder-global-classes-for-beginners/).

**Praised**: palette-plus-auto-themes (Squarespace) for owners; variables with modes (Webflow) and class/variable systems (Bricks) for professionals; kit import that sets colours and fonts in one step (Elementor).

**Criticized**: Elementor global-font override friction ("have to modify the unit dropdown before getting what they want") and un-deletable global widgets ([Yahoo Tech — Elementor review](https://tech.yahoo.com/apps/articles/elementor-website-builder-review-022722440.html)); Wix Site Styles not covering spacing ([Temperstack](https://www.temperstack.com/learn/wix/customize-colors-fonts-themes/)); Divi 5 presets "lock you into styling a particular element" unless you use Option Group Presets ([Elegant Themes](https://www.elegantthemes.com/blog/divi-resources/divi-5-exclusive-features-so-far)).

### 3.3 Template / kit libraries and how they grow

- **Squarespace**: Saved Sections — heart icon on a section, "Saved" tab in the picker; limit raised from 50 per site to **250 per account**; saved sections are **static snapshots** (editing one does not update others) and **inherit the destination site's styles**. "Site Themes" let owners mix curated palettes, font pairs and button styles. Sources: [Beyondspace](https://beyondspace.studio/blog/squarespace-saved-sections-new-account-wide-feature), [LaunchHappy — 2023 updates](https://launchhappy.co/guides/new-squarespace-updates-2023), [ilovecreatives](https://ilovecreatives.com/squarespace-online-course-resources-toolbox/whats-new-with-squarespace-2025).
- **Wix Studio**: Saved Assets per site plus account-level design libraries; sections picker with categories and wireframes. Source: [Wix support](https://support.wix.com/en/article/studio-editor-saving-and-reusing-design-assets).
- **Webflow**: Marketplace templates; Shared Libraries (1 library on Core/Growth/Freelancer, unlimited on Agency/Enterprise); Relume's 1,000+ components with semantic HTML and breakpoints pasted into projects, browsed by category. Sources: [Webflow — Shared Libraries](https://webflow.com/feature/shared-libraries), [Webflow × Relume](https://webflow.com/integrations/relume), [Supersparks — component libraries](https://supersparks.io/blog/best-webflow-components-libraries).
- **Framer**: marketplace plugins (Framestudio, Clonify 1,000+, FramerKit 500+ sections, Framify 620+) organised by Navbar/Hero/Features/Pricing/FAQ/CTA/Footer; preview cards insert as linked Components or editable Layers. Source: [Framer marketplace — Framestudio](https://www.framer.com/marketplace/plugins/framestudio/), [FramerKit](https://marketplace.framer.com/marketplace/plugins/framerkit), [Framify](https://framer.com/marketplace/plugins/framify).
- **Elementor**: Website Kits library — full-kit import sets globals and Theme Builder templates at once ([Dreamgrow](https://www.dreamgrow.com/elementor-review/)).
- **Divi**: layout library of pre-made layouts; Divi Cloud for cross-site storage **[verify: exact counts]** ([WP Marmite](https://wpmarmite.com/en/divi-5/)).
- **Bricks**: fewer templates than Elementor/Divi; remote/community templates and third-party design sets ([FatLab](https://fatlabwebsupport.com/blog/wordpress-development/bricks-builder-review/)).

**Praised**: libraries organised **by intent** (Hero, Features, FAQ, CTA) with live preview cards; account-wide reuse; inheriting the destination's style tokens so a saved section never clashes.
**Criticized**: snapshot-only saved sections (no "update everywhere") in Squarespace; Bricks' thin library.

### 3.4 Site structure: pages, menus, redirects

- **Squarespace** Pages panel has three zones — **Main Navigation, Footer Navigation, Not Linked**; drag to reorder; drag into a Folder for a one-level dropdown; drag to Not Linked to keep a page live but off the menu. Only one nesting level. Sources: [SEOSpace — dropdown menu](https://www.seospace.co/squarespace-faqs/drop-down-menu-in-squarespace), [Whatsquare — navigation](https://whatsquare.space/blog/how-to-edit-navigation-bar-in-squarespace). Redirects: Settings → Advanced → **URL Mappings**, one line per rule `/old -> /new 301` (301/302/404), field limit ≈400 KB (~2,500 lines), external targets allowed. Sources: [Collaborada — redirects](https://www.collaborada.com/blog/squarespace-redirects), [Sparkplugin](https://www.sparkplugin.com/blog/squarespace-redirect).
- **Webflow** Site settings → Publishing → 301 redirects; wildcard capture `(.*)` → `%1`; no hard cap but ≤1,000 recommended because rules ship in manifest.json. Sources: [Webflow help — redirects](https://help.webflow.com/hc/en-us/articles/33961294898835), [Brix — wildcard redirects](https://brixtemplates.com/blog/how-to-use-wildcard-redirects-in-webflow-step-by-step-guide-with-examples), [Webflow forum — limits](https://discourse.webflow.com/t/are-there-any-numerical-limits-for-301-redirects-in-the-webflow-project-settings/102888).
- **Framer** Site Settings → Redirects; `*` wildcards and `:1`, `:2` capture references; 301 by default; drag to reorder priority; paid plans only. Sources: [Framer help — redirects](https://framer.com/help/articles/how-to-setup-redirects-to-maintain-seo-ranking), [Brix — Framer wildcards](https://brixtemplates.com/blog/how-to-set-up-wildcard-redirects-in-framer-sites).
- **Wix** URL Redirect Manager: single or grouped (same path) 301s ([Wix SEO guide](https://wix.com/seo/learn/wix-seo-guide)).
- WordPress builders rely on WP menus and redirect plugins **[verify per plugin]**.

**Praised**: Squarespace's three-zone page list is the most legible mental model for owners. **Criticized**: Squarespace's single nesting level; Webflow's redirect payload growing with rule count.

### 3.5 Multilingual handling

- **Webflow Localization** (native since late 2024): primary + secondary locales served at `/es/`, `/de/` (customisable slug); localizes static pages, CMS, assets (Advanced), styles, SEO; built-in machine translation as a starting point; automatic hreflang and localized sitemaps; **slug translation only on Advanced**; pricing **$9/locale/month (Essential, ≤3 locales) or $29/locale/month (Advanced)**. Sources: [Flow Ninja](https://www.flowninja.com/blog/webflow-localization), [Lowcode Agency](https://www.lowcode.agency/blog/webflow-localization-and-multi-language-what-to-know), [Pravin Kumar — multilingual SEO 2026](https://www.pravinkumar.co/blog/multilingual-webflow-site-localization-seo-2026), [we-r — Webflow Localize prices](https://www.we-r.co/en/toolbox-equipe-marketing/webflow-localize-cest-quoi).
- **Framer**: Localization panel in **list view** or edit on canvas; AI translation with model choice (Auto by default) using workspace credits; "Translate all"; **localized page paths** for any page (e.g. `/de/blog/hallo-welt`); plan caps (2 locales Basic, 10 Pro, 20 Scale) and about **$20 per additional locale/month**. Sources: [Framer help — auto translate](https://www.framer.com/ja/help/articles/auto-translate-for-localization/), [Framer update — localized page paths](https://www.framer.com/updates/localized-page-paths), [Framer update — translate all](https://www.framer.com/updates/translate-all), [Costbench — Framer hidden costs](https://www.costbench.com/software/design/framer-design/hidden-costs/). Earlier criticism that URLs could not be translated is now out of date ([Experte](https://www.experte.com/website-builder/framer) vs the localized-paths update).
- **Wix Multilingual**: duplicates each page per language; translate **in context in the Editor** or **side-by-side in the Dashboard**; language menu; hreflang and language URLs; Google-Translate auto-translate with 3,000 free words; 180+ languages. Sources: [Wix App Market](https://www.wix.com/app-market/web-solution/wix-multilingual), [Wix Studio Academy](https://www.wix.com/studio/academy/tutorials/how-to-get-started-with-multilingual), [Intlayer — Wix i18n](https://intlayer.org/blog/i18n-technologies/CMS/wix).
- **Squarespace**: no native multilingual; recommended path is Weglot (subdomain per language, auto hreflang, switcher) or manual duplicate pages. Sources: [Weglot — Squarespace guide](https://weglot.dev/guides/squarespace-multilingual-site), [SQSPThemes — multilingual](https://www.sqspthemes.com/blog/how-to-create-a-multilingual-website-on-squarespace), [Collaborada — hreflang on Squarespace](https://www.collaborada.com/blog/squarespace-multilingual-sites).
- WordPress builders: WPML / Polylang / TranslatePress **[verify current compatibility]**.

**Praised**: subdirectory URLs, automatic hreflang, a dedicated translation list view with "untranslated" state, MT as a first draft. **Criticized**: per-locale pricing ("expensive, poor choice for multilingual sites" — [Experte](https://www.experte.com/website-builder/framer)); Framer's CMS "lacks proper roles and permissions" for multi-editor handoff ([Experte](https://www.experte.com/website-builder/framer)); Squarespace's total absence of native support.

### 3.6 Media library

- **Webflow Assets panel**: folders and nested folders; **alt text set on the asset** so it carries everywhere; 4 MB image cap; PNG/JPEG/GIF/SVG/WebP/AVIF. Sources: [Webflow help — assets](https://help.webflow.com/hc/en-us/articles/33961290329235), [Webflow University — image](https://university.webflow.com/lesson/image), [Momentic — Webflow image optimisation](https://momenticmarketing.com/blog/webflow-image-optimization).
- **Squarespace Asset Library**: bulk upload, folders/subfolders, but **no alt-text prompt on upload** (alt text is set per block) and no bulk download; 10 MB file cap, 250–10,000 px. Sources: [Collaborada — asset library](https://collaborada.com/blog/squarespace-asset-library), [Big Cat Creative — media library](https://www.bigcatcreative.com/blog/media-library-squarespace), [Nevada County Arts — asset library](https://www.nevadacountyarts.org/asset-library-best-practices).
- **Wix Media Manager**: folders, type filters, sort, built-in crop/filters/focal point; **alt text cannot be set in the manager** (a standing feature request). Sources: [Wix — alt text request](https://support.wix.com/en/article/wix-media-request-adding-alt-text-in-the-media-manager), [Wix dev — Media Manager](https://dev.wix.com/docs/overview/site-features-tools/media-manager).
- WordPress builders use the WP Media Library (alt text on attachment) **[general knowledge]**.

**Praised**: asset-level alt text and focal-point cropping. **Criticized**: alt text buried per-block (Squarespace, Wix); no bulk operations.

### 3.7 SEO tooling

- **Squarespace**: Pages → cog → **SEO tab**: SEO title, SEO description, **"Hide page from search results"**; **Social tab** for a per-page share image; auto sitemap. Sources: [Kickpoint — titles & descriptions](https://kickpoint.ca/how-to-change-title-tags-and-meta-descriptions-in-squarespace), [Big Cat Creative — SEO tricks](https://bigcatcreative.com/blog/squarespace-seo-tricks), [Website Builder Expert — Squarespace SEO](https://www.websitebuilderexpert.com/squarespace-seo-review/).
- **Webflow**: page settings with SEO title/description and a search preview widened to 300 characters, separate OG title/description/image, **"Exclude from sitemap"/sitemap indexing toggle**. Sources: [Webflow University — optimise page settings](https://university.webflow.com/course-lesson/optimize-page-settings-for-seo), [Rapid Developers — meta & OG](https://www.rapidevelopers.com/webflow-tutorial/how-to-set-meta-tags-and-open-graph-data-in-webflow-s-page-settings-for-better-seo-and-previews), [Webflow forum — 300-char preview](https://discourse.webflow.com/t/google-algorithm-update-now-accepting-300-char-meta-descriptions/54317/14).
- **Wix**: **default SEO patterns** (title = site name for home, canonical = page URL) auto-applied and overridable; SEO panel with **"Let search engines index this page"** toggle; Advanced tab with Robots Meta (nofollow). Sources: [Wix — default SEO settings](https://support.wix.com/en/article/default-seo-settings), [Wix — SEO panel](https://support.wix.com/en/article/customizing-your-seo-settings-in-the-seo-panel).
- **Framer**: Page Settings → SEO (title, description, social image, slug); auto sitemap.xml, robots.txt, canonical; global defaults overridable per page/CMS item. Sources: [Framer help — titles, descriptions, social images](https://framer.com/help/articles/how-to-update-page-titles-descriptions-and-social-images), [Stackmatix — Framer SEO](https://www.stackmatix.com/blog/framer-site-seo-startups).
- WordPress builders delegate to Yoast/Rank Math **[general knowledge]**.

**Praised**: sensible defaults with override (Wix), live search-result preview (Webflow), per-page share image (all). **Criticized**: Squarespace's thinner controls versus plugins ([LaunchHappy — SEO plugins](https://launchhappy.co/guides/achieve-seo-mastery-unlocking-the-potential-of-squarespace-plugins)).

### 3.8 Drafts, versioning, backups

- **Webflow**: automatic restore point every 50th autosave; manual named backup with ⇧⌘S / ⇧Ctrl S; Site settings → Backups with **eye icon to preview** and three-dots to restore/rename; current state saved before restore; unlimited on paid plans. Sources: [Webflow University — backups](https://university.webflow.com/lesson/backups), [Webflow update — preview/restore/rename backups](https://webflow.com/updates/preview-restore-and-rename-backups-from-the-designer).
- **Framer**: Version History (⇧⌘H): snapshots every 5 min for 4 h, hourly for 24 h, daily after; earlier versions are view-only — you **copy a section from an old version and paste it** into the current one, breakpoints included. Sources: [Framer help — revert](https://www.framer.com/help/articles/how-can-i-revert-to-a-previous-working-version-of-my-file/), [Framer update — version history](https://www.framer.com/updates/version-history-update), [Framer Academy](https://www.framer.com/academy/lessons/version-history).
- **Wix Studio**: Site History records every save/publish with who and when; restore reverts pages, code and permissions; filter "Release Candidate" to return to a test version. Sources: [Wix dev — about Site History](https://dev.wix.com/docs/develop-websites-sdk/publish-your-site/site-history/about-site-history), [Wix — viewing site history](https://support.wix.com/en/article/viewing-and-managing-your-site-history).
- **Squarespace**: **no site-level version history or undo**; Ctrl+Z works only inside the current editing session; section deletion is permanent; community advice is the Wayback Machine. Sources: [Elfsight — undo in Squarespace](https://elfsight.com/tutorials/how-to-undo-changes-in-squarespace/), [Whatsquare — original style](https://whatsquare.space/blog/how-do-i-go-back-to-my-site-s-original-style-), [Website Builder Insider — version history](https://www.websitebuilderinsider.com/does-squarespace-have-version-history/).
- WordPress builders: WP post revisions and "Save Draft" **[general knowledge]**.

**Praised**: named restore points, preview-before-restore, auto-snapshot cadence. **Criticized**: Squarespace's absence of history is the single most repeated complaint in owner-facing forums.

### 3.9 Preview

- Squarespace: device toggles in the editor; whole-site Private or Password mode is the only "preview before anyone sees it" ([Website Builder Insider — edit without going live](https://www.websitebuilderinsider.com/how-do-i-edit-my-squarespace-site-without-going-live/)).
- Webflow: staging site on `*.webflow.io` isolated from Designer changes ([Webflow — publishing workflows](https://webflow.com/blog/publishing-workflows)).
- Framer: Staging tab (Pro) and "Share for review" ([Framer dictionary — share for review](https://www.framer.com/dictionary/share-for-review), [Framer — staging and versions](https://www.framer.com/ja/help/articles/staging-and-versions/)).
- Wix Studio: preview mode plus test sites / Release Candidates ([Wix — test sites](https://wix.com/wix-lp/new-wixcode/forum/site-page-design/how-to-work-with-test-sites)).

### 3.10 Publishing flow

- **Webflow** (2025 "Publishing workflows"): three columns — **Designer** (last-modified timestamp, pre-publish summary of unpublished changes with who made them, publish to staging) → **Staging** (summary of what is on staging, publish to production) → **Production** (domains, last publish). Page Branching with approval requests and "request changes". Sources: [Webflow blog — publishing workflows](https://webflow.com/blog/publishing-workflows), [Webflow help — publishing workflow](https://help.webflow.com/hc/en-us/articles/33961266935187), [AirOps — review changes](https://airops.com/use-case-guides/webflow-review-changes-a-comprehensive-guide-to-publishing-updates).
- **Framer**: Publish button shows **a list of updated pages, components and CMS items below your domains, with the avatar of who changed each**; click an item to jump to it; "View Changes"; Staging tab then Production → "Deploy Latest"; rollback to any version. Sources: [Framer update — publishing changelog](https://www.framer.com/updates/publishing-changelog), [Framer — November 2024 update](https://framer.com/updates/november-update-2024), [Framer help — publishing](https://framer.com/help/articles/publishing-your-framer-website).
- **Squarespace**: no draft/live split — "once your website is live, any changes you make will be visible to the public immediately"; workarounds are duplicate the site, set it Private, or park pages in Not Linked ([Website Builder Insider](https://www.websitebuilderinsider.com/how-do-i-edit-my-squarespace-site-without-going-live/)).
- **Wix Studio**: Save vs Publish, Site History ([Wix dev](https://dev.wix.com/docs/develop-websites-sdk/publish-your-site/site-history/about-site-history)).
- WordPress builders: per-page Publish/Update; Elementor has maintenance/coming-soon mode **[verify]**.

**Praised**: "what changed and who" before the button; staging that mirrors production; one-click rollback. **Criticized**: immediate-live editing with no safety net (Squarespace).

### 3.11 Onboarding

- **Squarespace Blueprint AI** — five steps: (1) site name + **brand personality** (e.g. "professional", "bold") which drives all later suggestions; (2) build the homepage by picking sections and using "Change Layout"; (3) tick the pages you want; (4) choose from curated **palettes grouped by personality** (four per personality), live-previewed on the homepage; (5) choose a **font pairing** (two per personality, 14 total). Optional AI copy afterwards. Reviewers: "a professional-looking starting point in under 10 minutes, with more creative control than most AI website builders." Sources: [Sparkplugin — Blueprint AI](https://sparkplugin.com/blog/what-is-squarespace-blueprint-ai), [Website Builder Expert — Blueprint AI](https://www.websitebuilderexpert.com/website-builders/squarespace-blueprint-ai/), [Ecommerce-Platforms — Blueprint AI](https://ecommerce-platforms.com/articles/squarespace-blueprint-ai), [Feisworld — Blueprint review](https://www.feisworld.com/blog/squarespace-blueprint-ai-builder-review).
- **Framer**: blank desktop canvas → Insert → **Wireframer** prompt or preset; generates layout with all breakpoints; then "add a grid for project shots" style follow-ups ([Framer University — AI workflow](https://framer.university/blog/the-new-ai-workflow-for-building-websites)).
- **Wix Studio**: template or AI start; Responsive AI adapts desktop to tablet/mobile; "Smart sections" suggest layouts ([webdew — Wix Studio review](https://www.webdew.com/blog/wixstudio), [Wix Studio Academy — get started](https://www.wix.com/studio/academy/tutorials/how-to-get-started-in-the-wix-studio-editor)).
- **Elementor**: kit chooser as the first step ([Dreamgrow](https://www.dreamgrow.com/elementor-review/)); **Divi**: Quick Sites / AI starter **[verify]**; **Bricks**: none — a developer tool ([FatLab](https://fatlabwebsupport.com/blog/wordpress-development/bricks-builder-review/)).

**Praised**: a short, decision-light wizard whose early answer (personality) narrows every later choice; live preview while choosing palette/fonts. **Criticized**: AI-generated copy that must be rewritten; Webflow/Framer "overwhelming" first screens for non-developers ([G2](https://g2.com/products/webflow/reviews)).

### 3.12 Client-safe editing (cross-cutting)

- **Wix Studio** is the clearest: a client with only "Edit Content" sees a mode where they "can update text and images but can't modify your design"; agencies set **Permissions Per Page** including "Edit layout & design" on/off. Sources: [Wix Studio Academy — handover](https://www.wix.com/studio/academy/tutorials/how-to-handover-your-site-to-clients), [Wix — editing permissions per page](https://support.wix.com/en/article/studio-editor-editing-permissions-per-page).
- **Webflow Edit mode** replaces the legacy Editor (which lacked Localization, Assets and real-time collaboration); the legacy Editor retires 4 Aug 2026. Sources: [Webflow forum — Edit Mode vs legacy](https://discourse.webflow.com/t/edit-mode-vs-legacy-editor/329699), [Pravin Kumar — legacy editor retiring](https://www.pravinkumar.co/blog/webflow-legacy-editor-retiring-client-seats-2026).
- **Framer**: clients can edit CMS text "without breaking the design", but the CMS "lacks proper roles and permissions" ([Experte](https://www.experte.com/website-builder/framer)).
- Professionals describe Webflow as "a fantastic development tool for agencies and freelancers, but not for clients" ([GetApp Webflow reviews](https://www.getapp.com/website-builder-software/a/webflow/reviews/)).

---

## 4. Adopt / Adapt / Avoid — for our builder

### Adopt (copy the pattern closely)

| Pattern | Seen in | Why it fits us |
|---|---|---|
| **Section picker grouped by intent with live thumbnails**, plus a "Saved" tab | Squarespace, Wix Studio, Framer plugins | Matches the already-locked "curated sections" decision; intent grouping (Hero, Services, Team, Fees, FAQ, Contact) is how an accounting owner thinks. |
| **5-colour palette → auto-generated section themes with built-in contrast rules** | Squarespace | Lets a non-designer alternate light/dark bands safely. Our Navy + Soft Linen palette becomes the first preset; the Design Library grows by adding palettes. |
| **Font pairing presets (Font Packs)** rather than free font pickers | Squarespace Blueprint | Protects the locked Instrument Serif + Inter rule; future pairings are Design Library entries, not free choices. |
| **Five-step onboarding: name → personality → homepage sections → pages → palette/fonts**, live-previewed | Squarespace Blueprint | Short, decision-light, and each step narrows the next. Thai-first wording. |
| **Publish dialog that lists what changed and who changed it, then one button** | Framer, Webflow | Trivial for us: a git diff of content files is exactly this list. |
| **Named restore points with preview-before-restore** | Webflow backups, Wix Site History | Git history gives this for free; the UI must surface it as "versions", never as commits. |
| **Three-zone page list: Main menu / Footer menu / Not linked** with drag-to-reorder | Squarespace | Simplest mental model found; Not Linked doubles as our "draft page" state. |
| **Per-page SEO tab: title + description with live Google-style preview, share image, "hide from search" toggle; sensible defaults auto-filled** | Webflow, Wix, Squarespace | Covers 95% of a service firm's SEO needs with four fields. |
| **Alt text stored on the asset** so it travels with the image | Webflow | Avoids the Squarespace/Wix complaint of per-block alt text. |

### Adapt (take the idea, change the shape)

| Pattern | Seen in | Our adaptation |
|---|---|---|
| **Locale list view + on-canvas edit, MT first draft, untranslated indicators** | Framer, Webflow, Wix side-by-side | Build a side-by-side TH/EN/ZH translation table per section with "missing translation" badges and a fallback rule; no per-locale fees. Subdirectory URLs `/th/`, `/en/`, `/zh/` with hreflang generated at publish. |
| **Staging → Production** | Webflow, Framer | We have no staging server. Adapt as "Preview build" rendered in-browser from the working tree, with Publish = commit + push. A second GitHub Pages branch could serve as true staging — see open questions. |
| **Saved sections as snapshots that inherit the destination's styles** | Squarespace | Keep style inheritance, but add "linked preset" semantics so a Design Library update can offer "apply to all sections using this preset" (the thing Squarespace lacks). |
| **Variables with modes** | Webflow, Framer | Expose only two modes to the owner (Light theme / Dark band), hard-wired to the palette; never expose raw tokens. |
| **Client "Edit Content" mode vs design mode** | Wix Studio | Ship a single owner mode that is already content-only; a hidden "Design Library maintainer" mode for us. |
| **Layout Switcher (wand) on a section** | Squarespace Design Intelligence | Our bounded customization: each section type offers 2–4 layout variants; switching never changes content. |
| **Redirect manager with one-line rules** | Squarespace URL Mappings, Framer | GitHub Pages cannot do server redirects; adapt as generated meta-refresh/JS redirect pages plus a 404 page, with a simple "old path → new path" table. |
| **Default SEO patterns that auto-fill and can be overridden** | Wix | Patterns per language: `{Page} | {Firm name}` and description from the first paragraph of the page. |

### Avoid (deliberately not doing)

| Pattern | Seen in | Reason |
|---|---|---|
| Pixel-free positioning and separate mobile layouts | Squarespace Fluid Engine, Wix Studio, Framer | Consistently blamed for mobile breakage and double work ([Ecommerce-Platforms](https://ecommerce-platforms.com/articles/squarespace-fluid-engine-review), [Squarespace Forum](https://forum.squarespace.com/topic/224619-fluid-engine-is-trash/)). Already rejected. |
| Edits that go live immediately with no history | Squarespace | The most repeated owner complaint ([Elfsight](https://elfsight.com/tutorials/how-to-undo-changes-in-squarespace/)). |
| Class/variable panels exposed to the owner | Bricks, Webflow, Divi 5 presets | Professional power, but "larger learning curve for complete beginners" ([FatLab](https://fatlabwebsupport.com/blog/wordpress-development/bricks-builder-review/)). |
| Per-locale paywalls | Webflow ($9–29/locale/mo), Framer ($20/locale) | Trilingual is a requirement, not an upsell. |
| Global widgets that cannot be removed without unlinking | Elementor | Confusing failure mode ([Yahoo Tech](https://tech.yahoo.com/apps/articles/elementor-website-builder-review-022722440.html)). |
| Alt text only reachable per block | Squarespace, Wix | Hurts accessibility and SEO for a bilingual owner. |
| Heavy editor chrome that lags | Wix Studio | "Horrendously slow" reports ([Wix Studio forum](https://forum.wixstudio.com/t/my-wix-studio-is-extremely-slow-and-laggy-despite-powerful-hardware/65844)); a browser-only tool must stay light. |
| Plugin-dependent SEO/multilingual | Elementor, Divi, Bricks | We have no plugin surface; these must be first-class. |

### Must-haves for a "premium" feel to a non-technical accounting-firm owner (synthesis)

1. Open the admin and see the real site, in Thai, with a single obvious "เพิ่มส่วน / Add section" action that shows pictures, not names.
2. Change one palette or font pairing and watch the whole site follow, with no way to produce an ugly result.
3. Every edit is reversible: a visible "เวอร์ชัน / Versions" list with previews and one-click restore.
4. Publish is a single button that first says what will change and in which languages, then confirms when live.
5. Each section shows TH / EN / ZH status at a glance; missing translations are flagged, never silently blank.
6. SEO is four fields with a live preview, pre-filled sensibly.
7. Nothing in the UI mentions git, commits, branches, CSS, classes or tokens.

---

## 5. Open questions raised for other tickets

1. **Staging on GitHub Pages.** Do we want a true second environment (e.g. a `preview` branch deployed to a second Pages site, or PR-preview via GitHub Actions) to mirror Webflow/Framer staging, or is an in-browser preview enough? Cost: Actions complexity vs. owner confidence.
2. **Redirects without a server.** Decide the mechanism (meta-refresh stubs vs. JS vs. a `404.html` lookup table) and the SEO consequences; Webflow caps rules at ~1,000 for payload reasons — what is our cap?
3. **Translation state model.** Per-section or per-field translation status? Fallback order when ZH is missing (EN → TH?)? Should MT drafts be allowed inside the admin, and from which provider, given a no-server constraint?
4. **Design Library update semantics.** Snapshot (Squarespace) vs. linked preset (Webflow components). What happens to existing sections when a preset is revised?
5. **Section layout variants.** How many variants per section type before "bounded" stops being bounded? Squarespace's Layout Switcher suggests 3–5.
6. **Version UI vocabulary.** How to present git history as "versions" in Thai, with preview, without exposing commits; what retention/naming (manual named restore points like Webflow's ⇧⌘S)?
7. **Asset model.** Where do images live (repo vs. external), what size cap (Webflow 4 MB, Squarespace 10 MB), and how is asset-level alt text stored per language?
8. **Onboarding "personality" taxonomy.** Which 3–5 brand personalities make sense for Thai accounting/legal/advisory firms, and which palettes/font pairs map to each?
9. **Verification pass.** Confirm the items marked [verify] (Divi Quick Sites/Cloud, Elementor maintenance mode and role manager, WordPress multilingual plugin behaviour) directly against vendor docs once network access allows; none of them change the Adopt/Adapt/Avoid conclusions.

---

## Appendix — source index (all URLs cited above)

Squarespace: [tooltester review](https://www.tooltester.com/en/reviews/squarespace-review/) · [Ecommerce-Platforms Fluid Engine](https://ecommerce-platforms.com/articles/squarespace-fluid-engine-review) · [SQSPThemes Fluid Engine](https://www.sqspthemes.com/blog/squarespace-fluid-engine) · [Jessica Miller](https://www.jessicamiller.work/blog/squarespace-fluid-engine) · [Big Cat Creative](https://www.bigcatcreative.com/blog/squarespace-fluid-engine) · [Forum: Fluid engine is trash](https://forum.squarespace.com/topic/224619-fluid-engine-is-trash/) · [Beyondspace saved sections](https://beyondspace.studio/blog/squarespace-saved-sections-new-account-wide-feature) · [LaunchHappy 2023](https://launchhappy.co/guides/new-squarespace-updates-2023) · [ilovecreatives 2025](https://ilovecreatives.com/squarespace-online-course-resources-toolbox/whats-new-with-squarespace-2025) · [Paige Brunton styles PT1](https://www.paigebrunton.com/blog/customize-squarespace-style-editor) · [PT2](https://www.paigebrunton.com/blog/squarespace-site-styles-editor) · [SEOSpace fonts](https://www.seospace.co/blog/change-fonts-and-styles-squarespace) · [Collaborada redirects](https://www.collaborada.com/blog/squarespace-redirects) · [Sparkplugin redirect](https://www.sparkplugin.com/blog/squarespace-redirect) · [Weglot Squarespace](https://weglot.dev/guides/squarespace-multilingual-site) · [SQSPThemes multilingual](https://www.sqspthemes.com/blog/how-to-create-a-multilingual-website-on-squarespace) · [Collaborada hreflang](https://www.collaborada.com/blog/squarespace-multilingual-sites) · [Collaborada asset library](https://collaborada.com/blog/squarespace-asset-library) · [Big Cat media library](https://www.bigcatcreative.com/blog/media-library-squarespace) · [Kickpoint SEO](https://kickpoint.ca/how-to-change-title-tags-and-meta-descriptions-in-squarespace) · [WBE Squarespace SEO](https://www.websitebuilderexpert.com/squarespace-seo-review/) · [Elfsight undo](https://elfsight.com/tutorials/how-to-undo-changes-in-squarespace/) · [WBI version history](https://www.websitebuilderinsider.com/does-squarespace-have-version-history/) · [WBI edit without going live](https://www.websitebuilderinsider.com/how-do-i-edit-my-squarespace-site-without-going-live/) · [SEOSpace dropdown](https://www.seospace.co/squarespace-faqs/drop-down-menu-in-squarespace) · [Whatsquare nav](https://whatsquare.space/blog/how-to-edit-navigation-bar-in-squarespace) · [Sparkplugin Blueprint](https://sparkplugin.com/blog/what-is-squarespace-blueprint-ai) · [WBE Blueprint](https://www.websitebuilderexpert.com/website-builders/squarespace-blueprint-ai/) · [Ecommerce-Platforms Blueprint](https://ecommerce-platforms.com/articles/squarespace-blueprint-ai) · [Feisworld](https://www.feisworld.com/blog/squarespace-blueprint-ai-builder-review)

Webflow: [DXP Scorecard](https://www.dxpscorecard.com/platform/webflow) · [Flowout review](https://www.flowout.com/blog/webflow-review) · [CSS Agency features](https://www.thecssagency.com/blog/top-10-webflow-features) · [Publishing workflows blog](https://webflow.com/blog/publishing-workflows) · [Publishing workflow help](https://help.webflow.com/hc/en-us/articles/33961266935187) · [AirOps](https://airops.com/use-case-guides/webflow-review-changes-a-comprehensive-guide-to-publishing-updates) · [Edit Mode vs legacy](https://discourse.webflow.com/t/edit-mode-vs-legacy-editor/329699) · [Legacy editor retiring](https://www.pravinkumar.co/blog/webflow-legacy-editor-retiring-client-seats-2026) · [Shared Libraries](https://webflow.com/blog/shared-libraries) · [Libraries assets & modes](https://webflow.com/updates/shared-library-assets-and-variable-modes) · [Variables](https://webflow.com/webflow-way/design-systems/variables) · [Digidop variables](https://digidop.com/blog/webflow-variables-guide) · [Flow Ninja localization](https://www.flowninja.com/blog/webflow-localization) · [Lowcode localization](https://www.lowcode.agency/blog/webflow-localization-and-multi-language-what-to-know) · [we-r pricing](https://www.we-r.co/en/toolbox-equipe-marketing/webflow-localize-cest-quoi) · [Backups](https://university.webflow.com/lesson/backups) · [Backups update](https://webflow.com/updates/preview-restore-and-rename-backups-from-the-designer) · [Page SEO lesson](https://university.webflow.com/course-lesson/optimize-page-settings-for-seo) · [Redirects help](https://help.webflow.com/hc/en-us/articles/33961294898835) · [Brix wildcards](https://brixtemplates.com/blog/how-to-use-wildcard-redirects-in-webflow-step-by-step-guide-with-examples) · [Assets help](https://help.webflow.com/hc/en-us/articles/33961290329235) · [Relume](https://webflow.com/integrations/relume) · [G2](https://g2.com/products/webflow/reviews) · [GetApp](https://www.getapp.com/website-builder-software/a/webflow/reviews/)

Framer: [G2](https://www.g2.com/products/framer/reviews) · [Experte](https://www.experte.com/website-builder/framer) · [Flowstep](https://flowstep.ai/blog/framer-review/) · [Waida](https://waidastudio.com/learn/framer) · [Revert version](https://www.framer.com/help/articles/how-can-i-revert-to-a-previous-working-version-of-my-file/) · [Version history update](https://www.framer.com/updates/version-history-update) · [Publishing help](https://framer.com/help/articles/publishing-your-framer-website) · [Staging & versions](https://www.framer.com/ja/help/articles/staging-and-versions/) · [Publishing changelog](https://www.framer.com/updates/publishing-changelog) · [Redirects help](https://framer.com/help/articles/how-to-setup-redirects-to-maintain-seo-ranking) · [SEO help](https://framer.com/help/articles/how-to-update-page-titles-descriptions-and-social-images) · [Light/dark](https://www.framer.com/updates/light-and-dark-mode) · [Auto translate](https://www.framer.com/ja/help/articles/auto-translate-for-localization/) · [Localized paths](https://www.framer.com/updates/localized-page-paths) · [Costbench](https://www.costbench.com/software/design/framer-design/hidden-costs/) · [Framestudio](https://www.framer.com/marketplace/plugins/framestudio/) · [Framer University AI workflow](https://framer.university/blog/the-new-ai-workflow-for-building-websites)

Wix Studio: [webdew](https://www.webdew.com/blog/wixstudio) · [uiguides](https://www.uiguides.com/tools/wix-studio-review) · [TechRadar](https://www.techradar.com/pro/website-building/wix-studio-review) · [Site History](https://dev.wix.com/docs/develop-websites-sdk/publish-your-site/site-history/about-site-history) · [Adding sections](https://support.wix.com/en/article/studio-editor-adding-and-managing-sections) · [Design assets](https://support.wix.com/en/article/studio-editor-saving-and-reusing-design-assets) · [Site colors](https://support.wix.com/en/article/studio-editor-working-with-site-colors) · [Multilingual](https://www.wix.com/app-market/web-solution/wix-multilingual) · [Default SEO](https://support.wix.com/en/article/default-seo-settings) · [SEO panel](https://support.wix.com/en/article/customizing-your-seo-settings-in-the-seo-panel) · [Media alt text request](https://support.wix.com/en/article/wix-media-request-adding-alt-text-in-the-media-manager) · [Handover](https://www.wix.com/studio/academy/tutorials/how-to-handover-your-site-to-clients) · [Permissions per page](https://support.wix.com/en/article/studio-editor-editing-permissions-per-page) · [Forum slow editor](https://forum.wixstudio.com/t/my-wix-studio-is-extremely-slow-and-laggy-despite-powerful-hardware/65844) · [r/WIX](https://redlib.hbubli.cc/r/WIX/comments/1gru769/wix_studio_is_poorly_optimized)

Divi 5: [WP Marmite](https://wpmarmite.com/en/divi-5/) · [Elegant Themes features](https://www.elegantthemes.com/blog/divi-resources/divi-5-exclusive-features-so-far) · [MotoPress](https://motopress.com/blog/divi-5-review/) · [Ravenous Raven](https://ravenousravendesign.com/wordpress/divi-theme/divi-5-review-expert/) · [Divi People](https://divipeople.com/what-is-divi-5/)

Bricks: [Crocoblock](https://crocoblock.com/blog/wordpress-bricks-builder-review/) · [FatLab](https://fatlabwebsupport.com/blog/wordpress-development/bricks-builder-review/) · [PageBuildLab](https://pagebuildlab.com/bricks-builder-review-2026/) · [WPTuts global classes](https://wptuts.co.uk/mastering-bricks-builder-global-classes-for-beginners/)

Elementor: [Dreamgrow](https://www.dreamgrow.com/elementor-review/) · [Rapyd](https://rapyd.cloud/blog/elementor-review/) · [Pixelnet](https://www.pixelnet.in/blog/honest-elementor-pro-review/) · [ZealTyro](https://blog.zealtyro.com/elementor-pro-review-the-ultimate-visual-builder-or-a-path-to-bloat/) · [Yahoo Tech](https://tech.yahoo.com/apps/articles/elementor-website-builder-review-022722440.html)
