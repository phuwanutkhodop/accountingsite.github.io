import math
from marks6 import font, gw
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from marks12 import PAL as MP, LINE
from marks9 import DP, AP
from marks13 import petals, circle
F = lambda v: f"{v:.2f}"
FLAT = {'#f2eeea': ('#b07e80', '#d4d5d8'), '#7a2229': ('#c29998', '#85878c'), '#1b1112': ('#be9491', '#85878c')}
LINE['rose'] = lambda p: (FLAT[p['bg']][0], 1)
LINE['silver'] = lambda p: (FLAT[p['bg']][1], 1)
from marks13 import design
PAL = MP
TXT = 'CG600.ttf'

def glyph_d(ch, size, w):
    gs, cm, upm = font(TXT); s = size / upm
    sp = SVGPathPen(gs, lambda v: f"{v:.2f}")
    gs[cm[ord(ch)]].draw(TransformPen(sp, (s, 0, 0, -s, -w / 2, 0)))
    return sp.getCommands()

def arc_text(text, size, cx, cy, r, where='top', track=.18, fill='#000'):
    ws = [gw(TXT, c, size) if c != ' ' else size * .3 for c in text]
    adv = [w + track * size for w in ws]; total = sum(adv) - track * size
    out = ''; x = 0
    for c, w, a in zip(text, ws, adv):
        mid = x + w / 2; x += a
        if c == ' ': continue
        if where == 'top':
            th = -math.pi / 2 - total / 2 / r + mid / r; rot = math.degrees(th) + 90
        else:
            th = math.pi / 2 + total / 2 / r - mid / r; rot = math.degrees(th) - 90
        px, py = cx + r * math.cos(th), cy + r * math.sin(th)
        out += f'<path transform="translate({F(px)},{F(py)}) rotate({F(rot)})" d="{glyph_d(c, size, w)}" style="fill: {fill}"></path>'
    return out

def ring(cx, cy, r, c, w): return f'<circle cx="{cx}" cy="{cy}" r="{r}" style="fill: none; stroke: {c}; stroke-width: {w}"></circle>'
def disc(cx, cy, r, c): return f'<circle cx="{cx}" cy="{cy}" r="{r}" style="fill: {c}"></circle>'
def flower(cx, cy, r, c): return f'<path d="{petals(cx, cy, r) + petals(cx, cy, r * .52, rot=45, width=.4)}" style="fill: {c}"></path>'

def mono(cx, cy, width, c, rule='evenodd'):
    sc = width / 312.07
    return (f'<g transform="translate({F(cx - 176.03 * sc)},{F(cy - 113.16 * sc)}) scale({sc:.5f})">'
            f'<path d="{DP} {AP}" style="fill: {c}; fill-rule: {rule}"></path></g>')
def mono_patterned(cx, cy, width, p):
    sc = width / 312.07
    full = design(ring='rose', flowerc='silver', style='eight', tag='seal' + str(int(width)))(p)
    mark = full[:full.rfind('<path d="')]
    return f'<g transform="translate({F(cx - 176.03 * sc)},{F(cy - 113.16 * sc)}) scale({sc:.5f})">{mark}</g>'

def lattice(cx, cy, r, p, s=22, ratio=1.4, tag='lt'):
    rc, fc = FLAT[p['bg']]
    h = s * ratio; d = ''; fl = ''
    n = int(r / s) + 3
    for j in range(-2 * n, 2 * n + 1):
        for i in range(-n, n + 1):
            x = cx + i * s + (s / 2 if j % 2 else 0); y = cy + j * h / 2
            for k in (.94, .62):
                d += f'M{F(x)},{F(y - h / 2 * k)} L{F(x + s / 2 * k)},{F(y)} L{F(x)},{F(y + h / 2 * k)} L{F(x - s / 2 * k)},{F(y)} Z '
            fl += petals(x, y, s * .17) + petals(x, y, s * .17 * .52, rot=45, width=.4)
    u = p['bg'][1:] + tag
    return (f'<clipPath id="c{u}"><circle cx="{cx}" cy="{cy}" r="{r}"></circle></clipPath><g clip-path="url(#c{u})">'
            f'{disc(cx, cy, r, p["ink"])}<path d="{d}" style="fill: none; stroke: {rc}; stroke-width: .8"></path>'
            f'<path d="{fl}" style="fill: {fc}"></path></g>')

NAME, SUB = 'D.A. ACCOUNTING & CONSULTING', 'CO., LTD.'
C = 150
def seps(r, size, c, deg=38):
    # two flowers on the ring, between the end of the name and the start of the bottom line
    return ''.join(flower(C + r * math.cos(math.radians(90 + sgn * deg)), C + r * math.sin(math.radians(90 + sgn * deg)), size, c) for sgn in (-1, 1))

# ---- seals ----
def s_classic(p):            # two rings framing the name; plain monogram; flowers as separators
    i = p['ink']
    s = ring(C, C, 140, i, 3) + ring(C, C, 133, i, 1) + ring(C, C, 96, i, 1) + ring(C, C, 90, i, 3)
    s += arc_text(NAME, 13, C, C, 107, 'top', track=.13, fill=i) + arc_text(SUB, 13, C, C, 121, 'bottom', track=.13, fill=i)
    s += seps(114, 6, i)
    return s + mono(C, C + 4, 112, i)
def s_patterned(p):          # as classic, with the patterned 153 monogram at the centre
    i = p['ink']
    s = ring(C, C, 140, i, 3) + ring(C, C, 133, i, 1) + ring(C, C, 96, i, 1) + ring(C, C, 90, i, 3)
    s += arc_text(NAME, 13, C, C, 107, 'top', track=.13, fill=i) + arc_text(SUB, 13, C, C, 121, 'bottom', track=.13, fill=i)
    s += seps(114, 6, FLAT[p['bg']][0])
    return s + mono_patterned(C, C + 4, 118, p)
def s_lattice_disc(p):       # the centre disc carries the 153 lattice; the monogram is cut out of it
    i = p['ink']
    s = ring(C, C, 140, i, 3) + ring(C, C, 133, i, 1)
    s += arc_text(NAME, 13, C, C, 107, 'top', track=.13, fill=i) + arc_text(SUB, 13, C, C, 121, 'bottom', track=.13, fill=i)
    s += lattice(C, C, 92, p, tag='ld') + ring(C, C, 92, i, 1.5)
    return s + mono(C, C + 4, 112, p['bg'])
def s_lattice_band(p):       # a narrow lattice band between the text and the centre
    i = p['ink']; u = p['bg'][1:] + 'lb'
    s = ring(C, C, 140, i, 3) + ring(C, C, 133, i, 1)
    s += arc_text(NAME, 13, C, C, 107, 'top', track=.13, fill=i) + arc_text(SUB, 13, C, C, 121, 'bottom', track=.13, fill=i)
    s += f'<mask id="m{u}"><rect x="0" y="0" width="300" height="300" style="fill: #fff"></rect>{disc(C, C, 72, "#000")}</mask>'
    s += f'<g mask="url(#m{u})">{lattice(C, C, 92, p, s=16, tag="lb")}</g>' + ring(C, C, 92, i, 1.5) + ring(C, C, 72, i, 1.5)
    return s + mono(C, C + 3, 92, i)
def s_lozenge(p):            # a diamond-shaped seal: two diamond frames, name along the upper edges
    i = p['ink']
    def lz(k, w): return f'<polygon points="{C},{F(C - 140 * k)} {F(C + 140 * k)},{C} {C},{F(C + 140 * k)} {F(C - 140 * k)},{C}" style="fill: none; stroke: {i}; stroke-width: {w}; stroke-linejoin: miter"></polygon>'
    s = lz(1, 3) + lz(.95, 1) + lz(.68, 1) + lz(.64, 3)
    def edge(text, x0, y0, x1, y1):
        ang = math.degrees(math.atan2(y1 - y0, x1 - x0)); L = math.hypot(x1 - x0, y1 - y0)
        size = 12.5; ws = [gw(TXT, c, size) if c != ' ' else size * .3 for c in text]; tot = sum(ws) + .18 * size * (len(text) - 1)
        out = ''; x = (L - tot) / 2
        for c, w in zip(text, ws):
            if c != ' ':
                t = (x + w / 2) / L; px, py = x0 + (x1 - x0) * t, y0 + (y1 - y0) * t
                out += f'<path transform="translate({F(px)},{F(py)}) rotate({F(ang)})" d="{glyph_d(c, size, w)}" style="fill: {i}"></path>'
            x += w + .18 * size
        return out
    k = .815; s += edge('D.A. ACCOUNTING', C - 140 * k, C - 2, C - 2, C - 140 * k) + edge('& CONSULTING', C + 2, C - 140 * k, C + 140 * k, C - 2)
    s += flower(C, C + 100, 7, i)
    return s + mono(C, C + 8, 104, i)
def s_octagon(p):            # an emerald-cut octagon frame around a round name band
    i = p['ink']
    def oc(r, w): return '<polygon points="' + ' '.join(f'{F(C + r * math.cos(math.radians(22.5 + 45 * k)))},{F(C + r * math.sin(math.radians(22.5 + 45 * k)))}' for k in range(8)) + f'" style="fill: none; stroke: {i}; stroke-width: {w}"></polygon>'
    s = oc(150, 3) + oc(143, 1) + ring(C, C, 96, i, 1) + ring(C, C, 90, i, 3)
    s += arc_text(NAME, 13, C, C, 107, 'top', track=.13, fill=i) + arc_text(SUB, 13, C, C, 121, 'bottom', track=.13, fill=i)
    return s + mono(C, C + 4, 112, i)
def s_rosette(p):            # a scalloped rosette edge of 32 points, echoing the flower
    i = p['ink']; n = 32; pts = []
    for k in range(2 * n):
        a = math.pi * k / n; r = 144 if k % 2 == 0 else 136
        pts.append(f'{F(C + r * math.cos(a))},{F(C + r * math.sin(a))}')
    s = f'<polygon points="{" ".join(pts)}" style="fill: none; stroke: {i}; stroke-width: 2"></polygon>' + ring(C, C, 128, i, 1) + ring(C, C, 92, i, 1) + ring(C, C, 87, i, 2.5)
    s += arc_text(NAME, 12.5, C, C, 101, 'top', track=.13, fill=i) + arc_text(SUB, 12.5, C, C, 115, 'bottom', track=.13, fill=i)
    s += seps(108, 5.5, i)
    return s + mono(C, C + 4, 108, i)
def s_two_rings(p):          # two founders: two rings that overlap, the overlap opened; D in one, A in the other
    i = p['ink']; u = p['bg'][1:] + 'tr'
    r, dx = 92, 52
    band = (f'<path d="M{C - dx - r},{C} a{r},{r} 0 1 0 {2 * r},0 a{r},{r} 0 1 0 {-2 * r},0 Z '
            f'M{C - dx - r + 6},{C} a{r - 6},{r - 6} 0 1 0 {2 * (r - 6)},0 a{r - 6},{r - 6} 0 1 0 {-2 * (r - 6)},0 Z '
            f'M{C + dx - r},{C} a{r},{r} 0 1 0 {2 * r},0 a{r},{r} 0 1 0 {-2 * r},0 Z '
            f'M{C + dx - r + 6},{C} a{r - 6},{r - 6} 0 1 0 {2 * (r - 6)},0 a{r - 6},{r - 6} 0 1 0 {-2 * (r - 6)},0 Z" style="fill: {i}; fill-rule: evenodd"></path>')
    from marks6 import gd
    D = gd('BM700.ttf', 'D', 100, C - dx - 38, C + 37); A = gd('BM700.ttf', 'A', 100, C + dx - 38, C + 37)
    s = band + f'<path d="{D}" style="fill: {i}"></path><path d="{A}" style="fill: {i}"></path>'
    s += flower(C, C, 9, FLAT[p['bg']][0])
    from marks6 import text as tx
    return s + f'<path d="{tx(TXT, NAME, 12, C, C + r + 30, .18)}" style="fill: {i}"></path>'
def s_wax(p):                # a wax seal: an irregular oxblood disc, the monogram and rings pressed in
    i = p['ink']; bg = p['bg']
    pts = []
    for k in range(72):
        a = 2 * math.pi * k / 72
        r = 140 + 5 * math.sin(5 * a) + 3 * math.sin(11 * a + 1) + 2 * math.sin(23 * a)
        pts.append(f'{F(C + r * math.cos(a))},{F(C + r * math.sin(a))}')
    press = FLAT[bg][0]
    s = f'<polygon points="{" ".join(pts)}" style="fill: {i}"></polygon>' + ring(C, C, 112, press, 1.5) + ring(C, C, 108, press, 4)
    s += arc_text(NAME, 11.5, C, C, 84, 'top', track=.13, fill=press) + arc_text(SUB, 11.5, C, C, 96, 'bottom', track=.13, fill=press)
    return s + mono(C, C + 4, 96, bg)
def s_emboss(p):             # blind emboss / foil: one weight of line, no fills, for pressing into paper
    i = p['ink']
    s = ring(C, C, 140, i, 1.4) + ring(C, C, 134, i, 1.4) + ring(C, C, 96, i, 1.4) + ring(C, C, 90, i, 1.4)
    s += arc_text(NAME, 13, C, C, 107, 'top', track=.13, fill=i) + arc_text(SUB, 13, C, C, 121, 'bottom', track=.13, fill=i)
    sc = 112 / 312.07
    s += (f'<g transform="translate({F(C - 176.03 * sc)},{F(C + 4 - 113.16 * sc)}) scale({sc:.5f})">'
          f'<path d="{DP} {AP}" style="fill: none; stroke: {i}; stroke-width: {1.4 / sc:.2f}"></path></g>')
    return s
def s_flower(p):             # the eight-point flower as the whole seal; monogram at its heart
    i = p['ink']; rc = FLAT[p['bg']][0]
    s = ring(C, C, 140, i, 3) + ring(C, C, 133, i, 1)
    s += arc_text(NAME, 13, C, C, 107, 'top', track=.13, fill=i) + arc_text(SUB, 13, C, C, 121, 'bottom', track=.13, fill=i)
    s += f'<path d="{petals(C, C, 92, width=.3, bulge=.55) + petals(C, C, 50, rot=45, width=.36)}" style="fill: none; stroke: {rc}; stroke-width: 1.4"></path>'
    s += ring(C, C, 92, i, 1)
    return s + mono(C, C + 4, 96, i)
def s_hallmark(p):           # a hallmark plate: an emerald-cut rectangle, monogram and name in lines
    i = p['ink']; x0, y0, x1, y1, k = 20, 70, 280, 230, 22
    def plate(o, w):
        a, b, c, d, kk = x0 + o, y0 + o, x1 - o, y1 - o, k - o * .6
        return f'<polygon points="{a + kk},{b} {c - kk},{b} {c},{b + kk} {c},{d - kk} {c - kk},{d} {a + kk},{d} {a},{d - kk} {a},{b + kk}" style="fill: none; stroke: {i}; stroke-width: {w}"></polygon>'
    s = plate(0, 3) + plate(7, 1)
    s += mono(C, 132, 120, i)
    from marks6 import text as tx
    s += f'<path d="{tx(TXT, NAME, 9.6, C, 206, .16)}" style="fill: {i}"></path>'
    s += flower(x0 + 26, y0 + 26, 5, i) + flower(x1 - 26, y0 + 26, 5, i)
    return s

V = [
 ('160', 'Classic · two rings, name, monogram',          s_classic,      '0 0 300 300'),
 ('161', 'Classic · with the patterned monogram',        s_patterned,    '0 0 300 300'),
 ('162', 'Lattice disc · monogram cut from the pattern', s_lattice_disc, '0 0 300 300'),
 ('163', 'Lattice band · pattern as a ring',             s_lattice_band, '0 0 300 300'),
 ('164', 'Diamond shape · two diamond frames',           s_lozenge,      '0 0 300 300'),
 ('165', 'Octagon · emerald-cut frame',                  s_octagon,      '0 0 300 300'),
 ('166', 'Rosette · scalloped edge',                     s_rosette,      '0 0 300 300'),
 ('167', 'Two founders · two rings overlapping',         s_two_rings,    '0 40 300 250'),
 ('168', 'Wax seal',                                     s_wax,          '0 0 300 300'),
 ('169', 'Emboss / foil · line only',                    s_emboss,       '0 0 300 300'),
 ('170', 'Flower seal · the eight-point flower',         s_flower,       '0 0 300 300'),
 ('171', 'Hallmark plate',                               s_hallmark,     '10 60 280 180'),
]
CONCEPTS = [(f'Concept{n}', f'{n} · {t}', vb, fn) for n, t, fn, vb in V]
