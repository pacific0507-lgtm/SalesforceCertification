"""節の地図・「テキストのこの場所」の地図の色を、実際の画面の色から読み取る(社労士版から移植。patch_csloc.py の cslBands/cslPaint を置き換える)。
  これまでは要素の種類ごとに決まった色(見出し=紺、表=青…)だったのを、getComputedStyle で本文の要素の色を読んで帯にする。
  配色(テキスト画面)・ライト/ダーク・文字の大きさが変わっても、画面と同じ色になる。
  - 見出し(h2〜h5): 見出しの文字の色。
  - 囲み(試験ポイント・たとえるなら・ひっかけ・要点・過去問の関連知識・例など)・表・図: 背景の色に、枠を足す。
      左の太い線(border-left が2px以上)は帯の左の線、まわりの枠は帯の細い枠で描く。
      背景が透明なら、中の表(table → td → th の順)の背景を使う。どれも透明なら文字の色を薄くした色。
  - キャラの掛け合い: ひとまとめにせず、吹き出し(p.tk の .bub)ごとに、その話し手の吹き出しの色と枠の色で描く。
  - ふつうの段落・箇条書き: 文字の色を薄くした色(color-mix で 35%)。
  位置は article からの getBoundingClientRect の差を、article の縮み(写しは transform で縮めている)で割って求める。
  画面の右端の節の地図は、節・節の高さ・幅が変わったときに加えて、配色・ライト/ダーク(html の data-theme、body の data-pal、
  端末のダーク設定)が変わったときにも塗り直す。
使い方: python3 patch_csmap_color.py <index.html> <出力>
"""
import sys
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count: sys.exit(f"置換対象が {n} 件(期待 {count} 件): {old[:90]!r}")
    s = s.replace(old, new)

OLD_BANDS = """function cslBands(art){var out=[];Array.prototype.forEach.call(art.children,function(ch){var k=cslType(ch);if(!k)return;var h=ch.offsetHeight;if(!h)return;
  out.push({k:k,top:ch.offsetTop,h:h,hd:/^H[2-5]$/.test(ch.tagName),name:/^H[2-5]$/.test(ch.tagName)?cslTxt(ch):CSL_TN[k]})});return out}
function cslPaint(box,bands,H){if(!box)return;var h="";bands.forEach(function(b){h+='<span class="csmap-b csmap-'+b.k+'" style="top:'+(b.top/H*100).toFixed(3)+'%;height:'+(b.h/H*100).toFixed(3)+'%"></span>'});box.innerHTML=h}"""

NEW_BANDS = r"""/* 色が見えるか(透明・ほぼ透明でないか) */
function cslVis(c){if(!c||c==="transparent")return false;var m=/rgba\(\s*[\d.]+[ ,]+[\d.]+[ ,]+[\d.]+[ ,\/]+([\d.]+)\s*\)/.exec(c)||/\/\s*([\d.]+%?)\s*\)/.exec(c);if(m){var a=parseFloat(m[1]);if(/%$/.test(m[1]))a/=100;return a>0.04}return true}
function cslFade(c,p){return "color-mix(in srgb,"+c+" "+(p||35)+"%,transparent)"}
/* 要素の見た目(背景・左の太い線・まわりの枠)を、帯の style にする */
function cslLook(el,cs,alt){cs=cs||getComputedStyle(el);var bg=cs.backgroundColor,st="";
  if(!cslVis(bg)&&alt){for(var i=0;i<alt.length;i++){var a=alt[i];if(!a)continue;var b=getComputedStyle(a).backgroundColor;if(cslVis(b)){bg=b;break}}}
  var bl=parseFloat(cs.borderLeftWidth)||0,blc=cs.borderLeftColor,bt=parseFloat(cs.borderTopWidth)||0,btc=cs.borderTopColor,sh=[];
  if(bl>=2&&cs.borderLeftStyle!=="none"&&cslVis(blc))sh.push("inset 2px 0 0 "+blc);
  else if(bt>=1&&cs.borderTopStyle!=="none"&&cslVis(btc))sh.push("inset 0 0 0 1px "+btc);
  else if(alt){for(var j=0;j<alt.length;j++){var x=alt[j];if(!x)continue;var xs=getComputedStyle(x);if((parseFloat(xs.borderTopWidth)||0)>=1&&xs.borderTopStyle!=="none"&&cslVis(xs.borderTopColor)){sh.push("inset 0 0 0 1px "+xs.borderTopColor);break}}}
  if(cslVis(bg))st="background:"+bg;else if(sh.length)st="background:"+cslFade(sh[0].replace(/^inset [^ ]+ [^ ]+ [^ ]+ /,""),30);else st="background:"+cslFade(cs.color);
  if(sh.length)st+=";box-shadow:"+sh.join(",");return st}
/* 節の直下の要素ごとの帯。色は実際の画面から読む(掛け合いは吹き出しごと) */
function cslBands(art){var out=[],ar=art.getBoundingClientRect(),sc=ar.height?(art.offsetHeight/ar.height):1,top0=ar.top;
  function geo(el){var r=el.getBoundingClientRect();return {top:(r.top-top0)*sc,h:r.height*sc}}
  Array.prototype.forEach.call(art.children,function(ch){var k=cslType(ch);if(!k)return;if(!ch.offsetHeight)return;var hd=/^H[2-5]$/.test(ch.tagName),nm=hd?cslTxt(ch):CSL_TN[k];
    if(k==="tk"){var ps=ch.querySelectorAll("p.tk");if(ps.length){Array.prototype.forEach.call(ps,function(p){var bu=p.querySelector(".bub")||p,g=geo(bu);if(!g.h)return;out.push({k:k,top:g.top,h:g.h,hd:false,name:nm,st:cslLook(bu)})});return}}
    var cs=getComputedStyle(ch),g=geo(ch),st;if(!g.h)return;
    if(hd)st="background:"+cs.color;
    else if(k==="tx"&&!cslVis(cs.backgroundColor)&&!(parseFloat(cs.borderLeftWidth)>=2))st="background:"+cslFade(cs.color);
    else st=cslLook(ch,cs,k==="tb"?[ch.querySelector("table"),ch.querySelector("td"),ch.querySelector("th")]:k==="fg"?[ch.querySelector("svg"),ch.querySelector("img")]:null);
    out.push({k:k,top:g.top,h:g.h,hd:hd,name:nm,st:st})});return out}
function cslPaint(box,bands,H){if(!box)return;var h="";bands.forEach(function(b){h+='<span class="csmap-b csmap-'+b.k+'" style="top:'+(b.top/H*100).toFixed(3)+'%;height:'+(b.h/H*100).toFixed(3)+'%;'+esc(b.st||"")+'"></span>'});box.innerHTML=h}
/* 配色・ライト/ダークの目印(変わったら節の地図を塗り直す) */
function cslSig(){var dk=false;try{dk=matchMedia("(prefers-color-scheme:dark)").matches}catch(e){}return (document.documentElement.getAttribute("data-theme")||"")+"|"+(document.body.getAttribute("data-pal")||"")+"|"+(dk?1:0)+"|"+(document.body.className.match(/\bpal-\S+/)||[""])[0]}"""

rep(OLD_BANDS, NEW_BANDS)
rep("var cur0=null,curH=0,curW=0,bands=[]", "var cur0=null,curH=0,curW=0,curS=\"\",bands=[]")
rep("if(a!==cur0||a.offsetHeight!==curH||a.offsetWidth!==curW){cur0=a;curH=a.offsetHeight;curW=a.offsetWidth;bands=cslBands(a);cslPaint(bx,bands,curH||1)}",
    "var sg=cslSig();if(a!==cur0||a.offsetHeight!==curH||a.offsetWidth!==curW||sg!==curS){cur0=a;curH=a.offsetHeight;curW=a.offsetWidth;curS=sg;bands=cslBands(a);cslPaint(bx,bands,curH||1)}")
open(out, "w", encoding="utf-8").write(s); print("ok")
