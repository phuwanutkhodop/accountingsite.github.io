"""Export the locked D.A. pattern set (401, 406, 417, 420) as seamless repeat tiles. Geometry is identical to the boards."""
import os, sys, json
import patterns1 as P
from seals import mono_patterned
OUT = os.path.join(os.environ.get('DA_BRAND_OUT') or sys.exit('Run tools/brand/build.py: the exporters never write into brand/ directly.'), 'pattern', '')
LOCK = ['401', '406', '417', '420']
NAMES = {'mk': 'paper', 'mkL': 'oxblood', 'mkN': 'night'}
QUIET = .14
fns = {n: f for n, d, f in P.V}
def tile(num, key, quiet=False):
    c = P.COLS[key]; w, h, ground, body = fns[num](c)
    defs = f'<defs><g id="da{key}">{mono_patterned(0, 0, P.DA_W[num], c["p"])}</g></defs>' if num in P.DA_W else ''
    inner = f'<rect width="{P.F(w)}" height="{P.F(h)}" style="fill: {ground}"></rect>{body}'
    if quiet: inner = f'<rect width="{P.F(w)}" height="{P.F(h)}" style="fill: #f2eeea"></rect><g style="opacity: {QUIET}">{inner}</g>'
    t = f'D.A. pattern {num}'
    return (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{P.F(w)}" height="{P.F(h)}" viewBox="0 0 {P.F(w)} {P.F(h)}" role="img" aria-label="{t}">'
            f'<title>{t}</title>{defs}{inner}</svg>\n'), w, h
if __name__ == '__main__':
    spec = {}
    for num in LOCK:
        for key, nm in NAMES.items():
            s, w, h = tile(num, key); open(OUT + f'da-pattern-{num}-{nm}.svg', 'w').write(s)
        s, w, h = tile(num, 'mk', quiet=True); open(OUT + f'da-pattern-{num}-quiet.svg', 'w').write(s)
        spec[num] = {'tile_px': [round(w, 2), round(h, 2)], 'da_width_px': P.DA_W.get(num)}
    json.dump({'set': LOCK, 'quiet': f'paper version at {QUIET:.0%} opacity over paper #F2EEEA', 'tiles': spec}, open(OUT + 'da-patterns.json', 'w'), indent=1)
    print(spec)
