# fastfetch-matrix

Fastfetch config with a green Matrix cat logo.

## Install

```bash
git clone https://github.com/milovanovaanna26-commits/fastfetch-matrix ~/.config/fastfetch
fastfetch
```

## Files

- `config.jsonc` — fastfetch config, uses `logo.ansi` as the logo
- `logo.ansi` — ready-made logo
- `matrix-cat.png` — source image
- `matrix_logo.py` — regenerates `logo.ansi` from an image: `python3 matrix_logo.py matrix-cat.png [invert]`
- `matrix_fetch.py` — bigger logo variant printed next to fastfetch output (needs Pillow)
