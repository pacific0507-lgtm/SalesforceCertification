"""仕様書ページ(/spec/)を追加する。使い方(利用者向け)とは別に、エンジニア向けにアプリの作りを図と表でまとめる。
  - メニューのサイトマップの「使い方」の下に「仕様書」を足す
  - 科目ごとの問題数・用語カードの枚数は、作るときに <科目>/data から数える。パッチの数は rebuild.sh から数える
使い方: python3 patch_spec.py <index.html> <出力>   (同じフォルダの spec_figs.py と ../figs_m/lib.py を使う)
"""
import collections, json, os, re, sys, importlib.util
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.join(here, "..")
sys.path.insert(0, os.path.join(root, "figs_m")); import lib
lib.FIGS.clear()
m = importlib.util.spec_from_file_location("spec_figs", os.path.join(here, "spec_figs.py")); mod = importlib.util.module_from_spec(m); m.loader.exec_module(mod)
FIG = {k: v() for k, v in lib.FIGS.items()}
if lib.WARN: sys.exit("\n".join(lib.WARN))
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count: sys.exit(f"置換対象が {n} 件(期待 {count} 件): {old[:90]!r}")
    s = s.replace(old, new)

SUBJ = [("d360", "Data 360 コンサルタント"), ("mcadmin", "Marketing Cloud Engagement Administrator"), ("afsales", "Agentforce Sales コンサルタント"),
        ("afspec", "Agentforce スペシャリスト"), ("mulepa", "MuleSoft Platform Architect"), ("fe", "基本情報技術者"), ("sg", "情報セキュリティマネジメント")]
rows = []
for sid, name in SUBJ:
    R = json.load(open(os.path.join(root, sid, "data", "qrows.json"), encoding="utf-8"))
    c = collections.Counter(r.get("source") for r in R)
    tn = len(json.load(open(os.path.join(root, sid, "data", "terms.json"), encoding="utf-8")))
    rows.append((f"{name}<br><code>{sid}</code>", c.get("past", 0) or "—", c.get("th", 0) or "—", c.get("orig", 0) or "—", len(R), tn))
NPATCH = sum(1 for l in open(os.path.join(root, "rebuild.sh"), encoding="utf-8") if l.startswith("python3 "))

def T(head, body, cls=""):
    h = "".join(f"<th>{x}</th>" for x in head)
    b = "".join("<tr>" + "".join(f"<td>{x}</td>" for x in r) + "</tr>" for r in body)
    return f'<div class="sp-tw"><table class="sp-t{(" " + cls) if cls else ""}"><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'
H = lambda i, t: f'<h2>{t}</h2>'
C = lambda x: f"<code>{x}</code>"

SECS = [("sp-over", "概要"), ("sp-arch", "全体の構成"), ("sp-route", "画面とルーティング"), ("sp-subj", "科目と設定"), ("sp-data", "データの形式"),
        ("sp-quiz", "問題集"), ("sp-sync", "記録の保存と同期"), ("sp-train", "トレーニング"), ("sp-ai", "AI先生"), ("sp-rec", "学習の記録・草の庭"),
        ("sp-build", "作り方・テスト・公開"), ("sp-rule", "方針と制約")]
TOC = '<nav class="gd-toc" aria-label="目次">' + "".join(f'<a href="#{i}">{t}</a>' for i, t in SECS) + "</nav>"

MARKUP = f"""
<main class="wrap guide spec" id="main">
 <div class="hero"><h1>仕様書</h1>
  <p class="lead">CommitStudy の作りを、エンジニア向けにまとめたページです。画面の操作は「使い方」を見てください。</p></div>
 {TOC}
 <section class="bx gd" id="sp-over">{H(1, "概要")}
  <p>Salesforce と情報処理技術者試験の、テキスト・問題集・用語カード・学習記録をまとめた学習アプリです。claude.ai のアーティファクトとして公開し、サーバーを持たない1ページのアプリ(SPA)として動きます。</p>
  {T(["項目", "内容"], [
    ["形", "HTML 1ファイル(index.html、約1MB)+ 科目ごとの JSON + 画像"],
    ["動く場所", "claude.ai のアーティファクトのページ(index.html は body の中に入る)"],
    ["保存", "端末: localStorage / アカウント: window.claude の db(本人だけが読み書き)"],
    ["AI", "window.claude の sample(AI先生)"],
    ["ライブラリ", "使わない(素の JavaScript・CSS・SVG)"],
    ["前提の画面", "iPhone(幅390px前後)が第一。PC 幅(980px以上)では問題一覧を左に常に出す"],
    ["テーマ", "自動・ライト・ダーク。図は CSS のクラスで配色が切り替わる"],
  ])}
 </section>
 <section class="bx gd" id="sp-arch">{H(2, "全体の構成")}
  {FIG["arch"]}
  {T(["公開するファイル", "中身"], [
    [C("index.html"), "全画面の HTML・処理・CSS。ページごとの部品は window.FAMD(JSON)に入っている"],
    [C("data/&lt;科目&gt;/chapters.json"), "テキスト本文(章ごとの HTML。図は SVG を埋め込み)"],
    [C("data/&lt;科目&gt;/questions.json"), "問題(4択・複数選択)。正解・解説・根拠のURL・本文の該当箇所"],
    [C("data/&lt;科目&gt;/qrows.json"), "問題の索引(出典の種類・項目・問題文)。ホームや記録の集計に使う"],
    [C("data/&lt;科目&gt;/sections.json"), "項目の一覧(章・番号・題名)"],
    [C("data/&lt;科目&gt;/terms.json"), "用語カード(項目・用語・説明)"],
    [C("data/&lt;科目&gt;/img/"), "問題の図(webp)。IPA と MuleSoft の過去問で使う"],
    [C("data/catalog.json"), "科目カードのタグに出す、出典ごとの問題数と用語カードの枚数"],
    [C("brand/"), "キャラの顔・使い方ページの画面写真"],
  ])}
 </section>
 <section class="bx gd" id="sp-route">{H(3, "画面とルーティング")}
  <p>パスからページ名を決め、<code>FAMP.&lt;ページ名&gt;()</code> が画面を組み立てます。ページの見た目(markup・css)は <code>window.FAMD.pages</code> にあります。</p>
  {T(["パス", "ページ", "主な中身"], [
    [C("/"), "home", "きょうの一歩(前回の続き・お便り)・草の庭・お知らせ"],
    [C("/texts/"), "texts", "科目のカード(問題数のタグ)・並べ替え・合格の印"],
    [C("/&lt;科目&gt;/"), "subject", "テキスト・問題集・用語カード(科目ごとに設定 CFG を切り替える)"],
    [C("/practice/"), "practice", "トレーニング(全科目の問題・用語カード)"],
    [C("/record/"), "record", "学習の記録(カレンダー・勉強時間・進み具合・草の庭・庭の仲間・バッジ)"],
    [C("/news/"), "news", "更新情報"],
    [C("/guide/"), "guide", "使い方"],
    [C("/spec/"), "spec", "仕様書(このページ)"],
  ], "route")}
  {FIG["boot"]}
  <ul>
   <li>公開先では相対パスがそのまま使えないため、データや画像の URL は <code>famURL()</code> で公開先のものに直します。</li>
   <li>本文と問題は端末に控え(chcache / qcache)を持ち、次に開くときはまず控えで描いてから新しいデータで描き直します。</li>
  </ul>
 </section>
 <section class="bx gd" id="sp-subj">{H(4, "科目と設定")}
  {T(["科目(ID)", "過去問", "Trailhead", "オリジナル", "計", "用語カード"], rows, "num")}
  <p>科目ごとの違いは設定 <code>CFG</code> にまとめ、画面の処理は全科目で共通です。</p>
  {T(["設定", "意味"], [
    [C("key / quizKey"), "端末の保存の名前(例: sr-d360・sr-d360-quiz-v1)"],
    [C("srcs"), "出典の種類。<code>k</code>(past・orig・th)、表示名、出典の文字に当てる正規表現 <code>re</code>。どれにも当たらなければ先頭(過去問)"],
    [C("cx"), "試験の出題範囲(セクション)の名前の並び。問題の <code>c</code> はこの位置"],
    [C("years"), "出題回の絞り込みを出すか(過去問の回 v2026-08-04・令和8年度 など)"],
    [C("qWord / pal"), "画面の呼び方(問題)と配色"],
  ])}
 </section>
 <section class="bx gd" id="sp-data">{H(5, "データの形式")}
  <p>問題(questions.json の1件)は <code>{{"id":"q0001","data":{{…}}}}</code> の形です。<code>data</code> の項目は次のとおりです。</p>
  {T(["項目", "意味"], [
    [C("id"), "問題の番号。記録はこの番号で持つので、一度振ったら変えない(過去問・Trailhead・オリジナルは ids.json で固定)"],
    [C("q / o / a"), "問題文・選択肢・正解(選択肢の位置の配列。2つ以上なら複数選択)"],
    [C("ex"), "解説"],
    [C("f"), "テキストの項目(例: f-idr)。「テキストの該当箇所で復習する」の行き先"],
    [C("c"), "出題範囲(CFG.cx の位置)"],
    [C("s"), "出典。「v2026-08-19 Q12」「Trailhead: …」「オリジナル(…)」など。出典の種類はこの文字で決まる"],
    [C("u / v / n"), "根拠のURL・検証状況(公式で確認済み・要確認 など)・検証のメモ"],
    [C("x / xs"), "本文の該当する段落・表の行の文字列(xs は別の項目のとき)。本文の文字と完全に一致させる"],
    [C("qe / oe"), "英語の原文(過去問)"],
    [C("km"), "科目A・科目B(基本情報・情報セキュリティマネジメント)"],
  ])}
  <p>問題文・解説は、次の書き方で表やプログラムの枠になります(<code>csQF</code>)。</p>
  {T(["書き方", "表示"], [
    ["〔見出し〕の行", "枠の見出し"],
    ["「｜」を含む行が続く", "表(1行目が見出し)。収まらない表は表の中だけ横にスクロール"],
    ["〔プログラム〕〔SQL 文〕の後", "プログラムの枠(字下げを保つ)"],
    ["〔図:ファイル名〕代替テキスト", "画像。名前の末尾 _w300 などで表示の幅を決める"],
    ["選択肢の中の改行", "そのまま改行(pre-wrap)"],
  ])}
 </section>
 <section class="bx gd" id="sp-quiz">{H(6, "問題集")}
  {FIG["quiz"]}
  <ul>
   <li>番号の表示(問N)は、絞り込んだ並びの中での通し番号です。記録は元の番号(id)のまま持ちます。</li>
   <li>開き直すと、絞り込みを計算し直した並びの中で、前回見ていた問題から再開します。</li>
   <li>答えた結果は、回答の集計 <code>hist[id]</code>(回数・正解数・最後の結果・時刻)と、回答履歴 <code>log</code>(番号・選んだ選択肢・正誤・時刻・問題集かトレーニングか)に入ります。</li>
   <li>本文の該当箇所には「問題 N」の印が付き、押すとその箇所の問題を一覧します(全問正解なら緑)。</li>
  </ul>
 </section>
 <section class="bx gd" id="sp-sync">{H(7, "記録の保存と同期")}
  {FIG["sync"]}
  {T(["アカウントの書類", "中身"], [
    [C("data/users/&lt;ID&gt;/&lt;科目&gt;-quiz"), "問題集: 回答の集計・回答履歴・しおり・絞り込みと位置"],
    [C("…/&lt;科目&gt;-study"), "テキスト: 理解した項目・しおり・マーカーとメモ・前回の位置"],
    [C("…/&lt;科目&gt;-act"), "学習量: 日ごとの解いた数・正解数・読んだ項目(端末ごとの数)"],
    [C("…/fam-ls"), "端末の記録のうち同期するもの(用語カードの覚えた・復習の予定・合格した科目・お気に入りの仲間・既読など)"],
    [C("…/fam-theme"), "テーマ(自動・ライト・ダーク)"],
  ])}
  <p>合わせ方の決まり(<code>window.CSQ</code>):</p>
  <ul>
   <li><b>読む → 合わせる → 保存</b>: 保存の前に必ずアカウントの記録を読み直します。画面にある分で丸ごと上書きはしません。</li>
   <li><b>項目ごとの更新時刻</b>: 消した項目も時刻を残し(消した印)、ほかの端末の古い控えで復活させません。</li>
   <li><b>時刻</b>: 「端末の時計」と「これまでに見た一番新しい時刻+1」の大きい方を使い、時計のずれた端末でも後の操作が勝つようにします。</li>
   <li><b>数</b>: 解いた数・勉強時間は端末ごとに持ち、合計を表示します(2台で解いても大きい方にならない)。</li>
   <li><b>同じ端末のほかのタブ</b>: storage イベントで中身だけ合わせ、画面の位置や絞り込みはそのままにします。</li>
   <li><b>読み込みが終わるまで待つ</b>: fam-ls はアカウントから読み終えるまで保存しません。バッジのお知らせも読み終えてから(最長20秒)出します。</li>
  </ul>
  {T(["保存状態の帯", "条件"], [
    ["出ない", "アカウントに保存できている"],
    ["黄「クラウドに接続しています…」", "3秒たってもつながらない(15秒で赤に)"],
    ["赤「アカウントに保存されていません」", "アカウントにつながっていない(この端末だけ)"],
    ["赤「クラウドへの保存に失敗しています」", "保存に失敗した(再試行のボタン)"],
  ])}
 </section>
 <section class="bx gd" id="sp-train">{H(8, "トレーニング")}
  {FIG["train"]}
  <ul>
   <li>問題は各科目の questions.json をそのまま使います。絞り込みは すべて・今日の復習・間違えた問題・まだ解いていない、出し方は 順番に・ランダム です。</li>
   <li>絞り込んだ並びは、選び直すまで固定します(解いて条件から外れた問題にも「前へ」で戻れる)。「次へ」は並びの中で後ろにある、まだ条件に当てはまる問題へ進み、先頭には戻りません。残りがなくなると「解き終えました」を出します。</li>
   <li>出典の種類は <code>srcOf(科目, 出典)</code> で、問題集と同じく 過去問・Trailhead・オリジナル に分けます。</li>
  </ul>
 </section>
 <section class="bx gd" id="sp-ai">{H(9, "AI先生")}
  <ul>
   <li>テキストの各項目の末尾と、問題の解説の下から質問できます。<code>window.claude</code> の sample を使い、回答は少しずつ表示します(途中で止められる)。</li>
   <li>最初のメッセージに、答え方の決まりと文脈(項目の本文、または問題・選択肢・正解・受講者の解答・解説・関連する本文)を入れ、続けて直近8回分のやりとりを送ります。</li>
   <li>回答が途中で切れたときは、その旨を出し、「続きを教えて」で続きを聞けます。よい回答は保存できます。</li>
  </ul>
 </section>
 <section class="bx gd" id="sp-rec">{H(10, "学習の記録・草の庭")}
  {T(["しくみ", "決まり"], [
    ["学習した日", "1節読むか1問解いた日。カレンダーに草のスタンプ(日付ごとに8種類から決まる)"],
    ["草の本数", "学習した日に1本+解いた問題10問ごとに1本+勉強時間30分ごとに1本"],
    ["庭の段階", "本数で 芽 → 草むら → 庭 → 花の庭 → 丘 → 山 → 森 → 湖 → 虹の谷 → 楽園(1000本)"],
    ["空", "季節 × 時間帯。時間帯は東京の月ごとの日の出・日の入りで決める。日付で日替わりの演出"],
    ["庭の仲間", "全50種類(うち空を飛ぶ11種類)。成果で仲間になり、庭には最大10匹。お気に入りは最大10匹でいつも出る。夜は子ごとの時刻に眠る(昼に眠る夜型の子もいる)。近くの2匹がときどき交流する(会話・いっしょに跳ねる・追いかけっこ・空の子が回る。20〜40秒に1回まで、同時に1つ)"],
    ["バッジ", "獲得したものだけを一度だけお知らせ(お知らせ済みは cs-badge-told に記録して同期)"],
  ])}
  <p>テスト用に <code>window.__csSky={{tod:"night",season:"autumn",variant:"shoot",hh:22.4}}</code> で空の時間帯・季節・演出・時刻を固定できます。</p>
 </section>
 <section class="bx gd" id="sp-build">{H(11, "作り方・テスト・公開")}
  {FIG["build"]}
  <ol>
   <li><b>画面</b>: <code>rebuild.sh</code> が、トレーニング追加前の版(v21)に {NPATCH} 個のパッチ(<code>patch_*.py</code> など)を順に当てて index.html を作ります。パッチは置き換える文字が見つからない・複数あるときは止まります。新しいパッチは末尾に足します。</li>
   <li><b>データ</b>: 科目ごとの原稿から <code>build_&lt;科目&gt;.py</code> で組み立て、過去問は <code>add_pastq_*.py</code>、Trailhead のクイズは <code>add_trailhead.py</code>、オリジナル問題は <code>add_orig_*.py</code> で足します。どれも何度実行しても同じ結果になり、問題の番号は ids.json で固定します。科目カードの数は <code>make_catalog.py</code> で作り直します。</li>
   <li><b>図</b>: <code>figs_m/lib.py</code>(幅340)で SVG を作り、<code>figs_m/preview.py</code> で文字のはみ出し・箱の重なりを確かめます。</li>
   <li><b>テスト</b>: <code>wrap.sh</code> で公開先と同じく index.html を body に包み、Playwright のスモークテスト(18項目: 各画面の表示・問題を解く・記録・同期・コンソールのエラーなし など)を通します。</li>
   <li><b>公開</b>: テストが通ってから、アーティファクトに index.html と変わったデータを出します。</li>
  </ol>
 </section>
 <section class="bx gd" id="sp-rule">{H(12, "方針と制約")}
  <ul>
   <li>index.html は claude.ai のページの body の中に入り、科目を開くと body が作り直されます。足す CSS は <code>&lt;style&gt;</code> をファイルに置かず、スクリプトで <code>document.head</code> に入れます。</li>
   <li>画面・図は iPhone の幅を第一に作ります。表は列が細くなりすぎないよう最小幅を持たせ、収まらないときは表の中だけ横にスクロールします。</li>
   <li>端末の「視差効果を減らす」(prefers-reduced-motion)の設定は使いません(作者の方針)。</li>
   <li>記録の形を変えるときは、これまでの形の記録をそのまま読み込んで新しい形に移します(消さない)。</li>
   <li>機能を変えたら、使い方ページと更新情報も合わせて直します。</li>
  </ul>
 </section>
 <p class="gd-foot"><a class="bx-go pri" href="/guide/">使い方を見る</a></p>
</main>
"""
SCSS = """
/* 仕様書ページ */
.spec .sp-tw{overflow-x:auto;-webkit-overflow-scrolling:touch;margin:4px 0;border:1px solid var(--line);border-radius:10px}
.spec table.sp-t{width:100%;min-width:0;border-collapse:collapse;font-size:13.5px;line-height:1.65;margin:0}
.spec .sp-t th,.spec .sp-t td{padding:7px 9px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top;min-width:5em}
.spec .sp-t th:first-child,.spec .sp-t td:first-child{min-width:6.5em}
.spec .sp-t thead th{background:color-mix(in srgb,var(--brand) 10%,var(--paper));font-weight:700;white-space:nowrap}
.spec .sp-t tbody tr:last-child td{border-bottom:0}
.spec .sp-t.num td:nth-child(n+2){text-align:right;white-space:nowrap;min-width:2.6em;padding-left:4px;padding-right:6px}
.spec .sp-t.num th:nth-child(n+2){min-width:2.6em;white-space:normal;padding-left:4px;padding-right:6px;font-size:12px;text-align:right}
.spec .sp-t.num td:first-child{min-width:7.5em}
.spec code{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:.9em;background:color-mix(in srgb,var(--ink) 7%,transparent);border-radius:5px;padding:1px 5px;word-break:break-all}
.spec .sp-t code{word-break:break-all;white-space:normal}
.spec .sp-t.route td:first-child code{white-space:nowrap}
.spec .bx.gd ul,.spec .bx.gd ol{margin:4px 0 0}
"""
lines = s.split("\n"); LI = next(i for i, x in enumerate(lines) if "window.FAMD=" in x); l = lines[LI]
j = l.index("window.FAMD=") + len("window.FAMD="); F, end = json.JSONDecoder().raw_decode(l[j:])
F["pages"]["spec"] = {"title": "仕様書", "bodyPage": "spec", "css": F["pages"]["guide"]["css"] + SCSS, "markup": MARKUP}
lines[LI] = l[:j] + json.dumps(F, ensure_ascii=False).replace("</", "<\\/") + l[j+end:]
s = "\n".join(lines)
rep('"/guide/":`guide`}', '"/guide/":`guide`,"/spec/":`spec`}')
rep("FAMP.record=function(){", 'FAMP.spec=function(){};\n\nFAMP.record=function(){')
ARR = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 6l6 6-6 6"/></svg></a>'
LK = '<a class="lk" href="/guide/">使い方' + ARR
rep(LK, LK + '<a class="lk" href="/spec/">仕様書' + ARR, 4)
open(out, "w", encoding="utf-8").write(s); print("ok")
