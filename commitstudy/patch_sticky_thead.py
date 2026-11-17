"""テキスト・問題の表で、表の見出し行(thead)を画面の上に追従させる。
  表は横にスクロールする枠(.tw / .qb-tw、overflow-x:auto)の中にあり、position:sticky が効かないので、
  見出し行の写しを画面の上(上のメニューの下)に固定して出す。
  - 表の上端がメニューの下に隠れ、表の下端がまだ見えているあいだだけ出す
  - 列の幅は元の表に合わせ、表を横にスクロールすると写しも同じだけずらす
  - 上のメニュー(#mbar)が隠れているときは画面の一番上に出す
  公開先では body が作り直されるため、CSS はスクリプトで document.head に入れる。写しは表と同じ項目(.feat)の中に置く(項目の余白や色の指定がそのまま効くように)。
使い方: python3 patch_sticky_thead.py <index.html> <出力>
"""
import sys, json
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
css = ("#cs-sth{position:fixed;z-index:55;overflow:hidden;pointer-events:none;box-shadow:0 6px 12px -8px rgba(0,0,0,.35);border-radius:0 0 8px 8px}"
       "#cs-sth[hidden]{display:none}"
       "#cs-sth .tw,#cs-sth .qb-tw{margin:0!important;padding:0!important;border:0!important;box-shadow:none!important;background:none!important}"
       "#cs-sth table{margin:0!important;table-layout:fixed;border-collapse:collapse}"
       "#cs-sth th{box-sizing:border-box}")
JS = r"""(function(){if(window.__csSth)return;window.__csSth=1;
var st=document.createElement('style');st.id='cs-sticky-thead';st.textContent=__CSS__;document.head.appendChild(st);
var box=null,cur=null,curW=null,raf=0;
function topOff(){var m=document.getElementById('mbar');if(!m)return 0;var r=m.getBoundingClientRect();return r.bottom>0&&r.top<=0.5?r.bottom:0}
function ensure(par){if(!box){box=document.createElement('div');box.id='cs-sth';box.hidden=true}if(box.parentNode!==par){par.appendChild(box);cur=null}return box}
function hide(){if(box){box.hidden=true}cur=null}
function build(t,w){var b=ensure(t.closest('.feat')||t.closest('.qc')||document.body);cur=t;curW=w;
  /* 元の表と同じ見た目になるよう、表の親(.tw / .qb-tw)と同じクラスの入れ物に入れる */
  var wrap=document.createElement('div');wrap.className=w.className;wrap.style.cssText='overflow:visible;margin:0;padding:0;border:0';
  var tb=document.createElement('table');tb.className=t.className;var th=t.tHead.cloneNode(true);tb.appendChild(th);wrap.appendChild(tb);
  b.innerHTML='';b.appendChild(wrap);
  var src=t.tHead.rows[0]?t.tHead.rows[0].cells:[],dst=th.rows[0]?th.rows[0].cells:[];
  for(var i=0;i<dst.length&&i<src.length;i++){var cw=src[i].getBoundingClientRect().width;dst[i].style.width=cw+'px';dst[i].style.minWidth=cw+'px';dst[i].style.maxWidth=cw+'px';
    /* 色は元の見出しのセルと同じにする(セルが透明なら、行・表・項目と上へたどって最初に色のある背景) */
    var cs=getComputedStyle(src[i]),bg=cs.backgroundColor,el=src[i];
    while((!bg||bg==='transparent'||/rgba\([^)]*,\s*0\)$/.test(bg))&&el.parentElement){el=el.parentElement;bg=getComputedStyle(el).backgroundColor}
    dst[i].style.backgroundColor=bg;dst[i].style.color=cs.color;dst[i].style.borderBottom=cs.borderBottom}
  tb.style.width=t.getBoundingClientRect().width+'px'}
function tick(){raf=0;try{
  var off=topOff(),list=document.querySelectorAll('.feat .tw > table, .qb-tw > table'),hit=null,hw=null;
  for(var i=0;i<list.length;i++){var t=list[i];if(box&&box.contains(t))continue;if(!t.tHead||!t.tHead.rows.length)continue;var r=t.getBoundingClientRect();if(!r.height)continue;
    var hh=t.tHead.getBoundingClientRect().height;if(r.top<off&&r.bottom>off+hh+8){hit=t;hw=t.parentElement;break}}
  if(!hit){hide();return}
  if(hit!==cur||!box||!box.isConnected)build(hit,hw);
  var wr=hw.getBoundingClientRect();box.hidden=false;box.style.top=off+'px';box.style.left=wr.left+'px';box.style.width=wr.width+'px';
  var tb=box.querySelector('table');if(tb)tb.style.transform='translateX('+(-hw.scrollLeft)+'px)';
}catch(e){hide()}}
function req(){if(!raf)raf=requestAnimationFrame(tick)}
window.addEventListener('scroll',req,{passive:true});window.addEventListener('resize',function(){cur=null;req()});
document.addEventListener('scroll',function(e){if(e.target&&e.target.classList&&(e.target.classList.contains('tw')||e.target.classList.contains('qb-tw')))req()},{passive:true,capture:true});
setInterval(req,1500);
})();"""
js = "<script>" + JS.replace("__CSS__", json.dumps(css)) + "</script>"
if s.count("</head>") != 1: sys.exit("</head> が1件ではない")
s = s.replace("</head>", js + "</head>")
open(out, "w", encoding="utf-8").write(s); print("ok")
