"""スマホ(指で触る端末)で、選択肢をスワイプのとき指が触れただけで、選んだような枠(:hover の色)が残るのを直す。
  iPhone などは触れた要素に :hover が付いたまま残るため、マウスのない端末(hover:none)では選択肢の :hover の色を付けない。
  対象: 問題集の選択肢(.mcb)、模擬試験などの選択肢(.sopt)、トレーニングの選択肢(.tq-b)。選んだ・正解・不正解の色はそのまま。
  あわせて、触れたときの灰色の四角(タップのハイライト)も消す。
  公開先では body が作り直されるため、CSS はスクリプトで document.head に入れる。
使い方: python3 patch_touch_hover.py <index.html> <出力>
"""
import sys, json
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
css = (".mcb,.sopt,.tq-b,.omk button{-webkit-tap-highlight-color:transparent}"
       "@media (hover:none){"
       ".mcb:hover:not([disabled]):not(.selected){border-color:var(--line)}"
       ".sopt:hover:not([disabled]){border-color:var(--line)}"
       ".tq-b:hover:not(:disabled):not(.sel):not(.right):not(.wrong){border-color:var(--line);background:var(--paper)}"
       ".mcb:focus:not(:focus-visible),.sopt:focus:not(:focus-visible),.tq-b:focus:not(:focus-visible){outline:none}"
       "}")
js = "<script>(function(){if(document.getElementById('cs-touch-hover'))return;var st=document.createElement('style');st.id='cs-touch-hover';st.textContent=" + json.dumps(css) + ";document.head.appendChild(st)})();</script>"
if s.count("</head>") != 1: sys.exit("</head> が1件ではない")
s = s.replace("</head>", js + "</head>")
open(out, "w", encoding="utf-8").write(s); print("ok")
