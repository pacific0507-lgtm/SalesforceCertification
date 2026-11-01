"""トレーニング(/practice/)を追加するパッチ。社労士版の「1問トレーニング」と同じ画面構成で、
  - 問題: 各科目の4択(複数選択も)をそのまま出す。出し方は「順番どおり」「ランダム」「今日の復習」「間違えた問題」「まだ解いていない」
  - カード: 用語カード(data/<科目>/terms.json)。数字カードはなし
  - 解いた結果は ls-qpend-v1 に残し、科目の問題集を開いたときに回答履歴へ取り込む(社労士版の takePend と同じ)
使い方: python3 patch_practice.py <index.html> <出力> practice_extra.css   (同じフォルダの practice.js / practice.css も使う。practice_extra.css は社労士版トレーニングの CSS)
"""
import json, os, sys
here = os.path.dirname(os.path.abspath(__file__))
src, out, extra_css = sys.argv[1:4]
s = open(src, encoding="utf-8").read()
def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count: sys.exit(f"置換対象が {n} 件(期待 {count} 件): {old[:90]!r}")
    s = s.replace(old, new)
def rd(p): return open(os.path.join(here, p), encoding="utf-8").read()

# 0) スマホの下のタブを4つ(ホーム・テキスト・トレーニング・記録)に
rep(".tabbar{grid-template-columns:repeat(3,1fr)!important}", ".tabbar{grid-template-columns:repeat(4,1fr)!important}", 4)

# 1) ページ(FAMD.pages.practice)。CSS はテキスト一覧の CSS + 社労士版トレーニングの CSS + 4択・用語カード用
line = s.split("\n")[4]
D = json.loads(line[line.find("=") + 1:].rstrip().rstrip(";"))
LD = ('<div class="ld" role="status"><span class="ld-f" aria-hidden="true"><img src="brand/raf-face.webp" alt="" width="44" height="44"></span><small>読み込み中…</small></div>')
MARKUP = f'''
<main class="wrap">
 <header class="ph">
  <p class="eyebrow">トレーニング</p>
  <h1>1問ずつ、サクッと。</h1>
  <p>問題集の4択を1問ずつと、用語カード。すきま時間に、何問でも続けられます。解いた問題は各科目の問題集の回答履歴と「学習の記録」にも数えます。</p>
 </header>
 <div id="groups" hidden></div>
 <div class="pr">
  <div class="stage" id="stage">
   <div class="trow"><div class="tabs" role="tablist" aria-label="トレーニングの種類"><i class="pill" aria-hidden="true"></i><button type="button" role="tab" id="t-q" aria-controls="p-q" aria-selected="true">問題</button><button type="button" role="tab" id="t-g" aria-controls="p-g" aria-selected="false">用語カード</button></div></div>
   <section id="p-q" role="tabpanel" aria-labelledby="t-q">
    <p class="flt-l">科目</p><div class="flt" id="f-subj"></div>
    <div id="f-src-w"><p class="flt-l">出典</p><div class="flt" id="f-src"></div></div>
    <p class="flt-l">出し方</p><div class="flt" id="f-mode"></div>
    <div class="cw"><article class="bx" id="qbox" aria-live="polite">{LD}</article></div>
   </section>
   <section id="p-g" role="tabpanel" aria-labelledby="t-g" hidden>
    <p class="flt-l">科目</p><div class="flt" id="g-subj"></div>
    <p class="flt-l">カード</p><div class="flt" id="g-only"></div>
    <p class="gknown" id="g-known"></p>
    <div class="cw"><div class="flip"><div class="fc" id="fc" tabindex="0" role="button" aria-label="カードをめくる"><div class="front">{LD}</div><div class="back"></div></div></div></div>
    <div class="fc-nav"><button type="button" class="bx-btn" id="g-prev">前へ</button><span id="g-pos"></span><button type="button" class="bx-btn" id="g-shuf">シャッフル</button><button type="button" class="bx-go pri" id="g-next">次へ</button></div>
   </section>
  </div>
  <aside class="side">
   <div class="bx"><p class="bx-k">今日のトレーニング</p>
    <div class="meter"><div><b id="m-n">0</b><small>解いた</small></div><div><b id="m-c">0</b><small>正解</small></div><div><b id="m-combo">0</b><small>連続正解</small></div></div>
    <div id="m-say"></div>
   </div>
  </aside>
 </div>
</main>
'''
css = D["pages"]["texts"]["css"] + "\n" + open(extra_css, encoding="utf-8").read() + "\n" + rd("practice.css")
page = {"title": "トレーニング", "bodyPage": "practice", "css": css, "markup": MARKUP}
frag = '"practice": ' + json.dumps(page, ensure_ascii=False).replace("</", "<\\/") + ', '
rep('"news": {"title": "更新情報"', frag + '"news": {"title": "更新情報"')

# 2) ルーターとメニュー(ヘッダー・下のタブ・メニューのサイトマップ。4つのページの部品それぞれ)
rep('"/news/":`news`}', '"/news/":`news`,"/practice/":`practice`}')
NAV = '{id:`practice`,href:`/practice/`,label:`トレーニング`,short:`トレーニング`,icon:`<path d="M13 3L5 14h6l-1 7 8-11h-6z"/>`},'
rep('{id:`record`,href:`/record/`,label:`学習の記録`', NAV + '{id:`record`,href:`/record/`,label:`学習の記録`', 4)

# 3) ページの処理: テキスト一覧の部品でヘッダー・メニューを作り、そのあとトレーニングを動かす
rep("FAMP.record=function(){", "FAMP.practice=function(){\nFAMP.texts();\n" + rd("practice.js") + "\nCSPractice.init();\n};\n\nFAMP.record=function(){")

# 4) 科目の問題集: トレーニングで解いた結果(ls-qpend-v1)を回答履歴へ取り込む(社労士版と同じ)
TAKE = r'''S=fresh(S);
/* トレーニングやホームで解いた結果(ls-qpend-v1)を、この科目の回答履歴(hist)へ足す。取り込み済みは S.pa に控えて二重に数えない(社労士版と同じ) */
function takePend(bump){
  var p;try{p=JSON.parse(localStorage.getItem("ls-qpend-v1"))||{}}catch(e){p={}}
  var L=p[(window.FAMV&&FAMV.id)||""];if(!Array.isArray(L)||!L.length||!Q.length)return false;
  if(!Array.isArray(S.pa))S.pa=[];var ch=false;
  L.forEach(function(x){var k=x.id+"@"+x.t,m=/:q(\d+)$/.exec(x.id||""),q=m&&QMAP[+m[1]];if(!q||S.pa.indexOf(k)>=0)return;
    S.pa.push(k);ch=true;var h=S.hist[q.n]||(S.hist[q.n]={n:0,c:0});h.n=(+h.n||0)+1;if(x.ok)h.c=(+h.c||0)+1;
    if((+x.t||0)>=(+h.t||0)){h.l=x.ok?"o":"x";h.t=x.t}});
  if(!ch)return false;
  if(S.pa.length>1500)S.pa=S.pa.slice(-1500);
  if(bump)saveQ();else try{localStorage.setItem(QK,JSON.stringify(S))}catch(e){}
  return true;
}
'''
rep("S=fresh(S);\n", TAKE)
rep("function applyQ(arr,state){\n  prepQ(arr);qState=state;\n", "function applyQ(arr,state){\n  prepQ(arr);qState=state;takePend(false);\n")
rep("else{qcloud.set({json:JSON.stringify(S),ts:S.ts||Date.now()}).catch(function(){});renderToolbar()}\n",
    "else{qcloud.set({json:JSON.stringify(S),ts:S.ts||Date.now()}).catch(function(){});renderToolbar()}\n      if(takePend(true)){buildDeck();renderAll()}\n")
# トレーニングの「テキストで確認する」(#f-項目)は、前回問題集を開いていてもテキストで開く
rep('if(location.hash==="#quiz")startView="quiz";', 'if(location.hash==="#quiz")startView="quiz";else if(/^#f-/.test(location.hash))startView="text";')
open(out, "w", encoding="utf-8").write(s); print("ok")
