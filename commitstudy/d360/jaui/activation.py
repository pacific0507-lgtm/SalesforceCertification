"""Data 360 の「アクティベーション」を、日本語UIの名称「有効化」にそろえる(Activation Target は「有効化対象」)。
使い方: python3 activation.py <data/d360> <出力フォルダ>   (図の元 figs_m/spec_A.py・spec_B.py も直す)
"""
import json, os, re, sys
src, dst = sys.argv[1:3]; os.makedirs(dst, exist_ok=True)
def conv(t):
    if not t: return t
    t = t.replace("アクティベーションとターゲット", "有効化と有効化対象")
    t = t.replace("アクティベーションターゲット", "有効化対象")
    return t.replace("アクティベーション", "有効化")
L = lambda n: json.load(open(os.path.join(src, n), encoding="utf-8"))
CH, Q, R, T, S = L("chapters.json"), L("questions.json"), L("qrows.json"), L("terms.json"), L("sections.json")
for c in CH:
    c["data"]["html"] = conv(c["data"]["html"]); c["data"]["toc"] = conv(c["data"]["toc"])
    c["data"]["titles"] = {k: conv(v) for k, v in c["data"]["titles"].items()}
    if "parts" in c["data"]: c["data"]["parts"] = {k: conv(v) for k, v in c["data"]["parts"].items()}
for r in Q:
    d = r["data"]
    for k in ("q", "ex", "x"): d[k] = conv(d.get(k))
    d["o"] = [conv(o) for o in d["o"]]
for r in R: r["text"] = conv(r["text"])
for t in T: t["t"] = conv(t["t"]); t["d"] = conv(t["d"])
for s in S: s["title"] = conv(s["title"])
for n, o in (("chapters.json", CH), ("questions.json", Q), ("qrows.json", R), ("terms.json", T), ("sections.json", S)):
    json.dump(o, open(os.path.join(dst, n), "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
here = os.path.dirname(os.path.abspath(__file__))
for n in ("spec_A.py", "spec_B.py"):
    p = os.path.join(here, "..", "..", "figs_m", n); t = open(p, encoding="utf-8").read(); t2 = conv(t)
    if t2 != t: open(p, "w", encoding="utf-8").write(t2); print("図の元を更新:", n)
print("ok")
