"""スマホ向けに描き直した図(spec_*.py)を、各科目の chapters.json の図と差し替える。
使い方: python3 apply.py <d360 chapters.json> <d360 出力> <mcadmin chapters.json> <mcadmin 出力> <index.html> <index 出力>
  - 各項目(data-sec)の最初の <figure class="fig ...">…</figure> を置き換える(本文の「問題 N」の印は表示時に付くので影響なし)
  - index.html には .fig.m の CSS を足す(PCでは大きくなりすぎないよう最大 520px)
"""
import sys, os, re, json, importlib.util
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, here)
import lib
def load(name):
    lib.FIGS.clear(); m = importlib.util.spec_from_file_location(name, os.path.join(here, name + ".py")); mod = importlib.util.module_from_spec(m); m.loader.exec_module(mod)
    return {k: v() for k, v in lib.FIGS.items()}
D = {**load("spec_A"), **load("spec_B")}
M = {**load("spec_C"), **load("spec_D")}
if lib.WARN: sys.exit("警告があります:\n" + "\n".join(lib.WARN))
def apply(src, out, figs):
    ch = json.load(open(src, encoding="utf-8")); done = set()
    for c in ch:
        h = c["data"]["html"]
        for sec, fh in figs.items():
            i = h.find(f'data-sec="{sec}"')
            if i < 0: continue
            j = h.find("<article", i + 10); j = len(h) if j < 0 else j
            m = re.compile(r'<figure class="fig[^"]*"[^>]*>.*?</figure>', re.S).search(h, i, j)
            if not m: sys.exit(f"図が見つからない: {sec}")
            h = h[:m.start()] + fh + h[m.end():]; done.add(sec)
        c["data"]["html"] = h
    miss = set(figs) - done
    if miss: sys.exit(f"差し替えられなかった項目: {miss}")
    json.dump(ch, open(out, "w", encoding="utf-8"), ensure_ascii=False); print(os.path.basename(src), len(done), "図")
a = sys.argv[1:]
apply(a[0], a[1], D); apply(a[2], a[3], M)
s = open(a[4], encoding="utf-8").read()
def jesc(t): return json.dumps(t, ensure_ascii=False)[1:-1].replace("</", "<\\/")
anchor = "body.review .co.talk{display:none}\n"
CSS = "/* スマホ向けの図(横スクロールしない。PCでは最大520px) */\n.fig.m svg{max-width:520px}\n"
if s.count(jesc(anchor)) != 1: sys.exit("CSS の挿入位置が見つからない")
s = s.replace(jesc(anchor), jesc(anchor + CSS))
open(a[5], "w", encoding="utf-8").write(s); print("ok")
