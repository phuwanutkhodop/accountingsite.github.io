import math, random
from marks6 import gd, gb
from marks7 import name_d
B = 'BM700.ttf'
H = 190
db = gb(B, 'D', 100); SIZE = H / (db[3] / 100)
d0, a0 = gb(B, 'D', SIZE), gb(B, 'A', SIZE)
XD = 20 - d0[0]; BASE = 20 + d0[3]
XA = (XD + d0[2]) - .32 * (d0[2] - d0[0]) - a0[0]
DP, AP = gd(B, 'D', SIZE, XD, BASE), gd(B, 'A', SIZE, XA, BASE)
W, HH = 352, 230

# tonal facets = overlays on the letter colour: lighter (toward paper) or deeper
PAL = {
 'mk':  dict(bg='#f2eeea', ink='#7a2229', tones=[('#f2eeea', .34), ('#f2eeea', .16), None, ('#3a1316', .5)]),
 'mkL': dict(bg='#7a2229', ink='#f6efe8', tones=[None, ('#7a2229', .12), ('#7a2229', .26), ('#7a2229', .42)]),
 'mkN': dict(bg='#1b1112', ink='#efe6dc', tones=[None, ('#1b1112', .14), ('#1b1112', .3), ('#1b1112', .48)]),
}
F = lambda v: f"{v:.1f}"
def P(pts): return ' '.join(f'{F(x)},{F(y)}' for x, y in pts)

# ---- facet geometry ----
def lowpoly(cell, seed=7):
    rnd = random.Random(seed); j = cell * .32
    nx, ny = int(W / cell) + 3, int(HH / cell) + 3
    g = [[(i * cell - cell + (rnd.uniform(-j, j) if 0 < i < nx - 1 else 0),
           k * cell - cell + (rnd.uniform(-j, j) if 0 < k < ny - 1 else 0)) for k in range(ny)] for i in range(nx)]
    tris = []
    for i in range(nx - 1):
        for k in range(ny - 1):
            a, b, c, d = g[i][k], g[i + 1][k], g[i + 1][k + 1], g[i][k + 1]
            if (i + k) % 2: tris += [(a, b, c), (a, c, d)]
            else: tris += [(a, b, d), (b, c, d)]
    return tris
def brilliant(cx, cy, r, n=16):
    """Radial facets: table polygon, star and kite rings, out to radius r (covers letters when r is large)."""
    rt, rs = r * .38, r * .62
    polys = []
    for i in range(n):
        a0, a1 = 2 * math.pi * i / n, 2 * math.pi * (i + 1) / n; am = (a0 + a1) / 2
        p = lambda rr, a: (cx + rr * math.cos(a), cy + rr * math.sin(a))
        polys.append([(cx, cy), p(rt, a0), p(rt, a1)])                 # table slices
        polys.append([p(rt, a0), p(rs, am), p(rt, a1)])                # star
        polys.append([p(rt, a0), p(rs, am - (a1 - a0)), p(r, a0), p(rs, am)][::1])  # kite
        polys.append([p(rs, am), p(r, a0), p(r, a1)])                  # upper girdle
    return polys
def tone_of(poly, mode, seed=0, centre=None):
    cx = sum(x for x, _ in poly) / len(poly); cy = sum(y for _, y in poly) / len(poly)
    if mode == 'radial':   # light from the top left; facets facing it are lightest
        a = math.atan2(cy - centre[1], cx - centre[0])
        k = (1 - math.cos(a - math.radians(225))) / 2
        return min(3, int(k * 4))
    if mode == 'vertical':
        return min(3, max(0, int((cy - 10) / (HH - 20) * 4)))
    h = math.sin(cx * .071 + cy * .053 + seed) * 43758.5453
    return int((h - math.floor(h)) * 4)

def draw(polys, p, mode, centre=None):
    """mode: 'lines' = hairline cuts in bg colour; 'tone'/'vertical' = filled tonal facets."""
    if mode == 'lines':
        d = ' '.join('M' + ' L'.join(f'{F(x)},{F(y)}' for x, y in poly) + ' Z' for poly in polys)
        return (f'<rect x="0" y="0" width="{W}" height="{HH}" style="fill: {p["ink"]}"></rect>'
                f'<path d="{d}" style="fill: none; stroke: {p["bg"]}; stroke-width: 1.3; stroke-linejoin: round"></path>')
    out = ''
    for poly in polys:
        t = p['tones'][tone_of(poly, mode, centre=centre)]
        if t: out += f'<polygon points="{P(poly)}" style="fill: {t[0]}; fill-opacity: {t[1]}"></polygon>'
    return out

def mark(target, polys, mode, centre=None):
    """target: 'both' | 'D' | 'A' | 'window'."""
    def build(p):
        u = p['bg'][1:] + target + mode + str(len(polys))
        s = (f'<clipPath id="x{u}"><path d="{DP} {AP}" style="clip-rule: evenodd"></path></clipPath>'
             f'<clipPath id="d{u}"><path d="{DP}"></path></clipPath><clipPath id="a{u}"><path d="{AP}"></path></clipPath>')
        s += f'<path d="{DP} {AP}" style="fill: {p["ink"]}; fill-rule: evenodd"></path>'
        art = draw(polys, p, mode, centre)
        if target == 'both':   s += f'<g clip-path="url(#x{u})">{art}</g>'
        elif target == 'D':    s += f'<g clip-path="url(#x{u})"><g clip-path="url(#d{u})">{art}</g></g>'
        elif target == 'A':    s += f'<g clip-path="url(#x{u})"><g clip-path="url(#a{u})">{art}</g></g>'
        elif target == 'window': s += f'<g clip-path="url(#d{u})"><g clip-path="url(#a{u})">{art}</g></g>'
        return s + name_d(p, 176, 254, 312)
    return build

def stepcut(target):
    """Emerald / step cut: concentric inset rules inside the letter, made by stroking the outline in bg inside a clip."""
    def build(p):
        u = p['bg'][1:] + 'step' + target
        s = (f'<clipPath id="x{u}"><path d="{DP} {AP}" style="clip-rule: evenodd"></path></clipPath>'
             f'<clipPath id="t{u}"><path d="{DP if target != "A" else AP}{" " + AP if target == "both" else ""}" style="clip-rule: evenodd"></path></clipPath>')
        s += f'<path d="{DP} {AP}" style="fill: {p["ink"]}; fill-rule: evenodd"></path>'
        src = DP if target == 'D' else AP if target == 'A' else f'{DP} {AP}'
        rings = ''
        for w, c in ((15, p['bg']), (12.4, p['ink']), (7.4, p['bg']), (4.8, p['ink'])):
            rings += f'<path d="{src}" style="fill: none; stroke: {c}; stroke-width: {w}; stroke-linejoin: miter"></path>'
        s += f'<g clip-path="url(#x{u})"><g clip-path="url(#t{u})">{rings}</g></g>'
        return s + name_d(p, 176, 254, 312)
    return build

# window centre (where A's left leg crosses the D bowl) ~ (192, 118)
WX, WY = 192, 118
V = [
 ('80', 'Cut lines · brilliant across both letters', mark('both', brilliant(WX, WY, 260), 'lines')),
 ('81', 'Cut lines · large facets',                 mark('both', lowpoly(64), 'lines')),
 ('82', 'Cut lines · small facets',                 mark('both', lowpoly(22), 'lines')),
 ('83', 'Tonal · large facets',                     mark('both', lowpoly(64), 'tone')),
 ('84', 'Tonal · small facets',                     mark('both', lowpoly(22), 'tone')),
 ('85', 'Tonal · brilliant across both letters',    mark('both', brilliant(WX, WY, 260), 'radial', (WX, WY))),
 ('86', 'Tonal · light to dark, top to bottom',     mark('both', lowpoly(40), 'vertical')),
 ('87', 'D only · tonal large facets',              mark('D', lowpoly(56), 'tone')),
 ('88', 'A only · tonal large facets',              mark('A', lowpoly(56), 'tone')),
 ('89', 'D only · brilliant cut lines',             mark('D', brilliant(100, 115, 150), 'lines')),
 ('90', 'A only · brilliant cut lines',             mark('A', brilliant(240, 120, 150), 'lines')),
 ('91', 'Step cut · both letters',                  stepcut('both')),
 ('92', 'Step cut · D only',                        stepcut('D')),
 ('93', 'D only · tonal brilliant',                 mark('D', brilliant(100, 115, 150), 'radial', (100, 115))),
 ('94', 'A only · tonal brilliant',                 mark('A', brilliant(240, 120, 150), 'radial', (240, 120))),
]
VB = '0 -6 362 280'
CONCEPTS = [(f'Concept{n}', f'{n} · {t}', VB, fn) for n, t, fn in V]
