"""テキスト一覧で、「合格」の印を付けた科目を隠せるようにする。
  「並べ替え・合格の印」の横に「合格した科目を隠す」ボタン。押すと合格の科目のカードを隠し、ボタンは「合格した科目も表示(N)」になる。
  並べ替え・合格の印の編集中は、印を外せるように全部出す。グループの科目がすべて隠れたら、グループの見出しごと隠す(ボタンのあるグループは残す)。
  合格の印が1つもないときはボタンを出さない。設定は cs-subj-hidep(アカウントに同期)。
  公開先では body が作り直されるため、CSS はスクリプトで document.head に入れる。
使い方: python3 patch_texts_hidepassed.py <index.html> <出力>
"""
import sys, json
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
def rep(a, b):
    global s
    n = s.count(a)
    if n != 1: sys.exit(f"{n} 件: {a[:90]}")
    s = s.replace(a, b)
# 同期する鍵に足す
rep("`cs-plan-v1`,`cs-optmk-v1`]", "`cs-plan-v1`,`cs-optmk-v1`,`cs-subj-hidep`]")
# ボタン(並べ替えのボタンが bar の最初の button として扱われるので、こちらは後ろに置き、CSS の order で左に出す)
rep("bar.innerHTML='<button type=\"button\" id=\"tx-edbtn\" aria-pressed=\"false\">並べ替え・合格の印</button>';",
    "bar.innerHTML='<button type=\"button\" id=\"tx-edbtn\" aria-pressed=\"false\">並べ替え・合格の印</button><button type=\"button\" id=\"tx-hidep\" aria-pressed=\"false\" hidden>合格した科目を隠す</button>';"
    "bar.querySelector(\"#tx-hidep\").onclick=function(){LSs(\"cs-subj-hidep\",!LSg(\"cs-subj-hidep\",false));paint()};")
# 描くたびに隠す・出すを合わせる
rep('function paint(){var P=LSg("cs-subj-passed",{}),ed=list.classList.contains("ed");',
    'function paint(){var P=LSg("cs-subj-passed",{}),ed=list.classList.contains("ed");'
    'try{var hp=!!LSg("cs-subj-hidep",false),np=0,on=hp&&!ed;'
    'lists().forEach(function(l){var vis=0;cards(l).forEach(function(c){var p=!!P[c.dataset.id];if(p)np++;var h=on&&p;c.classList.toggle("tx-hid",h);if(!h)vis++});'
    'var g=l.closest(".grp");if(g)g.classList.toggle("grp-hid",on&&!vis&&!g.querySelector(".tx-edbar"))});'
    'var hb=document.getElementById("tx-hidep");if(hb){hb.hidden=!np||ed;hb.setAttribute("aria-pressed",String(hp));hb.textContent=hp?"合格した科目も表示("+np+")":"合格した科目を隠す"}}catch(e){}')
css = (".tx-edbar{gap:8px;flex-wrap:wrap}"
       ".tx.tx-hid,.grp.grp-hid{display:none!important}"
       "#tx-hidep{order:-1}#tx-hidep[hidden]{display:none}")
js = "<script>(function(){if(document.getElementById('cs-tx-hidep'))return;var st=document.createElement('style');st.id='cs-tx-hidep';st.textContent=" + json.dumps(css) + ";document.head.appendChild(st)})();</script>"
if s.count("</head>") != 1: sys.exit("</head> が1件ではない")
s = s.replace("</head>", js + "</head>")
open(out, "w", encoding="utf-8").write(s); print("ok")
