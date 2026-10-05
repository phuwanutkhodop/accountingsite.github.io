import math
from seals4 import *

def clip_circle(r, body, tag, p, cx=C, cy=C):
    u = p['bg'][1:] + tag
    return f'<clipPath id="k{u}"><circle cx="{cx}" cy="{cy}" r="{r}"></circle></clipPath><g clip-path="url(#k{u})">{body}</g>'
def lozenge_at(x, y, ang, hw, hh, line, fl, w=.9, fillc=None, flower_on=True):
    lz = f'M0,{-hh} L{hw},0 L0,{hh} L{-hw},0 Z'; inner = f'M0,{-hh * .6} L{hw * .6},0 L0,{hh * .6} L{-hw * .6},0 Z'
    st = f'fill: {fillc}' if fillc else 'fill: none'
    out = f'<g transform="translate({F(x)},{F(y)}) rotate({F(ang)})"><path d="{lz}" style="{st}; stroke: {line}; stroke-width: {w}"></path><path d="{inner}" style="fill: none; stroke: {line}; stroke-width: {w * .75}"></path>'
    if flower_on: out += f'<path d="{petals(0, 0, min(hw, hh) * .42) + petals(0, 0, min(hw, hh) * .42 * .52, rot=45, width=.4)}" style="fill: {fl}"></path>'
    return out + '</g>'
def polar_lattice(rings, line, fl, offset=True):
    """Concentric rings of diamonds pointing outward, like a rose window. rings = [(radius, count, half_w, half_h)]."""
    out = ''
    for k, (r, n, hw, hh) in enumerate(rings):
        off = (math.pi / n) if (offset and k % 2) else 0
        for j in range(n):
            a = 2 * math.pi * j / n + off
            out += lozenge_at(C + r * math.cos(a), C + r * math.sin(a), math.degrees(a) + 90, hw, hh, line, fl)
    return out
def name_arc(i, r=136, size=11): return arc_text(NAME, size, C, C, r, 'top', track=.16, fill=i)
def halo_mono(cx, cy, w, p, patterned=True):
    """Monogram with a paper halo so it reads cleanly over pattern."""
    i, bg = p['ink'], p['bg']; sc = w / 312.07
    halo = (f'<g transform="translate({F(cx - 176.03 * sc)},{F(cy - 113.16 * sc)}) scale({sc:.5f})">'
            f'<path d="{DP} {AP}" style="fill: {bg}; stroke: {bg}; stroke-width: {14 / sc:.1f}; stroke-linejoin: round"></path></g>')
    return halo + (mono_patterned(cx, cy, w, p) if patterned else mono(cx, cy, w, i))

def f208(p):   # the whole disc is the 153 lattice; the monogram cut out of it in paper; name round the rim
    i, bg = p['ink'], p['bg']
    s = name_arc(i) + ring(C, C, 126, i, 1) + lattice(C, C, 120, p, s=20, tag='f208')
    return s + mono(C, C + 4, 150, bg)
def f209(p):   # half and half: lattice above, a clear field below; divided by the accountant's double rule
    i, bg = p['ink'], p['bg']
    top = f'<rect x="0" y="0" width="300" height="{C + 18}" style="fill: none"></rect>' + lattice(C, C, 140, p, s=20, tag='f209')
    u = bg[1:] + 'f209'
    s = f'<clipPath id="h{u}"><rect x="0" y="0" width="300" height="{C + 18}"></rect></clipPath>'
    s += clip_circle(140, f'<g clip-path="url(#h{u})">{top}</g>', 'f209c', p) + ring(C, C, 140, i, 2.5)
    s += f'<line x1="14" y1="{C + 22}" x2="286" y2="{C + 22}" style="stroke: {i}; stroke-width: 1.4"></line><line x1="15" y1="{C + 28}" x2="285" y2="{C + 28}" style="stroke: {i}; stroke-width: 1.4"></line>'
    s += mono(C, C - 30, 150, bg)
    return s + f'<path d="{tx(TXT, "D.A. ACCOUNTING", 13, C, C + 70, .2)}" style="fill: {i}"></path><path d="{tx(TXT, "& CONSULTING", 13, C, C + 92, .2)}" style="fill: {i}"></path>'
def f210(p):   # a rose window: rings of diamonds, smaller toward the centre
    i, bg = p['ink'], p['bg']; r, sv = FLAT[bg]
    s = ring(C, C, 142, i, 2.5) + polar_lattice([(124, 28, 12, 15), (98, 22, 10.5, 12.5), (76, 16, 9, 10.5)], i, r)
    s += ring(C, C, 62, i, 1.2)
    return s + mono_patterned(C, C + 3, 84, p)
def f211(p):   # a field of flowers in concentric rings, growing toward the rim
    i, bg = p['ink'], p['bg']; r, sv = FLAT[bg]
    s = ring(C, C, 142, i, 2.5) + flower_ring(128, 36, 7, i) + flower_ring(108, 30, 5.6, r, math.pi / 30) + flower_ring(90, 24, 4.4, i) + flower_ring(74, 18, 3.4, r, math.pi / 18)
    return s + ring(C, C, 62, i, 1) + mono_patterned(C, C + 3, 86, p)
def f212(p):   # one great diamond set inside the circle, filled with the lattice; name round the top
    i, bg = p['ink'], p['bg']; u = bg[1:] + 'f212'
    d = f'M{C},{C - 122} L{C + 122},{C} L{C},{C + 122} L{C - 122},{C} Z'
    s = ring(C, C, 142, i, 2.5) + ring(C, C, 128, i, .8)
    s += f'<clipPath id="z{u}"><path d="{d}"></path></clipPath><g clip-path="url(#z{u})">{lattice(C, C, 130, p, s=18, tag="f212")}</g>'
    s += f'<path d="{d}" style="fill: none; stroke: {i}; stroke-width: 1.5"></path>'
    for a in (45, 135, 225, 315):
        s += flower(C + 98 * math.cos(math.radians(a)), C + 98 * math.sin(math.radians(a)), 8, i)
    return s + mono(C, C + 4, 112, bg)
def f213(p):   # quarters: lattice in two opposite quarters, flowers in the other two
    i, bg = p['ink'], p['bg']; r = FLAT[bg][0]; u = bg[1:] + 'f213'
    q = lambda a0: f'M{C},{C} L{F(C + 140 * math.cos(math.radians(a0)))},{F(C + 140 * math.sin(math.radians(a0)))} A140,140 0 0 1 {F(C + 140 * math.cos(math.radians(a0 + 90)))},{F(C + 140 * math.sin(math.radians(a0 + 90)))} Z'
    s = f'<clipPath id="q{u}"><path d="{q(-90)} {q(90)}"></path></clipPath><g clip-path="url(#q{u})">{lattice(C, C, 140, p, s=20, tag="f213")}</g>'
    for a0 in (0, 180):
        for rr, n in ((120, 9), (96, 7), (72, 5)):
            for k in range(n):
                a = math.radians(a0 + 90 * (k + .5) / n)
                s += flower(C + rr * math.cos(a), C + rr * math.sin(a), 5, r)
    s += ring(C, C, 140, i, 2.5) + f'<line x1="{C}" y1="10" x2="{C}" y2="290" style="stroke: {i}; stroke-width: 1"></line><line x1="10" y1="{C}" x2="290" y2="{C}" style="stroke: {i}; stroke-width: 1"></line>'
    return s + disc(C, C, 58, bg) + ring(C, C, 58, i, 1.2) + mono(C, C + 3, 84, i)
def f214(p):   # a sash of lattice crosses the circle; monogram above, name below
    i, bg = p['ink'], p['bg']; u = bg[1:] + 'f214'
    band = f'<clipPath id="b{u}"><polygon points="0,{C + 40} 300,{C - 10} 300,{C + 30} 0,{C + 80}"></polygon></clipPath>'
    s = clip_circle(140, band + f'<g clip-path="url(#b{u})">{lattice(C, C, 160, p, s=14, tag="f214")}</g>', 'f214c', p)
    s += ring(C, C, 140, i, 2.5) + ring(C, C, 133, i, .8)
    s += mono_patterned(C, C - 42, 128, p)
    return s + f'<path d="{tx(TXT, "D.A. ACCOUNTING", 12, C, C + 100, .2)}" style="fill: {i}"></path><path d="{tx(TXT, "& CONSULTING", 12, C, C + 118, .2)}" style="fill: {i}"></path>'
def f215(p):   # eight diamonds radiate from the centre like petals: the ประจำยาม drawn in diamonds
    i, bg = p['ink'], p['bg']; r = FLAT[bg][0]
    s = ring(C, C, 142, i, 2.5) + name_arc(i, 126, 10.5) + ring(C, C, 114, i, .8)
    for k in range(8):
        a = 2 * math.pi * k / 8 - math.pi / 2
        big = k % 2 == 0
        s += lozenge_at(C + (72 if big else 66) * math.cos(a), C + (72 if big else 66) * math.sin(a), math.degrees(a) + 90, 18 if big else 13, 36 if big else 26, i, r)
    return s + disc(C, C, 34, bg) + ring(C, C, 34, i, 1.2) + mono(C, C + 2, 50, i)
def f216(p):   # a wreath of large flowers touching, the monogram inside; name below the wreath
    i, bg = p['ink'], p['bg']; r = FLAT[bg][0]
    s = ring(C, C, 142, i, 2.5) + flower_ring(112, 16, 20, i) + flower_ring(112, 16, 8, r, math.pi / 16)
    s += disc(C, C, 86, bg) + ring(C, C, 86, i, 1)
    return s + mono_patterned(C, C + 3, 118, p)
def f217(p):   # the lattice at large scale: three tiles across, cropped by the circle; monogram on a paper halo
    i, bg = p['ink'], p['bg']
    s = clip_circle(140, lattice(C, C, 150, p, s=70, tag='f217'), 'f217c', p) + ring(C, C, 140, i, 2.5)
    return s + mono(C, C + 4, 156, bg)
def f218(p):   # layered rose window: necklace of diamonds, then a ring of flowers, then the monogram
    i, bg = p['ink'], p['bg']; r = FLAT[bg][0]
    s = ring(C, C, 143, i, 2.5) + lozenge_chain(128, 30, 12, 11, i, r) + ring(C, C, 113, i, .8)
    s += flower_ring(100, 24, 5, r) + ring(C, C, 88, i, 1) + name_arc(i, 72, 7.6)
    return s + mono_patterned(C, C + 6, 92, p)
def f219(p):   # a crescent: the lattice fills a moon-shaped band on the right; monogram and name sit left
    i, bg = p['ink'], p['bg']; u = bg[1:] + 'f219'
    s = f'<mask id="c{u}"><rect x="0" y="0" width="300" height="300" style="fill: #fff"></rect><circle cx="{C - 34}" cy="{C}" r="120" style="fill: #000"></circle></mask>'
    s += clip_circle(140, f'<g mask="url(#c{u})">{lattice(C, C, 150, p, s=18, tag="f219")}</g>', 'f219c', p)
    s += ring(C, C, 140, i, 2.5) + f'<circle cx="{C - 34}" cy="{C}" r="120" style="fill: none; stroke: {i}; stroke-width: 1.2"></circle>'
    s += mono_patterned(C - 30, C - 12, 150, p)
    return s + f'<path d="{tx(TXT, "D.A. ACCOUNTING", 11, C - 30, C + 62, .2)}" style="fill: {i}"></path><path d="{tx(TXT, "& CONSULTING", 11, C - 30, C + 80, .2)}" style="fill: {i}"></path>'

V = [
 ('208', 'Whole disc of lattice, monogram cut out', f208),
 ('209', 'Half lattice, half clear, double rule', f209),
 ('210', 'Rose window of diamonds', f210),
 ('211', 'Field of flowers in rings', f211),
 ('212', 'One great diamond in the circle', f212),
 ('213', 'Quarters: lattice and flowers', f213),
 ('214', 'A sash of lattice across', f214),
 ('215', 'Eight diamond petals', f215),
 ('216', 'Wreath of flowers', f216),
 ('217', 'Lattice at large scale', f217),
 ('218', 'Layered rose window', f218),
 ('219', 'Crescent of lattice', f219),
]
CONCEPTS = [(f'Concept{n}', f'{n} · {t}', '0 0 300 300', fn) for n, t, fn in V]
