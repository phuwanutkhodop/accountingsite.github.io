"""Seal round 10: deeper on 295 (name above, diamonds alternating with flowers along the lower half).
Owner's test: an inner circle filled with the 153 pattern on red (as inside the D A), and its reverse."""
import math
from seals9 import *

def base(p, span=150, n=15, r=122, fs=6, ds=5, graded=True, fc=None, dc=None, kind='solid', pair_on=True):
    i, rr = p['ink'], FLAT[p['bg']][0]
    s = (pair(i) if pair_on else '') + name(i)
    return s + alt_arc(r, n, span, fs, ds, fc or i, dc or rr, kind=kind, bg=p['bg'], graded=graded)
def inner_red(p, r=88, edge=True, tag='ir'):
    """The 153 interior as a disc: letter colour, rose diamonds, silver flowers. D A sits on it reversed, full detail."""
    s = lattice(C, C, r, p, s=18, tag=tag)
    if edge: s += ring(C, C, r, p['ink'], 1.2) + ring(C, C, r + 5, FLAT[p['bg']][0], .7)
    return s
def inner_reversed(p, r=88, tag='iv'):
    """The reverse: a paper disc, the lattice drawn in the letter colour, the flowers in rose."""
    i, bg = p['ink'], p['bg']; rc = FLAT[bg][0]
    h = 18 * 1.4; d = ''; fl = ''; n = int(r / 18) + 3
    for j in range(-2 * n, 2 * n + 1):
        for k in range(-n, n + 1):
            x = C + k * 18 + (9 if j % 2 else 0); y = C + j * h / 2
            for q in (.94, .62): d += f'M{F(x)},{F(y - h / 2 * q)} L{F(x + 9 * q)},{F(y)} L{F(x)},{F(y + h / 2 * q)} L{F(x - 9 * q)},{F(y)} Z '
            fl += petals(x, y, 18 * .17) + petals(x, y, 18 * .17 * .52, rot=45, width=.4)
    body = f'<path d="{d}" style="fill: none; stroke: {i}; stroke-width: .6; stroke-opacity: .5"></path><path d="{fl}" style="fill: {rc}"></path>'
    return clip_circle(r, body, tag, p) + ring(C, C, r, i, 1.2) + ring(C, C, r + 5, rc, .7)

def k296(p): return base(p) + inner_red(p, 88) + da_on_ink(p, w=128)
def k297(p): return base(p) + inner_reversed(p, 88) + da(p, w=128)
def k298(p): return base(p, r=126, fs=5.5, ds=4.6) + inner_red(p, 100, tag='ir2') + da_on_ink(p, w=144)
def k299(p):   # red inner disc with a flower clasp at its top edge
    i = p['ink']; return base(p) + inner_red(p, 88, tag='ir3') + disc(C, C - 93, 8, p['bg']) + flower(C, C - 93, 7, i) + da_on_ink(p, w=128)
def k300(p): return base(p, span=120, n=11) + da(p)
def k301(p): return base(p, span=180, n=17) + da(p)
def k302(p): return base(p, span=232, n=23, fs=5.4, ds=4.6) + da(p)
def k303(p): return base(p, graded=False, fs=5.4, ds=4.6) + da(p)
def k304(p):   # one large flower at the foot, graded either side
    i = p['ink']; return base(p) + disc(C, C + 122, 11, p['bg']) + flower(C, C + 122, 11, i) + da(p)
def k305(p): i, r = p['ink'], FLAT[p['bg']][0]; return base(p, fc=r, dc=i) + da(p)
def k306(p): i = p['ink']; return base(p, dc=i, kind='gem') + da(p)
def k307(p): i = p['ink']; return base(p, dc=i, kind='line') + da(p)
def k308(p):   # two rows: flowers on the outer arc, diamonds offset on the inner
    i, r = p['ink'], FLAT[p['bg']][0]
    s = pair(i) + name(i)
    s += ''.join(flower(C + 124 * math.cos(math.radians(90 - (k / 8 - .5) * 150)), C + 124 * math.sin(math.radians(90 - (k / 8 - .5) * 150)), 5.6 * (1 - .45 * abs(k / 8 - .5) * 2), i) for k in range(9))
    s += ''.join(dia(C + 111 * math.cos(math.radians(90 - (k / 7 - .5) * 131)), C + 111 * math.sin(math.radians(90 - (k / 7 - .5) * 131)), 4.6 * (1 - .4 * abs(k / 7 - .5) * 2), r, ang=90 - (k / 7 - .5) * 131 + 90) for k in range(8))
    return s + da(p)
def k309(p): return base(p, r=100, span=120, n=13, fs=4.6, ds=4) + da(p, y=-8, w=128)
def k310(p): return base(p, n=21, fs=4.6, ds=4) + da(p)
def k311(p): return base(p, n=9, fs=8, ds=7) + da(p)
def k312(p):   # the alternation sits on the edge of the red inner disc
    i, bg = p['ink'], p['bg']; r = FLAT[bg][0]
    s = pair(i) + name(i) + inner_red(p, 92, edge=False, tag='ir4') + ring(C, C, 92, i, 1.2) + ring(C, C, 96, r, .7)
    for k in range(15):
        t = k / 14 - .5; a = math.radians(90 - t * 150); g = 1 - .45 * abs(t) * 2
        x, y = C + 104 * math.cos(a), C + 104 * math.sin(a)
        s += flower(x, y, 6 * g, i) if k % 2 == 0 else dia(x, y, 5 * g, r, ang=math.degrees(a) + 90)
    return s + da_on_ink(p, w=132)
def k313(p): i, r = p['ink'], FLAT[p['bg']][0]; return base(p, fc=r, dc=i) + inner_reversed(p, 88, tag='iv2') + da(p, w=128)
def k314(p):   # a thin band of the red pattern under the arc, the centre clear
    i = p['ink']
    return base(p, r=124, fs=5.4, ds=4.6) + band(p, 92, 104, lattice(C, C, 104, p, s=10, tag='k314'), 'k314') + ring(C, C, 104, i, 1) + ring(C, C, 92, i, 1) + da(p, w=128)
def k315(p):   # the name split by a flower clasp, the alternation below
    i, r = p['ink'], FLAT[p['bg']][0]
    return pair(i) + split_name(i, r=114, size=13.5) + flower(C, C - 118, 8, i) + alt_arc(122, 15, 150, 6, 5, i, r, graded=True) + da(p)

V = [
 ('296', 'Inner circle in the red pattern, D A reversed', k296),
 ('297', 'Inner circle reversed: cream with the pattern in red', k297),
 ('298', 'Larger red inner circle', k298),
 ('299', 'Red inner circle with a flower clasp', k299),
 ('300', 'Arc narrower (120°)', k300),
 ('301', 'Arc wider (180°)', k301),
 ('302', 'Arc rising to the name (232°)', k302),
 ('303', 'Even sizes, not graded', k303),
 ('304', 'One large flower at the foot', k304),
 ('305', 'Colours swapped: rose flowers, red diamonds', k305),
 ('306', 'Gem diamonds', k306),
 ('307', 'Outline diamonds', k307),
 ('308', 'Two rows: flowers outside, diamonds inside', k308),
 ('309', 'Arc close under D A', k309),
 ('310', 'Denser: 21 pieces', k310),
 ('311', 'Sparser: 9 larger pieces', k311),
 ('312', 'Alternation on the edge of the red circle', k312),
 ('313', 'Reversed inner circle + swapped colours', k313),
 ('314', 'Thin band of red pattern under the arc', k314),
 ('315', 'Flower clasp splitting the name', k315),
]
CONCEPTS = [(f'Concept{n}', f'{n} · {t}', '0 0 300 300', fn) for n, t, fn in V]
