"""問題とテキストを「該当箇所」で結ぶパッチ。
  問題データの x(本文中の該当する文。xs があればその項目)を使い、
  1. 問題の「テキストで復習する」→ その箇所までスクロールし、黄色で光らせる(見つからなければ項目の先頭)
  2. 本文の該当箇所の末尾に「問題 N」の印を付け、押すとその箇所の問題を一覧して、問題へ飛べる
使い方: python3 patch_qx.py <index.html> <出力>
"""
import json, sys
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count: sys.exit(f"置換対象が {n} 件(期待 {count} 件): {old[:90]!r}")
    s = s.replace(old, new)
def jesc(t): return json.dumps(t, ensure_ascii=False)[1:-1].replace("</", "<\\/")

CSS = """
/* 問題とテキストの該当箇所 */
::highlight(qx){background-color:rgba(255,200,0,.6);color:inherit}
.qx-flash{animation:qxf 2.6s ease-out 1}
@keyframes qxf{0%,55%{box-shadow:0 0 0 3px var(--star);border-radius:6px;background:var(--yama-soft)}100%{box-shadow:0 0 0 3px transparent}}
.qx-b{display:inline-flex;align-items:center;gap:3px;vertical-align:1px;margin-left:6px;border:1px solid var(--accent);background:var(--surface);color:var(--accent);border-radius:999px;padding:0 8px;font:inherit;font-size:11.5px;font-weight:700;line-height:1.7;cursor:pointer;white-space:nowrap}
.qx-b:hover{background:var(--accent);color:var(--accent-ink)}
.qx-b svg{width:12px;height:12px;fill:none;stroke:currentColor;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round}
.qx-b.done{border-color:var(--ok);color:var(--ok)}
body.review .qx-b,body.sheet .qx-b{display:none}
.totext .tt .qx-s{display:block;font-weight:500;font-size:13px;color:var(--muted);overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
"""
anchor = "body.review .co.talk{display:none}\n"
rep(jesc(anchor), jesc(anchor + CSS))

# normQ に x / xs を通す
rep('var o={n:id,t:"mc",q:d.q,qe:d.qe||"",o:d.o,oe:d.oe||[],a:(d.a||[]).map(Number),v:d.v||"",c:typeof d.c==="number"?d.c:null,u:d.u||"",cite:"",exam:""};',
    'var o={n:id,t:"mc",q:d.q,qe:d.qe||"",o:d.o,oe:d.oe||[],a:(d.a||[]).map(Number),v:d.v||"",c:typeof d.c==="number"?d.c:null,u:d.u||"",cite:"",exam:"",x:d.x||"",xs:d.xs||""};')

# 問題 → テキストのリンク
TOTEXT_OLD = """$("#qtext").innerHTML='<a href="#" class="totext" data-act="totext" data-f="'+esc(q.s)+'"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 5.5C5.5 4 8.5 4 12 6c3.5-2 6.5-2 9-.5V19c-2.5-1.5-5.5-1.5-9 .5-3.5-2-6.5-2-9-.5z"/><path d="M12 6v13.5"/></svg><span class="tt"><small>テキストで復習する</small>'+dk(q.s)+" "+esc(TITLES[q.s]||"")+'</span><span class="ar" aria-hidden="true">→</span></a>';"""
TOTEXT_NEW = """var xsec=q.x?(q.xs||q.s):q.s;$("#qtext").innerHTML='<a href="#" class="totext" data-act="totext" data-f="'+esc(xsec)+'" data-q="'+q.n+'"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 5.5C5.5 4 8.5 4 12 6c3.5-2 6.5-2 9-.5V19c-2.5-1.5-5.5-1.5-9 .5-3.5-2-6.5-2-9-.5z"/><path d="M12 6v13.5"/></svg><span class="tt"><small>'+(q.x?"テキストの該当箇所で復習する":"テキストで復習する")+'</small>'+dk(xsec)+" "+esc(TITLES[xsec]||"")+(q.x?'<span class="qx-s">「'+esc(q.x.length>42?q.x.slice(0,42)+"…":q.x)+'」</span>':"")+'</span><span class="ar" aria-hidden="true">→</span></a>';"""
rep(TOTEXT_OLD, TOTEXT_NEW)
rep('else if(act==="totext"){e.preventDefault();goText(t.dataset.f)}',
    'else if(act==="totext"){e.preventDefault();goText(t.dataset.f,t.dataset.q?QMAP[+t.dataset.q]:null)}')

GOTEXT_NEW = r'''function goText(sec,q){setView("text");if(sec)setTimeout(function(){if(!(q&&q.x&&qxShow(sec,q.x)))jump("f-"+sec)},40)}
/* ==該当箇所== 問題データの x(本文中の文)を項目の本文から探す。見つからなければ null(項目の先頭に飛ぶ) */
function qxRange(sec,x){var f=byId("f-"+sec);if(!f||!x)return null;var ns=tnodes(f),full=ns.map(function(n){return n.nodeValue}).join(""),i=full.indexOf(x);if(i<0)return null;
  var e=i+x.length,p=0,r=document.createRange(),st=false;
  for(var k=0;k<ns.length;k++){var L=ns[k].length;if(!st&&i<p+L){r.setStart(ns[k],i-p);st=true}if(st&&e<=p+L){r.setEnd(ns[k],e-p);return r}p+=L}return null}
function qxBlock(r){var n=r.endContainer;n=n.nodeType===1?n:n.parentElement;return n?n.closest("p,li,tr,figcaption,blockquote,summary"):null}
var qxT=null;
function qxShow(sec,x){var r=qxRange(sec,x);if(!r)return false;hold(1200);
  var b=r.getBoundingClientRect(),top=window.scrollY+b.top-Math.max(90,window.innerHeight*0.3);window.scrollTo(0,Math.max(0,top));
  try{if(window.CSS&&CSS.highlights&&window.Highlight){CSS.highlights.set("qx",new Highlight(r));clearTimeout(qxT);qxT=setTimeout(function(){CSS.highlights.delete("qx")},4500)}}catch(e){}
  var bl=qxBlock(r);if(bl){bl.classList.remove("qx-flash");void bl.offsetWidth;bl.classList.add("qx-flash");setTimeout(function(){bl.classList.remove("qx-flash")},2700)}
  return true}
/* 本文の該当箇所に「問題 N」の印を付ける(押すと、その箇所の問題を一覧する) */
var QXM={};
function mountQx(){
  $$("#chapters .qx-b").forEach(function(b){b.remove()});QXM={};if(!Q.length||!Object.keys(TITLES).length)return;
  Q.forEach(function(q){if(!q.x)return;var k=(q.xs||q.s)+"|"+q.x;(QXM[k]=QXM[k]||[]).push(q.n)});
  Object.keys(QXM).forEach(function(k){var i=k.indexOf("|"),sec=k.slice(0,i),x=k.slice(i+1),r=qxRange(sec,x);if(!r)return;var bl=qxBlock(r);if(!bl)return;
    if(bl.tagName==="TR"){var cs=bl.querySelectorAll("td,th");bl=cs[cs.length-1]||bl}
    var ns=QXM[k],done=ns.every(function(n){var h=histOf(n);return h&&h.l==="o"});
    var b=document.createElement("button");b.type="button";b.className="qx-b"+(done?" done":"");b.dataset.qx=k;b.title="この箇所の問題";b.setAttribute("aria-label","この箇所の問題 "+ns.length+"問");
    b.innerHTML='<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 20l4-1L19 8l-3-3L5 16z"/></svg>問題 '+ns.length;bl.appendChild(b)});
}
var qxp=document.createElement("div");qxp.className="hlpop pmpop qxpop";qxp.hidden=true;qxp.setAttribute("role","dialog");qxp.setAttribute("aria-label","この箇所の問題");document.body.appendChild(qxp);
var qxAt=null;
function openQx(b){qxAt=b;var ns=(QXM[b.dataset.qx]||[]).map(function(n){return QMAP[n]}).filter(Boolean).sort(function(a,c){return dno(a)-dno(c)});
  var h='<div class="hp-top"><b>この箇所の問題('+ns.length+'問)</b><button class="x-close" type="button" data-x="close" aria-label="閉じる">×</button></div>';
  ns.forEach(function(q){var t=String(q.q);h+='<button class="pm-q" type="button" data-n="'+q.n+'"><small><span>問'+dno(q)+'</span><span>'+esc(q.exam||"")+'</span>'+pmHist(q.n)+'</small>'+esc(t.length>80?t.slice(0,80)+"…":t)+'</button>'});
  qxp.innerHTML=h;qxp.hidden=false;
  if(window.matchMedia&&matchMedia("(pointer:coarse)").matches){qxp.classList.add("sheetpos");return}
  qxp.classList.remove("sheetpos");var r=b.getBoundingClientRect(),vh=window.innerHeight,vw=document.documentElement.clientWidth,pw=qxp.offsetWidth||340,ph=qxp.offsetHeight||200;
  var top=r.bottom+8;if(top+ph>vh-8)top=Math.max(66,r.top-ph-8);qxp.style.top=top+"px";qxp.style.left=Math.max(8,Math.min(r.left,vw-pw-8))+"px"}
function closeQx(){qxp.hidden=true;qxAt=null}
document.addEventListener("click",function(e){var b=e.target.closest&&e.target.closest(".qx-b");if(!b)return;e.preventDefault();e.stopPropagation();if(qxAt===b&&!qxp.hidden){closeQx();return}openQx(b)},true);
qxp.addEventListener("click",function(e){var b=e.target.closest("button");if(!b)return;if(b.dataset.x==="close"){closeQx();return}
  if(b.dataset.n){var n=+b.dataset.n;closeQx();setView("quiz");jumpTo(n)}});
document.addEventListener("pointerdown",function(e){if(!qxp.hidden&&!qxp.contains(e.target)&&!(e.target.closest&&e.target.closest(".qx-b")))closeQx()});
document.addEventListener("keydown",function(e){if(e.key==="Escape")closeQx()});
window.addEventListener("scroll",function(){if(!qxp.hidden&&!qxp.classList.contains("sheetpos")&&qxAt){var r=qxAt.getBoundingClientRect();qxp.style.top=Math.max(66,r.bottom+8)+"px"}},{passive:true});'''
rep('function goText(sec){setView("text");if(sec)setTimeout(function(){jump("f-"+sec)},40)}', GOTEXT_NEW)

# 印を付けるタイミング: 本文の準備後と、問題の読み込み後
rep('markKaisei();try{mountTalk()}catch(e){}mountMemos();applyHL();renderQaInline();',
    'markKaisei();try{mountTalk()}catch(e){}mountMemos();applyHL();renderQaInline();try{mountQx()}catch(e){}')
rep('  buildDeck();updateCounts();renderAll();\n}', '  buildDeck();updateCounts();renderAll();try{mountQx()}catch(e){}\n}')
open(out, "w", encoding="utf-8").write(s); print("ok")
