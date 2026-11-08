"""IPA の公開問題・サンプル問題(<科目>/pastq/*.json)を、科目 fe(基本情報技術者)・sg(情報セキュリティマネジメント)の問題集に追加する。
  1. 本文に論点がない問題の「add」を、各項目の「過去問で問われた関連知識」に箇条書きで足す(試験ポイントの直前)
  2. 問題を questions.json / qrows.json の末尾に足す(出典 s は「令和8年度 基本情報技術者試験 公開問題 科目A 問1」や
     「基本情報技術者試験 科目A試験 サンプル問題セット 問1」。正解 a は IPA の解答例のとおり)
  3. x(本文の該当箇所)が本文に完全一致するか、f(項目)・a(正解の位置)が正しいかを確かめる
  "skip" の問題(図が前提で文章にできないもの、重複)は入れない。同じ出典 s が既にあれば入れない。
pastq/*.json の各問: {set, no, s, u, q, o, a:[正解index], f, x, xs(任意), add(任意), ex, v} または {set, no, s, skip:理由}
図を画像で出す問題は、問題文に「〔図:ファイル名〕代替テキスト」の行を書き(書式は qfmt.js)、画像を <pastq>/img/ に置く。
  画像は出力フォルダの img/ に写す(公開先では data/<科目>/img/)。問題文が指す画像がなければ警告。
使い方: python3 add_pastq_ipa.py <pastq のフォルダ> <ビルド済みのデータのフォルダ> <出力フォルダ>
  出力フォルダには chapters.json / questions.json / qrows.json を書き、ほかのファイルはそのまま写す。
"""
import glob, html, json, os, re, shutil, sys
pqd, src, dst = sys.argv[1:4]
os.makedirs(dst, exist_ok=True)
L = lambda n: json.load(open(os.path.join(src, n), encoding="utf-8"))
CH, Q, R = L("chapters.json"), L("questions.json"), L("qrows.json")
SUBJ = R[0]["subject_id"]
items, skipped = [], []
for f in sorted(glob.glob(os.path.join(pqd, "*.json"))):
    for it in json.load(open(f, encoding="utf-8")):
        (skipped if it.get("skip") else items).append(it)
secch = {}
for c in CH:
    for sec in re.findall(r'data-sec="([^"]+)"', c["data"]["html"]): secch[sec] = c["data"]["n"]
warn = 0
def W(*a):
    global warn
    warn += 1; print("警告:", *a)
# 1. 関連知識の追記
by = {}
for it in items:
    a = it.get("add")
    if a:
        L2 = by.setdefault(it["f"], [])
        if a not in L2: L2.append(a)
        it["x"] = a; it.pop("xs", None)
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
nid = max(r["data"]["id"] for r in Q); added = 0
per = {}
used_img = {fn for it in items for fn in re.findall(r"^〔図:([^〕]+)〕", it["q"], re.M)}
for it in items:
    s = it["s"]
    if s in have: print("skip(既にあり)", s); continue
    have.add(s)
    f = it["f"]
    if f not in secch: W("項目がない", s, f); continue
    if not (len(it["o"]) >= 2 and it["a"] and all(0 <= a < len(it["o"]) for a in it["a"])): W("正解の位置が不正", s); continue
    if len(it["o"]) > 10: W("選択肢が10を超える", s)
    x = it.get("x") or ""; xs = it.get("xs") or ""
    if not x: W("該当箇所 x がない", s)
    elif x not in units.get(xs or f, set()): W("該当箇所が本文にない", s, xs or f, x[:40])
    if xs and xs not in secch: W("xs の項目がない", s, xs)
    for fn in re.findall(r"^〔図:([^〕]+)〕", it["q"], re.M):
        if not re.fullmatch(r"[A-Za-z0-9_.\-]+", fn) or not os.path.isfile(os.path.join(pqd, "img", fn)): W("画像がない", s, fn)
    nid += 1; added += 1; per[it["set"]] = per.get(it["set"], 0) + 1
    d = {"a": sorted(it["a"]), "c": secch[f] - 1, "ex": it["ex"], "f": "f-" + f, "id": nid, "n": None, "o": it["o"],
         "q": it["q"], "s": s, "u": it.get("u"), "v": it["v"], "x": x}
    if xs and xs != f: d["xs"] = xs
    Q.append({"id": f"q{nid:04d}", "data": d})
    R.append({"id": f"{SUBJ}:q{nid}", "subject_id": SUBJ, "n": nid, "kind": "mc", "source": "past", "exam": s, "text": it["q"],
              "section_id": f"{SUBJ}:{f}", "kq": [], "law": None})
for n, obj in (("chapters.json", CH), ("questions.json", Q), ("qrows.json", R)):
    json.dump(obj, open(os.path.join(dst, n), "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
for n in os.listdir(src):
    if n not in ("chapters.json", "questions.json", "qrows.json") and os.path.isfile(os.path.join(src, n)):
        shutil.copy(os.path.join(src, n), os.path.join(dst, n))
imgd = os.path.join(pqd, "img")
if os.path.isdir(imgd):
    od = os.path.join(dst, "img"); os.makedirs(od, exist_ok=True)
    for n in set(os.listdir(od)) - set(os.listdir(imgd)): os.remove(os.path.join(od, n))  # 使わなくなった画像を消す
    for n in sorted(os.listdir(imgd)):
        if n not in used_img: W("使っていない画像", n)
        shutil.copy(os.path.join(imgd, n), os.path.join(od, n))
for k in sorted(per): print(f"  {k}: {per[k]} 問")
print("追加", added, "問 / 収録しない", len(skipped), "問 / 関連知識", sum(len(v) for v in by.values()), "件(", len(by), "項目) / 警告", warn)
