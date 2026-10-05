# D.A. brand toolchain

These are the exact scripts and fonts that produced the locked brand masters in `brand/`. With them, the logo, the seal and the patterns can be rebuilt at any time. The rebuild is identical to the originals, byte for byte.

## Use

```
pip install -r tools/brand/requirements.txt              # fontTools 4.66.1
python tools/brand/build.py --check                      # rebuild in a temp folder; compare with brand/ and its MANIFEST
python tools/brand/build.py --out some/folder            # rebuild every master into some/folder
python tools/brand/build.py --verify                     # only check brand/ against brand/MANIFEST.sha256
```

The script **never writes into `brand/`**:
- `--out` refuses any path inside it.
- The exporters exit unless `build.py` gives them an output folder.

**Last verified:** 2026-10-05, Python 3.11 and fontTools 4.66.1. All 31 files rebuilt identical.

## What is in it

| Path | Content |
|---|---|
| `build.py` | The entry point (see above). |
| `src/export153.py` | Logo 153 → `logo/` |
| `src/export346.py` | Seal 346 → `seal/` |
| `src/export_patterns.py` | Patterns 401, 406, 417 and 420 → `pattern/` |
| `src/marks*.py`, `src/seals*.py`, `src/patterns1.py` | The design modules, copied unchanged from the design rounds. |
| `fonts/` | The exact font files, with their SIL Open Font Licences. See `fonts/SOURCES.md`. |

**What changed when the scripts were copied in:** only the font folder and the output folder are now relative paths, so the toolchain runs from any copy of the repo. Nothing else was changed.

**Why there are so many modules:** each design round built on the last, and the exporters import that chain. The modules are kept unchanged rather than tidied, because tidying could change a decimal place in the output.

**Why there are extra fonts:** some early-round modules load other fonts when they start. Those fonts are included so the scripts run unchanged. No locked design uses them.

## Making new things from the brand

For example a business card, a larger seal or a new pattern colourway:
- write a new script in `src/` that imports these modules;
- write its output outside `brand/`;
- when the owner locks the result, add it to `brand/`, add it to `MANIFEST.sha256` and re-tag.

Never edit the existing exporters in a way that changes their output. Run `build.py --check` before committing.
