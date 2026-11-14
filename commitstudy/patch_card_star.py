"""用語カード(トレーニング)の☆が、カードの右上のほかに左上にも出ていたのを直す。
  原因: カードの裏面の☆(position:absolute・z-index)が独立した層になり、裏面を隠す指定(backface-visibility)が効かず、表から左右反転して透けて見えていた。
  直し方: 見えていない面の☆は隠す(表のときは裏面の☆、裏返したときは表の☆)。☆にも backface-visibility を付ける。
  公開先では body が作り直されるため、CSS はスクリプトで document.head に入れる。
使い方: python3 patch_card_star.py <index.html> <出力>
"""
import sys
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
css = (".fc .g-bm{backface-visibility:hidden;-webkit-backface-visibility:hidden}"
       ".fc:not(.on) .back .g-bm,.fc.on .front .g-bm{visibility:hidden}")
js = "<script>(function(){if(document.getElementById('cs-card-star'))return;var st=document.createElement('style');st.id='cs-card-star';st.textContent='" + css + "';document.head.appendChild(st)})();</script>"
if s.count("</head>") != 1: sys.exit("</head> が1件ではない")
s = s.replace("</head>", js + "</head>")
open(out, "w", encoding="utf-8").write(s); print("ok")
