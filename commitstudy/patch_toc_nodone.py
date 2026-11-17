"""テキストの目次で、「理解した」ボタンのない項目(「このテキストの使い方」や、章のまとめ・確認など)には「○」の印を出さない。
  目次の行(button.tr-it[data-id])の飛び先の項目に .donebtn がなければ tr-nodone を付け、印(.mk)を隠す。
  目次は後から描かれ、描き直されることもあるので、少しずつ見て付け直す。
  公開先では body が作り直されるため、CSS はスクリプトで document.head に入れる。
使い方: python3 patch_toc_nodone.py <index.html> <出力>
"""
import sys, json
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
css = ".tr-it.tr-nodone .mk{visibility:hidden}"
JS = r"""(function(){if(window.__csTocND)return;window.__csTocND=1;
var st=document.createElement('style');st.id='cs-toc-nodone';st.textContent=__CSS__;document.head.appendChild(st);
function run(){try{var bs=document.querySelectorAll('button.tr-it[data-id]:not([data-ndc])');for(var i=0;i<bs.length;i++){var b=bs[i],f=document.getElementById(b.getAttribute('data-id'));
  if(!f)continue;b.setAttribute('data-ndc','1');if(!f.querySelector('.donebtn'))b.classList.add('tr-nodone')}}catch(e){}}
setInterval(run,1200);document.addEventListener('DOMContentLoaded',run);})();"""
js = "<script>" + JS.replace("__CSS__", json.dumps(css)) + "</script>"
if s.count("</head>") != 1: sys.exit("</head> が1件ではない")
s = s.replace("</head>", js + "</head>")
open(out, "w", encoding="utf-8").write(s); print("ok")
