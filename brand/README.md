# D.A. Accounting & Consulting: brand assets

**Status:** locked by the owner on 2026-10-05. Everything in this folder is an **original master**. It is read-only.

**D A:** the letters are **Diamond** and **Atom**, the two founders.

## What is here

| Piece | Master files | Spec (how to use it, exact numbers) | Picture record |
|---|---|---|---|
| **Logo 153** | `logo/` | `docs/brand/da-logo-153.md` | `reference/logo.png` |
| **Brand seal 346** | `seal/` | `docs/brand/da-seal-346.md` | `reference/seal.png` |
| **Patterns 401 · 406 · 417 · 420** | `pattern/` | `docs/brand/da-patterns.md` | `reference/patterns.png` |

**Colours:** the logo spec §2 is the single source for the colours.

| | Hex |
|---|---|
| Paper | `#F2EEEA` |
| Oxblood | `#7A2229` |
| Night | `#1B1112` |
| Rose (paper / oxblood / night) | `#B07E80` / `#C29998` / `#BE9491` |
| Silver (paper / dark) | `#D4D5D8` / `#85878C` |

**What each element means:** the owner's definitions are in the logo spec §1.

The decision trail (every round, and every owner decision) is in `docs/decisions/36-generated-imagery.md`.

## Rules that never change

- D A is always the full logo 153. Never strip its detail.
- The seal has no "CO., LTD." and no year. It is English only. There is no rubber-stamp version.
- Never redraw, recolour, stretch or rotate anything here by hand. Use the master files as they are.
- Need a new size or format? Rebuild it with `tools/brand/` into a folder outside `brand/`.

## Proof that nothing has changed

- **`MANIFEST.sha256`:** the fingerprint (SHA-256) of every file in this folder.
- **Frozen snapshot: branch `brand-v1.0` on GitHub.** It holds this exact version of the brand. Never commit to it: it stays as the reference copy. (It replaces a git tag, which the cloud session could not push.)
- **Where it lives:** these originals are merged into `main`, the repository's main line.
- **Checking:**
  - Check the fingerprints: `python tools/brand/build.py --verify`.
  - Rebuild everything and compare it byte for byte: `python tools/brand/build.py --check`.
  - On Linux or macOS, `sha256sum -c MANIFEST.sha256` run inside `brand/` does the same as `--verify`.
- **`.gitattributes`:** stops git changing the line endings of these files (for example on Windows), so the fingerprints always match.
