"""節の重要度(社労士版から移植): 節の見出しに「★★★ 頻出」「★★ よく出る」「★ 出題少なめ」の印、目次の各行の右に小さな星。
  - データは make_imp.py が過去問から作る data/<科目>/imp.json(公開先も data/<科目>/imp.json)。テキストを組み立てたとき
    (initText の最後)に、科目ごとに1回だけ読む(famURL があればそれを通す)。afsvc のように過去問がない科目は secs が空で、何も出さない。
  - 見出し(.feat>h3)の末尾(英語のタグのあと)に button.imp を足す。ボタンなので、マーカー・メモの位置(tnodes)・検索には数えない。
    色: 頻出=朱色、よく出る=テーマの色(--accent)、出題少なめ=灰色。
  - 印を押すと、印のすぐ下に小さな枠(document.body に置く position:fixed の .imp-pop。本文の中には入れないので、マーカーの位置は変わらない)。
    どの回(版)に何問出たか、科目の中で何位か、★の決め方を出す。もう一度押す・枠の外を押す・Esc で閉じる。スクロールでは印について動き、
    印が画面の外に出たら閉じる。
  - 目次(メニューの目次 #toc-list の各行と、PC の左の目次 #toc-ol)の行の右に、小さな星(span.imp-mini、文字なし)。
  - titleOf(目次・しおりの名前など)・いまの節の表示(patch_secband.py の txt)・テキストのこの場所の文(cslTxt)・AI先生に渡す本文(featText)は、
    印の文字を数えない。
  - 表示の設定に「節の重要度(★): 表示する/表示しない」(prefs.imp、はじめは表示する)。表示しないときは body.imp-off で印・星・枠を隠す。
  公開先では body が作り直されるため、CSS はスクリプトで document.head に入れる。
使い方: python3 patch_imp.py <index.html> <出力>
"""
import sys, json
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count: sys.exit(f"置換対象が {n} 件(期待 {count} 件): {old[:90]!r}")
    s = s.replace(old, new)

CSS = r"""
:root{--imp-hi:#d4461f}
html[data-theme=dark]{--imp-hi:#ff8a62}
@media (prefers-color-scheme:dark){html:not([data-theme=light]){--imp-hi:#ff8a62}}
.feat h3 .imp{display:inline-flex;align-items:center;gap:3px;vertical-align:.12em;margin:0 0 0 6px;padding:1px 8px 1px 7px;border:1px solid currentColor;border-radius:999px;background:transparent;font-family:var(--f-body);font-size:11.5px;font-weight:700;line-height:1.55;letter-spacing:0;white-space:nowrap;cursor:pointer;-webkit-tap-highlight-color:transparent;color:var(--muted)}
.feat h3 .imp i{font-style:normal;letter-spacing:-.06em}
.feat h3 .imp.imp3{color:var(--imp-hi);background:color-mix(in srgb,var(--imp-hi) 9%,transparent)}
.feat h3 .imp.imp2{color:var(--accent);background:color-mix(in srgb,var(--accent) 8%,transparent)}
.feat h3 .imp[aria-expanded=true]{box-shadow:0 0 0 2px color-mix(in srgb,currentColor 25%,transparent)}
.feat h3 .imp:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.imp-mini{flex:none;align-self:center;margin-left:6px;font-size:9.5px;line-height:1;letter-spacing:-.08em;font-weight:700;color:var(--muted);white-space:nowrap}
.imp-mini.imp3{color:var(--imp-hi)}
.imp-mini.imp2{color:var(--accent)}
nav.toc a .imp-mini{margin-left:auto}
nav.toc a .imp-mini+.td{margin-left:4px}
#imp-pop{position:fixed;z-index:70;left:16px;top:0;width:min(340px,calc(100vw - 32px));box-sizing:border-box;max-height:min(46vh,340px);overflow:auto;-webkit-overflow-scrolling:touch;padding:10px 12px 11px;border:1px solid var(--line);border-radius:12px;background:var(--surface,#fff);color:var(--ink);box-shadow:0 8px 24px rgba(0,0,0,.18);font-family:var(--f-body);font-size:12.5px;font-weight:400;line-height:1.65;text-align:left}
#imp-pop[hidden]{display:none}
#imp-pop .imp-ph{display:flex;align-items:baseline;gap:8px;margin:0 0 4px;font-size:13px;font-weight:700}
#imp-pop .imp-ph b{white-space:nowrap}
#imp-pop .imp-ph b.imp3{color:var(--imp-hi)}#imp-pop .imp-ph b.imp2{color:var(--accent)}#imp-pop .imp-ph b.imp1{color:var(--muted)}
#imp-pop .imp-ph span{color:var(--muted);font-size:12px;font-weight:600;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
#imp-pop p{margin:0 0 6px}
#imp-pop .imp-u{display:flex;flex-wrap:wrap;gap:4px 5px;margin:0 0 7px;padding:0;list-style:none}
#imp-pop .imp-u li{font-size:11.5px;line-height:1.5;padding:0 7px;border-radius:999px;background:color-mix(in srgb,var(--line) 60%,transparent);white-space:nowrap}
#imp-pop .imp-rule{margin:0;color:var(--muted);font-size:11.5px;line-height:1.6}
body.imp-off .feat h3 .imp,body.imp-off .imp-mini,body.imp-off #imp-pop{display:none!important}
"""

JS = r"""
/* ==節の重要度== 過去問から計算した data/<科目>/imp.json を読み、節の見出しと目次に星を出す */
var IMP={sid:null,d:null,p:null},IMP_LB={3:"頻出",2:"よく出る",1:"出題少なめ"};
function impSid(){return (window.FAMV&&FAMV.id)||"d360"}
function impOf(sec){var d=IMP.d;return d&&d.secs&&sec?d.secs[sec]||null:null}
function impStars(lv){return lv===3?"★★★":lv===2?"★★":"★"}
function impLoad(){var sid=impSid();if(IMP.sid===sid&&IMP.p)return IMP.p;IMP.sid=sid;IMP.d=null;IMP.ok=false;var u="data/"+sid+"/imp.json";
  IMP.p=fetch(window.famURL?famURL(u):u).then(function(r){return r.ok?r.json():null}).catch(function(){return null}).then(function(d){if(IMP.sid===sid)IMP.d=d&&d.secs&&Object.keys(d.secs).length?d:null;return IMP.d});return IMP.p}
function impMini(b,f){var o=impOf(f&&f.dataset&&f.dataset.sec);if(!o)return;var m=sp("imp-mini imp"+o.lv,impStars(o.lv));m.title="節の重要度: "+impStars(o.lv)+" "+IMP_LB[o.lv];b.appendChild(m)}
function impDeco(){impClose();
  $$("#chapters .feat[data-sec]").forEach(function(f){var h=f.querySelector(":scope>h3");if(!h)return;var old=h.querySelector(":scope>.imp");if(old)old.remove();var o=impOf(f.dataset.sec);if(!o)return;
    var b=document.createElement("button");b.type="button";b.className="imp imp"+o.lv;b.dataset.imp=f.dataset.sec;b.setAttribute("aria-expanded","false");
    b.setAttribute("aria-label","節の重要度: "+impStars(o.lv)+" "+IMP_LB[o.lv]+"。押すと出題された回を表示");b.innerHTML='<i aria-hidden="true">'+impStars(o.lv)+"</i>"+IMP_LB[o.lv];h.appendChild(b)});
  $$("#toc-ol a[data-t]").forEach(function(a){var x=a.querySelector(".imp-mini");if(x)x.remove();var f=byId(a.dataset.t);if(!f||!f.dataset.sec)return;var o=impOf(f.dataset.sec);if(!o)return;
    var m=sp("imp-mini imp"+o.lv,impStars(o.lv));m.title="節の重要度: "+IMP_LB[o.lv];a.insertBefore(m,a.querySelector(".td"))})}
function impApply(){var sid=impSid();if(IMP.sid===sid&&IMP.ok){impDeco();return}
  impLoad().then(function(){if(impSid()!==sid)return;IMP.ok=true;impDeco();if(IMP.d&&typeof render==="function")try{render()}catch(e){}})}
/* 押したときの枠 */
function impText(sec,o){var d=IMP.d,u=o.u||[],h="";
  var head=d.head||"";
  if(d.mode==="round"){if(o.r)h+="<p>"+esc(head)+"のうち、<b>"+o.r+"回</b>で出題(計"+o.n+"問)</p>";else h+="<p>"+esc(head)+"では、この節からの出題はありません。</p>"}
  else{if(o.n)h+="<p>"+esc(head)+"のうち、<b>"+o.n+"問</b>で出題</p>";else h+="<p>"+esc(head)+"では、この節からの出題はありません。</p>"}
  if(u.length)h+='<ul class="imp-u">'+u.map(function(x){return "<li>"+esc(x[0])+(d.mode==="round"?(x[1]>1?" "+x[1]+"問":""):" "+x[1]+"問")+"</li>"}).join("")+"</ul>";
  if(o.rk&&d.ranked)h+="<p>この科目の過去問のある"+d.ranked+"節の中で "+o.rk+" 番目</p>";
  h+='<p class="imp-rule">'+esc(d.rule||"")+"</p>";return h}
var IMPP={el:null,b:null,raf:0};
function impPlace(){IMPP.raf=0;var el=IMPP.el,b=IMPP.b;if(!el||el.hidden||!b)return;if(!b.isConnected){impClose();return}
  var r=b.getBoundingClientRect(),vw=document.documentElement.clientWidth||innerWidth,vh=innerHeight;
  if(r.bottom<0||r.top>vh||(!r.width&&!r.height)){impClose();return}
  var w=el.offsetWidth,l=Math.max(16,Math.min(r.left,vw-16-w));el.style.left=l+"px";el.style.top=Math.round(r.bottom+6)+"px"}
function impClose(){if(IMPP.b)IMPP.b.setAttribute("aria-expanded","false");if(IMPP.el)IMPP.el.hidden=true;IMPP.b=null}
function impOpen(b){var sec=b.dataset.imp,o=impOf(sec);if(!o)return;
  if(!IMPP.el||!IMPP.el.isConnected){var e=document.createElement("div");e.id="imp-pop";e.setAttribute("role","dialog");e.hidden=true;document.body.appendChild(e);IMPP.el=e}
  if(IMPP.b&&IMPP.b!==b)IMPP.b.setAttribute("aria-expanded","false");
  IMPP.b=b;b.setAttribute("aria-expanded","true");var el=IMPP.el;
  el.setAttribute("aria-label","節の重要度: "+(TITLES[sec]||""));
  el.innerHTML='<div class="imp-ph"><b class="imp'+o.lv+'">'+impStars(o.lv)+" "+IMP_LB[o.lv]+"</b><span>"+esc(TITLES[sec]||"")+"</span></div>"+impText(sec,o);
  el.hidden=false;el.scrollTop=0;impPlace()}
(function(){
  if(window.__impAC){try{window.__impAC.abort()}catch(e){}}
  var ac=window.AbortController?new AbortController():null;window.__impAC=ac;var LO=ac?{signal:ac.signal}:false,LP=ac?{passive:true,signal:ac.signal}:{passive:true};
  var old=byId("imp-pop");if(old)old.remove();
  document.addEventListener("click",function(e){var b=e.target.closest&&e.target.closest("button.imp[data-imp]");if(!b)return;e.preventDefault();e.stopPropagation();
    if(IMPP.b===b&&IMPP.el&&!IMPP.el.hidden)impClose();else impOpen(b)},LO);
  document.addEventListener("pointerdown",function(e){if(!IMPP.b)return;var t=e.target;if(t.closest&&(t.closest("#imp-pop")||t.closest("button.imp[data-imp]")))return;impClose()},LO);
  document.addEventListener("keydown",function(e){if(e.key==="Escape"&&IMPP.b){var b=IMPP.b;impClose();try{b.focus()}catch(x){}}},LO);
  function req(){if(IMPP.b&&!IMPP.raf)IMPP.raf=requestAnimationFrame(impPlace)}
  window.addEventListener("scroll",req,LP);window.addEventListener("resize",req,LP);
})();
"""

# 1) 本体(テキストの組み立ての前に)
rep("function cleanHtml(h){", JS.strip() + "\nfunction cleanHtml(h){")
# 2) テキストを組み立てたあとに星を付ける
rep("renderQaInline();try{mountQx()}catch(e){}try{cslAgain()}catch(e){}", "renderQaInline();try{mountQx()}catch(e){}try{cslAgain()}catch(e){}try{impApply()}catch(e){}")
# 3) メニューの目次の行に小さな星
rep('if(state.marks[f.id])b.appendChild(sp("st","★"))', 'impMini(b,f);if(state.marks[f.id])b.appendChild(sp("st","★"))')
# 4) 節の名前を取り出すところは、印の文字を数えない
rep('n.classList&&n.classList.contains("kz")?"":n.textContent', 'n.classList&&(n.classList.contains("kz")||n.classList.contains("imp"))?"":n.textContent')
rep('$$(".no,.tag,.kz,button,.star",c)', '$$(".no,.tag,.kz,.imp,button,.star",c)')
rep('$$("button,.no,.tag,.qx-b,.kz-lab",c)', '$$("button,.no,.tag,.qx-b,.kz-lab,.imp",c)')
rep('$$(".ask,.done-row,.star,.unote,.qa-in,svg",c)', '$$(".ask,.done-row,.star,.unote,.qa-in,.imp,svg",c)')
# 5) 表示の設定「節の重要度」
rep('secb:"on",pv:2', 'secb:"on",imp:"on",pv:2')
rep('body.classList.toggle("secb-off",prefs.secb==="off");', 'body.classList.toggle("secb-off",prefs.secb==="off");body.classList.toggle("imp-off",prefs.imp==="off");if(prefs.imp==="off"&&typeof impClose==="function")impClose();')
SECB = 'data-k=\\"secb\\"><button type=\\"button\\" data-v=\\"on\\">表示する<\\/button><button type=\\"button\\" data-v=\\"off\\">表示しない<\\/button><\\/div>'
rep(SECB, SECB + '\\n  <div class=\\"mp-h t-only\\">節の重要度(見出しと目次の★)<\\/div><div class=\\"seg t-only\\" data-k=\\"imp\\"><button type=\\"button\\" data-v=\\"on\\">表示する<\\/button><button type=\\"button\\" data-v=\\"off\\">表示しない<\\/button><\\/div>')

js = "<script>(function(){if(document.getElementById('cs-imp-css'))return;var st=document.createElement('style');st.id='cs-imp-css';st.textContent=" + json.dumps(CSS.strip()) + ";document.head.appendChild(st)})();</script>"
if s.count("</head>") != 1: sys.exit("</head> が1件ではない")
s = s.replace("</head>", js + "</head>")
open(out, "w", encoding="utf-8").write(s); print("ok")
