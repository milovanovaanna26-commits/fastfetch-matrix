import os, random, subprocess
from PIL import Image

PATH = "/home/anya/Изображения/matrix-cat.png"
W = 64          # ширина логотипа в символах (больше = крупнее)
ASPECT = 0.44   # пропорции символа терминала
THRESH = 0.14   # порог яркости: больше = кот толще и тёмнее
GAP = 3         # отступ между картинкой и текстом

img = Image.open(PATH).convert("RGB")
w, h = img.size
H = int(W * h / w * ASPECT)
img = img.resize((W, H), Image.LANCZOS)

chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
random.seed(7)
logo = []
for y in range(H):
    line = ""
    for x in range(W):
        v = img.getpixel((x, y))[1] / 255
        if v > THRESH:
            g = int(90 + 165 * min(1, v * 2))
            line += f"\x1b[38;2;0;{g};0m{random.choice(chars)}"
        else:
            line += " "
    logo.append(line + "\x1b[0m")

info = subprocess.run(
    ["fastfetch", "--logo", "none", "--pipe", "false"],
    capture_output=True, text=True
).stdout.rstrip("\n").split("\n")

top = max(0, (len(logo) - len(info)) // 2)   # центрируем текст по высоте
info = [""] * top + info

out = []
for i in range(max(len(logo), len(info))):
    l = logo[i] if i < len(logo) else " " * W
    t = info[i] if i < len(info) else ""
    out.append(l + " " * GAP + t)
print("\n".join(out))
