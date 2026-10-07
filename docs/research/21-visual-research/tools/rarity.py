"""Rarity numbers for #21: how common each measured technique is on top sites versus the ordinary baseline.

Usage:  python rarity.py <path to the builder-research repo>
Writes ../rarity.md (next to this tools folder) and prints where it went.

Input: every shots/<site>/signals.json and baseline/<site>/signals.json written by capture.cjs.
Only text is written out (site names, font names, yes/no flags); no screenshots leave builder-research.
"""
import collections, datetime, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'rarity.md')

# Captures that show a bot wall, an error or a placeholder page instead of the site.
FAILED_TITLE = re.compile(r'just a moment|access denied|site not found|undergoing brief maintenance', re.I)
# Same brand captured twice (same stylesheets): count once.
DUPLICATE = {'rosewoodhotels.com_en_bangkok'}
# Sites captured outside sites.tsv.
EXTRA_GROUP = {'pentagram.com': 'studio', 'aesop.com': 'luxury'}
# Below this many bytes the capture did not see the site's CSS (Framer and CSS-in-JS sites put it inside the page).
CSS_MIN = 10_000
GROUP_LABEL = {'finance': 'finance / law / consulting', 'law': 'finance / law / consulting',
               'consulting': 'finance / law / consulting', 'editorial': 'editorial / craft', 'craft': 'editorial / craft',
               'luxury': 'luxury', 'thai': 'Thai', 'studio': 'design studios', 'award': 'award winners'}
GROUP_ORDER = ['finance / law / consulting', 'luxury', 'editorial / craft', 'Thai', 'design studios', 'award winners']

# Icon fonts are not typefaces.
ICON_FONTS = {'VideoJS', 'icomoon', 'Font Awesome 5 Free', 'Font Awesome 5 Brands', 'Font Awesome 6 Brands', 'FontAwesome',
              'FontAwesome--Brands', 'swiper-icons', 'bainicon', 'icons', 'Flaticon', 'nw-icons', 'svgicons', 'ETmodules',
              'swym-font', 'OrderArrow', 'Material Icons', 'Material_Icons--Filled', 'Material_Icons--Outlined'}
# Free faces: Google Fonts and other open-licence families seen in the captures.
FREE_FONTS = {'Inter', 'Inter Variable', 'InterVariable', 'Inter Medium', 'Manrope', 'Roboto', 'Open Sans', 'openSans',
              'OpenSans--Regular', 'OpenSans--SemiBold', 'OpenSans_Condensed--Bold', 'Playfair Display', 'Nunito Sans',
              'Lato', 'Trirong', 'IBM Plex Sans', 'Heebo', 'EBGaramond', 'eb-garamond', 'Overpass Mono', 'Work Sans',
              'Poppins', 'Source Sans Pro', 'Lora', 'lora', 'Mona Sans', 'DM Mono', 'Geist', 'Geist Mono', 'GeistMono',
              'JetBrains Mono', 'SourceCodePro', 'Cormorant SC', 'Hedvig Letters Serif', 'Prompt', 'Golos Text',
              'Instrument Serif', 'Cabinet Grotesk', 'Apfel Grotezk', 'Azeret Mono', 'Cagliostro'}
# Faces made for the brand itself (hand classification: the face carries the brand's name, or is publicly the brand's own).
OWN_FACE = {'coutts.com': 'Coutts Siena / Coutts Forme', 'freshfields.com': 'Freshfields Headline / Text',
            'lombardodier.com': 'Lombard Odier', 'kinfolk.com': 'Kinfolk Serif / Sans', 'rolex.com': 'RolexFont',
            'pjtpartners.com': 'pjtSans', 'bottegaveneta.com_en-us': 'Bottega Veneta', 'byredo.com': 'byredoSans',
            'locomotive.ca_en': 'LocomotiveNew', 'redcollar.co': 'RedCollar', 'obys.agency': 'Obys',
            'koto.studio': 'GT Kotoheim', 'bcg.com': 'Henderson BCG', 'pwc.com_th_en.html': 'PwC Charter / Helvetica',
            'ey.com_en_th': 'EYInterstate', 'farmgroup.co.th': 'Farm Sans', 'teenage.engineering': 'te-20 / te-40',
            'family.co': 'Family', 'theatlantic.com': 'Atlantic Serif', 'cartier.com_en-us': 'Brilliant Cut / Fancy Cut',
            'apple.com': 'SF Pro', 'vercel.com': 'Geist', 'instrument.com': 'Instrument Serif / Sans',
            'exemplarfromsweden.com': 'Exemplar'}
# Signals whose pattern also matches ordinary words, so their counts overstate use.
LOOSE = {'grain/noise texture': 'matches the words "noise" or "grain" anywhere in the CSS',
         'CSS masks': 'also matches vendor icon and image masks',
         'three.js / WebGL': 'matches the word "webgl" in any script (feature checks, maps, analytics)',
         'splitting': 'matches the word "splitting" in any script'}


def slug(url):
    s = re.sub(r'^https?://(www\.)?', '', url)
    return re.sub(r'_+$', '', re.sub(r'[^\w.-]+', '_', s))[:60]


def load(root):
    group = dict(EXTRA_GROUP)
    for line in open(os.path.join(root, 'tools', 'sites.tsv'), encoding='utf-8'):
        if '\t' in line:
            g, u = line.strip().split('\t')
            group[slug(u)] = g
    sites = []
    for top in ('shots', 'baseline'):
        for d in sorted(os.listdir(os.path.join(root, top))):
            p = os.path.join(root, top, d, 'signals.json')
            if not os.path.exists(p):
                continue
            j = json.load(open(p, encoding='utf-8'))
            dom = j.get('dom') or {}
            s = {'site': d, 'baseline': top == 'baseline',
                 'group': 'baseline' if top == 'baseline' else GROUP_LABEL.get(group.get(d), '?'),
                 'css': j.get('css') or {}, 'cssBytes': j.get('cssBytes') or 0, 'libs': j.get('libs') or [],
                 'fonts': [f for f in (dom.get('fontsLoaded') or []) if f not in ICON_FONTS]}
            title = dom.get('title') or ''
            if not j.get('ok'):
                s['excluded'] = 'did not load'
            elif FAILED_TITLE.search(title):
                s['excluded'] = f'"{title[:40]}" page instead of the site'
            elif d in DUPLICATE:
                s['excluded'] = 'same brand as another capture'
            s['cssReadable'] = s['cssBytes'] >= CSS_MIN
            if d in OWN_FACE:
                s['type'] = 'own'
            elif not s['fonts']:
                s['type'] = 'unknown'
            elif all(f in FREE_FONTS for f in s['fonts']):
                s['type'] = 'free'
            else:
                s['type'] = 'licensed'
            sites.append(s)
    return sites


def pct(k, n):
    return f'{round(100 * k / n)}%' if n else '–'


def main(root):
    sites = load(root)
    used = [s for s in sites if 'excluded' not in s]
    top = [s for s in used if not s['baseline']]
    base = [s for s in used if s['baseline']]
    groups = [g for g in GROUP_ORDER if any(s['group'] == g for s in top)]
    L = []
    w = L.append

    # Typefaces
    def type_row(label, ss):
        known = [s for s in ss if s['type'] != 'unknown']
        c = collections.Counter(s['type'] for s in known)
        n = len(known)
        return (f"| {label} | {n} | {c['own']} ({pct(c['own'], n)}) | {c['licensed']} ({pct(c['licensed'], n)}) "
                f"| {c['free']} ({pct(c['free'], n)}) | {pct(c['own'] + c['licensed'], n)} |")
    type_rows = [type_row('**All top sites**', top)] + [type_row(g, [s for s in top if s['group'] == g]) for g in groups]
    type_rows.append(type_row('**Baseline (ordinary)**', base))

    # CSS techniques
    ctop = [s for s in top if s['cssReadable']]
    cbase = [s for s in base if s['cssReadable']]
    techniques = list(next(s for s in sites if s['css'])['css'].keys())
    css_rows = []
    for t in techniques:
        k = sum(1 for s in ctop if s['css'].get(t))
        b = sum(1 for s in cbase if s['css'].get(t))
        share = k / len(ctop)
        band = 'common' if share >= 0.5 else 'uncommon' if share >= 0.2 else 'rare'
        css_rows.append((share, f"| {t} | {pct(k, len(ctop))} ({k}) | {b} of {len(cbase)} | {band}"
                                f"{' · loose pattern' if t in LOOSE else ''} |"))
    css_rows.sort(key=lambda r: -r[0])
    by_group = []
    for t in techniques:
        cells = []
        for g in groups:
            gs = [s for s in ctop if s['group'] == g]
            cells.append(pct(sum(1 for s in gs if s['css'].get(t)), len(gs)))
        by_group.append(f"| {t} | " + ' | '.join(cells) + ' |')

    # Script libraries
    all_libs = sorted({l for s in used for l in s['libs']})
    lib_rows = []
    for l in all_libs:
        k = sum(1 for s in top if l in s['libs'])
        b = sum(1 for s in base if l in s['libs'])
        lib_rows.append((k, f"| {l} | {pct(k, len(top))} ({k}) | {b} of {len(base)} |"
                            f"{' loose pattern' if l in LOOSE else ''} |"))
    lib_rows.sort(key=lambda r: -r[0])
    framer = [s for s in base if 'framer' in s['libs']]
    framer_lenis = sum(1 for s in framer if 'lenis' in s['libs'])
    top_lenis = sum(1 for s in top if 'lenis' in s['libs'])
    fin = [s for s in top if s['group'] == 'finance / law / consulting']
    fin_lenis = sum(1 for s in fin if 'lenis' in s['libs'])

    excluded = [s for s in sites if 'excluded' in s]
    css_blind_top = [s['site'] for s in top if not s['cssReadable']]
    css_blind_base = [s['site'] for s in base if not s['cssReadable']]
    tknown = [s for s in top if s['type'] != 'unknown']
    bknown = [s for s in base if s['type'] != 'unknown']
    t_paid = sum(1 for s in tknown if s['type'] in ('own', 'licensed'))
    b_free = sum(1 for s in bknown if s['type'] == 'free')
    top_free = [s['site'] for s in tknown if s['type'] == 'free']
    showcase = ('design studios', 'award winners')
    lenis_showcase = sum(1 for s in top if 'lenis' in s['libs'] and s['group'] in showcase)
    lib_by_group = []
    for l in ('gsap', 'lenis', 'barba', 'lottie', 'three.js / WebGL'):
        cells = []
        for g in groups:
            gs = [s for s in top if s['group'] == g]
            cells.append(pct(sum(1 for s in gs if l in s['libs']), len(gs)))
        lib_by_group.append(f"| {l} | " + ' | '.join(cells) + f" | {pct(sum(1 for s in base if l in s['libs']), len(base))} |")
    gsap_fin = sum(1 for s in fin if 'gsap' in s['libs'])
    gsap_show = [s for s in top if s['group'] in showcase]
    gsap_show_k = sum(1 for s in gsap_show if 'gsap' in s['libs'])

    w('# Rarity numbers: what the measurements show (#21, step 1)')
    w('')
    w(f'**Made:** {datetime.date.today():%d %B %Y} by `tools/rarity.py` from the `signals.json` of every capture in the private '
      '`builder-research` repo. Run it again with `python tools/rarity.py <path to builder-research>`.')
    w('')
    w('**What it is for:** the reviewers scored each finding\'s rarity by eye (1–5). This file adds the part that can be '
      'counted: which typefaces, CSS techniques and script libraries the top sites use, compared with the ordinary '
      'baseline (paid accounting templates, Big-4 Thailand, a Thai accounting firm, our current site).')
    w('')
    w('## In short')
    w('')
    w(f'1. **Type is the clearest measured gap.** {t_paid} of {len(tknown)} top sites ({pct(t_paid, len(tknown))}) load a '
      f'licensed typeface or one made for the brand. {b_free} of {len(bknown)} baseline sites use free fonts only.')
    w(f'2. **Smooth scrolling is a template trait, not a premium one.** {framer_lenis} of the {len(framer)} Framer '
      f'templates load Lenis smooth scrolling. Only {fin_lenis} of {len(fin)} finance, law and consulting sites do '
      f'({top_lenis} of {len(top)} top sites overall; {lenis_showcase} of those {top_lenis} are design studios or award winners).')
    w('3. **The CSS counts are weak.** They show what a stylesheet *contains*, not what the page *uses*, and the capture '
      f'could not read the CSS of {len(css_blind_base)} of the {len(base)} baseline sites. Treat the CSS table as a hint, '
      'not proof; section 5 says how to fix it.')
    w('')
    w('## Which sites count')
    w('')
    w(f'- **Used:** {len(top)} top sites and {len(base)} baseline sites.')
    w(f'- **Left out ({len(excluded)}):** ' + '; '.join(f"`{s['site']}` ({s['excluded']})" for s in excluded) + '.')
    w(f'- **CSS not readable** (under {CSS_MIN // 1000} KB of stylesheets captured; the site puts its CSS inside the page): '
      f'top: {", ".join(f"`{x}`" for x in css_blind_top)}; baseline: {", ".join(f"`{x}`" for x in css_blind_base)}. '
      'These sites still count for typefaces and libraries, but not in the CSS table.')
    w('')
    w('## 1. Typefaces')
    w('')
    w('Each site is put in one class by the text faces it loaded (icon fonts ignored):')
    w('- **own face:** a face made for the brand (it carries the brand\'s name, or is publicly the brand\'s own; listed in the appendix);')
    w('- **licensed:** at least one face that is not free (bought from a foundry, or an unnamed custom alias);')
    w('- **free only:** Google Fonts or other open-licence faces only.')
    w('')
    w('| Group | Sites with fonts | Own face | Licensed | Free only | Own + licensed |')
    w('|---|---|---|---|---|---|')
    L.extend(type_rows)
    w('')
    w(f'Top sites with free faces only: {", ".join(f"`{s}`" for s in top_free)}.')
    w('')
    w('*Observation (judgement, not measured):* free fonts do not make a site cheap on their own; the sites above use '
      'free faces only. The baseline\'s problem is free faces **plus** the template habits in `baseline.md`. A '
      'licensed face is a visible sign that money was spent, and the builder already supports any self-hosted face '
      '(decision #15).')
    w('')
    w('## 2. CSS techniques')
    w('')
    w(f'Share of the {len(ctop)} top sites whose CSS was readable, against the {len(cbase)} readable baseline sites '
      f'({", ".join(s["site"] for s in cbase)}). Bands: common ≥ 50%, uncommon 20–49%, rare < 20%.')
    w('')
    w('| Technique | Top sites | Baseline | Band |')
    w('|---|---|---|---|')
    L.extend(r for _, r in css_rows)
    w('')
    w('Large sites ship large stylesheets that contain rules they never show on the page (Bottega Veneta and KKR load '
      'over 4 MB of CSS), so a "yes" here means "available", not "seen".')
    w('')
    w('**By group** (share of readable sites in each group):')
    w('')
    w('| Technique | ' + ' | '.join(f'{g} ({sum(1 for s in ctop if s["group"] == g)})' for g in groups) + ' |')
    w('|---|' + '---|' * len(groups))
    L.extend(by_group)
    w('')
    w('## 3. Script libraries')
    w('')
    w(f'Share of all {len(top)} top sites against all {len(base)} baseline sites.')
    w('')
    w('| Library | Top sites | Baseline | Note |')
    w('|---|---|---|---|')
    L.extend(r for _, r in lib_rows)
    w('')
    w('**By group:**')
    w('')
    w('| Library | ' + ' | '.join(f'{g} ({sum(1 for s in top if s["group"] == g)})' for g in groups) + f' | baseline ({len(base)}) |')
    w('|---|' + '---|' * (len(groups) + 1))
    L.extend(lib_by_group)
    w('')
    w('## 4. What this means for the presets')
    w('')
    w('Measured:')
    w(f'- Own or licensed type: {pct(t_paid, len(tknown))} of top sites, against {pct(len(bknown) - b_free, len(bknown))} of the baseline.')
    w(f'- Smooth scrolling: {framer_lenis} of {len(framer)} paid templates, {fin_lenis} of {len(fin)} finance, law and consulting sites.')
    w('')
    w('Judgement *(ข้อคิดเห็น)*, for the owner board and the preset quality bar:')
    w('- **Type carries the premium signal more than effects do.** When the owner judges presets, show them set in a '
      'serious licensed face as well as in the free test-theme faces, so a weak preset cannot pass, and a good one '
      'cannot fail, because of the face alone.')
    w(f'- **No smooth scrolling and no scroll-jacking in presets.** The firms we want to resemble almost never use it '
      f'({fin_lenis} of {len(fin)}); the paid templates all do.' if framer_lenis == len(framer) else
      f'- **No smooth scrolling and no scroll-jacking in presets.** The firms we want to resemble almost never use it '
      f'({fin_lenis} of {len(fin)}); {framer_lenis} of {len(framer)} paid templates do.')
    w(f'- **Animation libraries are not what sets the firms apart.** GSAP loads on {gsap_fin} of {len(fin)} finance, law and '
      f'consulting sites and on {gsap_show_k} of {len(gsap_show)} studio and award sites. Studios use motion to show off '
      'their own craft. A firm\'s presets should not depend on it, and must read fully without it.')
    w('- The CSS table is too weak to rank craft details such as numerals, small caps or multi-column text. The '
      'reviewers\' rarity scores remain the main guide for those until the measurement is fixed (section 5).')
    w('')
    w('## 5. Limits, and how to make the numbers trustworthy')
    w('')
    w('- **Presence, not use.** `capture.cjs` tests stylesheet *text* with a pattern, so a rule that is never applied still '
      'counts. Fix: measure on the rendered page (for example, how many visible elements use tabular figures, sticky '
      'positioning or small caps).')
    w('- **Inline CSS is missed.** Only separate stylesheet files are read, so Framer and CSS-in-JS sites look empty. '
      'Fix: also read `<style>` blocks and `document.styleSheets`.')
    w('- **Loose patterns:** ' + '; '.join(f'*{k}* {v}' for k, v in LOOSE.items()) + '.')
    w('- **Small baseline:** only 4 baseline sites have readable CSS, and none of them is a paid template.')
    w('- Fonts list only faces loaded near the top of the page (first 12).')
    w('')
    w('Both fixes need the signal step to run again over the same sites in a real browser. No new screenshots are needed. '
      'This is a separate step and waits for the owner\'s OK.')
    w('')
    w('## Appendix: per-site classification')
    w('')
    w('| Site | Group | Type class | Faces (icons removed) | CSS readable | Libraries |')
    w('|---|---|---|---|---|---|')
    for s in sorted(used, key=lambda s: (s['baseline'], GROUP_ORDER.index(s['group']) if s['group'] in GROUP_ORDER else 9, s['site'])):
        faces = OWN_FACE.get(s['site']) or ', '.join(s['fonts'][:5]) or '–'
        w(f"| `{s['site']}` | {s['group']} | {s['type']} | {faces} | {'yes' if s['cssReadable'] else 'no'} "
          f"| {', '.join(s['libs']) or '–'} |")
    w('')
    with open(OUT, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(L))
    print(f'wrote {os.path.normpath(OUT)}: {len(top)} top, {len(base)} baseline, {len(excluded)} left out')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
