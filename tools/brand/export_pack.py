"""Build the D.A. brand export pack from the master files in brand/ (read only).

Step 1 (this script, Python): write maximum-compatibility SVGs, plus a job list for step 2.
Step 2 (export_pack.js, Node + Playwright/Chromium): render the PNG and PDF files from them.

    python tools/brand/export_pack.py OUT_DIR             # 1. compatible SVGs + job list
    node   tools/brand/export_pack.js OUT_DIR             # 2. PNG and PDF (Chromium)
    python tools/brand/export_pack.py --finish OUT_DIR    # 3. trim each PDF page to the exact artwork size
    python tools/brand/verify_export.py OUT_DIR           # 4. verify everything

Compatible SVG = the master, drawn identically, but with only basic SVG features:
  no <use> (copies are written out), no <pattern> (tiles are written out, clipped), no CSS style
  attributes (plain presentation attributes), no even-odd rule (the shapes are computed exactly instead). Programs such as Illustrator, Canva, PowerPoint and Word
  read these more reliably than the masters.
"""
import copy, json, os, re, sys
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
BRAND = os.path.normpath(os.path.join(HERE, '..', '..', 'brand'))
NS = 'http://www.w3.org/2000/svg'
ET.register_namespace('', NS)
q = lambda t: f'{{{NS}}}{t}'
VERSIONS = ['paper', 'oxblood', 'night']
BG = {'paper': '#f2eeea', 'oxblood': '#7a2229', 'night': '#1b1112'}
PATTERNS = ['401', '406', '417', '420']
# PNG tiles must be whole pixels or they leave a seam when repeated: 401/406 are 36 x 50.4, so 2.5x and 5x
TILE_SCALES = {'401': (2.5, 5), '406': (2.5, 5), '417': (2, 4), '420': (2, 4)}


def style_to_attrs(root):
    for el in root.iter():
        st = el.attrib.pop('style', None)
        if st:
            for part in st.split(';'):
                if ':' in part:
                    k, v = part.split(':', 1); el.set(k.strip(), v.strip())


def rename_ids(el, suffix):
    """Give every id inside a copy a unique suffix, and point its url(#...) references at the renamed ids."""
    ids = {e.get('id') for e in el.iter() if e.get('id')}
    for e in el.iter():
        if e.get('id'): e.set('id', e.get('id') + suffix)
        for k, v in list(e.attrib.items()):
            if 'url(#' in v:
                e.set(k, re.sub(r'url\(#([^)]+)\)', lambda m: f'url(#{m.group(1) + suffix if m.group(1) in ids else m.group(1)})', v))


def expand_use(root):
    """Replace each <use href="#id" x y> with a translated copy of the referenced element."""
    byid = {e.get('id'): e for e in root.iter() if e.get('id')}
    n = 0
    for parent in list(root.iter()):
        for i, child in enumerate(list(parent)):
            if child.tag == q('use'):
                ref = (child.get('href') or child.get('{http://www.w3.org/1999/xlink}href'))[1:]
                g = ET.Element(q('g'), {'transform': f'translate({child.get("x", "0")},{child.get("y", "0")})'})
                c = copy.deepcopy(byid[ref]); c.attrib.pop('id', None); rename_ids(c, f'-u{n}'); n += 1
                g.append(c); parent.remove(child); parent.insert(i, g)
    for defs in root.iter(q('defs')):                  # the originals of the copies are no longer needed
        for e in list(defs):
            if e.tag == q('g'): defs.remove(e)


def annulus_bbox(d):
    """Bounding box of the seal band path: 'M x,y a r,r ...' (outer circle first)."""
    x, y, r = re.match(r'M([\d.-]+),([\d.-]+) a([\d.-]+),', d).groups()
    x, y, r = float(x), float(y), float(r)
    return x, y - r, x + 2 * r, y + r


def expand_patterns(root):
    """Replace a fill="url(#pattern)" shape with the pattern's tiles written out, clipped to the shape."""
    pats = {e.get('id'): e for e in root.iter(q('pattern'))}
    n = 0
    for parent in list(root.iter()):
        for i, child in enumerate(list(parent)):
            m = re.match(r'url\(#([^)]+)\)', child.get('fill', ''))
            if not (m and m.group(1) in pats): continue
            p = pats[m.group(1)]
            px, py, pw, ph = (float(p.get(k, 0)) for k in ('x', 'y', 'width', 'height'))
            x0, y0, x1, y1 = annulus_bbox(child.get('d'))
            cid = f'pclip{n}'; n += 1
            cp = ET.Element(q('clipPath'), {'id': cid})
            shape = copy.deepcopy(child); shape.attrib.pop('fill', None)
            if shape.get('fill-rule'): shape.set('clip-rule', shape.attrib.pop('fill-rule'))
            cp.append(shape)
            g = ET.Element(q('g'), {'clip-path': f'url(#{cid})'})
            import math
            for jx in range(math.floor((x0 - px) / pw), math.ceil((x1 - px) / pw)):
                for jy in range(math.floor((y0 - py) / ph), math.ceil((y1 - py) / ph)):
                    t = ET.SubElement(g, q('g'), {'transform': f'translate({px + jx * pw:.2f},{py + jy * ph:.2f})'})
                    for c in p: t.append(copy.deepcopy(c))
            parent.remove(child); parent.insert(i, cp); parent.insert(i + 1, g)
    for parent in list(root.iter()):
        for c in list(parent):
            if c.tag == q('pattern'): parent.remove(c)


def resolve_evenodd(root):
    """Many programs ignore fill-rule / clip-rule "evenodd" (cairo-based tools, some importers), which would fill the
    opening where D and A overlap and let the seal band's lattice spill out of the band. Compute the even-odd shape
    exactly (skia-pathops, the geometry engine fontTools uses) and write it as a plain path that every program fills
    the same way under the default rule."""
    import pathops
    from fontTools.svgLib.path import parse_path
    from fontTools.pens.svgPathPen import SVGPathPen
    ntos = lambda v: (f'{v:.3f}'.rstrip('0').rstrip('.') or '0')
    for el in root.iter():
        rule_attr = [a for a in ('fill-rule', 'clip-rule') if el.get(a) == 'evenodd']
        if not rule_attr: continue
        assert el.get('d'), f'even-odd on a non-path element: {el.tag}'
        p = pathops.Path(); parse_path(el.get('d'), p.getPen()); p.fillType = pathops.FillType.EVEN_ODD
        p.simplify(fix_winding=True, keep_starting_points=False)
        assert p.fillType == pathops.FillType.WINDING
        pen = SVGPathPen(None, ntos=ntos); p.draw(pen); el.set('d', pen.getCommands())
        for a in rule_attr: el.attrib.pop(a)


def compat(src):
    root = ET.parse(src).getroot()
    style_to_attrs(root); expand_use(root); expand_patterns(root); resolve_evenodd(root)
    return root


def write(root, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    ET.ElementTree(root).write(path, encoding='utf-8', xml_declaration=False)


def strip_background(root):
    """Transparent variant: drop the full-size background rectangle (oxblood / night logo masters)."""
    for c in list(root):
        if c.tag == q('rect'): root.remove(c); return root
    return root


def main(out):
    jobs = []
    sv = lambda *p: os.path.join(out, 'svg-compatible', *p)
    # logo: mark, lockup, small
    for kind, stem in (('logo', 'da-logo-153'), ('lockup', 'da-lockup-153'), ('small', 'da-logo-small')):
        for v in VERSIONS:
            src = os.path.join(BRAND, 'logo', f'{stem}-{v}.svg')
            on = compat(src)
            if v == 'paper':                                       # master is transparent; add the paper background
                vb = [float(x) for x in on.get('viewBox').split()]
                rect = ET.Element(q('rect'), {'x': str(vb[0]), 'y': str(vb[1]), 'width': str(vb[2]), 'height': str(vb[3]), 'fill': BG[v]})
                title_i = [i for i, c in enumerate(on) if c.tag == q('title')]
                on.insert(title_i[0] + 1 if title_i else 0, rect)
                tr = compat(src)
            else:
                tr = strip_background(compat(src))
            write(on, sv('logo', f'{stem}-{v}-background.svg')); write(tr, sv('logo', f'{stem}-{v}-transparent.svg'))
            for variant in ('background', 'transparent'):
                f = sv('logo', f'{stem}-{v}-{variant}.svg')
                for w in (1000, 4000):
                    jobs.append({'src': f, 'png': os.path.join(out, 'png', 'logo', f'{stem}-{v}-{variant}-{w}px.png'), 'width': w, 'master': src,
                                 'transparent': variant == 'transparent', 'page_bg': BG[v] if variant == 'background' else None})
                jobs.append({'src': f, 'pdf': os.path.join(out, 'pdf', 'logo', f'{stem}-{v}-{variant}.pdf')})
    # seal
    for v in VERSIONS:
        src = os.path.join(BRAND, 'seal', f'da-seal-346-{v}.svg')
        f = sv('seal', f'da-seal-346-{v}.svg'); write(compat(src), f)
        for w in (1000, 4000):
            jobs.append({'src': f, 'png': os.path.join(out, 'png', 'seal', f'da-seal-346-{v}-{w}px.png'), 'width': w, 'master': src, 'transparent': True})
        jobs.append({'src': f, 'pdf': os.path.join(out, 'pdf', 'seal', f'da-seal-346-{v}.pdf')})
    # patterns: the tile (compatible SVG, vector PDF, PNG @2x/@4x) and a ready-tiled 3000 px PNG swatch
    for n in PATTERNS:
        for v in VERSIONS + ['quiet']:
            src = os.path.join(BRAND, 'pattern', f'da-pattern-{n}-{v}.svg')
            t = compat(src); f = sv('pattern', f'da-pattern-{n}-{v}-tile.svg'); write(t, f)
            tw, th = float(t.get('width')), float(t.get('height'))
            for k in TILE_SCALES[n]:
                pw, ph = tw * k, th * k
                assert pw == int(pw) and ph == int(ph), (n, k, pw, ph)
                jobs.append({'src': f, 'png': os.path.join(out, 'png', 'pattern', f'da-pattern-{n}-{v}-tile-{int(pw)}x{int(ph)}px.png'), 'width': int(pw), 'master': src, 'transparent': False})
            jobs.append({'src': f, 'pdf': os.path.join(out, 'pdf', 'pattern', f'da-pattern-{n}-{v}-tile.pdf')})
            jobs.append({'tile': src, 'png': os.path.join(out, 'png', 'pattern', f'da-pattern-{n}-{v}-swatch-3000px.png'), 'width': 3000, 'scale': TILE_SCALES[n][0]})
    json.dump(jobs, open(os.path.join(out, 'jobs.json'), 'w'), indent=1)
    print(len(jobs), 'render jobs')


def finish(out):
    """Step 2 prints each artwork at the top-left of a page with spare room. Set the page box to the artwork's exact
    size (1 unit = 1 CSS px = 0.75 pt). The drawing itself is not touched."""
    from pypdf import PdfReader, PdfWriter
    from pypdf.generic import RectangleObject
    n = 0
    for j in json.load(open(os.path.join(out, 'jobs.json'))):
        if not j.get('pdf'): continue
        vb = [float(x) for x in ET.parse(j['src']).getroot().get('viewBox').split()]
        w, h = vb[2] * .75, vb[3] * .75
        r = PdfReader(j['pdf']); wr = PdfWriter()
        for page in r.pages:
            top = float(page.mediabox.top)
            box = RectangleObject([0, top - h, w, top])
            page.mediabox = box; page.cropbox = box; page.trimbox = box; page.bleedbox = box; page.artbox = box
            wr.add_page(page)
        with open(j['pdf'], 'wb') as f: wr.write(f)
        n += 1
    print(n, 'PDF pages trimmed to the artwork size')


if __name__ == '__main__':
    if sys.argv[1] == '--finish':
        finish(os.path.abspath(sys.argv[2])); sys.exit()
    out = os.path.abspath(sys.argv[1])
    if os.path.commonpath([out, BRAND]) == BRAND and not out.startswith(os.path.join(BRAND, 'export')):
        sys.exit('Refusing to write into the originals (brand/logo, seal, pattern, reference).')
    main(out)
