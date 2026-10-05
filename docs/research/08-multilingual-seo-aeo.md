# 08 — Multilingual SEO / AEO for a trilingual (EN · TH · ZH) static site on GitHub Pages

**Wayfinder ticket:** GitHub issue #8
**Research date:** 5 October 2026
**Status:** Research complete → feeds the Site Builder acceptance criteria (section 3) and the Admin field list (section 4)
**Scope:** URL structure, hreflang, sitemaps, canonical, `lang`, JSON-LD per locale, Open Graph / Twitter, robots.txt, Baidu, Thai search behaviour, answer-engine (AEO) readiness, and what the Builder must generate vs. ask the owner.

> **Access note.** The network sandbox used for this research blocks `developers.google.com`, `schema.org`, `docs.github.com`, `platform.openai.com` and `llmstxt.org` directly. Facts attributed to those pages were confirmed through search-engine snippets of the pages themselves plus secondary sources that quote them, and the original URLs are cited so the Builder/owner can verify. Where a point rests only on secondary sources, it is marked **(secondary)**.

---

## 1. สรุปภาษาไทย (10 บรรทัด)

1. ใช้โครงสร้างโฟลเดอร์ `/en/` `/th/` `/zh/` ตามที่ทำอยู่ — Google ยอมรับโฟลเดอร์ย่อยเป็นวิธีมาตรฐาน และเป็นวิธีเดียวที่เป็นไปได้บน GitHub Pages ฟรี
2. หน้าแรกสุด (root) เป็นหน้า "เลือกภาษา" เบา ๆ ที่เปลี่ยนเส้นทางไป `/en/` และประกาศเป็น `hreflang="x-default"` — อย่าให้ Google เห็น root เป็นหน้าแยกต่างหาก
3. รหัสภาษาที่ล็อก: `en`, `th`, `zh-Hans` (จีนตัวย่อ ไม่ผูกประเทศ) และ `x-default` → ชี้ไปหน้า root/EN; ต้องมีลิงก์ย้อนกลับครบทุกคู่ และต้องชี้ไปหน้าที่แปลแล้วจริงเท่านั้น
4. ใส่ `hreflang` **ทั้ง** ใน `<head>` และใน sitemap (xhtml:link) — ฝั่งหนึ่งผิดอีกฝั่งยังช่วยได้ และ Bing/Baidu ไม่อ่าน hreflang จึงต้องมี `<meta http-equiv="content-language">` ด้วย
5. Canonical ของทุกหน้าชี้ไป **ตัวเอง** (ภาษาเดียวกัน) ห้ามชี้ข้ามภาษา; ใช้ URL เต็ม (absolute) เสมอ
6. JSON-LD: ประกาศบริษัทเป็น `AccountingService` (ลูกของ LocalBusiness) หนึ่งตัวตน `@id` เดียวทั้งสามภาษา เปลี่ยนแค่ `name`/`description`/`inLanguage`; บทความใช้ `Article` + `BreadcrumbList`; `FAQPage` ใส่ได้แต่ไม่คาดหวัง rich result; `SearchAction` เลิกใช้แล้ว
7. Open Graph แยกต่อภาษา: `og:locale` = `en_US` / `th_TH` / `zh_CN` และใส่ `og:locale:alternate` อีกสองตัว + รูป 1200×630 ทุกหน้า
8. **Baidu ไม่สามารถเก็บหน้า github.io ได้จริงในตอนนี้** — GitHub Pages ส่ง 403 ให้ Baiduspider; ต้องมีโดเมนของตัวเอง + CDN (Cloudflare) หรือโฮสต์เวอร์ชันจีนบนที่อื่น จึงจัดเป็น "เฟส 2"
9. คนไทยใช้ Google เกือบ 98% ค้นแบบผสมไทย-อังกฤษ ไม่เว้นวรรค และใช้มือถือเป็นหลัก → หน้าไทยต้องเขียนด้วยคำที่คนค้นจริง (เช่น "รับทำบัญชี", "จดทะเบียนบริษัท") ไม่ใช่แปลตรงจากอังกฤษ
10. AEO: ไม่ต้องทำไฟล์พิเศษ (`llms.txt` ยังไม่มี AI ตัวไหนใช้) — สิ่งที่ได้ผลคือ **อย่าบล็อก** bot ของ OpenAI/Anthropic/Perplexity/Google ใน robots.txt, เขียนย่อหน้าแรกตอบคำถามตรง ๆ, มีหัวข้อคำถาม-คำตอบชัด, และ JSON-LD ต้องอยู่ใน HTML ตั้งแต่ต้น ไม่ใช่ใส่ด้วย JavaScript ทีหลัง

---

## 2. Decisions — one recommendation per item, with sources

### 2.1 URL structure: `/en/` `/th/` `/zh/` subfolders

**Decision: subdirectories per language, locked as `/en/`, `/th/`, `/zh/`. Rename the planned `/cn/` folder to `/zh/` before anything is published there.**

- Google lists four options (ccTLD, subdomain, subdirectory, URL parameter) and treats subdirectories as fully acceptable: easy setup, one host, one Search Console property, shared authority. ccTLDs are the strongest geo signal but are irrelevant here (the audience is language-based, not country-based, and the firm cannot run `.cn`). Source: Google, *Managing multi-regional and multilingual sites* — https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites
- On GitHub Pages a project site is only ever one host under one path, so subdirectories are the only option anyway; a future custom domain keeps the same folder structure, which means **no URL migration later** (only the host part of every absolute URL changes).
- Folder name: `/zh/` (language code), not `/cn/` (country code). The hreflang code is `zh-Hans`; the folder is a URL convention and should follow the language, so a future Traditional Chinese version could be `/zh-hant/` without ambiguity. `/cn/` would imply mainland-China targeting the firm is not actually doing. The current files (`index.html`, `en/index.html`, `article-template.html`) all say `/cn/` — see section 5.
- Use lowercase, ASCII, hyphenated slugs in all three languages. Thai and Chinese **page slugs stay in Latin script** (e.g. `/th/posts/vat-registration-thailand.html`), because (a) one slug per article keeps the manifest simple and the hreflang pairing automatic, and (b) percent-encoded Thai/Chinese URLs are unreadable when shared and break easily in copy-paste. Google can index Unicode URLs, but there is no ranking gain that justifies the operational cost here. **(secondary; standard practitioner consensus)**
- Same filename across languages is a hard rule: `/en/X.html` ↔ `/th/X.html` ↔ `/zh/X.html`. This is what lets the Builder generate hreflang, sitemaps and language switchers mechanically.

### 2.2 Which language at the root, and `x-default`

**Decision: the root `/` stays a tiny redirect/language-chooser page that sends people to `/en/`, and it is declared as `hreflang="x-default"` from every language set. English is the default language.**

- Google: x-default "was designed for language selector pages" and the root homepage should redirect to the appropriate version **and** be listed as x-default, otherwise Google may treat the root as a separate page from the language homepages. Sources: Google blog *x-default hreflang for international pages* (2013) — https://developers.google.com/search/blog/2013/04/x-default-hreflang-for-international-pages ; summarised with Mueller follow-ups at https://searchenginejournal.com/how-googles-hreflang-x-default-enhances-website-navigation/486568
- Google explicitly discourages redirecting by IP or `Accept-Language` because Googlebot crawls mostly from the US and would only ever see one version. Source: *Managing multi-regional sites* (link above), section "Use locale-specific URLs… avoid automatic redirection".
- Therefore: **keep the root redirect to `/en/` but make it a real page** (it already has a `<noscript>` fallback with a link). Add visible links to all three languages in the root page body so it genuinely is a chooser, keep `meta refresh` to `/en/`, and remove the `<link rel="canonical" href="./en/">` (relative canonical pointing to a different page is wrong; the root should either be x-default-only with no canonical, or self-canonical). Do **not** add browser-language auto-detection JavaScript later.
- Because x-default must be one URL, and the root redirect only exists for the homepage, **for every non-homepage page x-default points at the English version** (`/en/knowledge.html`, `/en/posts/slug.html`). That is the normal pattern when there is no neutral page.

### 2.3 hreflang: HTML head vs. sitemap, and the exact codes

**Decision: emit hreflang in BOTH the `<head>` and the sitemap. Codes: `en`, `th`, `zh-Hans`, `x-default`. Only emit a link when the translated page actually exists.**

Rules the Builder must enforce (all from Google's *Tell Google about localized versions of your page* — https://developers.google.com/search/docs/specialty/international/localized-versions):
- Every page in a set lists **every** version, **including itself** (self-reference).
- Links must be **reciprocal** ("return links"); a one-sided link is ignored.
- URLs must be **absolute** (`https://…`), including the host/path of the GitHub project site.
- Value = ISO 639-1 language, optionally + ISO 3166-1 alpha-2 region. A region alone is invalid.
- Pages that are blocked by robots.txt or `noindex` must not appear in a set.
- Three equivalent delivery methods: HTML `<link rel="alternate" hreflang>`, HTTP header, or sitemap `<xhtml:link>`. We cannot set headers on GitHub Pages, so head + sitemap it is.

Why both head and sitemap: the head is what crawlers see first and what AEO fetchers and link-preview tools read; the sitemap is the cheapest place to keep the whole matrix correct in one file and is generated anyway. Doing both costs nothing when generated by a script and makes one mistake non-fatal. Google processes either source; conflicts are resolved by ignoring the inconsistent pair, so the generator must build both from the **same** language matrix.

**Chinese code — `zh-Hans`, not `zh-CN`, not bare `zh`:**
- `zh-CN` means "Chinese as used in mainland China" (region); `zh-Hans` means "Simplified-script Chinese wherever used" (script). BCP 47 / W3C recommend the script subtag for Chinese because the real difference users care about is the script. Sources: W3C/BCP47 discussion summarised at https://flyrank.com/blogs/seo-hub/how-to-handle-hreflang-for-languages-with-multiple-scripts-e-g-chinese-simplified-vs-traditional ; Microsoft/Optimizely locale guidance ("zh-CN is an old name and should be avoided") https://world.optimizely.com/forum/developer-forum/CMS/Thread-Container/2018/11/zh-hans-or-zh-cn-for-simplified-chinese
- Google's own product documentation lists `zh-Hans` and `zh-Hant` as supported language values (Programmable Search Engine) — https://developers.google.cn/custom-search/docs/ref_languages?hl=en — and the hreflang page's format rule is "language in ISO 639-1 optionally with region" without explicitly listing scripts. Practitioner consensus is that Google accepts `zh-Hans`/`zh-Hant`; Search Console's hreflang report will confirm within weeks of launch. **If Search Console flags `zh-Hans` as unknown (unlikely), fall back to `zh-CN` and open an issue.** Also decide the fallback now so the Builder has one switch, not a rewrite.
- Bare `zh` is valid but ambiguous (Simplified vs Traditional); the firm's audience includes Mainland, Singapore and Malaysia readers (Simplified) and could later include Taiwan/HK (Traditional), so the script subtag is the right level of precision.
- Correspondingly `<html lang="zh-Hans">`, `og:locale` `zh_CN` (Open Graph uses the Facebook-locale format, which has no script form — see 2.8), and `inLanguage: "zh-Hans"` in JSON-LD.

**Thai code: `th`** — one script, one country; `th-TH` adds nothing and would wrongly exclude Thai speakers abroad.

**English code: `en`** — the audience (UK, US, Japan-based foreign founders) is global; do not use `en-US`/`en-GB`.

**Bing and Baidu do not use hreflang.** Bing relies on `<meta http-equiv="content-language" content="th">` (and content), Baidu the same plus page content. Sources: Bing guidance quoted at https://technicalseo.com/tools/pages/docs/hreflang.html ; https://woorank.com/en/edu/seo-guides/best-practices-for-language-declaration ; Baidu at https://www.chinafy.com/blog/how-to-create-a-multilingual-website-that-ranks-on-baidu . So every page also gets `<meta http-equiv="content-language" content="en|th|zh-Hans">` (Baidu examples use `zh-CN`; this is the one place where emitting `zh-CN` is harmless and Baidu-friendly — see 2.10).

### 2.4 Sitemaps: per-language sitemaps + a sitemap index

**Decision: one sitemap per language (`/sitemap-en.xml`, `/sitemap-th.xml`, `/sitemap-zh.xml`), each carrying the full hreflang matrix via `xhtml:link`, plus `/sitemap.xml` as a sitemap index listing the three. Submit `/sitemap.xml` in Google Search Console and Bing Webmaster Tools.**

- A sitemap may hold up to 50,000 URLs / 50 MB, and a sitemap index may list multiple sitemaps; splitting by any logic you like (e.g. per language or per content type) is allowed and is a common way to read indexing coverage per segment in Search Console. Source: Google, *Manage your sitemaps using sitemap index files* — https://developers.google.com/search/docs/crawling-indexing/sitemaps/large-sitemaps
- A sitemap can only describe URLs **at or below its own path**. On the project site the sitemap lives at `https://phuwanutkhodop.github.io/accountingsite.github.io/sitemap.xml`, which covers everything under `/accountingsite.github.io/` — correct. Search Console property: add as a **URL-prefix** property `https://phuwanutkhodop.github.io/accountingsite.github.io/` (a Domain property is impossible — the owner does not control `github.io`). Source: Search Console sitemap/property model — https://developers.google.com/webmaster-tools/v1/sitemaps/submit
- Each `<url>` entry: `<loc>`, `<lastmod>` (ISO date, from the manifest `date`/`dateModified`), and one `<xhtml:link rel="alternate" hreflang="…">` per language version **plus x-default**. Google ignores `<changefreq>` and `<priority>`, so omit them. Source: Google *Build and submit a sitemap* — https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap
- Sitemap hreflang example format (from Google's localized-versions page):
  ```xml
  <url>
    <loc>https://HOST/BASE/en/posts/vat-registration-thailand.html</loc>
    <lastmod>2026-03-28</lastmod>
    <xhtml:link rel="alternate" hreflang="en" href="https://HOST/BASE/en/posts/vat-registration-thailand.html"/>
    <xhtml:link rel="alternate" hreflang="th" href="https://HOST/BASE/th/posts/vat-registration-thailand.html"/>
    <xhtml:link rel="alternate" hreflang="zh-Hans" href="https://HOST/BASE/zh/posts/vat-registration-thailand.html"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="https://HOST/BASE/en/posts/vat-registration-thailand.html"/>
  </url>
  ```
- Add `Sitemap: https://HOST/BASE/sitemap.xml` to robots.txt **only if the robots.txt is actually at the host root** (see 2.9). On the bare project site this line cannot be served; rely on Search Console / Bing submission instead.
- Bing: additionally wire **IndexNow** (free, a single key file at the site root + a POST on publish). It gives Bing/Copilot and Yandex near-instant indexing; Google does not use it. Source: https://www.bing.com/indexnow/getstarted . Optional for v1; cheap win later because the Builder already knows which URLs changed.

### 2.5 Canonical rules across languages

**Decision: every page carries exactly one absolute, self-referencing canonical to its own URL in its own language. Never canonicalise TH or ZH to EN. Never emit a relative canonical.**

- Google: hreflang alternates are different pages, not duplicates; canonical must be self-referencing per language version, and canonicalising translated pages to one language would de-index the translations. Source: *Localized versions* page (link above) and *Consolidate duplicate URLs* — https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls
- The canonical URL must be the **final** URL with no trailing-slash/`index.html` ambiguity. GitHub Pages serves `/en/` and `/en/index.html` as the same content; pick `/en/` (directory form) for homepages and `/en/knowledge.html` for files, and use the same form everywhere (canonical, og:url, hreflang, sitemap, JSON-LD `url`/`@id`). Mixed forms are the most common hreflang-mismatch bug.
- When the custom domain arrives: canonical, hreflang, og:url, sitemap and JSON-LD all switch to the new host **in one generated pass**; the old github.io URLs keep serving (GitHub does this automatically) and their canonical then points to the custom domain, which is the correct way to consolidate the two hosts. Source: GitHub custom-domain behaviour — https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/about-custom-domains-and-github-pages ; canonical-over-blocking advice **(secondary)** https://discourse.gohugo.io/t/canonical-url-for-domain-name-and-backup-site/52900
- The root chooser page: drop `rel="canonical"`; it is identified only by x-default. (A canonical to `/en/` would also work for Google but contradicts the "root is a distinct chooser page" model; pick one — the recommendation is no canonical.)

### 2.6 `lang` attributes

**Decision: `<html lang="en">`, `<html lang="th">`, `<html lang="zh-Hans">`; plus `lang="…"` on any inline foreign-language span (e.g. Thai legal terms inside an English article), plus `<meta http-equiv="content-language">` for Bing/Baidu.**

- Google ignores `lang` for language detection (Mueller, Sept 2023: "Google Search does not use the HTML lang tag… tries to understand the primary language from the actual content"), so the attribute is for **accessibility (screen readers), browsers (font selection, hyphenation, quotes), Bing and Baidu**, not Google ranking. Source summary: https://www.searchenginejournal.com/google-uses-different-algorithms-for-different-languages/434227/ ; https://woorank.com/en/edu/seo-guides/best-practices-for-language-declaration
- Practical consequence: one primary language per page; do not mix Thai and English body text on the same URL beyond short terms. Google: "best to have a primary language on a page and not mix languages" — https://searchengineland.com/google-best-to-have-a-primary-language-one-a-page-and-not-mix-languages-387721
- Thai pages also need `lang="th"` for correct line-breaking (browsers apply Thai word-segmentation dictionaries only when the language is declared) — this is a readability issue, not just SEO.

### 2.7 JSON-LD per locale for an accounting firm

**Decision summary**

| Page | Primary type | Also | Notes |
|---|---|---|---|
| Homepage (each language) | `AccountingService` (one entity, same `@id` in all three languages) | `WebSite` (one per language, `inLanguage` set), **no** `SearchAction` | AccountingService ⊂ FinancialService ⊂ LocalBusiness ⊂ Organization. |
| Services page | `Service` list (`OfferCatalog` optional) with `provider` → `@id` of the firm | `BreadcrumbList` | |
| About / Team | `AboutPage` + `Person` per partner (with `worksFor` → firm `@id`) | `BreadcrumbList` | Persons help E-E-A-T and AI attribution. |
| Contact | `ContactPage` | `BreadcrumbList` | Contact details live on the AccountingService node, not here. |
| Knowledge index | `CollectionPage` + `ItemList` of `Article` | `BreadcrumbList` | Already built; move from JS to static. |
| Article | `Article` (or `BlogPosting`) with `author` Person/Organization, `publisher` → firm `@id`, `datePublished`, `dateModified`, `image`, `inLanguage`, `mainEntityOfPage` | `BreadcrumbList`; `FAQPage` only when the article has a real Q&A block | |
| Privacy / Terms | `WebPage` (`PrivacyPolicy` / `TermsOfService` are not schema.org types — see 5) | | |

Rationale and sources:
- **LocalBusiness vs Organization vs ProfessionalService vs AccountingService.** Google's LocalBusiness rich-result documentation asks for the *most specific* LocalBusiness subtype; `AccountingService` is a schema.org type (FinancialService → LocalBusiness). `ProfessionalService` exists but schema.org marks it as a legacy catch-all that should be replaced by the specific subtype where one exists. Required for Google: `name`, `address` (PostalAddress). Recommended: `url`, `telephone`, `geo`, `openingHoursSpecification`, `priceRange`, `image`, `sameAs`, `aggregateRating` (only with real reviews). Sources: Google LocalBusiness — https://developers.google.com/search/docs/appearance/structured-data/local-business ; schema.org — https://schema.org/AccountingService , https://schema.org/ProfessionalService ; summary https://yoast.com/local-business-listings/
  Because the firm serves clients remotely (foreign founders) **and** has a Bangkok office, `AccountingService` with `areaServed` (`Country: TH` plus the client countries) captures both. Add `knowsLanguage: ["en","th","zh-Hans"]` — cheap and directly relevant to the trilingual proposition.
- **One entity, three languages.** Use a stable `@id` (e.g. `https://HOST/BASE/#organization`, host-neutral path so it survives the domain change) on every page in every language, and vary only the language-bearing strings (`name` if the firm has a Thai/Chinese legal name, `description`, `slogan`, `address` locality spelling) plus `inLanguage` on the page-level node. Link versions with `sameAs` to the firm's Google Business Profile, LinkedIn, Facebook, DBD registration page, Line Official, WeChat (as a URL where one exists). Sources: schema.org guidance on `inLanguage` / `sameAs` for multilingual entities **(secondary)** — https://multilipi.com/blog/guide-multilingual-schema-markup ; https://www.linguise.com/blog/guide/using-schema-markup-and-structured-data-for-multilingual-websites-seo/
  JSON-LD technically supports `{"@value": "...", "@language": "th"}` language maps, but Google's parsers do not act on them for rich results; **emit plain strings in the page's language** instead and keep the shared `@id`. Simpler, and it is what every validator expects.
- **Article.** Google: `headline` (≤110 chars) is the only strictly required field; `image`, `author` (Person or Organization, not a string), `datePublished`, `dateModified`, `publisher` with `logo` are "recommended" but in practice gate rich results. Source: https://developers.google.com/search/docs/appearance/structured-data/article . The current loader has no `image`, no `dateModified`, no `publisher.logo` → section 5.
- **BreadcrumbList.** Supported rich result, trivially generated from the folder structure (`Home › Insights › Article`), and helpful for both Google and AI engines to understand site sections. Source: https://developers.google.com/search/docs/appearance/structured-data/breadcrumb
- **FAQPage.** Since August 2023 Google shows FAQ rich results only for "well-known, authoritative government and health websites"; the markup is still *processed* and Google said there is no need to remove it. Source: https://developers.google.com/search/blog/2023/08/howto-faq-changes . Decision: emit `FAQPage` only when a page has a genuine visible Q&A block (it is also a clean format for answer engines), never as a bolt-on, and never for marketing fluff.
- **WebSite + SearchAction.** The Sitelinks Search Box was deprecated 21 Nov 2024; the `SearchAction` markup is dead weight (harmless but pointless, and our search is client-side filtering only). Keep `WebSite` for the *site name* feature (Google still uses `WebSite.name`/`alternateName`). Sources: https://ppc.land/google-to-remove-sitelinks-search-box/ ; https://www.queryclick.com/blog/google-deprecates-sitelink-search-box/
- **Static, not JavaScript-injected.** Google does render JS and does read JSON-LD injected after fetch (it documents this pattern), but (a) it depends on the second-wave render and (b) **most AI crawlers and link-preview fetchers do not execute JavaScript**. Current `article-loader.js` injects the ItemList at runtime — fine as a Google fallback, wrong as the primary mechanism. Sources: Google *Generate structured data with JavaScript* — https://developers.google.com/search/docs/appearance/structured-data/generate-structured-data-with-javascript ; caveat discussion https://www.bump.it.com/blog/client-injected-json-ld . **Decision: the Builder writes all JSON-LD statically into each HTML file at generation time; the runtime injector becomes redundant for pages the Builder generates.**
- **Does schema still matter for AI citations?** An Ahrefs study (May 2026; 1,885 treated pages vs 4,000 controls) found adding JSON-LD produced no measurable citation uplift in AI Overviews, AI Mode or ChatGPT. Other vendor studies claim 2× uplift. Treat schema as **hygiene + disambiguation**, not a growth lever; the content structure (2.11) is what moves citations. Sources: https://www.seroundtable.com/study-schema-citations-study-41311.html ; counter-claims (vendor) https://mikekhorev.com/google-ai-overview

### 2.8 Open Graph / Twitter per language

**Decision: every page in every language carries a full, translated OG + Twitter set, generated by the Builder, with a 1200×630 share image.**

- `og:locale` uses Facebook's `ll_CC` format: `en_US`, `th_TH`, `zh_CN` (Facebook has no `zh_Hans`; `zh_CN` is the Simplified locale, `zh_TW`/`zh_HK` Traditional). Each page also lists the other two as `og:locale:alternate`. Source: OGP spec https://ogp.me/#optional ; multilingual practice https://dev.to/lingodotdev/the-i18n-seo-checklist-15-seo-optimization-techniques-to-reach-a-global-audience-59l0
- `og:url` must equal the canonical. `og:title`, `og:description`, `og:site_name` are translated. `og:type` = `website` for pages, `article` for posts; for articles also `article:published_time`, `article:modified_time`, `article:author`, `article:section`, `article:tag`.
- `og:image` is **required in practice** for LinkedIn, WhatsApp, Line, WeChat and Facebook previews — the three channels this firm's clients actually use (Line for Thai, WeChat for Chinese, LinkedIn/WhatsApp for foreign founders). Absolute URL, 1200×630, ≤ 1 MB, plus `og:image:width/height/alt`. One default site image generated from the brand palette (navy + linen, firm name) is enough for v1; per-article images optional. **Images with embedded text must be per language** or text-free.
- Twitter/X: `twitter:card=summary_large_image`, `twitter:title`, `twitter:description`, `twitter:image` (falls back to og:image but set it explicitly; some parsers need it).
- Line (dominant in Thailand) and WeChat read standard OG tags; WeChat additionally prefers a square image ≥300×300 — optional second image, out of scope v1.

### 2.9 robots.txt

**Decision: allow everything (including AI crawlers), block nothing but the obvious; ship a robots.txt now at the repo root for the custom-domain future, and understand it is inert on the bare project site.**

- **Hard constraint:** robots.txt is only read at the host root (`https://phuwanutkhodop.github.io/robots.txt`). A file at `/accountingsite.github.io/robots.txt` is ignored by every crawler. To control crawling on the project site today the owner would need a *user site* repo named `phuwanutkhodop.github.io` with the robots.txt in it — do not do this just for robots. Source: GitHub community thread — https://github.com/orgs/community/discussions/64865 ; robots.txt standard (RFC 9309) root-only rule.
- Consequence: **on the bare project site the default is "everything allowed", which is exactly what we want.** The Builder still writes `/robots.txt` into the repo so that the moment a custom domain is attached it becomes live with the right content.
- Content:
  ```
  User-agent: *
  Allow: /
  Disallow: /docs/
  Disallow: /admin/        # if the Admin UI is ever published in the same repo

  Sitemap: https://HOST/BASE/sitemap.xml
  ```
  Explicit per-bot `Allow` lines are unnecessary (no `Disallow` = allowed) but the Builder may add a commented block listing the AI agents **deliberately not blocked** (`GPTBot`, `OAI-SearchBot`, `ChatGPT-User`, `ClaudeBot`, `Claude-SearchBot`, `Claude-User`, `PerplexityBot`, `Perplexity-User`, `Google-Extended`, `Applebot-Extended`, `Bingbot`, `Baiduspider`) so a future editor does not "clean up" by blocking them.
- Why not block training bots (`GPTBot`, `ClaudeBot`, `Google-Extended`)? For a marketing site the goal is to be *known* by the models; blocking training has no SEO benefit and reduces the chance the firm is recommended in zero-click answers. `Google-Extended` does **not** affect Search, AI Overviews or AI Mode (those ride Googlebot), only Gemini training/grounding. Sources: Google crawler docs — https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers ; summary https://ppc.land/google-extended/ ; Anthropic (updated 7 Apr 2026) — https://support.claude.com/en/articles/8896518-what-is-claudebot ; OpenAI — https://platform.openai.com/docs/bots ; crawler list https://www.searchenginejournal.com/ai-crawler-user-agents-list/558130/
- Do **not** `Disallow` the `/th/` or `/zh/` folders while they are "dormant"; instead do not generate/link them until content exists. A blocked URL inside an hreflang set invalidates the set.

### 2.10 Baidu and the Chinese version

**Decision: the `/zh/` version is built for Google (overseas Chinese, Singapore/Malaysia, Mainland users on VPN/Bing) and for AI engines; Baidu indexing is a documented Phase-2 item that requires a custom domain + CDN, and the Builder prepares the on-page parts now.**

Is Baidu indexing of a github.io site realistic? **No, not today.**
- GitHub Pages returns **HTTP 403 to Baiduspider**; the community request to allow it (31 Dec 2024) has no GitHub response as of this research. Source: https://github.com/orgs/community/discussions/148249
- Even with a custom domain the request still hits GitHub's origin; the workaround people report is a CDN (Cloudflare) with aggressive caching so most Baidu requests are served from cache without reaching GitHub — but Cloudflare's own bot rules can also 403 Baiduspider unless configured. Sources: https://github.com/tari-project/tari-dot-com/issues/120 ; https://community.cloudflare.com/t/baiduspider-from-cloudflare-ip/88727
- Cleaner Phase-2 option: deploy the same repo to **Cloudflare Pages** (free, no Baidu block, CNAME support) and point the custom domain there; GitHub stays the source of truth. Source: https://www.chengxiaobai.com/en/trouble-maker/build-and-host-hexo-site-with-cloudflare-pages.html
- Baidu accepts sites hosted outside China without an ICP licence, but ranks slower-loading foreign-hosted sites worse; Hong Kong/Singapore edge hosting helps. ICP filing is only required for servers physically in the Mainland. Sources: https://seosherpa.com/baidu-seo/ ; https://intl.aliyun.com/icp ; https://chinafy.com/blog/how-to-index-your-site-on-baidu-in-2024

What helps on-page (Builder can do now, costs nothing):
- Simplified Chinese written natively (not machine-translated), `<html lang="zh-Hans">`, `<meta http-equiv="content-language" content="zh-CN">` (Baidu's convention), `<meta charset="UTF-8">`, descriptive `<title>` with the firm's Chinese name, `<meta name="description">` in Chinese, `<meta name="keywords">` (Baidu still reads it; Google ignores it — harmless).
- Baidu does **not** support hreflang; it does respect canonical "mostly" but will ignore all canonicals site-wide if it finds them misused — one more reason canonicals must be perfectly self-referencing. Source: https://www.chinafy.com/blog/how-to-create-a-multilingual-website-that-ranks-on-baidu ; https://www.advance-metrics.com/en/blog/baidu-seo-guide/
- Avoid Google Fonts on `/zh/` pages (fonts.googleapis.com is blocked in the Mainland → pages render late/unstyled). Load Inter/Instrument Serif self-hosted or use `font-display: swap` with a system-font fallback for `/zh/`. Same for any Google Analytics/Tag Manager script — use a China-reachable analytics or none on `/zh/`. **(Project rule "no new fonts" is unaffected: same fonts, different delivery.)**
- Baidu Webmaster (ziyuan.baidu.com) verification meta tag `baidu-site-verification`, sitemap submission, and the active push API (`data.zz.baidu.com/urls`) are Phase-2 items once a Baidu-reachable host exists. Baidu site registration is domain/host-level; whether a path-level site under `github.io` would even be accepted is unverified (open question 6.3). Sources: https://www.theegg.com/seo/china/verifying-your-site-for-baidu-webmaster-tools ; https://en.anqicms.com/blog/4321.html
- Where Chinese prospects actually look for a Thai accounting firm: Baidu, but also **WeChat search, Xiaohongshu, Zhihu and Bing China**. The Chinese page should therefore also be shareable into WeChat (OG tags, square image) — which the Builder already covers.

### 2.11 Thai-specific search behaviour

- Google ≈ 97–98% of Thai search; Bing < 0.5%. Mobile > 90% of searches. Sources: https://gs.statcounter.com/search-engine-market-share/2025-12/thailand ; https://www.relevantaudience.com/the-ultimate-guide-to-seo-in-bangkok-for-2025
- Thai is written without spaces; tokenisation is imperfect, so keyword tools **understate** Thai volumes and Thai long-tail competition is thin. Searchers mix Thai and English in one query ("จดทะเบียนบริษัท BOI", "ทำบัญชี startup") and transliterate brand/terms several ways. Sources: https://www.relevantaudience.com/seo/long-tail-keywords-guide/ ; https://www.ranktracker.com/blog/a-complete-guide-for-doing-seo-in-thai/
- Implications for the Builder/owner:
  1. Thai `<title>`/`<h1>` must use the **search phrasing**, not a translation of the English title: e.g. "รับทำบัญชี บริษัทต่างชาติ", "จดทะเบียนบริษัท ต่างชาติถือหุ้น", "ขอใบอนุญาตทำงาน", "ยื่นภาษี ภ.ง.ด.50", "VAT ภ.พ.30". The Admin should ask for a **Thai title and Thai description separately**, never auto-translate.
  2. Keep the official Thai form names and their abbreviations (ภ.ง.ด., ภ.พ.30, สปส.) in body text — they are what Thai accountants and business owners type.
  3. Thai consumers weight Thai-language reviews and Google Business Profile map presence heavily (Bangkok local-intent); the `AccountingService` node with `address`, `geo`, `openingHours` and `sameAs` → Google Business Profile is the on-site half of that. The off-site half (claiming the GBP, collecting Thai reviews) is an owner task, not a Builder task.
  4. Thai body text: declare `lang="th"`, avoid justified text, allow long line length; Instrument Serif has no Thai glyphs, so the heading font for `/th/` falls back to the system Thai font — flag as a **design question**, not an SEO one (section 6).

### 2.12 AEO / answer-engine readiness

What the LLM-side crawlers actually do:
- **OpenAI:** `GPTBot` (training), `OAI-SearchBot` (indexes for ChatGPT search/citations), `ChatGPT-User` (fetches when a user asks). **Anthropic:** `ClaudeBot` (training), `Claude-SearchBot` (search index), `Claude-User` (user-triggered). **Perplexity:** `PerplexityBot` (index), `Perplexity-User` (user-triggered; Perplexity says this one is not bound by robots.txt). **Google:** Googlebot feeds Search + AI Overviews + AI Mode; `Google-Extended` only gates Gemini training/grounding. **Apple:** `Applebot` indexes, `Applebot-Extended` gates training. Sources: Anthropic https://support.claude.com/en/articles/8896518-what-is-claudebot ; OpenAI https://platform.openai.com/docs/bots ; list https://www.searchenginejournal.com/ai-crawler-user-agents-list/558130/ ; Perplexity behaviour https://geotoolbox.ai/blog/ai-crawlers
- They read the **served HTML**. Most do not execute JavaScript. They read `<title>`, meta description, headings, body text, and JSON-LD *that is in the HTML*. This is the single strongest argument for the Builder writing complete static pages (and static JSON-LD) rather than relying on `article-loader.js`.

**llms.txt — decision: do not build it in v1; revisit in 12 months.**
- Proposal: a Markdown file at `/llms.txt` summarising the site for LLMs. Source: https://llmstxt.org/
- Google's John Mueller (June 2025): "no AI system currently uses llms.txt"; server logs confirm bots fetch pages, not the file; Google confirmed it does not support it. A file appeared in Google's own docs for one day (3 Dec 2025) and was removed. Sources: https://seroundtable.com/google-ai-llms-txt-39607.html ; https://www.searchenginejournal.com/llms-txt/ ; https://www.omnius.so/industry-updates/google-adds-llms-txt-to-docs-after-publicly-dismissing-it
- It costs ~nothing to generate from the manifest, so the Builder **may** emit it behind a flag, but it must not appear in acceptance criteria and the owner must not be told it "does" anything.

**What does move AI citations (content structure the Builder must enforce in templates):**
- Put a **direct, self-contained answer in the first paragraph** (40–70 words, declarative, no "in this article we will…"). Studies: ~44% of AI citations come from the first 30% of the text; ~41% match "a clean declarative answer near the top". Sources **(secondary, vendor studies)**: https://mikekhorev.com/google-ai-overview ; https://icoda.io/ai/strategies-for-optimizing-content-for-google-ai-overviews/
- One H1; H2s phrased as the question people ask ("Do I need to register for VAT in Thailand?"); each H2 followed immediately by a 1–3 sentence answer, then detail. This is "FAQ structure" without needing FAQPage markup.
- **Definitional paragraphs**: for every term the firm wants to own (BOI promotion, ภ.ง.ด.53, Smart Visa), one paragraph that starts "X is …" with the term in bold. Answer engines lift these verbatim.
- Facts with **dates and sources** (Revenue Department, DBD, BOI links) — LLMs prefer pages that cite primary sources; it also protects the firm when rules change.
- `dateModified` visible on page and in JSON-LD; stale-looking pages are cited less.
- Named author with credentials (Person schema + visible byline) for E-E-A-T; the firm's `AccountingService` node with real address/phone makes the entity resolvable.
- Tables for thresholds/deadlines (e.g. VAT threshold, filing calendar) — extractable and quotable.
- Thai and Chinese versions follow the same structure; AI engines answer Thai/Chinese questions from Thai/Chinese pages.

---

## 3. GENERATION CHECKLIST (acceptance criteria for the Builder)

Notation: **MUST** = acceptance blocker; **SHOULD** = ship in v1 unless impossible; **MAY** = optional flag.

### 3.1 Site-wide (once per build)

- [ ] **MUST** read one site config (`site.config.json` or equivalent) containing: `siteUrl` (host + base path, no trailing slash), `defaultLang: "en"`, `languages: ["en","th","zh"]`, hreflang map `{en:"en", th:"th", zh:"zh-Hans"}`, OG locale map `{en:"en_US", th:"th_TH", zh:"zh_CN"}`, content-language map `{en:"en", th:"th", zh:"zh-CN"}`, and the business fields from section 4.
- [ ] **MUST** derive every absolute URL from `siteUrl` + relative path; zero hard-coded hosts in templates. Changing `siteUrl` once (custom domain) regenerates everything.
- [ ] **MUST** use one URL form consistently: homepages as `/<lang>/`, all other pages as `/<lang>/<file>.html`. The same form is used in canonical, hreflang, og:url, sitemap `<loc>`, JSON-LD `url`/`@id`.
- [ ] **MUST** keep all in-page links relative (project rule) while all *metadata* URLs are absolute.
- [ ] **MUST** generate `/sitemap.xml` (index) + `/sitemap-en.xml`, `/sitemap-th.xml`, `/sitemap-zh.xml`; each `<url>` has `<loc>`, `<lastmod>` and the full `xhtml:link` hreflang set incl. `x-default`; no `changefreq`/`priority`; only URLs that exist and are indexable.
- [ ] **MUST** generate `/robots.txt` (allow all, disallow `/docs/`, `Sitemap:` line) even though it is inert until a custom domain exists; document that in a comment inside the file.
- [ ] **MUST** generate the root `/index.html` as the x-default language chooser: visible links to `/en/`, `/th/`, `/zh/` (only languages that exist), `meta refresh` → `/en/`, `<noscript>` fallback, **no** `rel=canonical`, **no** browser-language auto-detect.
- [ ] **MUST** fail the build (not silently skip) if any hreflang target file does not exist, if any page lacks a canonical, or if two pages share a canonical.
- [ ] **MUST** validate every emitted JSON-LD block is parseable JSON and every `@id` reference resolves to a node emitted somewhere on the site.
- [ ] **SHOULD** generate one default OG image (1200×630, brand palette, firm name per language) into `/assets/og/` and reference it absolutely.
- [ ] **SHOULD** emit a `/.well-known/` nothing — not needed; but emit the IndexNow key file at root and POST changed URLs on publish (MAY in v1).
- [ ] **MAY** emit `/llms.txt` from the manifest behind a config flag, default off.
- [ ] **MUST NOT** emit any `/cn/` path; the Chinese folder is `/zh/`.

### 3.2 Per page (every generated HTML file, every language)

Head, in this order:
- [ ] **MUST** `<!DOCTYPE html>` and `<html lang="en|th|zh-Hans">`.
- [ ] **MUST** `<meta charset="UTF-8">`, viewport.
- [ ] **MUST** `<title>` ≤ 60 chars, translated/authored in the page language (never machine-translated for TH; see 2.11), pattern `Page title · Firm name`.
- [ ] **MUST** `<meta name="description">` 120–160 chars in the page language.
- [ ] **MUST** `<meta http-equiv="content-language" content="en|th|zh-CN">`.
- [ ] **MUST** `<link rel="canonical" href="ABSOLUTE SELF URL">` — exactly one, self-referencing, same language.
- [ ] **MUST** `<link rel="alternate" hreflang="…">` for **each existing** language version incl. self, plus `x-default` → root `/` for homepages, → `/en/<file>` for all other pages. Omit the whole block only if the page exists in one language and never emit a link to a missing file.
- [ ] **MUST** Open Graph: `og:type`, `og:title`, `og:description`, `og:url` (= canonical), `og:site_name` (translated), `og:locale`, `og:locale:alternate` × other existing languages, `og:image` + `og:image:width/height/alt`.
- [ ] **MUST** Twitter: `twitter:card`, `twitter:title`, `twitter:description`, `twitter:image`.
- [ ] **MUST** static JSON-LD (no runtime injection as the primary source) containing at least: the shared `AccountingService` node (full on homepage/contact, `@id` reference elsewhere), the page-type node (`WebPage`/`CollectionPage`/`Article`/`AboutPage`/`ContactPage`), `BreadcrumbList` for every non-home page, `inLanguage` on the page node using the hreflang code.
- [ ] **SHOULD** `<link rel="alternate" type="application/rss+xml">` per language if a feed is generated (MAY).
- [ ] **MUST** a visible language switcher whose links go to the **same page** in the other languages (fall back to that language's homepage only when the page does not exist, and then say so).
- [ ] **MUST** `/zh/` pages do not depend on `fonts.googleapis.com` or Google scripts for first render (self-hosted or system fallback with `font-display: swap`).

Body / content rules enforced by the templates:
- [ ] **MUST** exactly one `<h1>`; H2s may be questions; first paragraph after H1 is a direct answer/summary (template placeholder says so).
- [ ] **MUST** visible publish date and modified date on articles, matching JSON-LD.
- [ ] **MUST** visible author (Person or firm) matching JSON-LD.
- [ ] **SHOULD** every page shows the firm's NAP (name, address, phone) in the footer, identical across pages and identical to the JSON-LD.

### 3.3 Per article (from `articles.json`, per language)

- [ ] **MUST** manifest schema extended with per-language blocks: `title`, `excerpt`, `eyebrow`, `keywords` for each of `en`/`th`/`zh`, plus shared `slug`, `date`, `dateModified`, `author`, `image`, `featured`. A language block missing ⇒ no page, no hreflang, no sitemap entry for that language.
- [ ] **MUST** `Article` JSON-LD with `headline` (≤110), `description`, `image` (absolute), `datePublished`, `dateModified`, `author` (Person with `url`/`jobTitle` or Organization `@id`), `publisher` → firm `@id` (which carries `logo`), `inLanguage`, `mainEntityOfPage`, `articleSection`, `keywords`, `isPartOf` → the language's `WebSite`.
- [ ] **MUST** `BreadcrumbList`: Home › Insights › Article, in the page language.
- [ ] **MAY** `FAQPage` only if the article template's optional Q&A block is filled (questions = visible H3s, answers = visible text, no hidden content).
- [ ] **MUST** article OG `og:type=article` + `article:published_time`, `article:modified_time`, `article:section`.
- [ ] **MUST** Knowledge index per language lists only articles that exist in that language; its `ItemList` JSON-LD is static.

### 3.4 On custom-domain switch (one-time)

- [ ] **MUST** change `siteUrl` only; rebuild; verify robots.txt and sitemap now resolve at the new host root; add the new host as a Search Console property; resubmit sitemap; keep the github.io host serving with canonicals pointing to the new host.

---

## 4. Owner-facing inputs the Admin must collect

Grouped so the Admin UI can present them as short forms. Fields marked (per language) need EN, TH, ZH values; the Admin must not auto-translate TH/ZH titles or descriptions silently (it may *offer* a draft clearly marked as draft).

### 4.1 Identity (once)
- Legal firm name (EN) · Thai legal name (TH) · Chinese trading name (ZH, optional)
- Short brand name / `og:site_name` (per language)
- Tagline / `slogan` (per language)
- One-paragraph description (per language, 150–300 chars) — used for homepage meta description and `AccountingService.description`
- Logo file (PNG/SVG, square ≥ 512 px) → `publisher.logo`, favicon
- Default share image (or "generate one for me") → `og:image`
- Founding year (optional)
- Company registration number (DBD) (optional → `identifier`), licences (e.g. TFAC registration) (optional)

### 4.2 Location & contact (once)
- Street address, sub-district, district, province, postal code (EN + TH spellings) → `PostalAddress`
- Latitude / longitude (or "find from address") → `geo`
- Phone (E.164, e.g. +66…) and whether WhatsApp/Line are on it
- Public email
- Line Official ID / URL, WeChat ID (as a URL where possible), WhatsApp link, LinkedIn, Facebook, Google Business Profile URL → `sameAs` + contact section
- Opening hours (per weekday) and timezone → `openingHoursSpecification`
- Price range (`฿฿`-style or "contact for quote") → `priceRange` (optional)
- Areas served: Thailand + client countries (multi-select) → `areaServed`
- Languages spoken → `knowsLanguage` (default en, th, zh)

### 4.3 People (per person, optional but recommended)
- Full name (per language), job title (per language), credentials (CPA, TA number…), headshot, LinkedIn URL, short bio → `Person`, article `author`

### 4.4 Services (per service)
- Service name (per language), one-paragraph description (per language), who it is for, optional "from ฿X" → `Service` / `OfferCatalog`

### 4.5 Site & languages (once)
- Which languages are live (EN always; TH on/off; ZH on/off) — a language turned off generates nothing and appears nowhere
- Custom domain (empty until bought) → `siteUrl`
- Google Search Console verification token, Bing verification token, Baidu verification token (optional, Phase 2)
- IndexNow key (auto-generated; owner just confirms) (optional)
- Analytics choice (none / Plausible-style China-reachable / GA4) — recommendation: none or privacy-friendly in v1

### 4.6 Per page (About, Services, Contact…)
- Page title (per language) ≤ 60 chars, meta description (per language), optional page-specific share image

### 4.7 Per article
- Slug (Latin, auto-suggested from EN title, editable, immutable after publish)
- Per language: title, excerpt (≤160 chars), eyebrow/section, keywords (3–6), body
- Date published, date modified (auto), author (pick from 4.3 or "the firm"), featured flag, optional image + alt text (per language), optional FAQ pairs (per language)

### 4.8 What the Admin must NOT ask for (Builder derives it)
canonical, hreflang, sitemap, robots.txt, og:url, og:locale, content-language, `lang`, BreadcrumbList, `@id`s, `inLanguage`, `dateModified` on save, reading time, Twitter tags, `WebSite` node, ItemList, language switcher links, `/zh/` font delivery.

---

## 5. What the existing site already does right / wrong

Files read: `/home/user/accountingsite.github.io/index.html`, `/home/user/accountingsite.github.io/en/index.html` (head), `/home/user/accountingsite.github.io/en/knowledge.html` (head), `/home/user/accountingsite.github.io/en/privacy.html` and `en/terms.html` (JSON-LD), `/home/user/accountingsite.github.io/en/posts/article-template.html` (head + JSON-LD), `/home/user/accountingsite.github.io/en/posts/articles.json`, `/home/user/accountingsite.github.io/core/article-loader.js`, `/home/user/accountingsite.github.io/PROJECT-STATUS.md`.

### Right
- `/en/` subfolder structure with relative in-page links — exactly the structure recommended; no migration needed.
- Every page has `<html lang="en">`, `<title>`, meta description, absolute canonical, OG basics, Twitter card type, `og:locale`, a static JSON-LD shell with `inLanguage`, and `publisher`/`isPartOf` → `WebSite`.
- Root redirect already has three layers incl. `<noscript>` and a visible link — easy to turn into the x-default chooser.
- Article template already carries commented hreflang stubs incl. `x-default` and a Person-author JSON-LD variant with `jobTitle`/`worksFor`, `dateModified`, `mainEntityOfPage` — good bones.
- `articles.json` manifest with `author`, `keywords`, `date` is the right single source of truth for generation.
- Site-wide identity is already read from `<meta name="site-url">` / `firm-name` — the Builder's `site.config` is the natural successor.
- Microdata on cards is harmless (Google reads JSON-LD, microdata and RDFa) though redundant once static JSON-LD exists.

### Wrong / gaps (ordered by impact)
1. **`/cn/` vs `/zh/` naming** — `index.html:15-16`, `en/index.html:30,158`, `article-template.html:69-72` all say `/cn/`, and the template's hreflang stub uses bare `zh`. Decision here is `/zh/` + `zh-Hans`. Fix before any Chinese file exists.
2. **JSON-LD for articles is injected at runtime** (`core/article-loader.js` `injectStructuredData`, lines 500-592) — invisible to AI crawlers and link-preview fetchers; also hard-codes `'/en/posts/'` (line 520) so it can never serve `/th/` or `/zh/`. Must become static output of the Builder.
3. **No business entity anywhere.** The homepage declares `WebSite` → `publisher: Organization` with name + URL only. No `AccountingService`/`LocalBusiness`, no address, phone, geo, hours, `sameAs`, logo, `@id`. This is the biggest schema gap for a local professional-services firm.
4. **Invalid schema types**: `privacy.html:115` uses `"@type": "PrivacyPolicy"` and `terms.html:69` uses `"@type": "TermsOfService"` — neither is a schema.org type (there is no such class; validators will flag them). Use `WebPage` (optionally `about` → firm `@id`).
5. **Root `index.html` has `<link rel="canonical" href="./en/">`** — relative canonical pointing to a *different* page; Google wants absolute canonicals, and the root should be the x-default chooser, not a duplicate of `/en/`. Remove or make absolute-self; add hreflang set listing it as x-default.
6. **No hreflang anywhere** (expected — single language today), **no sitemap, no robots.txt** (Stage 7 items). Note robots.txt at the project path will be inert (2.9).
7. **No `og:image` / `twitter:image`** on any page (template has it commented out). Link previews on LinkedIn/Line/WhatsApp will be blank cards.
8. **No `og:locale:alternate`**, no `<meta http-equiv="content-language">` — needed once TH/ZH exist (Bing/Baidu).
9. **Article JSON-LD lacks `image`** and `publisher.logo`; runtime Article entities also lack `dateModified`. Google lists these as recommended for Article rich results.
10. **`WebSite` node has no `@id`, and `Organization` nodes are repeated by value** on every page with slightly different `url` values (`https://example.com/en/` on the homepage vs `https://example.com` on knowledge/privacy) — entity fragmentation. One `@id`, one `url`.
11. **`<meta name="keywords">`** present on EN pages — ignored by Google, harmless; keep only because Baidu reads it on `/zh/`.
12. **No `BreadcrumbList`** on any page.
13. **Duplicate `WebSite`/`Organization` entities between static shell and injected block** on knowledge.html (static `CollectionPage` + injected `CollectionPage`) — two `CollectionPage` nodes for one page. Once static, emit one.
14. **Mixed URL forms**: homepage canonical `https://example.com/en/` (directory) while article URLs are `.html` — fine *as a rule* (2.5) but must be written down so hreflang/sitemap match exactly.
15. **`formatDate` hard-codes `en-GB`** (`article-loader.js:228`) — card dates on `/th/`/`/zh/` would render in English; the Builder should render dates statically per locale (Thai pages: Buddhist-era is customary in Thai legal contexts; decide — open question 6.5).
16. **Placeholders** (`example.com`, `yourfirm.com`, `Your Firm Name`, `hello@yourfirm.com`) are inconsistent across files (two different placeholder domains). The `siteUrl` config removes the class of bug.
17. `PROJECT-STATUS.md` says "declare hreflang even before TH/ZH exist so search engines know the structure" — **do not**; hreflang to non-existent pages (404s) is an error and gets the whole set ignored. Declare only what exists.

---

## 6. Open questions

1. **`zh-Hans` acceptance in Search Console.** Google's hreflang doc states "language (ISO 639-1) optionally + region (ISO 3166-1)" and does not explicitly mention script subtags, although Google products elsewhere list `zh-Hans`. Verify in Search Console's International Targeting / hreflang report within a month of publishing `/zh/`. Fallback switch in config: `zh-CN`.
2. **Custom domain timing and host.** If Baidu matters at all, the decision is GitHub Pages + Cloudflare proxy (cache-only workaround, uncertain) vs. Cloudflare Pages mirror (clean). The owner needs to say how much the Mainland-China audience matters versus overseas Chinese; that decides Phase 2.
3. **Can Baidu Webmaster register a path-level site under `github.io` at all?** Unverified; moot while the 403 stands.
4. **Who writes Thai/Chinese titles and bodies?** The checklist assumes a human (the owner or a translator) authors TH/ZH metadata using search phrasing. If the Admin is expected to machine-translate, the acceptance criteria need a "draft, needs review" state and the Thai keyword guidance in 2.11 becomes a review checklist.
5. **Dates on Thai pages**: Gregorian (2569 vs 2026) — Thai official/legal usage is Buddhist Era; most Thai business websites show B.E. or both. Design/owner decision; the Builder can render either from the same ISO date.
6. **Thai heading font.** Instrument Serif has no Thai glyphs; the locked "Instrument Serif for headings" rule needs a Thai companion (e.g. a serif-ish Thai face) or an explicit fallback decision. Design discussion required (CLAUDE.md rule).
7. **Google Business Profile.** Off-site but decisive for Thai local intent; the `sameAs` link and consistent NAP depend on the owner claiming it. Who owns that task?
8. **Analytics on `/zh/`.** GA4 is unreliable from the Mainland; decide on a China-reachable, privacy-friendly option or none.
9. **Article slug immutability.** Same slug across languages is load-bearing for hreflang; the Admin must prevent renaming a slug after publish (or generate redirects, which GitHub Pages cannot do server-side — only a meta-refresh stub page).
10. **IndexNow and feeds** — cheap wins; decide if they are v1 or v1.1.

---

### Source index (all URLs cited above, grouped)

**Google Search Central (direct fetch blocked in this sandbox; verified via snippets/secondary):**
https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites ·
https://developers.google.com/search/docs/specialty/international/localized-versions ·
https://developers.google.com/search/blog/2013/04/x-default-hreflang-for-international-pages ·
https://developers.google.com/search/docs/crawling-indexing/sitemaps/large-sitemaps ·
https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap ·
https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls ·
https://developers.google.com/search/docs/appearance/structured-data/local-business ·
https://developers.google.com/search/docs/appearance/structured-data/article ·
https://developers.google.com/search/docs/appearance/structured-data/breadcrumb ·
https://developers.google.com/search/blog/2023/08/howto-faq-changes ·
https://developers.google.com/search/docs/appearance/structured-data/generate-structured-data-with-javascript ·
https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers ·
https://developers.google.cn/custom-search/docs/ref_languages?hl=en

**Standards / vendors:** https://ogp.me/#optional · https://schema.org/AccountingService · https://schema.org/ProfessionalService · https://llmstxt.org/ · https://www.bing.com/indexnow/getstarted · https://support.claude.com/en/articles/8896518-what-is-claudebot (7 Apr 2026) · https://platform.openai.com/docs/bots

**GitHub Pages / Baidu:** https://github.com/orgs/community/discussions/148249 (31 Dec 2024) · https://github.com/orgs/community/discussions/64865 · https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/about-custom-domains-and-github-pages · https://github.com/tari-project/tari-dot-com/issues/120 · https://community.cloudflare.com/t/baiduspider-from-cloudflare-ip/88727 · https://www.chengxiaobai.com/en/trouble-maker/build-and-host-hexo-site-with-cloudflare-pages.html · https://seosherpa.com/baidu-seo/ · https://chinafy.com/blog/how-to-index-your-site-on-baidu-in-2024 · https://www.chinafy.com/blog/how-to-create-a-multilingual-website-that-ranks-on-baidu · https://www.advance-metrics.com/en/blog/baidu-seo-guide/ · https://intl.aliyun.com/icp · https://www.theegg.com/seo/china/verifying-your-site-for-baidu-webmaster-tools · https://en.anqicms.com/blog/4321.html

**hreflang / lang / Bing:** https://flyrank.com/blogs/seo-hub/how-to-handle-hreflang-for-languages-with-multiple-scripts-e-g-chinese-simplified-vs-traditional · https://world.optimizely.com/forum/developer-forum/CMS/Thread-Container/2018/11/zh-hans-or-zh-cn-for-simplified-chinese · https://technicalseo.com/tools/pages/docs/hreflang.html · https://woorank.com/en/edu/seo-guides/best-practices-for-language-declaration · https://searchenginejournal.com/how-googles-hreflang-x-default-enhances-website-navigation/486568 · https://www.searchenginejournal.com/google-uses-different-algorithms-for-different-languages/434227/ · https://searchengineland.com/google-best-to-have-a-primary-language-one-a-page-and-not-mix-languages-387721 · https://dev.to/lingodotdev/the-i18n-seo-checklist-15-seo-optimization-techniques-to-reach-a-global-audience-59l0

**Schema / AEO:** https://ppc.land/google-to-remove-sitelinks-search-box/ · https://www.queryclick.com/blog/google-deprecates-sitelink-search-box/ · https://yoast.com/local-business-listings/ · https://multilipi.com/blog/guide-multilingual-schema-markup · https://www.linguise.com/blog/guide/using-schema-markup-and-structured-data-for-multilingual-websites-seo/ · https://www.bump.it.com/blog/client-injected-json-ld · https://www.seroundtable.com/study-schema-citations-study-41311.html (Ahrefs, May 2026) · https://mikekhorev.com/google-ai-overview · https://icoda.io/ai/strategies-for-optimizing-content-for-google-ai-overviews/ · https://seroundtable.com/google-ai-llms-txt-39607.html (June 2025) · https://www.searchenginejournal.com/llms-txt/ · https://www.omnius.so/industry-updates/google-adds-llms-txt-to-docs-after-publicly-dismissing-it · https://www.searchenginejournal.com/ai-crawler-user-agents-list/558130/ · https://geotoolbox.ai/blog/ai-crawlers · https://ppc.land/google-extended/

**Thailand:** https://gs.statcounter.com/search-engine-market-share/2025-12/thailand · https://www.relevantaudience.com/the-ultimate-guide-to-seo-in-bangkok-for-2025 · https://www.relevantaudience.com/seo/long-tail-keywords-guide/ · https://www.ranktracker.com/blog/a-complete-guide-for-doing-seo-in-thai/
