"""Seal round 12: deeper on 321 (reversed pattern band with a flower clasp at the top, one large flower at the foot)."""
import math
from seals11 import *

def tile(p, x, y, s):
    """The 153 tile as an ornament: background lozenge, two rose diamond rings, the flower in the letter colour."""
    i, rc = p['ink'], FLAT[p['bg']][0]; hw, hh = s * .62, s
    lz = lambda q: f'M{F(x)},{F(y - hh * q)} L{F(x + hw * q)},{F(y)} L{F(x)},{F(y + hh * q)} L{F(x - hw * q)},{F(y)} Z '
    return (f'<path d="{lz(1.15)}" style="fill: {p["bg"]}"></path><path d="{lz(.94)} {lz(.62)}" style="fill: none; stroke: {rc}; stroke-width: .9"></path>'
            + flower(x, y, hw * .6, i))
def medallion(p, y, r=11, f=8):
    return disc(C, y, r, p['bg']) + ring(C, y, r, p['ink'], .8) + flower(C, y, f, p['ink'])
R = lambda p, tag, **k: pband(p, 92, 104, rev=True, tag=tag, **k)          # the 321 band

def n336(p):   # clasp and foot flower set in matching medallions
    return B(p) + R(p, 'a') + medallion(p, C - 98) + disc(C, C + 124, 13, p['bg']) + ring(C, C + 124, 13, p['ink'], .8) + flower(C, C + 124, 10, p['ink']) + da(p, w=128)
def n337(p):   # the clasp is the 153 diamond tile itself
    return B(p) + R(p, 'b') + tile(p, C, C - 98, 13) + foot(p, 124) + da(p, w=128)
def n338(p):   # a larger pattern so each diamond and flower reads clearly
    return B(p) + pband(p, 89, 106, s=13, rev=True, tag='c') + top_clasp(p, 97.5, 9) + foot(p, 124) + da(p, w=124)
def n339(p):   # the band edged with fine double lines
    i = p['ink']
    return B(p) + R(p, 'd') + ring(C, C, 106.6, i, .5) + ring(C, C, 89.4, i, .5) + top_clasp(p, 98) + foot(p, 124) + da(p, w=126)
def n340(p):   # inside the band: rose diamond rings, flowers in the letter colour
    i, rc = p['ink'], FLAT[p['bg']][0]
    return B(p) + R(p, 'e', cols=(p['bg'], rc, i)) + top_clasp(p, 98) + foot(p, 124) + da(p, w=128)

V = [
 ('336', 'Clasp and foot flower in matching medallions', n336),
 ('337', 'The 153 diamond tile as the clasp', n337),
 ('338', 'Larger pattern in the band', n338),
 ('339', 'Band edged with fine double lines', n339),
 ('340', 'Band colours turned: rose diamonds, red flowers', n340),
]
CONCEPTS = [(f'Concept{n}', f'{n} · {t}', '0 0 300 300', fn) for n, t, fn in V]
