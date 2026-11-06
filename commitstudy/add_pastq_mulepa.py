"""検証済みの過去問(mulepa/pastq/out_*.json)を、科目 mulepa(MuleSoft Platform Architect)の問題集に追加する。
  1. 本文に論点がない問題の「add」を、各項目の「過去問で問われた関連知識」に箇条書きで足す(試験ポイントの直前)
  2. 問題を questions.json / qrows.json の末尾に足す(出典 s は「<版> Q<番号>」。英語の原文 qe/oe も持つ)
  3. x(本文の該当箇所)が本文に完全一致するかを確かめる
  4. 同じ問題がほかの回にも出ていたら、解説の最後に「(… でも出題)」と添える。原本が日本語だけの問題は英語の原文(qe/oe)を持たない。skip の問題は入れない
使い方: python3 add_pastq_mulepa.py <out_*.json のフォルダ> <in_*.json のフォルダ> <data/mulepa> <出力フォルダ>
"""
import glob, html, json, os, re, sys
outd, ind, src, dst = sys.argv[1:5]
os.makedirs(dst, exist_ok=True)
L = lambda n: json.load(open(os.path.join(src, n), encoding="utf-8"))
CH, Q, R = L("chapters.json"), L("questions.json"), L("qrows.json")
orig = {}
for f in glob.glob(os.path.join(ind, "in_*.json")):
    for it in json.load(open(f, encoding="utf-8")): orig[(it["label"], it["no"])] = it
items = []
for f in sorted(glob.glob(os.path.join(outd, "out_*.json"))): items += [it for it in json.load(open(f, encoding="utf-8")) if not it.get("skip")]
secch = {}
for c in CH:
    for sec in re.findall(r'data-sec="([^"]+)"', c["data"]["html"]): secch[sec] = c["data"]["n"]
# 1. 関連知識の追記
by = {}
for it in items:
    a = it.get("add")
    if a and a.get("text"):
        L2 = by.setdefault(it["f"], [])
        if a["text"] not in L2: L2.append(a["text"])
        it["x"] = a["text"]; it.pop("xs", None)
HEAD = '<h4 class="pq-h">過去問で問われた関連知識</h4>'
done = set()
for c in CH:
    def rep(m):
        art, sec = m.group(0), m.group(1)
        if sec not in by: return art
        art = re.sub(re.escape(HEAD) + r'<ul class="pq">.*?</ul>\n?', "", art, flags=re.S)
        block = HEAD + '<ul class="pq">\n' + "".join(f"<li>{html.escape(t, quote=False)}</li>\n" for t in by[sec]) + "</ul>\n"
        for anchor in ('<div class="co memo">', '<div class="done-row">'):
            i = art.rfind(anchor)
            if i >= 0: done.add(sec); return art[:i] + block + art[i:]
        sys.exit("挿入位置なし: " + sec)
    c["data"]["html"] = re.sub(r'<article class="feat" data-sec="([^"]+)".*?</article>', rep, c["data"]["html"], flags=re.S)
if set(by) - done: sys.exit(f"項目が見つからない: {set(by) - done}")
# 本文の単位(該当箇所の照合用)
def plain(h): return html.unescape(re.sub(r"<[^>]+>", "", h)).strip()
units = {}
for c in CH:
    for m in re.finditer(r'<article class="feat" data-sec="([^"]+)".*?</article>', c["data"]["html"], re.S):
        a = re.sub(r"<svg.*?</svg>", "", m.group(0), flags=re.S)
        u = {plain(x[1]) for x in re.findall(r"<(li|p)(?:\s[^>]*)?>(.*?)</\1>", a, re.S)} | {plain(x) for x in re.findall(r"<tr[^>]*>(.*?)</tr>", a, re.S)}
        units[m.group(1)] = u
# 2. 問題を追加
have = {r["data"]["s"] for r in Q}
nid = max(r["data"]["id"] for r in Q); added = 0; warn = 0
for it in items:
    s = f'{it["label"]} Q{it["no"]}'
    if s in have: print("skip(既にあり)", s); continue
    o = orig[(it["label"], it["no"])]
    assert len(it["o"]) == len(o["oe"]), s
    assert it["f"] in secch, (s, it["f"])
    x = it.get("x") or ""; xs = it.get("xs") or ""
    if x and x not in units.get(xs or it["f"], set()): print("警告: 該当箇所が本文にない", s, (xs or it["f"]), x[:40]); warn += 1
    nid += 1; added += 1
    ja = o.get("lang") == "ja" and not o.get("qj")
    ex = it["ex"]
    if o.get("also"): ex += "(" + "・".join(f"{a[0]} Q{a[1]}" for a in o["also"]) + " でも出題)"
    d = {"a": sorted(it["a"]), "c": secch[it["f"]] - 1, "ex": ex, "f": "f-" + it["f"], "id": nid, "n": None, "o": it["o"], "oe": [] if ja else o["oe"],
         "q": it["q"], "qe": "" if ja else o["qe"], "s": s, "u": it.get("u"), "v": it["v"], "x": x}
    if xs and xs != it["f"]: d["xs"] = xs
    Q.append({"id": f"q{nid:04d}", "data": d})
    R.append({"id": f"mulepa:q{nid}", "subject_id": "mulepa", "n": nid, "kind": "mc", "source": "past", "exam": s, "text": it["q"], "section_id": "mulepa:" + it["f"], "kq": [], "law": None})
for n, obj in (("chapters.json", CH), ("questions.json", Q), ("qrows.json", R)):
    json.dump(obj, open(os.path.join(dst, n), "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print("追加", added, "問 / 関連知識", sum(len(v) for v in by.values()), "件(", len(by), "項目) / 警告", warn)
