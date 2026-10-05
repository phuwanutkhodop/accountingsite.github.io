import os
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
FD = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'fonts', '')     # tools/brand/fonts/
_F = {}
def font(n):
    if n not in _F:
        f = TTFont(FD + n); _F[n] = (f.getGlyphSet(), f.getBestCmap(), f['head'].unitsPerEm)
    return _F[n]
def gd(fn, ch, size, x, base):
    gs, cm, upm = font(fn); s = size / upm
    sp = SVGPathPen(gs, lambda v: f"{v:.1f}")
    gs[cm[ord(ch)]].draw(TransformPen(sp, (s, 0, 0, -s, x, base)))
    return sp.getCommands()
def gw(fn, ch, size):
    gs, cm, upm = font(fn); return gs[cm[ord(ch)]].width * size / upm
def gb(fn, ch, size):
    gs, cm, upm = font(fn); bp = BoundsPen(gs); gs[cm[ord(ch)]].draw(bp); return [v * size / upm for v in bp.bounds]
def text(fn, t, size, cx, base, track=0.0):
    ws = [gw(fn, c, size) if c != ' ' else size * .28 for c in t]
    total = sum(ws) + track * size * (len(t) - 1); x = cx - total / 2; out = []
    for c, w in zip(t, ws):
        if c != ' ': out.append(gd(fn, c, size, x, base))
        x += w + track * size
    return ' '.join(out)

PAL = {
 'mk':  dict(bg='#f2eeea', ink='#7a2229'),
 'mkL': dict(bg='#7a2229', ink='#f6efe8'),
 'mkN': dict(bg='#1b1112', ink='#efe6dc'),
}
B, BI, C = 'BM700.ttf', 'BM700i.ttf', 'CG700.ttf'
def fill(d, p, halo=0, rule=''):
    st = f'fill: {p["ink"]}'
    if rule: st += f'; fill-rule: {rule}'
    if halo: st += f'; stroke: {p["bg"]}; stroke-width: {halo}; paint-order: stroke; stroke-linejoin: round'
    return f'<path d="{d}" style="{st}"></path>'
def name(p, cx, base, maxw=280):
    t = "D.A. ACCOUNTING & CONSULTING"
    w1 = sum(gw("CG600.ttf", c, 1) if c != ' ' else .28 for c in t) + .2 * (len(t) - 1)
    return f'<path d="{text("CG600.ttf", t, min(17, maxw / w1), cx, base, .2)}" style="fill: {p["ink"]}"></path>'
def uid(p): return p['bg'][1:]

# 41 Interlock — D and A woven: A passes over D at the top, under it at the foot
def interlock(fn):
    def build(p):
        D, A = gd(fn, 'D', 260, 20, 230), gd(fn, 'A', 260, 120, 230)
        cid = f'lo{fn[:3]}{uid(p)}'
        s = f'<clipPath id="{cid}"><rect x="0" y="168" width="400" height="80"></rect></clipPath>'
        s += fill(D, p) + fill(A, p, 9)
        s += f'<g clip-path="url(#{cid})">' + fill(D, p, 9) + '</g>'
        return s + name(p, 170, 296)
    return build

# 42 Offset — LV logic: the A set lower and to the right, laid over the D
def offset(p):
    s = fill(gd(B, 'D', 250, 20, 200), p) + fill(gd(B, 'A', 250, 128, 238), p, 9)
    return s + name(p, 168, 296)

# 43 Mirror — the A and its reflection meet at the baseline and make a diamond
def mirror(p):
    A = gd(B, 'A', 200, 0, 0)
    s = f'<g transform="translate(97,150)">' + fill(A, p) + '</g>'
    s += f'<g transform="translate(97,150) scale(1,-1)">' + fill(A, p) + '</g>'
    s += f'<rect x="80" y="148" width="200" height="4" style="fill: {p["bg"]}"></rect>'
    return s + name(p, 175, 344)

# 44 Ledger lines — NB logic: bold italic D A cut by ruled lines, as on ledger paper
def ledger(p):
    s = fill(gd(BI, 'D', 250, 20, 220), p) + fill(gd(BI, 'A', 250, 160, 220), p)
    for y in (70, 100, 130, 160, 190):
        s += f'<rect x="0" y="{y}" width="{150 - (y - 70) * 0.45}" height="7" style="fill: {p["bg"]}"></rect>'
    return s + name(p, 190, 280)

# 45 Overlap window — where the A crosses the D the overlap opens as a window
def xor(p):
    d = gd(B, 'D', 260, 20, 230) + ' ' + gd(B, 'A', 260, 112, 230)
    return fill(d, p, rule='evenodd') + name(p, 168, 296)

# 46 Stacked — D above, the A rising into it from below
def stacked(p):
    s = fill(gd(B, 'D', 200, 85, 170), p) + fill(gd(B, 'A', 200, 80, 270), p, 8)
    return s + name(p, 160, 330)

CONCEPTS = [
 ('Concept41', '41 · Interlock (Bodoni)',    '0 20 340 300', interlock(B)),
 ('Concept42', '42 · Offset',                '0 20 340 300', offset),
 ('Concept43', '43 · Mirror diamond',        '20 20 310 340', mirror),
 ('Concept44', '44 · Ledger lines',          '0 20 380 280', ledger),
 ('Concept45', '45 · Overlap window',        '0 20 340 300', xor),
 ('Concept47', '47 · Interlock (Cormorant)', '0 20 340 300', interlock(C)),
]
