"""画面の下に固定したもの(下のタブ・問題集のボタン・戻るの帯など)が、ときどき画面の下に埋もれるのを直す。
  原因: claude.ai のアプリはページを枠(iframe)の中に表示し、アプリのツールバーの出し入れなどで、枠が実際に見えている範囲より
        縦に長くなることがある。position:fixed; bottom:0 は枠の下端に付くので、見えている範囲の外に出てしまう。
  直し方: 画面の下に透明の「見張り」(高さ240px、position:fixed; bottom:0)を置き、IntersectionObserver で、見張りのうち実際に
          見えている高さを測る(枠の外で切れた分も分かる)。切れた分を --vb-hide に入れ、下に固定したものをその分だけ持ち上げる。
  公開先では body が作り直されるため、見張りは body の外(html の直下)に置き、CSS はスクリプトで document.head に入れる。
使い方: python3 patch_vbottom.py <index.html> <出力>
"""
import sys, json
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
css = (".tabbar{bottom:var(--vb-hide,0px)!important;transition:bottom .15s}"
       "body.view-q #actions.qact{bottom:calc(10px + var(--vb-hide,0px) + env(safe-area-inset-bottom,0px))!important}"
       ".backpill,.qxback{bottom:calc(14px + var(--vb-hide,0px) + env(safe-area-inset-bottom,0px))!important}"
       "body.view-q .qxback,body.view-q.has-back .backpill{bottom:calc(84px + var(--vb-hide,0px) + env(safe-area-inset-bottom,0px))!important}"
       "body::after{content:\"\";display:block;height:var(--vb-hide,0px)}"
       "#cs-vb-probe{position:fixed;left:0;bottom:0;width:1px;height:240px;pointer-events:none;visibility:hidden;z-index:-1}")
JS = r"""(function(){if(window.__csVB)return;window.__csVB=1;
var st=document.createElement('style');st.id='cs-vbottom';st.textContent=__CSS__;document.head.appendChild(st);
if(!('IntersectionObserver' in window))return;
var H=240,last=-1,p=document.createElement('div');p.id='cs-vb-probe';p.setAttribute('aria-hidden','true');document.documentElement.appendChild(p);
function set(v){v=Math.round(v);if(v<2)v=0;if(v>200)v=0;if(v===last)return;last=v;document.documentElement.style.setProperty('--vb-hide',v+'px')}
var th=[];for(var i=0;i<=120;i++)th.push(i/120);
var io=new IntersectionObserver(function(es){var e=es[es.length-1];if(!e)return;
  var b=e.boundingClientRect,r=e.intersectionRect;
  /* 見張りの下端が切れている分 = 見張りの下端 - 見えている部分の下端(見えていなければ測らない) */
  if(!e.isIntersecting||r.height<=0){return}
  set(b.bottom-r.bottom)},{threshold:th});
io.observe(p);
/* body が作り直されても見張りは html の直下に残る。消えていたら戻す */
setInterval(function(){if(!p.isConnected){document.documentElement.appendChild(p);io.observe(p)}},3000);
})();"""
js = "<script>" + JS.replace("__CSS__", json.dumps(css)) + "</script>"
if s.count("</head>") != 1: sys.exit("</head> が1件ではない")
s = s.replace("</head>", js + "</head>")
open(out, "w", encoding="utf-8").write(s); print("ok")
