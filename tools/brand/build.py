"""D.A. brand toolchain: rebuild the locked master files and prove they match the originals.

    python tools/brand/build.py --check      rebuild into a temporary folder and compare byte for byte with brand/
                                              (also verifies brand/MANIFEST.sha256). Changes nothing.
    python tools/brand/build.py --out DIR    rebuild every master into DIR (DIR/logo, DIR/seal, DIR/pattern).
    python tools/brand/build.py --verify     only check brand/ against brand/MANIFEST.sha256.

The originals in brand/ are never written by this script. Needs Python 3 and fontTools (tools/brand/requirements.txt).
"""
import argparse, filecmp, hashlib, os, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'src')
BRAND = os.path.normpath(os.path.join(HERE, '..', '..', 'brand'))
MANIFEST = os.path.join(BRAND, 'MANIFEST.sha256')
EXPORTERS = ['export153.py', 'export346.py', 'export_patterns.py']      # logo 153, seal 346, patterns
PARTS = ['logo', 'seal', 'pattern']


def rebuild(out):
    for p in PARTS: os.makedirs(os.path.join(out, p), exist_ok=True)
    env = dict(os.environ, DA_BRAND_OUT=out)
    for e in EXPORTERS:           # each in its own process: the modules keep shared state, as when they were first run
        subprocess.run([sys.executable, e], cwd=SRC, env=env, check=True, stdout=subprocess.DEVNULL)


def sha(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f: h.update(f.read())
    return h.hexdigest()


def verify():
    bad = 0
    with open(MANIFEST, encoding='utf-8') as f:
        rows = [l.split(None, 1) for l in f if l.strip() and not l.startswith('#')]
    for digest, name in rows:
        name = name.strip().lstrip('*'); path = os.path.join(BRAND, name)
        if not os.path.exists(path): print('MISSING ', name); bad += 1
        elif sha(path) != digest: print('CHANGED ', name); bad += 1
    print(f'manifest: {len(rows) - bad}/{len(rows)} files match')
    return bad == 0


def check():
    ok = verify()
    with tempfile.TemporaryDirectory() as out:
        rebuild(out)
        n = 0
        for p in PARTS:
            for name in sorted(os.listdir(os.path.join(out, p))):
                n += 1
                orig = os.path.join(BRAND, p, name)
                if not os.path.exists(orig): print('NOT IN brand/ ', p + '/' + name); ok = False
                elif not filecmp.cmp(orig, os.path.join(out, p, name), shallow=False): print('DIFFERS ', p + '/' + name); ok = False
        print(f'rebuild: {n} files compared with brand/')
    print('OK: the toolchain reproduces the originals exactly.' if ok else 'FAILED: see the lines above.')
    return ok


if __name__ == '__main__':
    a = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = a.add_mutually_exclusive_group(required=True)
    g.add_argument('--check', action='store_true'); g.add_argument('--verify', action='store_true'); g.add_argument('--out')
    args = a.parse_args()
    if args.out:
        if os.path.commonpath([os.path.abspath(args.out), BRAND]) == BRAND: sys.exit('Refusing to write inside brand/: the originals are read-only.')
        rebuild(os.path.abspath(args.out)); print('rebuilt into', args.out)
    else:
        sys.exit(0 if (check() if args.check else verify()) else 1)
