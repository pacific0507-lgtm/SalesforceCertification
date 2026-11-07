"""使い方ページ(/guide/)と、ホームの紹介文の切り替え・はじめての人への案内を追加する。
  - ホームの紹介文(.hero .lead)を、開くたびに複数のパターンから選んで表示(前回と同じものは避ける)
  - 使い方ページを一度も開いたことがない人には、紹介文の下に「はじめての方へ: 使い方を見る」を出し続ける(使い方ページを開くと消える)
  - メニューのサイトマップに「使い方」を追加
  - 使い方ページ: 機能と使い方を図入りで説明し、改善のためのコメントのお願いを書く
使い方: python3 patch_guide.py <index.html> <出力>   (同じフォルダの spec_guide.py と ../figs_m/lib.py を使う)
"""
import json, os, sys, importlib.util
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(here, "..", "figs_m")); import lib
m = importlib.util.spec_from_file_location("spec_guide", os.path.join(here, "spec_guide.py")); mod = importlib.util.module_from_spec(m); m.loader.exec_module(mod)
FIG = {k: v() for k, v in lib.FIGS.items()}
if lib.WARN: sys.exit("\n".join(lib.WARN))
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count: sys.exit(f"置換対象が {n} 件(期待 {count} 件): {old[:90]!r}")
    s = s.replace(old, new)

LEADS = [
 "読みながら覚えて、その場で問題を解く。コミットくん・クラウドちゃん・まなびんといっしょに、毎日1節か1問ずつ“コミット”して、学習の草を生やしていくテキストです。草(笑)が生えるくらい、肩の力を抜いて続けましょう。",
 "1日5分、1節だけでもOK。読んで、解いて、記録に草を生やす。コミットくんたちと、資格の勉強を毎日の習慣にしましょう。",
 "わからない所はその場でAI先生に質問。問題を間違えたら、テキストの該当箇所へひとっ飛び。読むと解くを行き来しながら覚えるテキストです。",
 "スキマ時間にトレーニングで1問、週末にテキストで1章。iPhoneでもPCでも、記録はアカウントにまとまって続きから学べます。",
 "マーカーを引いて、暗記シートで隠して、問題で確かめる。コツコツ積んだ“コミット”が、学習の記録に草として残ります。",
 "今日の1コミットは、1節でも1問でも。続けた日が草になって、合格までの道のりが目に見えるテキストです。",
 "クラウドちゃんの解説、コミットくんのツッコミ、まなびんの素朴な疑問。3人の掛け合いで、試験の要点を肩の力を抜いて覚えましょう。",
 "図とたとえで仕組みをつかみ、問題で確かめる。毎日少しずつ“コミット”して、学習の草を育てていきましょう。",
]
HOME_JS = r'''
/* ==ホームの紹介文と、はじめての人への案内== */
function csHomeExtra(){try{
  var L=__LEADS__,lead=document.querySelector(".hero .lead");
  if(lead){var last=-1;try{last=+localStorage.getItem("cs-lead-last")}catch(e){}var i;do{i=Math.floor(Math.random()*L.length)}while(L.length>1&&i===last);
    lead.textContent=L[i];try{localStorage.setItem("cs-lead-last",String(i))}catch(e){}}
  var seen=null;try{seen=localStorage.getItem("cs-guide-seen")}catch(e){}
  if(lead&&!seen&&!document.getElementById("guide-cta")){var a=document.createElement("div");a.className="guide-cta";a.id="guide-cta";
    a.innerHTML='<a href="/guide/"><b>はじめての方へ</b><span>使い方を見る</span><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>';
    lead.after(a)}
}catch(e){}}
'''.replace("__LEADS__", json.dumps(LEADS, ensure_ascii=False))
HOME_CSS = """
/* はじめての人への案内(ホームの紹介文の下) */
.guide-cta{display:flex;align-items:center;gap:6px;margin:-14px 0 24px;max-width:34em}
.guide-cta a{flex:1;display:flex;align-items:center;gap:10px;text-decoration:none;color:var(--ink);background:var(--paper);border:1.5px solid var(--sun);border-radius:14px;padding:10px 14px;font-size:14.5px;line-height:1.4}
.guide-cta a b{flex:none;font-size:12px;background:var(--sun);color:#2b1900;border-radius:999px;padding:2px 9px}
.guide-cta a span{flex:1;font-weight:700}
.guide-cta a svg{width:16px;height:16px;flex:none;color:var(--sub)}
.guide-cta button{flex:none;width:36px;height:36px;border-radius:10px;border:1px solid var(--line);background:var(--paper);color:var(--sub);font-size:18px;cursor:pointer}
"""
def jesc(t): return json.dumps(t, ensure_ascii=False)[1:-1].replace("</", "<\\/")
# ---- ページ ----
lines = s.split("\n"); l = lines[4]
j = l.index("window.FAMD=") + len("window.FAMD="); F, end = json.JSONDecoder().raw_decode(l[j:])
F["pages"]["home"]["css"] += HOME_CSS
H = lambda t: f"<h2>{t}</h2>"
def SHOT(n, cap, alt=None):
    return (f'<figure class="shot"><img src="brand/guide/{n}.webp" width="270" height="540" loading="lazy" alt="{alt or cap}">'
            f'<figcaption>{cap}</figcaption></figure>')
def SHOTS(*xs): return '<div class="shots">' + "".join(SHOT(*x) for x in xs) + '</div>'
MARKUP = f"""
<main class="wrap guide">
 <header class="ph">
  <p class="eyebrow">使い方</p>
  <h1>CommitStudy の使い方</h1>
  <p>読んで、解いて、記録に草を生やす。はじめての方は、ここから全体をつかんでください。画面の写真は iPhone で見たときのものです。</p>
 </header>
 <div id="groups" hidden></div>
 <nav class="gd-toc" aria-label="このページの目次"><a href="#g-screens">4つの画面</a><a href="#g-flow">学び方の流れ</a><a href="#g-text">テキスト</a><a href="#g-quiz">問題集</a><a href="#g-train">トレーニング</a><a href="#g-rec">学習の記録</a><a href="#g-save">記録の保存</a><a href="#g-app">アプリのように使う</a><a href="#g-comment">改善へのご協力</a></nav>
 <section class="bx gd" id="g-screens">{H("4つの画面")}
  <p>CommitStudy は、Salesforce などシステム系資格のテキストと問題集です。いまの科目は Data 360 コンサルタント、Marketing Cloud Administrator、Agentforce Sales コンサルタント、Agentforce スペシャリスト、MuleSoft Platform Architect の5つです。</p>
  {FIG["screens"]}
  {SHOTS(("home", "ホーム。下のタブで4つの画面を行き来します"), ("texts", "テキスト一覧。科目を選んで「読みはじめる」か「続きから」"))}
  <ul><li>各科目のカードのタグで、収録されている問題の種類(過去問・Trailhead・オリジナル)と問題数、用語カードの枚数がわかります。</li><li>テキスト一覧の右上の「並べ替え・合格の印」を押すと、↑↓で科目の並びを変えたり、合格した科目に「合格」の印を付けたりできます。終えるときは画面下の中央の「完了」を押します。変えた並びは、メニュー・ホーム・トレーニング(科目の絞り込みや、順番に解くときの順)・学習の記録など、科目が並ぶところすべてに反映されます。並びと印はアカウントに保存されます。</li></ul>
 </section>
 <section class="bx gd" id="g-flow">{H("学び方の流れ")}
  {FIG["flow"]}
  <ul><li>1節読むか1問解いた日に、学習の記録にスタンプ(草)が付きます。</li><li>迷ったら「テキスト」から科目を選び、「読みはじめる」を押してください。前回の続きはホームの「前回の続き」からも開けます。</li></ul>
 </section>
 <section class="bx gd" id="g-text">{H("テキスト")}
  {SHOTS(("text", "各項目は、キャラの掛け合いから始まります"), ("text_fig", "図と本文。「問題 N」の印は、その箇所が問われた問題"))}
  <ul>
   <li><b>キャラの掛け合い</b>: クラウドちゃん(先生)・コミットくん(ロボット)・まなびん(学習者)の会話で、要点をつかみます。</li>
   <li><b>問題へ</b>: 本文の「問題 N」の印を押すと、その箇所が問われた問題が出ます。</li>
  </ul>
  {SHOTS(("text_sel", "文字を選ぶと、マーカーの色とメモのボタンが出ます"), ("text_end", "項目の末尾。「理解した」と「問題に挑戦する」"))}
  <ul>
   <li><b>マーカー・メモ</b>: 本文の文字を選ぶと、マーカー・メモ・質問のボタンが出ます。引いたマーカーは「ノート」にまとまり、「暗記シート」で隠して覚えられます。</li>
   <li><b>理解した・問題</b>: 項目の末尾で「理解した」を押すと目次に印が付きます。「問題に挑戦する」から、その項目の問題を解けます。</li>
   <li><b>AI先生</b>: 各項目の末尾の「AI先生に質問する」で、その項目の本文をふまえて答えてもらえます。</li>
   <li><b>メニュー</b>: 上のメニューで、問題集への切り替え・目次・しおり・ノート・検索ができます。☆でしおりを付けられます。</li>
   <li><b>表示設定</b>: テキストの「表示設定」で配色や文字の大きさを、画面右上のメニューでライト/ダークの表示を変えられます。</li>
  </ul>
 </section>
 <section class="bx gd" id="g-quiz">{H("問題集")}
  {SHOTS(("quiz", "問題集。選択肢を選んで答え合わせ(選ぶ前は「答えを見る」)"), ("quiz_ans", "答え合わせのあと。解説・回答履歴・根拠のページ"), ("quiz_cards", "上の切り替えで用語カードに。カードを押すと説明、下のボタンで本文のその語句の箇所へ"))}
  <ul>
   <li>選択式(4択。一部は2つ選ぶ問題、Agentforce スペシャリストは3択)です。答え合わせのあと、解説と「テキストの該当箇所で復習する」が出ます。</li>
   <li>上のメニューの「絞込」で、Chapter・項目・出題回(過去問の回。例: v2026-08-04)・出典(過去問/オリジナルなど)・状態(未回答・要復習・しおり)を選べます。</li>
   <li>過去問は、英語の原文も表示できます。解説の下でも AI先生に質問できます。</li>
   <li>開き直すと、前回見ていた問題から再開します。</li>
   <li>一番上の「問題 / 用語カード」で、その科目の用語カードに切り替えられます。用語カードにすると、「絞込」(Chapter・項目・状態・ランダム)と「一覧」も用語カード用になります。カードは押すと説明が出て、「覚えた」「まだ」で仕分けられます。右上の☆でしおりを付けると、「状態: ★しおり」で絞れます(トレーニングの用語カードと共通)。「テキストの該当箇所で確認する」で、本文でその語句が出てくる箇所へ移れます(見つからない語句は項目の先頭へ)。覚えたカードは、トレーニングの用語カードと共通です。</li>
  </ul>
 </section>
 <section class="bx gd" id="g-train">{H("トレーニング")}
  {SHOTS(("train", "問題。科目・出典・絞り込み・出し方を選んで1問ずつ"), ("cards", "用語カード。カードを押すと裏の説明が出ます"))}
  <ul>
   <li><b>問題</b>: 全科目の問題を1問ずつ解けます。絞り込み(すべて・今日の復習・間違えた問題・まだ解いていない)と、出し方(順番に・ランダム)を選べます。絞り込んだ並びは、絞り込みや出し方を選び直すまでそのまま残るので、解いて条件から外れた問題にも「前へ」で戻れます。</li>
   <li><b>用語カード</b>: 表に用語、裏に説明。「覚えた」を付けたカードは、「まだ覚えていないカード」の絞り込みで外せます。右上の☆でしおりを付けたカードは「★しおり」で集められます。</li>
  </ul>
  {SHOTS(("train_full", "カード右上のボタンで全画面に。下の「前へ・答え合わせ・次へ」で進みます"))}
  <ul><li>解いた結果は、すぐに問題集の回答履歴と学習の記録に入ります。「今日のトレーニング」に、今日解いた数が出ます。</li></ul>
 </section>
 <section class="bx gd" id="g-rec">{H("学習の記録")}
  {SHOTS(("record", "学習の記録。連続日数・勉強時間と、スタンプのカレンダー"), ("record2", "科目ごとの進み具合と累計の勉強時間。押すとくわしい記録"))}
  <ul>
   <li>カレンダーの草、勉強した時間、この2週間に解いた問題、科目ごとの進み具合を見られます。</li>
   <li>バッジ・称号のほか、週に1回キャラからお便りが届きます(ホームに表示)。</li>
   <li><b>草の庭</b>: 学習した日に1本、さらに解いた問題10問ごとに1本、勉強時間30分ごとに1本の草が生え、本数に応じて 芽 → 草むら → 庭 → 花の庭 → 丘 → 山 → 森 → 湖 → 虹の谷 → 楽園(1000本)と育ちます。ホームでいまの庭を、学習の記録で草の種類ごとの本数や次の段階までの本数を見られます。</li>
  </ul>
  {SHOTS(("home2", "ホームの「きょうの一歩」。お便りと前回の続き"))}
 </section>
 <section class="bx gd" id="g-save">{H("記録の保存")}
  {FIG["save"]}
  {SHOTS(("menu", "右上のメニュー。保存先とサイトマップ・表示の切り替え"))}
 </section>
 <section class="bx gd" id="g-app">{H("アプリのように使う(ホーム画面に追加)")}
  <p>ホーム画面にアイコンを置いておくと、アプリのようにワンタップで開けます。追加は、claude.ai にログインしたブラウザで行ってください(記録はそのアカウントに保存されます)。</p>
  {FIG["homescreen"]}
  <h3 class="gd-h3">iPhone(Safari)</h3>
  <ol>
   <li>このページを <b>Safari</b> で開きます。Claude アプリの中で開いている場合は、リンクをコピーして Safari に貼り付けて開いてください。</li>
   <li>画面下(またはアドレスバー横)の<b>共有ボタン</b>(四角から上向きの矢印)を押します。見当たらないときは、アドレスバーの「…」から「共有」を選びます。</li>
   <li>一覧を下へスクロールして<b>「ホーム画面に追加」</b>を押します。</li>
   <li>名前を「CommitStudy」などに変えて、右上の<b>「追加」</b>を押します。</li>
  </ol>
  <h3 class="gd-h3">Android(Chrome)</h3>
  <ol>
   <li>このページを <b>Chrome</b> で開きます。</li>
   <li>右上の<b>︙(メニュー)</b>を押します。</li>
   <li><b>「ホーム画面に追加」</b>(機種によっては「アプリをインストール」)を押します。</li>
   <li>名前を確かめて<b>「追加」</b>を押します。ホーム画面にアイコンができます。</li>
  </ol>
  <ul>
   <li>ブラウザやOSのバージョンで、ボタンの場所や名前が少し違うことがあります。</li>
   <li>アイコンの絵は claude.ai のものになり、好きな画像には変えられません。自分の画像にしたい場合は、iPhone の「ショートカット」アプリで「URLを開く」ショートカットを作り、ホーム画面に追加するときに写真を選ぶ方法があります。</li>
  </ul>
 </section>
 <section class="bx gd" id="g-comment">{H("改善へのご協力(コメントのお願い)")}
  <p>CommitStudy は、使う人の声をもとに毎日よくしています。読みにくい所、まちがい、ほしい機能などに気づいたら、<b>claude.ai のアーティファクトのコメント機能</b>で、その場所にコメントを残してください。</p>
  {FIG["comment"]}
  <ul>
   <li>アーティファクトの画面のコメント機能で、ページの気になる場所を選んでコメントを書けます。</li>
   <li>例:「Ch3·2 の図の文字がはみ出している」「問題 45 の解説が分かりにくい」「トレーニングに○○がほしい」</li>
   <li>届いたコメントは作者が確認し、Claude といっしょに直します。直したものは「更新情報」でお知らせします。</li>
  </ul>
 </section>
 <p class="gd-foot"><a class="bx-go pri" href="/texts/">科目を選んではじめる</a></p>
</main>
"""
FIGCSS = open(os.path.join(here, "..", "figs_m", "fig.css"), encoding="utf-8").read().split("\n")
FIGCSS = "\n".join(x for x in FIGCSS if x.startswith(".fig") and not x.startswith(".fig figcaption")) 
GCSS = """
/* 使い方ページ */
.guide{--accent:var(--brand);--accent-soft:var(--brand-soft);--shu:var(--ng);--shu-soft:color-mix(in srgb,var(--ng) 14%,var(--paper));--yama:color-mix(in srgb,var(--sun) 55%,var(--ink));--yama-soft:var(--sun-soft);--ok-soft:color-mix(in srgb,var(--ok) 14%,var(--paper));--muted:var(--sub)}
.gd-toc{display:flex;flex-wrap:wrap;gap:6px;margin:0 0 16px}
.gd-toc a{font-size:13px;font-weight:700;text-decoration:none;color:var(--sub);background:var(--paper);border:1px solid var(--line);border-radius:999px;padding:4px 12px}
.bx.gd{margin:0 0 14px;scroll-margin-top:80px}
.bx.gd h2{margin:0;font-size:19px}
.bx.gd p,.bx.gd ul{margin:0;font-size:15px;line-height:1.85}
.bx.gd ul{padding-left:1.2em}
.bx.gd li{margin:0 0 6px}
.guide .fig{margin:6px 0}
.guide .fig figcaption{font-size:13px;color:var(--sub);text-align:center;margin-top:8px;line-height:1.65}
.gd-foot{text-align:center;margin:20px 0}
.gd-h3{font-size:15.5px;margin:6px 0 0}
.bx.gd ol{margin:0;padding-left:1.4em;font-size:15px;line-height:1.85}
.bx.gd ol li{margin:0 0 6px}
.shots{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:16px;margin:4px 0}
.shot{margin:0;text-align:center}
.shot img{display:block;width:100%;max-width:270px;height:auto;margin:0 auto;border-radius:16px;border:1px solid var(--line);box-shadow:0 10px 28px -16px rgba(0,0,0,.35);background:var(--paper)}
.shot figcaption{font-size:12.5px;color:var(--sub);line-height:1.6;margin-top:8px}
""" + FIGCSS + "\n.guide .fig.m svg{max-width:440px}\n"
F["pages"]["guide"] = {"title": "使い方", "bodyPage": "guide", "css": F["pages"]["texts"]["css"] + GCSS, "markup": MARKUP}
lines[4] = l[:j] + json.dumps(F, ensure_ascii=False).replace("</", "<\\/") + l[j+end:]
s = "\n".join(lines)
# ---- ルーター・ページの処理・メニュー ----
rep('"/practice/":`practice`}', '"/practice/":`practice`,"/guide/":`guide`}')
rep("FAMP.home=function(){", HOME_JS + "\nFAMP.home=function(){setTimeout(csHomeExtra,0);")
rep("FAMP.record=function(){", 'FAMP.guide=function(){FAMP.texts();try{localStorage.setItem("cs-guide-seen",String(Date.now()))}catch(e){}};\n\nFAMP.record=function(){')
LK = '<a class="lk" href="/news/">更新情報'
rep(LK, '<a class="lk" href="/guide/">使い方<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 6l6 6-6 6"/></svg></a>' + LK, 4)
# 「使い方を見た」は端末をまたいで覚える
rep("`cs-practice-v1`,`cs-train-today`]", "`cs-practice-v1`,`cs-train-today`,`cs-guide-seen`]")
open(out, "w", encoding="utf-8").write(s); print("ok")
