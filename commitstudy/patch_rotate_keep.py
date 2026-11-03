"""スマホを縦⇔横に回したとき、読んでいた位置がずれないようにする(全ページ共通)。
  スクロールのたびに、画面の上端(ヘッダーのすぐ下)にある本文の要素とその位置を控え、
  画面の幅が変わったら(回転・ウィンドウの幅の変更)、その要素が同じ位置に来るようにスクロールし直す。
使い方: python3 patch_rotate_keep.py <index.html> <出力>
"""
import sys
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
JS = r'''
/* ==回転しても読んでいた位置を保つ== */
(function(){
  var anchor=null,off=0,lastW=window.innerWidth,busy=0;
  function topY(){var h=document.querySelector(".mbar,header.hd,.hd");var b=h?h.getBoundingClientRect().bottom:0;return Math.max(0,Math.min(b,window.innerHeight/3))+8}
  function pick(){var y=topY(),x=Math.round(window.innerWidth/2);
    var e=document.elementFromPoint(x,y)||document.elementFromPoint(24,y);
    while(e&&e!==document.body&&!/^(P|LI|H1|H2|H3|H4|TR|FIGURE|ARTICLE|SECTION|BLOCKQUOTE|TABLE|UL|OL|DETAILS)$/.test(e.tagName))e=e.parentElement;
    if(!e||e===document.body||e.closest(".mbar,.hd,.tabbar,.mpanel"))return;
    anchor=e;off=e.getBoundingClientRect().top}
  var t=null;
  window.addEventListener("scroll",function(){if(busy)return;clearTimeout(t);t=setTimeout(pick,120)},{passive:true});
  setTimeout(pick,1500);
  function fix(){if(!anchor||!document.contains(anchor))return;var d=anchor.getBoundingClientRect().top-off;if(Math.abs(d)>2)window.scrollTo(0,window.scrollY+d)}
  function onResize(){var w=window.innerWidth;if(w===lastW)return;lastW=w;if(!anchor)return;busy++;
    requestAnimationFrame(function(){requestAnimationFrame(function(){fix();setTimeout(fix,250);setTimeout(function(){fix();busy--},600)})})}
  window.addEventListener("resize",onResize);window.addEventListener("orientationchange",function(){setTimeout(onResize,50)});
})();
'''
k = "FAMP.record=function(){"
if s.count(k) != 1: sys.exit("挿入位置が見つからない")
s = s.replace(k, JS + "\n" + k)
open(out, "w", encoding="utf-8").write(s); print("ok")
