"""画面写真に、説明している箇所の赤枠を描く。python3 draw.py <png フォルダ> <出力 webp フォルダ>"""
import json, os, sys
from PIL import Image, ImageDraw
src, dst = sys.argv[1:3]; os.makedirs(dst, exist_ok=True)
R = json.load(open(os.path.join(src, "rects.json")))
SC = 2; W, H = 390, 780
for n, rects in R.items():
    im = Image.open(os.path.join(src, n + ".png")).convert("RGB"); d = ImageDraw.Draw(im)
    for r in rects:
        if not r: continue
        x0, y0 = max(3, r["x"] - 5), max(3, r["y"] - 5); x1, y1 = min(W - 3, r["r"] + 5), min(H - 3, r["b"] + 5)
        d.rounded_rectangle([x0 * SC, y0 * SC, x1 * SC, y1 * SC], radius=12 * SC, outline=(229, 57, 53), width=3 * SC)
    im.resize((540, 1080), Image.LANCZOS).save(os.path.join(dst, n + ".webp"), "WEBP", quality=72, method=6)
print("ok", len(R))
