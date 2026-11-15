"""実際の Salesforce の画面(screens/raw/<科目>/*.png)を切り出し・赤枠を付けて webp にし、テキスト(<科目>/data/chapters.json)の項目に差し込む。
  - 画像: <科目>/data/img/scr_<元の名前>.webp(横は最大1200px。表示はスマホの幅に合わせ、押すと拡大)
  - 差し込む場所: その項目(article.feat[data-sec])の「試験ポイント」の直前に「実際の画面」のまとまり(div.scr-g)として入れる
  - 何度実行しても同じ結果になる(先に div.scr-g を取り除いてから入れ直す)
  - 表示の CSS・拡大・画像の URL は patch_scr.py(rebuild.sh)
使い方: python3 screens/apply_screens.py d360
"""
import html, json, os, re, sys
from PIL import Image, ImageDraw
subj = sys.argv[1]
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.join(here, "..")
RAW = os.path.join(here, "raw", subj); IMG = os.path.join(root, subj, "data", "img"); CH = os.path.join(root, subj, "data", "chapters.json")
SPEC = json.load(open(os.path.join(here, f"spec_{subj}.json"), encoding="utf-8"))
SHOT = "Salesforce Developer Edition(日本語表示)・2026年11月撮影"
os.makedirs(IMG, exist_ok=True)
by_sec = {}
for it in SPEC:
    im = Image.open(os.path.join(RAW, it["file"])).convert("RGB")
    x0, y0, x1, y1 = it.get("crop") or (0, 0, im.width, im.height)
    im = im.crop((x0, y0, x1, y1))
    d = ImageDraw.Draw(im)
    lw = max(4, im.width // 260)
    for i, b in enumerate(it.get("boxes", [])):
        bx = (b[0] - x0, b[1] - y0, b[2] - x0, b[3] - y0)
        d.rounded_rectangle(bx, radius=10, outline=(230, 30, 40), width=lw)
    if im.width > 1200: im = im.resize((1200, round(im.height * 1200 / im.width)), Image.LANCZOS)
    name = "scr_" + os.path.splitext(it["file"])[0] + ".webp"
    im.save(os.path.join(IMG, name), "WEBP", quality=82, method=6)
    by_sec.setdefault(it["sec"], []).append((name, im.width, im.height, it))
C = json.load(open(CH, encoding="utf-8"))
done = set()
for c in C:
    h = c["data"]["html"]
    h = re.sub(r'<div class="scr-g">.*?</div><!--/scr-g-->', "", h, flags=re.S)
    for sec, items in by_sec.items():
        m = re.search(r'<article class="feat" data-sec="' + re.escape(sec) + r'".*?</article>', h, re.S)
        if not m: continue
        art = m.group(0)
        figs = "".join(
            f'<figure class="scr"><button type="button" class="scr-z" aria-label="画面を拡大する"><img data-scr="data/{subj}/img/{n}" alt="{html.escape(it["alt"])}" width="{w}" height="{hh}" loading="lazy"></button>'
            f'<figcaption><b>{html.escape(it["title"])}</b>{html.escape(it.get("cap", ""))}</figcaption></figure>'
            for n, w, hh, it in items)
        blk = f'<div class="scr-g"><h4 class="scr-h">実際の画面</h4>{figs}<p class="scr-src">{SHOT}。画面は更新で変わることがあります。押すと拡大します。</p></div><!--/scr-g-->'
        k = art.find('<div class="co memo"><p><b class="lab">試験ポイント</b>')
        art2 = art[:k] + blk + art[k:] if k >= 0 else art.replace("</article>", blk + "</article>")
        h = h.replace(art, art2); done.add(sec)
    c["data"]["html"] = h
missing = set(by_sec) - done
if missing: sys.exit("項目が見つからない: " + ", ".join(sorted(missing)))
json.dump(C, open(CH, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print(f"{subj}: {sum(len(v) for v in by_sec.values())} 枚を {len(by_sec)} 項目に入れた")
