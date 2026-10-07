import { content } from './content.mjs';
const flat=(v)=>typeof v==='string'?[v]:Array.isArray(v)?v.flatMap(flat):Object.values(v).flatMap(flat);
const cps=new Set([...flat(content.zh).join('')].map(c=>c.codePointAt(0)));
const css=await (await fetch('https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400&display=swap',{headers:{'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0 Safari/537.36'}})).text();
const blocks=[...css.matchAll(/src: url\((.+?)\).*?unicode-range: (.+?);/gs)];
let need=[],total=0;
for(const [,url,ur] of blocks){
  const rs=ur.split(',').map(s=>s.trim().replace('U+','').split('-').map(h=>parseInt(h,16)));
  const hit=[...cps].some(cp=>rs.some(([a,b=a])=>cp>=a&&cp<=b));
  if(hit) need.push(url);
}
for(const u of need){const r=await fetch(u);total+=(await r.arrayBuffer()).byteLength;}
console.log(`slices: ${blocks.length}, needed for zh specimen: ${need.length}, bytes: ${(total/1024).toFixed(1)} KB (WOFF2)`);
