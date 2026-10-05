import math
from marks9 import DP, AP, W, HH, F
from marks7 import name_d
from marks12 import PAL, LINE, lozenge

def petals(cx, cy, r, n=4, width=.34, bulge=.55, rot=0):
    d = ''
    for k in range(n):
        a = math.radians(rot + 360 / n * k); ca, sa = math.cos(a), math.sin(a)
        w = r * width
        tip = (cx + r * ca, cy + r * sa)
        l = (cx - w * sa + r * bulge * ca, cy + w * ca + r * bulge * sa)
        rr = (cx + w * sa + r * bulge * ca, cy - w * ca + r * bulge * sa)
        d += f'M{F(cx)},{F(cy)} Q{F(l[0])},{F(l[1])} {F(tip[0])},{F(tip[1])} Q{F(rr[0])},{F(rr[1])} {F(cx)},{F(cy)} Z '
    return d
def circle(cx, cy, r): return f'M{F(cx - r)},{F(cy)} a{F(r)},{F(r)} 0 1 0 {F(2 * r)},0 a{F(r)},{F(r)} 0 1 0 {F(-2 * r)},0 Z '

def design(ring='gold', flowerc=None, s=44, ratio=1.4, levels=(.94, .62), fs=.17, style='pointed',
           alternate=False, target='both', width=1.0, tag=''):
    flowerc = flowerc or ring
    def build(p):
        rc, ro = LINE[ring](p); fc, fo = LINE[flowerc](p)
        h = s * ratio; rings = ''; fl = ''; fl_out = ''; holes = ''; dots = ''
        for j in range(-1, int(HH / (h / 2)) + 3):
            for i in range(-1, int(W / s) + 2):
                cx = i * s + (s / 2 if j % 2 else 0); cy = j * h / 2
                for k in levels: rings += lozenge(cx, cy, s / 2 * k, h / 2 * k)
                r = min(s, h) * fs
                if alternate and (i + j) % 2:
                    fl += lozenge(cx, cy, s / 2 * .13, h / 2 * .13); continue
                if style == 'pointed': fl += petals(cx, cy, r)
                elif style == 'round': fl += petals(cx, cy, r, width=.5, bulge=.62)
                elif style == 'eight': fl += petals(cx, cy, r) + petals(cx, cy, r * .52, rot=45, width=.4)
                elif style == 'ring':
                    fl += petals(cx, cy, r); holes += circle(cx, cy, r * .24); dots += circle(cx, cy, r * .1)
                elif style == 'outline': fl_out += petals(cx, cy, r, width=.42)
        u = p['bg'][1:] + tag
        art = f'<path d="{rings}" style="fill: none; stroke: {rc}; stroke-opacity: {ro}; stroke-width: {width}; stroke-linejoin: miter"></path>'
        if fl: art += f'<path d="{fl}" style="fill: {fc}; fill-opacity: {fo}"></path>'
        if holes:   # a ring at the heart of the flower: letter colour, then a small gold dot
            art += f'<path d="{holes}" style="fill: {p["ink"]}"></path><path d="{dots}" style="fill: {fc}; fill-opacity: {fo}"></path>'
        if fl_out: art += f'<path d="{fl_out}" style="fill: none; stroke: {fc}; stroke-opacity: {fo}; stroke-width: {width * .9}"></path>'
        s_ = (f'<clipPath id="x{u}"><path d="{DP} {AP}" style="clip-rule: evenodd"></path></clipPath>'
              f'<clipPath id="d{u}"><path d="{DP}"></path></clipPath>')
        s_ += f'<path d="{DP} {AP}" style="fill: {p["ink"]}; fill-rule: evenodd"></path>'
        inner = art if target == 'both' else f'<g clip-path="url(#d{u})">{art}</g>'
        return s_ + f'<g clip-path="url(#x{u})">{inner}</g>' + name_d(p, 176, 254, 312)
    return build
def petals_only(d): return ''

V = [
 ('125', 'Flower · rounded petals',                 design(style='round', tag='a')),
 ('126', 'Flower · eight points',                    design(style='eight', tag='b')),
 ('127', 'Flower · with a centre ring',              design(style='ring', fs=.2, tag='c')),
 ('128', 'Flower · outline only',                    design(style='outline', fs=.19, tag='d')),
 ('129', 'Rhythm · one ring, larger flower',         design(levels=(.94,), fs=.24, tag='e')),
 ('130', 'Rhythm · three rings, smaller flower',     design(levels=(.95, .72, .5), fs=.12, tag='f')),
 ('131', 'Rhythm · flower and gem alternating',      design(alternate=True, tag='g')),
 ('132', 'Rhythm · smaller scale',                   design(s=32, width=.8, tag='h')),
 ('133', 'Colour · deep, tone on tone',              design(ring='deep', tag='i')),
 ('134', 'Colour · soft rose',                       design(ring='rose', tag='j')),
 ('135', 'Colour · quiet rings, gold flowers',       design(ring='deep', flowerc='gold', tag='k')),
 ('136', 'Colour · D only',                          design(target='D', tag='l')),
]
VB = '0 -6 362 280'
CONCEPTS = [(f'Concept{n}', f'{n} · {t}', VB, fn) for n, t, fn in V]
