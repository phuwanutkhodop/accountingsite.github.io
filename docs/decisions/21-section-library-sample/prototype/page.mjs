// PROTOTYPE (#21) — writes out/sample.html. Usage: node page.mjs
import { writeFile } from 'node:fs/promises';
import { renders, themeCss, baseCss, presetCss, fontsCss, problems, contrast } from './build.mjs';
import { types } from './library.mjs';

const esc = (s) => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const LANGS = { en: 'en', th: 'th', zh: 'zh-Hans' };
const toneTh = { plain: 'พื้นปกติ', tinted: 'พื้นอ่อน', bold: 'พื้นเข้ม' };
const lowest = Math.min(...contrast.map((c) => c.ratio)).toFixed(2);

const pages = Object.entries(renders).map(([lang, list]) => `<div class="langpage" lang="${LANGS[lang]}" data-l="${lang}">${list.map(({ p, html }) => `
<div class="plabel" lang="th"><span class="plabel__type">${esc(types[p.type].name.th)}</span><strong>${esc(p.name.th)}</strong><code>${p.id}@${p.version}</code><span>${toneTh[p.options.tone]}</span></div>
${html}`).join('')}</div>`).join('');

const html = `<title>Section Library Sample</title>
<style>
/* Layout: a short brief, then the sample site in a frame (full width or phone width); controls in a bottom bar. */
:root{--bg:#eceeed;--fg:#1b1f1d;--muted:#5a6360;--rule:#cfd5d2;--card:#ffffff;--bar:#1b1f1d;--bar-fg:#f3f5f4;--bar-muted:#a5ada9;--chip:#353d3a;--ok:#1e6b45;
--chrome:system-ui,-apple-system,"Segoe UI",Roboto,"Noto Sans Thai","Leelawadee UI",sans-serif}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#0d0f0e;--fg:#e3e8e5;--muted:#99a39e;--rule:#2c3330;--card:#161a18;--bar:#e3e8e5;--bar-fg:#0d0f0e;--bar-muted:#55605b;--chip:#c3cbc7;--ok:#7fd1a5;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#0d0f0e;--fg:#e3e8e5;--muted:#99a39e;--rule:#2c3330;--card:#161a18;--bar:#e3e8e5;--bar-fg:#0d0f0e;--bar-muted:#55605b;--chip:#c3cbc7;--ok:#7fd1a5;color-scheme:dark}
body{background:var(--bg);color:var(--fg);font:15px/1.55 var(--chrome);padding-inline:16px;padding-block:20px 150px}
.intro{max-width:46rem;margin:0 auto 24px;display:grid;gap:12px}
.intro h1{font:600 1.45rem/1.3 var(--chrome);margin:0;text-wrap:balance}
.intro p{margin:0;color:var(--muted)}
.intro .ok{color:var(--ok);font-weight:600}
.ask{background:var(--card);border:1px solid var(--rule);border-radius:6px;padding:14px 16px}
.ask h2{font:600 1rem/1.4 var(--chrome);margin:0 0 6px}
.ask ol{margin:0;padding-left:1.3em;display:grid;gap:4px}
.frame{margin-inline:auto;max-width:90rem;border:1px solid var(--rule);border-radius:8px;overflow:hidden}
#app[data-width="phone"] .frame{max-width:390px;border-radius:20px}
#app[data-labels="off"] .plabel{display:none}
.plabel{display:flex;flex-wrap:wrap;gap:4px 12px;align-items:baseline;padding:8px 16px;font:12.5px/1.4 var(--chrome);background:var(--card);color:var(--muted);border-block:1px solid var(--rule)}
.plabel strong{color:var(--fg)}
.plabel__type{font-weight:600;letter-spacing:.02em}
#app:not([data-lang="en"]) .langpage[data-l="en"],#app:not([data-lang="th"]) .langpage[data-l="th"],#app:not([data-lang="zh"]) .langpage[data-l="zh"]{display:none}
${fontsCss}
${themeCss}
${baseCss}
${presetCss}
.bar{position:fixed;inset-inline:0;bottom:0;background:var(--bar);color:var(--bar-fg);padding:10px 16px calc(10px + env(safe-area-inset-bottom,0px));font:13px/1.3 var(--chrome);display:flex;flex-wrap:wrap;gap:8px 18px;justify-content:center;z-index:10}
.ctl{display:flex;align-items:center;gap:6px}
.ctl > span{color:var(--bar-muted)}
.seg{display:flex;border:1px solid var(--chip);border-radius:5px;overflow:hidden}
.seg button{font:inherit;color:inherit;background:transparent;border:0;padding:6px 10px;cursor:pointer}
.seg button+button{border-left:1px solid var(--chip)}
.seg button[aria-pressed="true"]{background:var(--bar-fg);color:var(--bar)}
.seg button:focus-visible{outline:2px solid var(--bar-fg);outline-offset:2px}
</style>

<div id="app" data-set="a" data-scheme="light" data-lang="th" data-width="full" data-labels="on">
<header class="intro">
  <h1>ตัวอย่างคลังดีไซน์ · Section Library Sample</h1>
  <p>ต้นแบบสำหรับตั๋ว #21: section 3 ชนิด (เปิดหน้า · บริการ · ติดต่อ) ชนิดละ 3 ดีไซน์ บนธีมทดสอบที่เป็นกลาง 2 ธีม ทุกดีไซน์ใช้ HTML ชุดเดียวกัน สลับธีมแล้วหน้าตาเปลี่ยนด้วยค่าในธีมเท่านั้น ข้อความเป็นเนื้อหาตัวอย่าง รูปเป็นรูปแทน</p>
  <p class="${problems.length ? '' : 'ok'}">${problems.length ? 'การตรวจคลังไม่ผ่าน ' + problems.length + ' ข้อ' : `การตรวจคลังผ่าน: 9 ดีไซน์ · 2 ธีม × สว่าง/มืด × 3 พื้น · ความคมชัดต่ำสุด ${lowest}:1 (เกณฑ์ 4.5:1)`}</p>
  <div class="ask">
    <h2>สิ่งที่อยากให้คุณดู</h2>
    <ol>
      <li>ดีไซน์ไหนดูไม่ถึงระดับเว็บมืออาชีพ บอกชื่อดีไซน์ เช่น "การ์ด" หรือ "แถบเข้ม"</li>
      <li>สลับธีม A กับ B: ธีมทดสอบทั้งสองดูเป็นกลางพอ ไม่เอนไปทางแบรนด์ใดหรือไม่</li>
      <li>สลับภาษา: ภาษาไทยและจีนดูเรียบร้อยเท่าภาษาอังกฤษหรือไม่</li>
      <li>ลอง "มือถือ" หรือเปิดบนโทรศัพท์จริง ทุก section อ่านง่ายหรือไม่</li>
    </ol>
  </div>
</header>

<div class="frame"><div class="site" data-set="a" data-scheme="light">${pages}</div></div>

<nav class="bar" aria-label="ตัวเลือกของต้นแบบ">
  <div class="ctl"><span>ธีม</span><div class="seg" data-key="set"><button type="button" id="t-a" data-v="a">ทดสอบ A</button><button type="button" id="t-b" data-v="b">ทดสอบ B</button></div></div>
  <div class="ctl"><span>สี</span><div class="seg" data-key="scheme"><button type="button" id="c-l" data-v="light">สว่าง</button><button type="button" id="c-d" data-v="dark">มืด</button></div></div>
  <div class="ctl"><span>ภาษา</span><div class="seg" data-key="lang"><button type="button" id="l-th" data-v="th">TH</button><button type="button" id="l-en" data-v="en">EN</button><button type="button" id="l-zh" data-v="zh">ZH</button></div></div>
  <div class="ctl"><span>ความกว้าง</span><div class="seg" data-key="width"><button type="button" id="w-f" data-v="full">เต็ม</button><button type="button" id="w-p" data-v="phone">มือถือ</button></div></div>
  <div class="ctl"><span>ป้ายชื่อ</span><div class="seg" data-key="labels"><button type="button" id="b-on" data-v="on">แสดง</button><button type="button" id="b-off" data-v="off">ซ่อน</button></div></div>
</nav>
</div>

<script>
(() => {
  const app = document.getElementById('app');
  const site = app.querySelector('.site');
  const dark = window.matchMedia && matchMedia('(prefers-color-scheme: dark)').matches;
  const state = { set: 'a', scheme: dark ? 'dark' : 'light', lang: 'th', width: 'full', labels: 'on' };
  try { Object.assign(state, JSON.parse(localStorage.getItem('lib21') || '{}')); } catch (e) {}
  function apply() {
    for (const [k, v] of Object.entries(state)) app.dataset[k] = v;
    site.dataset.set = state.set; site.dataset.scheme = state.scheme;
    document.querySelectorAll('.seg').forEach((seg) => seg.querySelectorAll('button').forEach((b) => b.setAttribute('aria-pressed', String(state[seg.dataset.key] === b.dataset.v))));
    try { localStorage.setItem('lib21', JSON.stringify(state)); } catch (e) {}
  }
  document.querySelectorAll('.seg').forEach((seg) => seg.addEventListener('click', (e) => {
    const b = e.target.closest('button'); if (!b) return; state[seg.dataset.key] = b.dataset.v; apply();
  }));
  document.querySelectorAll('.site a[href^="#"]').forEach((a) => a.addEventListener('click', (e) => e.preventDefault()));
  apply();
})();
</script>
`;
await writeFile(new URL('./out/sample.html', import.meta.url), html);
await writeFile(new URL('./out/local.html', import.meta.url), `<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"></head><body>${html}</body></html>`);
console.log('sample.html', (Buffer.byteLength(html) / 1024).toFixed(0), 'KB');
