"""Export the locked D.A. logo (153) as master SVGs with flat colours. Geometry is identical to board 153."""
import os, sys, re, json
from marks12 import PAL, LINE
LINE['silver'] = lambda p: ('#d4d5d8', 1) if p['kind'] == 'day' else ('#85878c', 1)
FLAT_ROSE = {'#f2eeea': '#b07e80', '#7a2229': '#c29998', '#1b1112': '#be9491'}   # rose rings resolved to solid colour per background
LINE['rose'] = lambda p: (FLAT_ROSE[p['bg']], 1)
from marks13 import design
from marks9 import DP, AP, XD, BASE, XA, d0, a0
from marks6 import gw
build = design(ring='rose', flowerc='silver', style='eight', tag='153')
OUT = os.path.join(os.environ.get('DA_BRAND_OUT') or sys.exit('Run tools/brand/build.py: the exporters never write into brand/ directly.'), 'logo', '')
x0, y0, x1, y1 = XD + d0[0], BASE - a0[3], XA + a0[2], BASE
W, H = x1 - x0, y1 - y0
names = {'mk': 'paper', 'mkL': 'oxblood', 'mkN': 'night'}
t = "D.A. ACCOUNTING & CONSULTING"
w1 = sum(gw("CG600.ttf", c, 1) if c != ' ' else .28 for c in t) + .2 * (len(t) - 1)
NAME_SIZE = min(17, 312 / w1)
def esc(t): return t.replace('&', '&amp;')
def svg(vb, body, title, bg=None):
    b = f'<rect x="{vb[0]}" y="{vb[1]}" width="{vb[2]}" height="{vb[3]}" fill="{bg}"/>' if bg else ''
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb[0]:.2f} {vb[1]:.2f} {vb[2]:.2f} {vb[3]:.2f}" role="img" aria-label="{esc(title)}">'
            f'<title>{esc(title)}</title>{b}{body}</svg>\n')
for k, p in PAL.items():
    full = build(p)
    mark_only = full[:full.rfind('<path d="')]          # drop the name line
    tight = (x0, y0, W, H)
    open(OUT + f'da-logo-153-{names[k]}.svg', 'w').write(svg(tight, mark_only, 'D.A. logo', p['bg'] if k != 'mk' else None))
    lock = (x0, y0, W, 254 - y0 + 8)
    open(OUT + f'da-lockup-153-{names[k]}.svg', 'w').write(svg(lock, full, 'D.A. Accounting & Consulting', p['bg'] if k != 'mk' else None))
    solid = f'<path d="{DP} {AP}" fill="{p["ink"]}" fill-rule="evenodd"/>'
    open(OUT + f'da-logo-small-{names[k]}.svg', 'w').write(svg(tight, solid, 'D.A. logo (small sizes)', p['bg'] if k != 'mk' else None))
spec = {
 'design': '153', 'unit': 'H = cap height of the D (190 units in the master files)',
 'H_units': 190, 'mark_bbox_units': [round(x0, 2), round(y0, 2), round(W, 2), round(H, 2)],
 'ratios_of_H': {
   'mark_width': round(W / 190, 4), 'mark_height': round(H / 190, 4),
   'D_width': round((d0[2] - d0[0]) / 190, 4), 'overlap_D_A': round(((XD + d0[2]) - (XA + a0[0])) / 190, 4),
   'tile_width': round(44 / 190, 4), 'tile_height': round(61.6 / 190, 4),
   'ring_outer': '94% of tile half-width/height', 'ring_inner': '62% of tile half-width/height',
   'ring_stroke': round(1 / 190, 5), 'flower_radius': round(0.17 * 44 / 190, 4), 'minor_petal_radius': round(0.17 * 44 * .52 / 190, 4),
   'pattern_origin_from_D_topleft': [round(-20 / 190, 4), round(-20 / 190, 4)],
   'name_cap_size': round(NAME_SIZE / 190, 4), 'name_baseline_below_letters': round(44 / 190, 4), 'clear_space': 0.25},
 'font': {'letters': 'Bodoni Moda Bold, optical size 11 (Google Fonts, OFL)', 'letter_size_units': round(253.3333, 4),
          'name': 'Cormorant Garamond SemiBold, capitals, tracking 0.20 em'},
 'colours': {
   'paper':   {'background': '#f2eeea', 'letters': '#7a2229', 'rings': '#b07e80', 'flowers': '#d4d5d8'},
   'oxblood': {'background': '#7a2229', 'letters': '#f6efe8', 'rings': '#c29998', 'flowers': '#85878c'},
   'night':   {'background': '#1b1112', 'letters': '#efe6dc', 'rings': '#be9491', 'flowers': '#85878c'}},
 'min_size_px': {'patterned': 96, 'plain_small_version_below': 96, 'plain_absolute_min': 16}}
json.dump(spec, open(OUT + 'da-logo-153.json', 'w'), indent=1, ensure_ascii=False)
print(NAME_SIZE, W, H); print(json.dumps(spec['ratios_of_H'], indent=0))
