"""マーカーのメモが長いと、編集パネル(.hlpop)が画面より高くなり、上の「×」や色のボタンが見えず閉じられなかったのを直す。
  パネルの高さを画面に収め(上下の余白と iPhone の安全領域を除く)、メモの表示欄と入力欄だけをパネルの中でスクロールさせる。
  公開先では body が作り直されるため、CSS はスクリプトで document.head に入れる。
使い方: python3 patch_memo_pop.py <index.html> <出力>
"""
import sys
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
css = (".hlpop{display:flex;flex-direction:column;box-sizing:border-box;max-height:calc(100vh - 16px);max-height:calc(100dvh - 16px - env(safe-area-inset-top,0px) - env(safe-area-inset-bottom,0px))}"
       ".hlpop.sheetpos{max-height:calc(100vh - 72px);max-height:calc(100dvh - 72px - env(safe-area-inset-top,0px) - env(safe-area-inset-bottom,0px))}"
       ".hlpop>.hp-top,.hlpop>.hp-row{flex:none}"
       ".hlpop>.hp-view{flex:0 1 auto;min-height:2.6em;overflow-y:auto;-webkit-overflow-scrolling:touch;overscroll-behavior:contain}"
       ".hlpop>textarea{flex:0 1 auto;min-height:4.5em;max-height:60vh;overflow-y:auto;overscroll-behavior:contain}")
js = "<script>(function(){if(document.getElementById('cs-memo-pop'))return;var st=document.createElement('style');st.id='cs-memo-pop';st.textContent='" + css + "';document.head.appendChild(st)})();</script>"
if s.count("</head>") != 1: sys.exit("</head> が1件ではない")
s = s.replace("</head>", js + "</head>")
open(out, "w", encoding="utf-8").write(s); print("ok")
