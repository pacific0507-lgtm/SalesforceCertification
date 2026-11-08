"""検証済みの過去問(mcadmin/pastq/out_*.json)を、科目 mcadmin(Marketing Cloud Engagement Administrator)の問題集に追加する。
add_pastq_mulepa.py と同じ流れで、問題の番号(id)だけは add_pastq_ipa.py と同じく ids.json で固定する。
  1. 本文に論点がない問題の「add」を、各項目の「過去問で問われた関連知識」に箇条書きで足す(試験ポイントの直前)
  2. 問題を questions.json / qrows.json の末尾に足す(出典 s は「<版> Q<番号>」。例「v2026-03-24 Q12」。英語の原文 qe/oe も持つ)
  3. x(本文の該当箇所)が本文に完全一致するかを確かめる
  4. 同じ問題がほかの回にも出ていたら、解説の最後に「(… でも出題)」と添える。原本が日本語だけの問題は英語の原文(qe/oe)を持たない。skip の問題は入れない
問題の番号は出典 s ごとに <pastq>/ids.json で固定する(過去問を足し直しても、既存の問題の番号がずれて回答履歴が別の問題に付かないように)。
  オリジナル問題の番号(最大値)と重なるときは止まる。
使い方: python3 add_pastq_mcadmin.py <out_*.json のフォルダ> <in_*.json のフォルダ> <data/mcadmin> <出力フォルダ>
  出力フォルダには chapters.json / questions.json / qrows.json を書き、ほかのファイルはそのまま写す。
"""
import glob, html, json, os, re, shutil, sys
outd, ind, src, dst = sys.argv[1:5]
os.makedirs(dst, exist_ok=True)
SUBJ = "mcadmin"
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
warn = 0
def W(*a):
    global warn
    warn += 1; print("警告:", *a)
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
idp = os.path.join(outd, "ids.json")
IDS = json.load(open(idp, encoding="utf-8")) if os.path.exists(idp) else {}
base_max = max(r["data"]["id"] for r in Q if not str(r["data"].get("s", "")).startswith("v"))
if IDS and min(IDS.values()) <= base_max: sys.exit(f"原稿の問題番号(最大 {base_max})と過去問の番号(最小 {min(IDS.values())})が重なっています")
nid = max([base_max] + list(IDS.values())); added = 0
per = {}
for it in items:
    s = f'{it["label"]} Q{it["no"]}'
    if s in have: print("skip(既にあり)", s); continue
    have.add(s)
    o = orig[(it["label"], it["no"])]
    if len(it["o"]) != len(o["oe"]): W("選択肢の数が原文と違う", s); continue
    if it["f"] not in secch: W("項目がない", s, it["f"]); continue
    if not (it["a"] and all(0 <= a < len(it["o"]) for a in it["a"])): W("正解の位置が不正", s); continue
    if not re.match(r"v\d{4}(-\d\d-\d\d)?\s", s): W("出典の先頭が回のラベルでない", s)
    x = it.get("x") or ""; xs = it.get("xs") or ""
    if x and x not in units.get(xs or it["f"], set()): W("該当箇所が本文にない", s, (xs or it["f"]), x[:40])
    if s not in IDS: nid += 1; IDS[s] = nid
    qid = IDS[s]; added += 1; per[it["label"]] = per.get(it["label"], 0) + 1
    ja = o.get("lang") == "ja" and not o.get("qj")
    ex = it["ex"]
    if o.get("also"): ex += "(" + "・".join(f"{a[0]} Q{a[1]}" for a in o["also"]) + " でも出題)"
    d = {"a": sorted(it["a"]), "c": secch[it["f"]] - 1, "ex": ex, "f": "f-" + it["f"], "id": qid, "n": None, "o": it["o"], "oe": [] if ja else o["oe"],
         "q": it["q"], "qe": "" if ja else o["qe"], "s": s, "u": it.get("u"), "v": it["v"], "x": x}
    if xs and xs != it["f"]: d["xs"] = xs
    Q.append({"id": f"q{qid:04d}", "data": d})
    R.append({"id": f"{SUBJ}:q{qid}", "subject_id": SUBJ, "n": qid, "kind": "mc", "source": "past", "exam": s, "text": it["q"],
              "section_id": f"{SUBJ}:{it['f']}", "kq": [], "law": None})
json.dump(dict(sorted(IDS.items(), key=lambda kv: kv[1])), open(idp, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
for n, obj in (("chapters.json", CH), ("questions.json", Q), ("qrows.json", R)):
    json.dump(obj, open(os.path.join(dst, n), "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
for n in os.listdir(src):
    if n not in ("chapters.json", "questions.json", "qrows.json") and os.path.isfile(os.path.join(src, n)):
        shutil.copy(os.path.join(src, n), os.path.join(dst, n))
for k in sorted(per): print(f"  {k}: {per[k]} 問")
print("追加", added, "問 / 関連知識", sum(len(v) for v in by.values()), "件(", len(by), "項目) / 警告", warn)
