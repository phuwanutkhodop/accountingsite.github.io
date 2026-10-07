// PROTOTYPE (#21) — library check + theme CSS + sample page. Usage: node build.mjs
import { readFile, writeFile, mkdir } from 'node:fs/promises';
import { parse, names, render } from './engine/template.mjs';
import { types, presets, strings, content } from './library.mjs';
import { themes } from './themes.mjs';

const OUT = new URL('./out/', import.meta.url);
await mkdir(new URL('library/presets/', OUT), { recursive: true });
await mkdir(new URL('library/types/', OUT), { recursive: true });
const LANGS = { en: 'en', th: 'th', zh: 'zh-Hans' };
const BREAKPOINTS = ['40rem', '48rem', '64rem'];
const problems = [];
const fail = (where, msg) => problems.push(`${where}: ${msg}`);

// ---- 1. library check ------------------------------------------------------------------------
const EXPAND = { link: ['href', 'label'], image: ['src', 'alt', 'w', 'h'], phone: ['phoneE164'] };
function allowedNames(type) {
  const s = new Set(['opt', 't']);
  const walk = (fields) => { for (const [k, f] of Object.entries(fields)) { s.add(k); (EXPAND[f.kind] || []).forEach((x) => s.add(x)); if (f.item) walk(f.item); } };
  walk(type.fields);
  return s;
}
const TOKEN_ONLY = /^(color|background|background-color|border-color|outline-color|text-decoration-color|fill|stroke|font-family|font-size|margin|margin-\w+|padding|padding-\w+|gap|row-gap|column-gap|border-radius|box-shadow)$/;
function checkCss(p, prefix) {
  const css = p.css;
  if (/#[0-9a-f]{3,8}\b|rgba?\(|hsla?\(|oklch\(|\b(white|black|red|blue|green|gray|grey)\b/i.test(css)) fail(p.id, 'literal colour in CSS');
  for (const m of css.matchAll(/@container\s+section\s+\(min-width:\s*([^)]+)\)/g)) if (!BREAKPOINTS.includes(m[1].trim())) fail(p.id, `breakpoint ${m[1]} is not one of ${BREAKPOINTS}`);
  if (/@media|@import|url\(/.test(css)) fail(p.id, '@media, @import or url() in CSS');
  // selectors are scoped to the preset's own prefix
  const flat = css.replace(/@container[^{]+\{/g, '').replace(/\}\s*\}/g, '}');
  for (const m of flat.matchAll(/([^{}]+)\{([^}]*)\}/g)) {
    for (const sel of m[1].split(',').map((s) => s.trim()).filter(Boolean)) if (!sel.startsWith('.' + prefix)) fail(p.id, `selector not scoped: ${sel}`);
    for (const decl of m[2].split(';').map((d) => d.trim()).filter(Boolean)) {
      const [prop, ...rest] = decl.split(':'); const val = rest.join(':').trim();
      if (!TOKEN_ONLY.test(prop.trim())) continue;
      const leftover = val.replace(/var\(--[\w-]+\)/g, '').replace(/\b(0|1px|2px|auto|none|inherit|currentColor|transparent|solid)\b/g, '').replace(/[\s,]/g, '');
      if (leftover) fail(p.id, `"${prop.trim()}: ${val}" must use tokens`);
    }
  }
}
for (const p of presets) {
  const type = types[p.type];
  let tree;
  try { tree = parse(p.markup); } catch (e) { fail(p.id, e.message); continue; }
  const allowed = allowedNames(type);
  for (const n of names(tree)) if (!allowed.has(n)) fail(p.id, `template reads undeclared "${n}"`);
  for (const m of p.markup.matchAll(/\{\{opt\.(\w+)\}\}/g)) if (!(m[1] in p.options)) fail(p.id, `option "${m[1]}" has no default`);
  if (/<script|\son\w+=|\sstyle=/i.test(p.markup)) fail(p.id, 'script, event handler or style attribute in markup');
  const prefix = p.markup.match(/class="s__in (\w+)/)?.[1];
  if (!prefix) fail(p.id, 'root element must be <div class="s__in <prefix>">'); else checkCss(p, prefix);
  p.tree = tree;
  await writeFile(new URL(`library/presets/${p.id}@${p.version}.json`, OUT), JSON.stringify({ ...p, tree: undefined }, null, 2));
}
for (const t of Object.values(types)) await writeFile(new URL(`library/types/${t.id}.json`, OUT), JSON.stringify(t, null, 2));

// ---- 2. contrast check (WCAG 2.x relative luminance) -------------------------------------------
const lum = (hex) => { const c = hex.match(/\w\w/g).map((h) => parseInt(h, 16) / 255).map((v) => (v <= 0.04045 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4)); return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]; };
const ratio = (a, b) => { const [x, y] = [lum(a), lum(b)].sort((m, n) => n - m); return (x + 0.05) / (y + 0.05); };
const contrast = [];
for (const [tid, th] of Object.entries(themes))
  for (const [scheme, tones] of Object.entries(th.color))
    for (const [tone, c] of Object.entries(tones)) {
      const pairs = { 'text/bg': [c.text, c.bg], 'muted/bg': [c.muted, c.bg], 'accent/bg': [c.accent, c.bg], 'onAccent/accent': [c.onAccent, c.accent], 'text/surface': [c.text, c.surface], 'muted/surface': [c.muted, c.surface] };
      for (const [k, [f, b]] of Object.entries(pairs)) {
        const r = ratio(f, b);
        contrast.push({ theme: tid, scheme, tone, pair: k, ratio: +r.toFixed(2) });
        if (r < 4.5) fail(`theme ${tid} ${scheme}/${tone}`, `${k} contrast ${r.toFixed(2)} < 4.5`);
      }
    }

// ---- 3. generated CSS -----------------------------------------------------------------------
const fontsCss = await readFile(new URL('../t15/out/fonts.css', import.meta.url), 'utf8');
const FB = {
  serif: 'Georgia, "Times New Roman", "Noto Serif Thai", Ayuthaya, Tahoma, "Noto Serif CJK SC", "Source Han Serif SC", "Songti SC", STSong, SimSun, serif',
  sans: '"Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans Thai Looped", "Noto Sans Thai", Thonburi, "Leelawadee UI", Tahoma, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Noto Sans CJK SC", "Source Han Sans SC", sans-serif',
};
const PAIRINGS = { // from #15
  sans: { display: ['Hanken Grotesk', 'Noto Sans Thai Looped', 'Noto Sans SC', FB.sans], body: ['Hanken Grotesk', 'Noto Sans Thai Looped', 'Noto Sans SC', FB.sans], ui: ['Hanken Grotesk', 'Noto Sans Thai Looped', 'Noto Sans SC', FB.sans], punct: 'Noto Sans SC Punct' },
  serif: { display: ['Cormorant Garamond', 'Trirong', 'Noto Serif SC', FB.serif], body: ['Newsreader', 'Taviraj', 'Noto Serif SC', FB.serif], ui: ['Hanken Grotesk', 'Noto Sans Thai Looped', 'Noto Serif SC', FB.sans], punct: 'Noto Serif SC Punct' },
};
const stack = (list) => list.map((f, i) => (i === list.length - 1 ? f : `"${f}"`)).join(', ');
const colorVars = (c) => Object.entries(c).map(([k, v]) => `--c-${k.replace(/[A-Z]/g, (m) => '-' + m.toLowerCase())}:${v}`).join(';');
let themeCss = '';
for (const [tid, th] of Object.entries(themes)) {
  const P = PAIRINGS[th.font.pairing];
  const S = `.site[data-set="${tid}"]`;
  const vars = [
    ...['display', 'body', 'ui'].map((r) => `--font-${r}:${stack(P[r])}`),
    `--weight-display:${th.font.display.weight}`, `--weight-body:${th.font.body.weight}`, `--weight-ui:${th.font.ui.weight}`, `--weight-ui-strong:${th.font.ui.strong}`,
    ...Object.entries(th.size).map(([k, v]) => `--size-${k}:${v}`),
    ...Object.entries(th.space).map(([k, v]) => `--space-${k}:${v}`),
    ...Object.entries(th.radius).map(([k, v]) => `--radius-${k}:${v}`),
    `--measure-page:${th.measure.page}`, `--eyebrow-transform:${th.eyebrow.transform}`, `--eyebrow-tracking:${th.eyebrow.tracking}`,
  ];
  themeCss += `${S}{${vars.join(';')}}\n`;
  themeCss += `${S} :lang(zh){${['display', 'body', 'ui'].map((r) => `--font-${r}:"${P.punct}", ${stack(P[r])}`).join(';')}}\n`;
  for (const scheme of ['light', 'dark']) {
    const SS = scheme === 'light' ? S : `${S}[data-scheme="dark"]`;
    themeCss += `${SS}{${colorVars(th.color[scheme].plain)};color-scheme:${scheme}}\n`;
    for (const tone of ['plain', 'tinted', 'bold']) themeCss += `${SS} .tone-${tone}{${colorVars(th.color[scheme][tone])}}\n`;
  }
}

// Generator-owned base: the #15 type system plus the shared parts every preset may use (.s, .s__in, .btn, .eyebrow, .lead, .actions).
const baseCss = `
.site{font-family:var(--font-body);font-weight:var(--weight-body);font-size:var(--size-body);line-height:var(--lh-body);color:var(--c-text);background:var(--c-bg);font-synthesis:none;font-variant-numeric:lining-nums;font-size-adjust:ex-height .5;container:page/inline-size;--lh-body:1.6;--lh-head:1.15;--track-head:-.01em}
.site :lang(th){--lh-body:1.8;--lh-head:1.4;--track-head:0}
.site :lang(zh){--lh-body:1.8;--lh-head:1.35;--track-head:0;text-autospace:normal}
.site :is(h1,h2,h3){font-family:var(--font-display);font-weight:var(--weight-display);line-height:var(--lh-head);letter-spacing:var(--track-head);text-wrap:balance;margin:0}
.site :is(p,ul,ol,dl,dd,figure){margin:0}
.site em{font-style:normal;font-weight:600}
.s{background:var(--c-bg);color:var(--c-text);padding-block:var(--space-section);container:section/inline-size}
.s__in{max-width:var(--measure-page);margin-inline:auto;padding-inline:var(--space-gutter)}
.site .lead{font-size:var(--size-lead);text-wrap:pretty}
.site .eyebrow{font-family:var(--font-ui);font-weight:var(--weight-ui-strong);font-size:var(--size-small);letter-spacing:var(--eyebrow-tracking);text-transform:var(--eyebrow-transform);color:var(--c-accent)}
.site :is(:lang(th),:lang(zh)) .eyebrow{letter-spacing:0}
.site .actions{display:flex;flex-wrap:wrap;gap:var(--space-3)}
.site .btn{display:inline-flex;align-items:center;font-family:var(--font-ui);font-weight:var(--weight-ui);font-size:var(--size-ui);line-height:1.3;padding:.8em 1.25em;border-radius:var(--radius-control);border:1px solid var(--c-accent);background:var(--c-accent);color:var(--c-on-accent);text-decoration:none}
.site :lang(th) .btn{line-height:1.5}
.site .btn--quiet{background:transparent;color:var(--c-accent)}
.site .btn:hover{filter:brightness(1.08)}
.site a:focus-visible{outline:2px solid var(--c-accent);outline-offset:3px}
`;
const presetCss = presets.map((p) => `/* ${p.id}@${p.version} */\n${p.css}`).join('\n');

// ---- 4. render the sample page ----------------------------------------------------------------
const heroB64 = (await readFile(new URL('hero.webp', OUT))).toString('base64');
const renders = {};
for (const lang of Object.keys(LANGS)) {
  renders[lang] = presets.map((p) => {
    const c = content[p.type][lang];
    const data = { ...c, opt: p.options, t: strings[lang], image: c.image ? { ...c.image, src: `data:image/webp;base64,${heroB64}`, w: 1200, h: 900 } : undefined };
    let html;
    try { html = render(p.tree, data); } catch (e) { fail(`${p.id} [${lang}]`, e.message); html = ''; }
    return { p, html: `<section class="s tone-${p.options.tone}" id="${p.id}-${lang}" data-preset="${p.id}@${p.version}">${html}</section>` };
  });
}
await writeFile(new URL('check.json', OUT), JSON.stringify({ problems, contrast }, null, 1));
console.log(problems.length ? 'LIBRARY CHECK FAILED:\n' + problems.join('\n') : 'Library check passed: 9 presets, 3 types, 2 themes × 2 schemes × 3 tones.');
console.log('lowest contrast:', contrast.sort((a, b) => a.ratio - b.ratio).slice(0, 4));
export { renders, themeCss, baseCss, presetCss, fontsCss, problems, contrast };
