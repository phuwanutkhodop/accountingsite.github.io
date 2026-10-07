// PROTOTYPE (#21) — strict Mustache subset (decision #16-5), pure: no DOM, no I/O.
// Supports {{name}} {{a.b}} {{#x}}…{{/x}} {{^x}}…{{/x}} {{! comment}} and {{.}} inside a list of strings.
// Forbids {{{raw}}}, {{&raw}}, partials {{>x}} and delimiter changes {{=…=}}: a template error.
// A plain variable that is missing is an error; a missing section key is false (how optional fields work).

const esc = (s) => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;').replace(/'/g, '&#39;');

export function parse(src) {
  const root = { kind: 'root', children: [] };
  const stack = [root];
  const re = /\{\{(\{?)([#^\/!>&=]?)\s*([^}]*?)\s*\}?\}\}/g;
  let last = 0, m;
  while ((m = re.exec(src))) {
    if (m.index > last) stack.at(-1).children.push({ kind: 'text', value: src.slice(last, m.index) });
    last = re.lastIndex;
    const [, brace, sigil, name] = m;
    if (brace || sigil === '&') throw new Error(`raw output is forbidden: ${m[0]}`);
    if (sigil === '>' || sigil === '=') throw new Error(`partials and delimiter changes are forbidden: ${m[0]}`);
    if (sigil === '!') continue;
    if (!/^(\.|[a-zA-Z_][\w-]*(\.[a-zA-Z_][\w-]*)*)$/.test(name)) throw new Error(`bad tag name: ${m[0]}`);
    if (sigil === '#' || sigil === '^') {
      const node = { kind: sigil === '#' ? 'section' : 'inverted', name, children: [] };
      stack.at(-1).children.push(node);
      stack.push(node);
    } else if (sigil === '/') {
      const open = stack.pop();
      if (!open || open.name !== name) throw new Error(`unbalanced {{/${name}}}`);
    } else stack.at(-1).children.push({ kind: 'var', name });
  }
  if (stack.length !== 1) throw new Error(`unclosed {{#${stack.at(-1).name}}}`);
  if (last < src.length) root.children.push({ kind: 'text', value: src.slice(last) });
  return root;
}

/** Every name the template reads, for the library check. */
export function names(node, out = new Set()) {
  if (node.name && node.name !== '.') out.add(node.name.split('.')[0]);
  (node.children || []).forEach((c) => names(c, out));
  return out;
}

function lookup(ctx, name) {
  if (name === '.') return { found: true, value: ctx[0] };
  const [head, ...rest] = name.split('.');
  for (let i = 0; i < ctx.length; i++) {
    const c = ctx[i];
    if (c && typeof c === 'object' && head in c) {
      let v = c[head];
      for (const k of rest) { if (v == null || !(k in Object(v))) return { found: false }; v = v[k]; }
      return { found: true, value: v };
    }
  }
  return { found: false };
}

export function render(tree, data) {
  const out = [];
  const walk = (node, ctx) => {
    for (const n of node.children) {
      if (n.kind === 'text') out.push(n.value);
      else if (n.kind === 'var') {
        const r = lookup(ctx, n.name);
        if (!r.found || r.value == null || typeof r.value === 'object') throw new Error(`missing value: {{${n.name}}}`);
        out.push(esc(r.value));
      } else {
        const r = lookup(ctx, n.name);
        const v = r.found ? r.value : undefined;
        const truthy = Array.isArray(v) ? v.length > 0 : !!v;
        if (n.kind === 'inverted') { if (!truthy) walk(n, ctx); continue; }
        if (!truthy) continue;
        if (Array.isArray(v)) v.forEach((item) => walk(n, [item, ...ctx]));
        else walk(n, typeof v === 'object' ? [v, ...ctx] : ctx);
      }
    }
  };
  walk(tree, [data]);
  return out.join('');
}
