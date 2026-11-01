/* CommitStudy のトレーニング(/practice/)。社労士版の「1問トレーニング」と同じ画面構成で、
   問題は各科目の4択をそのまま出す。カードは用語カード。
   結果は ls-qpend-v1(科目の問題集が開いたときに回答履歴へ取り込む)と、学習記録(sr-<科目>-act-v1 とクラウドの <科目>-act)に残す。 */
(function(){
var SUBJ=[{id:"d360",short:"D360",title:"Data 360 コンサルタント",color:"#24345e"},{id:"mcadmin",short:"MCA",title:"Marketing Cloud Administrator",color:"#b5560f"}];
var SRCN={past:"過去問",th:"Trailhead",orig:"オリジナル"};
var $=function(s,r){return (r||document).querySelector(s)},$$=function(s,r){return Array.prototype.slice.call((r||document).querySelectorAll(s))};
var esc=function(s){return String(s==null?"":s).replace(/[&<>"]/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]})};
var LS={get:function(k,d){try{var v=JSON.parse(localStorage.getItem(k));return v==null?d:v}catch(e){return d}},set:function(k,v){try{localStorage.setItem(k,JSON.stringify(v))}catch(e){}}};
var pad=function(n){return (n<10?"0":"")+n},today=function(d){d=d||new Date;return d.getFullYear()+"-"+pad(d.getMonth()+1)+"-"+pad(d.getDate())};
var addDays=function(n){var d=new Date;d.setDate(d.getDate()+n);return today(d)};
var url=function(p){return window.famURL?window.famURL(p):p};
var getJSON=function(p){return fetch(url(p)).then(function(r){return r.ok?r.json():[]}).catch(function(){return []})};
var ST=Object.assign({subj:"all",src:"all",mode:"order",tab:"q",gsubj:"all",gonly:"all"},LS.get("cs-practice-v1",{}));
var save=function(){LS.set("cs-practice-v1",ST)};

/* ---- クラウド ---- */
var cloud=(async function(){try{var c=window.claude;if(!c||!c.use)return null;var r=await Promise.all([c.use("db"),c.use("user")]);var uid=r[1]?await r[1].id():null;return r[0]&&uid?{db:r[0],uid:uid}:null}catch(e){return null}})();
var cdoc=function(cl,name){return cl.db.doc("data/users/"+cl.uid+"/"+name)};

/* ---- 問題データ ---- */
var Q={},HIST={},READY={};
function srcOf(id,s){s=String(s||"");if(id==="mcadmin")return "orig";return /^Trailhead/.test(s)?"th":"past"}
async function loadSubj(id){
  if(READY[id])return READY[id];
  READY[id]=(async function(){
    var rows=await getJSON("data/"+id+"/questions.json"),secs=await getJSON("data/"+id+"/sections.json");
    var rank={},title={};secs.slice().sort(function(a,b){return a.sort_order-b.sort_order}).forEach(function(s,i){var k=String(s.id).split(":").pop();rank[k]=i;title[k]=s.title});
    var list=rows.map(function(r){var d=r.data||r;var n=typeof d.id==="number"?d.id:+d.n;var sec=String(d.f||d.s||"").replace(/^f-/,"");
      return {subj:id,n:n,q:d.q,o:d.o||[],a:(d.a||[]).map(Number),ex:d.ex||d.e||"",sec:sec,xs:d.xs||"",x:d.x||"",src:srcOf(id,d.s),label:d.s||"",u:d.u||"",title:title[sec]||""}}).filter(function(q){return q.n&&q.q&&q.o.length>1&&q.a.length});
    list.sort(function(a,b){var x=rank[a.sec],y=rank[b.sec];return (x==null?1e9:x)-(y==null?1e9:y)||a.n-b.n});
    list.forEach(function(q,i){q.d=i+1});
    Q[id]=list;HIST[id]=await loadHist(id);return list})();
  return READY[id];
}
async function loadHist(id){
  var h={},merge=function(src){Object.keys(src||{}).forEach(function(k){var a=src[k],b=h[k];if(!b||(+a.t||0)>(+b.t||0)||(+a.n||0)>(+b.n||0))h[k]={n:Math.max(+a.n||0,b?+b.n||0:0),c:Math.max(+a.c||0,b?+b.c||0:0),l:(!b||(+a.t||0)>=(+b.t||0))?a.l:b.l,t:Math.max(+a.t||0,b?+b.t||0:0)}})};
  var loc=LS.get("sr-"+id+"-quiz-v1",null);if(loc&&loc.hist)merge(loc.hist);
  try{var cl=await cloud;if(cl){var s=await cdoc(cl,id+"-quiz").get();if(s.exists){var d=s.data();var q=d&&d.json?JSON.parse(d.json):d;if(q&&q.hist)merge(q.hist)}}}catch(e){}
  (LS.get("ls-qpend-v1",{})[id]||[]).forEach(function(x){var m=/:q(\d+)$/.exec(x.id||"");if(!m)return;var k=m[1],b=h[k]||(h[k]={n:0,c:0,t:0});if((+x.t||0)>(+b.t||0)){b.n=(+b.n||0)+1;if(x.ok)b.c=(+b.c||0)+1;b.l=x.ok?"o":"x";b.t=x.t}});
  return h;
}

/* ---- 記録 ---- */
var REVK="cs-review-v1",STEPS=[1,3,7,14];
var lastAt=Date.now(),actT=null;
function record(q,ok){
  var key=q.subj+":q"+q.n,now=Date.now();
  var p=LS.get("ls-qpend-v1",{});(p[q.subj]=p[q.subj]||[]).push({id:key,ok:ok,t:now});if(p[q.subj].length>500)p[q.subj]=p[q.subj].slice(-500);LS.set("ls-qpend-v1",p);
  var h=HIST[q.subj][q.n]||(HIST[q.subj][q.n]={n:0,c:0});h.n++;if(ok)h.c++;h.l=ok?"o":"x";h.t=now;
  var rv=LS.get(REVK,{}),r=rv[key]||{step:-1};if(ok){r.step=Math.min(r.step+1,STEPS.length-1);r.due=addDays(STEPS[r.step])}else{r.step=-1;r.due=addDays(1)}rv[key]=r;LS.set(REVK,rv);
  var sec=Math.max(5,Math.min(120,Math.round((now-lastAt)/1000)));lastAt=now;
  var ak="sr-"+q.subj+"-act-v1",act=LS.get(ak,{ts:0,d:{}});if(!act.d)act.d={};var dd=act.d[today()]||(act.d[today()]={q:0,c:0,r:[],t:0});dd.q=(+dd.q||0)+1;if(ok)dd.c=(+dd.c||0)+1;dd.t=(+dd.t||0)+sec;act.ts=now;LS.set(ak,act);
  clearTimeout(actT);actT=setTimeout(function(){pushAct(q.subj)},2500);
  var m=LS.get("cs-train-today",{});if(m.date!==today())m={date:today(),n:0,c:0,combo:0};m.n++;if(ok){m.c++;m.combo++}else m.combo=0;LS.set("cs-train-today",m);renderMeter();
}
async function pushAct(id){
  try{var cl=await cloud;if(!cl)return;var d=cdoc(cl,id+"-act"),s=await d.get(),rem=s.exists?s.data():{d:{}},loc=LS.get("sr-"+id+"-act-v1",{d:{}}),out={d:{},ts:Date.now()};
    [rem.d||{},loc.d||{}].forEach(function(src){Object.keys(src).forEach(function(k){var a=src[k]||{},b=out.d[k]||(out.d[k]={q:0,c:0,t:0,r:[]});["q","c","t"].forEach(function(f){b[f]=Math.max(+b[f]||0,+a[f]||0)});(a.r||[]).forEach(function(x){if(b.r.indexOf(x)<0)b.r.push(x)})})});
    await d.set(out)}catch(e){}
}
document.addEventListener("visibilitychange",function(){if(document.visibilityState==="hidden"&&actT){clearTimeout(actT);actT=null;SUBJ.forEach(function(s){pushAct(s.id)})}});

/* ---- 画面 ---- */
function chips(box,items,cur,cb){box.innerHTML=items.map(function(it){return '<button type="button" data-v="'+esc(it.v)+'" aria-pressed="'+(it.v===cur)+'">'+esc(it.l)+(it.n!=null?'<small>'+it.n+'</small>':"")+'</button>'}).join("");
  box.onclick=function(e){var b=e.target.closest("button[data-v]");if(b)cb(b.dataset.v)}}
function subjItems(){return [{v:"all",l:"すべて"}].concat(SUBJ.map(function(s){return {v:s.id,l:s.short}}))}
function renderMeter(){var m=LS.get("cs-train-today",{});if(m.date!==today())m={n:0,c:0,combo:0};$("#m-n").textContent=m.n||0;$("#m-c").textContent=m.c||0;$("#m-combo").textContent=m.combo||0;
  var mi=$("#mini");if(mi)mi.textContent="今日 "+(m.n||0)+"問・正解 "+(m.c||0)+"・連続正解 "+(m.combo||0);
  $("#m-say").innerHTML='<p class="bx-s">'+(m.n?(m.combo>=5?"連続正解 "+m.combo+"問。その調子です。":"今日は "+m.n+" 問解きました。"):"1問からどうぞ。解いた数は学習の記録にも数えます。")+'</p>'}
function setTab(t){ST.tab=t;save();$$(".tabs [role=tab]").forEach(function(b){var on=b.id==="t-"+t;b.setAttribute("aria-selected",String(on));if(on){var p=$(".tabs .pill");if(p){p.style.width=b.offsetWidth+"px";p.style.transform="translateX("+b.offsetLeft+"px)"}}});
  $("#p-q").hidden=t!=="q";$("#p-g").hidden=t!=="g";if(t==="g")renderTerms()}

/* 問題 */
var CUR=null,SEL=[],DONE=false,RECENT=[],BACK=[];
function subjList(){return ST.subj==="all"?SUBJ.map(function(s){return s.id}):[ST.subj]}
function pool(){var out=[];subjList().forEach(function(id){(Q[id]||[]).forEach(function(q){if(ST.src==="all"||q.src===ST.src)out.push(q)})});return out}
function isWrong(q){var h=HIST[q.subj][q.n];return h&&h.l==="x"}
function isNew(q){return !HIST[q.subj][q.n]}
function isDue(q){var r=LS.get(REVK,{})[q.subj+":q"+q.n];return r&&r.due&&r.due<=today()}
function deck(){var p=pool();if(ST.mode==="wrong")return p.filter(isWrong);if(ST.mode==="new")return p.filter(isNew);if(ST.mode==="review")return p.filter(isDue);return p}
function posKey(){return "cs-practice-pos:"+ST.subj+":"+ST.src}
function counts(){var p=pool();return {review:p.filter(isDue).length,wrong:p.filter(isWrong).length,"new":p.filter(isNew).length}}
function renderFilters(){
  chips($("#f-subj"),subjItems(),ST.subj,function(v){ST.subj=v;save();refreshQ(true)});
  var srcs={};subjList().forEach(function(id){(Q[id]||[]).forEach(function(q){srcs[q.src]=1})});
  if(ST.src!=="all"&&!srcs[ST.src])ST.src="all";
  var sl=Object.keys(srcs);$("#f-src-w").hidden=sl.length<2;
  chips($("#f-src"),[{v:"all",l:"すべて"}].concat(sl.map(function(k){return {v:k,l:SRCN[k]||k}})),ST.src,function(v){ST.src=v;save();refreshQ(true)});
  var c=counts();
  chips($("#f-mode"),[{v:"order",l:"順番どおり"},{v:"random",l:"ランダム"},{v:"review",l:"今日の復習",n:c.review},{v:"wrong",l:"間違えた問題",n:c.wrong},{v:"new",l:"まだ解いていない",n:c["new"]}],ST.mode,function(v){ST.mode=v;save();refreshQ(true)});
}
function pick(){
  var d=deck();if(!d.length)return null;
  if(ST.mode==="random"){var c=d.filter(function(q){return RECENT.indexOf(q.subj+q.n)<0});if(!c.length)c=d;return c[Math.floor(Math.random()*c.length)]}
  if(ST.mode==="order"){var pos=LS.get(posKey(),null),i=0;if(pos){var k=d.findIndex(function(q){return q.subj===pos.s&&q.n===pos.n});if(k>=0)i=k}return d[i]}
  return d[0];
}
function advance(){if(!CUR)return;if(ST.mode==="order"){var d=deck(),i=d.indexOf(CUR),nx=d[(i+1)%d.length];if(nx)LS.set(posKey(),{s:nx.subj,n:nx.n})}RECENT.push(CUR.subj+CUR.n);if(RECENT.length>20)RECENT.shift()}
async function refreshQ(reset){
  var box=$("#qbox");box.innerHTML='<p class="bx-s">問題を読み込んでいます…</p>';
  await Promise.all(subjList().map(loadSubj));renderFilters();
  if(reset||!CUR||deck().indexOf(CUR)<0){CUR=pick();SEL=[];DONE=false;BACK=[]}
  renderQ();
}
function renderQ(){
  var box=$("#qbox");
  if(!CUR){box.innerHTML='<p class="bx-k">問題</p><p>'+(ST.mode==="review"?"今日の復習はありません。間違えた問題は、翌日以降にここへ戻ってきます。":ST.mode==="wrong"?"間違えた問題はありません。":ST.mode==="new"?"この範囲の問題は、すべて一度は解きました。":"この範囲に問題がありません。")+'</p>';return}
  var PREV='<button type="button" class="bx-btn" id="tq-prev"'+(canPrev()?"":" disabled")+'>前へ</button>';
  var q=CUR,sj=SUBJ.filter(function(s){return s.id===q.subj})[0],multi=q.a.length>1,d=deck(),pos=d.indexOf(q);
  var h='<p class="bx-k tq-h"><span class="tq-sj" style="--gc:'+sj.color+'">'+esc(sj.short)+'</span> 問'+q.d+(ST.mode==="order"?' <span class="tq-pos">('+(pos+1)+' / '+d.length+')</span>':'')+'<span>'+esc(q.title)+'</span></p>';
  h+='<p class="tq-q">'+esc(q.q)+'</p>';if(multi&&!DONE)h+='<p class="tq-need">'+q.a.length+'つ選んでください</p>';
  h+='<div class="tq-o" role="group" aria-label="選択肢">'+q.o.map(function(o,i){var c="tq-b";if(DONE){if(q.a.indexOf(i)>=0)c+=" right";else if(SEL.indexOf(i)>=0)c+=" wrong";else c+=" dim"}else if(SEL.indexOf(i)>=0)c+=" sel";
    return '<button type="button" class="'+c+'" data-i="'+i+'"'+(DONE?" disabled":"")+'><b>'+"ABCDEFGH".charAt(i)+'</b><span>'+esc(o)+'</span></button>'}).join("")+'</div>';
  if(DONE){var ok=SEL.length===q.a.length&&SEL.every(function(i){return q.a.indexOf(i)>=0});
    h+='<div class="tq-ban '+(ok?"ok":"ng")+'">'+(ok?"正解です":"不正解 — 正解は "+q.a.map(function(i){return "ABCDEFGH".charAt(i)}).join("・"))+'</div>';
    h+='<div class="tq-ex"><b>解説</b><p>'+esc(q.ex)+'</p></div>';
    h+='<p class="tq-links"><a class="bx-go" href="/'+q.subj+'/#f-'+esc(q.xs||q.sec)+'">テキストで確認する</a>'+(/^https?:/.test(q.u)?' <a class="bx-go" href="'+esc(q.u)+'" target="_blank" rel="noopener noreferrer">参照ページ ↗</a>':'')+'</p>';
    h+='<div class="tq-act">'+PREV+'<button type="button" class="bx-go pri" id="tq-next">次の問題へ</button></div>';
  }else h+='<div class="tq-act">'+PREV+'<button type="button" class="bx-btn" id="tq-skip">次へ</button><button type="button" class="bx-go pri" id="tq-check"'+(SEL.length?"":" disabled")+'>答え合わせ</button></div>';
  h+='<p class="bx-s tq-key">キー操作: 1〜'+q.o.length+' で選ぶ、Enter で答え合わせ・次へ、← → で前へ・次へ</p>';
  box.innerHTML=h;
}
function choose(i){if(!CUR||DONE)return;var multi=CUR.a.length>1,k=SEL.indexOf(i);if(multi){if(k>=0)SEL.splice(k,1);else if(SEL.length<CUR.a.length)SEL.push(i)}else SEL=k>=0?[]:[i];renderQ()}
function check(){if(!CUR||DONE||!SEL.length)return;if(CUR.a.length>1&&SEL.length!==CUR.a.length)return;DONE=true;var ok=SEL.length===CUR.a.length&&SEL.every(function(i){return CUR.a.indexOf(i)>=0});record(CUR,ok);renderQ();renderFilters()}
function canPrev(){return ST.mode==="order"?deck().length>1:BACK.length>0}
function prev(){if(!CUR)return;var t=null;
  if(ST.mode==="order"){var d=deck(),i=d.indexOf(CUR);if(d.length>1)t=d[(i-1+d.length)%d.length];if(t)LS.set(posKey(),{s:t.subj,n:t.n})}
  else{while(BACK.length&&!t){var b=BACK.pop();if(deck().indexOf(b)>=0)t=b}}
  if(!t)return;CUR=t;SEL=[];DONE=false;renderFilters();renderQ();var x=$("#qbox");if(x&&x.getBoundingClientRect().top<0)x.scrollIntoView({block:"start",behavior:"smooth"})}
function next(){if(CUR){BACK.push(CUR);if(BACK.length>100)BACK.shift()}advance();CUR=pick();SEL=[];DONE=false;renderFilters();renderQ();var b=$("#qbox");if(b&&b.getBoundingClientRect().top<0)b.scrollIntoView({block:"start",behavior:"smooth"})}
function bindQ(){var box=$("#qbox");box.addEventListener("click",function(e){var b=e.target.closest(".tq-b");if(b){choose(+b.dataset.i);return}if(e.target.closest("#tq-check"))check();else if(e.target.closest("#tq-next")||e.target.closest("#tq-skip"))next();else if(e.target.closest("#tq-prev"))prev()});
  document.addEventListener("keydown",function(e){if(ST.tab!=="q"||e.target.closest&&e.target.closest("input,textarea,select,#fclose,a"))return;if(/^[1-8]$/.test(e.key)&&CUR&&+e.key<=CUR.o.length){choose(+e.key-1);e.preventDefault()}else if(e.key==="Enter"){DONE?next():check();e.preventDefault()}else if(e.key==="ArrowRight"){next();e.preventDefault()}else if(e.key==="ArrowLeft"){prev();e.preventDefault()}})}

/* 用語カード */
var TERMS={},TKN="cs-term-known-v1",KNOWN=LS.get(TKN,{}),TL=[],TI=0,FLIP=false;
var tkey=function(c){return c.subj+":"+c.s+":"+c.t};
async function loadTerms(id){if(TERMS[id])return TERMS[id];var rows=await getJSON("data/"+id+"/terms.json"),secs=await getJSON("data/"+id+"/sections.json");var rank={},title={};secs.forEach(function(s){var k=String(s.id).split(":").pop();rank[k]=s.sort_order;title[k]=s.title});
  TERMS[id]=rows.map(function(r,i){return {subj:id,s:r.s,t:r.t,d:r.d,title:title[r.s]||"",o:(rank[r.s]||999)*1000+i}}).sort(function(a,b){return a.o-b.o});return TERMS[id]}
async function renderTerms(rebuild){
  chips($("#g-subj"),subjItems(),ST.gsubj,function(v){ST.gsubj=v;save();TI=0;renderTerms(true)});
  var ids=ST.gsubj==="all"?SUBJ.map(function(s){return s.id}):[ST.gsubj];await Promise.all(ids.map(loadTerms));
  var all=[];ids.forEach(function(id){all=all.concat(TERMS[id]||[])});
  var todo=all.filter(function(c){return !KNOWN[tkey(c)]});
  chips($("#g-only"),[{v:"all",l:"すべて"},{v:"todo",l:"まだ覚えていないカード",n:todo.length}],ST.gonly,function(v){ST.gonly=v;save();TI=0;renderTerms(true)});
  $("#g-known").textContent="この範囲で覚えたカード "+(all.length-todo.length)+" / "+all.length+"枚";
  if(rebuild||!TL.length||TL.shuffled===undefined){TL=(ST.gonly==="todo"?todo:all).slice();TL.shuffled=false}
  drawCard();
}
function drawCard(){
  var fc=$("#fc");FLIP=false;fc.classList.remove("on");
  if(!TL.length){fc.querySelector(".front").innerHTML='<p>'+(ST.gonly==="todo"?"この範囲のカードは、すべて「覚えた」になっています。":"カードがありません。")+'</p>';fc.querySelector(".back").innerHTML="";$("#g-pos").textContent="";return}
  if(TI>=TL.length)TI=0;if(TI<0)TI=TL.length-1;var c=TL[TI],sj=SUBJ.filter(function(s){return s.id===c.subj})[0];
  fc.querySelector(".front").innerHTML='<p class="bx-k tq-h"><span class="tq-sj" style="--gc:'+sj.color+'">'+esc(sj.short)+'</span><span>'+esc(c.title)+'</span></p><h3>'+esc(c.t)+'</h3><p class="hint">押すと説明が出ます</p>';
  fc.querySelector(".back").innerHTML='<p class="bx-k"><span>'+esc(c.t)+'</span></p><p class="tc-d">'+esc(c.d)+'</p><p class="tq-links"><a class="bx-go" href="/'+c.subj+'/#f-'+esc(c.s)+'">テキストで確認する</a></p><div class="gk"><button type="button" data-k="again">まだ</button><button type="button" data-k="known"'+(KNOWN[tkey(c)]?' aria-pressed="true"':"")+'>覚えた</button></div>';
  $("#g-pos").textContent=(TI+1)+" / "+TL.length;
  var sb=$("#g-shuf");sb.textContent=TL.shuffled?"順番に戻す":"シャッフル";sb.setAttribute("aria-pressed",String(!!TL.shuffled));sb.title=TL.shuffled?"シャッフル中。押すと順番どおりに戻します":"カードの順番をシャッフルします";
}
function bindTerms(){
  var fc=$("#fc");fc.addEventListener("click",function(e){var k=e.target.closest(".gk button");if(k){e.stopPropagation();var c=TL[TI];if(k.dataset.k==="known")KNOWN[tkey(c)]=Date.now();else delete KNOWN[tkey(c)];LS.set(TKN,KNOWN);TI++;renderTerms(false);return}if(e.target.closest("a"))return;FLIP=!FLIP;fc.classList.toggle("on",FLIP)});
  fc.addEventListener("keydown",function(e){if(e.key===" "||e.key==="Enter"){e.preventDefault();FLIP=!FLIP;fc.classList.toggle("on",FLIP)}});
  $("#g-prev").onclick=function(){TI--;drawCard()};$("#g-next").onclick=function(){TI++;drawCard()};
  $("#g-shuf").onclick=function(){if(TL.shuffled){renderTerms(true)}else{for(var i=TL.length-1;i>0;i--){var j=Math.floor(Math.random()*(i+1)),t=TL[i];TL[i]=TL[j];TL[j]=t}TL.shuffled=true;TI=0;drawCard()}};
}

/* 大きく表示(社労士版と同じ): カード右上のボタンで画面いっぱいに。閉じるは右上の×・戻る・Esc */
var upHist=false;
function focusMode(on){document.body.classList.toggle("focus",on);
  if(on){$("#ftitle").textContent=ST.tab==="g"?"用語カード":"問題";renderMeter();window.scrollTo(0,0);requestAnimationFrame(function(){var b=$("#fclose");if(b)b.focus()})}
  else requestAnimationFrame(function(){setTab(ST.tab)})}
function closeFocus(){if(upHist)history.back();else focusMode(false)}
function bindFocus(){
  $$("[data-up]").forEach(function(b){b.onclick=function(e){e.stopPropagation();try{history.pushState({up:1},"");upHist=true}catch(x){upHist=false}focusMode(true)}});
  $("#fclose").onclick=function(e){e.stopPropagation();closeFocus()};
  window.addEventListener("popstate",function(){if(document.body.classList.contains("focus")){upHist=false;focusMode(false)}});
  document.addEventListener("keydown",function(e){if(e.key==="Escape"&&document.body.classList.contains("focus"))closeFocus()});
}
function init(){
  $$(".tabs [role=tab]").forEach(function(b){b.onclick=function(){setTab(b.id.slice(2))}});
  bindQ();bindTerms();bindFocus();renderMeter();
  if(location.hash==="#terms")ST.tab="g";
  setTab(ST.tab==="g"?"g":"q");requestAnimationFrame(function(){setTab(ST.tab)});
  refreshQ(true);
}
window.CSPractice={init:init};
})();
