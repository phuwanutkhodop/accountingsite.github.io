const {chromium}=require('../t15/tools/node_modules/playwright-core');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome'});
const out=process.argv[2];
for (const [w,name,st] of [[1280,'d-a-th',{set:'a',scheme:'light',lang:'th'}],[1280,'d-b-en',{set:'b',scheme:'dark',lang:'en'}],[390,'p-a-zh',{set:'a',scheme:'light',lang:'zh'}],[390,'p-b-th',{set:'b',scheme:'light',lang:'th'}]]){
 const p=await b.newPage({viewport:{width:w,height:900}}); const errs=[];
 p.on('pageerror',e=>errs.push(e.message)); p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
 await p.goto('file://'+out+'/local.html');
 await p.evaluate(s=>localStorage.setItem('lib21',JSON.stringify({width:'full',labels:'on',...s})),st);
 await p.reload(); await p.evaluate(()=>document.fonts.ready);
 const info=await p.evaluate(()=>({overflowX:document.documentElement.scrollWidth>innerWidth, wide:[...document.querySelectorAll('.site *')].filter(e=>e.getBoundingClientRect().right>innerWidth+1).slice(0,3).map(e=>e.className)}));
 const el=await p.$('.frame'); await el.screenshot({path:out+'/'+name+'.png'});
 console.log(name,JSON.stringify(info),errs);
 await p.close();}
await b.close();})();
