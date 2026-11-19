"""問題集の用語カード(#tcCard)で、☆がカードの右上のほかに左上にも透けて出ていたのを直す(トレーニングのカードの patch_card_star.py と同じ原因)。
  裏面の☆(position:absolute・z-index)が独立した層になり、裏面を隠す指定が効かず、表から左右反転して見えていた。
  見えていない面の☆は隠し、☆にも backface-visibility を付ける。
  公開先では body が作り直されるため、CSS はスクリプトで document.head に入れる。
使い方: python3 patch_tc_star.py <index.html> <出力>
"""
import sys, json
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
css = ("#tcCard .tc-bm{backface-visibility:hidden;-webkit-backface-visibility:hidden}"
       "#tcCard:not(.on) .tc-b .tc-bm,#tcCard.on .tc-f .tc-bm{visibility:hidden}")
js = "<script>(function(){if(document.getElementById('cs-tc-star'))return;var st=document.createElement('style');st.id='cs-tc-star';st.textContent=" + json.dumps(css) + ";document.head.appendChild(st)})();</script>"
if s.count("</head>") != 1: sys.exit("</head> が1件ではない")
s = s.replace("</head>", js + "</head>")
open(out, "w", encoding="utf-8").write(s); print("ok")
