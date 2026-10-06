# 16 — Builder tech stack

**Ticket:** GitHub issue #16 (Wayfinder grilling)
**Date:** 6 October 2026
**Decided by:** Claude, under the owner's standing delegation of technical choices (map #1, "Working preference"). Nothing here changes what visitors see or what the owner must do, except §2-11 (a current browser).
**Inputs:** research #3 (CMS landscape), #4 (browser publishing and security), #6 (rich-text editors), #7 (image pipeline); decisions #10 (content model), #11 (rendering strategy)
**Evidence:** a hands-on spike on 6 October 2026, described in §4
**Status:** locked. **Amended 6 October 2026** after the plan review (`docs/reviews/2026-10-06-plan-review.md`, findings M2, M11, M12, L3): decision 6's link list, and §4.1.
**Amended 6 October 2026 by #31** (`docs/decisions/31-multi-site-hosting.md`): the §3 layout is the root of the Admin's own repo, `<admin-org>/<admin-org>.github.io`, on its own origin. `connect-src` adds the sites' origins for the live check. The Admin repo holds no HTML besides its two `index.html` files and no SVG (rule A1).

---

## 1. สรุปสำหรับเจ้าของกิจการ (ภาษาไทย)

1. **ไม่มีขั้นตอน "build":** โค้ดของ Admin เป็นไฟล์ JavaScript ธรรมดา ไฟล์ใน repo คือไฟล์ที่ทำงานจริง คุณไม่ต้องติดตั้งโปรแกรมใดในเครื่องเลย
2. **หน้าจอ Admin ใช้ไลบรารีเล็ก Preact (ขนาดราว 9 KB):** ใช้แบบแผนเดียวกับ React ซึ่งนักพัฒนาและ AI ทุกคนรู้จัก โค้ดจึงเป็นระเบียบเดียวกันทุก session
3. **ไลบรารีภายนอกทุกตัวเก็บสำเนาไว้ใน repo ของเราเอง** ไม่ดึงจากเว็บอื่นตอนใช้งาน โทเคนจึงปลอดภัยกว่า และ Admin ยังใช้ได้แม้เว็บผู้ให้บริการไลบรารีล่ม
4. **เครื่องสร้างหน้าเว็บเป็นโค้ดล้วน** ไม่พึ่งเบราว์เซอร์ ตัวเดียวกันใช้ทั้งพรีวิว การ Publish และการทดสอบอัตโนมัติ
5. **ตัวแก้บทความคือ Tiptap** ทดสอบจริงในเบราว์เซอร์แล้ว พิมพ์ไทยและจีนได้ และทำงานภายใต้กฎความปลอดภัยแบบเข้มงวด
6. **บทความเก็บเป็นข้อมูลที่มีโครงสร้าง ไม่ใช่ HTML ดิบ** สิ่งที่ไม่อยู่ในรายการที่อนุญาต (เช่นสคริปต์แปลกปลอมที่ติดมากับการวาง) จึงขึ้นเว็บไม่ได้เลย
7. **หน้าเว็บที่ผู้เข้าชมเห็นไม่มี framework** มีแค่ JavaScript เล็ก ๆ สำหรับส่วนเสริม
8. **สิ่งที่คุณต้องทำ:** ใช้เบราว์เซอร์ที่อัปเดตอยู่ (Chrome, Edge, Safari หรือ Firefox) ซึ่งเป็นค่าเริ่มต้นของทุกเครื่องอยู่แล้ว

---

## 2. Decisions

| # | Question | Decision | Why |
|---|---|---|---|
| 1 | Build step for our own code | **None.** Plain ES2022 modules, loaded by the browser through `<script type="module">`. Imports are relative paths (`../vendor/ui.js`); there is no import map, because the policy in decision 8 blocks an inline one (verified, §4). The file in the repo is the file that runs. | Any session can edit a file, push, and see it live. No `dist/` drifts from its source. No GitHub Actions sits between Publish and the live site, which keeps research #4's publishing model intact. Debugging reads the real source. |
| 2 | UI library for the Admin | **Preact 10.29.8 + htm 3.1.1 + @preact/signals 2.11.3.** Components are written with htm tagged templates (`` html`<${Tree} pages=${p} />` ``), not JSX, so nothing is compiled. **8.8 KB gzip** in total (measured). | The Admin is a real application: 9 areas, an always-visible page tree, a four-zone editor, forms in three languages, and Publish and Versions screens (#12, #24). Hand-written DOM updates at that size become the main source of bugs, and every session invents its own pattern. Preact gives one component model, React's API (the best-known UI pattern for people and AI sessions), and needs no compiler. |
| 3 | Third-party code | **Vendored, never loaded from a CDN at runtime.** Each library is bundled once into a single-file ES module in `admin/vendor/` by `tools/vendor/` (esbuild 0.28.2, with an npm lockfile that pins every transitive version). The bundles are byte-reproducible, and `--check` proves it, following the pattern of `tools/brand/`. Licence texts ship beside them. **Only Claude sessions run this, and only when adding or upgrading a library.** | The Admin's origin holds the GitHub token (research #4). Every runtime CDN is a party that could serve script into that origin. Integrity pins cannot practically cover the chain of nested module imports a CDN serves. Vendoring also gives a strict `script-src 'self'` policy (decision 8), removes Tiptap's mixed-version crash (research #6), and keeps the Admin working offline from a CDN outage. |
| 4 | The generator ("engine") | **Pure ES modules in `admin/engine/`.** No DOM, no `fetch`, no `Intl`, no clock and no randomness (decision #11 §3.1–3.2). Node 22 imports the same files unchanged. A test enforces that `engine/` imports only from `engine/`. | Decision #11 requires one generator for preview, Publish and tests. Plain modules are the only form that runs in both places without a build. |
| 5 | Preset template engine (from #11 §3.8) | **In-house strict Mustache subset, about 200 lines, in `admin/engine/`.** It supports `{{name}}` (always escaped), `{{#list}}…{{/list}}`, `{{^x}}…{{/x}}` and `{{! comment}}`. **It forbids** `{{{raw}}}`, `{{& raw}}`, partials, lambdas and delimiter changes; using one is a template error. A missing variable is an error, which the validation gate reports (decision #11 §3.5). Conformance is tested against the official Mustache spec suites for the supported features. | mustache.js is lenient where we need strict: it prints missing values silently as blanks, offers unescaped output, and supports lambdas and partials. Strictness turns preset mistakes into Publish-blocking errors instead of quietly broken pages. |
| 6 | Rich-text storage and sanitiser (from #11 §3.8 and research #6, open question 4) | **The stored format is the editor's JSON document**, not HTML. The engine's **whitelist renderer** turns it into HTML and is the sanitiser. It knows a closed set of nodes, marks and attributes. It escapes all text and allows only these links: `https:`, `mailto:`, `tel:`, internal links by id (`page:<id>`, `page:<id>#<anchor>`, `article:<id>`, decision #14 §3.7) and `#<anchor>` on the same page. Images are referenced by **media id** (`media:<id>`, resolved to `media/` renditions) and may be flagged *decorative* (empty `alt`). YouTube embeds are allowed on `youtube-nocookie.com` only. *(Amended — review L3: the first list had raw `./` and `../` links, which would break when pages move, and no phone or anchor links.)* Anything else is a validation error. **There is no template syntax for raw HTML:** when `{{body}}` meets a rich-text document, the engine renders it through this renderer. **DOMPurify is not used.** | With no HTML parsing in the generator, there is nothing to sanitise and no parser mismatch to exploit. It also needs no DOM in Node. The editor's schema already drops scripts, event handlers, `javascript:` links and stray styles at input (verified, §4). The renderer is the second, independent layer. |
| 7 | Rich-text editor | **Tiptap 3.31.4 confirmed** (research #6). It is vendored as one bundle of **141 KB gzip** (StarterKit, table, image, YouTube, file handler), loaded only when an editor opens. Two configurations: *inline* (bold, italic, link) for section text, and *article* (H2/H3, lists, table, image, callout, YouTube) for articles. | Research #6's first choice. It passed the spike: it works vendored under a strict policy, and Thai with stacked tone marks, Chinese and Backspace behave in Chromium. |
| 8 | Security baseline for `admin/` | A Content-Security-Policy `<meta>` with **no `unsafe-inline`, no `unsafe-eval` and no third-party script origins**: `default-src 'self'; script-src 'self' 'wasm-unsafe-eval'; style-src 'self'; img-src 'self' data: blob:; connect-src 'self' https://api.github.com; worker-src 'self'; object-src 'none'; base-uri 'none'; form-action 'none'`. `'wasm-unsafe-eval'` permits WebAssembly only, which the image pipeline needs (research #7); it does not permit JavaScript `eval`. A `<meta>` cannot carry `frame-ancestors`, so the Admin **refuses to start inside a frame**. Its stylesheets, including ProseMirror's, are files. | Research #4: XSS in the Admin is the real threat to the token. Every rule above was tested in the spike (§4). The first build session finalises the exact string; the baseline does not loosen. |
| 9 | Language and types | **JavaScript with JSDoc type annotations.** No TypeScript compilation. Sessions may type-check, but it is not required. | It keeps decision 1 intact. JSDoc gives editors and sessions the types without a compile step. |
| 10 | Tests | **Node's built-in runner (`node --test`), with no test framework dependency.** Golden-file tests for the engine (decision #11 §3.1). Playwright smoke tests of the Admin run in sessions, where cloud containers provide Chromium. A **GitHub Actions check** runs the tests and `tools/vendor --check` on pushes that touch `admin/`, `tests/` or `tools/`. It only checks; it never builds or deploys. | Tests need no installs beyond Node. Publish commits from the Admin do not trigger the check, because it is limited to code paths. |
| 11 | Browser baseline | **Current Chrome and Edge, Safari 17+ (Mac, iPhone, iPad), current Firefox.** No polyfills. Features relied on: ES modules, module workers, IndexedDB, SubtleCrypto, WebAssembly, `OffscreenCanvas` (with a main-thread fallback, research #7). | All of these have been in every major browser for over two years. The owner's Windows laptop and iPhone are covered. |
| 12 | Routing | **Hash routes** (`#/pages/home`). | GitHub Pages has no fallback for deep links into a single-page app; hash routes always load `admin/index.html`. |
| 13 | JavaScript on the published site | **No framework.** Small progressive-enhancement modules (search, animations, form sending). Widgets in the extension slot get a framework-free contract (`mount(element, config)`); the details belong to the later widget work. | Decision #11: pages work fully with JavaScript off. Visitors download no Admin libraries. |
| 14 | Preact 11 | **Start on Preact 10.29.8.** Preact 11.0.0 came out on 30 September 2026. Moving to 11 is a deliberate vendor upgrade once it has had a few weeks of patch releases. | The API we use (`h`, `render`, hooks, signals) is the same on both. A one-week-old major release is not the base for a new product. |

### 2.1 Options rejected

- **A framework with a build step** (Svelte, Vue, or React with Vite). The repo file would no longer be the running file. Either sessions commit a built `dist/`, which drifts from its source, or GitHub Actions builds the site, which changes the publishing model of research #4 and adds a step between Publish and live. The gains (compiled reactivity, JSX, TypeScript) are modest at this size, and Preact with htm gives the same component model. Svelte cannot run without its compiler at all.
- **Plain DOM code with no library.** This is zero bytes, but at the Admin's size it means re-inventing a renderer, and each session writes it differently.
- **Lit (web components).** ProseMirror inside Shadow DOM has had long-standing selection problems in Safari. Using Lit without Shadow DOM loses its main benefit. React-style components are also more familiar to future sessions.
- **Alpine.js or petite-vue.** Their standard builds evaluate template expressions as code, which needs `unsafe-eval` and breaks decision 8. They also suit page sprinkles, not an application.
- **Loading libraries from jsDelivr or esm.sh at runtime**, as research #6 and #7 assumed. Rejected by decision 3.

---

## 3. Layout of `admin/`

```
admin/
├── index.html        CSP meta and one <script type="module" src="./app/main.js">; nothing inline
├── app/              the Admin UI: Preact + htm components, screens, hash router, Thai/English strings
├── engine/           PURE: generator, template engine, rich-text renderer, validation, date and number tables
│                     (no DOM, no fetch, no Intl, no clock); runs unchanged in the browser and in Node
├── services/         GitHub API, IndexedDB cache, token store, image pipeline (module workers)
├── styles/           the Admin's own neutral look (#22) and vendored editor CSS
└── vendor/           pinned single-file ES modules + VENDOR.json (name, version, licence, sha256) + licences

tests/                node --test: engine golden files, Mustache spec conformance, import-boundary check
tools/vendor/         package.json + lockfile, the esbuild entry files, build.mjs (--check)
package.json          { "private": true, "type": "module" }; no runtime dependencies
```

Everything inside `admin/` refers to other files by relative path, so it moves unchanged into the Admin repo that #31 decided.

**Planned vendor set:**

| Bundle | Libraries | Licence | When it loads |
|---|---|---|---|
| `ui.js` | Preact, htm, @preact/signals | MIT, Apache-2.0 | always |
| `editor.js` | Tiptap 3.31.4 with ProseMirror | MIT | first editor opened |
| image libraries | pica, @jsquash/webp (wasm), heic-to (wasm) | MIT, Apache-2.0, **LGPL-3.0** | first upload that needs them (research #7) |

heic-to is shipped as a separate, unmodified file with its licence. That keeps the LGPL's terms; it is never merged into another bundle.

---

## 4. Evidence: the spike (6 October 2026)

This was a throwaway test in a scratch folder; no spike code is committed. Libraries were bundled with esbuild 0.28.2 and served from the same origin under the policy in §2-8, then driven with Playwright in headless Chromium.

| Check | Result |
|---|---|
| Preact + htm + signals under `script-src 'self'` | Renders and updates with no policy violation. htm uses no `eval`. |
| Tiptap under the same policy (`injectCSS: false`) | Works with no violation. |
| Typing `กี่ ปั๊ม ใต้ ที่สุด`, Backspace, H2, then `税务 2026 <b>` | Correct document. `<b>` is stored as text, and the renderer printed `&lt;b&gt;`. |
| Setting content to `<img onerror>`, `<script>`, a `javascript:` link and a Calibri `<span>` | The schema dropped the script, the handler, the link and the style. The policy blocked the inline style. The image node survived the schema, and the whitelist renderer refused it (an image must point to `./media/…`). Both layers work. |
| The same engine module in Node 22 | Imports and runs unchanged and gives the same output. |
| WebAssembly under `script-src 'self'` | **Blocked.** With `'wasm-unsafe-eval'` it works, hence decision 8. |
| An inline import map under `script-src 'self'` | **Blocked**, hence relative imports in decision 1. |
| Rebuilding the vendor bundles | Byte-identical (sha256). |
| Sizes, gzip | `ui.js` 8.8 KB · `editor.js` 141.5 KB |
| First load of the Admin shell with the editor, served locally | ~120 ms |

### 4.1 Not yet proven, and must be before #23 *(added after the plan review)*

- **The strict policy has not been tested on the live preview** (review M2). The preview must show unpublished theme CSS, focal-point positioning, YouTube frames and web fonts while staying under decision 8. #22 runs this test first. If anything must loosen, the record names the exact source and the reason (for example `style-src blob:` for preview-only stylesheets); `unsafe-inline` and `unsafe-eval` stay forbidden whatever happens.
- **`.nojekyll` must exist before any Admin code ships** (review M12). Without it, GitHub's Jekyll step skips folders such as `vendor`, so `admin/vendor/` would silently not be served. The repo does not have it today. #20 adds it. **Done in #20.**
- **Blob hashing rules for `engine/` and `services/`** (review M11): the git blob length is the **UTF-8 byte count**, never the JavaScript string length (Thai and Chinese differ), and every text file the Admin writes uses **LF** line endings. The repo gains `* text=auto eol=lf` beside the existing brand rules in `.gitattributes`. **Proven against real git in #20; the `.gitattributes` rule is in place.**
- **`X-GitHub-Api-Version`:** **proven allowed** from the browser by #20 (`docs/decisions/20-publish-proof.md`), although GitHub's documented CORS list omits it. The Admin sends `X-GitHub-Api-Version: 2022-11-28` on every call, so a future default version cannot change behaviour silently.

**Not proven by the spike:** real Thai keyboard input (Kedmanee on Windows, Thai on iPhone) and Safari and Firefox. Playwright types characters, not IME keystrokes, and only Chromium is available in cloud sessions. The owner should try this by hand on their own devices when the first editor exists (#27). Research #6's open question 2 stays open until then.

---

## 5. Effects on other tickets

- **#6 Rich-text editors:** open question 1 (live CDN test) is replaced by vendoring and the spike. Question 4 is answered: the editor's JSON is stored. Question 2 (Thai typing on real devices) moves to #27.
- **#7 Image pipeline:** its libraries are vendored, not imported from esm.sh or jsDelivr. The Admin's policy includes `'wasm-unsafe-eval'` for them.
- **#10 §5:** the Admin's code layout is §3 here.
- **#11 §3.8:** the template engine and the sanitiser are chosen (decisions 5 and 6).
- **#13 Design Library:** preset markup is written in the strict subset of decision 5; that subset is the authoring contract.
- **#20 Token task:** the first code written follows this stack and layout, and it adds `package.json`, `tests/` and the check workflow.
- **#22 Admin prototype:** it is built in this stack, so the prototype can grow into the product instead of being thrown away.
- **#31 Multi-site hosting:** `admin/` is self-contained with relative imports, so it can be moved.

---

## 6. Not decided here

- Drag-and-drop for the page tree, and its keyboard alternative → #14 and #22. Any library chosen must be framework-free and is vendored.
- The Admin's look → #22.
- The exact JSON schema of rich-text nodes, including the callout node → the first editor build (#27), following decision 6.
- The extension-slot contract in detail → later widget work.
