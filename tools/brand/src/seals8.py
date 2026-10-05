"""Seal round 8. Rules: DA is always the full 153 monogram; no CO., LTD.; the thick+thin ring pair is allowed, never required."""
import math
from seals7 import *
from seals import PAL as SP
INV = {'#7a2229': 'mkL', '#f6efe8': 'mk', '#efe6dc': 'mk'}         # palette for a monogram set on a disc of the ink colour
def da_on_ink(p, w=130, y=0): return mono_patterned(C, C - 2 + y, w, SP[INV[p['ink']]])
def arcs(r0, r1, a0, a1, c, w):
    pt = lambda a: (C + r0 * math.cos(math.radians(a)), C + r0 * math.sin(math.radians(a)))
    (x0, y0), (x1, y1) = pt(a0), pt(a1); large = 1 if (a1 - a0) % 360 > 180 else 0
    return f'<path d="M{F(x0)},{F(y0)} A{r0},{r0} 0 {large} 1 {F(x1)},{F(y1)}" style="fill: none; stroke: {c}; stroke-width: {w}"></path>'
def pair_arc(i, a0, a1): return arcs(141, 0, a0, a1, i, 3.2) + arcs(134.5, 0, a0, a1, i, 1)
def straight_name(i, y, size=12, lines=False):
    if not lines: return f'<path d="{tx(TXT, NAME, size, C, y, .18)}" style="fill: {i}"></path>'
    return f'<path d="{tx(TXT, "D.A. ACCOUNTING", size, C, y, .2)}" style="fill: {i}"></path><path d="{tx(TXT, "& CONSULTING", size, C, y + size * 1.6, .2)}" style="fill: {i}"></path>'
def pearls(r, n, rad, c): return dot_ring(r, n, rad, c)

# ---------- A. circles made of elements, not lines ----------
def i244(p): i, r = p['ink'], FLAT[p['bg']][0]; return flower_ring(136, 40, 6, i) + name(i) + da(p)
def i245(p): i, r = p['ink'], FLAT[p['bg']][0]; return lozenge_chain(134, 34, 9, 9, i, r) + arc_text(NAME, 13, C, C, 104, 'top', track=.14, fill=i) + da(p, w=126)
def i246(p):   # the name itself draws the circle, twice round, with flowers between
    i, r = p['ink'], FLAT[p['bg']][0]
    s = arc_text(NAME, 11.5, C, C, 128, 'top', track=.12, fill=i) + arc_text(NAME, 11.5, C, C, 138, 'bottom', track=.12, fill=i)
    s += ''.join(flower(C + 133 * math.cos(math.radians(a)), C + 133 * math.sin(math.radians(a)), 6, r) for a in (0, 180))
    return s + da(p, w=150)
def i247(p): i = p['ink']; return pearls(138, 72, 2.2, i) + pearls(130, 72, 1.1, FLAT[p['bg']][0]) + name(i) + bottom_flowers(112, 5, 8, i, span=52, graded=True) + da(p)
def i248(p): i = p['ink']; return band(p, 124, 142, lattice(C, C, 142, p, s=12, tag='i248'), 'i248') + arc_text(NAME, 12.5, C, C, 104, 'top', track=.14, fill=i) + da(p, w=126)

# ---------- B. broken or partial circles ----------
def i249(p):   # the ring pair opens at the top; the name sits straight in the gap
    i = p['ink']; return pair_arc(i, -58, 238) + straight_name(i, 30, 10.6) + bottom_flowers(112, 5, 8, i, span=52, graded=True) + da(p, w=146, y=6)
def i250(p):   # the ring pair opens at the foot for a single flower
    i = p['ink']; return pair_arc(i, 100, 80 + 360) + flower(C, C + 138, 11, i) + name(i) + da(p)
def i251(p):   # two arcs like brackets, one for each founder; name below
    i, r = p['ink'], FLAT[p['bg']][0]
    s = pair_arc(i, 110, 250) + arcs(141, 0, -70, 70, i, 3.2) + arcs(134.5, 0, -70, 70, i, 1)
    s += flower(C, C - 136, 7, r) + flower(C, C + 136, 7, r)
    return s + da(p, w=150, y=-12) + straight_name(i, C + 74, 10.4)
def i252(p):   # a three-quarter ring; the name finishes the circle
    i = p['ink']; return pair_arc(i, -30, 210) + arc_text(NAME, 13.5, C, C, 133, 'top', track=.14, fill=i) + bottom_flowers(112, 3, 8.5, i, span=24, graded=True) + da(p)
def i253(p):   # the ring pair broken by four flowers at the quarters
    i = p['ink']; s = ''
    for a in (0, 90, 180, 270): s += pair_arc(i, a + 9, a + 81)
    for a in (0, 90, 180, 270): s += flower(C + 138 * math.cos(math.radians(a)), C + 138 * math.sin(math.radians(a)), 8, i)
    return s + arc_text(NAME, 13, C, C, 112, 'top', track=.14, fill=i) + da(p)

# ---------- C. the circle as a filled shape ----------
def i254(p):   # a solid disc; the monogram sits in it in reverse, still in full detail
    i, bg = p['ink'], p['bg']
    return disc(C, C, 142, i) + ring(C, C, 135, bg, .8) + arc_text(NAME, 13, C, C, 112, 'top', track=.14, fill=bg) + bottom_flowers(112, 5, 8, bg, span=52, graded=True) + da_on_ink(p)
def i255(p):   # a light rose disc
    i, bg = p['ink'], p['bg']; r = FLAT[bg][0]
    return disc(C, C, 142, r) + f'<circle cx="{C}" cy="{C}" r="142" style="fill: {bg}; fill-opacity: .55"></circle>' + ring(C, C, 142, i, 2) + name(i) + bottom_flowers(112, 5, 8, i, span=52, graded=True) + da(p)
def i256(p):   # a disc with a petalled edge
    i, bg = p['ink'], p['bg']
    s = lobes(24, 128, 18, i, bg, 2.6, 2.6, .9)
    return s + arc_text(NAME, 12.5, C, C, 108, 'top', track=.14, fill=i) + bottom_flowers(108, 3, 7, i, span=22, graded=True) + da(p, w=128)

# ---------- D. the name placed differently ----------
def i257(p):   # name straight across under the monogram, flowers either end
    i = p['ink']; return pair(i) + da(p, y=-14, w=146) + straight_name(i, C + 66, 9.2) + flower(C - 116, C + 63, 4, i) + flower(C + 116, C + 63, 4, i) + flower(C, C - 112, 8, i)
def i258(p):   # name on the bottom arc, reading level; a flower crown at the top
    i = p['ink']
    s = pair(i) + arc_text(NAME, 12.5, C, C, 121, 'bottom', track=.14, fill=i)
    s += ''.join(flower(C + 116 * math.cos(math.radians(a)), C + 116 * math.sin(math.radians(a)), sz, i) for a, sz in ((-90, 9), (-104, 6), (-76, 6), (-117, 4), (-63, 4)))
    return s + da(p, y=4)
def i259(p):   # name in two lines inside the circle, under the monogram
    i = p['ink']; return pair(i) + da(p, y=-22, w=146) + straight_name(i, C + 56, 12.5, lines=True) + flower(C, C - 116, 7, i)
def i260(p):   # no name at all: an emblem of monogram and flowers
    i, r = p['ink'], FLAT[p['bg']][0]; return pair(i) + flower_ring(118, 24, 5.5, r) + flower_ring(118, 24, 2.6, i, math.pi / 24) + da(p, w=150)

# ---------- E. the ring pair, varied ----------
def i261(p):   # the pair reversed: thin outside, thick inside
    i = p['ink']; return ring(C, C, 141, i, 1) + ring(C, C, 135.5, i, 3.2) + name(i) + bottom_flowers(112, 5, 8, i, span=52, graded=True) + da(p)
def i262(p):   # flowers sit on the thick line at eight points
    i, bg = p['ink'], p['bg']; s = pair(i)
    for k in range(8):
        a = math.radians(45 * k + 22.5); x, y = C + 141 * math.cos(a), C + 141 * math.sin(a)
        s += disc(x, y, 7, bg) + flower(x, y, 6.5, i)
    return s + name(i) + da(p)
def i263(p):   # a fine necklace of diamonds runs between the thick and thin lines
    i, r = p['ink'], FLAT[p['bg']][0]
    return ring(C, C, 143, i, 3) + lozenge_chain(134, 52, 4.6, 4.6, i, r) + ring(C, C, 125, i, 1) + arc_text(NAME, 13, C, C, 104, 'top', track=.14, fill=i) + da(p, w=126)
def i264(p):   # the name set over a whisper of lattice in its band
    i, bg = p['ink'], p['bg']; r, sv = FLAT[bg]
    lt = lattice(C, C, 134, p, s=10, tag='i264').replace(f'fill: {i}"></circle>', f'fill: {bg}"></circle>', 1).replace(f'stroke: {r}; stroke-width: .8', f'stroke: {r}; stroke-width: .45; stroke-opacity: .5').replace(f'fill: {sv}"', f'fill: {r}; fill-opacity: .3"')
    return pair(i) + band(p, 98, 134, lt, 'i264') + ring(C, C, 98, i, .8) + arc_text(NAME, 13, C, C, 110, 'top', track=.14, fill=i) + da(p, w=126)

# ---------- F. two founders ----------
def i265(p):   # two circles overlap; a flower where they meet; the monogram across both
    i, r = p['ink'], FLAT[p['bg']][0]
    s = ''.join(ring(C + dx, C, 112, i, 2) + ring(C + dx, C, 106, i, .8) for dx in (-26, 26))
    s += flower(C, C - 109, 7, r) + flower(C, C + 109, 7, r)
    return s + da(p, w=150) + straight_name(i, C + 140, 10)
def i266(p):   # half lattice under the D, half flowers under the A
    i, bg = p['ink'], p['bg']; r = FLAT[bg][0]; u = bg[1:] + 'i266'
    s = f'<clipPath id="l{u}"><rect x="0" y="0" width="{C}" height="300"></rect></clipPath>'
    s += clip_circle(128, f'<g clip-path="url(#l{u})">{lattice(C, C, 140, p, s=14, tag="i266")}</g>', 'i266c', p)
    for rr, n in ((116, 9), (96, 7), (76, 5)):
        for k in range(n):
            a = math.radians(-90 + 180 * (k + .5) / n); s += flower(C + rr * math.cos(a), C + rr * math.sin(a), 4.2, r)
    s += pair(i) + disc(C, C - 4, 62, bg)
    return s + da(p, w=120)

# ---------- G. other ideas ----------
def i267(p):   # a compass of diamonds pointing outward round the circle
    i, r = p['ink'], FLAT[p['bg']][0]; s = pair(i)
    for k in range(16):
        a = 360 * k / 16; big = k % 4 == 0
        s += lozenge_at(C + 124 * math.cos(math.radians(a)), C + 124 * math.sin(math.radians(a)), a + 90, 5 if big else 3.4, 9 if big else 6, i, r, flower_on=big)
    return s + arc_text(NAME, 12, C, C, 100, 'top', track=.14, fill=i) + da(p, w=122)
def i268(p):   # fine engraved rays behind the monogram
    i, r = p['ink'], FLAT[p['bg']][0]
    rays = ''.join(f'<line x1="{F(C + 62 * math.cos(a))}" y1="{F(C + 62 * math.sin(a))}" x2="{F(C + 100 * math.cos(a))}" y2="{F(C + 100 * math.sin(a))}" style="stroke: {r}; stroke-width: .6"></line>' for a in [2 * math.pi * k / 96 for k in range(96)])
    return pair(i) + rays + name(i) + bottom_flowers(118, 3, 7, i, span=20, graded=True) + da(p, w=126)
def i269(p):   # the monogram breaks out of the circle: letters larger than the ring
    i = p['ink']; return pair(i) + flower(C, C - 128, 8, i) + bottom_flowers(126, 5, 6, i, span=40, graded=True) + da(p, w=230)
def i270(p):   # a wreath: two flower branches curve up the sides; name below
    i, r = p['ink'], FLAT[p['bg']][0]; s = ''
    for side in (-1, 1):
        for k in range(9):
            a = math.radians(90 + side * (24 + 15 * k)); sz = 7.5 - .5 * k
            s += flower(C + 126 * math.cos(a), C + 126 * math.sin(a), sz, i if k % 2 == 0 else r)
    return s + flower(C, C + 128, 9, i) + da(p, w=150, y=-8) + straight_name(i, C + 74, 9.6)
def i271(p):   # a small circle of flowers round the monogram, a large ring of name outside
    i, r = p['ink'], FLAT[p['bg']][0]
    return pair(i) + name(i) + flower_ring(90, 28, 3.6, r) + bottom_flowers(114, 3, 7, i, span=20, graded=True) + da(p, w=118)

V = [
 ('244', 'A · circle of flowers', i244), ('245', 'A · circle of diamonds', i245), ('246', 'A · the name draws the circle', i246),
 ('247', 'A · ring of pearls', i247), ('248', 'A · lattice band as the circle', i248),
 ('249', 'B · ring open at the top for the name', i249), ('250', 'B · ring open at the foot for a flower', i250),
 ('251', 'B · two arcs, one per founder', i251), ('252', 'B · three-quarter ring', i252), ('253', 'B · ring broken by four flowers', i253),
 ('254', 'C · solid disc, monogram reversed', i254), ('255', 'C · light rose disc', i255), ('256', 'C · petalled edge', i256),
 ('257', 'D · name straight under the monogram', i257), ('258', 'D · name on the bottom arc, flower crown', i258),
 ('259', 'D · name in two lines', i259), ('260', 'D · emblem without the name', i260),
 ('261', 'E · ring pair reversed', i261), ('262', 'E · flowers set on the ring', i262), ('263', 'E · necklace between the lines', i263),
 ('264', 'E · name over a whisper of lattice', i264),
 ('265', 'F · two founders, two circles', i265), ('266', 'F · lattice for D, flowers for A', i266),
 ('267', 'G · compass of diamonds', i267), ('268', 'G · engraved rays', i268), ('269', 'G · monogram breaks out of the ring', i269),
 ('270', 'G · wreath of flowers', i270), ('271', 'G · small flower ring inside', i271),
]
CONCEPTS = [(f'Concept{n}', f'{n} · {t}', '0 0 300 300', fn) for n, t, fn in V]
