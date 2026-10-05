"""Seal round 11: the inner layer is a band (as 314), in red and reversed; one large flower at the foot (as 304)."""
import math
from seals10 import *

def pband(p, ri, ro, s=10, rev=False, edge=None, tag='pb', cols=None):
    """A pattern band between ri and ro, edged by two fine rings. One 153 tile, repeated (SVG pattern), aligned so a
    tile centre sits at the seal centre. Red: letter-colour ground, rose rings, silver flowers.
    Reversed: background ground, rings in the letter colour, rose flowers."""
    i, bg = p['ink'], p['bg']; rc, sc = FLAT[bg]
    ground, line, flc, lw = (bg, i, rc, .6) if rev else (i, rc, sc, .8)
    if cols: ground, line, flc = cols
    h = s * 1.4; d = ''; fl = ''
    for x, y in ((s / 2, h / 2), (0, 0), (s, 0), (0, h), (s, h)):
        for q in (.94, .62): d += f'M{F(x)},{F(y - h / 2 * q)} L{F(x + s / 2 * q)},{F(y)} L{F(x)},{F(y + h / 2 * q)} L{F(x - s / 2 * q)},{F(y)} Z '
        fl += petals(x, y, s * .17) + petals(x, y, s * .17 * .52, rot=45, width=.4)
    u = 'pt' + bg[1:] + tag
    ann = f'M{C - ro},{C} a{ro},{ro} 0 1 0 {2 * ro},0 a{ro},{ro} 0 1 0 {-2 * ro},0 Z M{C - ri},{C} a{ri},{ri} 0 1 0 {2 * ri},0 a{ri},{ri} 0 1 0 {-2 * ri},0 Z'
    e = edge or i
    return (f'<pattern id="{u}" patternUnits="userSpaceOnUse" x="{F(C - s / 2)}" y="{F(C - h / 2)}" width="{F(s)}" height="{F(h)}">'
            f'<rect width="{F(s)}" height="{F(h)}" style="fill: {ground}"></rect><path d="{d}" style="fill: none; stroke: {line}; stroke-width: {lw}"></path>'
            f'<path d="{fl}" style="fill: {flc}"></path></pattern>'
            f'<path d="{ann}" style="fill: url(#{u}); fill-rule: evenodd"></path>' + ring(C, C, ro, e, 1) + ring(C, C, ri, e, 1))
def foot(p, r=122, size=11):
    return disc(C, C + r, size, p['bg']) + flower(C, C + r, size, p['ink'])
def foot_tile(p, r=122, s=15):
    """The 153 tile itself at the foot: two diamond rings and the flower."""
    i, rc = p['ink'], FLAT[p['bg']][0]; x, y = C, C + r; hw, hh = s * .62, s
    lz = lambda q: f'M{F(x)},{F(y - hh * q)} L{F(x + hw * q)},{F(y)} L{F(x)},{F(y + hh * q)} L{F(x - hw * q)},{F(y)} Z '
    return (f'<path d="{lz(1.12)}" style="fill: {p["bg"]}"></path><path d="{lz(.94)} {lz(.62)}" style="fill: none; stroke: {rc}; stroke-width: .9"></path>'
            + flower(x, y, hw * .62, i))
def top_clasp(p, r, size=8):
    return disc(C, C - r, size + 1, p['bg']) + flower(C, C - r, size, p['ink'])

B = lambda p, **k: base(p, r=124, fs=5.4, ds=4.6, **k)          # the 295 arc, sized for a band inside it
def m316(p): return B(p) + pband(p, 92, 104, tag='a') + foot(p, 124) + da(p, w=128)
def m317(p): return B(p) + pband(p, 92, 104, rev=True, tag='b') + foot(p, 124) + da(p, w=128)
def big(p):   # the name moved out to make room for a larger band
    i, r = p['ink'], FLAT[p['bg']][0]
    return pair(i) + arc_text(NAME, 12.5, C, C, 121, 'top', track=.14, fill=i) + alt_arc(126, 15, 150, 5, 4.3, i, r, graded=True)
def m318(p): return big(p) + pband(p, 97, 110, s=11, tag='c') + foot(p, 126, 10) + da(p, w=136)
def m319(p): return big(p) + pband(p, 97, 110, s=11, rev=True, tag='d') + foot(p, 126, 10) + da(p, w=136)
def m320(p): return B(p) + pband(p, 92, 104, tag='e') + top_clasp(p, 98) + foot(p, 124) + da(p, w=128)
def m321(p): return B(p) + pband(p, 92, 104, rev=True, tag='f') + top_clasp(p, 98) + foot(p, 124) + da(p, w=128)
def m322(p): return B(p) + pband(p, 97, 104, s=8, tag='g') + foot(p, 124) + da(p, w=132)
def m323(p): return B(p) + pband(p, 97, 104, s=8, rev=True, tag='h') + foot(p, 124) + da(p, w=132)
def m324(p): return B(p) + pband(p, 84, 104, s=12, tag='i') + foot(p, 124) + da(p, w=122)
def m325(p): return B(p) + pband(p, 84, 104, s=12, rev=True, tag='j') + foot(p, 124) + da(p, w=122)
def m326(p): return B(p) + pband(p, 88, 106, s=15, tag='k') + foot(p, 124) + da(p, w=126)
def m327(p):   # the band hugs D A; the arc sits just outside it
    return base(p, r=110, span=140, n=13, fs=5, ds=4.3) + pband(p, 80, 92, s=9, tag='l') + foot(p, 110, 9.5) + da(p, w=124)
def m328(p):   # two layers: red outside, reversed inside
    return B(p) + pband(p, 98, 106, s=8, tag='m') + pband(p, 89, 98, s=8, rev=True, tag='n') + foot(p, 124) + da(p, w=126)
def m329(p): i = p['ink']; return B(p, dc=i, kind='gem') + pband(p, 92, 104, tag='o') + foot(p, 124) + da(p, w=128)
def m330(p): i = p['ink']; return B(p, dc=i, kind='gem') + pband(p, 92, 104, rev=True, tag='q') + foot(p, 124) + da(p, w=128)
def m331(p): return B(p, span=180, n=17) + pband(p, 92, 104, tag='r') + foot(p, 124, 13) + da(p, w=128)
def m332(p):   # no ring pair: one fine outer ring
    i = p['ink']; return ring(C, C, 140, i, 1.2) + B(p, pair_on=False) + pband(p, 92, 104, tag='s') + foot(p, 124) + da(p, w=128)
def m333(p): return B(p) + pband(p, 92, 104, rev=True, edge=FLAT[p['bg']][0], tag='t') + foot(p, 124) + da(p, w=128)
def m334(p): i, r = p['ink'], FLAT[p['bg']][0]; return B(p, fc=r, dc=i) + pband(p, 92, 104, rev=True, tag='u') + foot(p, 124) + da(p, w=128)
def m335(p): return B(p) + pband(p, 92, 104, tag='v') + foot_tile(p, 123, 19) + da(p, w=128)

V = [
 ('316', 'Red pattern band + one large foot flower', m316),
 ('317', 'Reversed band (cream, red pattern) + foot flower', m317),
 ('318', 'Larger red band', m318),
 ('319', 'Larger reversed band', m319),
 ('320', 'Red band with a flower clasp at the top', m320),
 ('321', 'Reversed band with a flower clasp', m321),
 ('322', 'Thin red band', m322),
 ('323', 'Thin reversed band', m323),
 ('324', 'Wide red band', m324),
 ('325', 'Wide reversed band', m325),
 ('326', 'Red band, larger pattern', m326),
 ('327', 'Band close around D A', m327),
 ('328', 'Two layers: red outside, reversed inside', m328),
 ('329', 'Red band + gem diamonds', m329),
 ('330', 'Reversed band + gem diamonds', m330),
 ('331', 'Red band, wider arc, larger foot flower', m331),
 ('332', 'Red band, one fine outer ring', m332),
 ('333', 'Reversed band with rose edges', m333),
 ('334', 'Reversed band + swapped arc colours', m334),
 ('335', 'Red band, the 153 diamond tile at the foot', m335),
]
CONCEPTS = [(f'Concept{n}', f'{n} · {t}', '0 0 300 300', fn) for n, t, fn in V]
