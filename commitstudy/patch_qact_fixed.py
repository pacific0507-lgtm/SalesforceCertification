"""問題集の答え合わせ・前へ・次へ・もう一度解く などのボタン(#actions)を、トレーニングと同じく画面の下に固定する。
  - 問題の画面(body.view-q)のときだけ。本文の下に余白をとり、最後の行がボタンに隠れないようにする
  - 「← テキストに戻る」などの帯は、固定したボタンの上に出す
  公開先では body が作り直されるため、CSS はスクリプトで document.head に入れる。
使い方: python3 patch_qact_fixed.py <index.html> <出力>
"""
import sys, json
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
css = ("body.view-q #actions.qact{position:fixed;z-index:60;left:max(12px,calc((100vw - 760px)/2));right:max(12px,calc((100vw - 760px)/2));"
       "bottom:calc(10px + env(safe-area-inset-bottom,0px));margin:0;padding:8px 10px;border:1px solid var(--line);border-radius:16px;"
       "background:color-mix(in srgb,var(--surface) 92%,transparent);-webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px);box-shadow:0 10px 30px -12px rgba(0,0,0,.35)}"
       "body.view-q main,body.view-q #main{padding-bottom:calc(96px + env(safe-area-inset-bottom,0px))}"
       "body.view-q .qxback,body.view-q.has-back .backpill{bottom:calc(84px + env(safe-area-inset-bottom,0px))}"
       "body.view-q.has-qxback main,body.view-q.has-qxback #main{padding-bottom:calc(150px + env(safe-area-inset-bottom,0px))}")
JS = r"""(function(){if(document.getElementById('cs-qact-fixed'))return;var st=document.createElement('style');st.id='cs-qact-fixed';st.textContent=__CSS__;document.head.appendChild(st);
/* PC では左の問題一覧があるので、ボタンの帯を問題の列(#qv-in)の幅にそろえる */
function al(){try{var a=document.getElementById('actions'),c=document.getElementById('qv-in');if(!a)return;
  if(!document.body.classList.contains('view-q')||!c||window.innerWidth<980){a.style.left='';a.style.right='';return}
  var r=c.getBoundingClientRect();if(!r.width)return;a.style.left=Math.max(12,r.left)+'px';a.style.right=Math.max(12,document.documentElement.clientWidth-r.right)+'px'}catch(e){}}
window.addEventListener('resize',al);setInterval(al,800);})();"""
js = "<script>" + JS.replace("__CSS__", json.dumps(css)) + "</script>"
if s.count("</head>") != 1: sys.exit("</head> が1件ではない")
s = s.replace("</head>", js + "</head>")
open(out, "w", encoding="utf-8").write(s); print("ok")
