// PROTOTYPE (#15) — renders out/specimen.html from content.mjs + the subset fonts in out/fonts.css.
// Usage: node build.mjs && node render.mjs
import { readFile, writeFile } from 'node:fs/promises';
import { content } from './content.mjs';

const OUT = new URL('../out/', import.meta.url);
const fontsCss = await readFile(new URL('fonts.css', OUT), 'utf8');
const perPage = JSON.parse(await readFile(new URL('perpage.json', OUT), 'utf8'));

const esc = (s) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');

// ---- the proposed role stacks (what the generator would emit) -----------------------------
const FB = {
  serif: 'Georgia, "Times New Roman", "Noto Serif Thai", Ayuthaya, Tahoma, "Noto Serif CJK SC", "Source Han Serif SC", "Songti SC", STSong, SimSun, serif',
  sans: '"Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans Thai Looped", "Noto Sans Thai", Thonburi, "Leelawadee UI", Tahoma, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Noto Sans CJK SC", "Source Han Sans SC", sans-serif',
};
const PAIR = {
  serif: {
    display: { fonts: ['Cormorant Garamond', 'Trirong', 'Noto Serif SC'], punct: 'Noto Serif SC Punct', fb: FB.serif, weight: 600 },
    body: { fonts: ['Newsreader', 'Taviraj', 'Noto Serif SC'], punct: 'Noto Serif SC Punct', fb: FB.serif, weight: 400 },
    ui: { fonts: ['Hanken Grotesk', 'Noto Sans Thai Looped', 'Noto Serif SC'], punct: 'Noto Serif SC Punct', fb: FB.sans, weight: 500 },
  },
  sans: {
    display: { fonts: ['Hanken Grotesk', 'Noto Sans Thai Looped', 'Noto Sans SC'], punct: 'Noto Sans SC Punct', fb: FB.sans, weight: 700 },
    body: { fonts: ['Hanken Grotesk', 'Noto Sans Thai Looped', 'Noto Sans SC'], punct: 'Noto Sans SC Punct', fb: FB.sans, weight: 400 },
    ui: { fonts: ['Hanken Grotesk', 'Noto Sans Thai Looped', 'Noto Sans SC'], punct: 'Noto Sans SC Punct', fb: FB.sans, weight: 500 },
  },
  fallback: {
    display: { fonts: [], fb: FB.serif, weight: 600 },
    body: { fonts: [], fb: FB.serif, weight: 400 },
    ui: { fonts: [], fb: FB.sans, weight: 500 },
  },
};
const q = (f) => `"${f}"`;
let stackCss = '';
for (const [pair, roles] of Object.entries(PAIR)) {
  const base = [], zh = [];
  for (const [role, r] of Object.entries(roles)) {
    const k = { display: 'fd', body: 'fb', ui: 'fu' }[role];
    base.push(`--${k}:${[...r.fonts.map(q), r.fb].join(', ')};--${k}w:${r.weight}`);
    if (r.punct) zh.push(`--${k}:${[q(r.punct), ...r.fonts.map(q), r.fb].join(', ')}`);
  }
  stackCss += `#app[data-pair="${pair}"] .spec{${base.join(';')}}\n`;
  if (zh.length) stackCss += `#app[data-pair="${pair}"] .spec:lang(zh){${zh.join(';')}}\n`;
}

// ---- markup --------------------------------------------------------------------------------
const LANGS = { en: { tag: 'en', code: 'EN' }, th: { tag: 'th', code: 'TH' }, zh: { tag: 'zh-Hans', code: 'ZH' } };
const table = (t) => `<div class="tablewrap"><table><caption>${esc(t.caption)}</caption><thead><tr>${t.head.map((h, i) => `<th scope="col"${i === 1 ? ' class="num"' : ''}>${esc(h)}</th>`).join('')}</tr></thead><tbody>${t.rows.map((r) => `<tr>${r.map((c, i) => (i === 0 ? `<th scope="row">${esc(c)}</th>` : `<td${i === 1 ? ' class="num"' : ''}>${esc(c)}</td>`)).join('')}</tr>`).join('')}</tbody><tfoot><tr><th scope="row">${esc(t.total[0])}</th><td class="num">${esc(t.total[1])}</td><td></td></tr></tfoot></table></div>`;
const article = (a) => a.map(([k, v]) => (k === 'ul' ? `<ul>${v.map((li) => `<li>${esc(li)}</li>`).join('')}</ul>` : k === 'quote' ? `<blockquote>${esc(v)}</blockquote>` : `<${k}>${esc(v)}</${k}>`)).join('\n');

const compare = Object.entries(content).map(([l, c]) => `<div class="spec cmp" lang="${LANGS[l].tag}" data-l="${l}"><span class="tag">${LANGS[l].code}</span><h2 class="h1like">${esc(c.h1)}</h2><p class="lead">${esc(c.lead)}</p><p class="mix">${esc(c.mixed)}</p><div class="btns"><button type="button" class="btn">${esc(c.button)}</button></div></div>`).join('');

const sheets = Object.entries(content).map(([l, c]) => `
<section class="sheet spec" lang="${LANGS[l].tag}" data-l="${l}" aria-label="${esc(c.name)}">
  <header class="sheethead"><span class="tag">${LANGS[l].code}</span><span class="sheetname">${esc(c.name)}</span><code>lang="${LANGS[l].tag}"</code><span class="cost" data-cost="${l}"></span></header>
  <h1>${esc(c.h1)}</h1>
  <p class="lead">${esc(c.lead)}</p>
  <div class="btns"><button type="button" class="btn">${esc(c.button)}</button><button type="button" class="btn btn2">${esc(c.buttonSecondary)}</button></div>
  <h2>${esc(c.h2)}</h2>
  <h3>${esc(c.h3)}</h3>
  <dl class="probe"><dt>ปนหลายภาษา</dt><dd>${esc(c.mixed)}</dd><dt>${l === 'th' ? 'สระ วรรณยุกต์ และหางอักษร' : l === 'zh' ? 'เครื่องหมายวรรคตอนจีน' : 'ตัวเลขและสัญลักษณ์'}</dt><dd class="stress">${esc(c.stress)}</dd><dt>หัวข้อขนาดใหญ่</dt><dd class="bigprobe">${esc(l === 'th' ? 'ปั๊มน้ำ ผู้ถือหุ้น ฎีกา' : l === 'zh' ? '财务报表“税务”' : 'Quarterly 2026 Fig.')}</dd></dl>
  ${table(c.table)}
  <article class="article">${article(c.article)}</article>
</section>`).join('\n');

const kb = (n) => `${n.toLocaleString('en-US', { maximumFractionDigits: 0 })} KB`;

const html = `<title>Builder Type Specimen</title>
<style>
/* Layout: one reading column; a three-language comparison strip, then one full sheet per language; controls in a bottom bar. */
:root{
  --bg:#f5f6f4; --paper:#ffffff; --fg:#1a1e1c; --muted:#5b6460; --rule:#d7dcd9; --accent:#2c5b86; --accent-fg:#ffffff; --guide:rgba(44,91,134,.28); --bar:#1a1e1c; --bar-fg:#f5f6f4; --bar-muted:#a6aeaa; --chip:#2c3330;
  --chrome:system-ui,-apple-system,"Segoe UI",Roboto,"Noto Sans Thai","Leelawadee UI",sans-serif;
  --s-h1:clamp(2rem,1.25rem + 3vw,3.25rem); --s-h2:clamp(1.5rem,1.15rem + 1.4vw,2rem); --s-h3:1.25rem; --s-lead:1.1875rem; --s-body:1.0625rem; --s-ui:.9375rem; --s-small:.8125rem;
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#111413;--paper:#181c1a;--fg:#e4e9e6;--muted:#9aa39f;--rule:#2b322f;--accent:#8db5dc;--accent-fg:#0f1a24;--guide:rgba(141,181,220,.3);--bar:#e4e9e6;--bar-fg:#111413;--bar-muted:#4d5552;--chip:#c9d0cc;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#111413;--paper:#181c1a;--fg:#e4e9e6;--muted:#9aa39f;--rule:#2b322f;--accent:#8db5dc;--accent-fg:#0f1a24;--guide:rgba(141,181,220,.3);--bar:#e4e9e6;--bar-fg:#111413;--bar-muted:#4d5552;--chip:#c9d0cc;color-scheme:dark}
body{background:var(--bg);color:var(--fg);font:15px/1.5 var(--chrome);padding-inline:16px;padding-block:24px 160px}
${fontsCss}
${stackCss}
.wrap{max-width:46rem;margin-inline:auto;display:grid;gap:40px}
.intro{display:grid;gap:12px}
.intro h1{font:600 1.5rem/1.25 var(--chrome);margin:0;text-wrap:balance}
.intro p{margin:0;color:var(--muted);max-width:40rem}
.facts{display:grid;grid-template-columns:repeat(auto-fit,minmax(10rem,1fr));gap:12px;margin:0}
.facts div{background:var(--paper);border:1px solid var(--rule);border-radius:6px;padding:10px 12px;min-width:0}
.facts dt{font-size:var(--s-small);color:var(--muted)}
.facts dd{margin:2px 0 0;font-variant-numeric:tabular-nums;font-weight:600}
.check{background:var(--paper);border:1px solid var(--rule);border-radius:6px;padding:14px 16px}
.check h2{font:600 1rem/1.4 var(--chrome);margin:0 0 6px}
.check ol{margin:0;padding-left:1.3em;display:grid;gap:4px}
.group{display:grid;gap:14px}
.label{font:600 var(--s-small)/1.4 var(--chrome);letter-spacing:.04em;color:var(--muted);margin:0}

/* ---- the type system under test ---- */
.spec{font-family:var(--fb);font-weight:var(--fbw);font-size:var(--s-body);line-height:var(--lh-body);font-synthesis:none;font-variant-numeric:lining-nums;--lh-body:1.6;--lh-head:1.15;--track-head:-.01em}
.spec:lang(th){--lh-body:1.8;--lh-head:1.4;--track-head:0}
.spec:lang(zh){--lh-body:1.8;--lh-head:1.35;--track-head:0;text-autospace:normal}
#app[data-fsa="on"] .spec{font-size-adjust:ex-height .5}
.spec :is(h1,h2,h3,.h1like,.bigprobe,blockquote){font-family:var(--fd);font-weight:var(--fdw);line-height:var(--lh-head);letter-spacing:var(--track-head);text-wrap:balance;margin:0}
.spec h1{font-size:var(--s-h1)}
.spec :is(h2,.h1like){font-size:var(--s-h2)}
.spec h3{font-size:var(--s-h3)}
.spec .bigprobe{font-size:var(--s-h1)}
.spec p,.spec ul,.spec dl,.spec dd{margin:0}
.spec .lead{font-size:var(--s-lead)}
.spec .btns{display:flex;flex-wrap:wrap;gap:10px}
.spec .btn{font-family:var(--fu);font-weight:var(--fuw);font-size:var(--s-ui);line-height:1.3;padding:.7em 1.15em;border-radius:4px;border:1px solid var(--accent);background:var(--accent);color:var(--accent-fg);cursor:pointer}
.spec .btn2{background:transparent;color:var(--accent)}
.spec .btn:focus-visible,.bar button:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.spec:lang(th) .btn,.spec:lang(zh) .btn{line-height:1.5}
.spec strong,.spec th{font-weight:600}
.spec em{font-style:normal;font-weight:600}
.spec blockquote{font-size:var(--s-h3);border-left:2px solid var(--accent);padding-left:16px}
.cmpgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(13rem,1fr));gap:20px}
.cmp{display:grid;gap:12px;align-content:start;background:var(--paper);border:1px solid var(--rule);border-radius:6px;padding:16px;min-width:0}
.tag{font:600 .75rem/1 var(--chrome);letter-spacing:.06em;color:var(--muted)}
.sheet{display:grid;gap:22px;background:var(--paper);border:1px solid var(--rule);border-radius:6px;padding:28px clamp(16px,4vw,40px);min-width:0}
.sheethead{display:flex;flex-wrap:wrap;gap:8px 14px;align-items:baseline;font:var(--s-small)/1.4 var(--chrome);color:var(--muted);border-bottom:1px solid var(--rule);padding-bottom:10px}
.sheethead code{font-size:.75rem}.sheethead .cost{margin-left:auto;font-variant-numeric:tabular-nums}
.probe{display:grid;gap:6px}
.probe dt{font:var(--s-small)/1.4 var(--chrome);color:var(--muted);margin-top:8px}
.tablewrap{overflow-x:auto;min-width:0}
.spec table{border-collapse:collapse;width:100%;font-family:var(--fu);font-weight:var(--fuw);font-size:var(--s-ui);line-height:1.5}
.spec caption{text-align:left;font-family:var(--fd);font-weight:var(--fdw);font-size:var(--s-h3);line-height:var(--lh-head);padding-bottom:8px}
.spec :is(td,th){border-bottom:1px solid var(--rule);padding:.55em .9em .55em 0;text-align:left;vertical-align:top}
.spec thead th{color:var(--muted)}
.spec tbody th{font-weight:var(--fuw)}
.spec tfoot :is(th,td){border-bottom:0;font-weight:600}
.spec .num{text-align:right;font-variant-numeric:tabular-nums lining-nums;white-space:nowrap}
.spec td:last-child{white-space:nowrap}
.spec:lang(th) :is(td,th){line-height:1.7}
.article{display:grid;gap:16px;max-width:38em}
.article ul{padding-left:1.2em;display:grid;gap:6px}
#app[data-guides="on"] .spec :is(h1,h2,h3,.h1like,.bigprobe,p,li,dd,blockquote,td,th){background-image:repeating-linear-gradient(to bottom,transparent 0 calc(1lh - 1px),var(--guide) calc(1lh - 1px) 1lh)}
#app[data-show="en"] [data-l]:not([data-l="en"]),#app[data-show="th"] [data-l]:not([data-l="th"]),#app[data-show="zh"] [data-l]:not([data-l="zh"]){display:none}

/* ---- controls ---- */
.bar{position:fixed;inset-inline:0;bottom:0;background:var(--bar);color:var(--bar-fg);padding:10px 16px calc(10px + env(safe-area-inset-bottom,0px));font:13px/1.3 var(--chrome);display:flex;flex-wrap:wrap;gap:8px 18px;justify-content:center;z-index:10}
.ctl{display:flex;align-items:center;gap:6px;flex-wrap:wrap}
.ctl > span{color:var(--bar-muted)}
.seg{display:flex;border:1px solid var(--chip);border-radius:5px;overflow:hidden}
.seg button{font:inherit;color:inherit;background:transparent;border:0;padding:6px 10px;cursor:pointer}
.seg button+button{border-left:1px solid var(--chip)}
.seg button[aria-pressed="true"]{background:var(--bar-fg);color:var(--bar)}
@media (prefers-reduced-motion:no-preference){.seg button{transition:background .12s}}
</style>

<div id="app" data-pair="serif" data-fsa="on" data-guides="off" data-show="all">
<main class="wrap">
  <section class="intro">
    <h1>ตัวอย่างระบบตัวอักษรสามภาษา · Builder Type Specimen</h1>
    <p>ต้นแบบสำหรับตั๋ว #15 บนธีมทดสอบที่เป็นกลาง ฟอนต์ที่เห็นเป็นชุดตัวอย่าง ไม่ใช่ฟอนต์ของบริษัท สิ่งที่ทดสอบคือ "ระบบ" ที่ทุกธีมจะใช้: ฟอนต์ 3 บทบาทต่อภาษา ขนาดที่เข้ากันระหว่างอักษร และไฟล์ฟอนต์ที่ตัดเหลือเฉพาะตัวอักษรที่เว็บใช้จริง ใช้แถบด้านล่างสลับชุดฟอนต์และการตั้งค่า</p>
    <dl class="facts">
      <div><dt>ฟอนต์ที่หน้าอังกฤษโหลด</dt><dd id="c-en"></dd></div>
      <div><dt>ฟอนต์ที่หน้าไทยโหลด</dt><dd id="c-th"></dd></div>
      <div><dt>ฟอนต์ที่หน้าจีนโหลด</dt><dd id="c-zh"></dd></div>
      <div><dt>Google Fonts สำหรับข้อความจีนชุดเดียวกัน</dt><dd>692 KB ต่อ 1 น้ำหนัก</dd></div>
    </dl>
    <div class="check">
      <h2>สิ่งที่ขอให้คุณดู (บน Windows และบน iPhone)</h2>
      <ol>
        <li>สระและวรรณยุกต์ไทย เช่น "ปั๊ม ที่สุด ฎีกา" ไม่ชนหรือถูกตัด ทั้งหัวข้อใหญ่และเนื้อความ เปิด "เส้นบรรทัด" ช่วยดูได้</li>
        <li>ตัวเลขในตารางค่าบริการเรียงตรงหลักกันทุกภาษา</li>
        <li>คำอังกฤษและตัวเลขที่ปนในประโยคไทยและจีน มีขนาดกลมกลืน ไม่ใหญ่หรือเล็กเกิน</li>
        <li>ลอง "ปรับขนาดให้เท่ากัน" เปิดกับปิด แบบไหนอ่านสบายกว่า โดยเฉพาะหน้าไทย</li>
        <li>ลอง "ฟอนต์สำรอง" เพื่อดูหน้าตาเมื่อฟอนต์โหลดไม่ได้ เช่น ผู้อ่านในจีนบางเครือข่าย</li>
      </ol>
    </div>
  </section>

  <section class="group"><p class="label">เทียบสามภาษาเคียงกัน</p>
  <div class="cmpgrid">${compare}</div></section>

  <section class="group"><p class="label">หน้าเต็มแต่ละภาษา</p>
  ${sheets}</section>
</main>

<nav class="bar" aria-label="ตัวเลือกของต้นแบบ">
  <div class="ctl"><span>ชุดฟอนต์</span><div class="seg" data-key="pair"><button type="button" id="p-serif" data-v="serif">มีเชิง</button><button type="button" id="p-sans" data-v="sans">ไม่มีเชิง</button><button type="button" id="p-fb" data-v="fallback">ฟอนต์สำรอง</button></div></div>
  <div class="ctl"><span>ปรับขนาดให้เท่ากัน</span><div class="seg" data-key="fsa"><button type="button" id="f-on" data-v="on">เปิด</button><button type="button" id="f-off" data-v="off">ปิด</button></div></div>
  <div class="ctl"><span>เส้นบรรทัด</span><div class="seg" data-key="guides"><button type="button" id="g-off" data-v="off">ปิด</button><button type="button" id="g-on" data-v="on">เปิด</button></div></div>
  <div class="ctl"><span>แสดง</span><div class="seg" data-key="show"><button type="button" id="s-all" data-v="all">ทั้งหมด</button><button type="button" id="s-en" data-v="en">EN</button><button type="button" id="s-th" data-v="th">TH</button><button type="button" id="s-zh" data-v="zh">ZH</button></div></div>
</nav>
</div>

<script>
(() => {
  const COST = ${JSON.stringify(perPage)};
  const app = document.getElementById('app');
  const fmt = (n) => Math.round(n) + ' KB';
  const state = { pair: 'serif', fsa: 'on', guides: 'off', show: 'all' };
  try { Object.assign(state, JSON.parse(localStorage.getItem('spec15') || '{}')); } catch (e) {}
  function apply() {
    for (const [k, v] of Object.entries(state)) app.dataset[k] = v;
    document.querySelectorAll('.seg').forEach((seg) => seg.querySelectorAll('button').forEach((b) => b.setAttribute('aria-pressed', String(state[seg.dataset.key] === b.dataset.v))));
    const c = COST[state.pair];
    for (const l of ['en', 'th', 'zh']) {
      const txt = c ? fmt(c[l]) + ' · WOFF' : '0 KB · ฟอนต์ในเครื่อง';
      document.getElementById('c-' + l).textContent = txt;
      document.querySelectorAll('[data-cost="' + l + '"]').forEach((e) => (e.textContent = 'ฟอนต์ของหน้านี้ ' + txt));
    }
    try { localStorage.setItem('spec15', JSON.stringify(state)); } catch (e) {}
  }
  document.querySelectorAll('.seg').forEach((seg) => seg.addEventListener('click', (e) => {
    const b = e.target.closest('button'); if (!b) return;
    state[seg.dataset.key] = b.dataset.v; apply();
  }));
  apply();
})();
</script>
`;
await writeFile(new URL('specimen.html', OUT), html);
console.log('specimen.html', (Buffer.byteLength(html) / 1024).toFixed(0), 'KB');
