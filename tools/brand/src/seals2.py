import math
from seals import *          # arc_text, ring, disc, flower, mono, mono_patterned, lattice, seps, FLAT, PAL, NAME, SUB, C, F, petals

def top_bottom(i, rt=107, rb=121, size=13):
    return arc_text(NAME, size, C, C, rt, 'top', track=.13, fill=i) + arc_text(SUB, size, C, C, rb, 'bottom', track=.13, fill=i)
def flower_ring(r, n, size, c, offset=0):
    return ''.join(flower(C + r * math.cos(2 * math.pi * k / n + offset), C + r * math.sin(2 * math.pi * k / n + offset), size, c) for k in range(n))
def dot_ring(r, n, rad, c):
    return ''.join(f'<circle cx="{F(C + r * math.cos(2 * math.pi * k / n))}" cy="{F(C + r * math.sin(2 * math.pi * k / n))}" r="{rad}" style="fill: {c}"></circle>' for k in range(n))
def lozenge_chain(r, n, hw, hh, line, fl, fill=None):
    """A necklace of diamonds around the ring, each with a flower at its heart."""
    out = ''
    for k in range(n):
        a = 360 * k / n
        x, y = C + r * math.cos(math.radians(a)), C + r * math.sin(math.radians(a))
        lz = f'M0,{-hh} L{hw},0 L0,{hh} L{-hw},0 Z'
        inner = f'M0,{-hh * .62} L{hw * .62},0 L0,{hh * .62} L{-hw * .62},0 Z'
        st = f'fill: {fill}' if fill else 'fill: none'
        out += (f'<g transform="translate({F(x)},{F(y)}) rotate({F(a + 90)})"><path d="{lz}" style="{st}; stroke: {line}; stroke-width: .9"></path>'
                f'<path d="{inner}" style="fill: none; stroke: {line}; stroke-width: .7"></path>'
                f'<path d="{petals(0, 0, hw * .42) + petals(0, 0, hw * .42 * .52, rot=45, width=.4)}" style="fill: {fl}"></path></g>')
    return out
def microtext(r, size, c):
    unit = 'D.A. ACCOUNTING & CONSULTING · '
    from marks6 import gw
    w = sum(gw('CG600.ttf', ch, size) if ch != ' ' else size * .3 for ch in unit) + .1 * size * len(unit)
    reps = max(1, int(2 * math.pi * r / w))
    return arc_text((unit * reps).strip(' ·'), size, C, C, r, 'top', track=.1, fill=c)
def guilloche(r0, amp, k, lines, c, w=.5):
    out = ''
    for L in range(lines):
        ph = 2 * math.pi * L / lines / k
        pts = []
        for t in range(0, 721):
            th = 2 * math.pi * t / 720
            rr = r0 + amp * math.sin(k * th + ph * k)
            pts.append(f'{F(C + rr * math.cos(th))},{F(C + rr * math.sin(th))}')
        out += f'<polyline points="{" ".join(pts)}" style="fill: none; stroke: {c}; stroke-width: {w}"></polyline>'
    return out
def base_rings(i, outer=True):
    return (ring(C, C, 140, i, 3) + ring(C, C, 133, i, 1) if outer else '') + ring(C, C, 96, i, 1) + ring(C, C, 90, i, 3)

# ---- from 161: classic with patterned monogram ----
def a172(p):   # flowers fill the outer band, all the way round
    i = p['ink']; r = FLAT[p['bg']][0]
    s = ring(C, C, 146, i, 3) + flower_ring(140, 48, 3.2, r) + ring(C, C, 134, i, 1) + base_rings(i, False)
    return s + top_bottom(i) + seps(114, 6, r) + mono_patterned(C, C + 4, 118, p)
def a173(p):   # a flower at each of the four quarters, cutting the outer rings like a compass
    i = p['ink']; r = FLAT[p['bg']][0]
    s = base_rings(i) + top_bottom(i)
    for a in (0, 90, 180, 270):
        x, y = C + 136.5 * math.cos(math.radians(a)), C + 136.5 * math.sin(math.radians(a))
        s += disc(x, y, 9, p['bg']) + flower(x, y, 9, i)
    return s + mono_patterned(C, C + 4, 118, p)
def a174(p):   # a chain of small flowers just inside the name, round the monogram
    i = p['ink']; r = FLAT[p['bg']][0]
    s = ring(C, C, 140, i, 3) + ring(C, C, 133, i, 1) + ring(C, C, 96, i, 1) + flower_ring(88, 36, 3, r) + ring(C, C, 80, i, 2)
    return s + top_bottom(i) + seps(114, 6, i) + mono_patterned(C, C + 4, 108, p)
def a175(p):   # two-tone: the rings in rose, the type and monogram in oxblood
    i = p['ink']; r = FLAT[p['bg']][0]
    s = ring(C, C, 140, r, 3) + ring(C, C, 133, r, 1) + ring(C, C, 96, r, 1) + ring(C, C, 90, r, 3)
    return s + top_bottom(i) + seps(114, 6, r) + mono_patterned(C, C + 4, 118, p)
def a176(p):   # microtext ring (banknote-fine) between the outer rings
    i = p['ink']
    s = ring(C, C, 144, i, 2) + microtext(136.5, 4.6, i) + ring(C, C, 132, i, 1) + base_rings(i, False)
    return s + top_bottom(i, rt=105, rb=119) + seps(112, 6, i) + mono_patterned(C, C + 4, 118, p)

# ---- from 163: lattice band ----
def band(p, inner_r, outer_r, content, tag):
    u = p['bg'][1:] + tag
    return (f'<mask id="m{u}"><rect x="0" y="0" width="300" height="300" style="fill: #fff"></rect>{disc(C, C, inner_r, "#000")}</mask>'
            f'<g mask="url(#m{u})">{content}</g>')
def b177(p):   # a wider band with a larger lattice
    i = p['ink']
    s = ring(C, C, 140, i, 3) + ring(C, C, 133, i, 1) + top_bottom(i)
    s += band(p, 62, 92, lattice(C, C, 92, p, s=22, tag='b177'), 'b177') + ring(C, C, 92, i, 1.5) + ring(C, C, 62, i, 1.5)
    return s + mono(C, C + 3, 80, i)
def b178(p):   # the band carries flowers only, in three staggered rows
    i = p['ink']; fc = FLAT[p['bg']][1]
    s = ring(C, C, 140, i, 3) + ring(C, C, 133, i, 1) + top_bottom(i)
    s += disc(C, C, 92, i) + disc(C, C, 72, p['bg'])
    s += flower_ring(86, 30, 3.4, fc) + flower_ring(78, 30, 3.4, fc, math.pi / 30)
    s += ring(C, C, 92, i, 1.5) + ring(C, C, 72, i, 1.5)
    return s + mono(C, C + 3, 92, i)
def b179(p):   # a necklace of diamonds, each with a flower, forms the band
    i = p['ink']; r = FLAT[p['bg']][0]
    s = ring(C, C, 140, i, 3) + ring(C, C, 133, i, 1) + top_bottom(i)
    s += ring(C, C, 93, i, 1) + lozenge_chain(82, 24, 10.5, 9.5, r, i) + ring(C, C, 71, i, 1)
    return s + mono_patterned(C, C + 3, 96, p)
def b180(p):   # the band in rose on paper, light; the monogram patterned
    i = p['ink']; r = FLAT[p['bg']][0]
    s = ring(C, C, 140, i, 3) + ring(C, C, 133, i, 1) + top_bottom(i)
    rc = FLAT[p['bg']][0]
    lt = lattice(C, C, 92, p, s=16, tag='b180').replace(f'fill: {p["ink"]}"></circle>', f'fill: {p["bg"]}"></circle>', 1)
    s += band(p, 72, 92, lt, 'b180') + ring(C, C, 92, r, 1.5) + ring(C, C, 72, r, 1.5)
    return s + mono_patterned(C, C + 3, 96, p)
def b181(p):   # two bands: a thin lattice ring and a chain of flowers
    i = p['ink']; r = FLAT[p['bg']][0]
    s = ring(C, C, 140, i, 3) + ring(C, C, 133, i, 1) + top_bottom(i)
    s += band(p, 80, 92, lattice(C, C, 92, p, s=12, tag='b181'), 'b181') + ring(C, C, 92, i, 1.2) + ring(C, C, 80, i, 1.2)
    s += flower_ring(73, 28, 2.8, r) + ring(C, C, 66, i, 1)
    return s + mono(C, C + 3, 84, i)

# ---- from 170: flower seal ----
def c182(p):   # the great flower, petals softly filled in rose behind the monogram
    i = p['ink']; r = FLAT[p['bg']][0]
    s = ring(C, C, 140, i, 3) + ring(C, C, 133, i, 1) + top_bottom(i) + ring(C, C, 94, i, 1)
    s += f'<path d="{petals(C, C, 90, width=.3) + petals(C, C, 50, rot=45, width=.36)}" style="fill: {r}; fill-opacity: .35; stroke: {r}; stroke-width: 1.2"></path>'
    return s + mono(C, C + 4, 96, i)
def c183(p):   # a flower of flowers: the great flower, with small flowers between its petals
    i = p['ink']; r = FLAT[p['bg']][0]
    s = ring(C, C, 140, i, 3) + ring(C, C, 133, i, 1) + top_bottom(i) + ring(C, C, 94, i, 1)
    s += f'<path d="{petals(C, C, 90, width=.3)}" style="fill: none; stroke: {r}; stroke-width: 1.3"></path>'
    for k in range(4):
        a = math.pi / 4 + k * math.pi / 2
        s += flower(C + 64 * math.cos(a), C + 64 * math.sin(a), 11, r)
    return s + mono(C, C + 4, 92, i)
def c184(p):   # a sixteen-point rosette: two eight-point flowers turned 22.5° (the one guilloche on the page)
    i = p['ink']; r = FLAT[p['bg']][0]
    s = ring(C, C, 140, i, 3) + ring(C, C, 133, i, 1) + top_bottom(i) + ring(C, C, 94, i, 1)
    d = ''.join(petals(C, C, 90, width=.18, bulge=.5, rot=a) for a in (0, 22.5, 45, 67.5))
    s += f'<path d="{d}" style="fill: none; stroke: {r}; stroke-width: .8"></path>'
    s += disc(C, C, 58, p['bg']) + ring(C, C, 58, i, 1)
    return s + mono(C, C + 3, 80, i)
def c185(p):   # the lattice pattern lives inside the petals of the great flower
    i = p['ink']; u = p['bg'][1:] + 'c185'
    s = ring(C, C, 140, i, 3) + ring(C, C, 133, i, 1) + top_bottom(i) + ring(C, C, 94, i, 1)
    pd = petals(C, C, 90, width=.3) + petals(C, C, 50, rot=45, width=.36)
    s += f'<clipPath id="f{u}"><path d="{pd}"></path></clipPath><g clip-path="url(#f{u})">{lattice(C, C, 92, p, s=14, tag="c185")}</g>'
    s += disc(C, C, 44, p['bg'])
    return s + mono(C, C + 3, 74, i)
def c186(p):   # guilloche flower: fine woven curves in rose, like a banknote rosette, monogram at the centre
    i = p['ink']; r = FLAT[p['bg']][0]
    s = ring(C, C, 140, i, 3) + ring(C, C, 133, i, 1) + top_bottom(i) + ring(C, C, 94, i, 1)
    s += guilloche(74, 16, 8, 6, r, .5) + disc(C, C, 52, p['bg']) + ring(C, C, 52, i, 1)
    return s + mono(C, C + 3, 74, i)
def c187(p):   # the flower seal with a microtext ring and flower separators
    i = p['ink']; r = FLAT[p['bg']][0]
    s = ring(C, C, 144, i, 2) + microtext(136.5, 4.6, i) + ring(C, C, 132, i, 1) + top_bottom(i, rt=105, rb=119) + ring(C, C, 92, i, 1)
    s += f'<path d="{petals(C, C, 88, width=.3) + petals(C, C, 48, rot=45, width=.36)}" style="fill: none; stroke: {r}; stroke-width: 1.3"></path>'
    s += seps(112, 6, i)
    return s + mono(C, C + 4, 94, i)

V = [
 ('172', '161 · flower band all round',             a172),
 ('173', '161 · four flowers, like a compass',      a173),
 ('174', '161 · flower chain round the monogram',   a174),
 ('175', '161 · two-tone, rose rings',              a175),
 ('176', '161 · microtext ring',                    a176),
 ('177', '163 · wider band, larger lattice',        b177),
 ('178', '163 · band of flowers only',              b178),
 ('179', '163 · necklace of diamonds',              b179),
 ('180', '163 · light band in rose',                b180),
 ('181', '163 · lattice ring + flower chain',       b181),
 ('182', '170 · petals softly filled',              c182),
 ('183', '170 · a flower of flowers',               c183),
 ('184', '170 · sixteen-point rosette',             c184),
 ('185', '170 · lattice inside the petals',         c185),
 ('186', '170 · guilloche flower',                  c186),
 ('187', '170 · microtext ring',                    c187),
]
CONCEPTS = [(f'Concept{n}', f'{n} · {t}', '0 0 300 300', fn) for n, t, fn in V]
