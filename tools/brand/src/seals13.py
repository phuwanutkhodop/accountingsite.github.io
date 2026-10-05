"""Seal round 13: 339 (reversed band, fine double edge lines, flower clasp, one large foot flower) with a larger diamond pattern."""
import math
from seals12 import *

def frame(p, ri, ro, w=126, band_svg=None, tag='x', s=10):
    """339's frame around a band from ri to ro."""
    i = p['ink']; mid = (ri + ro) / 2
    b = band_svg if band_svg is not None else pband(p, ri, ro, s=s, rev=True, tag=tag)
    return (B(p) + b + ring(C, C, ro + 2.6, i, .5) + ring(C, C, ri - 2.6, i, .5)
            + top_clasp(p, mid, 8 + (ro - ri - 12) * .25) + foot(p, 124) + da(p, w=w))
def ann(ri, ro):
    return (f'M{C - ro},{C} a{ro},{ro} 0 1 0 {2 * ro},0 a{ro},{ro} 0 1 0 {-2 * ro},0 Z '
            f'M{C - ri},{C} a{ri},{ri} 0 1 0 {2 * ri},0 a{ri},{ri} 0 1 0 {-2 * ri},0 Z')
def radial_band(p, ri, ro, n, tag):
    """One row of 153 tiles following the circle (long axis pointing to the centre), with the half rows of the
    lattice tucked in at the edges. Reversed colours: background ground, letter-colour rings, rose flowers."""
    i, bg = p['ink'], p['bg']; rc = FLAT[bg][0]
    rm = (ri + ro) / 2; hh = (ro - ri) / 2
    n = n or round(math.pi * rm / (hh / 1.4))          # tiles 1.4 times taller than wide, as in 153
    hw = math.pi * rm / n
    d = ''; fl = ''
    for k in range(n):
        for off, rr in ((0, rm), (.5, rm - hh), (.5, rm + hh)):
            a = 2 * math.pi * (k + off) / n - math.pi / 2
            ux, uy = math.cos(a), math.sin(a); tx, ty = -uy, ux
            cx, cy = C + rr * ux, C + rr * uy
            for q in (.94, .62):
                pts = [(cx + ux * hh * q, cy + uy * hh * q), (cx + tx * hw * q, cy + ty * hw * q),
                       (cx - ux * hh * q, cy - uy * hh * q), (cx - tx * hw * q, cy - ty * hw * q)]
                d += 'M' + ' L'.join(f'{F(x)},{F(y)}' for x, y in pts) + ' Z '
            r0 = min(hw, hh) * .34 * 1.4
            fl += petals(cx, cy, r0) + petals(cx, cy, r0 * .52, rot=45, width=.4)
    u = 'rb' + bg[1:] + tag
    return (f'<clipPath id="{u}"><path d="{ann(ri, ro)}" style="clip-rule: evenodd"></path></clipPath>'
            f'<path d="{ann(ri, ro)}" style="fill: {bg}; fill-rule: evenodd"></path>'
            f'<g clip-path="url(#{u})"><path d="{d}" style="fill: none; stroke: {i}; stroke-width: .6"></path>'
            f'<path d="{fl}" style="fill: {rc}"></path></g>' + ring(C, C, ro, i, 1) + ring(C, C, ri, i, 1))

def o341(p): return frame(p, 92, 104, s=12, tag='a')
def o342(p): return frame(p, 91, 105, s=14, tag='b')
def o343(p): return frame(p, 90, 106, s=16, tag='c', w=124)
def o344(p): return frame(p, 89, 107, s=18, tag='d', w=122)
def o345(p): return frame(p, 88, 108, s=20, tag='e', w=120)
def o346(p): return frame(p, 86, 108, s=24, tag='f', w=116)
def o347(p): return frame(p, 90, 106, band_svg=radial_band(p, 90, 106, None, 'g'), w=124)
def o348(p): return frame(p, 87, 108, band_svg=radial_band(p, 87, 108, None, 'h'), w=118)

V = [
 ('341', 'Pattern a little larger', o341),
 ('342', 'Pattern larger, band slightly wider', o342),
 ('343', 'Pattern larger again', o343),
 ('344', 'Large pattern', o344),
 ('345', 'Larger pattern, wider band', o345),
 ('346', 'Largest pattern', o346),
 ('347', 'Diamonds follow the circle', o347),
 ('348', 'Diamonds follow the circle, larger', o348),
]
CONCEPTS = [(f'Concept{n}', f'{n} · {t}', '0 0 300 300', fn) for n, t, fn in V]
