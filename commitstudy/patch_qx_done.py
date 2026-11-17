"""本文の「問題 N」の印で、その箇所の問題をすべて正解したとき(.qx-b.done)を分かりやすくする。大きさは変えない。
  これまで: 枠と文字が緑になるだけ → 緑で塗りつぶし、白い文字、えんぴつのアイコンの代わりに「✓」
  公開先では body が作り直されるため、CSS はスクリプトで document.head に入れる。
使い方: python3 patch_qx_done.py <index.html> <出力>
"""
import sys, json
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
css = (".qx-b.done{background:var(--ok)!important;border-color:var(--ok)!important;color:#fff!important}"
       ".qx-b.done:hover{background:color-mix(in srgb,var(--ok) 85%,#000)!important;color:#fff!important}"
       ".qx-b.done svg{display:none}"
       ".qx-b.done::before{content:\"✓\";display:inline-block;width:12px;text-align:center;font-weight:900;line-height:1}")
js = "<script>(function(){if(document.getElementById('cs-qx-done'))return;var st=document.createElement('style');st.id='cs-qx-done';st.textContent=" + json.dumps(css) + ";document.head.appendChild(st)})();</script>"
if s.count("</head>") != 1: sys.exit("</head> が1件ではない")
s = s.replace("</head>", js + "</head>")
# 読み上げにも「すべて正解」を伝える
old = 'b.setAttribute("aria-label","この箇所の問題 "+ns.length+"問");'
if s.count(old) != 1: sys.exit("aria-label の置換対象が見つからない")
s = s.replace(old, 'b.setAttribute("aria-label","この箇所の問題 "+ns.length+"問"+(done?"(すべて正解)":""));')
# 印の色(すべて正解)を、回答履歴が変わったら(アカウントの記録を読み込んだあと・問題を解いたあと)作り直さずに更新する。
# これまでは本文を描いたときの履歴で決めていたので、アカウントの記録があとから届くと、全問正解でも緑にならなかった
old2 = 'function closeQx(){qxp.hidden=true;qxAt=null}'
if s.count(old2) != 1: sys.exit("closeQx の置換対象が見つからない")
s = s.replace(old2, old2 + """
function qxRefresh(){try{$$("#chapters .qx-b").forEach(function(b){var ns=QXM[b.dataset.qx]||[];if(!ns.length)return;
  var d=ns.every(function(n){var h=histOf(n);return h&&h.l==="o"});if(b.classList.contains("done")!==d){b.classList.toggle("done",d);b.setAttribute("aria-label","この箇所の問題 "+ns.length+"問"+(d?"(すべて正解)":""))}})}catch(e){}}
setInterval(qxRefresh,2000);document.addEventListener("visibilitychange",function(){if(!document.hidden)qxRefresh()});""")
open(out, "w", encoding="utf-8").write(s); print("ok")
