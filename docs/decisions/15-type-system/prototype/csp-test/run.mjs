import { createSubsetter, toWoff, browserDeflate } from './fontsubset.mjs';
const out = {};
try {
  const hb = await createSubsetter(await (await fetch('./harfbuzz-subset.wasm')).arrayBuffer());
  const master = new Uint8Array(await (await fetch('./master.ttf')).arrayBuffer());
  const text = document.body.textContent;
  const t0 = performance.now();
  const sfnt = hb.subset(master, [...new Set([...text].map(c => c.codePointAt(0)))], { wght: 400 });
  const woff = await toWoff(sfnt, browserDeflate);
  out.subsetMs = Math.round(performance.now() - t0); out.woffBytes = woff.byteLength;
  // A: FontFace from bytes (what a preview can use without any font-src change)
  const fa = new FontFace('SubA', woff); await fa.load(); document.fonts.add(fa); out.fontFaceFromBytes = fa.status;
  // B: FontFace from a blob: URL (needs font-src blob:)
  const url = URL.createObjectURL(new Blob([woff], { type: 'font/woff' }));
  const fb = new FontFace('SubB', `url(${url})`);
  try { await fb.load(); out.fontFaceFromBlobUrl = fb.status; } catch (e) { out.fontFaceFromBlobUrl = 'blocked: ' + e.name; }
  document.getElementById('a').className = 'a';
} catch (e) { out.error = String(e); }
window.__result = out;
