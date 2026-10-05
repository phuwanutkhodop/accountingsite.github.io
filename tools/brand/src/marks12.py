import math
from marks9 import DP, AP, W, HH, F
from marks7 import name_d
PAL = {
 'mk':  dict(bg='#f2eeea', ink='#7a2229', deep='#3a1316', kind='day'),
 'mkL': dict(bg='#7a2229', ink='#f6efe8', deep='#3a1316', kind='light'),
 'mkN': dict(bg='#1b1112', ink='#efe6dc', deep='#3a1316', kind='light'),
}
# line colours, defined per background so they always sit on the letter colour correctly
LINE = {
 'white':   lambda p: (p['bg'], 1),
 'gold':    lambda p: ('#e3c891', 1) if p['kind'] == 'day' else ('#7d5f28', .9),
 'rose':    lambda p: ('#f2eeea', .45) if p['kind'] == 'day' else ('#7a2229', .42),
 'deep':    lambda p: ('#3a1316', .62) if p['kind'] == 'day' else ('#3a1316', .45),
 'whisper': lambda p: ('#f2eeea', .2) if p['kind'] == 'day' else (p['bg'], .16),
}
def lozenge(cx, cy, hw, hh): return f'M{F(cx)},{F(cy - hh)} L{F(cx + hw)},{F(cy)} L{F(cx)},{F(cy + hh)} L{F(cx - hw)},{F(cy)} Z '
def flower(cx, cy, r):
    """A four-petal centre in the spirit of ลายประจำยาม: four pointed petals on the axes."""
    k = r * .34; d = ''
    for a in (0, 90, 180, 270):
        ca, sa = math.cos(math.radians(a)), math.sin(math.radians(a))
        tip = (cx + r * ca, cy + r * sa); l = (cx - k * sa, cy + k * ca); rr = (cx + k * sa, cy - k * ca)
        d += f'M{F(cx)},{F(cy)} Q{F(l[0] + r * .55 * ca)},{F(l[1] + r * .55 * sa)} {F(tip[0])},{F(tip[1])} Q{F(rr[0] + r * .55 * ca)},{F(rr[1] + r * .55 * sa)} {F(cx)},{F(cy)} Z '
    return d

def nested(colour='gold', s=40, ratio=1.4, levels=(.92, .58, .26), width=1.0, centre=None, target='both', tag=''):
    def build(p):
        c, o = LINE[colour](p)
        h = s * ratio; d = ''; fills = ''
        for j in range(-1, int(HH / (h / 2)) + 3):
            for i in range(-1, int(W / s) + 2):
                cx = i * s + (s / 2 if j % 2 else 0); cy = j * h / 2
                for k in levels: d += lozenge(cx, cy, s / 2 * k, h / 2 * k)
                if centre == 'gem': fills += lozenge(cx, cy, s / 2 * .12, h / 2 * .12)
                if centre == 'flower': fills += flower(cx, cy, min(s, h) * .17)
        u = p['bg'][1:] + tag
        art = f'<path d="{d}" style="fill: none; stroke: {c}; stroke-opacity: {o}; stroke-width: {width}; stroke-linejoin: miter"></path>'
        if fills: art += f'<path d="{fills}" style="fill: {c}; fill-opacity: {o}"></path>'
        s_ = (f'<clipPath id="x{u}"><path d="{DP} {AP}" style="clip-rule: evenodd"></path></clipPath>'
              f'<clipPath id="d{u}"><path d="{DP}"></path></clipPath>')
        s_ += f'<path d="{DP} {AP}" style="fill: {p["ink"]}; fill-rule: evenodd"></path>'
        inner = art if target == 'both' else f'<g clip-path="url(#d{u})">{art}</g>'
        return s_ + f'<g clip-path="url(#x{u})">{inner}</g>' + name_d(p, 176, 254, 312)
    return build

V = [
 ('115', 'Colour · light gold on red',            nested('gold', tag='g')),
 ('116', 'Colour · soft rose',                     nested('rose', tag='r')),
 ('117', 'Colour · deep, tone on tone',            nested('deep', tag='dp')),
 ('118', 'Colour · whisper',                       nested('whisper', tag='w')),
 ('119', 'Gold · smaller pattern',                 nested('gold', s=26, width=.8, tag='sm')),
 ('120', 'Gold · larger pattern',                  nested('gold', s=62, width=1.2, tag='lg')),
 ('121', 'Gold · four rings and a gem at the centre', nested('gold', levels=(.94, .7, .46, .22), centre='gem', tag='gm')),
 ('122', 'Gold · ประจำยาม flower at the centre',    nested('gold', s=44, levels=(.94, .62), centre='flower', tag='fl')),
 ('123', 'Gold · D only (D for Diamond)',          nested('gold', target='D', tag='do')),
 ('124', 'Gold · taller lozenges, finer line',     nested('gold', s=34, ratio=1.75, width=.75, tag='tl')),
]
VB = '0 -6 362 280'
CONCEPTS = [(f'Concept{n}', f'{n} · {t}', VB, fn) for n, t, fn in V]
