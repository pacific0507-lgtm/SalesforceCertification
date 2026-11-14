"""トレーニングの用語カード:
  - 「カード」の絞り込みに「覚えたカード」を足す(すべて・まだ覚えていないカード・覚えたカード・★しおり)
  - 全画面にしないとき、カードの上の見出し(科目・項目名)が右上の☆・全画面ボタンや下の用語と重なっていたのを直す
    (見出しの右側をボタン2つ分あけ、項目名は折り返す。カードに最低の高さを持たせ、用語は見出しの下に置く)
  公開先では body が作り直されるため、CSS はスクリプトで document.head に入れる。
使い方: python3 patch_card_known.py <index.html> <出力>
"""
import sys
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count: sys.exit(f"置換対象が {n} 件(期待 {count} 件): {old[:90]!r}")
    s = s.replace(old, new)
rep('var GB=LS.get(GBK,{}),bms=all.filter(function(c){return GB[tkey(c)]});',
    'var GB=LS.get(GBK,{}),bms=all.filter(function(c){return GB[tkey(c)]}),kn=all.filter(function(c){return !!KNOWN[tkey(c)]});')
rep('{v:"todo",l:"まだ覚えていないカード",n:todo.length},{v:"bm",l:"★しおり",n:bms.length}]',
    '{v:"todo",l:"まだ覚えていないカード",n:todo.length},{v:"known",l:"覚えたカード",n:kn.length},{v:"bm",l:"★しおり",n:bms.length}]')
rep('TL=(ST.gonly==="todo"?todo:ST.gonly==="bm"?bms:all).slice();',
    'TL=(ST.gonly==="todo"?todo:ST.gonly==="known"?kn:ST.gonly==="bm"?bms:all).slice();')
rep('ST.gonly==="bm"?"しおりを付けたカードはありません。カードの右上の☆で付けられます。":"カードがありません。"',
    'ST.gonly==="bm"?"しおりを付けたカードはありません。カードの右上の☆で付けられます。":ST.gonly==="known"?"「覚えた」にしたカードはまだありません。カードを裏返して「覚えた」を押すと、ここに集まります。":"カードがありません。"')
css = (".fc .front .tq-h,.fc .back .bx-k{padding-right:96px!important;align-items:flex-start}"
       ".fc .front .tq-h>span:last-child:not(.tq-sj){margin-left:0!important;text-align:left!important;white-space:normal;overflow-wrap:anywhere;flex:1 1 8em;min-width:0}"
       ".fc .front{min-height:200px;justify-content:flex-start}"
       ".fc .front h3{margin:14px 0 auto!important;padding-top:4px}"
       "body.focus .fc .front .tq-h,body.focus .fc .back .bx-k{padding-right:52px!important}")
js = "<script>(function(){if(document.getElementById('cs-card-known'))return;var st=document.createElement('style');st.id='cs-card-known';st.textContent='" + css + "';document.head.appendChild(st)})();</script>"
if s.count("</head>") != 1: sys.exit("</head> が1件ではない")
s = s.replace("</head>", js + "</head>")
open(out, "w", encoding="utf-8").write(s); print("ok")
