# 07 — Client-side image pipeline and media library (Wayfinder research, issue #7)

Date: 2026-10-05. Scope: how the browser-only Admin should turn an owner's phone photo into web-ready assets with no server, what storing images in git/GitHub Pages costs, and what a "premium" media library looks like.

---

## 1. สรุปภาษาง่าย (ภาษาไทย)

1. รูปจากมือถือ (4–8 MB, JPEG หรือ HEIC) ใหญ่เกินไปสำหรับเว็บ — ต้องย่อและแปลงก่อนเก็บลง GitHub ทุกครั้ง
2. การย่อ/แปลงทั้งหมดทำได้ในเบราว์เซอร์ของ Admin เอง ไม่ต้องมีเซิร์ฟเวอร์ — ใช้ความสามารถของเบราว์เซอร์ (Canvas) บวกไลบรารีเล็ก ๆ โหลดจาก CDN
3. ผลลัพธ์ต่อรูป 1 ภาพ = WebP 4 ขนาด (480 / 960 / 1600 / 2400 px) + ภาพเบลอจิ๋ว (ThumbHash) สำหรับโชว์ระหว่างโหลด รวมประมาณ 0.4–0.9 MB แทนที่ 6 MB
4. ข้อมูลส่วนตัวในรูป (พิกัด GPS, รุ่นกล้อง, เวลา) จะถูกลบออกโดยอัตโนมัติเมื่อวาดลง Canvas แล้วบันทึกใหม่ — ปลอดภัยต่อเจ้าของและลูกค้า
5. รูปถ่ายแนวตั้งจากมือถือจะไม่หมุนผิดด้าน เพราะเบราว์เซอร์ยุคนี้อ่านค่า EXIF orientation ให้เองตั้งแต่ Chrome 81 / Safari 15 / Firefox 93
6. HEIC (รูป iPhone) เปิดได้เองเฉพาะ Safari 17+; บน Chrome/Edge ต้องโหลดตัวแปลง `heic-to` (WebAssembly) เพิ่มเฉพาะตอนเจอไฟล์ HEIC
7. แนะนำ WebP เป็นหลัก; AVIF เบราว์เซอร์ยังเข้ารหัสเองไม่ได้ ต้องใช้ WebAssembly ช้ากว่ามาก — ให้เป็นตัวเลือก "ภายหลัง"
8. GitHub จำกัดไฟล์เดียวไม่เกิน 100 MB (เตือนที่ 50 MB), repo ควรไม่เกิน 1 GB, เว็บ Pages ไม่เกิน 1 GB และแบนด์วิดธ์ 100 GB/เดือน; Git LFS ใช้กับ Pages ไม่ได้
9. นโยบายที่เสนอ: จำกัด 1 รูปต้นฉบับ ≤ 12 MB ก่อนย่อ, ชุดผลลัพธ์ ≤ 1 MB ต่อรูป, งบสื่อรวม 300 MB แสดงแถบในหน้า Admin, ลบรูปที่ไม่ได้ใช้ได้จาก Admin
10. หน้า "คลังสื่อ" ขั้นแรกต้องมี: กริดรูป, ค้นหา/แท็ก, บังคับใส่ alt text, จุดโฟกัส (focal point), แสดงว่า "ใช้อยู่ที่ X หน้า", แทนที่รูปทุกจุดในคลิกเดียว

---

## 2. Recommended client-side pipeline

### 2.1 Design principles

- No build step: everything is a `<script>` or `import` from a CDN (cdnjs / jsDelivr / unpkg / esm.sh). Same rule the site already follows.
- Progressive enhancement: the browser's own Canvas encoder does the work when it can (WebP in Chrome/Edge/Firefox); a WebAssembly encoder is lazy-loaded only where the browser cannot (WebP on Safari, AVIF everywhere, HEIC decode outside Safari).
- Never trust `toBlob()` silently: per the HTML spec, an unsupported `type` returns a **PNG without any error** — always check `blob.type` after encoding and fall back to wasm ([MDN: toBlob](https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/toBlob); [write-up](https://dev.to/meltem_intepeler_7189d77b/canvastoblobimageavif-silently-returns-a-png-heres-how-i-shipped-avif-export-anyway-1o13)).
- Work in a Web Worker with `OffscreenCanvas` where available so a 24-megapixel decode does not freeze the Admin UI; fall back to a hidden `<canvas>` on the main thread.
- Output is deterministic and content-addressed (`<slug>-<8-char hash>-960.webp`) so git never stores two copies of the same picture and browser caches invalidate correctly.

### 2.2 Step-by-step

| Step | What happens | How (API / library) | Notes |
|---|---|---|---|
| 0. Accept | `<input type="file" accept="image/*,.heic,.heif">` + drag/drop | native | Reject > 12 MB source or > 40 MP with a plain-language message. |
| 1. Sniff | Detect HEIC/HEIF by magic bytes (`ftypheic`, `ftypmif1`), not by extension | `HeicTo.isHeic(file)` or 12-byte read | iOS sometimes labels HEIC as `.jpeg` when "Most compatible" is off. |
| 2. Decode | JPEG/PNG/WebP → `createImageBitmap(file, { imageOrientation: "from-image" })`. HEIC → Safari 17+ decodes natively; others → lazy `import()` of **heic-to** (libheif wasm) to a JPEG blob first | `createImageBitmap` ([BCD](https://github.com/mdn/browser-compat-data/blob/main/api/_globals/createImageBitmap.json)); [heic-to](https://github.com/hoppergee/heic-to) | `from-image` is the default in all current engines, so EXIF orientation is applied for free. Use `resizeWidth` on `createImageBitmap` to downscale **during** decode when the source exceeds ~4096 px — keeps Safari under its canvas memory limits. |
| 3. Normalise | Draw the bitmap onto a canvas no larger than the longest target (2400 px) | Canvas 2D / `OffscreenCanvas` | iOS Safari caps canvas area at 16,777,216 px (4096×4096) — never draw the full 8000×6000 original ([pqina](https://pqina.nl/blog/canvas-area-exceeds-the-maximum-limit/), [WebKit 230855](https://bugs.webkit.org/show_bug.cgi?id=230855)). |
| 4. Focal point | Admin clicks on the preview to set `(fx, fy)` in 0–1 coordinates, default `(0.5, 0.5)` | own UI (crosshair over `<img>`) | Store in `media.json`; the site uses it as `object-position: fx*100% fy*100%`. Only generate *cropped* renditions (e.g. 16:9 hero) when a slot demands it; otherwise keep aspect ratio and let CSS crop. |
| 5. Resize | Produce 480 / 960 / 1600 / 2400 px wide (never upscale; skip widths larger than the source) | `drawImage` with `imageSmoothingQuality: "high"` for a 2× step-down; for > 2× use **pica** (Lanczos/mks2013, wasm+worker) or `@jsquash/resize` | Plain `drawImage` in one jump from 6000→480 px produces aliasing; pica avoids it ([pica](https://github.com/nodeca/pica), on [cdnjs](https://cdnjs.com/libraries/pica)). |
| 6. Encode | WebP q=75–80. Primary: `canvas.toBlob(cb, "image/webp", 0.78)`. If `blob.type !== "image/webp"` (Safari) → **@jsquash/webp** (`encode(imageData, { quality: 75 })`) | Canvas ([BCD](https://github.com/mdn/browser-compat-data/blob/main/api/HTMLCanvasElement.json)); [@jsquash/webp](https://github.com/jamsinclair/jSquash) via `https://esm.sh/@jsquash/webp` | jSquash default WebP quality is 75 (libwebp defaults, `method: 4`). Re-encoding through Canvas discards **all** metadata (EXIF, GPS, ICC) — that is the privacy feature. Convert to sRGB first if the source has a wide-gamut ICC; the browser does this on decode. |
| 7. AVIF (optional, later) | No browser can encode AVIF from Canvas in 2026 (Chromium bug 40848792 open; Firefox/Safari same) → requires **@jsquash/avif** wasm; single-threaded without COOP/COEP headers, which GitHub Pages cannot set | [@jsquash/avif](https://github.com/jamsinclair/jSquash/blob/main/packages/avif/README.md) | jSquash AVIF defaults: quality 50, speed 6. Expect several seconds per 2400 px image single-threaded. Recommendation: **ship WebP only now; add AVIF behind an "extra compression" toggle later**. |
| 8. Placeholder | Downscale to ≤ 100×100, run **ThumbHash** → ~25-byte hash → stored as base64 in `media.json`; the site decodes to a data-URL PNG on render | [thumbhash](https://github.com/evanw/thumbhash) (MIT, npm/CDN, decoder ~1.5 KB gz) | Preserves aspect ratio and average colour, better quality than BlurHash at the same size. Avoids committing one more file per image. |
| 9. Verify | Check each blob: `type`, byte size against caps, decode once with `createImageBitmap` to ensure not corrupt | native | Show a before/after panel: "6.4 MB → 4 files, 712 KB total (−89%)". |
| 10. Commit | Write renditions + updated `media.json` through the existing GitHub API commit flow (one commit per upload batch) | existing Admin | Base64 upload via Contents API is fine at these sizes; Git Trees API for batches > 5 files. |

### 2.3 Concrete targets

| Rendition | Width | Use | Target size (photo) | Quality |
|---|---|---|---|---|
| `-480.webp` | 480 px | phones, cards | 25–45 KB | WebP q78 |
| `-960.webp` | 960 px | tablets, 2× phones | 70–120 KB | WebP q78 |
| `-1600.webp` | 1600 px | desktop content | 150–260 KB | WebP q75 |
| `-2400.webp` | 2400 px | hero / 2× desktop | 300–450 KB | WebP q72 |
| ThumbHash | ≤100 px in, 25 B out | blur placeholder | ~35 chars in JSON | — |
| **Total per photo** | | | **≈ 0.55–0.9 MB** | hard cap 1.2 MB, warn at 1 MB |

Rules of thumb: a 2400 px WebP over 500 KB means the source was noisy — offer "re-encode at lower quality". Logos/illustrations with flat colour: detect by file type (PNG/SVG) and keep PNG (lossless) or offer lossless WebP (`lossless: 1`) instead. Never emit JPEG fallback — WebP is universally decodable in every browser the site supports (Safari 14+, 2020).

Markup emitted by the page templates:

```html
<img src="./media/office-3f9a2c1d-960.webp"
     srcset="./media/office-3f9a2c1d-480.webp 480w, ./media/office-3f9a2c1d-960.webp 960w,
             ./media/office-3f9a2c1d-1600.webp 1600w, ./media/office-3f9a2c1d-2400.webp 2400w"
     sizes="(min-width: 1100px) 1040px, 100vw"
     width="2400" height="1600" alt="…"
     loading="lazy" decoding="async"
     style="object-position: 62% 38%; background: url(data:image/png;base64,…) center/cover">
```

### 2.4 Library choices (all loadable without a build step)

| Need | Pick | Why | CDN / size |
|---|---|---|---|
| Decode + orientation + resize-on-decode | native `createImageBitmap` | zero bytes, honours EXIF orientation by default | — |
| Off-main-thread | native `OffscreenCanvas` in a Worker | zero bytes; fallback to hidden canvas | — |
| High-quality downscale (> 2×) | **pica** 10.x | auto-selects wasm/worker; mks2013 filter resizes + sharpens | `https://cdnjs.cloudflare.com/ajax/libs/pica/10.0.1/pica.min.js` (~60 KB) |
| WebP encode where Canvas cannot (Safari) | **@jsquash/webp** | Squoosh-derived libwebp wasm, ESM, works in workers | `import { encode } from "https://esm.sh/@jsquash/webp"` (~200 KB wasm, lazy) |
| AVIF encode (later) | **@jsquash/avif** | only practical client-side AVIF encoder; single-thread fallback | `https://esm.sh/@jsquash/avif` (~1 MB wasm, lazy) |
| HEIC decode outside Safari | **heic-to** 1.6.x (libheif 1.23.5) | actively tracks libheif; CSP-safe build; worker build | `https://cdn.jsdelivr.net/npm/heic-to@1.6.5/dist/iife/heic-to.js` (several MB wasm, lazy on first HEIC only) |
| Blur placeholder | **thumbhash** | 25 B, aspect-ratio aware, MIT | `https://esm.sh/thumbhash` (~2 KB) |
| Alternative "one call does it all" | browser-image-compression 2.x | `maxWidthOrHeight`, `fileType: "image/webp"`, `useWebWorker`, `preserveExif` default false | `https://cdn.jsdelivr.net/npm/browser-image-compression@2.0.2/dist/browser-image-compression.js` |

Why not just browser-image-compression for everything: it produces one output per call, uses plain Canvas scaling (aliasing on big step-downs), and cannot encode WebP on Safari (it inherits the Canvas limitation). It is a fine fallback or a v1 shortcut, but the pica + jSquash combination gives control over quality and works on all three engines. **heic2any** is the older alternative to heic-to; it is less actively maintained against libheif releases and drops metadata/animation ([heic2any](https://github.com/alexcorvi/heic2any), [heic-to](https://github.com/hoppergee/heic-to)).

EXIF handling summary: drawing to Canvas and re-encoding strips EXIF, GPS, IPTC, XMP and ICC — desired here. The only EXIF value that matters (orientation) is applied *before* stripping because `createImageBitmap`/`drawImage` default to `imageOrientation: "from-image"` (Chrome 81+, Firefox 93+, Safari 15+) ([Chromium image-orientation](https://lists.w3.org/Archives/Public/public-css-archive/2020Jan/0244.html), [BCD createImageBitmap](https://github.com/mdn/browser-compat-data/blob/main/api/_globals/createImageBitmap.json)). Do not set `preserveExif: true` anywhere.

---

## 3. Browser support table (as of 2026-10)

| Capability | Chrome / Edge | Firefox | Safari (macOS) | iOS Safari | Source |
|---|---|---|---|---|---|
| `canvas.toBlob(…, "image/webp")` encode | 50+ | 96+ | **No** (returns PNG) | **No** | [BCD HTMLCanvasElement](https://github.com/mdn/browser-compat-data/blob/main/api/HTMLCanvasElement.json), [WebKit bug 226950](https://bugs.webkit.org/show_bug.cgi?id=226950) |
| `OffscreenCanvas.convertToBlob` "image/webp" | 69+ | 105+ | No | No | [caniuse mdn-api_offscreencanvas_converttoblob_option_type_parameter_webp](https://caniuse.com/mdn-api_offscreencanvas_converttoblob_option_type_parameter_webp) |
| Canvas AVIF encode | **No** (Chromium issue 40848792 open) | No | No | No | [dev.to write-up citing the bug](https://dev.to/meltem_intepeler_7189d77b/canvastoblobimageavif-silently-returns-a-png-heres-how-i-shipped-avif-export-anyway-1o13) |
| AVIF **decode** (`<img>`) | 85+ | 93+ | 16+ | 16+ | [caniuse avif](https://caniuse.com/avif) |
| WebP decode | 32+ | 65+ | 14+ | 14+ | caniuse webp |
| `OffscreenCanvas` (2D) | 69+ | 105+ | 16.4+ (2D only; WebGL 17+) | 16.4+ | [BCD OffscreenCanvas](https://github.com/mdn/browser-compat-data/blob/main/api/OffscreenCanvas.json), [caniuse](https://caniuse.com/offscreencanvas) |
| `createImageBitmap` | 50+ | 42+ | 15+ | 15+ | BCD |
| `createImageBitmap` `imageOrientation` option | 52+ | 93+ | 15+ | 15+ | BCD |
| `createImageBitmap` `resizeWidth/Height` | 54+ | 98+ | 15+ | 15+ | BCD |
| `createImageBitmap` `resizeQuality` | 54+ | 149+ | 15+ | 15+ | BCD |
| Native HEIC/HEIF decode | **No** (any version) | No ([Bugzilla 1402293](https://bugzilla.mozilla.org/show_bug.cgi?id=1402293) open) | 17+ | 17+ | [caniuse heif](https://caniuse.com/heif) |
| Canvas max area | ~268 MP (16384²) | ~124 MP (11180²) | 16,777,216 px (4096×4096) on iOS; `getImageData` fails > 4096² | same | [pqina](https://pqina.nl/blog/canvas-area-exceeds-the-maximum-limit/), [WebKit 230855](https://bugs.webkit.org/show_bug.cgi?id=230855) |
| WebAssembly (needed for jSquash / heic-to / pica wasm) | yes | yes | yes | yes | — |
| SharedArrayBuffer (multithreaded wasm) | needs COOP/COEP headers | same | same | same | GitHub Pages cannot set headers → single-thread wasm only ([@jsquash/avif README](https://github.com/jamsinclair/jSquash/blob/main/packages/avif/README.md)) |

Practical consequence: the owner will likely upload from an iPhone or a Windows laptop with Chrome/Edge. Chrome path = fully native and fast. Safari path = native decode (incl. HEIC) but wasm WebP encode. Chrome + HEIC = wasm decode + native encode. All three paths are covered by the lazy-loading design above.

---

## 4. Git / GitHub Pages storage limits and mitigation policy

### 4.1 Limits (official)

| Limit | Value | Kind | Source |
|---|---|---|---|
| Single file pushed to GitHub | **100 MiB** blocked | hard | [about-large-files-on-github](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github) (`max_github_size: 100 MiB`) |
| Single file warning | **50 MiB** | warning | same (`warning_size: 50 MiB`) |
| File uploaded via web browser UI | 25 MiB | hard | same (`max_github_browser_size`) |
| Repository size | ideally < 1 GB, < 5 GB strongly recommended | soft | same |
| GitHub Pages source repo | 1 GB recommended | soft | [github-pages-limits](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits) |
| Published Pages site | **1 GB** maximum | hard | same |
| Pages bandwidth | 100 GB / month | soft | same |
| Pages builds | 10 / hour (not with custom Actions workflow) | soft | same |
| Pages deploy timeout | 10 minutes | hard | same |
| Git LFS on Pages | **"Git LFS cannot be used with GitHub Pages sites"** | hard | [about-git-large-file-storage](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage) |

Hidden cost nobody puts in a table: **git never forgets**. Every replaced or deleted image stays in history, so repo size only grows. A 1 MB rendition set replaced 10 times = 10 MB of history for one picture. The Admin must make this visible and discourage re-uploading the same photo at different crops (hence focal point instead of cropped copies).

### 4.2 Mitigation policy (recommended, "professional" tier)

| Rule | Value | Where enforced |
|---|---|---|
| Source file accepted | ≤ 12 MB and ≤ 40 MP; JPEG/PNG/WebP/HEIC only | Admin, before decode |
| Per image rendition set | ≤ 1.2 MB total (warn at 1 MB); no single file > 500 KB | Admin, after encode |
| Largest rendition | 2400 px (skip if source smaller) | pipeline |
| Formats committed | WebP only (+ PNG for logos/transparency; SVG passthrough ≤ 200 KB) | pipeline |
| Originals | **never committed** (owner keeps them on phone/OneDrive) | pipeline |
| Media budget shown in Admin | bar: "Media 84 MB of 300 MB" (committed size, read from Trees API `size`) | Admin dashboard |
| Soft ceiling | 300 MB of `/media` → yellow; 500 MB → red + "clean up unused" nudge | Admin |
| Repo ceiling | alert at 700 MB total repo size (GitHub `size` field) | Admin |
| Unused media | "Not used on any page" filter + bulk delete | Admin usage index |
| History growth | document once per year: if repo > 800 MB, maintainer may squash history (one-time technical task, not Admin) | PROJECT-STATUS |
| Bandwidth | 100 GB/mo ≈ 110k page views at ~0.9 MB/page — far beyond an accounting firm; no action, just note it | — |

Why this is enough: a firm site realistically carries 50–150 photos. At ≤ 1 MB each that is ≤ 150 MB — 15% of the 1 GB Pages cap, with headroom for years of history.

### 4.3 Future option only: external image host

Not needed now; listed so the data model does not block it. Store `media.json` entries with a `src` base URL so a host can be swapped in later.

| Host | Free tier (2026) | Notes |
|---|---|---|
| ImageKit | 20 GB bandwidth / month, 3 GB storage (sources vary; some list 20 GB), unlimited transforms, real CDN | Most balanced free tier; URL-based resizing would make the client pipeline optional ([comparison](https://devtoolpicks.com/blog/best-cloudinary-alternatives-indie-hackers-2026), [freetier.co](https://freetier.co/compare/cloudinary-vs-imagekitio)) |
| Cloudinary | 25 credits / month (1 credit = 1 GB storage or 1 GB bandwidth or 1k transforms) | Credit model is confusing; next tier $89/mo ([toolradar](https://toolradar.com/tools/cloudinary/pricing)) |

Trade-offs if ever adopted: a third-party account, uploads need an API key (unsigned upload presets can be abused), and the site gains an external dependency — against the "static, no backend" principle. Keep as "later / only if repo nears 700 MB".

---

## 5. Media library feature list (ranked)

What the premium builders do, from their documentation and community threads:

- **Webflow** Assets panel: grid, folders, search, per-asset alt text (inherited everywhere the asset is used, plus a "Decorative" = `alt=""` option), asset detail shows **"Uses"** count and "Used in" list, deleting an in-use asset shows "Review & delete" with links to each usage, 4 MB image cap, auto-generates 7 srcset variants (3200/2600/2000/1600/1080/800/500) on upload ([Assets panel](https://help.webflow.com/hc/en-us/articles/33961269934227), [alt text](https://help.webflow.com/hc/en-us/articles/33961330170643), [responsive images](https://help.webflow.com/hc/en-us/articles/33961378697107), [forum](https://discourse.webflow.com/t/delete-images-from-asset-manager/11509)).
- **Squarespace** Asset Library: grid, folders/subfolders, rename (filename doubles as alt in many blocks), 20 MB upload cap and 2500 px width cap, 7 generated variants, **focal point** on image blocks/galleries/section backgrounds (`data-image-focal-point="0.5,0.5"`), warning when deleting an in-use image, 30-day trash, recent "view where assets are used" ([Asset library](https://support.squarespace.com/hc/en-us/articles/206542377-Add-and-reuse-images-with-the-Asset-library), [image loader](https://developers.squarespace.com/image-loader), [sizes](https://beyondspace.studio/blog/squarespace-image-sizes-in-various-upload)).
- **Framer**: automatic AVIF conversion and responsive sizes (Auto/512/1024/2048/4096), alt text set once per asset via Asset Manager plugin; usage tracking exists only through marketplace plugins (Asset Analyzer, Assetify) ([how Framer optimises images](https://framer.com/help/articles/how-are-images-optimized-in-framer), [Asset Analyzer](https://www.framer.com/community/marketplace/plugins/asset-analyzer/), [Asset Manager](https://www.framer.com/marketplace/plugins/asset-manager/)).
- **WordPress**: Media Library grid/list, "Uploaded to" column and "Unattached" filter (notoriously unreliable: blocks/ACF images show as unattached), alt text field per attachment, focal point only in the Cover block (core ticket #50092 asks for a library-wide picker), "replace everywhere" via the Enable Media Replace plugin ([Media Attached Filter](https://wordpress.org/plugins/media-attached-filter/), [trac 50092](https://core.trac.wordpress.org/ticket/50092), [Enable Media Replace](https://publishpress.com/blog/enable-media-replace/)).

Ranked list for this Admin:

| Priority | Feature | Detail / rationale |
|---|---|---|
| **Must** | Grid view with thumbnails (480 rendition), name, dimensions, size | the baseline every builder has |
| **Must** | Upload → pipeline → before/after size panel | makes the compression visible and builds trust |
| **Must** | Alt-text prompt on upload, required before "Insert", with a "Decorative (no alt)" checkbox | Webflow pattern; accessibility + SEO; stored once per asset in `media.json` |
| **Must** | Focal point picker (click on preview) saved per asset | Squarespace pattern; avoids cropped duplicates and repo bloat |
| **Must** | Usage tracking: "Used on 3 pages" with links; computed by scanning page JSON/HTML for the media id | Webflow "Uses"; without it deletion is dangerous |
| **Must** | Delete with in-use warning; bulk "delete unused" | prevents broken images; the primary storage mitigation |
| **Must** | Media budget bar (used / 300 MB) + repo size readout | section 4.2 |
| **Must** | Search by name/alt; sort by date, size, usage | minimal findability |
| **Should** | Replace-everywhere: upload a new photo onto an existing asset → same id, new hash suffix, all pages update | Enable-Media-Replace / Webflow behaviour; cache-safe because filenames carry a content hash |
| **Should** | Tags (flat) rather than folders | folders in a static repo mean path moves and history churn; tags are JSON-only |
| **Should** | Re-encode action ("make smaller", drops quality one step) | fixes the occasional 600 KB hero |
| **Should** | HEIC support indicator ("converting iPhone photo…") and HEIC wasm lazy-load | owner likely uses iPhone |
| **Should** | Keyboard/paste upload (Ctrl+V from clipboard) | small, high delight |
| **Later** | AVIF renditions behind a toggle (wasm, slow) | until a browser ships Canvas AVIF encode |
| **Later** | Manual crop presets (16:9 hero, 1:1 avatar) generating extra renditions | only if a layout truly needs a hard crop |
| **Later** | Trash with 30-day restore (git history already is the trash; UI could surface `git revert`) | Squarespace pattern, low priority |
| **Later** | External host adapter (ImageKit) | section 4.3 |
| **Later** | Image "doctor" audit: missing alt, oversize, unused, no focal point | Framer Image Doctor plugin idea |

Data model sketch (`en/media/media.json`, one entry per asset):

```json
{
  "id": "office-3f9a2c1d",
  "alt": "Reception desk at our Bangkok office",
  "decorative": false,
  "width": 2400, "height": 1600,
  "focal": [0.62, 0.38],
  "thumbhash": "3OcRJYB4d3h/iIeHeEh3eIhw+j2w",
  "renditions": { "480": 38112, "960": 94870, "1600": 211340, "2400": 388021 },
  "tags": ["office", "team"],
  "created": "2026-10-05T08:12:00Z"
}
```

Usage is **not** stored here; it is derived at Admin load time by scanning page content for `"office-3f9a2c1d"`, which avoids stale counts.

---

## 6. Open questions

1. Minimum browser for the Admin (not the public site): proposing Chrome/Edge 110+, Safari 16.4+, Firefox 115+ so `OffscreenCanvas` is always available. Confirm the owner's actual devices (iPhone model / iOS version, Windows laptop browser).
2. Do we want AVIF at all before browsers can encode it natively? Cost is a ~1 MB wasm download and several seconds per image on a laptop; benefit is ~20–30% smaller than WebP. Current recommendation: no.
3. Where should `/media` live — `en/media/` (relative paths stay short) or root `media/` shared by a future Thai site? Root is better for the bilingual future; all paths must stay relative per CLAUDE.md.
4. Should "replace everywhere" also keep the old renditions one release for cached pages, or rely purely on content-hashed filenames? Hashed names make the old files safe to delete immediately.
5. Budget numbers (300 MB yellow / 500 MB red / 1.2 MB per image) are proposals; the owner should see them in plain language and agree.
6. History squashing is the only remedy for repo growth and rewrites commit SHAs. Decide now whether that is ever acceptable, or whether the policy is simply "never exceed, so never squash".
7. Logos and illustrations: PNG passthrough vs lossless WebP vs SVG. SVG upload needs sanitising (scripts, external refs) if ever allowed — may be simpler to forbid SVG uploads in the Admin and commit SVGs by hand.
8. Should alt text be required (blocking) or nudged (warning)? Webflow nudges; accessibility practice says required for non-decorative images. Proposal: required, with the explicit "decorative" escape hatch.
9. Verify on a real iPhone that `createImageBitmap` on a 48 MP HEIC with `resizeWidth: 2400` stays within Safari memory limits; if not, decode via heic-to with a target size instead.
10. Multi-image HEIC (Live Photos / bursts): heic-to takes the primary image; confirm acceptable.

---

### Source list

- GitHub Pages limits — https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits
- About large files on GitHub (50 MiB warning, 100 MiB block, 1 GB / 5 GB repo guidance) — https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github
- Git LFS cannot be used with Pages — https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage
- MDN `HTMLCanvasElement.toBlob` — https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/toBlob
- MDN `OffscreenCanvas` — https://developer.mozilla.org/en-US/docs/Web/API/OffscreenCanvas
- MDN `createImageBitmap` — https://developer.mozilla.org/en-US/docs/Web/API/Window/createImageBitmap
- Browser-compat-data (HTMLCanvasElement, OffscreenCanvas, createImageBitmap) — https://github.com/mdn/browser-compat-data
- caniuse HEIF — https://caniuse.com/heif ; OffscreenCanvas — https://caniuse.com/offscreencanvas ; AVIF — https://caniuse.com/avif ; convertToBlob WebP — https://caniuse.com/mdn-api_offscreencanvas_converttoblob_option_type_parameter_webp
- WebKit bug: canvas WebP export returns PNG — https://bugs.webkit.org/show_bug.cgi?id=226950
- WebKit bug: canvas area limit — https://bugs.webkit.org/show_bug.cgi?id=230855
- Firefox HEIF bug (open) — https://bugzilla.mozilla.org/show_bug.cgi?id=1402293
- Chromium image-orientation from-image for canvas (Chrome 81) — https://lists.w3.org/Archives/Public/public-css-archive/2020Jan/0244.html
- Canvas AVIF encode not supported, silent PNG fallback — https://dev.to/meltem_intepeler_7189d77b/canvastoblobimageavif-silently-returns-a-png-heres-how-i-shipped-avif-export-anyway-1o13
- jSquash (WebP/AVIF/resize wasm, esm.sh usage) — https://github.com/jamsinclair/jSquash ; defaults: packages/webp/meta.ts (quality 75), packages/avif/meta.ts (quality 50, speed 6)
- pica — https://github.com/nodeca/pica ; cdnjs — https://cdnjs.com/libraries/pica
- heic-to — https://github.com/hoppergee/heic-to ; heic2any — https://github.com/alexcorvi/heic2any
- browser-image-compression — https://github.com/donaldcwl/browser-image-compression
- ThumbHash — https://github.com/evanw/thumbhash
- Canvas size limits — https://pqina.nl/blog/canvas-area-exceeds-the-maximum-limit/
- Webflow Assets panel / alt text / responsive images — https://help.webflow.com/hc/en-us/articles/33961269934227 , https://help.webflow.com/hc/en-us/articles/33961330170643 , https://help.webflow.com/hc/en-us/articles/33961378697107
- Squarespace Asset library — https://support.squarespace.com/hc/en-us/articles/206542377-Add-and-reuse-images-with-the-Asset-library ; focal point attribute — https://developers.squarespace.com/image-loader
- Framer image optimisation — https://framer.com/help/articles/how-are-images-optimized-in-framer ; Asset Analyzer plugin — https://www.framer.com/community/marketplace/plugins/asset-analyzer/
- WordPress: focal point ticket — https://core.trac.wordpress.org/ticket/50092 ; Enable Media Replace — https://publishpress.com/blog/enable-media-replace/ ; Media Attached Filter — https://wordpress.org/plugins/media-attached-filter/
- ImageKit vs Cloudinary free tiers — https://devtoolpicks.com/blog/best-cloudinary-alternatives-indie-hackers-2026 , https://toolradar.com/tools/cloudinary/pricing
