"""テキスト一覧のカードで、タイトルの上に資格の種類のラベル(Salesforce / 情報処理 / その他)を出す。
  Salesforce: d360・mcadmin・afsales・afsvc・afspec・mulepa、情報処理: fe・sg、それ以外は「その他」。
  公開先では body が作り直されるため、CSS はスクリプトで document.head に入れる。
使い方: python3 patch_texts_kind.py <index.html> <出力>
"""
import sys, json
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
def rep(a, b):
    global s
    n = s.count(a)
    if n != 1: sys.exit(f"{n} 件: {a[:80]}")
    s = s.replace(a, b)
rep("`</div><p class=\"tt\">`+B(e.title)+`</p>`",
    "`</div><p class=\"tt\">`+(function(k){return `<span class=\"tx-kindrow\"><span class=\"tx-kind tx-kind-`+k[0]+`\">`+k[1]+`</span></span>`})([`d360`,`mcadmin`,`afsales`,`afsvc`,`afspec`,`mulepa`].includes(e.id)?[`sf`,`Salesforce`]:[`fe`,`sg`].includes(e.id)?[`ipa`,`情報処理`]:[`etc`,`その他`])+B(e.title)+`</p>`")
css = (".tx .tt:has(.tx-kindrow){flex-wrap:wrap;row-gap:0}.tx .tx-kindrow{flex:0 0 100%;display:block;line-height:1}"
       ".tx .tx-kind{display:inline-block;font-size:11px;font-weight:700;line-height:1;padding:3px 8px;border-radius:999px;margin:0 0 5px;letter-spacing:.02em;border:1px solid currentColor}"
       ".tx .tx-kind-sf{color:#0b6fb8;background:rgba(11,111,184,.08)}"
       ".tx .tx-kind-ipa{color:#2f7d32;background:rgba(47,125,50,.08)}"
       ".tx .tx-kind-etc{color:#8a5a00;background:rgba(138,90,0,.08)}"
       "html[data-theme=dark] .tx .tx-kind-sf,.dark .tx .tx-kind-sf{color:#6cb6f0}"
       "html[data-theme=dark] .tx .tx-kind-ipa,.dark .tx .tx-kind-ipa{color:#7cc77f}"
       "html[data-theme=dark] .tx .tx-kind-etc,.dark .tx .tx-kind-etc{color:#e0b453}")
js = "<script>(function(){if(document.getElementById('cs-tx-kind'))return;var st=document.createElement('style');st.id='cs-tx-kind';st.textContent=" + json.dumps(css) + ";document.head.appendChild(st)})();</script>"
if s.count("</head>") != 1: sys.exit("</head> が1件ではない")
s = s.replace("</head>", js + "</head>")
open(out, "w", encoding="utf-8").write(s); print("ok")
