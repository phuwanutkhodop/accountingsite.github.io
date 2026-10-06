import { readFile } from 'node:fs/promises';
import { createSubsetter } from './fontsubset.mjs';
const hb = await createSubsetter(await readFile('node_modules/harfbuzzjs/dist/harfbuzz-subset.wasm'));
const dec = new TextDecoder('gb18030'); const gb = new Set();
for (let a = 0xb0; a <= 0xf7; a++) for (let b = 0xa1; b <= 0xfe; b++) { const s = dec.decode(new Uint8Array([a, b])); if (s.length === 1 && s !== '�') gb.add(s.codePointAt(0)); }
const extra = []; for (const [x, y] of [[0x20, 0x7e], [0xa0, 0xff], [0x2010, 0x2027], [0x3000, 0x303f], [0xff00, 0xffef]]) for (let c = x; c <= y; c++) extra.push(c);
const cps = [...gb, ...extra];
for (const f of ['NotoSerifSC[wght].ttf', 'NotoSansSC[wght].ttf']) {
  const m = new Uint8Array(await readFile('../dl/' + f));
  const t0 = performance.now(); const v = hb.subset(m, cps); const s = hb.subset(m, cps, { wght: 400 });
  console.log(f, `full ${(m.length / 1048576).toFixed(1)} MB · GB2312 (${gb.size} Han) variable ${(v.length / 1048576).toFixed(2)} MB · one static weight ${(s.length / 1048576).toFixed(2)} MB · ${Math.round(performance.now() - t0)} ms`);
}
