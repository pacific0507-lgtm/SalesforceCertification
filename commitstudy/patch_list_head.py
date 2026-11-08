"""問題一覧・用語カード一覧の章の見出し(.gl-ch)を、次の章の見出しが来たら上に押し出されて抜けるようにする(社労士版と同じ見え方)。
  見出しは一覧の上に貼り付く(sticky)が、これまでは全部の見出しが同じ親に並んでいたため、次の章の見出しが前の見出しの上に重なり、
  2行の章名だと2行目が下からはみ出していた。章ごとに見出しとその中身を枠(.gl-cg)に入れ、貼り付く範囲をその章の中だけにする。
  章名は省略せず、長ければ2行で出す。
  一覧は何か所かで作り直されるので、画面の変化を見張って、まだ枠に入っていない見出しを見つけたら枠に入れる。
  公開先では body が作り直されるため、CSS とスクリプトは document.head 側に置く(スクリプトは最初に一度だけ動く)。
使い方: python3 patch_list_head.py <index.html> <出力>
"""
import sys
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
css = ".gl-cg>.gl-ch{margin-top:4px}.gl-cg+.gl-cg>.gl-ch{margin-top:14px}"
js = r"""<script>(function(){if(window.__csGlCg)return;window.__csGlCg=1;
var st=document.createElement('style');st.id='cs-glcg';st.textContent='""" + css + r"""';document.head.appendChild(st);
function wrap(p){var kids=[].slice.call(p.children),g=null;kids.forEach(function(k){if(k.classList.contains('gl-ch')){g=document.createElement('div');g.className='gl-cg';p.insertBefore(g,k);g.appendChild(k)}else if(g){g.appendChild(k)}})}
function scan(){var seen=[];document.querySelectorAll('.gl-ch').forEach(function(h){var p=h.parentElement;if(p&&!p.classList.contains('gl-cg')&&seen.indexOf(p)<0)seen.push(p)});seen.forEach(wrap)}
var t=0;new MutationObserver(function(){if(t)return;t=requestAnimationFrame(function(){t=0;scan()})}).observe(document.documentElement,{childList:true,subtree:true});
document.addEventListener('DOMContentLoaded',scan);})();</script>"""
if s.count("</head>") != 1: sys.exit("</head> が1件ではない")
s = s.replace("</head>", js + "</head>")
open(out, "w", encoding="utf-8").write(s); print("ok")
