"""Export the locked D.A. brand seal (346) as master SVGs. Geometry is identical to board 346 (seals13.o346);
the only difference is that the arc's centre flower, which the foot flower covers completely, is not drawn."""
import os, sys, math, json
from seals13 import *

OUT = os.path.join(os.environ.get('DA_BRAND_OUT') or sys.exit('Run tools/brand/build.py: the exporters never write into brand/ directly.'), 'seal', '')
RO = 141 + 3.2 / 2                     # outer edge of the thick ring = seal radius
ARC = dict(r=124, n=15, span=150, flower=5.4, diamond=4.6, shrink=.45)
BAND = dict(ri=86, ro=108, tile=24, fine_gap=2.6, fine_w=.5, edge_w=1, line_w=.6)
CLASP = dict(r=97, flower=10.5, disc=11.5)
FOOT = dict(r=124, flower=11, disc=11)
MONO_W, MONO_DY = 116, -4

def arc(p):
    i, rc = p['ink'], FLAT[p['bg']][0]; a_ = ARC; out = ''
    for k in range(a_['n']):
        if k == a_['n'] // 2: continue                   # under the foot flower
        t = k / (a_['n'] - 1) - .5; a = math.radians(90 - t * a_['span']); g = 1 - a_['shrink'] * abs(t) * 2
        x, y = C + a_['r'] * math.cos(a), C + a_['r'] * math.sin(a)
        out += flower(x, y, a_['flower'] * g, i) if k % 2 == 0 else dia(x, y, a_['diamond'] * g, rc, 'solid', None, math.degrees(a) + 90)
    return out
def seal346(p, tag='s346'):
    i, b = p['ink'], BAND
    return (disc(C, C, RO, p['bg']) + pair(i) + name(i) + arc(p)
            + pband(p, b['ri'], b['ro'], s=b['tile'], rev=True, tag=tag)
            + ring(C, C, b['ro'] + b['fine_gap'], i, b['fine_w']) + ring(C, C, b['ri'] - b['fine_gap'], i, b['fine_w'])
            + disc(C, C - CLASP['r'], CLASP['disc'], p['bg']) + flower(C, C - CLASP['r'], CLASP['flower'], i)
            + disc(C, C + FOOT['r'], FOOT['disc'], p['bg']) + flower(C, C + FOOT['r'], FOOT['flower'], i)
            + da(p, w=MONO_W))
names = {'mk': 'paper', 'mkL': 'oxblood', 'mkN': 'night'}
VB = (C - RO, C - RO, 2 * RO, 2 * RO)
def esc(t): return t.replace('&', '&amp;')
def svg(body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{VB[0]:.2f} {VB[1]:.2f} {VB[2]:.2f} {VB[3]:.2f}" role="img" aria-label="{esc(title)}">'
            f'<title>{esc(title)}</title>{body}</svg>\n')
if __name__ == '__main__':
    for k, p in PAL.items():
        open(OUT + f'da-seal-346-{names[k]}.svg', 'w').write(svg(seal346(p, 's346' + names[k]), 'D.A. Accounting & Consulting seal'))
    S = 2 * RO; f = lambda v: round(v / S, 4)
    spec = {
     'design': '346', 'unit': 'S = seal diameter (outer edge of the thick ring); 285.2 units in the master files',
     'S_units': round(S, 2), 'centre_units': [C, C],
     'ratios_of_S': {
      'thick_ring': {'radius': f(141), 'stroke': f(3.2)},
      'thin_ring': {'radius': f(134.5), 'stroke': f(1)},
      'name': {'baseline_radius': f(114), 'font_size': f(13.5), 'tracking_em': .14, 'text': NAME},
      'lower_arc': {'radius': f(ARC['r']), 'pieces': ARC['n'], 'span_deg': ARC['span'], 'flower_radius_centre': f(ARC['flower']),
                    'diamond_half_height_centre': f(ARC['diamond']), 'diamond_half_width': '0.62 of half-height',
                    'grading': 'size x (1 - 0.9 |t|), t = -0.5 ... 0.5 along the arc (100% at the foot, 55% at the ends)',
                    'order': 'flower, diamond, flower ... ending on flowers; the centre piece is replaced by the large foot flower'},
      'band': {'inner_radius': f(BAND['ri']), 'outer_radius': f(BAND['ro']), 'tile_width': f(BAND['tile']), 'tile_height': f(BAND['tile'] * 1.4),
               'tile_centre': 'at the seal centre', 'ring_1': '94% of tile half-width/height', 'ring_2': '62%',
               'lattice_stroke': f(BAND['line_w']), 'flower_radius': f(.17 * BAND['tile']), 'edge_stroke': f(BAND['edge_w']),
               'fine_lines': {'gap': f(BAND['fine_gap']), 'stroke': f(BAND['fine_w'])}},
      'top_clasp': {'centre_radius': f(CLASP['r']), 'flower_radius': f(CLASP['flower']), 'background_disc': f(CLASP['disc'])},
      'foot_flower': {'centre_radius': f(FOOT['r']), 'flower_radius': f(FOOT['flower']), 'background_disc': f(FOOT['disc'])},
      'monogram': {'width': f(MONO_W), 'centre_offset_y': f(MONO_DY), 'definition': 'logo 153, full detail (docs/brand/da-logo-153.md)'}},
     'colours': {
      'paper':   {'background': '#f2eeea', 'letter_colour': '#7a2229', 'rose': '#b07e80', 'silver_in_monogram': '#d4d5d8'},
      'oxblood': {'background': '#7a2229', 'letter_colour': '#f6efe8', 'rose': '#c29998', 'silver_in_monogram': '#85878c'},
      'night':   {'background': '#1b1112', 'letter_colour': '#efe6dc', 'rose': '#be9491', 'silver_in_monogram': '#85878c'}},
     'colour_use': {'rings_name_band_lines_edge_lines_clasp_foot_arc_flowers': 'letter colour', 'arc_diamonds_band_flowers': 'rose',
                    'band_ground_and_discs': 'background'},
     'min_size': {'screen_px': 160, 'print_mm': 30}}
    json.dump(spec, open(OUT + 'da-seal-346.json', 'w'), indent=1, ensure_ascii=False)
    print(S, VB)
