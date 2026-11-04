"""ホームの見出し(毎日1コミット、草が生える勉強。)の背景で、草がゆっくり生えてくる。
  - 見出しの区画の下側に、草の葉を描いた SVG を敷く(文字の後ろ)。1本ずつ時間差で伸び、伸びきるとそよぐ
  - 草は区画の下端から見出しの高さまで伸びる(高い草ほどゆっくり伸び、文字が読めるよう上ほど薄く)
  - 見出しの「草」の字の上にも、小さな草が生える(少し遅れて1本ずつ)
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
  var t1=document.querySelector(".hero h1");if(!t1||!t1.getBoundingClientRect().height){if(n++<50)setTimeout(wait,120);return}
  var old=h.querySelector(".hero-grass");if(old){if(old.dataset.w==String(Math.round(h.clientWidth)))return;old.remove()}
  /* 草の高さ: 区画の下端から見出しの上端まで */
  var W=Math.max(320,Math.round(h.clientWidth)),hr=h.getBoundingClientRect(),H=Math.max(140,Math.round(hr.bottom-t1.getBoundingClientRect().top)),seed=7;
  var rnd=function(){seed=(seed*16807)%2147483647;return (seed-1)/2147483646};
  var C=["#5aa83a","#7cc24f","#3f8f2e","#94cf63","#4c9c45"],g="",cnt=Math.round(W/8);
  for(var i=0;i<cnt;i++){var x=(i+rnd())*W/cnt,r=rnd(),hh=H*(.08+Math.pow(r,1.7)*.92),f=hh/H,w=2+rnd()*2+f*5,b=(rnd()-.5)*hh*.35,c=C[Math.floor(rnd()*C.length)],d=(rnd()*24).toFixed(1),t=(5+f*16+rnd()*4).toFixed(1),sw=(4+rnd()*3+f*3).toFixed(1),op=(.30+rnd()*.25-f*.08).toFixed(2);
    g+='<g class="hg-b" style="--d:'+d+'s;--t:'+t+'s"><path style="--sw:'+sw+'s;--a:'+(2.6-f*1.8).toFixed(2)+'deg;opacity:'+op+'" fill="'+c+'" d="M'+(x-w).toFixed(1)+' '+H+' Q'+(x+b*.35).toFixed(1)+' '+(H-hh*.55).toFixed(1)+' '+(x+b).toFixed(1)+' '+(H-hh).toFixed(1)+' Q'+(x+b*.35+w*.5).toFixed(1)+' '+(H-hh*.5).toFixed(1)+' '+(x+w).toFixed(1)+' '+H+'Z"/></g>';
    if(rnd()<.05){var fx=x+b,fy=H-hh;g+='<g class="hg-b hg-f" style="--d:'+(+d+ +t).toFixed(1)+'s;--t:2.5s"><circle cx="'+fx.toFixed(1)+'" cy="'+fy.toFixed(1)+'" r="'+(3+f*2).toFixed(1)+'" fill="'+(rnd()<.5?"#f2c94c":"#f4a3b8")+'" opacity=".7"/></g>'}}
  var el=document.createElement("div");el.className="hero-grass";el.dataset.w=String(Math.round(h.clientWidth));el.setAttribute("aria-hidden","true");el.style.height=H+"px";
  el.innerHTML='<svg viewBox="0 0 '+W+' '+H+'" preserveAspectRatio="xMidYMax slice" width="100%" height="'+H+'">'+g+'</svg>';h.insertBefore(el,h.firstChild)})()}
var csHgT=null;window.addEventListener("resize",function(){clearTimeout(csHgT);csHgT=setTimeout(function(){if(document.querySelector("section.hero"))csHeroGrass()},400)});
/* 見出しの「草」の字の上にも草が生える */
function csKusa(){var n=0;(function wait(){var u=document.querySelector(".hero h1 .u");if(!u){if(n++<50)setTimeout(wait,120);return}if(u.querySelector(".ks"))return;
  var B=[[14,30,-6,"#4c9c45"],[24,40,-3,"#7cc24f"],[33,26,4,"#5aa83a"],[44,46,-2,"#3f8f2e"],[53,34,5,"#94cf63"],[62,44,2,"#5aa83a"],[71,28,-5,"#7cc24f"],[80,38,6,"#4c9c45"],[88,24,3,"#94cf63"]],g="";
  B.forEach(function(b,i){var x=b[0],h=b[1],k=b[2],w=3.2;g+='<g class="ks-b" style="--d:'+(1.3+i*.22).toFixed(2)+'s;--sw:'+(3.2+(i%3)*.7).toFixed(1)+'s"><path fill="'+b[3]+'" d="M'+(x-w)+' 50 Q'+(x+k*.4)+' '+(50-h*.55)+' '+(x+k)+' '+(50-h)+' Q'+(x+k*.4+w*.5)+' '+(50-h*.5)+' '+(x+w)+' 50Z"/></g>'});
  g+='<g class="ks-b ks-fl" style="--d:3.6s;--sw:4s"><circle cx="43" cy="5" r="3.6" fill="#f2c94c"/></g>';
  var sp=document.createElement("span");sp.className="ks";sp.setAttribute("aria-hidden","true");sp.innerHTML='<svg viewBox="0 0 100 50" preserveAspectRatio="none">'+g+'</svg>';u.appendChild(sp)})()}
(function(){var o=FAMP.home;FAMP.home=function(){o();setTimeout(csHeroGrass,0);setTimeout(csKusa,0)}})();
'''
rep("FAMP.record=function(){", JS + "\nFAMP.record=function(){")
CSS = """
/* 見出しの背景の草 */
.hero{position:relative;overflow:hidden}
.hero>.wrap{position:relative;z-index:1}
.hero-grass{position:absolute;left:0;right:0;bottom:0;height:120px;z-index:0;pointer-events:none;-webkit-mask-image:linear-gradient(to top,#000 35%,rgba(0,0,0,.55) 75%,rgba(0,0,0,.15));mask-image:linear-gradient(to top,#000 35%,rgba(0,0,0,.55) 75%,rgba(0,0,0,.15))}
.hero-grass svg{display:block;position:absolute;bottom:0;left:0}
.hero-grass .hg-b{transform-box:fill-box;transform-origin:50% 100%;transform:scaleY(0);animation:hgGrow var(--t) var(--d) cubic-bezier(.2,.7,.2,1) forwards}
.hero-grass .hg-b path{transform-box:fill-box;transform-origin:50% 100%;animation:hgSway var(--sw) ease-in-out infinite alternate}
.hero-grass .hg-f{transform-origin:50% 50%}
@keyframes hgGrow{to{transform:scaleY(1)}}
@keyframes hgSway{from{transform:rotate(calc(var(--a,2.5deg) * -1))}to{transform:rotate(var(--a,2.5deg))}}
.hero h1 .u{position:relative;display:inline-block}
.hero h1 .ks{position:absolute;left:8%;width:84%;bottom:80%;height:.3em;z-index:-1;pointer-events:none;line-height:0}
.hero h1 .ks svg{display:block;width:100%;height:100%;overflow:visible}
.hero h1 .ks-b{transform-box:fill-box;transform-origin:50% 100%;transform:scaleY(0);animation:hgGrow 1.6s var(--d) cubic-bezier(.2,.8,.2,1.15) forwards}
.hero h1 .ks-b path{transform-box:fill-box;transform-origin:50% 100%;animation:hgSway var(--sw) ease-in-out infinite alternate}
.hero h1 .ks-fl{transform-origin:50% 50%}
"""
lines = s.split("\n"); l = lines[4]
j = l.index("window.FAMD=") + len("window.FAMD="); F, end = json.JSONDecoder().raw_decode(l[j:])
F["pages"]["home"]["css"] += CSS
lines[4] = l[:j] + json.dumps(F, ensure_ascii=False).replace("</", "<\\/") + l[j+end:]
s = "\n".join(lines)
open(out, "w", encoding="utf-8").write(s); print("ok")
