import math
from seals2 import *

def bottom_flowers(r, n, size, c, span=70, graded=False, gap=None):
    """Flowers along the bottom arc, centred on 6 o'clock. span = total degrees covered.
    graded: largest at the centre. gap: leave this many degrees empty in the middle (for text)."""
    out = ''
    for k in range(n):
        t = k / (n - 1) - .5                      # -0.5 .. 0.5
        a = 90 - t * span
        if gap and abs(90 - a) < gap / 2: continue
        sz = size * (1 - .55 * abs(t) * 2) if graded else size
        out += flower(C + r * math.cos(math.radians(a)), C + r * math.sin(math.radians(a)), sz, c)
    return out
def name_top(i, rt=107, size=13): return arc_text(NAME, size, C, C, rt, 'top', track=.13, fill=i)

def d188(p):   # seven flowers along the bottom in place of the second line
    i = p['ink']
    s = base_rings(i) + name_top(i) + bottom_flowers(115, 7, 6.5, i, span=74)
    return s + mono_patterned(C, C + 4, 118, p)
def d189(p):   # five flowers along the bottom, graded: largest at the centre
    i = p['ink']
    s = base_rings(i) + name_top(i) + bottom_flowers(115, 5, 9, i, span=60, graded=True)
    return s + mono_patterned(C, C + 4, 118, p)
def d190(p):   # CO., LTD. at the centre, three flowers either side
    i = p['ink']; r = FLAT[p['bg']][0]
    s = base_rings(i) + name_top(i) + arc_text(SUB, 13, C, C, 121, 'bottom', track=.13, fill=i)
    s += bottom_flowers(115, 9, 5.5, r, span=100, gap=44)
    return s + mono_patterned(C, C + 4, 118, p)
def d191(p):   # a straight row of flowers under the monogram, inside the centre
    i = p['ink']; r = FLAT[p['bg']][0]
    s = base_rings(i) + name_top(i) + bottom_flowers(115, 7, 6.5, i, span=74)
    s += ''.join(flower(C + dx, C + 58, 4.2 if dx else 5.5, r) for dx in (-36, -18, 0, 18, 36))
    return s + mono_patterned(C, C - 4, 110, p)
def d192(p):   # the necklace of diamonds (179) with flowers along the bottom
    i = p['ink']; r = FLAT[p['bg']][0]
    s = ring(C, C, 140, i, 3) + ring(C, C, 133, i, 1) + name_top(i) + bottom_flowers(115, 7, 6, i, span=74)
    s += ring(C, C, 93, i, 1) + lozenge_chain(82, 24, 10.5, 9.5, r, i) + ring(C, C, 71, i, 1)
    return s + mono_patterned(C, C + 3, 96, p)
def d193(p):   # microtext ring (176) with graded flowers along the bottom
    i = p['ink']
    s = ring(C, C, 144, i, 2) + microtext(136.5, 4.6, i) + ring(C, C, 132, i, 1) + base_rings(i, False)
    s += name_top(i, rt=105) + bottom_flowers(113, 5, 8.5, i, span=60, graded=True)
    return s + mono_patterned(C, C + 4, 118, p)
def d194(p):   # the flower seal (187) with flowers along the bottom
    i = p['ink']; r = FLAT[p['bg']][0]
    s = ring(C, C, 144, i, 2) + microtext(136.5, 4.6, i) + ring(C, C, 132, i, 1) + name_top(i, rt=105) + ring(C, C, 92, i, 1)
    s += bottom_flowers(113, 7, 6, i, span=74)
    s += f'<path d="{petals(C, C, 88, width=.3) + petals(C, C, 48, rot=45, width=.36)}" style="fill: none; stroke: {r}; stroke-width: 1.3"></path>'
    return s + mono(C, C + 4, 94, i)
def d195(p):   # the lattice band (177) with flowers along the bottom
    i = p['ink']
    s = ring(C, C, 140, i, 3) + ring(C, C, 133, i, 1) + name_top(i) + bottom_flowers(115, 7, 6, i, span=74)
    s += band(p, 62, 92, lattice(C, C, 92, p, s=22, tag='d195'), 'd195') + ring(C, C, 92, i, 1.5) + ring(C, C, 62, i, 1.5)
    return s + mono(C, C + 3, 80, i)

V = [
 ('188', 'Bottom · seven flowers instead of CO., LTD.', d188),
 ('189', 'Bottom · five flowers, graded',               d189),
 ('190', 'Bottom · CO., LTD. with flowers either side', d190),
 ('191', 'Bottom · flowers, and a row under the monogram', d191),
 ('192', 'Bottom · flowers + necklace of diamonds',     d192),
 ('193', 'Bottom · graded flowers + microtext',         d193),
 ('194', 'Bottom · flowers + flower seal',              d194),
 ('195', 'Bottom · flowers + lattice band',             d195),
]
CONCEPTS = [(f'Concept{n}', f'{n} · {t}', '0 0 300 300', fn) for n, t, fn in V]
