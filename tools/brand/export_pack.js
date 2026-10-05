// Step 2 of the D.A. brand export pack: render PNG and PDF files with Chromium (the same engine the designs were made in).
//   node tools/brand/export_pack.js OUT_DIR        (after: python tools/brand/export_pack.py OUT_DIR)
// Needs Node and Playwright with Chromium. Set CHROMIUM_PATH to use a specific Chromium build.
const fs = require('fs'), path = require('path');
const { chromium } = require('playwright');

const out = path.resolve(process.argv[2]);
const jobs = JSON.parse(fs.readFileSync(path.join(out, 'jobs.json'), 'utf8'))
  .map(j => Object.fromEntries(Object.entries(j).map(([k, v]) => [k, ['src', 'png', 'pdf', 'master', 'tile'].includes(k) ? path.resolve(out, v) : v])));
const size = svg => { const m = svg.match(/viewBox="([\d.\s-]+)"/)[1].trim().split(/\s+/).map(Number); return [m[2], m[3]]; };
const page0 = (body, bg = 'transparent') => `<!doctype html><html><head><meta charset="utf-8"><style>html,body{margin:0;padding:0;background:${bg}}svg{display:block}</style></head><body>${body}</body></html>`;
// set the artwork's pixel size on its <svg> (replacing any width/height already there)
const sized = (svg, W, H) => svg.replace('<svg ', `<svg width="${W}" height="${H}" `).replace(/<svg([^>]*?) width="[\d.]+" height="[\d.]+"([^>]*?) width="[\d.]+" height="[\d.]+"/, `<svg$1 width="${W}" height="${H}"$2`);

(async () => {
  const browser = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {});
  for (const j of jobs) {
    const target = j.png || j.pdf;
    fs.mkdirSync(path.dirname(target), { recursive: true });
    if (j.tile) {                                   // ready-tiled swatch from the master tile, repeated by the browser
      const svg = fs.readFileSync(j.tile, 'utf8'); const [w, h] = size(svg);
      const url = 'data:image/svg+xml;base64,' + Buffer.from(svg).toString('base64');
      const p = await browser.newPage({ viewport: { width: j.width, height: j.width } });
      await p.setContent(page0(`<div style="width:${j.width}px;height:${j.width}px;background:url(${url}) 0 0/${w * j.scale}px ${h * j.scale}px repeat"></div>`));
      await p.screenshot({ path: target, clip: { x: 0, y: 0, width: j.width, height: j.width } });
      await p.close(); continue;
    }
    const svg = fs.readFileSync(j.src, 'utf8'); const [w, h] = size(svg);
    if (j.png) {
      const W = j.width, H = Math.round(W * h / w);
      const p = await browser.newPage({ viewport: { width: W, height: H } });
      await p.setContent(page0(sized(svg, W, H), j.page_bg || 'transparent'));   // background variants: page matches, so no edge blends with white
      await p.screenshot({ path: target, clip: { x: 0, y: 0, width: W, height: H }, omitBackground: !!j.transparent });
      await p.close();
    } else {                                        // vector PDF, 1 unit = 1 CSS px = 0.75 pt
      // Chromium clips a PDF page's content at the last whole pixel and shrinks it slightly when the page size is
      // fractional; so print on a whole-pixel page with spare room, artwork at the top-left, untouched. Step 3
      // (export_pack.py --finish) then trims the page to the artwork's exact size.
      // Chromium also snaps the <svg> box itself to whole pixels (and rescales the drawing to fit), so widen the
      // viewBox to whole units at exactly 1 unit = 1 px; the extra room is empty and is trimmed away in step 3.
      const [vx, vy] = svg.match(/viewBox="([\d.\s-]+)"/)[1].trim().split(/\s+/).map(Number);
      const W2 = Math.ceil(w), H2 = Math.ceil(h);
      const svg2 = sized(svg, W2, H2).replace(/viewBox="[^"]*"/, `viewBox="${vx} ${vy} ${W2} ${H2}" preserveAspectRatio="xMinYMin meet"`);
      const p = await browser.newPage();
      await p.setContent(page0(svg2));
      await p.pdf({ path: target, width: `${W2 + 2}px`, height: `${H2 + 2}px`, printBackground: true, margin: { top: 0, right: 0, bottom: 0, left: 0 }, pageRanges: '1' });
      await p.close();
    }
  }
  await browser.close();
  console.log(jobs.length, 'files rendered');
})();
