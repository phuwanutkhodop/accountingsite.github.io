// PROTOTYPE (#15) — builds the type specimen exactly as Publish would: subset every face to
// guard set ∪ characters used, wrap as WOFF, emit @font-face with unicode-range.
// Usage: node build.mjs   (fonts in ../dl, output in ../out)
import { readFile, writeFile, mkdir } from 'node:fs/promises';
import { deflateSync } from 'node:zlib';
import { createHash } from 'node:crypto';
import { createSubsetter, toWoff } from './fontsubset.mjs';
import { content } from './content.mjs';

const DL = new URL('../dl/', import.meta.url);
const OUT = new URL('../out/', import.meta.url);
await mkdir(OUT, { recursive: true });

const hb = await createSubsetter(await readFile(new URL('node_modules/harfbuzzjs/dist/harfbuzz-subset.wasm', import.meta.url)));
const deflate = async (b) => new Uint8Array(deflateSync(b, { level: 9 }));

// ---- characters used, per language -------------------------------------------------------
const flat = (v) => (typeof v === 'string' ? [v] : Array.isArray(v) ? v.flatMap(flat) : Object.values(v).flatMap(flat));
const used = Object.fromEntries(Object.entries(content).map(([l, c]) => [l, new Set([...flat(c).join('')].map((ch) => ch.codePointAt(0)))]));
const allUsed = new Set(Object.values(used).flatMap((s) => [...s]));

const range = (a, b) => Array.from({ length: b - a + 1 }, (_, i) => a + i);
const inRanges = (cp, rs) => rs.some(([a, b]) => cp >= a && cp <= b);

// Script ranges = the unicode-range of each face, and the guard set it always carries.
const SCRIPT = {
  latin: { ranges: [[0x20, 0x7e], [0xa0, 0x17f], [0x2010, 0x2027], [0x2030, 0x203a], [0x2044, 0x2044], [0x20ac, 0x20ac], [0x2190, 0x2193], [0x2212, 0x2212]], guard: [[0x20, 0x7e], [0xa0, 0xff], [0x2010, 0x2027], [0x2030, 0x203a], [0x20ac, 0x20ac], [0x2212, 0x2212]] },
  thai: { ranges: [[0x0e00, 0x0e7f], [0x200b, 0x200d], [0x25cc, 0x25cc]], guard: 'all' },
  cjk: { ranges: [[0x3000, 0x303f], [0x3400, 0x4dbf], [0x4e00, 0x9fff], [0xff00, 0xffef]], guard: [] },
  // CJK punctuation alias: shared codepoints that must take the full-width CJK form in Chinese text.
  cjkpunct: { ranges: [[0x00b7, 0x00b7], [0x2014, 0x2014], [0x2018, 0x2019], [0x201c, 0x201d], [0x2026, 0x2026]], guard: 'all' },
};
function codepointsFor(script) {
  const s = SCRIPT[script];
  const guard = s.guard === 'all' ? s.ranges : s.guard;
  const cps = new Set(guard.flatMap(([a, b]) => range(a, b)));
  for (const cp of allUsed) if (inRanges(cp, s.ranges)) cps.add(cp);
  return cps;
}
const unicodeRange = (script) => SCRIPT[script].ranges.map(([a, b]) => (a === b ? `U+${a.toString(16)}` : `U+${a.toString(16)}-${b.toString(16)}`)).join(', ');

// ---- the font plan: variant → role → script → face ----------------------------------------
const F = {
  cormorant: { file: 'CormorantGaramond[wght].ttf', family: 'Cormorant Garamond' },
  newsreader: { file: 'Newsreader[opsz,wght].ttf', family: 'Newsreader' },
  hanken: { file: 'HankenGrotesk[wght].ttf', family: 'Hanken Grotesk' },
  trirong: { files: { 400: 'Trirong-Regular.ttf', 500: 'Trirong-Medium.ttf', 600: 'Trirong-SemiBold.ttf' }, family: 'Trirong' },
  taviraj: { files: { 400: 'Taviraj-Regular.ttf', 600: 'Taviraj-SemiBold.ttf' }, family: 'Taviraj' },
  notothai: { file: 'NotoSansThaiLooped[wdth,wght].ttf', family: 'Noto Sans Thai Looped' },
  notoserifsc: { file: 'NotoSerifSC[wght].ttf', family: 'Noto Serif SC' },
  notosanssc: { file: 'NotoSansSC[wght].ttf', family: 'Noto Sans SC' },
};
// role: [latin, thai, cjk] with the weights each role uses (regular + strong)
export const PLAN = {
  serif: {
    display: { latin: ['cormorant', [600]], thai: ['trirong', [500]], cjk: ['notoserifsc', [600]] },
    body: { latin: ['newsreader', [400, 600]], thai: ['taviraj', [400, 600]], cjk: ['notoserifsc', [400, 600]] },
    ui: { latin: ['hanken', [500, 600]], thai: ['notothai', [500, 600]], cjk: ['notoserifsc', []] },
  },
  sans: {
    display: { latin: ['hanken', [700]], thai: ['notothai', [600]], cjk: ['notosanssc', [600]] },
    body: { latin: ['hanken', [400, 600]], thai: ['notothai', [400, 600]], cjk: ['notosanssc', [400, 600]] },
    ui: { latin: ['hanken', [500, 600]], thai: ['notothai', [500, 600]], cjk: ['notosanssc', []] },
  },
};
const OPSZ = { display: 48, body: 16, ui: 14 };

// ---- subset every face once --------------------------------------------------------------
const masters = new Map();
const master = async (file) => masters.get(file) ?? masters.set(file, new Uint8Array(await readFile(new URL(file, DL)))).get(file);
const faces = new Map(); // key -> { family, weight, script, b64, sizes }
const report = [];

async function face(fontKey, weight, script, role) {
  const f = F[fontKey];
  const file = f.files ? f.files[weight] : f.file;
  const pin = f.files ? {} : { wght: weight, ...(fontKey === 'newsreader' ? { opsz: OPSZ[role] } : {}), ...(fontKey === 'notothai' ? { wdth: 100 } : {}) };
  const scripts = script === 'cjk' ? ['cjk', 'cjkpunct'] : [script];
  const out = [];
  for (const sc of scripts) {
    const cps = codepointsFor(sc);
    // Cache key from inputs, not output bytes: the file name stays stable whichever browser compressed it.
    const key = createHash('sha256').update(file + JSON.stringify(pin) + [...cps].sort((a, b) => a - b).join(',')).digest('hex').slice(0, 10);
    const family = sc === 'cjkpunct' ? `${f.family} Punct` : f.family;
    const id = `${family}|${weight}|${key}`;
    if (!faces.has(id)) {
      const m = await master(file);
      const t0 = performance.now();
      const sfnt = hb.subset(m, cps, pin);
      const woff = await toWoff(sfnt, deflate);
      const ms = Math.round(performance.now() - t0);
      faces.set(id, { family, weight, script: sc, key, woff });
      report.push({ family, weight, script: sc, glyphsRequested: cps.size, masterKB: +(m.byteLength / 1024).toFixed(1), sfntKB: +(sfnt.byteLength / 1024).toFixed(1), woffKB: +(woff.byteLength / 1024).toFixed(1), ms, file: `${family.replace(/\s+/g, '')}-${weight}-${key}.woff` });
    }
    out.push(id);
  }
  return out;
}

const variantFaces = {};
for (const [variant, roles] of Object.entries(PLAN)) {
  variantFaces[variant] = new Set();
  for (const [role, scripts] of Object.entries(roles))
    for (const [script, [fontKey, weights]] of Object.entries(scripts))
      for (const w of weights) for (const id of await face(fontKey, w, script, role)) variantFaces[variant].add(id);
}

// ---- CSS ---------------------------------------------------------------------------------
let css = '';
for (const [id, fc] of faces) {
  await writeFile(new URL(report.find((r) => r.family === fc.family && r.weight === fc.weight && r.file.includes(fc.key)).file, OUT), fc.woff);
  const b64 = Buffer.from(fc.woff).toString('base64');
  css += `@font-face{font-family:"${fc.family}";font-weight:${fc.weight};font-style:normal;font-display:swap;src:url(data:font/woff;base64,${b64}) format("woff");unicode-range:${unicodeRange(fc.script)}}\n`;
}
await writeFile(new URL('fonts.css', OUT), css);
const LANG_SCRIPTS = { en: ['latin'], th: ['latin', 'thai'], zh: ['latin', 'cjk', 'cjkpunct'] };
const perPage = Object.fromEntries(Object.entries(variantFaces).map(([v, ids]) => [v, Object.fromEntries(Object.entries(LANG_SCRIPTS).map(([l, scs]) => [l, +[...ids].filter((id) => scs.includes(faces.get(id).script)).reduce((s, id) => s + faces.get(id).woff.byteLength / 1024, 0).toFixed(1)]))]));
console.log('per page KB:', JSON.stringify(perPage));
await writeFile(new URL('perpage.json', OUT), JSON.stringify(perPage));
await writeFile(new URL('report.json', OUT), JSON.stringify({ report, perVariant: Object.fromEntries(Object.entries(variantFaces).map(([v, ids]) => [v, +[...ids].reduce((s, id) => s + faces.get(id).woff.byteLength / 1024, 0).toFixed(1)])) }, null, 1));
console.table(report);
console.log('per variant KB:', Object.fromEntries(Object.entries(variantFaces).map(([v, ids]) => [v, [...ids].reduce((s, id) => s + faces.get(id).woff.byteLength / 1024, 0).toFixed(1)])));
