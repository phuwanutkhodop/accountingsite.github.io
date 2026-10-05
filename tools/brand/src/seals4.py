import math
from seals3 import *
from marks6 import text as tx, gd

def lobes(n, d, R, i, bg, w_outer=3.2, gap=3.5, w_inner=1.1):
    """Outline of n overlapping circles (union): a thick outer line and a thin inner line."""
    cs = [(C + d * math.cos(2 * math.pi * k / n - math.pi / 2), C + d * math.sin(2 * math.pi * k / n - math.pi / 2)) for k in range(n)]
    layer = lambda r, c: ''.join(f'<circle cx="{F(x)}" cy="{F(y)}" r="{F(r)}" style="fill: {c}"></circle>' for x, y in cs) + \
        f'<circle cx="{C}" cy="{C}" r="{F(d + r - R)}" style="fill: {c}"></circle>'   # a centre disc so the lobes join into one shape
    return (layer(R, i) + layer(R - w_outer, bg) + layer(R - w_outer - gap, i) + layer(R - w_outer - gap - w_inner, bg))
def name_line(i, y, size=11.5): return f'<path d="{tx(TXT, NAME, size, C, y, .18)}" style="fill: {i}"></path>'

def e196(p):   # ประจำยาม four-lobe seal: the seal takes the flower's own outline
    i, bg = p['ink'], p['bg']; r = FLAT[bg][0]
    s = lobes(4, 62, 82, i, bg) + ring(C, C, 98, r, .8)
    s += arc_text(NAME, 11, C, C, 86, 'top', track=.12, fill=i)
    s += bottom_flowers(92, 5, 5, i, span=40, graded=True)
    return s + mono_patterned(C, C + 6, 100, p)
def e197(p):   # eight-lobe seal, like a carved rosette; name inside
    i, bg = p['ink'], p['bg']
    s = lobes(8, 104, 40, i, bg, 3, 3, 1)
    s += ring(C, C, 104, i, 1) + arc_text(NAME, 12, C, C, 90, 'top', track=.13, fill=i) + arc_text(SUB, 12, C, C, 103 - 2, 'bottom', track=.13, fill=i)
    return s + mono_patterned(C, C + 4, 104, p)
def e198(p):   # a coin: milled edge, the monogram struck in the field — finance at its plainest
    i, bg = p['ink'], p['bg']; r = FLAT[bg][0]
    s = disc(C, C, 142, i) + disc(C, C, 128, bg)
    s += ''.join(f'<line x1="{F(C + 130 * math.cos(a))}" y1="{F(C + 130 * math.sin(a))}" x2="{F(C + 141 * math.cos(a))}" y2="{F(C + 141 * math.sin(a))}" style="stroke: {bg}; stroke-width: 1.4"></line>' for a in [2 * math.pi * k / 150 for k in range(150)])
    s += ring(C, C, 120, i, 1) + dot_ring(112, 64, 1.1, r)
    s += arc_text(NAME, 12.5, C, C, 92, 'top', track=.14, fill=i) + bottom_flowers(100, 5, 6, i, span=44, graded=True)
    return s + mono_patterned(C, C + 4, 110, p)
def e199(p):   # an arch, like a library doorway: monogram inside, flowers along the curve, name on the sill
    i, bg = p['ink'], p['bg']; r = FLAT[bg][0]
    def arch(x0, x1, top, bot, w):
        rr = (x1 - x0) / 2; cx = (x0 + x1) / 2
        return f'<path d="M{x0},{bot} L{x0},{top + rr} A{rr},{rr} 0 0 1 {x1},{top + rr} L{x1},{bot} Z" style="fill: none; stroke: {i}; stroke-width: {w}"></path>'
    s = arch(50, 250, 20, 280, 3) + arch(58, 242, 28, 272, 1)
    for k in range(9):
        a = math.pi + math.pi * k / 8
        s += flower(C + 80 * math.cos(a), 128 + 80 * math.sin(a), 4.5 if k % 2 else 3, r)
    s += mono_patterned(C, 150, 132, p)
    s += f'<line x1="66" y1="236" x2="234" y2="236" style="stroke: {i}; stroke-width: 1"></line>'
    return s + f'<path d="{tx(TXT, "D.A. ACCOUNTING", 11.5, C, 256, .2)}" style="fill: {i}"></path>'
def e200(p):   # a tall diamond medallion: two diamond frames, flowers at the four points
    i, bg = p['ink'], p['bg']
    def lz(hw, hh, w): return f'<polygon points="{C},{C - hh} {C + hw},{C} {C},{C + hh} {C - hw},{C}" style="fill: none; stroke: {i}; stroke-width: {w}; stroke-linejoin: miter"></polygon>'
    s = lz(118, 146, 3) + lz(110, 136, 1) + lz(84, 104, 1)
    for x, y in ((C, C - 146), (C + 118, C), (C, C + 146), (C - 118, C)):
        s += disc(x, y, 10, bg) + flower(x, y, 9, i)
    return s + mono_patterned(C, C + 4, 112, p)
def e201(p):   # an upright oval cartouche with a lattice band
    i, bg = p['ink'], p['bg']; u = bg[1:] + 'ov'
    s = f'<ellipse cx="{C}" cy="{C}" rx="112" ry="146" style="fill: none; stroke: {i}; stroke-width: 3"></ellipse>'
    s += f'<ellipse cx="{C}" cy="{C}" rx="105" ry="139" style="fill: none; stroke: {i}; stroke-width: 1"></ellipse>'
    s += (f'<mask id="m{u}"><rect x="0" y="0" width="300" height="300" style="fill: #fff"></rect><ellipse cx="{C}" cy="{C}" rx="78" ry="108" style="fill: #000"></ellipse></mask>'
          f'<clipPath id="o{u}"><ellipse cx="{C}" cy="{C}" rx="96" ry="128"></ellipse></clipPath>'
          f'<g mask="url(#m{u})" clip-path="url(#o{u})">{lattice(C, C, 150, p, s=16, tag="ov")}</g>')
    s += f'<ellipse cx="{C}" cy="{C}" rx="96" ry="128" style="fill: none; stroke: {i}; stroke-width: 1.2"></ellipse><ellipse cx="{C}" cy="{C}" rx="78" ry="108" style="fill: none; stroke: {i}; stroke-width: 1.2"></ellipse>'
    return s + mono(C, C + 3, 112, i)
def e202(p):   # a postage stamp: perforated edge, patterned monogram, the name as the denomination line
    i, bg = p['ink'], p['bg']
    s = f'<rect x="34" y="20" width="232" height="260" style="fill: {i}"></rect>'
    for k in range(13):
        x = 34 + k * 232 / 12; s += disc(x, 20, 6, bg) + disc(x, 280, 6, bg)
    for k in range(14):
        y = 20 + k * 260 / 13; s += disc(34, y, 6, bg) + disc(266, y, 6, bg)
    s += f'<rect x="50" y="36" width="200" height="228" style="fill: {bg}"></rect><rect x="56" y="42" width="188" height="216" style="fill: none; stroke: {i}; stroke-width: 1"></rect>'
    s += mono_patterned(C, 130, 150, p) + f'<line x1="72" y1="196" x2="228" y2="196" style="stroke: {i}; stroke-width: 1"></line>'
    s += f'<path d="{tx(TXT, "D.A. ACCOUNTING", 12, C, 220, .2)}" style="fill: {i}"></path><path d="{tx(TXT, "& CONSULTING", 12, C, 240, .2)}" style="fill: {i}"></path>'
    return s
def e203(p):   # no ring lines at all: the border is a necklace of diamonds
    i, bg = p['ink'], p['bg']; r = FLAT[bg][0]
    s = lozenge_chain(132, 40, 11, 10, i, r, fill=None)
    s += arc_text(NAME, 12.5, C, C, 100, 'top', track=.14, fill=i) + bottom_flowers(108, 5, 6, i, span=44, graded=True)
    return s + mono_patterned(C, C + 4, 112, p)
def e204(p):   # a full banknote rosette: woven guilloche fills the seal, the monogram cut clear in the middle
    i, bg = p['ink'], p['bg']; r = FLAT[bg][0]
    s = ring(C, C, 143, i, 2.5) + ring(C, C, 137, i, .8) + arc_text(NAME, 11.5, C, C, 122, 'top', track=.14, fill=i) + ring(C, C, 116, i, .8)
    s += guilloche(98, 11, 12, 8, r, .45) + guilloche(74, 8, 9, 6, i, .4)
    s += disc(C, C, 58, bg) + ring(C, C, 58, i, 1.2)
    return s + mono(C, C + 3, 84, i)
def e205(p):   # two founders: two rings joined, a flower where they meet; the name runs round them both
    i, bg = p['ink'], p['bg']; r = FLAT[bg][0]
    s = ring(C, C, 142, i, 2.5) + ring(C, C, 136, i, .8) + arc_text(NAME, 12, C, C, 122, 'top', track=.14, fill=i)
    for dx in (-36, 36):
        s += ring(C + dx, C + 12, 62, i, 2.6)
    s += f'<path d="{gd("BM700.ttf", "D", 64, C - 36 - 24, C + 12 + 24)}" style="fill: {i}"></path><path d="{gd("BM700.ttf", "A", 64, C + 36 - 26, C + 12 + 24)}" style="fill: {i}"></path>'
    return s + disc(C, C + 12, 9, bg) + flower(C, C + 12, 8, r) + bottom_flowers(126, 5, 4.5, i, span=36, graded=True)
def e206(p):   # a hallmark plate: an emerald-cut tablet, lattice along the top, name in two lines
    i, bg = p['ink'], p['bg']; u = bg[1:] + 'hp'
    x0, y0, x1, y1, k = 26, 40, 274, 260, 26
    pts = lambda o, kk: f'{x0 + o + kk},{y0 + o} {x1 - o - kk},{y0 + o} {x1 - o},{y0 + o + kk} {x1 - o},{y1 - o - kk} {x1 - o - kk},{y1 - o} {x0 + o + kk},{y1 - o} {x0 + o},{y1 - o - kk} {x0 + o},{y0 + o + kk}'
    s = f'<polygon points="{pts(0, k)}" style="fill: none; stroke: {i}; stroke-width: 3"></polygon><polygon points="{pts(7, k - 4)}" style="fill: none; stroke: {i}; stroke-width: 1"></polygon>'
    s += f'<clipPath id="h{u}"><rect x="{x0 + 14}" y="{y0 + 14}" width="{x1 - x0 - 28}" height="30"></rect></clipPath><g clip-path="url(#h{u})">{lattice(C, y0 + 29, 160, p, s=14, tag="hp")}</g>'
    s += mono_patterned(C, 148, 136, p)
    s += f'<path d="{tx(TXT, "D.A. ACCOUNTING", 13, C, 222, .2)}" style="fill: {i}"></path><path d="{tx(TXT, "& CONSULTING", 13, C, 242, .2)}" style="fill: {i}"></path>'
    return s
def e207(p):   # a wax seal pressed with the pattern: the lattice shows in the wax, the monogram raised
    i, bg = p['ink'], p['bg']; r, sv = FLAT[bg]; u = bg[1:] + 'wx'
    pts = []
    for k in range(72):
        a = 2 * math.pi * k / 72
        rr = 140 + 5 * math.sin(5 * a) + 3 * math.sin(11 * a + 1) + 2 * math.sin(23 * a)
        pts.append(f'{F(C + rr * math.cos(a))},{F(C + rr * math.sin(a))}')
    s = f'<polygon points="{" ".join(pts)}" style="fill: {i}"></polygon>'
    s += f'<clipPath id="w{u}"><circle cx="{C}" cy="{C}" r="104"></circle></clipPath><g clip-path="url(#w{u})">{lattice(C, C, 104, p, s=18, tag="wx")}</g>'
    s += ring(C, C, 106, r, 2) + ring(C, C, 116, r, .8)
    return s + disc(C, C + 2, 60, i) + ring(C, C + 2, 60, r, 1) + mono(C, C + 4, 92, bg)

V = [
 ('196', 'ประจำยาม four-lobe seal', e196),
 ('197', 'Eight-lobe rosette', e197),
 ('198', 'Coin with a milled edge', e198),
 ('199', 'Arch, like a library doorway', e199),
 ('200', 'Tall diamond medallion', e200),
 ('201', 'Oval cartouche with a lattice band', e201),
 ('202', 'Postage stamp', e202),
 ('203', 'Necklace of diamonds as the border', e203),
 ('204', 'Banknote rosette', e204),
 ('205', 'Two founders, two rings', e205),
 ('206', 'Hallmark tablet', e206),
 ('207', 'Wax seal pressed with the pattern', e207),
]
CONCEPTS = [(f'Concept{n}', f'{n} · {t}', '0 0 300 300', fn) for n, t, fn in V]
