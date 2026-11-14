"""本文の文字を選んで「質問」から AI先生に聞いた回答を「保存」すると、その文字のマーカーに「AIのメモ」として残す。
  - 選んだ範囲を覚えておき(window.__askHL)、その項目の AI先生で、選んだ文字を含む質問の回答を保存したときにマーカーへ入れる
    (同じ所にマーカーがあればそれに足す。なければ黄色のマーカーを引く)。それ以外の質問の保存は、これまでどおり「保存した回答」へ
  - マーカーを押したときの編集パネルに「AIのメモ」(質問と回答)を出し、1つずつ消せる。自分用メモとは別
  - AIのメモのあるマーカーには小さな印(hai)。マーカーと同じくアカウントに保存・同期(notes.hl の ai)
  - 保存を解除すると AIのメモも消える(自動で引いたマーカーで、ほかにメモがなければマーカーも消す)
  公開先では body が作り直されるため、CSS はスクリプトで document.head に入れる。
使い方: python3 patch_ask_marker.py <index.html> <出力>
"""
import sys
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count: sys.exit(f"置換対象が {n} 件(期待 {count} 件): {old[:90]!r}")
    s = s.replace(old, new)
# A: 「質問」を押したときに選んだ範囲を覚える
rep('else if(b.dataset.x==="ask"){if(selFeat&&selFeat._ask&&selFeat._ask._open){',
    'else if(b.dataset.x==="ask"){hlAskCapture();if(selFeat&&selFeat._ask&&selFeat._ask._open){')
# B: マーカーに AIのメモを入れる・消す
HELP = r'''function hlAskCapture(){try{var f=selFeat;window.__askHL=null;if(!f||!selRange)return;var ns=tnodes(f),s=posOf(ns,selRange.startContainer,selRange.startOffset),e=posOf(ns,selRange.endContainer,selRange.endOffset);
  var full=ns.map(function(n){return n.nodeValue}).join("");while(s<e&&/\s/.test(full[s]))s++;while(e>s&&/\s/.test(full[e-1]))e--;if(e<=s)return;
  window.__askHL={f:f.id,s:s,t:full.slice(s,e),ts:Date.now()}}catch(x){window.__askHL=null}}
/* 保存した回答を、選んだ文字のマーカーの「AIのメモ」に入れる。戻り値: {h:マーカーid,ts} */
window.__hlAI=function(p,q,a){try{var f=byId(p.f);if(!f||!p.t)return null;var ns=tnodes(f),full=ns.map(function(n){return n.nodeValue}).join(""),s=p.s;
  if(full.slice(s,s+p.t.length)!==p.t){s=full.indexOf(p.t);if(s<0)return null}
  var probe={f:f.id,s:s,t:p.t},hit=Object.keys(notes.hl).map(function(k){return notes.hl[k]}).filter(function(x){return hlOverlap(x,probe)})[0],h=hit;
  if(!h){h={id:"h"+Date.now().toString(36)+Math.random().toString(36).slice(2,5),f:f.id,s:s,t:p.t,c:"y",note:"",ts:Date.now(),title:f.dataset.title||titleOf(f),auto:1};notes.hl[h.id]=h;wrapRange(ns,s,s+p.t.length,h)}
  if(!Array.isArray(h.ai))h.ai=[];var ts=Date.now();h.ai.push({q:String(q||""),a:String(a||""),ts:ts});h.ts=ts;setMarkClass(h);nSave();
  if(popId===h.id)popMode(false);toast("マーカーに「AIのメモ」として保存しました");return {h:h.id,ts:ts}}catch(x){return null}};
window.__hlAIdel=function(hid,ts){try{var h=notes.hl[hid];if(!h||!Array.isArray(h.ai))return;h.ai=h.ai.filter(function(x){return x.ts!==ts});h.ts=Date.now();
  if(!h.ai.length&&h.auto&&!h.note){if(popId===hid)closePop();dropHL([hid])}else{setMarkClass(h);if(popId===hid)popMode(false)}nSave()}catch(x){}};
'''
rep('sb.addEventListener("click",function(e){\n  var b=e.target.closest("button");if(!b)return;\n  if(b.dataset.c)addHL(b.dataset.c,false);',
    HELP + 'sb.addEventListener("click",function(e){\n  var b=e.target.closest("button");if(!b)return;\n  if(b.dataset.c)addHL(b.dataset.c,false);')
# C/E: 印
rep('m.classList.toggle("hn",!!h.note)})}', 'm.classList.toggle("hn",!!h.note);m.classList.toggle("hai",!!(h.ai&&h.ai.length))})}')
rep('m.className="hl hl-"+h.c+(h.note?" hn":"");', 'm.className="hl hl-"+h.c+(h.note?" hn":"")+(h.ai&&h.ai.length?" hai":"");')
# D: 編集パネルに AIのメモ
rep('function popMode(e){\n  var h=popId&&notes.hl[popId];if(!h)return;popEditing=e;',
    '''function popAI(h){var box=pop.querySelector(".hp-ai");if(!box){box=document.createElement("div");box.className="hp-ai";var v0=pop.querySelector(".hp-view");v0.parentNode.insertBefore(box,v0)}
  var L=Array.isArray(h.ai)?h.ai:[];box.hidden=!L.length;
  box.innerHTML=L.length?'<p class="hp-ai-k">AIのメモ</p>'+L.map(function(x){return '<div class="hp-ai-i"><p class="hp-ai-q">'+esc(x.q)+'</p><div class="hp-ai-a">'+esc(x.a)+'</div><button type="button" class="chip hp-ai-del" data-aits="'+x.ts+'">このAIのメモを消す</button></div>'}).join(""):""}
pop.addEventListener("click",function(ev){var d=ev.target.closest&&ev.target.closest(".hp-ai-del");if(!d||!popId)return;ev.stopPropagation();if(confirm("このAIのメモを消しますか?"))window.__hlAIdel(popId,+d.dataset.aits)},true);
function popMode(e){
  var h=popId&&notes.hl[popId];if(!h)return;popEditing=e;popAI(h);''')
# F: 選んだ文字からの質問の回答は、マーカーへ保存
rep('''      if(sid){await window.__qa.remove(sid);sid=null;b.textContent="この回答を保存"}
      else{sid=await window.__qa.add({feat:o.featId,featTitle:o.featTitle,q:q,a:a,src:o.src,qn:o.qn});b.textContent="保存済み(押すと解除)"}''',
'''      if(hk){window.__hlAIdel(hk.h,hk.ts);hk=null;b.textContent=lbl0}
      else if(sid){await window.__qa.remove(sid);sid=null;b.textContent="この回答を保存"}
      else if(pk){hk=window.__hlAI(pk,q,a);if(hk)b.textContent="マーカーに保存済み(押すと解除)";else{sid=await window.__qa.add({feat:o.featId,featTitle:o.featTitle,q:q,a:a,src:o.src,qn:o.qn});b.textContent="保存済み(押すと解除)"}}
      else{sid=await window.__qa.add({feat:o.featId,featTitle:o.featTitle,q:q,a:a,src:o.src,qn:o.qn});b.textContent="保存済み(押すと解除)"}''')
rep('''  var b=document.createElement("button");b.type="button";b.className="chip qsave";b.textContent="この回答を保存";
  var sid=null;''',
'''  var b=document.createElement("button");b.type="button";b.className="chip qsave";b.textContent="この回答を保存";
  var sid=null,hk=null,pk=null,P=window.__askHL;
  if(P&&P.f===o.featId&&typeof window.__hlAI==="function"&&String(q).indexOf(P.t)>=0&&Date.now()-P.ts<36e5)pk={f:P.f,s:P.s,t:P.t};
  var lbl0=pk?"マーカーにAIのメモとして保存":"この回答を保存";b.textContent=lbl0;''')
css = (".hlpop>.hp-ai{flex:0 1 auto;overflow-y:auto;-webkit-overflow-scrolling:touch;overscroll-behavior:contain;max-height:48vh;margin:0 0 8px;min-height:3em}"
       ".hp-ai-k{margin:0 0 6px;font-size:12px;font-weight:700;color:var(--sub,#666);letter-spacing:.04em}"
       ".hp-ai-i{border:1px solid color-mix(in srgb,var(--brand,#1d4a6e) 30%,var(--line,#ddd));background:color-mix(in srgb,var(--brand,#1d4a6e) 7%,var(--surface,#fff));border-radius:10px;padding:8px 10px;margin:0 0 8px}"
       ".hp-ai-q{margin:0 0 4px;font-size:12.5px;font-weight:700;color:var(--sub,#555);overflow-wrap:anywhere}"
       ".hp-ai-a{white-space:pre-wrap;overflow-wrap:anywhere;font-size:14px;line-height:1.75}"
       ".hp-ai-del{margin-top:6px;font-size:12px}"
       "mark.hl.hai.hl-end::after{content:\"AI\";display:inline-block;margin-left:2px;padding:0 3px;border-radius:4px;font-size:9px;font-weight:800;line-height:1.5;vertical-align:super;background:var(--brand,#1d4a6e);color:#fff}"
       "mark.hl.hn.hai.hl-end::after{content:\"メモ・AI\";background:var(--brand,#1d4a6e)}")
js = "<script>(function(){if(document.getElementById('cs-ask-marker'))return;var st=document.createElement('style');st.id='cs-ask-marker';st.textContent=" + __import__("json").dumps(css).replace("</", "<\\/") + ";document.head.appendChild(st)})();</script>"
if s.count("</head>") != 1: sys.exit("</head> が1件ではない")
s = s.replace("</head>", js + "</head>")
open(out, "w", encoding="utf-8").write(s); print("ok")
