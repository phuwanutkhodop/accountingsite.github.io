from marks6 import gd, gb, gw, text, PAL, gw
B, BI = 'BM700.ttf', 'BM700i.ttf'

def name_d(p, cx, base, maxw):
    t = "D.A. ACCOUNTING & CONSULTING"
    w1 = sum(gw("CG600.ttf", c, 1) if c != ' ' else .28 for c in t) + .2 * (len(t) - 1)
    size = min(17, maxw / w1)
    return f'<path d="{text("CG600.ttf", t, size, cx, base, .2)}" style="fill: {p["ink"]}"></path>'

def mono(fn, f=.32, dy=0.0, sa=1.0, H=190):
    """D and A in font fn, cap height ~H. A's left edge overlaps D by fraction f of D's width.
    dy shifts A down (fraction of H); sa scales A. Returns path d, bbox."""
    db = gb(fn, 'D', 100); capD = -db[1] if db[1] < 0 else db[3]
    size = H / (db[3] / 100)
    d0 = gb(fn, 'D', size); a0 = gb(fn, 'A', size * sa)
    xD = 20 - d0[0]; base = 20 + d0[3]
    dw = d0[2] - d0[0]
    xA = (xD + d0[2]) - f * dw - a0[0]
    bA = base + dy * H
    d = gd(fn, 'D', size, xD, base) + ' ' + gd(fn, 'A', size * sa, xA, bA)
    x1 = max(xD + d0[2], xA + a0[2]); y1 = max(base, bA)
    return d, (20, 20 + d0[3] - d0[3], x1, y1)

def xor_mark(fn, **kw):
    d, (x0, y0, x1, y1) = mono(fn, **kw)
    w = x1 - x0
    def build(p):
        return f'<path d="{d}" style="fill: {p["ink"]}; fill-rule: evenodd"></path>' + name_d(p, (x0 + x1) / 2, y1 + 44, w)
    vb = f'0 0 {x1 + 20:.0f} {y1 + 64:.0f}'
    return build, vb

def stacked_mark(fn, ov=.35):
    db = gb(fn, 'D', 100); size = 150 / (db[3] / 100)
    d0, a0 = gb(fn, 'D', size), gb(fn, 'A', size)
    cx = 160
    xD = cx - (d0[0] + d0[2]) / 2; bD = 20 + d0[3]
    xA = cx - (a0[0] + a0[2]) / 2; bA = bD + a0[3] * (1 - ov)
    d = gd(fn, 'D', size, xD, bD) + ' ' + gd(fn, 'A', size, xA, bA)
    def build(p):
        return f'<path d="{d}" style="fill: {p["ink"]}; fill-rule: evenodd"></path>' + name_d(p, cx, bA + 44, 260)
    return build, f'0 0 320 {bA + 64:.0f}'

def inside_mark(fn):
    db = gb(fn, 'D', 100); size = 200 / (db[3] / 100)
    d0 = gb(fn, 'D', size); a0 = gb(fn, 'A', size * .62)
    xD = 30 - d0[0]; base = 20 + d0[3]
    cxA = xD + d0[0] + (d0[2] - d0[0]) * .52
    xA = cxA - (a0[0] + a0[2]) / 2
    d = gd(fn, 'D', size, xD, base) + ' ' + gd(fn, 'A', size * .62, xA, base - (d0[3] - a0[3]) / 2)
    x1 = xD + d0[2]
    def build(p):
        return f'<path d="{d}" style="fill: {p["ink"]}; fill-rule: evenodd"></path>' + name_d(p, (x1 + 30) / 2 + 0, base + 44, x1)
    return build, f'0 0 {x1 + 30:.0f} {base + 64:.0f}'

def boxed_mark(fn, shape):
    d, (x0, y0, x1, y1) = mono(fn, H=150)
    w, h = x1 - x0, y1 - y0
    pad = 34; bx0, by0, bx1, by1 = x0 - pad, y0 - pad, x1 + pad, y1 + pad
    if shape == 'square':
        s = max(bx1 - bx0, by1 - by0); cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
        frame = f'M{cx - s/2:.1f},{cy - s/2:.1f} h{s:.1f} v{s:.1f} h{-s:.1f} Z'
        top, bottom = cy - s / 2, cy + s / 2
    else:
        r = max(w, h) / 2 + pad + 6; cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
        frame = f'M{cx - r:.1f},{cy:.1f} a{r:.1f},{r:.1f} 0 1 0 {2*r:.1f},0 a{r:.1f},{r:.1f} 0 1 0 {-2*r:.1f},0 Z'
        top, bottom = cy - r, cy + r
    def build(p):
        return (f'<path d="{frame} {d}" style="fill: {p["ink"]}; fill-rule: evenodd"></path>'
                + name_d(p, cx, bottom + 40, 300))
    ox = min(0, cx - 170)
    return build, f'{cx - 170:.0f} {top - 16:.0f} 340 {bottom - top + 76:.0f}'

def ruled_mark(fn):
    d, (x0, y0, x1, y1) = mono(fn)
    def build(p):
        r = (f'<rect x="{x0}" y="{y1 + 16:.1f}" width="{x1 - x0:.1f}" height="2.2" style="fill: {p["ink"]}"></rect>'
             f'<rect x="{x0}" y="{y1 + 23:.1f}" width="{x1 - x0:.1f}" height="2.2" style="fill: {p["ink"]}"></rect>')
        return f'<path d="{d}" style="fill: {p["ink"]}; fill-rule: evenodd"></path>' + r + name_d(p, (x0 + x1) / 2, y1 + 66, x1 - x0)
    return build, f'0 0 {x1 + 20:.0f} {y1 + 86:.0f}'

V = [
 ('50', 'Depth · light overlap',     xor_mark(B, f=.18)),
 ('51', 'Depth · medium (45)',       xor_mark(B, f=.32)),
 ('52', 'Depth · deep overlap',      xor_mark(B, f=.5)),
 ('53', 'Type · Playfair Display',   xor_mark('Playfair800.ttf')),
 ('54', 'Type · DM Serif Display',   xor_mark('DMSerif.ttf')),
 ('55', 'Type · Cinzel',             xor_mark('Cinzel700.ttf')),
 ('56', 'Type · Libre Caslon',       xor_mark('LibreCaslonD.ttf')),
 ('57', 'Type · Cormorant',          xor_mark('CG700.ttf')),
 ('58', 'Arrangement · offset',      xor_mark(B, dy=.2)),
 ('59', 'Arrangement · stacked',     stacked_mark(B)),
 ('60', 'Arrangement · A inside D',  inside_mark(B)),
 ('61', 'Arrangement · italic',      xor_mark(BI, f=.36)),
 ('62', 'Frame · square block',      boxed_mark(B, 'square')),
 ('63', 'Frame · round',             boxed_mark(B, 'circle')),
 ('64', 'Frame · double underline',  ruled_mark(B)),
]
CONCEPTS = [(f'Concept{n}', f'{n} · {t}', vb, fn) for n, t, (fn, vb) in V]
