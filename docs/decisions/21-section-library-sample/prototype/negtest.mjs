import { presets } from './library.mjs';
const bad = [
  ['raw output', { markup: '<div class="s__in x">{{{title}}}</div>', css: '.x{gap:var(--space-2)}' }],
  ['partial', { markup: '<div class="s__in x">{{>evil}}</div>', css: '.x{gap:var(--space-2)}' }],
  ['undeclared field', { markup: '<div class="s__in x">{{price}}</div>', css: '.x{gap:var(--space-2)}' }],
  ['literal colour', { markup: '<div class="s__in x">{{title}}</div>', css: '.x{color:#ff0000}' }],
  ['literal size', { markup: '<div class="s__in x">{{title}}</div>', css: '.x{font-size:18px}' }],
  ['unscoped selector', { markup: '<div class="s__in x">{{title}}</div>', css: 'body{gap:var(--space-2)}' }],
  ['odd breakpoint', { markup: '<div class="s__in x">{{title}}</div>', css: '@container section (min-width: 33rem){.x{gap:var(--space-2)}}' }],
  ['event handler', { markup: '<div class="s__in x"><img onerror="x" alt="{{title}}"></div>', css: '.x{gap:var(--space-2)}' }],
  ['font literal', { markup: '<div class="s__in x">{{title}}</div>', css: '.x{font-family:Arial}' }],
];
presets.length = 0;
for (const [name, b] of bad) presets.push({ id: name.replace(/ /g, '-'), version: '1.0', type: 'cta', options: { tone: 'plain' }, ...b });
await import('./build.mjs').catch(e => console.log('build threw:', e.message));
