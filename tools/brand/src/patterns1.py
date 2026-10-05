"""Brand pattern round 1 (401-420). Each pattern is one SVG tile repeated with <pattern>, so files stay light.
Colours come only from the locked palette (logo 153 / seal 346)."""
import math
from seals import petals, F, mono_patterned, PAL, FLAT
COLS = {k: dict(key=k, bg=p['bg'], ink=p['ink'], rose=FLAT[p['bg']][0], silver=FLAT[p['bg']][1], p=p) for k, p in PAL.items()}

def fl(x, y, r, c):            # the 153 eight-point flower
    return f'<path d="{petals(x, y, r) + petals(x, y, r * .52, rot=45, width=.4)}" style="fill: {c}"></path>'
def loz(x, y, hw, hh):         # a lozenge path
    return f'M{F(x)},{F(y - hh)} L{F(x + hw)},{F(y)} L{F(x)},{F(y + hh)} L{F(x - hw)},{F(y)} Z '
def st(d, c, w): return f'<path d="{d}" style="fill: none; stroke: {c}; stroke-width: {w}; stroke-linejoin: miter"></path>'
def fill(d, c): return f'<path d="{d}" style="fill: {c}"></path>'
def stag(w, h, centre, corner=None):
    """Half-drop: one motif at the tile centre, its neighbours at the four corners (seamless)."""
    corner = corner or centre
    return centre(w / 2, h / 2) + ''.join(corner(x, y) for x in (0, w) for y in (0, h))
def edges(w, h, f):            # the four edge midpoints (between staggered motifs)
    return ''.join(f(x, y) for x, y in ((w / 2, 0), (w / 2, h), (0, h / 2), (w, h / 2)))
def da_use(c, x, y): return f'<use href="#da{c["key"]}" x="{F(x)}" y="{F(y)}"></use>'

# ---- A. from the 153 lattice ----
def lattice(s, ground, ring, flower, levels=(.94, .62), sw=.8, fr=.17, ratio=1.4):
    def t(c):
        w, h = s, s * ratio
        m = lambda x, y: st(''.join(loz(x, y, w / 2 * q, h / 2 * q) for q in levels), c[ring], sw) + (fl(x, y, s * fr, c[flower]) if flower else '')
        return w, h, c[ground], stag(w, h, m)
    return t
t401 = lattice(36, 'ink', 'rose', 'silver')
t402 = lattice(36, 'bg', 'ink', 'rose', sw=.7)
t403 = lattice(64, 'bg', 'ink', 'rose', sw=.9)
t404 = lattice(16, 'ink', 'rose', 'silver', sw=.5)
t405 = lattice(36, 'bg', 'rose', None, sw=.8)
def t406(c):                   # flowers only, on the lattice points; tiny diamonds where the lozenges would touch
    s = 36; w, h = s, s * 1.4
    m = lambda x, y: fl(x, y, s * .2, c['ink'])
    tiny = ''.join(fill(loz(x, y, 1.6, 2.4), c['rose']) for x, y in ((w / 4, h / 4), (3 * w / 4, h / 4), (w / 4, 3 * h / 4), (3 * w / 4, 3 * h / 4)))
    return w, h, c['bg'], stag(w, h, m) + tiny
def t407(c):                   # alternate tiles solid: a solid diamond with a pale flower, then an open one
    s = 40; w, h = s, s * 1.4
    solid = lambda x, y: fill(loz(x, y, w / 2 * .94, h / 2 * .94), c['ink']) + st(loz(x, y, w / 2 * .62, h / 2 * .62), c['rose'], .7) + fl(x, y, s * .17, c['silver'])
    open_ = lambda x, y: st(loz(x, y, w / 2 * .94, h / 2 * .94) + loz(x, y, w / 2 * .62, h / 2 * .62), c['ink'], .7) + fl(x, y, s * .17, c['rose'])
    return w, h, c['bg'], stag(w, h, solid, open_)
t408 = lattice(30, 'bg', 'ink', 'ink', levels=(.94,), sw=.6, fr=.2, ratio=1.8)

# ---- B. new patterns from the same motifs ----
def t409(c):                   # flower and diamond alternating, as on the seal's arc
    w, h = 24, 24
    return w, h, c['bg'], stag(w, h, lambda x, y: fill(loz(x, y, 2.8, 4.4), c['rose']), lambda x, y: fl(x, y, 5, c['ink']))
def t410(c):                   # a trellis: touching diamonds drawn as lines, flowers where they cross
    s = 40; w, h = s, s * 1.4
    lines = st(loz(w / 2, h / 2, w / 2, h / 2) + ''.join(loz(x, y, w / 2, h / 2) for x in (0, w) for y in (0, h)), c['ink'], .6)
    return w, h, c['bg'], lines + edges(w, h, lambda x, y: fl(x, y, 4.6, c['ink'])) + stag(w, h, lambda x, y: fill(loz(x, y, 2, 3), c['rose']))
def t411(c):                   # rows of the alternation, like ruled lines
    w, h = 28, 34
    row = fl(0, 8, 4, c['ink']) + fl(w, 8, 4, c['ink']) + fill(loz(w / 2, 8, 2.2, 3.4), c['rose'])
    return w, h, c['bg'], row
def t412(c):                   # medallions: a flower in a ring, half-drop, small diamonds between
    s = 58; w, h = s, s
    med = lambda x, y: f'<circle cx="{F(x)}" cy="{F(y)}" r="{F(s * .3)}" style="fill: none; stroke: {c["ink"]}; stroke-width: .8"></circle>' + fl(x, y, s * .2, c['ink'])
    return w, h, c['bg'], stag(w, h, med) + edges(w, h, lambda x, y: fill(loz(x, y, 2.4, 3.8), c['rose']))
def t413(c):                   # large nested diamonds: four rings
    s = 64; w, h = s, s * 1.4
    m = lambda x, y: st(loz(x, y, w / 2 * .96, h / 2 * .96) + loz(x, y, w / 2 * .78, h / 2 * .78), c['ink'], .7) + st(loz(x, y, w / 2 * .6, h / 2 * .6) + loz(x, y, w / 2 * .42, h / 2 * .42), c['rose'], .7) + fl(x, y, s * .1, c['ink'])
    return w, h, c['bg'], stag(w, h, m)
def gem(x, y, hw, hh, c):      # a cut stone seen from above: outline, table, facet lines
    o = loz(x, y, hw, hh); t = loz(x, y, hw * .45, hh * .45)
    fac = ''.join(f'M{F(x + a * hw)},{F(y + b * hh)} L{F(x + a * hw * .45)},{F(y + b * hh * .45)} ' for a, b in ((1, 0), (-1, 0), (0, 1), (0, -1)))
    return fill(o, c['rose']) + st(t, c['bg'], .6) + st(fac, c['bg'], .5)
def t414(c):
    s = 40; w, h = s, s * 1.4
    return w, h, c['bg'], stag(w, h, lambda x, y: gem(x, y, 8, 12, c), lambda x, y: fl(x, y, 6, c['ink']))
def t415(c):                   # ledger: ruled lines, double column rules, a flower where they meet
    w, h = 96, 72
    rules = ''.join(f'M0,{F(y)} L{w},{F(y)} ' for y in range(0, 73, 12))
    cols = f'M{F(w / 2 - 1.6)},0 L{F(w / 2 - 1.6)},{h} M{F(w / 2 + 1.6)},0 L{F(w / 2 + 1.6)},{h} '
    return w, h, c['bg'], st(rules, c['rose'], .5) + st(cols, c['ink'], .6) + fl(w / 2, h / 2, 5.5, c['ink']) + fl(w / 2, 0, 5.5, c['ink']) + fl(w / 2, h, 5.5, c['ink'])
def t416(c):                   # ruled lines carrying small diamonds, half-drop
    w, h = 36, 32
    rules = ''.join(f'M0,{F(y)} L{w},{F(y)} ' for y in (0, h / 2, h))
    return w, h, c['bg'], st(rules, c['rose'], .5) + stag(w, h, lambda x, y: fill(loz(x, y, 2.6, 4.2), c['ink']))

# ---- C. with D A (always the full 153 monogram) ----
def t417(c):                   # monogram canvas: D A half-drop, flowers between
    w, h = 200, 150
    return w, h, c['bg'], stag(w, h, lambda x, y: da_use(c, x, y)) + edges(w, h, lambda x, y: fl(x, y, 9, c['rose']))
def t418(c):                   # a row of D A, then a row of the alternation
    w, h = 150, 120
    alt = ''.join((fl(x, 95, 4.6, c['ink']) if k % 2 == 0 else fill(loz(x, 95, 2.4, 3.8), c['rose'])) for k, x in enumerate(range(0, 151, 15)))
    return w, h, c['bg'], da_use(c, w / 2, 40) + alt
def t419(c):                   # the 153 lattice, with D A set into it on a plain lozenge
    s = 30; w, h = s * 8, s * 1.4 * 4
    m = lambda x, y: st(loz(x, y, s / 2 * .94, s * .7 * .94) + loz(x, y, s / 2 * .62, s * .7 * .62), c['ink'], .6) + fl(x, y, s * .17, c['rose'])
    body = ''.join(m(i * s + (s / 2 if j % 2 else 0), j * s * .7) for j in range(0, 9) for i in range(-1, 9))
    plate = fill(loz(w / 2, h / 2, 100, 72), c['bg']) + st(loz(w / 2, h / 2, 100, 72), c['ink'], .8)
    return w, h, c['bg'], body + plate + da_use(c, w / 2, h / 2)
def t420(c):                   # D A inside the two diamond rings (the 153 tile, with the monogram for the flower)
    w, h = 220, 180
    frame = lambda x, y: st(loz(x, y, 110, 90), c['ink'], .8) + st(loz(x, y, 100, 82), c['rose'], .6)
    return w, h, c['bg'], stag(w, h, lambda x, y: frame(x, y) + da_use(c, x, y), lambda x, y: frame(x, y) + da_use(c, x, y))

DA_W = {'417': 92, '418': 100, '419': 96, '420': 96}
V = [
 ('401', 'The 153 lattice as a fabric (as inside D A)', t401),
 ('402', '153 reversed: paper ground, red rings, rose flowers', t402),
 ('403', '153 reversed, large scale', t403),
 ('404', '153, fine scale (a texture)', t404),
 ('405', 'Rings only, rose (quiet)', t405),
 ('406', 'Flowers only, tiny diamonds between', t406),
 ('407', 'Solid and open diamonds, alternating', t407),
 ('408', 'One ring, tall diamonds, larger flower', t408),
 ('409', 'Flower and diamond alternating (from the seal)', t409),
 ('410', 'Trellis: flowers where the lines cross', t410),
 ('411', 'Rows of the alternation (ruled)', t411),
 ('412', 'Medallions: a flower in a ring', t412),
 ('413', 'Large nested diamonds', t413),
 ('414', 'Cut gems and flowers', t414),
 ('415', 'Ledger: ruled lines, column rules, flowers', t415),
 ('416', 'Ruled lines carrying diamonds', t416),
 ('417', 'D A monogram canvas', t417),
 ('418', 'D A rows with the alternation', t418),
 ('419', 'D A set into the 153 lattice', t419),
 ('420', 'D A inside the diamond rings', t420),
]
