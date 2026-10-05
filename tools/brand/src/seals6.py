import math
from seals5 import *

def classic_frame(i, inner=True):
    return ring(C, C, 140, i, 3) + ring(C, C, 133, i, 1) + (ring(C, C, 96, i, 1) + ring(C, C, 90, i, 3) if inner else '')
def lozenge_dots(r, n, hw, hh, c):
    return ''.join(f'<g transform="translate({F(C + r * math.cos(2 * math.pi * k / n))},{F(C + r * math.sin(2 * math.pi * k / n))}) rotate({F(360 * k / n + 90)})"><path d="M0,{-hh} L{hw},0 L0,{hh} L{-hw},0 Z" style="fill: {c}"></path></g>' for k in range(n))
def split_name(i, r=107, size=13):
    """Name split in two arcs, left and right of the top centre, leaving room for a flower at 12 o'clock."""
    from marks6 import gw
    def span(t): return (sum(gw(TXT, c, size) if c != ' ' else size * .3 for c in t) + .13 * size * (len(t) - 1)) / r
    a, b = 'D.A. ACCOUNTING', '& CONSULTING'
    gap = .2
    out = ''
    for t, centre in ((a, -math.pi / 2 - gap - span(a) / 2), (b, -math.pi / 2 + gap + span(b) / 2)):
        rot = math.degrees(centre + math.pi / 2)
        out += f'<g transform="rotate({F(rot)} {C} {C})">' + arc_text(t, size, C, C, r, 'top', track=.13, fill=i) + '</g>'
    return out

def g220(p):   # one flower sets the name apart at the top, like a clasp
    i = p['ink']; r = FLAT[p['bg']][0]
    s = classic_frame(i) + split_name(i) + flower(C, C - 112, 7, i) + arc_text(SUB, 13, C, C, 121, 'bottom', track=.13, fill=i)
    return s + mono(C, C + 4, 112, i)
def g221(p):   # the inner ring becomes a thin band of lattice
    i = p['ink']
    s = ring(C, C, 140, i, 3) + ring(C, C, 133, i, 1) + top_bottom(i) + seps(114, 6, i)
    s += band(p, 89, 96, lattice(C, C, 96, p, s=9, tag='g221'), 'g221') + ring(C, C, 96, i, 1) + ring(C, C, 89, i, 1)
    return s + mono(C, C + 4, 112, i)
def g222(p):   # the monogram sits in a small diamond frame within the circle
    i = p['ink']; r = FLAT[p['bg']][0]
    s = classic_frame(i, inner=False) + ring(C, C, 96, i, 1) + top_bottom(i) + seps(114, 6, i)
    d = lambda k: f'{C},{F(C - 86 * k)} {F(C + 86 * k)},{C} {C},{F(C + 86 * k)} {F(C - 86 * k)},{C}'
    s += f'<polygon points="{d(1)}" style="fill: none; stroke: {r}; stroke-width: 1.2"></polygon><polygon points="{d(.93)}" style="fill: none; stroke: {r}; stroke-width: .6"></polygon>'
    return s + mono(C, C + 4, 104, i)
def g223(p):   # the inner ring drawn as a line of tiny diamonds
    i = p['ink']
    s = ring(C, C, 140, i, 3) + ring(C, C, 133, i, 1) + top_bottom(i) + seps(114, 6, i)
    s += lozenge_dots(93, 72, 2.2, 3.2, i)
    return s + mono(C, C + 4, 112, i)
def g224(p):   # three graded flowers in place of the second line
    i = p['ink']
    s = classic_frame(i) + top_bottom(i).split('</path>', 1)[0] if False else classic_frame(i) + name_top(i)
    s += bottom_flowers(115, 3, 8, i, span=22, graded=True)
    return s + mono(C, C + 4, 112, i)
def g225(p):   # four small diamonds set into the outer ring at the quarters, like stones in a bezel
    i, bg = p['ink'], p['bg']; r = FLAT[bg][0]
    s = classic_frame(i) + top_bottom(i) + seps(114, 6, i)
    for a in (0, 90, 180, 270):
        x, y = C + 136.5 * math.cos(math.radians(a)), C + 136.5 * math.sin(math.radians(a))
        s += f'<g transform="translate({F(x)},{F(y)}) rotate({a + 90})"><path d="M0,-9 L6,0 L0,9 L-6,0 Z" style="fill: {i}; stroke: {bg}; stroke-width: 2"></path></g>'
    return s + mono(C, C + 4, 112, i)
def g226(p):   # a faint flower watermark behind the monogram
    i = p['ink']; r = FLAT[p['bg']][0]
    s = classic_frame(i) + top_bottom(i) + seps(114, 6, i)
    s += f'<path d="{petals(C, C, 80, width=.3) + petals(C, C, 44, rot=45, width=.36)}" style="fill: {r}; fill-opacity: .22"></path>'
    return s + mono(C, C + 4, 112, i)
def g227(p):   # a whisper of lattice inside the centre, barely there
    i = p['ink']; bg = p['bg']; r = FLAT[bg][0]
    lt = lattice(C, C, 90, p, s=16, tag='g227').replace(f'fill: {i}"></circle>', f'fill: {bg}"></circle>', 1)
    lt = lt.replace(f'stroke: {r}; stroke-width: .8', f'stroke: {r}; stroke-width: .5; stroke-opacity: .55').replace(f'fill: {FLAT[bg][1]}"', f'fill: {r}; fill-opacity: .4"')
    s = classic_frame(i) + top_bottom(i) + seps(114, 6, i) + lt + ring(C, C, 90, i, 3)
    return s + disc(C, C + 2, 0, bg) + mono(C, C + 4, 112, i)
def g228(p):   # a fine necklace of diamonds replaces the inner rings
    i = p['ink']; r = FLAT[p['bg']][0]
    s = ring(C, C, 140, i, 3) + ring(C, C, 133, i, 1) + top_bottom(i) + seps(114, 6, i)
    s += lozenge_chain(92, 36, 6, 5.5, i, r)
    return s + mono(C, C + 4, 108, i)
def g229(p):   # the accountant's double underline under the monogram, a flower at each end
    i = p['ink']
    s = classic_frame(i) + top_bottom(i) + seps(114, 6, i)
    s += f'<line x1="{C - 52}" y1="{C + 40}" x2="{C + 52}" y2="{C + 40}" style="stroke: {i}; stroke-width: 1.2"></line><line x1="{C - 52}" y1="{C + 45}" x2="{C + 52}" y2="{C + 45}" style="stroke: {i}; stroke-width: 1.2"></line>'
    s += flower(C - 60, C + 42.5, 4, i) + flower(C + 60, C + 42.5, 4, i)
    return s + mono(C, C - 4, 106, i)
def g230(p):   # only the rim changes: a fine microtext line between the outer rings
    i = p['ink']
    s = ring(C, C, 144, i, 2) + microtext(136.5, 4.6, i) + ring(C, C, 132, i, 1) + ring(C, C, 96, i, 1) + ring(C, C, 90, i, 3)
    return s + top_bottom(i, rt=105, rb=119) + seps(112, 6, i) + mono(C, C + 4, 112, i)
def g231(p):   # the classic seal with the patterned 153 monogram and one flower as the clasp
    i = p['ink']
    s = classic_frame(i) + split_name(i) + flower(C, C - 112, 7, i) + arc_text(SUB, 13, C, C, 121, 'bottom', track=.13, fill=i)
    return s + mono_patterned(C, C + 4, 118, p)

V = [
 ('220', 'One flower as a clasp at the top', g220),
 ('221', 'Inner ring as a thin lattice band', g221),
 ('222', 'Monogram in a small diamond frame', g222),
 ('223', 'Inner ring of tiny diamonds', g223),
 ('224', 'Three graded flowers below', g224),
 ('225', 'Four diamonds set in the rim', g225),
 ('226', 'Faint flower watermark', g226),
 ('227', 'A whisper of lattice in the centre', g227),
 ('228', 'Fine necklace of diamonds', g228),
 ('229', 'Double underline with flowers', g229),
 ('230', 'Microtext rim', g230),
 ('231', 'Flower clasp + patterned monogram', g231),
]
CONCEPTS = [(f'Concept{n}', f'{n} · {t}', '0 0 300 300', fn) for n, t, fn in V]
