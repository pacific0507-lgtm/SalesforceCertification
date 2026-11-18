"""章ごとの原稿(out_ch1.json など)から、科目 afsvc(Agentforce Service コンサルタント)のデータファイルを組み立てる。
使い方: python3 build_afsvc.py <原稿フォルダ> <出力フォルダ(data/afsvc)>
"""
import glob, html, json, os, random, re, sys, time
src, out = sys.argv[1:3]
os.makedirs(out, exist_ok=True)
# 項目 → 出題範囲(試験ガイドの8分野: 業界知識/導入戦略/ソリューション設計/ナレッジ管理/受付・対話チャネル/ケース管理/コンタクトセンター分析/インテグレーション)
CXS = {"kpi": 0, "outcome": 0, "engage": 1, "deploy": 1, "datamig": 1, "console": 2, "cx": 2, "security": 2, "knowledge": 3, "kcs": 3,
       "intake": 4, "routing": 4, "messaging": 4, "agents": 4, "caseproc": 5, "deflect": 5, "entitle": 5, "automation": 5,
       "reports": 6, "analytics": 6, "integ": 7, "slack": 7}
DONE_SVG = '<svg aria-hidden="true" viewbox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7.5"></path></svg>'
HOWTO = ('<article class="feat plain" id="f-howto"><h3>このテキストの使い方</h3><p>Agentforce Service コンサルタント(旧 Service Cloud コンサルタント)認定試験の出題範囲(業界知識・導入戦略・ソリューション設計・ナレッジ管理・受付と対話のチャネル・ケース管理・コンタクトセンター分析・インテグレーション)に沿って学ぶテキストです。問題は4択です。'
         '試験は採点対象60問(ほかに採点対象外が最大5問)・105分・合格ライン78%で、前提資格は Platform アドミニストレーターです。'
         'わからないところは、各項目の末尾の「AI先生に質問する」で、その項目の本文を踏まえた回答がもらえます。</p><ul><li>本文の文字を選ぶと、マーカー・メモ・質問のボタンが出ます。引いたマーカーは「ノート」にまとまり、「暗記シート」で隠して覚えられます。</li>'
         '<li>各項目の末尾の「この項目の練習問題」から、その項目の問題を解けます。答え合わせのあとの「テキストのこの場所」から本文の該当箇所へ、本文の「問題 N」の印から問題へ移れます。</li><li>前回読んだ位置としおりは、アカウントに保存されます。</li></ul></article>\n')
chs = {}
for f in sorted(glob.glob(os.path.join(src, "out_ch*.json"))):
    d = json.load(open(f, encoding="utf-8")); n = int(d["chapter"])
    c = chs.setdefault(n, {"title": d["chapter_title"], "sub": d.get("chapter_sub", ""), "sections": []})
    c["sections"] += d["sections"]
def plain(h): return html.unescape(re.sub(r"<[^>]+>", "", h)).strip()
chapters, sections, Q, R = [], [], [], []
qid = 0; order = 0; ts = int(time.time())
for n in sorted(chs):
    c = chs[n]; secs = c["sections"]
    secs.sort(key=lambda s: int(s["no"].split("·")[1]))
    h = f'<h2 class="chap chtop" id="c{n-1}">Chapter {n} {html.escape(c["title"])}</h2>\n<p class="sub">{html.escape(c["sub"])}</p>\n'
    if n == 1: h += HOWTO
    toc = f'<li class="tc"><a href="#c{n-1}" data-t="c{n-1}">Chapter {n} {html.escape(c["title"])}</a></li>\n' + ('<li><a href="#f-howto" data-t="f-howto">このテキストの使い方</a></li>\n' if n == 1 else "")
    nos, titles, secmap = {}, {}, {}
    for s in secs:
        sid = s["id"]; k = s["no"].split("·")[1]
        h += (f'<article class="feat" data-sec="{sid}" id="f-{sid}"><h3><span class="no">{s["no"]}</span>{html.escape(s["title"])}<span class="tag">{html.escape(s.get("tag",""))}</span></h3>'
              f'{s["html"]}<div class="done-row"><button aria-pressed="false" class="donebtn" data-done="{sid}" type="button">{DONE_SVG}<span>理解した</span></button><a class="qlink" data-quiz="{sid}" href="#quiz">この項目の練習問題</a></div></article>\n')
        toc += f'<li><a href="#f-{sid}" data-t="f-{sid}"><span class="tn">{s["no"]}</span>{html.escape(s["title"])}<i class="td" data-d="{sid}" hidden></i></a></li>\n'
        nos[sid] = k; titles[sid] = s["title"]; secmap[sid] = f"{n}.1"
        order += 1
        sections.append({"id": f"afsvc:{sid}", "subject_id": "afsvc", "chapter_id": f"afsvc:ch{n:02d}", "sort_order": order, "title": s["title"], "no": s["no"]})
        units = {plain(m[1]) for m in re.findall(r"<(li|p)(?:\s[^>]*)?>(.*?)</\1>", re.sub(r"<svg.*?</svg>", "", s["html"], flags=re.S), re.S)}
        units |= {plain(m) for m in re.findall(r"<tr[^>]*>(.*?)</tr>", s["html"], re.S)}
        for q in s.get("questions", []):
            qid += 1
            x = q.get("x") or ""
            if x not in units: print(f"警告: 該当箇所が本文にない Q{qid} [{sid}] {x[:40]}", file=sys.stderr)
            # 正解の位置が偏らないよう、選択肢を問題ごとに固定の乱数で並べ替える
            perm = list(range(len(q["o"]))); random.Random(f"afsvc-{qid}").shuffle(perm)
            opts = [q["o"][k] for k in perm]; ans = sorted(perm.index(k) for k in q["a"])
            d = {"a": ans, "c": CXS[sid], "ex": q["ex"], "f": f"f-{sid}", "id": qid, "n": None, "o": opts, "q": q["q"],
                 "s": "オリジナル(公式ヘルプにもとづく)", "u": q.get("u"), "v": "公式ヘルプにもとづく", "x": x}
            Q.append({"id": f"q{qid:04d}", "data": d})
            R.append({"id": f"afsvc:q{qid}", "subject_id": "afsvc", "n": qid, "kind": "mc", "source": "orig", "exam": d["s"], "text": q["q"], "section_id": f"afsvc:{sid}", "kq": [], "law": None})
    chapters.append({"id": f"ch{n:02d}", "data": {"html": h, "n": n, "nos": nos, "parts": {f"{n}.1": c["title"]}, "secs": secmap, "title": c["title"], "titles": titles, "toc": toc, "ts": ts}})
W = lambda name, obj: json.dump(obj, open(os.path.join(out, name), "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
W("chapters.json", chapters); W("sections.json", sections); W("questions.json", Q); W("qrows.json", R)
for name, v in (("mcq.json", []), ("numcards.json", []), ("presets.json", []), ("traps.json", {})): W(name, v)
# 用語カード: 原稿フォルダの隣の terms.json(afsvc/terms.json)があれば、そのまま data に入れる
tp = os.path.join(os.path.dirname(os.path.abspath(src)), "terms.json")
T = json.load(open(tp, encoding="utf-8")) if os.path.exists(tp) else []
if T: W("terms.json", T)
print("chapters", len(chapters), "sections", len(sections), "questions", len(Q), "terms", len(T))
