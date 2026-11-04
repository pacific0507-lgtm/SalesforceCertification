"""ホームの見出し(毎日1コミット、草が生える勉強。)の背景で、草がゆっくり生えてくる。
  - 見出しの区画の下側に、草の葉を描いた SVG を敷く(文字の後ろ)。1本ずつ時間差で伸び、伸びきるとそよぐ
  - 動きを減らす設定(prefers-reduced-motion)では、伸びた状態で止めて表示
使い方: python3 patch_hero_grass.py <index.html> <出力>
"""
import json, sys
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count: sys.exit(f"置換対象が {n} 件(期待 {count} 件): {old[:90]!r}")
    s = s.replace(old, new)
JS = r'''
/* ==ホームの見出しの背景で草が生える== */
function csHeroGrass(){var n=0;(function wait(){var h=document.querySelector("section.hero");if(!h){if(n++<50)setTimeout(wait,120);return}
  if(h.querySelector(".hero-grass"))return;var W=Math.max(320,Math.round(h.clientWidth)),H=96,seed=7;
  var rnd=function(){seed=(seed*16807)%2147483647;return (seed-1)/2147483646};
  var C=["#5aa83a","#7cc24f","#3f8f2e","#94cf63","#4c9c45"],g="",cnt=Math.round(W/9);
  for(var i=0;i<cnt;i++){var x=(i+rnd())*W/cnt,hh=26+rnd()*(rnd()<.18?62:40),w=2.2+rnd()*2.6,b=(rnd()-.5)*hh*.55,c=C[Math.floor(rnd()*C.length)],d=(rnd()*22).toFixed(1),t=(5+rnd()*7).toFixed(1),sw=(4+rnd()*3).toFixed(1),op=(.38+rnd()*.32).toFixed(2);
    g+='<g class="hg-b" style="--d:'+d+'s;--t:'+t+'s"><path style="--sw:'+sw+'s;opacity:'+op+'" fill="'+c+'" d="M'+(x-w).toFixed(1)+' '+H+' Q'+(x+b*.35).toFixed(1)+' '+(H-hh*.55).toFixed(1)+' '+(x+b).toFixed(1)+' '+(H-hh).toFixed(1)+' Q'+(x+b*.35+w*.5).toFixed(1)+' '+(H-hh*.5).toFixed(1)+' '+(x+w).toFixed(1)+' '+H+'Z"/></g>';
    if(rnd()<.05){var fx=x+b,fy=H-hh;g+='<g class="hg-b hg-f" style="--d:'+(+d+ +t).toFixed(1)+'s;--t:2.5s"><circle cx="'+fx.toFixed(1)+'" cy="'+fy.toFixed(1)+'" r="3.2" fill="'+(rnd()<.5?"#f2c94c":"#f4a3b8")+'" opacity=".75"/></g>'}}
  var el=document.createElement("div");el.className="hero-grass";el.setAttribute("aria-hidden","true");
  el.innerHTML='<svg viewBox="0 0 '+W+' '+H+'" preserveAspectRatio="xMidYMax slice" width="100%" height="'+H+'">'+g+'</svg>';h.insertBefore(el,h.firstChild)})()}
(function(){var o=FAMP.home;FAMP.home=function(){o();setTimeout(csHeroGrass,0)}})();
'''
rep("FAMP.record=function(){", JS + "\nFAMP.record=function(){")
CSS = """
/* 見出しの背景の草 */
.hero{position:relative;overflow:hidden}
.hero>.wrap{position:relative;z-index:1}
.hero-grass{position:absolute;left:0;right:0;bottom:0;height:96px;z-index:0;pointer-events:none;-webkit-mask-image:linear-gradient(to top,#000 55%,transparent);mask-image:linear-gradient(to top,#000 55%,transparent)}
.hero-grass svg{display:block;position:absolute;bottom:0;left:0}
.hero-grass .hg-b{transform-box:fill-box;transform-origin:50% 100%;transform:scaleY(0);animation:hgGrow var(--t) var(--d) cubic-bezier(.2,.7,.2,1) forwards}
.hero-grass .hg-b path{transform-box:fill-box;transform-origin:50% 100%;animation:hgSway var(--sw) ease-in-out infinite alternate}
.hero-grass .hg-f{transform-origin:50% 50%}
@keyframes hgGrow{to{transform:scaleY(1)}}
@keyframes hgSway{from{transform:rotate(-2.5deg)}to{transform:rotate(2.5deg)}}
@media (prefers-reduced-motion:reduce){.hero-grass .hg-b{animation:none;transform:none}.hero-grass .hg-b path{animation:none}}
"""
lines = s.split("\n"); l = lines[4]
j = l.index("window.FAMD=") + len("window.FAMD="); F, end = json.JSONDecoder().raw_decode(l[j:])
F["pages"]["home"]["css"] += CSS
lines[4] = l[:j] + json.dumps(F, ensure_ascii=False).replace("</", "<\\/") + l[j+end:]
s = "\n".join(lines)
open(out, "w", encoding="utf-8").write(s); print("ok")
