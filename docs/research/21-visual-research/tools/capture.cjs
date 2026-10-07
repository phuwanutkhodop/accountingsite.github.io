// Visual research capture: node capture.cjs <outDir> <url> [url...]
// For each URL: desktop 1440 and phone 390 viewport frames while scrolling, a full-page shot, and a signals JSON
// (fonts, libraries, notable CSS/DOM techniques) used later to measure how rare each technique is.
const { chromium, devices } = require('../t15/tools/node_modules/playwright-core');
const fs = require('fs'), path = require('path');

const UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36';
const CSS_SIGNALS = {
  'scroll-driven animation': /animation-timeline\s*:|scroll-timeline|view-timeline/i,
  'view transitions': /view-transition-name|::view-transition/i,
  'blend modes': /mix-blend-mode\s*:\s*(difference|exclusion|multiply|screen|overlay)/i,
  'clip-path shapes/reveals': /clip-path\s*:\s*(polygon|inset|circle|ellipse|path)/i,
  'CSS masks': /(-webkit-)?mask(-image)?\s*:/i,
  'backdrop blur': /backdrop-filter/i,
  'text stroke / outline type': /-webkit-text-stroke/i,
  'variable-font axes': /font-variation-settings/i,
  'drop caps (initial-letter / first-letter)': /initial-letter|::first-letter/i,
  'multi-column text': /column-count|columns\s*:\s*\d/i,
  'hanging punctuation': /hanging-punctuation/i,
  'text-wrap balance/pretty': /text-wrap\s*:\s*(balance|pretty)/i,
  'subgrid': /subgrid/i,
  'container queries': /@container/i,
  'sticky positioning': /position\s*:\s*sticky/i,
  '3D transforms': /perspective\s*:|preserve-3d|rotate[XY]\(/i,
  'custom cursor (cursor:none)': /cursor\s*:\s*none/i,
  'grain/noise texture': /noise|grain/i,
  'oldstyle/tabular numerals': /font-variant-numeric|"tnum"|"onum"|"lnum"/i,
  'small caps': /font-variant(-caps)?\s*:\s*(all-)?small-caps|"smcp"|"c2sc"/i,
  'gradient text': /background-clip\s*:\s*text/i,
  'marquee keyframes': /@keyframes[^{]*(marquee|ticker|scroll-x|loop)/i,
  'writing-mode vertical text': /writing-mode\s*:\s*vertical/i,
  'shape-outside text wrap': /shape-outside/i,
};
const LIB_SIGNALS = { gsap: /gsap|ScrollTrigger/i, lenis: /lenis/i, 'locomotive-scroll': /locomotive-scroll/i, 'three.js / WebGL': /three(\.module)?\.js|THREE\.|webgl/i, barba: /barba/i, swup: /swup/i, splitting: /splitting|SplitText|split-type/i, framer: /framer\.com|framerusercontent/i, webflow: /webflow/i, lottie: /lottie/i, rive: /rive\.app|@rive-app/i };

async function dismiss(page) {
  for (const re of [/accept all/i, /accept/i, /agree/i, /allow all/i, /^ok$/i, /got it/i, /i understand/i, /ยอมรับ/]) {
    const b = page.getByRole('button', { name: re }).first();
    try { if (await b.isVisible({ timeout: 300 })) { await b.click({ timeout: 1000 }); await page.waitForTimeout(400); return; } } catch {}
  }
}

async function shoot(browser, url, dir, mode) {
  const ctx = await browser.newContext(mode === 'phone'
    ? { ...devices['iPhone 13'], userAgent: devices['iPhone 13'].userAgent, deviceScaleFactor: 2 }
    : { viewport: { width: 1440, height: 900 }, userAgent: UA, deviceScaleFactor: 1 });
  const page = await ctx.newPage();
  const css = [], scripts = [];
  page.on('response', async (r) => {
    try {
      const t = r.request().resourceType();
      if (t === 'stylesheet' && css.length < 40) css.push(await r.text());
      if (t === 'script' && scripts.length < 60) scripts.push(r.url() + '\n' + (await r.text()).slice(0, 200000));
    } catch {}
  });
  const out = { url, mode, ok: false };
  try {
    await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
    await page.waitForTimeout(3500);
    await dismiss(page);
    const H = mode === 'phone' ? 844 : 900;
    const total = await page.evaluate(() => document.documentElement.scrollHeight);
    const max = mode === "phone" ? 6 : 8;
    let steps = Math.min(max, Math.max(1, Math.ceil(total / H)));
    // Smooth-scroll sites (Lenis, Locomotive…) report a one-screen document; drive them by wheel anyway.
    if (total <= H * 1.3) steps = max;
    for (let i = 0; i < steps; i++) {
      await page.mouse.wheel(0, i === 0 ? 0 : H);
      await page.waitForTimeout(1100);
      await page.screenshot({ path: path.join(dir, `${mode}-${String(i).padStart(2, '0')}.jpg`), type: 'jpeg', quality: 66 });
    }
    if (mode === 'desktop') {
      await page.evaluate(() => window.scrollTo(0, 0)); await page.waitForTimeout(800);
      const dom = await page.evaluate(() => {
        const cs = (el) => el && getComputedStyle(el);
        const h = document.querySelector('h1') || document.querySelector('h2');
        const fams = [...new Set([...document.fonts].filter((f) => f.status === 'loaded').map((f) => f.family.replace(/["']/g, '')))];
        return {
          title: document.title,
          fontsLoaded: fams.slice(0, 12),
          headingFont: h ? cs(h).fontFamily.slice(0, 80) + ' / ' + cs(h).fontSize + ' / ' + cs(h).fontWeight : null,
          bodyFont: cs(document.body).fontFamily.slice(0, 80) + ' / ' + cs(document.body).fontSize,
          bg: cs(document.body).backgroundColor, fg: cs(document.body).color,
          canvas: document.querySelectorAll('canvas').length, video: document.querySelectorAll('video').length,
          svg: document.querySelectorAll('svg').length, imgs: document.images.length,
          spans: document.querySelectorAll('span').length, links: document.links.length,
          height: document.documentElement.scrollHeight,
          customCursor: getComputedStyle(document.body).cursor === 'none' || !!document.querySelector('[class*="cursor" i]'),
        };
      });
      const cssText = css.join('\n'), jsText = scripts.join('\n');
      out.dom = dom;
      out.css = Object.fromEntries(Object.entries(CSS_SIGNALS).map(([k, re]) => [k, re.test(cssText)]));
      out.libs = Object.entries(LIB_SIGNALS).filter(([, re]) => re.test(jsText)).map(([k]) => k);
      out.cssBytes = cssText.length;
    }
    out.ok = true;
  } catch (e) { out.error = String(e).slice(0, 200); }
  await ctx.close();
  return out;
}

(async () => {
  const [outDir, ...urls] = process.argv.slice(2);
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args: ['--disable-blink-features=AutomationControlled'] });
  for (const url of urls) {
    const slug = url.replace(/^https?:\/\/(www\.)?/, '').replace(/[^\w.-]+/g, '_').replace(/_+$/, '').slice(0, 60);
    const dir = path.join(outDir, slug); fs.mkdirSync(dir, { recursive: true });
    const d = await shoot(browser, url, dir, 'desktop');
    const p = await shoot(browser, url, dir, 'phone');
    fs.writeFileSync(path.join(dir, 'signals.json'), JSON.stringify({ ...d, phoneOk: p.ok, phoneError: p.error }, null, 1));
    console.log(`${d.ok ? 'ok ' : 'ERR'} ${slug} ${d.error || ''} ${d.libs ? '[' + d.libs.join(',') + ']' : ''}`);
  }
  await browser.close();
})();
