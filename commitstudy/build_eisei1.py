"""章ごとの原稿(out_ch1.json など)と公表問題(pastq/out.json)から、科目 eisei1(第一種衛生管理者)のデータファイルを組み立てる。
使い方: python3 build_eisei1.py <原稿フォルダ(eisei1/manuscript)> <出力フォルダ(eisei1/data)>
  - 項目の html(図はこのあと figs_m/apply_eisei1.py で chapters.json に入れる)を章ごとの chapters.json にする。plain の項目(取りこぼし注意まとめ)は
    <article class="feat plain"> にして「理解した」と練習問題のリンクを付けない
  - オリジナル問題: 出典 s は「オリジナル(法令・公式資料にもとづく) eisei1-orig-<項目>-NN」。keep のない問題は選択肢を固定の乱数で並べ替える
  - 公表問題(過去問): 出典 s は「令和8年10月公表 問1」(第二種は「令和8年10月公表 第二種 問13」)。選択肢は公表どおりの順(並べ替えない)、正解は公表の正答
    問題の番号(id)は出典ごとに pastq/ids.json で固定する(問題を足しても既存の番号がずれないように)
    公表時期が違う同じ問題は一番新しい回の1問にまとめ、ほかの回の出典を s2、消した問題の番号を al に入れる(番号は ids.json に残す)
  - c(試験科目)は 0〜4(関係法令(有害)/労働衛生(有害)/関係法令(有害以外)/労働衛生(有害以外)/労働生理)。オリジナルは章、過去問は km で決める
  - 法改正の注記(law)は lw に入れる(解説のあとに「法改正の注記」として出す。patch_add_eisei1.py)
  - x(本文の該当箇所)が項目の本文に完全一致するかを確かめる(過去問は x が空なら項目へのリンクだけ)
  - 用語カード: eisei1/terms.json があれば data に入れる
"""
import glob, html, json, os, random, re, sys, time, unicodedata
src, out = sys.argv[1:3]
os.makedirs(out, exist_ok=True)
base = os.path.dirname(os.path.abspath(src))
KM = ["関係法令(有害)", "労働衛生(有害)", "関係法令(有害以外)", "労働衛生(有害以外)", "労働生理"]
DONE_SVG = '<svg aria-hidden="true" viewbox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7.5"></path></svg>'
HOWTO = ('<article class="feat plain" id="f-howto"><h3>このテキストの使い方</h3><p>第一種衛生管理者免許試験の5つの試験科目(関係法令と労働衛生はそれぞれ「有害業務に係るもの」と「有害業務に係るもの以外のもの」、労働生理)に沿って学ぶテキストです。'
         '試験は5肢択一の44問・3時間・400点で、科目ごと(関係法令・労働衛生は範囲ごと)に40%以上、かつ全体で60%以上の得点が合格の基準です。配点と足切り、受験資格、申請のしかた、試験範囲は、Chapter 1 の最初の項目「試験の概要と受け方」にまとめています。'
         '問題集には、法令と公式資料にもとづくオリジナル問題と、安全衛生技術試験協会の公表問題(令和4年4月〜令和8年10月公表の10回分)が入っています。公表問題の正解は公表された正答のとおりで、その後の法改正が関わる問題には「法改正の注記」を付けています。'
         '本文は2026年11月時点で施行されている法令で書いています。わからないところは、各項目の末尾の「AI先生に質問する」で、その項目の本文を踏まえた回答がもらえます。</p><ul><li>本文の文字を選ぶと、マーカー・メモ・質問のボタンが出ます。引いたマーカーは「ノート」にまとまり、「暗記シート」で隠して覚えられます。</li>'
         '<li>各項目の末尾の「この項目の練習問題」から、その項目の問題を解けます。答え合わせのあとの「テキストのこの場所」から本文の該当箇所へ、本文の「問題 N」の印から問題へ移れます。</li>'
         '<li>各章の最後の「取りこぼし注意まとめ」は、足切り(40%)を防ぐための直前の見直し用の一覧です。</li><li>前回読んだ位置としおりは、アカウントに保存されます。</li></ul></article>\n')
chs = {}
for f in sorted(glob.glob(os.path.join(src, "out_ch*.json"))):
    d = json.load(open(f, encoding="utf-8")); n = int(d["chapter"])
    c = chs.setdefault(n, {"title": d["chapter_title"], "sub": d.get("chapter_sub", ""), "sections": []})
    c["sections"] += d["sections"]
def plain(h): return html.unescape(re.sub(r"<[^>]+>", "", h)).strip()
def units_of(h):
    h = re.sub(r"<svg.*?</svg>", "", h, flags=re.S)
    u = {plain(m[1]) for m in re.findall(r"<(li|p)(?:\s[^>]*)?>(.*?)</\1>", h, re.S)}
    return u | {plain(m) for m in re.findall(r"<tr[^>]*>(.*?)</tr>", h, re.S)}
chapters, sections, Q, R = [], [], [], []
qid = 0; order = 0; ts = int(time.time()); warn = 0
UNITS, SECCH, PLAIN = {}, {}, set()
for n in sorted(chs):
    c = chs[n]; secs = c["sections"]
    secs.sort(key=lambda s: int(s["no"].split("·")[1]))
    h = f'<h2 class="chap chtop" id="c{n-1}">Chapter {n} {html.escape(c["title"])}</h2>\n<p class="sub">{html.escape(c["sub"])}</p>\n'
    if n == 1: h += HOWTO
    toc = f'<li class="tc"><a href="#c{n-1}" data-t="c{n-1}">Chapter {n} {html.escape(c["title"])}</a></li>\n' + ('<li><a href="#f-howto" data-t="f-howto">このテキストの使い方</a></li>\n' if n == 1 else "")
    nos, titles, secmap = {}, {}, {}
    for s in secs:
        sid = s["id"]; k = s["no"].split("·")[1]
        head = f'<h3><span class="no">{s["no"]}</span>{html.escape(s["title"])}<span class="tag">{html.escape(s.get("tag",""))}</span></h3>'
        if s.get("plain"):
            if s.get("questions"): sys.exit(f"plain の項目に問題がある: {sid}")
            PLAIN.add(sid)
            h += f'<article class="feat plain" id="f-{sid}">{head}{s["html"]}</article>\n'
            toc += f'<li><a href="#f-{sid}" data-t="f-{sid}"><span class="tn">{s["no"]}</span>{html.escape(s["title"])}</a></li>\n'
            continue
        h += (f'<article class="feat" data-sec="{sid}" id="f-{sid}">{head}'
              f'{s["html"]}<div class="done-row"><button aria-pressed="false" class="donebtn" data-done="{sid}" type="button">{DONE_SVG}<span>理解した</span></button><a class="qlink" data-quiz="{sid}" href="#quiz">この項目の練習問題</a></div></article>\n')
        toc += f'<li><a href="#f-{sid}" data-t="f-{sid}"><span class="tn">{s["no"]}</span>{html.escape(s["title"])}<i class="td" data-d="{sid}" hidden></i></a></li>\n'
        nos[sid] = k; titles[sid] = s["title"]; secmap[sid] = f"{n}.1"
        order += 1
        sections.append({"id": f"eisei1:{sid}", "subject_id": "eisei1", "chapter_id": f"eisei1:ch{n:02d}", "sort_order": order, "title": s["title"], "no": s["no"]})
        UNITS[sid] = units_of(s["html"]); SECCH[sid] = n
        for j, q in enumerate(s.get("questions", []), 1):
            qid += 1
            x = q.get("x") or ""
            if x not in UNITS[sid]: warn += 1; print(f"警告: 該当箇所が本文にない Q{qid} [{sid}] {x[:40]}", file=sys.stderr)
            if len(q["o"]) != 5 or len(q["a"]) != 1: warn += 1; print(f"警告: 5肢択一でない Q{qid} [{sid}]", file=sys.stderr)
            if q.get("keep"):
                opts, ans = list(q["o"]), sorted(q["a"])
            else:
                # 正解の位置が偏らないよう、選択肢を問題ごとに固定の乱数で並べ替える
                perm = list(range(len(q["o"]))); random.Random(f"eisei1-{qid}").shuffle(perm)
                opts = [q["o"][k2] for k2 in perm]; ans = sorted(perm.index(k2) for k2 in q["a"])
            sname = f"オリジナル(法令・公式資料にもとづく) eisei1-orig-{sid}-{j:02d}"
            d = {"a": ans, "c": n - 1, "ex": q["ex"], "f": f"f-{sid}", "id": qid, "n": None, "o": opts, "q": q["q"],
                 "s": sname, "u": q.get("u"), "v": "法令・公式資料にもとづく", "x": x}
            if q.get("law"): d["lw"] = q["law"]
            Q.append({"id": f"q{qid:04d}", "data": d})
            R.append({"id": f"eisei1:q{qid}", "subject_id": "eisei1", "n": qid, "kind": "mc", "source": "orig", "exam": sname, "text": q["q"],
                      "section_id": f"eisei1:{sid}", "kq": [], "law": q.get("law") or None})
    chapters.append({"id": f"ch{n:02d}", "data": {"html": h, "n": n, "nos": nos, "parts": {f"{n}.1": c["title"]}, "secs": secmap, "title": c["title"], "titles": titles, "toc": toc, "ts": ts}})
n_orig = len(Q)
# ---- 公表問題(過去問) ----
pq = os.path.join(base, "pastq")
P = json.load(open(os.path.join(pq, "out.json"), encoding="utf-8"))
idp = os.path.join(pq, "ids.json")
IDS = json.load(open(idp, encoding="utf-8")) if os.path.exists(idp) else {}
if IDS and min(IDS.values()) <= n_orig: sys.exit(f"オリジナル問題の番号(最大 {n_orig})と過去問の番号(最小 {min(IDS.values())})が重なっています")
nid = max([200] + list(IDS.values()))  # 過去問は 201 から(オリジナル問題を足す余地を残す)
seen = set(); nx = 0; nlaw = 0
for p in P:
    s = p["s"]
    if s in seen: sys.exit(f"出典が重複: {s}")
    seen.add(s)
    if s not in IDS: nid += 1; IDS[s] = nid
# ---- 公表時期が違う同じ問題を1問にまとめる ----
# 問題文と選択肢が、全角/半角・空白・句読点の違いと選択肢の順を除いて同じものを同じ問題とみなす(out.json の same と一致することを確かめる)。
# 残すのは一番新しい回の1問(番号 id・出典 s・解説・注記はその問題のもの)。注記・本文の該当箇所・URL がなければ、ほかの回のものを足す。
# ほかの回の出典は s2 に入れ(出題回の絞り込みではどの回にも出る)、まとめて消した問題の番号は al に入れる(ids.json には残して番号を使い回さない。
# アプリは al の番号の回答履歴を残した問題に引き継ぐ。patch_pastq_same.py)
def nk(t): return re.sub(r"[\s、。,.，．・「」()（）:：;；]", "", unicodedata.normalize("NFKC", t))
def rkey(s):
    m = re.match(r"令和(\d+)年(\d+)月公表", s)
    if not m: sys.exit(f"公表回が読めない: {s}")
    return int(m[1]) * 100 + int(m[2])
GRP = {}
for p in P: GRP.setdefault((nk(p["q"]), tuple(sorted(nk(o) for o in p["o"]))), []).append(p)
DROP, MERGE = set(), {}
for g in GRP.values():
    for p in g:
        if sorted(p.get("same") or []) != sorted(x["s"] for x in g if x is not p): sys.exit(f"out.json の same が同じ問題のグループと違う: {p['s']}")
    if len(g) < 2: continue
    g = sorted(g, key=lambda x: (-rkey(x["s"]), x["s"]))
    if rkey(g[0]["s"]) == rkey(g[1]["s"]): sys.exit(f"同じ回に同じ問題: {[x['s'] for x in g]}")
    if len({nk(x["o"][x["a"][0]]) for x in g}) != 1:
        warn += 1; print(f"警告: 同じ問題で正答が違うのでまとめない {[x['s'] for x in g]}", file=sys.stderr); continue
    if len({x["f"] for x in g}) != 1: warn += 1; print(f"警告: 同じ問題で項目が違う {[(x['s'], x['f']) for x in g]}", file=sys.stderr)
    k = dict(g[0])
    for x in g[1:]:
        if not k.get("law") and x.get("law"): k["law"] = x["law"]
        if not k.get("x") and x.get("x") and x["f"] == k["f"]: k["x"] = x["x"]
        if not k.get("u") and x.get("u"): k["u"] = x["u"]
        DROP.add(x["s"])
    k["s2"] = [x["s"] for x in g[1:]]; k["al"] = [IDS[x["s"]] for x in g[1:]]
    MERGE[k["s"]] = k
n_merge = len(MERGE)
for p in P:
    if p["s"] in DROP: continue
    p = MERGE.get(p["s"], p); s = p["s"]
    f = p.get("f") or ""
    if f not in SECCH: sys.exit(f"項目がない: {s} {f!r}")
    if p["km"] not in KM: sys.exit(f"試験科目が不明: {s} {p['km']}")
    if not (len(p["o"]) == 5 and len(p["a"]) == 1 and 0 <= p["a"][0] < 5): sys.exit(f"正解の位置が不正: {s}")
    if SECCH[f] - 1 != KM.index(p["km"]): warn += 1; print(f"警告: 項目の章と試験科目が違う {s} {f} {p['km']}", file=sys.stderr)
    x = p.get("x") or ""
    if x and x not in UNITS[f]: warn += 1; print(f"警告: 該当箇所が本文にない {s} [{f}] {x[:40]}", file=sys.stderr); x = ""
    nx += bool(x)
    q = IDS[s]
    d = {"a": list(p["a"]), "c": KM.index(p["km"]), "ex": p["ex"], "f": "f-" + f, "id": q, "n": None, "o": p["o"], "q": p["q"],
         "s": s, "u": p.get("u") or None, "v": p.get("v") or "公表問題", "x": x}
    if p.get("law"): d["lw"] = p["law"]; nlaw += 1
    if p.get("s2"): d["s2"] = p["s2"]; d["al"] = p["al"]
    Q.append({"id": f"q{q:04d}", "data": d})
    r = {"id": f"eisei1:q{q}", "subject_id": "eisei1", "n": q, "kind": "mc", "source": "past", "exam": s, "text": p["q"],
         "section_id": f"eisei1:{f}", "kq": [], "law": p.get("law") or None}
    if p.get("s2"): r["s2"] = p["s2"]; r["al"] = p["al"]
    R.append(r)
json.dump(dict(sorted(IDS.items(), key=lambda kv: kv[1])), open(idp, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
W = lambda name, obj: json.dump(obj, open(os.path.join(out, name), "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
W("chapters.json", chapters); W("sections.json", sections); W("questions.json", Q); W("qrows.json", R)
for name, v in (("mcq.json", []), ("numcards.json", []), ("presets.json", []), ("traps.json", {})): W(name, v)
tp = os.path.join(base, "terms.json")
T = json.load(open(tp, encoding="utf-8")) if os.path.exists(tp) else []
if T: W("terms.json", T)
print("chapters", len(chapters), "sections", len(sections) + len(PLAIN), f"(plain {len(PLAIN)})", "orig", n_orig, "past", len(Q) - n_orig,
      f"(公表 {len(P)} 問のうち同じ問題 {n_merge} 組をまとめて {len(DROP)} 問減)",
      f"(x {nx} / law {nlaw})", "terms", len(T), "warn", warn)
