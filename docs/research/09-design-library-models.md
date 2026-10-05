# 09 — How builders model a growing Design Library

**Wayfinder research ticket #9** · researched 2026-10-05 · status: draft for discussion

Scope: how Squarespace, Webflow (+Relume), Framer, Elementor, Divi, WordPress Gutenberg, Wix Studio and
design-system tooling (Figma, Storybook, W3C/DTCG design tokens) model a *growing* library of designs, and
what we should borrow for a **curated, bounded-customization builder** for a non-technical accounting-firm owner
where "every new design is saved back into the library" is a core principle.

> Note on sources: most vendor help centres (Squarespace, Webflow, Framer, Elementor, Elegant Themes, Wix,
> developer.wordpress.org, w3.org) were blocked by the research sandbox's egress proxy, so findings come from
> web-search summaries of those official pages plus mirrored copies (e.g. the DTCG spec on GitHub). Every claim
> below carries the URL it came from; anything marked **(unverified)** should be re-checked against the primary page
> before it becomes a locked decision.

---

## 1. สรุปภาษาไทย (10 บรรทัด)

1. ทุกเครื่องมือใช้ลำดับชั้นคล้ายกัน: **ธีม/ตัวแปรกลาง → เทมเพลตหน้า → เซกชัน → รูปแบบย่อย (variant) → ชิ้นที่วางบนหน้า (instance)** แค่เรียกชื่อต่างกัน
2. จุดต่างสำคัญคือ "ของที่บันทึกไว้" เป็น **สำเนา (snapshot)** หรือ **ลิงก์ (linked)**: Squarespace / Wix Studio / Framer Templates เป็นสำเนา — แก้ต้นฉบับแล้วหน้าที่ใช้อยู่ไม่เปลี่ยน; Webflow / Figma / Divi global / WordPress synced pattern เป็นลิงก์ — แก้ที่เดียวเปลี่ยนทุกที่
3. มืออาชีพบ่นทั้งสองขั้ว: สำเนาทำให้ "แก้ทั่วเว็บไม่ได้" (Wix, Squarespace), ส่วนลิงก์ทำให้ "ปรับเฉพาะจุดไม่ได้ ต้องตัดลิงก์ (detach) แล้วอัปเดตไม่ถึง" (Figma, Webflow) — ทางออกที่ทุกคนเดินไปคือ **ลิงก์ + ช่องแก้ได้เฉพาะจุด (overrides / props / slots)**
4. การผูกกับธีม: ทุกเครื่องมือที่ดีผูกสี/ฟอนต์/ระยะห่าง/มุมโค้ง กับ **ตัวแปรกลาง (tokens / variables)** ไม่ใช่ค่าตายตัว เพื่อให้เปลี่ยนธีมแล้วทุกชิ้นเปลี่ยนตาม (Webflow Variables, Divi 5 Design Variables, Figma Variables + modes, WP theme.json, Squarespace color themes)
5. ภาพตัวอย่าง (thumbnail): เครื่องมือเว็บส่วนใหญ่ **เรนเดอร์สด** ย่อส่วนใน iframe (WordPress ใช้ `viewportWidth`) หรือใช้ภาพนิ่งที่ผู้ออกแบบจัดเอง (Figma); สำหรับเราควร "เรนเดอร์สดด้วยธีมปัจจุบัน" เพื่อให้ตัวอย่างตรงกับของจริง
6. การจัดหมวด: ใช้ **หมวดตามความตั้งใจ (intent)** เช่น Hero / Services / Testimonials / Contact / Pricing + แท็ก; WordPress และ Elementor Kits ให้หนึ่งชิ้นอยู่ได้หลายหมวด
7. ตอน "บันทึกกลับเข้าคลัง": ของจริงมักบันทึก **ทั้งดีไซน์และเนื้อหา** (Squarespace, Wix, Divi static) — Divi มี Selective Sync ให้เลือกซิงก์เฉพาะ Design ไม่ซิงก์ Content ซึ่งใกล้กับที่เรา​ต้องการที่สุด
8. การเวอร์ชัน: ไม่มีเครื่องมือ no-code ตัวไหนมีเลขเวอร์ชันของ preset จริง ๆ; Webflow Libraries มี changelog + "Accept updates"; Figma ให้ทีมคิดระบบเอง (semver, ป้าย ⚠️ deprecated, swap library); DTCG มีฟิลด์ `$deprecated` อย่างเป็นทางการ
9. หลายภาษา: Webflow แยก "localize ตัวนิยาม component" กับ "localize instance"; WordPress ใช้ไฟล์ PHP pattern เพื่อให้แปล placeholder ได้; ที่อื่นแทบไม่รองรับ — เราควรเก็บ placeholder เป็น key แยกตามภาษาตั้งแต่แรก (EN ตอนนี้, TH ภายหลัง)
10. ข้อเสนอสำหรับเรา: **Section Preset ที่ลิงก์กับ token ของธีม + บันทึกกลับแบบ "ถอดเนื้อหาจริงออก เหลือ placeholder" + เวอร์ชันแบบ "ชิ้นที่วางแล้วตรึงเลขเวอร์ชันไว้ จนกว่าเจ้าของจะกดอัปเกรด" + ป้าย deprecated แทนการลบ**

---

## 2. Per-product notes

### 2.1 Squarespace 7.1 (Fluid Engine) — Site Styles → Page layouts → Sections → Blocks → Saved Sections

**Hierarchy & vocabulary.** Site Styles (global fonts, 5-colour palette → 10 generated "color themes") → *Page layouts* (pre-built pages made of sections) → *Sections* (each section picks a color theme) → *Blocks* placed on the Fluid Engine grid.
Sources: https://htmlburger.com/blog/squarespace-7-1-vs-7-0/ · https://bigcatcreative.com/blog/squarespace-fluid-engine-tutorial · https://www.applet.studio/blog/squarespace-color-variables

**Saved Sections (May 2025; account-wide later in 2025).** Hover a section → heart icon → "My Saved Sections". Per-site limit was 50; account-level saves allow 250 and work across all sites on the account.
Sources: https://ilovecreatives.com/squarespace-online-course-resources-toolbox/whats-new-with-squarespace-2025 · https://beyondspace.studio/blog/squarespace-saved-sections-new-account-wide-feature · https://www.beyondspace.studio/blog/how-to-use-squarespace-account-saved-sections

**Snapshot, not linked.** "Saved Sections act as static snapshots, meaning edits made to one instance won't affect others." Updating the original does not update the saved copy or any placed copy. Third-party plugins ("Synced Blocks") exist precisely to fill the gap.
Sources: https://www.temperstack.com/learn/squarespace/save-reusable-sections/ · https://beyondspace.studio/qanda/how-to-create-reusable-blocks-across-your-squarespace-site

**Token binding.** Because sections reference a *color theme* (not hex values) and fonts come from Site Styles, "when you use a saved section on a different website, the section preserves all customizations but adopts the new site's fonts and colors". Custom CSS that follows this uses CSS variables such as `--headingLargeColor` / `siteBackgroundColor`.
Sources: https://squarekicker.com/tutorials/squarespace-saved-sections-squarekicker · https://www.will-myers.com/articles/custom-code-that-actually-works-with-squarespace-color-themes

**Content.** Saved with the section (text, images) — it is a snapshot of the whole section. Cannot save collection pages or footers.
Source: https://www.temperstack.com/learn/squarespace/save-reusable-sections/

**Praise / criticism.** Praised: simplest possible save-back flow (one click), colour-theme indirection makes copies restyle automatically. Criticised: no linked updates; a hard cap (50/250); no versioning at all.

---

### 2.2 Webflow — Variables → Styles (classes) → Components (+properties, variants, slots) → Libraries (+Relume)

**Hierarchy & vocabulary.** *Variables* ("also known as design tokens, the most atomic unit of your design system"; types Size, Color, Font, Percentage, Number; *Variable modes* for light/dark or per-breakpoint) → *Classes/styles* → *Components* (a *main component* + *instances*) → *Component properties* (Text, Rich text, Link, Video, Number, Visibility, Variant, Slot) → *Libraries* shared across a Workspace.
Sources: https://webflow.com/feature/variables · https://webflow.com/updates/variables · https://webflow.com/webflow-way/design-systems/variables · https://help.webflow.com/hc/en-us/articles/33961195339923-Slots · https://developers.webflow.com/code-components/reference/prop-types/variant

**Linked instances with bounded overrides.** Instances inherit from the main component; only exposed properties can differ per instance. `unlinkComponent()` turns an instance into plain elements that "will no longer" receive updates (a *detached copy*). Slots (2025–26) let any element be dropped into a designated area without unlinking.
Sources: https://developers.webflow.com/designer/reference/component-element/unlinkComponent · https://releases.sh/release/rel_NPLtElsFfOtyLT42-FCDu-component-slots-open-to-any-element-type

**Libraries = the only no-code tool with an explicit publish/accept cycle.** Source site → "Review updates" → changelog → "Share updates"; consuming site → "Review updates" → "Accept all updates". A Library component can be converted to a *site component* (a copy that stops receiving updates). Variables travel with the Library so components restyle to the installed variable values.
Sources: https://university.webflow.com/lesson/libraries · https://webflow.com/feature/shared-libraries · https://webflow.com/updates/libraries

**Relume.** A 1,000+ section library delivered as a Webflow Library; components "automatically adapt to sync with the selected style guide" (Client-First v2.1 class system + colour variables). Relume withheld *size* variables because Webflow variables did not support breakpoints — a reminder that token coverage limits what presets can bind to.
Sources: https://library.relume.io/whats-new/january-component-day · https://relume.io/resources/docs/customizing-the-relume-style-guide-for-webflow · https://community.relume.io/x/issues/msg_8DPzf0ZEhQZb/confusion-around-relume-style-guides-and-color-var

**Multilingual.** Webflow Localization distinguishes *localizing the component definition* (default text per locale, applies to all instances — good for navbars/footers) from *localizing one instance* (good for heroes, testimonials, CTAs). Property defaults can differ per locale.
Sources: https://help.webflow.com/hc/en-us/articles/33961240676371 · https://developers.webflow.com/data/v2.0.0-beta/docs/localizing-components-beta · https://webflow.com/updates/reset-localized-component-prop-defaults

**Praise / criticism.** Praised: variables + linked components + Library changelog is the most complete model. Criticised by professionals: Webflow says "X instances of component Y" but not *where* ("making site cleanups virtually impossible"), and many settings cannot be exposed as properties, so people end up unlinking. "Creating a stable and consistent design system is nearly impossible" is a direct quote from a wishlist thread.
Sources: https://wishlist.webflow.com/ideas/WEBFLOW-I-6506 · https://wishlist.webflow.com/ideas/WEBFLOW-I-6810

---

### 2.3 Framer — Color/Text styles → Components (primary variant → variants) → Component variables → Templates

**Hierarchy & vocabulary.** *Color styles* and *Text styles* in the Assets panel (global; change one swatch → everything updates) → *Components* ("parents") → *Variants* ("Every variant inherits its layer structure and shared properties from the primary variant"; overrides highlighted purple and resettable) → *Component variables* (text, link, colour, image, boolean exposed as per-instance controls) → *Instances*. Insertion can be as a linked instance or a *detached layer*.
Sources: https://www.framer.com/academy/lessons/component-variants-in-framer · https://www.framer.com/academy/lessons/component-variables-in-framer · https://www.framer.com/developers/plugins-with-components · https://www.framer.com/dictionary/variant

**Templates.** "A Framer template is a copy of a complete project, not a theme or style package applied to another project." Buyers restyle by editing the shared colour/text styles. Cross-project paste works but "Text Styles now automatically flatten when pasted across projects" — i.e. the token binding is lost when something leaves its project.
Sources: https://www.framer.com/help/articles/how-templates-work/ · https://www.framer.com/updates/page-pasting · https://framer.com/updates/copy-and-pasting

**Multilingual.** Native Localization feature; text in components/CMS can be translated per locale; marketplace "locale toggle" components use the Locale API.
Sources: https://Framer.com/academy/topics/localization · https://www.framer.com/marketplace/components/locale-lang-toggle/

**Praise / criticism.** Praised: the primary-variant inheritance + "reset override" model is the clearest UI for *why* something looks the way it does. Criticised: a template is a whole-project copy — no mechanism to pull later improvements into an existing site; style flattening on paste.

---

### 2.4 Elementor — Kit (Site Settings) → Templates (page/section/container) → Widgets → Global Widget → Loop templates

**Hierarchy & vocabulary.** The active *Kit* is a hidden WordPress post that stores the site's design system: Global Colors, Global Fonts, theme styles, layout settings. *Saved Templates* (page, section/container, popup, Theme Builder parts) live in Templates → Saved Templates. *Global Widgets* (Pro) are linked widget instances; "Unlink from global" detaches one. *Website Kits* (3.3+) export/import an entire site (content, templates, site settings) as a zip, with 3.6+ letting you choose which parts to include.
Sources: https://developers.elementor.com/docs/data-structure/global-styles/ · https://elementor.com/academy/global-colors-and-fonts/ · https://elementor.com/help/global-widget-pro · https://elementor.com/blog/introducing-elementor-3-3/ · https://elementor.com/help/?p=59020 · https://developers.elementor.com/docs/cli/kit-export

**Token binding.** Widgets bind to Global Colors/Fonts by reference; changing the Kit restyles every bound widget. A "Global Style Preview" sheet shows all fonts/colours at once.
Source: https://elementor.com/academy/?p=7932

**Loop Builder.** A *Loop template* is a single-item design applied to every item of a query (posts, products) — the "design once, content many" pattern.
Source: https://elementor.com/blog/introducing-314-nested-carousel-loop-grid-ads-and-more/

**Versioning / deprecation reality.** Editor V4 ("Atomic") replaces Global Widgets with a *Class Manager*; users report V4 "removes the useful Global Widgets feature" and that 4.3 "broke their global widgets". Elementor keeps V3 editing opt-in so old sites keep working — a *parallel-track* deprecation rather than a migration.
Sources: https://elementor.com/help/what-are-the-differences-between-the-elementor-editor-3-x-and-v4 · https://theplusaddons.com/blog/disable-elementor-atomic-editor/ · https://roadmap.wdesignkit.com/boards/feature-requests/posts/global-widget · https://elementor.com/help/?p=3872

**Content in saved templates.** Saved templates and Kits include the content that was in them at save time; Kits explicitly export pages/posts/products.

**Praise / criticism.** Praised: Kit as a single design-system record; Loop templates. Criticised: Global Widgets were all-or-nothing linked (no per-instance overrides), then dropped in V4; Website Kits are heavy "whole site" bundles, not a growing library.

---

### 2.5 Divi (4 → 5) — Design Variables → Option Group Presets → Element Presets → Divi Library (static or global, selective sync)

**Hierarchy & vocabulary.** Divi 5 *Design Variables* (six types: colours, fonts, numbers, images, text, links — so a variable can hold a logo, phone number or CTA label, not just a colour) → *Option Group Presets* (a reusable set for one option group: borders, shadow, typography, spacing…) → *Element Presets* (a whole module's configuration; a module can have several named presets with one default) → *Divi Library* items (module/row/section/layout) saved either as a *static* copy or as a *Global* item (green in the builder; edits propagate everywhere) → Theme Builder templates (header/footer/post layouts) saved to Library or Divi Cloud.
Sources: https://help.elegantthemes.com/en/articles/15520440-part-3-creating-a-divi-5-global-design-system-with-design-variables · https://help.elegantthemes.com/en/articles/13348842-global-variables-in-divi-5 · https://www.elegantthemes.com/blog/divi-resources/using-design-variables-with-presets-in-divi-5 · https://www.elegantthemes.com/blog/divi-resources/using-the-divi-theme-builder-in-divi-5

**Token binding.** "Every preset in the system connects to design variables for colors, fonts, and spacing values, and changing a single variable updates all presets that reference it." Divi 5 adds HSL *relative colours* (e.g. "20% darker than brand") so derived shades stay in sync — a fix for Divi 4 Global Colors, which were "a set of fixed hex values… with no parent-child relationships".
Sources: https://www.elegantthemes.com/blog/divi-resources/mastering-global-colors-in-divi-5 · https://www.elegantthemes.com/blog/divi-resources/everything-you-need-to-know-about-divi-5s-relative-colors-hsl

**Selective Sync — the closest existing answer to "design yes, content no".** When saving a global item you can "selectively sync any or all of the Content, Design, or Advanced tabs… edit settings to only sync the Design Settings while allowing unique content in the Content tab for each instance."
Source: https://www.elegantthemes.com/documentation/divi/selective-sync/ · https://www.elegantthemes.com/gallery/divi/documentation/global-modules/

**Versioning.** Divi 5 replaced shortcode storage with a new structured format and ships a Migrator; unsupported third-party modules are wrapped in a backward-compatibility layer. Known migration defects (font resets vs presets, menu colours, blurb icon placement) show the cost of changing the storage format under existing pages.
Sources: https://www.elegantthemes.com/blog/divi-news/divi-5-migration · https://help.elegantthemes.com/en/articles/12767407-how-to-safely-migrate-from-divi-4-to-divi-5 · https://docs.respira.press/docs/troubleshooting/divi-5

**Praise / criticism.** Praised: three-layer variables → option-group presets → element presets is the most granular restyle model among page builders; variables that hold business text. Criticised: the migration pain above; green "global" items are easy to edit by accident (a classic complaint since Divi 2.4: https://www.elegantthemes.com/blog/tips-tricks/exploring-divi-2-4-the-power-of-divis-global-modules-and-how-to-use-them).

---

### 2.6 WordPress Gutenberg — theme.json (+style variations, section styles) → Templates/Template parts → Patterns (synced / unsynced, overrides) → Blocks

**Hierarchy & vocabulary.** `theme.json` defines the palette, type scale, spacing presets; *style variations* are alternate JSON files that override it (whole-theme skins); WP 6.6 *section styles* are block style variations defined in theme.json that re-skin a Group and everything inside it. *Templates* and *template parts* (header/footer) are block HTML. *Patterns* are pre-arranged blocks; *unsynced* patterns are inserted as a copy, *synced* patterns (formerly Reusable Blocks) are linked; a synced pattern can be *detached* to regular blocks.
Sources: https://developer.wordpress.org/themes/patterns/introduction-to-patterns/ · https://fullsiteediting.com/?p=14656 · https://fastcomet.com/blog/?p=9925 · https://wordpress.org/support/article/reusable-block/

**Pattern Overrides (WP 6.6, 2024).** Inside a synced pattern the author flags specific blocks (paragraph, heading, button, image) as *overridable*; each placed instance may change that text/URL/image while layout and style stay linked. This is the "linked structure, local content" model. Turning overrides on/off got a dedicated modal in Gutenberg 18.2.
Sources: https://developer.wordpress.org/news/2024/06/an-introduction-to-overrides-in-synced-patterns/ · https://make.wordpress.org/core/2024/04/24/whats-new-in-gutenberg-18-2-24-april/ · https://essential-blocks.com/wordpress-synced-patterns-consistent-design/

**Registration record.** `register_block_pattern( name, { title, content, description, categories[], keywords[], viewportWidth, blockTypes[], postTypes[], templateTypes[], inserter } )`. A pattern may belong to several categories; `inserter:false` hides it (used for translatable "hidden patterns").
Sources: https://developer.wordpress.org/block-editor/reference-guides/block-api/block-patterns/ · https://wp-kama.com/function/register_block_pattern

**Preview.** Patterns are **live-rendered** in the inserter inside a scaled iframe; `viewportWidth` "is the width of the iframe viewport when previewing the pattern (in pixels)" so the thumbnail is a real render at the intended width, scaled down. No static image is stored.
Source: https://developer.wordpress.org/block-editor/reference-guides/block-api/block-patterns/

**Multilingual.** Block HTML templates "cannot execute PHP translation functions", so themes register patterns from PHP files using `esc_html__()` / `__()` + `wp_kses_post()` and reference them via `wp:pattern` in templates; the Pattern Directory has a translation project.
Sources: https://kinsta.com/blog/block-themes-internationalization/ · https://make.wordpress.org/polyglots/2021/09/19/how-to-handle-block-pattern-translations/

**Praise / criticism.** Praised: live previews, multi-category, theme.json indirection, overrides. Criticised: overrides limited to a few attributes and only in block themes; synced-pattern UI confusion (synced vs unsynced vs detached); patterns bake content in unless the theme author writes placeholder-only patterns.

---

### 2.7 Wix Studio — Site Styles → Global sections → Sections → Design assets → Design libraries

**Hierarchy & vocabulary.** *Site Styles* (colour + typography palettes; connected elements update automatically) → *Global sections* (header/footer, or any section reused site-wide and kept in sync) → *Sections* → *Design assets* (any section/element right-click → "Save as Asset", named, put in a library) → *Design libraries* at the account level ("every library contains a single set of color and typography styles, and unlimited space for designed assets").
Sources: https://support.wix.com/en/article/studio-editor-saving-and-reusing-design-assets · https://support.wix.com/en/article/studio-editor-creating-and-managing-design-libraries · https://support.wix.com/en/article/studio-editor-adding-and-managing-sections

**Token binding.** When reusing from a library you can choose "Site Styles", which "automatically adapts your design to the current look and feel" — i.e. remap to the destination theme at insert time.
Source: https://support.wix.com/en/article/studio-editor-saving-and-reusing-design-assets

**Snapshot, not linked.** Once placed, "they become independent from the original saved version… there is no way to make global updates that automatically apply to all instances". Wix tracks this as an open feature request; the Wix Studio forum asks whether "global component management" is on the roadmap. Global sections cannot be saved as assets; sections with apps/forms/inputs/galleries cannot be saved.
Sources: https://support.wix.com/en/article/studio-editor-request-making-global-changes-to-saved-assets · https://forum.wixstudio.com/t/wix-studio-is-global-component-management-on-the-roadmap/78483

**Praise / criticism.** Praised: libraries carry their own colour/type set, and "use Site Styles" at insert is a clean theme-remap step. Criticised: no linked updates; many element types excluded from saving.

---

### 2.8 Design-system tooling

#### Figma — Variables (collections, modes) → Styles → Components (properties, variants, slots) → Libraries (publish, swap)

- *Variable* = named value with one value **per mode** of its collection (Light/Dark, brand A/B). Two-collection practice: *primitive* collection (raw values) + *semantic* collection (aliases with modes); components bind only to semantic tokens so a mode switch restyles everything.
  Sources: https://figma-signup.helpjuice.com/variables/overview-of-variables-collections-and-modes · https://www.resumelens.org/blog/figma/figma-variables-and-design-tokens · https://atomize.tools/blog/figma-variables-dark-mode/
- *Component properties* (Boolean, Text, Instance swap, Variant) are the bounded overrides; *detach* makes a plain frame that no longer updates. *Slots* (beta 2025, GA 2026-03-05) exist "to eliminate detaching components" — designated areas where custom content keeps the link.
  Sources: https://figma-signup.helpjuice.com/detach-an-instance-from-the-component · https://www.createwith.com/tool/figma/updates/figma-launches-slots-in-open-beta-to-eliminate-detaching-components · https://www.createwith.com/tool/figma/updates/figma-rolls-out-slots-feature-to-general-availability-on-march-5
- *Versioning*: "Figma does not enforce version numbers on library publishes, which is where most teams go wrong". Mature teams apply semver to publishes, announce breaking changes ahead of time, mark deprecated components (prefix "⚠️", shown monochrome, kept but hidden), and use *Swap library* to move a file from an old library version to a new one. Legacy libraries pile up ("library_01.01.03-legacy").
  Sources: https://www.resumelens.org/blog/figma/figma-library-publishing-best-practices · https://forum.figma.com/ask-the-community-7/managing-legacy-libraries-of-a-design-system-14295 · https://forum.figma.com/ask-the-community-7/best-approach-for-replacing-legacy-components-in-an-existing-figma-library-51621 · https://forum.figma.com/ask-the-community-7/deprecations-library-update-name-with-hidden-components-problem-22517
- *Thumbnails*: file thumbnail is the first page or a chosen frame (static, designer-curated).
  Source: https://help.figma.com/hc/en-us/articles/23510169950871-Design-a-file-thumbnail
- Criticism: editing a main component can reset instance overrides; detaching nested instances is painful (why Slots exist).
  Sources: https://forum.figma.com/archive-21/modifying-component-resets-overrides-on-instances-of-that-component-24126 · https://forum.figma.com/t/lock-an-instance-of-a-component-so-its-not-affected-by-updates/42545

#### Storybook — a *story* is a named, saved configuration (args) of one component

- CSF3: one file per component; each named export is a *story* = component + `args` (the preset values). *Autodocs* generates a docs page from JSDoc + prop types + all stories; *tags* control inclusion ("many different uses of the same total set of stories"). Previews are **live renders** in an iframe; static PNGs only via add-ons/visual testing.
  Sources: https://storybook.js.org/docs/8/writing-stories/tags · https://storybook.js.org/addons/storybook-addon-figma-sync
- Versioning literature (Nathan Curtis / EightShapes, UXPin, enterprise guides): semver per package or per component; a written **deprecation policy** ("what counts as deprecated, how it is announced, how long it stays, what migration help exists, when removal happens"); component-level deprecation notices inside docs and types. "Design systems without a deprecation policy tend to oscillate between breaking too fast or carrying legacy behavior forever."
  Sources: https://eightshapes.com/articles/versioning-design-systems · https://nathanacurtis.substack.com/p/versioning-design-systems-48cceb5ace4d · https://www.uxpin.com/studio/blog/component-versioning-vs-design-system-versioning/ · https://www.pathtoproject.com/blog/20260505-component-api-versioning-for-enterprise-design-systems

#### W3C Design Tokens Community Group — Format Module 2025.10 (first stable, 2025-10-28) + Resolver Module

- A token is any object with `$value`; optional `$type` (inheritable from group; "Tools MUST NOT attempt to guess the type"), `$description`, `$extensions` (reverse-domain keys, must be preserved), and **`$deprecated`** (`true`, a reason string, or `false` to override a deprecated group). Aliases use `{group.token}` syntax; composite types (typography, shadow, border) are objects of sub-values. The Resolver Module models *sets* + *modifiers/contexts* for theming (light/dark, brand).
  Sources: https://www.w3.org/community/design-tokens/2025/10/28/design-tokens-specification-reaches-first-stable-version/ · https://www.designtokens.org/TR/drafts/format · https://www.w3.org/community/reports/design-tokens/CG-FINAL-resolver-20251028/ · https://raw.githubusercontent.com/design-tokens/community-group/main/technical-reports/format/design-token.md
- Relevance: gives us a vendor-neutral vocabulary (token, group, alias, type, deprecated) and a precedent that **deprecation is a flag, not a deletion**.

---

### 2.9 Cross-product comparison

| Product | Saved thing is… | Per-instance customisation | Binds to theme tokens | Preview | Content saved? | Versioning / deprecation | Multilingual |
|---|---|---|---|---|---|---|---|
| Squarespace Saved Sections | snapshot copy | free (it is a copy) | yes, via colour themes + Site Styles | live render in picker (unverified) | yes, all | none | none |
| Webflow Components/Libraries | linked instance | only exposed properties + slots; unlink = copy | yes, Variables (+modes) | live render | definition holds defaults | Library changelog + accept; no numbers | definition vs instance per locale |
| Framer Components/Templates | linked instance / template = project copy | component variables + variant switch; detach | colour/text styles; flattened on cross-project paste | live render | defaults in primary variant | none | native Localization |
| Elementor Global Widget / Kit | linked (GW) or copy (template) | none for GW (unlink = copy) | Global Colors/Fonts in Kit | live render | yes | V4 drops GW; V3 kept opt-in | via plugins |
| Divi global item / presets | linked (global) or static copy | Selective Sync: sync Design, not Content | Design Variables (6 types, relative colours) | live render | choose per tab | storage-format migration + compat layer | via plugins |
| WP synced pattern | linked; unsynced = copy; detach = copy | Pattern Overrides on flagged blocks | theme.json presets, section styles | live iframe at `viewportWidth` | yes unless author uses placeholders | none native | PHP pattern files |
| Wix Studio design assets | snapshot copy | free (copy) | "use Site Styles" remap on insert | static/live (unverified) | yes | none; global update is an open request | none |
| Figma components | linked instance | properties, variants, slots; detach | Variables + modes | curated frame | n/a | team-run semver, ⚠️ deprecated, swap library | n/a |
| Storybook story | code | args | tokens in code | live iframe | args only | semver + deprecation policy | n/a |
| DTCG tokens | data | — | is the token layer | — | — | `$deprecated` flag | — |

---

## 3. Reference model for our Design Library

Our context: a static site (no backend), one owner who is non-technical, a locked Navy + Soft Linen palette and Instrument Serif/Inter type, English now and Thai later, and the rule "every new design is saved back into the library". The model below borrows the pieces that fit that context and deliberately leaves out the ones that do not.

### 3.1 Hierarchy (five levels, nothing deeper)

1. **Theme** — the single source of truth for *tokens*: colours (navy, linen and their derived shades), type (two font families + a type scale), spacing scale, radius scale, shadow, container widths. Exactly one active theme per site; it is what Squarespace calls Site Styles, Elementor calls the Kit, Divi calls Design Variables, WordPress calls theme.json. Tokens follow DTCG vocabulary (name, type, value, description, deprecated) and may alias other tokens (semantic → primitive, as in Figma's two-collection practice).
2. **Page template** — a named ordered list of *slots* for sections (e.g. "Service page: Hero → Intro → Service list → FAQ → CTA"). Templates reference section *types*, not specific presets, so any preset of the right type can sit in a slot (Squarespace page layouts; WP templates).
3. **Section type** — the structural contract: what content fields a section carries (heading, body, up to N items each with icon/title/text, one CTA…). This is the thing a template slot asks for. Webflow/Figma call it the main component; WP calls it the block pattern's block structure.
4. **Preset** (a.k.a. *variant* of a section type) — one saved *design* of a section type: layout arrangement, which tokens each part binds to, option choices (alignment, density, image side, columns), and **placeholder** content per language. Several presets per section type (e.g. Hero / Centered, Hero / Split-image, Hero / Quiet). This is Divi's Element Preset, Framer's variant, Storybook's story.
5. **Instance** — a preset placed on a page, with the owner's real content in the content fields and, optionally, a small set of allowed *overrides* (e.g. alignment, image side, colour mode light/dark) chosen from the preset's option list. Instances never carry raw colours, fonts or pixel values.

Vocabulary to adopt in the UI and docs: **Theme, Token, Page template, Section, Preset, Instance, Option, Override, Placeholder, Deprecated**. Avoid "component", "variant", "pattern", "block", "global widget" in owner-facing text (they mean different things in every product and the owner will Google them).

### 3.2 What a preset record contains (field list, prose)

- **Identity**: a stable id (never reused), a human name ("Hero — Split image"), the section type it implements, a one-line purpose written for the owner ("Use at the top of a service page when you have a good photo").
- **Version**: an integer or semver string, plus a short changelog entry per version, and a `deprecated` flag with a reason and a pointer to the replacement preset (DTCG `$deprecated` precedent; Figma ⚠️ practice).
- **Lineage**: the preset it was saved from (parent id + parent version), and the date/author of the save-back. This is how "the library grows" stays legible — a family tree rather than a flat pile.
- **Categorisation**: one primary *intent* category (see 3.5), any number of tags, and an ordering weight within its category (WP patterns allow multiple categories; we keep one primary for a tidy picker and use tags for the rest).
- **Structure**: the arrangement of parts — which parts exist, their order, the layout option set (e.g. `imageSide: left|right`, `align: left|center`, `density: compact|regular`) and the default value of each option.
- **Token bindings**: for every styled part, the *token name* it uses (e.g. `color.surface.section-alt`, `type.heading.l`, `space.section-y`, `radius.card`). No literal values are stored in a preset. If a preset needs a new look, a new *token* is added to the theme first (Divi's rule: variables → option-group presets → element presets).
- **Allowed overrides on instances**: an explicit, short whitelist — the bounded-customization boundary. Everything not listed is locked to the preset. (Webflow properties / WP Pattern Overrides / Divi Selective Sync all converge here.)
- **Placeholder content per language**: for every content field, placeholder text keyed by locale (`en`, later `th`), plus placeholder image references from a small neutral stock set. Marked clearly as placeholder so the save-back step can tell real content from placeholder content.
- **Constraints**: min/max item counts, maximum heading length that still fits the layout, image aspect ratio required — the preset's "fits" rules so the owner is warned before the design breaks.
- **Preview spec**: which placeholder set and which option values to use when rendering the thumbnail, and the viewport width to render at (WP `viewportWidth` idea).
- **Usage index**: the list of pages/instances currently using this preset and at which version (addresses the Webflow "where are my instances?" complaint).

### 3.3 Token binding rule

- Presets bind to **semantic** tokens only (`color.text.on-dark`, not `navy-900`), and semantic tokens alias primitives. Changing the theme means editing primitives or re-pointing semantics; every preset and every instance restyles because nothing stored a literal. This is the Figma two-collection model, Divi 5's variables→presets chain, and Squarespace's colour-theme indirection.
- A preset may offer a **colour mode** option (light section / dark section / linen section) implemented as a token *set switch* (DTCG Resolver "modifier"; Webflow/Figma "modes"), not as a different preset. That keeps the preset count small.
- Tokens themselves can be deprecated with a replacement pointer; a theme change that removes a token must first re-point every preset that uses it (the usage index makes this checkable).
- Because the site is static, tokens become CSS custom properties in `theme/theme.css`; presets reference them by name. This mirrors what Squarespace does with `--headingLargeColor` and what Webflow does when exporting variables as CSS variables.

### 3.4 Preview

- **Live render, not stored image.** Render the preset with its placeholder content and the *current* theme, at a fixed viewport width, scaled down in the picker (the WordPress inserter approach). This guarantees the thumbnail always matches what will appear, including after a theme change — a stored PNG goes stale the moment the palette changes (Figma's curated-frame thumbnails are fine for designers, wrong for a non-technical owner).
- Show two previews when the preset has a colour-mode option (light/dark), otherwise one.
- Preview text should be the English placeholder until Thai exists; the picker should switch placeholder language with the site language.

### 3.5 Categories for an accounting-firm site

Intent-based, one primary category per preset, mirroring the pages a Thai accounting firm actually has:

- **Hero / Opening** (service hero, home hero, article hero)
- **Trust** (credentials, licences, years in business, client logos, numbers/stats)
- **Services** (service list, service detail, pricing/packages, what-is-included)
- **Process** (how we work, onboarding steps, document checklist, deadlines calendar)
- **People** (team, partner profile, "who handles your account")
- **Proof** (testimonials, case notes, before/after of a clean-up engagement)
- **Knowledge** (article list, article card grid, newsletter/tax-deadline reminder)
- **FAQ & Compliance notes** (FAQ accordion, legal/PDPA notice, disclaimer)
- **Contact & Conversion** (CTA band, contact form area, map/office hours, LINE/phone)
- **Structure** (header, footer, breadcrumb, section divider)

Tags cut across: `dark`, `with-image`, `compact`, `thai-ready`, `seasonal` (tax season), `home-only`.

### 3.6 Save-back flow ("every new design goes back into the library")

1. The owner customises an instance within the allowed overrides, or asks for a new design; the designer/AI builds it as an instance on a page.
2. "Save to library" opens a short form: name, intent category, one-line purpose, and a required choice **"Save design only (recommended)"** vs "Save with this content as an example". Default is design-only.
3. **Strip step** (design-only): every content field is replaced by the section type's placeholder for each language; real images are replaced by neutral placeholders; real phone numbers/links are removed. Token bindings and option values are kept. Anything that was a literal value (should not happen, but if an override introduced one) is flagged and must be mapped to a token before saving. This is Divi Selective Sync's "Design yes, Content no", made the default.
4. **Lineage step**: the new preset records parent preset + version. If the change was *small* (an option default changed, spacing tweak), offer "Update the existing preset as a new version" instead of creating a sibling — otherwise the library fills with near-duplicates (the Figma "dozen legacy libraries" problem).
5. **Preview step**: the live thumbnail renders immediately from placeholders; the owner approves the name/category.
6. The page keeps using the instance exactly as before; it is now recorded as using the new preset (or new version) in the usage index.

### 3.7 Versioning rule (so old pages never break)

- **Instances pin a preset version.** A page that placed "Hero — Split image v3" keeps rendering v3 until someone explicitly upgrades it. New pages always get the latest non-deprecated version. (Webflow Libraries' "Review updates → Accept" made explicit per instance; avoids Figma's "editing the main component reset my overrides".)
- **Minor vs major.** A change that keeps the same content fields and allowed overrides is *minor* (safe to offer "Upgrade all N instances" with one click; token-only changes don't even need a version bump because they live in the theme). A change that adds/removes a content field or an option is *major*: the owner is shown each affected page with a side-by-side preview before upgrading.
- **Deprecate, never delete.** A preset marked deprecated disappears from the picker, keeps rendering wherever it is used, shows a "newer design available" note on those pages, and points to its replacement. Removal happens only when the usage index is empty. (DTCG `$deprecated`; Figma ⚠️; the EightShapes/Curtis deprecation-policy checklist: what counts, how announced, how long kept, migration help, when removed.)
- **No detached copies.** We do not offer "unlink" for owner use; a design that needs to differ from its preset becomes a *new preset version or sibling* via the save-back flow, so it stays in the library. Detaching is what every product's professionals end up regretting (Webflow, Figma, Elementor GW).
- **Theme changes are not versions.** They apply everywhere instantly by design; the only protection needed is the token-usage check in 3.3.

### 3.8 Multilingual rule

- Placeholder content is stored per locale inside the preset from day one, even if only `en` is filled; `th` falls back to `en` with a visible "needs Thai placeholder" badge.
- Real content lives on the instance, also keyed per locale; the preset never knows the owner's real text.
- Constraints (max heading length etc.) are checked per locale, because Thai line-breaking and glyph height differ from English — this is why a one-size English placeholder is not enough.

---

## 4. Pitfalls to avoid (with evidence)

1. **Snapshot-only libraries.** Squarespace and Wix Studio saved sections are copies; users then ask for "global updates" and buy plugins to get them (Squarespace Synced Blocks; Wix feature request). For a library that is supposed to grow and improve, copies mean every improvement must be re-applied by hand.
   https://support.wix.com/en/article/studio-editor-request-making-global-changes-to-saved-assets · https://beyondspace.studio/qanda/how-to-create-reusable-blocks-across-your-squarespace-site
2. **All-or-nothing linking that forces detach.** Elementor Global Widgets had no per-instance overrides, so people unlinked; Figma users detached whenever props did not cover a need and then lost updates — Figma shipped Slots specifically "to eliminate detaching". Our override whitelist must cover the realistic cases (text, image, alignment, colour mode), or owners will ask for detach.
   https://elementor.com/help/global-widget-pro · https://www.createwith.com/tool/figma/updates/figma-launches-slots-in-open-beta-to-eliminate-detaching-components
3. **Not knowing where a preset is used.** Webflow shows instance counts but not pages, "making site cleanups virtually impossible". Keep a usage index from day one.
   https://wishlist.webflow.com/ideas/WEBFLOW-I-6506
4. **Literal values leaking into presets.** Divi 4 Global Colors were fixed hex values with no relationships; Framer flattens text styles on cross-project paste; Relume could not ship size variables because Webflow variables lacked breakpoint support. Any literal in a preset is a future restyle bug — reject at save time.
   https://www.elegantthemes.com/blog/divi-resources/mastering-global-colors-in-divi-5 · https://www.framer.com/updates/page-pasting · https://library.relume.io/whats-new/january-component-day
5. **Saving real content into the library.** Squarespace/Wix/Elementor templates carry the content they had when saved; WordPress patterns do too unless the theme author deliberately writes placeholders. Our owner would otherwise see a client's name or an old price inside a "design". Default to design-only save.
   https://www.temperstack.com/learn/squarespace/save-reusable-sections/ · https://kinsta.com/blog/block-themes-internationalization/
6. **Silent propagation of breaking changes.** Figma: "modifying component resets overrides on instances". Webflow solved this with an explicit changelog + accept step. Pin versions on instances; upgrade deliberately.
   https://forum.figma.com/archive-21/modifying-component-resets-overrides-on-instances-of-that-component-24126 · https://university.webflow.com/lesson/libraries
7. **Changing the storage format under live pages.** Divi 5's migrator produced documented regressions (font resets vs presets, menu colours, icon placement) and needed a compatibility layer. Decide the preset record shape carefully now; add fields, do not rename them.
   https://www.elegantthemes.com/blog/divi-news/divi-5-migration · https://docs.respira.press/docs/troubleshooting/divi-5
8. **Dropping a feature instead of deprecating it.** Elementor V4 removed Global Widgets; users report broken sites and "a step back". Deprecate with a replacement pointer and keep rendering.
   https://theplusaddons.com/blog/disable-elementor-atomic-editor/ · https://roadmap.wdesignkit.com/boards/feature-requests/posts/global-widget
9. **Unbounded library growth / legacy sprawl.** Figma teams end up with "a dozen legacy versions" of a library because nothing distinguishes a new version from a new thing. Force the "new version vs sibling" decision in the save-back flow and show lineage.
   https://forum.figma.com/ask-the-community-7/managing-legacy-libraries-of-a-design-system-14295
10. **Stale static thumbnails.** A stored PNG shows the old palette after a theme change; WordPress's live iframe at `viewportWidth` does not. For a non-technical owner the thumbnail *is* the contract — render it live.
    https://developer.wordpress.org/block-editor/reference-guides/block-api/block-patterns/
11. **Hard caps and excluded element types.** Squarespace caps at 50/250 saves; Wix cannot save sections containing forms, galleries or apps. If our forms/maps/LINE buttons cannot be presets, the library has holes exactly where an accounting site converts.
    https://beyondspace.studio/blog/squarespace-saved-sections-new-account-wide-feature · https://support.wix.com/en/article/studio-editor-saving-and-reusing-design-assets
12. **Jargon in the owner's UI.** Every product uses a different word for the same thing (component / pattern / global widget / asset / preset). Pick the vocabulary in 3.1 and use it everywhere, including file names.

---

## 5. Open questions

1. **Where does the library live in a static GitHub Pages site?** Presets as JSON files + HTML partials in the repo (like `en/posts/articles.json`), rendered by a small loader like `core/article-loader.js`? Or pre-rendered at build time so pages stay plain HTML? This decides whether "live preview" is possible in a picker without a server.
2. **Who performs the save-back?** The owner in a UI, or Claude/the designer via a documented procedure in the repo? The strip step and token check are easy to enforce in a script, hard to enforce by hand.
3. **How many allowed overrides are enough?** Start with text, image, alignment, colour mode, item count — and measure how often a "detach" request still appears.
4. **Version pinning vs static output.** If pages are plain HTML, "an instance pins v3" means the v3 markup is already baked into the page; upgrading = regenerating that section. Is a `data-preset="hero-split@3"` marker on each section enough for the usage index?
5. **Thai placeholders**: who writes them, and do we need Thai-specific constraints (heading length, line-height) per preset before Thai launch?
6. **Preview rendering without a backend**: iframe-scaled live render of the real section markup is feasible in a static picker page; confirm it works at phone width and with the Instrument Serif / Inter webfonts loaded.
7. **Token source of truth**: keep `theme/theme.css` as the canonical token list, or introduce a DTCG JSON file that generates `theme.css`? The JSON gives us `$deprecated` and aliases; the CSS alone does not.
8. **Deprecation policy wording** for the owner: how long does a deprecated preset stay before we propose upgrading pages — "until you say so" (safe) or "we review every tax season"?
9. **Unverified items to confirm against primary docs** (sandbox blocked them): Squarespace picker preview mechanism; Wix asset thumbnail mechanism; exact Elementor V4 status of Global Widgets; whether Framer Localization applies to component variables per instance.
