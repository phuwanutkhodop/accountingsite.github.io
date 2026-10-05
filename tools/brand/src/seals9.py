"""Seal round 9: deeper on 244 / 270 / 271, with diamonds alternating with flowers."""
import math
from seals8 import *
from marks6 import gw

def dia(x, y, s, c, kind='solid', bg=None, ang=0):
    """A small diamond: solid, line (double, like the 153 rings) or gem (solid with a paper inner line)."""
    hw, hh = s * .62, s
    o = f'M0,{-hh} L{hw},0 L0,{hh} L{-hw},0 Z'; n = f'M0,{-hh * .55} L{hw * .55},0 L0,{hh * .55} L{-hw * .55},0 Z'
    g = f'<g transform="translate({F(x)},{F(y)}) rotate({F(ang)})">'
    if kind == 'solid': return g + f'<path d="{o}" style="fill: {c}"></path></g>'
    if kind == 'line':  return g + f'<path d="{o} {n}" style="fill: none; stroke: {c}; stroke-width: .9"></path></g>'
    return g + f'<path d="{o}" style="fill: {c}"></path><path d="{n}" style="fill: none; stroke: {bg}; stroke-width: .7"></path></g>'
def alt_ring(r, n, fsize, dsize, fc, dc, kind='solid', bg=None, start=0, graded=False, skip=None):
    out = ''
    for k in range(n):
        a = start + 2 * math.pi * k / n
        if skip and skip(a): continue
        g = 1.0
        if graded: g = .7 + .5 * (math.sin(a) + 1) / 2          # larger toward the foot
        x, y = C + r * math.cos(a), C + r * math.sin(a)
        out += flower(x, y, fsize * g, fc) if k % 2 == 0 else dia(x, y, dsize * g, dc, kind, bg)
    return out
def alt_arc(r, n, span, fsize, dsize, fc, dc, centre=90, kind='solid', bg=None, graded=False, ang=True):
    out = ''
    for k in range(n):
        t = k / (n - 1) - .5; a = math.radians(centre - t * span)
        g = (1 - .45 * abs(t) * 2) if graded else 1
        x, y = C + r * math.cos(a), C + r * math.sin(a)
        out += flower(x, y, fsize * g, fc) if k % 2 == 0 else dia(x, y, dsize * g, dc, kind, bg, math.degrees(a) + 90 if ang else 0)
    return out
top_gap = lambda half: (lambda a: abs(((math.degrees(a) + 90 + 180) % 360) - 180) < half)   # True near 12 o'clock

# ---- 1. alternating border ----
def j272(p): i, r = p['ink'], FLAT[p['bg']][0]; return alt_ring(136, 48, 5.6, 5, i, r) + name(i) + da(p)
def j273(p): i, r = p['ink'], FLAT[p['bg']][0]; return alt_ring(136, 44, 6, 5.4, i, r, graded=True) + name(i) + da(p)
def j274(p): i, r = p['ink'], FLAT[p['bg']][0]; return flower_ring(138, 36, 5.6, i) + ''.join(dia(C + 126 * math.cos(a), C + 126 * math.sin(a), 3.6, r, ang=math.degrees(a) + 90) for a in [2 * math.pi * (k + .5) / 36 for k in range(36)]) + arc_text(NAME, 12.5, C, C, 106, 'top', track=.14, fill=i) + da(p, w=126)
def j275(p): i, r = p['ink'], FLAT[p['bg']][0]; return alt_ring(136, 48, 5.6, 5, i, i, 'gem', p['bg']) + arc_text(NAME, 12.5, C, C, 108, 'top', track=.14, fill=i) + flower_ring(88, 28, 3.4, r) + da(p, w=112)
def j276(p): i, bg = p['ink'], p['bg']; r, sv = FLAT[bg]; return alt_ring(136, 40, 6, 6, i, i, 'gem', bg, start=math.pi / 40) + name(i) + da(p)
def j277(p):   # a chain: diamond and flower touching, all round
    i, r = p['ink'], FLAT[p['bg']][0]
    return ring(C, C, 136, r, .6) + alt_ring(136, 56, 4.8, 4.4, i, i, 'line') + name(i) + da(p)

# ---- 2. from 244 ----
def j278(p): i, r = p['ink'], FLAT[p['bg']][0]; return ''.join(flower(C + 136 * math.cos(a), C + 136 * math.sin(a), 6.5 if k % 2 == 0 else 3.6, i if k % 2 == 0 else r) for k, a in enumerate([2 * math.pi * k / 48 for k in range(48)])) + name(i) + da(p)
def j279(p): i, r = p['ink'], FLAT[p['bg']][0]; return ''.join(flower(C + 137 * math.cos(a), C + 137 * math.sin(a), 5, i if k % 2 == 0 else r) for k, a in enumerate([2 * math.pi * k / 56 for k in range(56)])) + name(i) + da(p)
def j280(p):
    i, r = p['ink'], FLAT[p['bg']][0]
    return ''.join(flower(C + 136 * math.cos(a), C + 136 * math.sin(a), 5.5, i) for a in [2 * math.pi * k / 44 for k in range(44)] if abs(math.degrees(a) - 90) > 10) + flower(C, C + 136, 11, i) + name(i) + bottom_flowers(112, 3, 6, r, span=20) + da(p)
def j281(p):   # flowers only where the name is not; the name closes the circle
    i, r = p['ink'], FLAT[p['bg']][0]
    return ''.join(flower(C + 136 * math.cos(a), C + 136 * math.sin(a), 6, i) for a in [math.radians(-28 + 236 * k / 26) for k in range(27)]) + arc_text(NAME, 13.5, C, C, 132, 'top', track=.14, fill=i) + da(p, w=146)

# ---- 3. from 270 ----
def wreath(p, n=9, items='flower', top=None, inner=False):
    i, r = p['ink'], FLAT[p['bg']][0]; s = ''
    for side in (-1, 1):
        for k in range(n):
            a = math.radians(90 + side * (22 + (138 / n) * k)); sz = 7.5 - (3.5 / n) * k
            x, y = C + 126 * math.cos(a), C + 126 * math.sin(a)
            if items == 'alt': s += flower(x, y, sz, i) if k % 2 == 0 else dia(x, y, sz * 1.15, i, 'gem', p['bg'], ang=math.degrees(a) + 90)
            else: s += flower(x, y, sz, i if k % 2 == 0 else r)
            if inner and k % 2 == 1: s += dia(C + 112 * math.cos(a), C + 112 * math.sin(a), 3.4, r, ang=math.degrees(a) + 90)
    s += flower(C, C + 128, 10, i)
    if top: s += top
    return s
def j282(p): i = p['ink']; return wreath(p, items='alt') + da(p, w=150, y=-8) + straight_name(i, C + 74, 9.6)
def j283(p): i = p['ink']; return wreath(p, n=11, items='alt', top=dia(C, C - 128, 7, i, 'gem', p['bg'])) + da(p, w=150, y=-6) + straight_name(i, C + 76, 9.6)
def j284(p): i = p['ink']; return wreath(p, n=7, items='alt') + arc_text(NAME, 12, C, C, 112, 'top', track=.14, fill=i) + da(p, w=130)
def j285(p): i = p['ink']; return wreath(p, items='flower', inner=True) + da(p, w=150, y=-8) + straight_name(i, C + 74, 9.6)

# ---- 4. from 271 ----
def j286(p): i, r = p['ink'], FLAT[p['bg']][0]; return pair(i) + name(i) + alt_ring(90, 32, 3.8, 3.4, r, i) + da(p, w=118)
def j287(p): i, r = p['ink'], FLAT[p['bg']][0]; return alt_ring(136, 48, 5.6, 5, i, r) + arc_text(NAME, 12.5, C, C, 110, 'top', track=.14, fill=i) + flower_ring(88, 28, 3.6, r) + da(p, w=112)
def j288(p): i, r = p['ink'], FLAT[p['bg']][0]; return flower_ring(137, 44, 5.4, i) + arc_text(NAME, 12.5, C, C, 110, 'top', track=.14, fill=i) + alt_ring(88, 28, 3.6, 3.2, r, i) + da(p, w=112)
def j289(p): i, r = p['ink'], FLAT[p['bg']][0]; return pair(i) + name(i) + ''.join(dia(C + 90 * math.cos(a), C + 90 * math.sin(a), 3.4, r, ang=math.degrees(a) + 90) for a in [2 * math.pi * k / 30 for k in range(30)]) + bottom_flowers(114, 3, 6.5, i, span=20, graded=True) + da(p, w=118)

# ---- 5. alternation used beyond the border ----
def arc_tokens(tokens, size, r, fill, gapf=.6):
    """Lay words and marks along the top arc: tokens are strings or ('f'|'d', s)."""
    def w(t): return (sum(gw(TXT, c, size) if c != ' ' else size * .3 for c in t) + .14 * size * (len(t) - 1)) if isinstance(t, str) else t[1] * 2.2
    widths = [w(t) for t in tokens]; gap = size * gapf
    total = sum(widths) + gap * (len(tokens) - 1); a = -math.pi / 2 - total / 2 / r; out = ''
    for t, wd in zip(tokens, widths):
        mid = a + wd / 2 / r
        if isinstance(t, str):
            out += f'<g transform="rotate({F(math.degrees(mid + math.pi / 2))} {C} {C})">' + arc_text(t, size, C, C, r, 'top', track=.14, fill=fill) + '</g>'
        else:
            x, y = C + (r + size * .35) * math.cos(mid), C + (r + size * .35) * math.sin(mid)
            out += flower(x, y, t[1], fill) if t[0] == 'f' else dia(x, y, t[1], fill, ang=math.degrees(mid) + 90)
        a += (wd + gap) / r
    return out
def j290(p):   # the name's words separated by a diamond, a flower, a diamond
    i = p['ink']
    toks = ['D.A.', ('d', 4.6), 'ACCOUNTING', ('f', 5), '&', ('f', 5), 'CONSULTING']
    return pair(i) + arc_tokens(toks, 12.5, 115, i, gapf=.32) + alt_arc(112, 5, 40, 7, 5.5, i, FLAT[p['bg']][0], graded=True) + da(p)
def j291(p):   # a short ribbon of alternating diamonds and flowers under the monogram
    i, r = p['ink'], FLAT[p['bg']][0]
    s = pair(i) + name(i) + da(p, y=-10)
    for k, dx in enumerate(range(-60, 61, 15)):
        s += flower(C + dx, C + 54, 4.8 if dx == 0 else 3.6, i) if k % 2 == 0 else dia(C + dx, C + 54, 3.6, r)
    return s + flower(C, C + 116, 8, i)
def j292(p):   # diamonds at north and south, flowers at east and west
    i, r = p['ink'], FLAT[p['bg']][0]
    return pair(i) + arc_text(NAME, 13, C, C, 110, 'top', track=.14, fill=i) + dia(C, C + 114, 10, i, 'gem', p['bg']) + flower(C - 114, C, 8, r) + flower(C + 114, C, 8, r) + da(p, w=130)
def j293(p):   # sixteen short rays, each ending in a diamond or a flower
    i, r = p['ink'], FLAT[p['bg']][0]; s = pair(i)
    for k in range(16):
        a = 2 * math.pi * k / 16 + math.pi / 16
        if -math.pi / 2 - .9 < a - 2 * math.pi < -math.pi / 2 + .9 or -math.pi / 2 - .9 < a < -math.pi / 2 + .9: continue
        x, y = C + 118 * math.cos(a), C + 118 * math.sin(a)
        s += f'<line x1="{F(C + 100 * math.cos(a))}" y1="{F(C + 100 * math.sin(a))}" x2="{F(C + 112 * math.cos(a))}" y2="{F(C + 112 * math.sin(a))}" style="stroke: {r}; stroke-width: .8"></line>'
        s += flower(x, y, 4.6, i) if k % 2 == 0 else dia(x, y, 4.2, i, ang=math.degrees(a) + 90)
    return s + name(i) + da(p, w=126)
def j294(p):   # layers that alternate: flowers outside, diamonds between, flowers inside
    i, r = p['ink'], FLAT[p['bg']][0]
    return flower_ring(138, 40, 5, i) + ''.join(dia(C + 126 * math.cos(a), C + 126 * math.sin(a), 3.4, r, ang=math.degrees(a) + 90) for a in [2 * math.pi * (k + .5) / 40 for k in range(40)]) + arc_text(NAME, 12, C, C, 104, 'top', track=.14, fill=i) + flower_ring(86, 26, 3.2, r) + da(p, w=110)
def j295(p):   # only the lower half carries the alternation; the name holds the top
    i, r = p['ink'], FLAT[p['bg']][0]
    return pair(i) + name(i) + alt_arc(122, 15, 150, 6, 5, i, r, graded=True) + da(p)

V = [
 ('272', 'Alternating border', j272), ('273', 'Alternating, larger toward the foot', j273),
 ('274', 'Two rows: flowers outside, diamonds inside', j274), ('275', 'Gem-and-flower border + inner flower ring', j275),
 ('276', 'Alternating gems and flowers', j276), ('277', 'A chain of diamond and flower', j277),
 ('278', '244 · large and small flowers alternate', j278), ('279', '244 · two-tone flowers', j279),
 ('280', '244 · flower circle, one large flower at the foot', j280), ('281', '244 · flowers close under the name', j281),
 ('282', '270 · wreath of flowers and diamonds', j282), ('283', '270 · fuller wreath, a gem at the top', j283),
 ('284', '270 · wreath with the name above', j284), ('285', '270 · wreath with an inner row of diamonds', j285),
 ('286', '271 · inner ring alternates', j286), ('287', '271 · alternating border + inner flowers', j287),
 ('288', '271 · flower border + alternating inner ring', j288), ('289', '271 · inner ring of tiny diamonds', j289),
 ('290', 'Diamond and flowers between the words', j290), ('291', 'A ribbon of diamonds and flowers', j291),
 ('292', 'Diamonds north and south, flowers east and west', j292), ('293', 'Rays ending in diamonds and flowers', j293),
 ('294', 'Alternating layers', j294), ('295', 'Alternation along the lower half', j295),
]
CONCEPTS = [(f'Concept{n}', f'{n} · {t}', '0 0 300 300', fn) for n, t, fn in V]
