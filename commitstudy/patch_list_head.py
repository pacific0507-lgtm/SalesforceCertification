"""問題一覧・用語カード一覧の章の見出し(.gl-ch)を1行にする(長い章名は … で省略)。
  見出しは一覧の上に貼り付く(sticky)ので、2行の見出しの上に次の章の見出し(1行)が重なると、
  前の章名の2行目が下からはみ出して「ダブって」見えていた。
  公開先では body が作り直されるため、CSS はスクリプトで document.head に入れる。
使い方: python3 patch_list_head.py <index.html> <出力>
"""
import sys
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
css = ".gl-ch>span{min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}"
js = "<script>(function(){if(document.getElementById('cs-glch'))return;var st=document.createElement('style');st.id='cs-glch';st.textContent='" + css + "';document.head.appendChild(st)})();</script>"
if s.count("</head>") != 1: sys.exit("</head> が1件ではない")
s = s.replace("</head>", js + "</head>")
open(out, "w", encoding="utf-8").write(s); print("ok")
