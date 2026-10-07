const { chromium } = require('../t15/tools/node_modules/playwright-core');
const UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36';
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--disable-blink-features=AutomationControlled']});
for (const g of process.argv.slice(2)) {
  const p=await b.newPage({userAgent:UA,viewport:{width:1440,height:900}});
  try{ await p.goto(g,{waitUntil:'domcontentloaded',timeout:40000}); await p.waitForTimeout(4000);
    for(let i=0;i<6;i++){await p.mouse.wheel(0,2000);await p.waitForTimeout(600);}
    const host=new URL(g).hostname.replace(/^www\./,'');
    const links=await p.evaluate(()=>[...document.querySelectorAll('a[href]')].map(a=>({h:a.href,t:(a.innerText||a.title||'').trim().slice(0,60)})));
    const ext=[...new Map(links.filter(l=>/^https?:/.test(l.h)&&!l.h.includes(host)&&!/twitter|x\.com|instagram|facebook|linkedin|youtube|pinterest|tiktok|dribbble|behance|github|google|apple\.com\/app|discord|threads|medium/.test(l.h)).map(l=>[new URL(l.h).origin,l])).values()];
    console.log(`## ${g} title="${(await p.title()).slice(0,60)}" external=${ext.length}`);
    ext.slice(0,80).forEach(l=>console.log(l.h.split('?')[0]+'  '+l.t.replace(/\s+/g,' ')));
  }catch(e){console.log(`## ${g} ERROR ${String(e).slice(0,120)}`)}
  await p.close();}
await b.close();})();
