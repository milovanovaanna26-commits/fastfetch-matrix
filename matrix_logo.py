import sys, os, re, random
from PIL import Image

path = sys.argv[1]
invert = len(sys.argv) > 2 and sys.argv[2] == "invert"
W = 40          # ширина в символах
THRESH = 0.14   # порог яркости: больше = кот толще и тёмнее

img = Image.open(path).convert("RGB")
w, h = img.size
H = int(W * h / w * 0.5)   # 0.5 из-за того, что символы вдвое выше, чем шире
img = img.resize((W, H), Image.LANCZOS)

chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
random.seed(7)
lines = []
for y in range(H):
    line = ""
    for x in range(W):
        v = img.getpixel((x, y))[1] / 255
        lit = v > THRESH
        if invert:
            lit = not lit
        if lit:
            g = int(90 + 165 * min(1, v * 2))
            line += f"\x1b[38;2;0;{g};0m{random.choice(chars)}"
        else:
            line += " "
    lines.append(line + "\x1b[0m")

base = os.path.expanduser("~/.config/fastfetch/")
open(base + "logo.ansi", "w", encoding="utf-8").write("\n".join(lines) + "\n")

cfg = base + "config.jsonc"
s = open(cfg, encoding="utf-8").read()
s = re.sub(r'"width":\s*\d+', f'"width": {W}', s, count=1)
s = re.sub(r'"height":\s*\d+', f'"height": {H}', s, count=1)
open(cfg, "w", encoding="utf-8").write(s)
print("готово:", W, "x", H)
