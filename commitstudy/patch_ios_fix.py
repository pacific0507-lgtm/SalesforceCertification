"""iPhone で入力欄を押すと画面が拡大されるのを、どの画面でも起きないようにする(社労士版 2026-11-10 に合わせたもの)。
  公開先は claude.ai のページの中の枠(iframe)なので、ページの viewport の maximum-scale が効かないことがある。
  iPhone は文字が16pxより小さい入力欄を押すと拡大するため、iOS(-webkit-touch-callout がある端末)だけ、入力欄・選択欄の文字を16pxにする。
  あわせて、スマホで文字を選んだときに出るマーカーの色・メモ・質問のボタン(画面の下に出る帯)が画面の下に隠れないようにする(社労士版 2026-11-19):
  - 下に埋もれた分(--vb-hide。patch_vbottom.py が測る値)だけ上げる
  - 問題集では画面の下に固定した「前へ・答え合わせ・次へ」(#actions.qact)の下に隠れていたので、帯と横に重なる下の固定のもの
    (問題集のボタン・下のタブ・戻るの帯)があれば、その上に出す
  公開先では body が作り直されるため、CSS はスクリプトで document.head に入れる。
使い方: python3 patch_ios_fix.py <index.html> <出力>
"""
import sys, json
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count: sys.exit(f"置換対象が {n} 件(期待 {count} 件): {old[:90]!r}")
    s = s.replace(old, new)
rep('sb.style.bottom="calc(18px + env(safe-area-inset-bottom))";sb.style.left="50%";sb.style.transform="translateX(-50%)";return}',
    'sb.style.bottom="calc(18px + env(safe-area-inset-bottom,0px) + var(--vb-hide,0px))";sb.style.left="50%";sb.style.transform="translateX(-50%)";csSbLift();return}')
rep("function placeSb(){",
    "/* 帯と横に重なる、画面の下に固定したもの(問題集のボタン・下のタブ・戻るの帯)の上に出す */\n"
    "function csSbLift(){try{var r=sb.getBoundingClientRect(),vh=window.innerHeight,top=vh;\n"
    "  document.querySelectorAll(\"#actions.qact,nav.tabbar,.backpill,.qxback\").forEach(function(x){var q=x.getBoundingClientRect();if(!q.height||!q.width||q.bottom<=0||q.top>=vh)return;\n"
    "    var cs=getComputedStyle(x);if(cs.display===\"none\"||cs.visibility===\"hidden\"||cs.position!==\"fixed\")return;if(q.right<=r.left||q.left>=r.right||q.bottom<r.top-1)return;if(q.top<top)top=q.top});\n"
    "  if(top<vh){var need=vh-top+8;if(need>vh-r.bottom)sb.style.bottom=need+\"px\"}}catch(e){}}\n"
    "function placeSb(){")
css = ("@supports (-webkit-touch-callout:none){textarea,select,input:not([type=checkbox]):not([type=radio]):not([type=range]):not([type=button]):not([type=submit]):not([type=reset]):not([type=color]):not([type=file]){font-size:16px!important}}")
js = "<script>(function(){if(document.getElementById('cs-ios-nozoom'))return;var st=document.createElement('style');st.id='cs-ios-nozoom';st.textContent=" + json.dumps(css) + ";document.head.appendChild(st)})();</script>"
if s.count("</head>") != 1: sys.exit("</head> が1件ではない")
s = s.replace("</head>", js + "</head>")
open(out, "w", encoding="utf-8").write(s); print("ok")
