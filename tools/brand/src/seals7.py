"""Seal rules (owner, locked): monogram is always the full 153 patterned DA; one ring pair only (thick + thin);
no CO., LTD.; flowers / diamonds used more than round 6 but with restraint."""
import math
from seals6 import *

def pair(i): return ring(C, C, 141, i, 3.2) + ring(C, C, 134.5, i, 1)          # the only rings: thick + thin
def name(i): return arc_text(NAME, 13.5, C, C, 114, 'top', track=.14, fill=i)
def da(p, y=0, w=136): return mono_patterned(C, C - 4 + y, w, p)               # always the full 153 monogram
def arc_items(r, n, span, fn, centre=90):
    out = ''
    for k in range(n):
        t = k / (n - 1) - .5; a = math.radians(centre - t * span)
        out += fn(C + r * math.cos(a), C + r * math.sin(a), t, math.degrees(a))
    return out
def gem(x, y, ang, hw, hh, line, fl, fillc=None): return lozenge_at(x, y, ang, hw, hh, line, fl, fillc=fillc)

def h232(p):   # five graded flowers along the bottom
    i = p['ink']
    return pair(i) + name(i) + bottom_flowers(112, 5, 9, i, span=56, graded=True) + da(p)
def h233(p):   # an arc of nine small diamonds, each with a flower, under the monogram
    i, r = p['ink'], FLAT[p['bg']][0]
    return pair(i) + name(i) + arc_items(110, 9, 84, lambda x, y, t, a: gem(x, y, 0, 6.5, 9.5, i, r)) + da(p)
def h234(p):   # a ring of small flowers just inside the ring pair, all the way round
    i, r = p['ink'], FLAT[p['bg']][0]
    return pair(i) + flower_ring(127, 56, 2.6, r) + arc_text(NAME, 12.5, C, C, 106, 'top', track=.14, fill=i) + bottom_flowers(106, 3, 6, i, span=20, graded=True) + da(p, w=128)
def h235(p):   # three lattice diamonds along the bottom, the centre one largest
    i, bg = p['ink'], p['bg']; u = bg[1:] + 'h235'; out = ''
    for k, (dx, hw, hh) in enumerate(((-40, 13, 17), (0, 18, 24), (40, 13, 17))):
        x, y = C + dx, C + 104 - (0 if dx == 0 else 6)
        d = f'M{x},{y - hh} L{x + hw},{y} L{x},{y + hh} L{x - hw},{y} Z'
        out += f'<clipPath id="g{u}{k}"><path d="{d}"></path></clipPath><g clip-path="url(#g{u}{k})">{lattice(x, y, 30, p, s=9, tag=f"h235{k}")}</g><path d="{d}" style="fill: none; stroke: {i}; stroke-width: 1"></path>'
    return pair(i) + name(i) + out + da(p)
def h236(p):   # a flower clasp at the top splitting the name; five graded flowers at the bottom
    i = p['ink']
    return pair(i) + split_name(i, r=114, size=13.5) + flower(C, C - 118, 8, i) + bottom_flowers(112, 5, 8.5, i, span=56, graded=True) + da(p)
def h237(p):   # a fine circle of tiny diamonds inside the ring pair; one large flower at the foot
    i, r = p['ink'], FLAT[p['bg']][0]
    return pair(i) + lozenge_dots(127, 90, 1.6, 2.6, r) + arc_text(NAME, 12.5, C, C, 106, 'top', track=.14, fill=i) + flower(C, C + 108, 11, i) + da(p, w=128)
def h238(p):   # flowers flank the monogram; three graded flowers below
    i, r = p['ink'], FLAT[p['bg']][0]
    s = pair(i) + name(i) + flower(C - 98, C - 4, 7, r) + flower(C + 98, C - 4, 7, r)
    return s + bottom_flowers(112, 3, 8.5, i, span=26, graded=True) + da(p, w=128)
def h239(p):   # a crescent band of lattice along the bottom of the ring
    i, bg = p['ink'], p['bg']; u = bg[1:] + 'h239'
    a0, a1 = math.radians(150), math.radians(30)
    def pt(r, a): return f'{F(C + r * math.cos(a))},{F(C + r * math.sin(a))}'
    path = f'M{pt(130, a0)} A130,130 0 0 0 {pt(130, a1)} L{pt(108, a1)} A108,108 0 0 1 {pt(108, a0)} Z'
    s = pair(i) + name(i) + f'<clipPath id="c{u}"><path d="{path}"></path></clipPath><g clip-path="url(#c{u})">{lattice(C, C, 140, p, s=12, tag="h239")}</g>'
    return s + f'<path d="{path}" style="fill: none; stroke: {i}; stroke-width: 1"></path>' + da(p)
def h240(p):   # four flowers at the quarters inside the ring; name above
    i, r = p['ink'], FLAT[p['bg']][0]
    s = pair(i) + name(i)
    for a in (0, 90, 180):
        s += flower(C + 118 * math.cos(math.radians(a)), C + 118 * math.sin(math.radians(a)), 9 if a == 90 else 7, i if a == 90 else r)
    return s + da(p)
def h241(p):   # a half-necklace of diamonds round the bottom, a flower clasp at the top
    i, r = p['ink'], FLAT[p['bg']][0]
    s = pair(i) + split_name(i, r=114, size=13.5) + flower(C, C - 118, 8, i)
    return s + arc_items(116, 13, 150, lambda x, y, t, a: gem(x, y, 0, 6, 8.5, i, r)) + da(p, w=128)
def h242(p):   # a whisper of lattice across the field, five graded flowers at the foot
    i, bg = p['ink'], p['bg']; r, sv = FLAT[bg]
    lt = lattice(C, C, 131, p, s=18, tag='h242').replace(f'fill: {i}"></circle>', f'fill: {bg}"></circle>', 1)
    lt = lt.replace(f'stroke: {r}; stroke-width: .8', f'stroke: {r}; stroke-width: .5; stroke-opacity: .45').replace(f'fill: {sv}"', f'fill: {r}; fill-opacity: .35"')
    s = pair(i) + lt + name(i) + bottom_flowers(112, 5, 8.5, i, span=56, graded=True)
    return s + disc(C, C - 4, 0, bg) + da(p)
def h243(p):   # one large flower at the foot with small ones either side
    i, r = p['ink'], FLAT[p['bg']][0]
    s = pair(i) + name(i) + flower(C, C + 108, 12, i)
    s += ''.join(flower(C + 110 * math.cos(math.radians(a)), C + 110 * math.sin(math.radians(a)), sz, r) for a, sz in ((72, 6), (108, 6), (56, 4.2), (124, 4.2)))
    return s + da(p)

V = [
 ('232', 'Five graded flowers below', h232),
 ('233', 'An arc of nine small diamonds', h233),
 ('234', 'A ring of small flowers inside', h234),
 ('235', 'Three lattice diamonds below', h235),
 ('236', 'Flower clasp + graded flowers', h236),
 ('237', 'Circle of tiny diamonds + one flower', h237),
 ('238', 'Flowers flank the monogram', h238),
 ('239', 'A crescent of lattice below', h239),
 ('240', 'Flowers at three quarters', h240),
 ('241', 'Half-necklace + flower clasp', h241),
 ('242', 'Whisper of lattice + graded flowers', h242),
 ('243', 'One large flower with small ones', h243),
]
CONCEPTS = [(f'Concept{n}', f'{n} · {t}', '0 0 300 300', fn) for n, t, fn in V]
