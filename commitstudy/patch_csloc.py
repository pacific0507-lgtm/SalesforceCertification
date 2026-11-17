"""答え合わせのあとの「テキストのこの場所」と、テキストを読みながらの「節の地図」(社労士版から移植)。
  目的: 試験中にテキストの該当箇所が頭に浮かんで答えられるようにする。
  1. 問題集の答え合わせのあと、正解・不正解(と論点の囲み)のすぐ下、解説の上に「テキストのこの場所」を出す。
     - その節の本文(article)を cloneNode(true) で写し、約0.56倍に縮めて、高さ230pxの窓に論点が真ん中に来るよう置く。
       論点(問題の x の文)は赤い枠で囲み、2回だけ脈打たせる。飛ぶ先の決め方は、これまでの「テキストの該当箇所で復習する」と同じ。
     - 写しの中の id・data-sec・マーカーの data-k/data-h/data-t などは外し、inert・aria-hidden を付ける
       (マーカー・暗記の印・検索の数え方・目次の追跡・表の見出しの追従に入らないように)。
     - 右の細い帯は節全体の地図: 節の直下の要素ごとに色の帯(見出し=紺、表=青、図=紫、掛け合い=灰、試験ポイント=緑、
       たとえるなら=橙、要点=水色、過去問の関連知識=桃、本文=薄い灰)。窓に見えている範囲を枠、論点を赤い点で示す。
     - 「📍 節のおわりのほう ・ 見出し『〜』の下 ・ 表の中」の形で、場所を言葉でも出す。
     - 絵を押すと、テキストのその場所へ移る。そのため「テキストの該当箇所で復習する」のリンクはやめる(答える前にも出さない)。
       場所の絵が作れない問題(x がない・本文に見つからない)だけ、答え合わせのあとに従来のリンクを出す。
     - 写しは、テキストを最後に見たときの列の幅で組む(画面の幅ごとに cs-csloc-w-v1 に控える)。まだ見ていない幅は、
       同じ種類の画面で見た幅に画面の幅の差を足して見積もる。それもなければ、テキストの列をその場で測る。
     - 向きを変えたら resize で組み直し、ResizeObserver(窓と写し)の知らせの中で描き直す。描くまでは赤い枠を隠しておく。
       紙の幅を先に決めてから位置を測る。横にスクロールする表の中の論点は、写しの表を論点が真ん中に来るよう送ってから測る。
  2. テキストを読んでいるとき、画面の右端(本文の外の余白)に「節の地図」を出す。
     - いま読んでいる節の並び(1と同じ色の帯)と、いま画面に出ている範囲の枠。
     - スマホ・タブレットはスクロール中だけ出し、止まって1.5秒で消す。マウスで使う画面では常に出す。
     - 押すと太くなり、指の位置の見出しの名前を出す。なぞると節の中のその位置へ移る。出ていないときは押せない(pointer-events:none)。
     - 表示の設定に「節の地図: 表示する/表示しない」(prefs.csmap、はじめは表示する)。
  表の見出しの追従(patch_sticky_thead.py)は、写しの中の表を対象にしないようにする。
  公開先では body が作り直されるため、CSS はスクリプトで document.head に入れる。
使い方: python3 patch_csloc.py <index.html> <出力>
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
.csloc{margin:14px 0 4px;padding:10px 12px 10px;border:1px solid var(--line);border-radius:12px;background:var(--bg,var(--surface))}
.csloc-h{display:flex;align-items:baseline;gap:8px;flex-wrap:wrap;margin:0 0 8px;font-size:13px;line-height:1.4}
.csloc-h b{font-size:13.5px;color:var(--ink)}
.csloc-h .csloc-s{color:var(--sub,#666);font-size:12px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;min-width:0;flex:1 1 auto}
.csloc-h .csloc-go{margin-left:auto;color:var(--accent);font-size:12px;font-weight:700;white-space:nowrap}
.csloc-row{display:grid;grid-template-columns:minmax(0,1fr) 12px;gap:8px;align-items:stretch}
.csloc-win{position:relative;height:230px;overflow:hidden;border-radius:10px;background:color-mix(in srgb,var(--line) 45%,var(--bg,var(--surface)));cursor:pointer;outline-offset:2px;-webkit-tap-highlight-color:transparent;contain:paint}
.csloc-win:focus-visible{outline:2px solid var(--accent)}
.csloc-win>article.feat{position:absolute!important;left:0;top:0;margin:0!important;transform-origin:0 0;box-sizing:border-box;pointer-events:none;box-shadow:0 2px 10px rgba(0,0,0,.12);scroll-margin-top:0}
.csloc-win>article.feat .tw{scrollbar-width:none}
.csloc-fr{position:absolute;z-index:2;border:2.5px solid #e0362c;border-radius:5px;pointer-events:none;visibility:hidden;box-shadow:0 0 0 0 rgba(224,54,44,.5)}
.csloc-fr.csloc-pulse{animation:csloc-p .85s ease-out 2}
@keyframes csloc-p{0%{box-shadow:0 0 0 0 rgba(224,54,44,.55);transform:scale(1)}40%{transform:scale(1.04)}100%{box-shadow:0 0 0 9px rgba(224,54,44,0);transform:scale(1)}}
.csloc-where{margin:8px 0 0;font-size:13px;line-height:1.55;color:var(--ink);font-weight:600}
.csloc-map{height:230px}
:where(.csmap-strip){position:relative;border-radius:4px;background:color-mix(in srgb,var(--line) 70%,transparent)}
:where(.csmap-bands){position:absolute;inset:0;overflow:hidden;border-radius:inherit}
:where(.csmap-b){position:absolute;left:0;right:0;min-height:1px;background:#c9ced6}
.csmap-tx{background:#c9ced6}
.csmap-hd{background:#1f3a68}
.csmap-tb{background:#3b82f6}
.csmap-fg{background:#8b5cf6}
.csmap-tk{background:#8f96a3}
.csmap-pt{background:#16a34a}
.csmap-tp{background:#f59e0b}
.csmap-one{background:#06b6d4}
.csmap-pq{background:#ec4899}
html[data-theme=dark] .csmap-tx{background:#4b5563}
html[data-theme=dark] .csmap-hd{background:#93b4ea}
html[data-theme=dark] .csmap-tk{background:#6b7280}
@media (prefers-color-scheme:dark){html:not([data-theme=light]) .csmap-tx{background:#4b5563}html:not([data-theme=light]) .csmap-hd{background:#93b4ea}html:not([data-theme=light]) .csmap-tk{background:#6b7280}}
:where(.csmap-vf){position:absolute;left:-3px;right:-3px;border:2px solid var(--ink);border-radius:3px;box-shadow:0 0 0 1px var(--surface);pointer-events:none;min-height:4px;box-sizing:border-box}
:where(.csmap-dot){position:absolute;left:50%;width:9px;height:9px;border-radius:50%;background:#e0362c;border:1.5px solid #fff;transform:translate(-50%,-50%);box-sizing:border-box;pointer-events:none}
#csmap-rd{position:fixed;z-index:45;right:max(3px,env(safe-area-inset-right,0px));top:calc(var(--barh,56px) + 14px);bottom:calc(100px + env(safe-area-inset-bottom,0px));width:6px;opacity:0;pointer-events:none;touch-action:none;transition:opacity .25s,width .15s;-webkit-user-select:none;user-select:none}
#csmap-rd::before{content:"";position:absolute;top:-6px;bottom:-6px;left:-12px;right:-6px}
#csmap-rd.csmap-on{opacity:1;pointer-events:auto}
#csmap-rd.csmap-act{width:20px}
#csmap-rd .csmap-tip{position:absolute;right:calc(100% + 10px);top:0;transform:translateY(-50%);display:none;max-width:min(260px,70vw);overflow:hidden;text-overflow:ellipsis;white-space:nowrap;background:var(--ink);color:var(--surface);font-size:12.5px;font-weight:700;line-height:1.4;padding:5px 10px;border-radius:8px;box-shadow:0 4px 14px rgba(0,0,0,.25)}
#csmap-rd.csmap-act .csmap-tip{display:block}
body.view-q #csmap-rd,body.csmap-off #csmap-rd{display:none}
@media (hover:hover) and (pointer:fine){#csmap-rd{bottom:28px}#csmap-rd:hover{width:10px}#csmap-rd.csmap-act{width:20px}}
"""

JS = r"""
/* ==テキストのこの場所== 答え合わせのあとに、その節の本文を縮めた写しで論点の場所を見せる(押すとテキストのその場所へ) */
var CSL={el:null,n:null,src:null,ver:"",link:"",ro:null,s:0.56,colW:0},CSL_WK="cs-csloc-w-v1";
function cslKind(){var pc=false;try{pc=matchMedia("(hover:hover) and (pointer:fine)").matches}catch(e){}var m=Math.min(screen.width||0,screen.height||0)||Math.min(innerWidth,innerHeight);return (pc?"pc":"tc")+(m<600?"s":"l")}
function cslVW(){return document.documentElement.clientWidth||innerWidth}
function cslWLoad(){try{var o=JSON.parse(localStorage.getItem(CSL_WK));return o&&typeof o==="object"?o:{}}catch(e){return {}}}
function cslWSave(vw,w){var o=cslWLoad(),k=String(vw);w=Math.round(w*10)/10;if(o[k]&&o[k].w===w&&o[k].k===cslKind())return;o[k]={w:w,k:cslKind(),t:Date.now()};
  var ks=Object.keys(o);if(ks.length>24){ks.sort(function(a,b){return (o[a].t||0)-(o[b].t||0)});delete o[ks[0]]}try{localStorage.setItem(CSL_WK,JSON.stringify(o))}catch(e){}}
/* テキストを見ているときの列の幅を、画面の幅ごとに控える */
function cslRemember(){if(view==="quiz")return;var fs=$$("#chapters .feat[data-sec]");for(var i=0;i<fs.length;i++){var r=fs[i].getBoundingClientRect();if(r.width&&r.bottom>0&&r.top<innerHeight){cslWSave(cslVW(),r.width);return}}}
/* 控えがないとき: 隠れているテキストの列を、見えないままその場で組んで測る */
function cslMeasureNow(){var wr=$(".wrap"),f=$("#chapters .feat[data-sec]");if(!wr||!f)return 0;var old=wr.getAttribute("style"),w=0;
  try{wr.style.cssText=(old||"")+";display:grid!important;position:absolute!important;left:0!important;right:0!important;top:0!important;visibility:hidden!important;pointer-events:none!important";w=f.getBoundingClientRect().width}catch(e){}
  if(old==null)wr.removeAttribute("style");else wr.setAttribute("style",old);return w}
function cslColW(){var vw=cslVW(),o=cslWLoad(),e=o[String(vw)];if(e&&e.w)return e.w;
  var kd=cslKind(),best=null;Object.keys(o).forEach(function(k){var x=o[k];if(!x||!x.w||x.k!==kd)return;var d=Math.abs(+k-vw);if(!best||d<best.d)best={d:d,w:x.w,vw:+k}});
  if(best)return Math.max(220,Math.min(best.w+(vw-best.vw),vw));
  var m=view==="quiz"?cslMeasureNow():0;if(m)return m;
  var c=$("#card");return Math.max(220,c&&c.clientWidth?c.clientWidth:vw-32)}
function cslPath(n,root){var p=[];while(n&&n!==root){var par=n.parentNode;if(!par)return null;p.unshift(Array.prototype.indexOf.call(par.childNodes,n));n=par}return n===root?p:null}
function cslAt(root,p){var n=root;for(var i=0;i<p.length&&n;i++)n=n.childNodes[p[i]];return n||null}
function cslTxt(el){var c=el.cloneNode(true);$$("button,.no,.tag,.qx-b,.kz-lab",c).forEach(function(x){x.remove()});return c.textContent.replace(/\s+/g," ").trim()}
function cslCut(t,n){return t.length>n?t.slice(0,n-1)+"…":t}
/* 節の直下の要素ごとの色の帯(2の地図と共通) */
function cslType(el){var t=el.tagName,c=el.classList;
  if(/^H[2-5]$/.test(t))return c.contains("pq-h")?"pq":"hd";
  if(c.contains("tw")||t==="TABLE")return "tb";
  if(t==="FIGURE"||c.contains("scr-g"))return "fg";
  if(c.contains("talk"))return "tk";
  if(c.contains("memo"))return "pt";
  if(c.contains("tips"))return "tp";
  if(c.contains("one"))return "one";
  if(c.contains("pq"))return "pq";
  if(c.contains("ex")||/^(P|UL|OL|PRE|DETAILS|BLOCKQUOTE|DL)$/.test(t))return "tx";
  return ""}
var CSL_TN={hd:"見出し",tb:"表",fg:"図",tk:"キャラの掛け合い",pt:"試験ポイント",tp:"たとえるなら",one:"要点",pq:"過去問で問われた関連知識",tx:"本文"};
function cslBands(art){var out=[];Array.prototype.forEach.call(art.children,function(ch){var k=cslType(ch);if(!k)return;var h=ch.offsetHeight;if(!h)return;
  out.push({k:k,top:ch.offsetTop,h:h,hd:/^H[2-5]$/.test(ch.tagName),name:/^H[2-5]$/.test(ch.tagName)?cslTxt(ch):CSL_TN[k]})});return out}
function cslPaint(box,bands,H){if(!box)return;var h="";bands.forEach(function(b){h+='<span class="csmap-b csmap-'+b.k+'" style="top:'+(b.top/H*100).toFixed(3)+'%;height:'+(b.h/H*100).toFixed(3)+'%"></span>'});box.innerHTML=h}
/* 場所のひとこと */
function cslWhere(art,blk,p){
  var pos=p<0.2?"節のはじめのほう":p<0.4?"節の前半":p<0.6?"節のなかほど":p<0.8?"節の後半":"節のおわりのほう",top=blk;
  while(top&&top.parentNode!==art)top=top.parentNode;
  var hs="";if(top){if(/^H[2-5]$/.test(top.tagName))hs=top.tagName==="H3"?"節の見出し":"見出し「"+cslCut(cslTxt(top),24)+"」";
    else{var x=top.previousElementSibling;while(x&&!/^H[3-5]$/.test(x.tagName))x=x.previousElementSibling;if(x)hs=x.tagName==="H3"?"節の見出しのすぐ下":"見出し「"+cslCut(cslTxt(x),24)+"」の下"}}
  var bx="";if(top){var c=top.classList,t=top.tagName;
    if(c.contains("tw")||t==="TABLE"){bx="表の中";var tr=blk&&blk.closest&&blk.closest("tr");if(tr&&tr.parentNode&&tr.parentNode.tagName==="TBODY")bx="表の中("+(Array.prototype.indexOf.call(tr.parentNode.rows,tr)+1)+"行目)"}
    else if(c.contains("memo"))bx="「試験ポイント」の囲み";else if(c.contains("tips"))bx="「たとえるなら」の囲み";else if(c.contains("talk"))bx="キャラの掛け合いの中";
    else if(t==="FIGURE"||c.contains("scr-g"))bx="図の中";else if(c.contains("pq")||c.contains("pq-h"))bx="「過去問で問われた関連知識」の中";
    else if(c.contains("steps"))bx="手順の中";else if(c.contains("one"))bx="節のはじめの要点";else if(t==="UL"||t==="OL")bx="箇条書きの中";
    else if(t==="DETAILS")bx="折りたたみの中";else if(c.contains("ex"))bx="例の中"}
  if(/過去問/.test(bx)&&/過去問/.test(hs))hs="";
  return "📍 "+[pos,hs,bx].filter(Boolean).join(" ・ ")}
function cslRect(C){var r=null;try{r=C.rg.getBoundingClientRect()}catch(e){}if((!r||(!r.width&&!r.height))&&C.blk)r=C.blk.getBoundingClientRect();return r}
function cslDraw(){var C=CSL;if(!C.el||!C.el.isConnected)return;var win=C.win,art=C.art,winW=win.clientWidth,winH=win.clientHeight;if(!winW||!winH)return;
  var s=Math.min(0.56,(winW-6)/C.colW);
  art.style.transform="scale("+s+")";if(C.tw)C.tw.scrollLeft=0;
  var pr=art.getBoundingClientRect(),r=cslRect(C);if(!r)return;
  if(C.tw){var tr=C.tw.getBoundingClientRect(),cx=(r.left+r.width/2-tr.left)/s,tg=cx-C.tw.clientWidth/2;if(tg>0){C.tw.scrollLeft=tg;r=cslRect(C)}
    /* 表の見えている幅の外(横にはみ出した部分)は枠に入れない */
    tr=C.tw.getBoundingClientRect();var l=Math.max(r.left,tr.left),rt=Math.min(r.right,tr.right);if(rt>l)r={left:l,top:r.top,width:rt-l,height:r.height}}
  var ax=(r.left-pr.left)/s,ay=(r.top-pr.top)/s,aw=r.width/s,ah=r.height/s,H=art.offsetHeight||1;
  var Y=ay+ah/2-winH/2/s,x0=Math.max(0,(winW-C.colW*s)/2);
  art.style.transform="translate("+x0.toFixed(2)+"px,"+(-Y*s).toFixed(2)+"px) scale("+s+")";
  var pad=3,fl=x0+ax*s-pad,ft=(ay-Y)*s-pad,fw=aw*s+pad*2,fh=ah*s+pad*2;
  if(fl<2){fw-=2-fl;fl=2}if(fl+fw>winW-2)fw=winW-2-fl;if(ft<2){fh-=2-ft;ft=2}if(ft+fh>winH-2)fh=winH-2-ft;
  var fr=C.fr;fr.style.left=fl+"px";fr.style.top=ft+"px";fr.style.width=Math.max(8,fw)+"px";fr.style.height=Math.max(8,fh)+"px";
  if(fr.style.visibility!=="visible"){fr.style.visibility="visible";if(C.seen&&!C.pulsed)cslPulse(C)}
  cslPaint(C.bands,cslBands(art),H);
  var v0=Math.max(0,Y/H),v1=Math.min(1,(Y+winH/s)/H);C.vf.style.top=(v0*100)+"%";C.vf.style.height=(Math.max(0.02,v1-v0)*100)+"%";
  var p=Math.max(0,Math.min(1,(ay+ah/2)/H));C.dot.style.top=(p*100)+"%";
  var w=cslWhere(art,C.blk||C.rg.startContainer.parentElement,p);if(C.wh.textContent!==w)C.wh.textContent=w}
/* 赤枠の点滅は、場所の絵が画面に入ってきたときに出す(見る前に終わらないように)。いったん画面から出て、また入ってきたらもう一度 */
function cslPulse(C){var fr=C.fr;if(!fr||fr.style.visibility!=="visible")return;C.pulsed=true;fr.classList.remove("csloc-pulse");void fr.offsetWidth;fr.classList.add("csloc-pulse")}
function cslSee(){var C=CSL;if(C.io)C.io.disconnect();C.seen=false;C.pulsed=false;if(!window.IntersectionObserver){C.seen=true;cslPulse(C);return}
  C.io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting&&e.intersectionRatio>=0.6){if(!C.seen){C.seen=true;cslPulse(C)}}else if(!e.isIntersecting){C.seen=false;C.pulsed=false}})},{threshold:[0,0.6]});C.io.observe(C.win)}
function cslObs(){var C=CSL;cslSee();if(!window.ResizeObserver){cslDraw();return}if(C.ro)C.ro.disconnect();C.ro=new ResizeObserver(function(){cslDraw()});C.ro.observe(C.win);C.ro.observe(C.art)}
function cslVer(a){return a.innerHTML.length+":"+a.childElementCount}
function cslMount(q){var slot=byId("csloc-slot");if(!slot||!q||!q.x)return false;var sec=q.xs||q.s,src=byId("f-"+sec);if(!src)return false;
  if(CSL.el&&CSL.n===q.n&&CSL.src===src&&CSL.ver===cslVer(src)){slot.appendChild(CSL.el);CSL.fr.style.visibility="hidden";var w=cslColW();if(Math.abs(w-CSL.colW)>0.5){CSL.colW=w;CSL.art.style.width=w+"px"}cslObs();return true}
  var r=qxRange(sec,q.x);if(!r)return false;
  var c=src.cloneNode(true),sp=cslPath(r.startContainer,src),ep=cslPath(r.endContainer,src),bl=qxBlock(r),bp=bl?cslPath(bl,src):null;if(!sp||!ep)return false;
  var sN=cslAt(c,sp),eN=cslAt(c,ep),bN=bp?cslAt(c,bp):null;if(!sN||!eN)return false;
  var rg=document.createRange();try{rg.setStart(sN,r.startOffset);rg.setEnd(eN,r.endOffset)}catch(e){return false}
  /* 写しの中は、マーカー・暗記の印・検索・目次の追跡などに数えられないよう、目印になる属性を外す */
  $$("#cs-sth,.csloc,script,style",c).forEach(function(x){if(!x.contains(sN))x.remove()});
  var ATT=["id","data-sec","data-k","data-h","data-t","data-done","data-quiz","data-jump","data-up","data-act","data-qx","data-id","data-mode","data-p","data-kz","name","for"];
  [c].concat($$("*",c)).forEach(function(x){ATT.forEach(function(a){if(x.hasAttribute(a))x.removeAttribute(a)});x.classList.remove("hit","qx-flash")});
  c.setAttribute("inert","");c.setAttribute("aria-hidden","true");c.setAttribute("data-csclone","1");
  var colW=cslColW();c.style.width=colW+"px";
  var box=document.createElement("div");box.className="csloc";box.setAttribute("role","group");box.setAttribute("aria-label","テキストのこの場所");
  box.innerHTML='<div class="csloc-h"><b>テキストのこの場所</b><span class="csloc-s">'+esc(dk(sec)+" "+(TITLES[sec]||""))+'</span><span class="csloc-go" aria-hidden="true">押すと開く →</span></div>'+
    '<div class="csloc-row"><div class="csloc-win" role="button" tabindex="0" aria-label="'+esc("テキストのこの場所を開く: "+dk(sec)+" "+(TITLES[sec]||""))+'"><span class="csloc-fr"></span></div>'+
    '<div class="csmap-strip csloc-map" aria-hidden="true"><div class="csmap-bands"></div><div class="csmap-vf"></div><span class="csmap-dot"></span></div></div><p class="csloc-where"></p>';
  var win=box.querySelector(".csloc-win");win.insertBefore(c,win.firstChild);
  var fr=box.querySelector(".csloc-fr");fr.addEventListener("animationend",function(){fr.classList.remove("csloc-pulse")});
  function go(e){if(e)e.preventDefault();goText(sec,q)}
  win.addEventListener("click",go);win.addEventListener("keydown",function(e){if(e.key==="Enter"||e.key===" ")go(e)});
  if(CSL.ro)CSL.ro.disconnect();if(CSL.io)CSL.io.disconnect();
  CSL={el:box,n:q.n,src:src,ver:cslVer(src),link:CSL.link,ro:null,colW:colW,win:win,art:c,fr:fr,rg:rg,blk:bN||(sN.nodeType===1?sN:sN.parentElement),tw:null,
    bands:box.querySelector(".csmap-bands"),vf:box.querySelector(".csmap-vf"),dot:box.querySelector(".csmap-dot"),wh:box.querySelector(".csloc-where"),pulsed:false};
  var tw=CSL.blk&&CSL.blk.closest?CSL.blk.closest(".tw,.qb-tw"):null;CSL.tw=tw&&c.contains(tw)?tw:null;
  slot.appendChild(box);cslObs();return true}
function cslRun(q,rev){var qt=$("#qtext");if(!rev){if(qt)qt.innerHTML="";return}var ok=false;try{ok=cslMount(q)}catch(e){ok=false}if(qt)qt.innerHTML=ok?"":CSL.link}
/* 本文があとから届いたとき(答え合わせ済みで場所の絵がまだないなら作り直す) */
function cslAgain(){try{var q=cur();if(!q||view!=="quiz")return;var a=ans()[q.n];if(!a||!a.checked)return;var sl=byId("csloc-slot");if(sl&&!sl.firstChild)cslRun(q,true)}catch(e){}}
/* ==節の地図== テキストを読んでいるとき、画面の右端に、いま読んでいる節の並びと見えている範囲を出す */
(function(){
  if(window.__csmapAC){try{window.__csmapAC.abort()}catch(e){}}
  var ac=window.AbortController?new AbortController():null;window.__csmapAC=ac;var LO=ac?{passive:true,signal:ac.signal}:{passive:true};
  var old=byId("csmap-rd");if(old)old.remove();
  var el=document.createElement("div");el.id="csmap-rd";el.className="csmap-strip";el.setAttribute("aria-hidden","true");
  el.innerHTML='<div class="csmap-bands"></div><div class="csmap-vf"></div><div class="csmap-tip"></div>';document.body.appendChild(el);
  var bx=el.querySelector(".csmap-bands"),vf=el.querySelector(".csmap-vf"),tip=el.querySelector(".csmap-tip");
  var fine=null;try{fine=matchMedia("(hover:hover) and (pointer:fine)")}catch(e){}
  var cur0=null,curH=0,curW=0,bands=[],drag=false,lock=null,hideT=0,raf=0,fs=[],fsT=0,remT=0;
  function isFine(){return !!(fine&&fine.matches)}
  function active(){return view!=="quiz"&&!body.classList.contains("csmap-off")&&el.isConnected}
  function list(){var now=Date.now();if(!fs.length||now-fsT>2000||(fs[0]&&!fs[0].isConnected)){fs=$$("#chapters .feat[data-sec]");fsT=now}return fs}
  function pick(){var probe=innerHeight*0.35,L=list(),best=null;
    if(cur0&&cur0.isConnected){var r0=cur0.getBoundingClientRect();if(r0.height&&r0.top<=probe&&r0.bottom>probe)return cur0}
    for(var i=0;i<L.length;i++){var r=L[i].getBoundingClientRect();if(!r.height)continue;if(r.top<=probe){if(r.bottom>0)best=L[i]}else{if(!best&&r.top<innerHeight)best=L[i];break}}return best}
  function hide(){if(!drag&&!isFine())el.classList.remove("csmap-on")}
  function upd(){raf=0;if(!active()){el.classList.remove("csmap-on");return}
    var a=drag&&lock?lock:pick();if(!a){el.classList.remove("csmap-on");cur0=null;return}
    if(a!==cur0||a.offsetHeight!==curH||a.offsetWidth!==curW){cur0=a;curH=a.offsetHeight;curW=a.offsetWidth;bands=cslBands(a);cslPaint(bx,bands,curH||1)}
    var r=a.getBoundingClientRect(),H=r.height||1,t0=Math.max(0,-r.top)/H,t1=Math.min(H,innerHeight-r.top)/H;
    t0=Math.min(1,t0);t1=Math.max(t0,Math.min(1,t1));vf.style.top=(t0*100)+"%";vf.style.height=(Math.max(0.015,t1-t0)*100)+"%";
    if(isFine())el.classList.add("csmap-on")}
  function req(){if(!raf)raf=requestAnimationFrame(upd)}
  function onScroll(){if(!active())return;if(!isFine()){el.classList.add("csmap-on");clearTimeout(hideT);hideT=setTimeout(hide,1500)}req();
    clearTimeout(remT);remT=setTimeout(cslRemember,600)}
  function nameAt(y){var n="";for(var i=0;i<bands.length;i++){if(bands[i].top>y)break;if(bands[i].hd)n=bands[i].name}return n}
  function goTo(e){if(!lock)return;var sr=el.getBoundingClientRect(),f=Math.max(0,Math.min(1,(e.clientY-sr.top)/(sr.height||1)));
    var r=lock.getBoundingClientRect(),abs=r.top+window.scrollY,H=r.height,y=abs+f*H-innerHeight/2;
    y=Math.max(abs-80,Math.min(y,abs+H-innerHeight+80));if(H<innerHeight)y=abs-80;
    try{hold(400)}catch(x){}window.scrollTo(0,Math.max(0,y));
    tip.textContent=nameAt(f*(lock.offsetHeight||H))||cslTxt(lock.querySelector("h3")||lock);tip.style.top=(f*100)+"%";upd()}
  el.addEventListener("pointerdown",function(e){if(!el.classList.contains("csmap-on")||!cur0)return;e.preventDefault();drag=true;lock=cur0;clearTimeout(hideT);
    try{el.setPointerCapture(e.pointerId)}catch(x){}el.classList.add("csmap-act");goTo(e)});
  el.addEventListener("pointermove",function(e){if(drag){e.preventDefault();goTo(e)}});
  function end(){if(!drag)return;drag=false;lock=null;el.classList.remove("csmap-act");clearTimeout(hideT);if(!isFine())hideT=setTimeout(hide,1500);req()}
  el.addEventListener("pointerup",end);el.addEventListener("pointercancel",end);el.addEventListener("lostpointercapture",end);
  window.addEventListener("scroll",onScroll,LO);
  var rzT=0;window.addEventListener("resize",function(){req();clearTimeout(rzT);rzT=setTimeout(function(){cslRemember();
    if(CSL.el&&CSL.el.isConnected){var w=cslColW();if(Math.abs(w-CSL.colW)>0.5){CSL.colW=w;CSL.fr.style.visibility="hidden";CSL.art.style.width=w+"px"}else cslDraw()}},150)},LO);
  if(fine&&fine.addEventListener)fine.addEventListener("change",req,ac?{signal:ac.signal}:false);
  var iv=setInterval(function(){if(!el.isConnected){clearInterval(iv);return}if(isFine())req();if(view!=="quiz"&&Math.random()<0.2)cslRemember()},1000);
})();
"""

# 1) 答え合わせのあと、正解・不正解(論点の囲み)のすぐ下に場所の絵の置き場
rep("h+=ronPoint(q,hasSel(a)&&!a.correct);", "h+=ronPoint(q,hasSel(a)&&!a.correct)+'<div id=\"csloc-slot\"></div>';")
# 2) 「テキストで復習する」のリンクは、場所の絵が作れない問題の答え合わせのあとだけ出す
rep("var xsec=q.x?(q.xs||q.s):q.s;$(\"#qtext\").innerHTML='", "var xsec=q.x?(q.xs||q.s):q.s;CSL.link='")
rep("if(revealed)mountQ(q);", "if(revealed)mountQ(q);cslRun(q,revealed);")
# 3) 本体
rep("function qxBlock(r){", JS.strip() + "\nfunction qxBlock(r){")
rep("renderQaInline();try{mountQx()}catch(e){}", "renderQaInline();try{mountQx()}catch(e){}try{cslAgain()}catch(e){}")
# 4) 表示の設定「節の地図」
rep('talk:"on",pv:2', 'talk:"on",csmap:"on",pv:2')
rep('body.classList.toggle("talk-off",prefs.talk==="off");', 'body.classList.toggle("talk-off",prefs.talk==="off");body.classList.toggle("csmap-off",prefs.csmap==="off");')
TALK = 'data-k=\\"talk\\"><button type=\\"button\\" data-v=\\"on\\">表示する<\\/button><button type=\\"button\\" data-v=\\"off\\">表示しない<\\/button><\\/div>'
rep(TALK, TALK + '\\n  <div class=\\"mp-h t-only\\">節の地図(画面の右端)<\\/div><div class=\\"seg t-only\\" data-k=\\"csmap\\"><button type=\\"button\\" data-v=\\"on\\">表示する<\\/button><button type=\\"button\\" data-v=\\"off\\">表示しない<\\/button><\\/div>')
# 5) 表の見出しの追従は、写しの中の表を対象にしない
rep("if(box&&box.contains(t))continue;", "if((box&&box.contains(t))||t.closest('.csloc'))continue;")

js = "<script>(function(){if(document.getElementById('cs-csloc'))return;var st=document.createElement('style');st.id='cs-csloc';st.textContent=" + json.dumps(CSS.strip()) + ";document.head.appendChild(st)})();</script>"
if s.count("</head>") != 1: sys.exit("</head> が1件ではない")
s = s.replace("</head>", js + "</head>")
open(out, "w", encoding="utf-8").write(s); print("ok")
