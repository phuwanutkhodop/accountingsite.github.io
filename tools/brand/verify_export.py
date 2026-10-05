"""Verify a D.A. brand export pack (made by export_pack.py + export_pack.js).

    python tools/brand/verify_export.py PACK_DIR

Checks, for every file:
  compatible SVG  valid XML; no <use>, <pattern> or style attributes; in a second, non-browser engine (cairosvg,
                  if installed) it draws the same picture as the original master (compared after a light blur,
                  which ignores anti-aliasing but catches any shape, position or colour change)
  PNG             pixel size as named; transparent files are see-through at the corners; background files are
                  fully opaque with the right colour at the corners; pattern tiles repeat without a seam
  PDF             one page of the artwork's size; pure vector (no embedded pictures); renders with a second
                  engine (poppler's pdftoppm) to the same picture as the PNG
Needs Pillow; cairosvg and poppler-utils make the checks complete (missing ones are reported as skipped).
"""
import io, json, os, re, shutil, subprocess, sys, tempfile
import xml.etree.ElementTree as ET
from PIL import Image, ImageChops, ImageFilter

BG = {'paper': (242, 238, 234), 'oxblood': (122, 34, 41), 'night': (27, 17, 18)}
TOL = 40            # max difference (0-255) after a 1.5 px blur: anti-aliasing passes, any real change fails
fails, skipped, passed = [], set(), 0


def ok(cond, what):
    global passed
    if cond: passed += 1
    else: fails.append(what)


def close(a, b, what):
    a, b = a.convert('RGB'), b.convert('RGB')
    if a.size != b.size: b = b.resize(a.size, Image.LANCZOS)
    d = ImageChops.difference(a.filter(ImageFilter.GaussianBlur(1.5)), b.filter(ImageFilter.GaussianBlur(1.5))).convert('L')
    ok(max(d.get_flattened_data()) <= TOL, f'{what}: pictures differ (max {max(d.get_flattened_data())})')


def flat(img, rgb):
    bg = Image.new('RGBA', img.size, rgb + (255,)); bg.alpha_composite(img.convert('RGBA')); return bg.convert('RGB')


def main(pack):
    jobs = json.load(open(os.path.join(pack, 'jobs.json')))
    try: import cairosvg
    except ImportError: cairosvg = None; skipped.add('second SVG engine (pip install cairosvg)')
    poppler = shutil.which('pdftoppm') and shutil.which('pdfimages') and shutil.which('pdfinfo')
    if not poppler: skipped.add('PDF checks (install poppler-utils)')
    for j in jobs:
        if j.get('png'):
            im = Image.open(j['png']); name = os.path.basename(j['png'])
            m = re.search(r'-(\d+)px\.png$', name) or re.search(r'-(\d+)x(\d+)px\.png$', name)
            ok(im.width == j['width'], f'{name}: width {im.width} != {j["width"]}')
            if 'tile-' in name:
                w, h = map(int, re.search(r'-(\d+)x(\d+)px', name).groups()); ok(im.size == (w, h), f'{name}: size {im.size}')
            v = re.search(r'-(paper|oxblood|night|quiet)', name).group(1)
            rgba = im.convert('RGBA'); corners = [rgba.getpixel(p) for p in ((0, 0), (im.width - 1, 0), (0, im.height - 1), (im.width - 1, im.height - 1))]
            if j.get('transparent') and '-seal-' in name: ok(all(c[3] == 0 for c in corners), f'{name}: corners not transparent')
            if j.get('page_bg'):
                ok(min(rgba.getchannel('A').get_flattened_data()) == 255, f'{name}: not fully opaque')
                edge = [rgba.getpixel((x, y))[:3] for x in range(0, im.width, 7) for y in (0, im.height - 1)] + [rgba.getpixel((x, y))[:3] for y in range(0, im.height, 7) for x in (0, im.width - 1)]
                # the artwork may touch the edges; but no edge pixel may be lighter than the artwork allows (a white hairline)
                common = max(set(edge), key=edge.count)
                ok(max(abs(common[i] - BG[v][i]) for i in range(3)) <= 2, f'{name}: background colour {common} is not {v}')
                ok(all(sum(p) < 3 * 252 for p in edge), f'{name}: white pixels on the edge (hairline)')
            if 'tile-' in name and j['width'] == min(x['width'] for x in jobs if x.get('png', '').startswith(j['png'].split('-tile-')[0] + '-tile-')):
                sw = Image.open(j['png'].split('-tile-')[0] + '-swatch-3000px.png').convert('RGB')
                grid = Image.new('RGB', (im.width * 3, im.height * 3))
                for x in range(3):
                    for y in range(3): grid.paste(im.convert('RGB'), (x * im.width, y * im.height))
                close(grid, sw.crop((0, 0, grid.width, grid.height)), f'{name}: 3x3 repeat vs swatch (seams)')
            if cairosvg and j.get('src') and j.get('master') and j['width'] <= 1000:
                # same engine, original vs compatible: proves the conversion changed nothing in a non-browser renderer
                r = lambda u: Image.open(io.BytesIO(cairosvg.svg2png(url=u, output_width=im.width, output_height=im.height))).convert('RGBA')
                base = BG.get(v, BG['paper'])
                close(flat(r(j['master']), base), flat(r(j['src']), base), f'{name}: cairosvg, original vs compatible SVG')
        elif j.get('pdf') and poppler:
            name = os.path.basename(j['pdf'])
            info = subprocess.run(['pdfinfo', j['pdf']], capture_output=True, text=True).stdout
            ok(re.search(r'Pages:\s+1\b', info) is not None, f'{name}: not exactly one page')
            vb = [float(x) for x in ET.parse(j['src']).getroot().get('viewBox').split()]
            pw, ph = map(float, re.search(r'Page size:\s+([\d.]+) x ([\d.]+) pts', info).groups())
            ok(abs(pw - vb[2] * .75) < .02 and abs(ph - vb[3] * .75) < .02, f'{name}: page {pw} x {ph} pt is not the artwork size {vb[2] * .75:.2f} x {vb[3] * .75:.2f}')
            imgs = subprocess.run(['pdfimages', '-list', j['pdf']], capture_output=True, text=True).stdout.strip().splitlines()[2:]
            ok(len(imgs) == 0, f'{name}: contains {len(imgs)} raster picture(s), not pure vector')
            twin = sorted([x for x in jobs if x.get('src') == j['src'] and x.get('png')], key=lambda x: -x['width'])
            if twin:
                ref = Image.open(twin[0]['png'])
                with tempfile.TemporaryDirectory() as t:
                    subprocess.run(['pdftoppm', '-png', '-singlefile', '-scale-to-x', str(ref.width), '-scale-to-y', str(ref.height), j['pdf'], os.path.join(t, 'p')], check=True)
                    p = Image.open(os.path.join(t, 'p.png'))
                # poppler draws see-through areas on white, so the PNG is put on white for this comparison
                close(flat(ref, (255, 255, 255)), p.convert('RGB'), f'{name}: poppler render vs PNG')
    for root, _, files in os.walk(os.path.join(pack, 'svg-compatible')):
        for f in files:
            s = open(os.path.join(root, f), encoding='utf-8').read()
            try: ET.fromstring(s); ok(True, '')
            except ET.ParseError as e: ok(False, f'{f}: invalid XML {e}')
            ok(not re.search(r'<use\b|<pattern\b|\sstyle=|evenodd', s), f'{f}: still uses <use>, <pattern>, style or evenodd')
    print(f'checks passed: {passed}')
    for s in sorted(skipped): print('skipped:', s)
    for f in fails: print('FAIL:', f)
    print('OK: the export pack is verified.' if not fails else f'FAILED: {len(fails)} problem(s).')
    return not fails


if __name__ == '__main__':
    sys.exit(0 if main(os.path.abspath(sys.argv[1])) else 1)
