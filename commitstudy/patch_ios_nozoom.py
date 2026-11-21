"""iPhone で入力欄を押すと画面が拡大されるのを、どの画面でも起きないようにする(社労士版 2026-11-10 に合わせたもの)。
  公開先は claude.ai のページの中の枠(iframe)なので、ページの viewport の maximum-scale が効かないことがある。
  iPhone は文字が16pxより小さい入力欄を押すと拡大するため、iOS(-webkit-touch-callout がある端末)だけ、入力欄・選択欄の文字を16pxにする。
  あわせて、スマホで文字を選んだときに出るマーカーの色・メモ・質問のボタン(画面の下に出る帯)を、
  下に埋もれた分(--vb-hide)だけ上げる(社労士版 2026-11-19。patch_vbottom.py が測る値)。
  公開先では body が作り直されるため、CSS はスクリプトで document.head に入れる。
使い方: python3 patch_ios_nozoom.py <index.html> <出力>
"""
import sys, json
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count: sys.exit(f"置換対象が {n} 件(期待 {count} 件): {old[:90]!r}")
    s = s.replace(old, new)
rep('sb.style.bottom="calc(18px + env(safe-area-inset-bottom))"',
    'sb.style.bottom="calc(18px + env(safe-area-inset-bottom,0px) + var(--vb-hide,0px))"')
css = ("@supports (-webkit-touch-callout:none){textarea,select,input:not([type=checkbox]):not([type=radio]):not([type=range]):not([type=button]):not([type=submit]):not([type=reset]):not([type=color]):not([type=file]){font-size:16px!important}}")
js = "<script>(function(){if(document.getElementById('cs-ios-nozoom'))return;var st=document.createElement('style');st.id='cs-ios-nozoom';st.textContent=" + json.dumps(css) + ";document.head.appendChild(st)})();</script>"
if s.count("</head>") != 1: sys.exit("</head> が1件ではない")
s = s.replace("</head>", js + "</head>")
open(out, "w", encoding="utf-8").write(s); print("ok")
