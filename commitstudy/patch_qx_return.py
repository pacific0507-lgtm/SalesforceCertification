"""本文の「問題 N」(この箇所の問題)から問題へ移ったあと:
  - 問題の画面の左下に「← テキストに戻る」を出す。押すと、移る前と同じ本文の位置に戻り、「この箇所の問題」の一覧を開き直す
    (一覧の正解の印も、そのとき解いた結果に更新される)
  - テキストに戻ったときは、本文の「問題 N」の印を作り直す。その箇所の問題をすべて正解したら、読み込み直さなくても緑になる
  公開先では body が作り直されるため、CSS はスクリプトで document.head に入れる。
使い方: python3 patch_qx_return.py <index.html> <出力>
"""
import sys, json
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count: sys.exit(f"置換対象が {n} 件(期待 {count} 件): {old[:90]!r}")
    s = s.replace(old, new)
rep('if(b.dataset.n){var n=+b.dataset.n;closeQx();setView("quiz");jumpTo(n)}});',
    '''if(b.dataset.n){var n=+b.dataset.n,qk=qxAt?qxAt.dataset.qx:null;closeQx();setView("quiz");jumpTo(n);qxShowBack(qk)}});
var qxBackK=null;
function qxShowBack(k){qxBackK=k;var el=document.getElementById("qxback");if(el)el.remove();if(!k)return;
  el=document.createElement("div");el.id="qxback";el.className="qxback";el.setAttribute("role","navigation");el.setAttribute("aria-label","テキストに戻る");
  el.innerHTML='<button type="button" class="qxb-go"><span aria-hidden="true">←</span> テキストに戻る</button><button type="button" class="qxb-x" aria-label="戻るボタンを閉じる">×</button>';
  document.body.appendChild(el);document.body.classList.add("has-qxback");
  el.querySelector(".qxb-go").onclick=function(){setView("text")};
  el.querySelector(".qxb-x").onclick=function(){qxBackK=null;el.remove();document.body.classList.remove("has-qxback")}}
var qxSetView0=setView;
setView=function(v){var k=qxBackK,r=qxSetView0.apply(this,arguments);
  if(!(v==="quiz"||v==="q")){try{mountQx()}catch(e){}
    if(k){qxBackK=null;var el=document.getElementById("qxback");if(el)el.remove();document.body.classList.remove("has-qxback");
      setTimeout(function(){try{mountQx();var b=null;$$("#chapters .qx-b").forEach(function(x){if(x.dataset.qx===k)b=x});if(b){var r2=b.getBoundingClientRect();if(r2.top<70||r2.bottom>window.innerHeight-20)b.scrollIntoView({block:"center"});b.classList.add("qx-flash");setTimeout(function(){b.classList.remove("qx-flash")},1600);openQx(b)}}catch(e){}},120)}}
  return r};''')
css = (".qxback{position:fixed;z-index:65;left:12px;bottom:calc(14px + env(safe-area-inset-bottom,0px));display:flex;align-items:center;gap:4px;max-width:calc(100vw - 24px);background:var(--ink,#1a1a1a);color:var(--surface,#fff);border-radius:999px;padding:4px 4px 4px 14px;box-shadow:0 8px 24px rgba(0,0,0,.25)}"
       ".qxback .qxb-go{border:0;background:none;color:inherit;font:inherit;font-weight:700;font-size:14px;white-space:nowrap;padding:6px 4px;cursor:pointer}"
       ".qxback .qxb-x{flex:none;width:30px;height:30px;border-radius:50%;border:0;background:rgba(255,255,255,.16);color:inherit;font-size:16px;line-height:1;cursor:pointer}"
       "body:not(.view-q) .qxback{display:none}"
       "body.view-q.has-qxback{padding-bottom:64px}"
       ".qx-b.qx-flash{box-shadow:0 0 0 4px color-mix(in srgb,var(--accent,#1d4a6e) 30%,transparent)}")
js = "<script>(function(){if(document.getElementById('cs-qx-return'))return;var st=document.createElement('style');st.id='cs-qx-return';st.textContent=" + json.dumps(css) + ";document.head.appendChild(st)})();</script>"
if s.count("</head>") != 1: sys.exit("</head> が1件ではない")
s = s.replace("</head>", js + "</head>")
open(out, "w", encoding="utf-8").write(s); print("ok")
