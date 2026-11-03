"""本文・問題・用語カードに英語のまま書いていた機能名などを、公式の日本語UIの名称にそろえる(科目 afsales)。
使い方: python3 apply_jaui.py <glossary.json> <data/afsales> <出力フォルダ>
  - 置き換えるのは日本語の文だけ(本文の文字、問題の q/o/ex/x、用語カードの t/d)。英語の原文(qe/oe)と、見出しの英語タグ(.tag)、図(svg)は変えない
    (図は figs_m/spec_*.py を直して作り直す)
  - 「日本語名(英語名)」と併記していたところは「日本語名(英語名)」のまま残す
  - 用語カードの表が英語名だけだったときは「日本語名(英語名)」にする
  - 置き換え後、問題の該当箇所 x が本文と一致するか確かめ、一致しなくなったものは本文側の文字列に合わせる
"""
import html, json, os, re, sys
gp, src, dst = sys.argv[1:4]
G = json.load(open(gp, encoding="utf-8"))["replace"]
G = sorted(G, key=lambda r: -len(r["en"]))
os.makedirs(dst, exist_ok=True)
def rx(en): return re.compile(r"(?<![A-Za-z0-9])" + re.escape(en) + r"(?![A-Za-z0-9])")
RX = [(rx(r["en"]), r["en"], r["ja"]) for r in G]
cnt = {}
def conv(t):
    if not t: return t
    # 併記の英語部分を一時的に守る: 「…(English)」の English
    keep = {}
    def protect(m):
        k = f"\u0000{len(keep)}\u0000"; keep[k] = m.group(0); return k
    for r, en, ja in RX:
        t = re.sub(r"[((]" + re.escape(en) + r"[))]", protect, t)
    for r, en, ja in RX:
        t, n = r.subn(ja, t)
        if n: cnt[en] = cnt.get(en, 0) + n
    for k, v in keep.items(): t = t.replace(k, v)
    return t
L = lambda n: json.load(open(os.path.join(src, n), encoding="utf-8"))
CH, Q, T = L("chapters.json"), L("questions.json"), L("terms.json")
# 本文: タグの外の文字だけ。svg と見出しの英語タグ(span.tag)は除く
def conv_html(h):
    parts = re.split(r"(<svg.*?</svg>|<span class=\"tag\">.*?</span>|<[^>]+>)", h, flags=re.S)
    return "".join(p if (i % 2 == 1) else conv(p) for i, p in enumerate(parts))
for c in CH:
    c["data"]["html"] = conv_html(c["data"]["html"])
    c["data"]["titles"] = {k: conv(v) for k, v in c["data"]["titles"].items()}
    c["data"]["toc"] = conv_html(c["data"]["toc"])
for r in Q:
    d = r["data"]
    for k in ("q", "ex", "x"): d[k] = conv(d.get(k))
    d["o"] = [conv(o) for o in d["o"]]
EN2JA = {r["en"]: r["ja"] for r in G}
for t in T:
    t["t"] = f'{EN2JA[t["t"]]}({t["t"]})' if t["t"] in EN2JA else conv(t["t"])
    t["d"] = conv(t["d"])
# 該当箇所の照合
def plain(h): return html.unescape(re.sub(r"<[^>]+>", "", h)).strip()
units = {}
for c in CH:
    for m in re.finditer(r'<article class="feat" data-sec="([^"]+)".*?</article>', c["data"]["html"], re.S):
        a = re.sub(r"<svg.*?</svg>", "", m.group(0), flags=re.S)
        units[m.group(1)] = {plain(x[1]) for x in re.findall(r"<(li|p)(?:\s[^>]*)?>(.*?)</\1>", a, re.S)} | {plain(x) for x in re.findall(r"<tr[^>]*>(.*?)</tr>", a, re.S)}
bad = 0
for r in Q:
    d = r["data"]; x = d.get("x")
    if not x: continue
    sec = d.get("xs") or d["f"][2:]
    if x not in units.get(sec, set()): bad += 1; print("該当箇所が一致しない:", d["s"], sec, x[:50])
R = L("qrows.json")
qtext = {r["id"]: r["data"]["q"] for r in Q}
for r in R:
    n = r["n"]; k = f"q{n:04d}"
    if k in qtext: r["text"] = qtext[k]
S = L("sections.json")
for s in S: s["title"] = conv(s["title"])
for n, obj in (("chapters.json", CH), ("questions.json", Q), ("terms.json", T), ("sections.json", S), ("qrows.json", R)):
    json.dump(obj, open(os.path.join(dst, n), "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print("置き換え", sum(cnt.values()), "か所 /", len(cnt), "語 / 該当箇所の不一致", bad)
for en, n in sorted(cnt.items(), key=lambda x: -x[1]): print(f"  {n:4d}  {en} → {EN2JA[en]}")
# 図の元(figs_m/spec_E〜G.py)の文字列にも同じ置き換えを当てる(--figs を付けたとき)
if "--figs" in sys.argv:
    here = os.path.dirname(os.path.abspath(__file__))
    for n in ("spec_E.py", "spec_F.py", "spec_G.py"):
        p = os.path.join(here, "figs_m", n); t = open(p, encoding="utf-8").read()
        t2 = re.sub(r'"([^"\\n]*)"', lambda m: '"' + conv(m.group(1)) + '"', t)
        if t2 != t: open(p, "w", encoding="utf-8").write(t2); print("図の元を更新:", n)
