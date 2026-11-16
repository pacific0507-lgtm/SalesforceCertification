/* ==学習計画(/plan/)。保存は cs-plan-v1(アカウントに同期)。社労士版の学習計画をもとに、複数の資格・受験日に対応== */
var csPlan=(function(){
var KEY="cs-plan-v1",TGK="cs-plan-tg-v1",AIK="cs-plan-ai-v1";
/* h: 合格までに必要な勉強時間の目安(時間)。qm: 1問にかける時間の目安(分) */
var SUBJ=[
 {id:"d360",short:"D360",title:"Data 360 コンサルタント",pal:"navy",h:60,qm:1.5},
 {id:"mcadmin",short:"MCA",title:"Marketing Cloud Administrator",pal:"orange",h:50,qm:1.5},
 {id:"afsales",short:"AF Sales",title:"Agentforce Sales コンサルタント",pal:"teal",h:40,qm:1.5},
 {id:"afspec",short:"AF Spec",title:"Agentforce スペシャリスト",pal:"purple",h:40,qm:1.5},
 {id:"mulepa",short:"Mule PA",title:"MuleSoft Platform Architect",pal:"blue",h:60,qm:2},
 {id:"fe",short:"FE",title:"基本情報技術者",pal:"olive",h:150,qm:2.5},
 {id:"sg",short:"SG",title:"情報セキュリティマネジメント",pal:"pink",h:80,qm:2}];
var PAL={navy:["#24345e","#90a6df","#dee3f2","#1c243b"],orange:["#b5560f","#f2a766","#f8e4d0","#3d2814"],teal:["#0b6e7c","#7ce5f3","#def0f2","#1c373b"],
 purple:["#6b3fa0","#c3a1f5","#e8dff5","#2b1f42"],blue:["#2456a6","#7db0ff","#dce7f7","#172a47"],olive:["#55691a","#cde38d","#edf2de","#333b1c"],pink:["#a8336d","#df90b7","#f2dee8","#3b1c2b"]};
var WD="日月火水木金土",DEFW=[90,30,30,30,30,30,90],REV=[0,3,5,7,10,14,21,28],QS=[20,30,40,50,60,70];
var ARR='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>';
function SB(id){for(var i=0;i<SUBJ.length;i++)if(SUBJ[i].id===id)return SUBJ[i];return null}
function subjs(){try{return window.csOrd?csOrd(SUBJ):SUBJ.slice()}catch(e){return SUBJ.slice()}}
function cv(id){var p=PAL[(SB(id)||{}).pal]||PAL.navy;return "--c1:"+p[0]+";--c2:"+p[1]+";--s1:"+p[2]+";--s2:"+p[3]}
function esc(t){return String(t==null?"":t).replace(/[&<>"']/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]})}
/* ---- 日付(端末の時刻の日付で数える) ---- */
function p2(n){return (n<10?"0":"")+n}
function ymd(d){return d.getFullYear()+"-"+p2(d.getMonth()+1)+"-"+p2(d.getDate())}
function pd(s){var a=String(s).split("-");return new Date(+a[0],+a[1]-1,+a[2])}
function okD(s){if(typeof s!=="string"||!/^\d{4}-\d\d-\d\d$/.test(s))return false;var d=pd(s);return !isNaN(d)&&ymd(d)===s}
function add(s,n){var d=pd(s);d.setDate(d.getDate()+n);return ymd(d)}
function diff(a,b){return Math.round((pd(b)-pd(a))/864e5)}
function today(){return ymd(new Date())}
function dow(s){return pd(s).getDay()}
function wk(s){return add(s,-((dow(s)+6)%7))}
function md(s){var d=pd(s);return (d.getMonth()+1)+"/"+d.getDate()}
function mdw(s){return md(s)+"("+WD[dow(s)]+")"}
function ymdJ(s){var d=pd(s);return d.getFullYear()+"年"+(d.getMonth()+1)+"月"+d.getDate()+"日"}
function K(m){m=Math.max(0,Math.round(m));var h=Math.floor(m/60),r=m%60;return h?h+"時間"+(r?r+"分":""):r+"分"}
function HR(h){return (Math.round(h*10)/10).toLocaleString("ja-JP")+"時間"}
function clamp(v,a,b){v=+v;if(!isFinite(v))v=a;return Math.max(a,Math.min(b,v))}
function LSj(k,d){try{var v=JSON.parse(localStorage.getItem(k)||"null");return v==null?d:v}catch(e){return d}}
function LSs(k,v){try{localStorage.setItem(k,JSON.stringify(v))}catch(e){}}
function obj(x){return !!x&&typeof x==="object"&&!Array.isArray(x)}
/* ---- 保存(cs-plan-v1)。壊れたデータ・知らない資格は捨てる ---- */
function normP(p,used){if(!obj(p))return null;var s=SB(p.subj);if(!s||!okD(p.exam))return null;
  var id=typeof p.id==="string"&&/^[\w-]{1,24}$/.test(p.id)?p.id:"p"+Math.random().toString(36).slice(2,9);while(used[id])id+="x";used[id]=1;
  var sn=obj(p.snap)&&okD(p.snap.d)?{d:p.snap.d,h:clamp(p.snap.h,0,5000),r:Math.round(clamp(p.snap.r,0,999)),a:Math.round(clamp(p.snap.a,0,99999))}:null;
  return {id:id,subj:s.id,exam:p.exam,fixed:!!p.fixed,start:okD(p.start)?p.start:"",goalH:Math.round(clamp(p.goalH!=null?p.goalH:s.h,1,3000)),baseH:Math.round(clamp(p.baseH,0,3000)),
    revD:Math.round(clamp(p.revD!=null?p.revD:7,0,60)),qs:Math.round(clamp(p.qs!=null?p.qs:40,10,90)),res:["pass","fail","skip"].indexOf(p.res)>=0?p.res:"",resAt:+p.resAt||0,snap:sn,at:+p.at||0}}
function norm(d){if(!obj(d))d={};var r={v:1,ts:+d.ts||0,wk:d.wk?1:0,week:DEFW.slice(),plans:[]},used={};
  if(Array.isArray(d.week)&&d.week.length===7)r.week=d.week.map(function(x){return Math.round(clamp(x,0,960))});
  (Array.isArray(d.plans)?d.plans:[]).forEach(function(p){var q=normP(p,used);if(q&&r.plans.length<20)r.plans.push(q)});
  return r}
function load(){return norm(LSj(KEY,null))}
function save(D){D.ts=Date.now();LSs(KEY,D)}
/* ---- 学習の記録を読む(端末+アカウント) ---- */
var JC={};
function getJ(u){return JC[u]=JC[u]||fetch(window.famURL?window.famURL(u):u).then(function(r){return r.ok?r.json():[]}).catch(function(){return []})}
var DBP=null;
function dbp(){return DBP||(DBP=(async function(){try{var c=window.claude;if(!c||!c.use)return null;var a=await Promise.all([c.use("db"),c.use("user")]);var u=a[1]?await a[1].id():null;return a[0]&&u?{db:a[0],uid:u}:null}catch(e){return null}})())}
async function rdoc(sid,name){var x=await dbp();if(!x)return null;try{var g=await x.db.doc("data/users/"+x.uid+"/"+sid+"-"+name).get();return g&&g.exists?g.data():null}catch(e){return null}}
function skey(k){k=String(k||"");k=k.split(":").pop();return k.indexOf("f-")===0?k.slice(2):k}
var SC={};
function stats(sid,remote){var ck=sid+(remote?":r":":l");return SC[ck]=SC[ck]||(async function(){
  var secs=[],qr=[];try{secs=await getJ("data/"+sid+"/sections.json")}catch(e){}try{qr=await getJ("data/"+sid+"/qrows.json")}catch(e){}
  secs=(Array.isArray(secs)?secs:[]).filter(obj).slice().sort(function(a,b){return (a.sort_order||0)-(b.sort_order||0)}).map(function(x){return {k:skey(x.id),t:String(x.title||""),no:String(x.no||"")}});
  qr=Array.isArray(qr)?qr.filter(obj):[];
  var q=LSj("sr-"+sid+"-quiz-v1",{}),st=LSj("sr-"+sid+"-study-v1",{}),act=LSj("sr-"+sid+"-act-v1",{});
  if(!obj(q))q={};if(!obj(st))st={};if(!obj(act))act={};
  if(remote){var r=await Promise.all([rdoc(sid,"quiz"),rdoc(sid,"study"),rdoc(sid,"act")]);
    try{var rq=r[0]&&r[0].json?JSON.parse(r[0].json):null;if(obj(rq)&&obj(rq.hist)&&(+rq.ts||0)>(+q.ts||0))q=rq}catch(e){}
    if(obj(r[1])&&(+r[1].ts||0)>(+st.ts||0))st=r[1];
    if(obj(r[2])){try{act=window.CSQ?CSQ.actMerge(act,r[2]):((+r[2].ts||0)>(+act.ts||0)?r[2]:act)}catch(e){}}}
  var read={},done={},days={},h=obj(q.hist)?q.hist:{};
  if(obj(st.done))Object.keys(st.done).forEach(function(k){if(st.done[k])done[skey(k)]=1});
  var ad=obj(act.d)?act.d:{};
  Object.keys(ad).forEach(function(k){var x=ad[k];if(!okD(k)||!obj(x))return;var t=+x.t||0;
    if(!(t>0)&&obj(x.v))Object.keys(x.v).forEach(function(v){t+=+(x.v[v]&&x.v[v].t)||0});
    days[k]=t;(Array.isArray(x.r)?x.r:[]).forEach(function(s){read[skey(s)]=1})});
  var tm=LSj("ls-time-v1",{});tm=obj(tm)&&obj(tm.d)?tm.d:{};
  Object.keys(tm).forEach(function(k){var v=obj(tm[k])&&obj(tm[k].k)?+tm[k].k[sid]||0:0;if(okD(k)&&v>(days[k]||0))days[k]=v});
  var ans=0,wrong=0;qr.forEach(function(r){var e=h[r.n];if(obj(e)&&(+e.n||0)>0){ans++;if(e.l==="x")wrong++}});
  return {secs:secs,read:read,done:done,days:days,qn:qr.length,ans:ans,wrong:wrong}})()}
async function loadStats(ids,remote){var o={};await Promise.all(ids.map(async function(id){try{o[id]=await stats(id,remote)}catch(e){o[id]={secs:[],read:{},done:{},days:{},qn:0,ans:0,wrong:0}}}));return o}
function EMPTY(){return {secs:[],read:{},done:{},days:{},qn:0,ans:0,wrong:0}}
/* ---- 計画を立てる ----
   1) 資格ごとに、残りの時間(必要な時間 − これまでの勉強時間)を出す
   2) 日ごとの使える時間を、その日に勉強する資格で分ける。分け方は「残りの時間 ÷ 試験までの使える時間」(急ぐ度合い)の比で、
      どの資格も同じくらいの割合で間に合うように少しずつ直す(試験日が早い・残りが多い資格ほど多め。ただし3割は均等に分け、後の試験の資格も止めない)
   3) 資格ごとに、日の時間を「テキストを読む」と「問題を解く」(問題演習の割合)に分け、まだ読んでいない節 → 理解した印のない節の順に割り当てる。
      問題は、まだ解いていない問題と間違えた問題から。本試験の前の総復習の期間は、問題と見直しだけにする
   毎回、いまの記録から立て直すので、遅れや先取りは残りの日に自動で振り分け直される */
function compute(D,ST,T){T=T||today();ST=ST||{};
  var R={today:T,list:[],on:[],days:[],todo:[],todayMin:0,todaySec:0,week:D.week};
  D.plans.forEach(function(P){var s=SB(P.subj),st=ST[P.subj]||EMPTY(),x={P:P,s:s,st:st,left:diff(T,P.exam)};
    x.state=P.res?"fin":x.left<0?"ask":x.left===0?"exam":(P.start&&P.start>T)?"wait":"on";
    var tot=0;Object.keys(st.days).forEach(function(k){if(k<T)tot+=st.days[k]});
    x.todaySec=st.days[T]||0;x.doneH=tot/3600+P.baseH;x.remainH=Math.max(0,P.goalH-x.doneH);
    x.secsN=st.secs.length;x.unread=st.secs.filter(function(c){return !st.read[c.k]&&!st.done[c.k]});
    x.notDone=st.secs.filter(function(c){return st.read[c.k]&&!st.done[c.k]});
    x.nRead=x.secsN-x.unread.length;x.nDone=st.secs.filter(function(c){return st.done[c.k]}).length;
    x.qn=st.qn;x.ans=Math.min(st.ans,st.qn);x.wrong=st.wrong;x.newQ=Math.max(0,st.qn-st.ans);
    R.list.push(x)});
  var on=R.list.filter(function(x){return x.state==="on"||x.state==="wait"});R.on=on;
  var end=T;on.forEach(function(x){if(x.P.exam>end)end=x.P.exam});
  var N=Math.min(1100,diff(T,end)),days=[];
  for(var i=0;i<N;i++){var d=add(T,i);days.push({d:d,cap:+D.week[dow(d)]||0,sh:{}})}
  R.days=days;
  on.forEach(function(x){x.from=x.P.start&&x.P.start>T?x.P.start:T;x.R=x.remainH*60;x.idx=[];
    days.forEach(function(dy,i){if(dy.d>=x.from&&dy.d<x.P.exam)x.idx.push(i)});
    x.capSum=x.idx.reduce(function(a,i){return a+days[i].cap},0);x.rho=x.R>0?(x.capSum>0?x.R/x.capSum:1):0});
  function share(){on.forEach(function(x){x.A=0});
    days.forEach(function(dy){var t=0,ac=on.filter(function(x){return dy.d>=x.from&&dy.d<x.P.exam});
      ac.forEach(function(x){t+=x.rho});dy.sh={};var nn=ac.filter(function(x){return x.R>0}).length;ac.forEach(function(x){var f=x.R>0&&t>0?.3/nn+.7*x.rho/t:0;dy.sh[x.P.id]=f;x.A+=dy.cap*f})})}
  for(var it=0;it<60;it++){share();var ch=0;
    on.forEach(function(x){if(x.R<=0||x.A<=0)return;var f=clamp(Math.sqrt(x.R/x.A),.5,2);x.rho*=f;ch=Math.max(ch,Math.abs(f-1))});
    var sm=on.reduce(function(a,x){return a+x.rho},0);if(sm>0)on.forEach(function(x){x.rho/=sm});if(ch<.002)break}
  share();
  var tg=LSj(TGK,{});if(!obj(tg))tg={};
  on.forEach(function(x){var P=x.P,u=x.A>0?x.R/x.A:(x.R>0?Infinity:0);x.u=u;
    var left=diff(x.from,P.exam),rv=Math.min(P.revD,Math.floor(left/3));x.rv=rv;x.revStart=add(P.exam,-rv);
    x.days=x.idx.map(function(i){var dy=days[i];return {d:dy.d,m:isFinite(u)?dy.cap*(dy.sh[P.id]||0)*u:0}});
    var qs=P.qs/100,W=x.unread.map(function(c){return {c:c,w:1}}).concat(x.notDone.map(function(c){return {c:c,w:.5,re:1}}));
    var units=W.reduce(function(a,y){return a+y.w},0),readPre=0;
    x.days.forEach(function(z){if(z.d<x.revStart)readPre+=z.m*(1-qs)});
    var S=units?clamp(readPre/units,15,60):30;x.S=S;
    var wi=0,carry=0,cumQ=0,prevQ=0,pool=x.newQ+x.wrong;
    x.days.forEach(function(z){var rev=z.d>=x.revStart,readM=wi<W.length?(rev?z.m*(1-qs)*.5:z.m*(1-qs)):0;
      var b=readM+carry;z.secs=[];z.cont=(carry<-.5&&wi>0)?W[wi-1]:null;
      while(wi<W.length&&b>.5){var y=W[wi++];z.secs.push(y);b-=y.w*S}
      var spare=0;if(wi>=W.length&&b>0){spare=b;b=0}carry=Math.min(0,b);
      var qM=z.m-readM+spare;z.qM=qM;z.rM=readM-spare;cumQ+=qM/x.s.qm;var nq=Math.round(cumQ)-prevQ;prevQ=Math.round(cumQ);
      var nn=Math.min(nq,pool);pool-=nn;z.qNew=nn;z.qRev=nq-nn;z.rev=rev});
    x.weeks=[];x.days.forEach(function(z){var k=wk(z.d),w=x.weeks[x.weeks.length-1];
      if(!w||w.k!==k){w={k:k,from:z.d,to:z.d,m:0,secs:0,re:0,q:0,qr:0,rev:false};x.weeks.push(w)}
      w.to=z.d;w.m+=z.m;z.secs.forEach(function(y){if(y.re)w.re++;else w.secs++});w.q+=z.qNew;w.qr+=z.qRev;if(z.rev)w.rev=true});
    x.today=x.days.length&&x.days[0].d===T?x.days[0]:null;
    x.needPerDay=x.idx.length?x.R/x.idx.length:0;
    /* 予定ではここまで: 計画を作った日から試験の日までの使える時間のうち、きのうまでの分の割合 */
    var sn=P.snap,exp=0;
    if(sn&&sn.d<T){var a=0,b=0,n=0;for(var d=sn.d;d<P.exam&&n<1500;d=add(d,1),n++){var c=+D.week[dow(d)]||0;b+=c;if(d<T)a+=c}exp=b>0?a/b:0}
    var fr=function(now,base,tot){return tot-base>0?clamp((now-base)/(tot-base),0,1):1};
    var b0=sn||{h:0,r:0,a:0};
    x.aH=fr(x.doneH+x.todaySec/3600,Math.min(b0.h,P.goalH-.01),P.goalH);x.aR=fr(x.nRead,Math.min(b0.r,x.secsN),x.secsN);x.aQ=fr(x.ans,Math.min(b0.a,x.qn),x.qn);
    x.exp=exp;x.act=.4*x.aH+.3*x.aR+.3*x.aQ;x.lag=exp-x.act;
    x.eH=b0.h+(P.goalH-b0.h)*exp;x.eR=b0.r+(x.secsN-b0.r)*exp;x.eQ=b0.a+(x.qn-b0.a)*exp;
    x.pace=x.state==="wait"?"wait":x.R<=0?"done":!isFinite(u)?"none":(u>1.15||x.lag>.12)?"late":(u>1||x.lag>.04)?"slow":(u<=.85&&x.lag<=0)?"ahead":"ok";
    var lt=0,la=0;for(var j=1;j<=7;j++){var dd=add(T,-j),g=obj(tg[dd])?+tg[dd][P.id]:NaN;if(isFinite(g)){lt+=g;la+=(x.st.days[dd]||0)/60}}x.lastT=lt;x.lastA=la});
  days.forEach(function(dy,i){dy.parts=[];dy.tot=0;on.forEach(function(x){var k=x.idx.indexOf(i);if(k>=0&&x.days[k].m>=.5){dy.parts.push({x:x,m:x.days[k].m});dy.tot+=x.days[k].m}})});
  R.todo=on.filter(function(x){return x.today&&x.today.m>=1}).sort(function(a,b){return a.P.exam<b.P.exam?-1:a.P.exam>b.P.exam?1:0});
  R.todayMin=R.todo.reduce(function(a,x){return a+x.today.m},0);
  var seen={};R.list.forEach(function(x){if((x.state==="on"||x.state==="exam")&&!seen[x.P.subj]){seen[x.P.subj]=1;R.todaySec+=x.todaySec}});
  return R}
/* 今日の目安を端末に残す(先週の目安と実際の比較に使う。60日分) */
function recordTg(R){try{var tg=LSj(TGK,{});if(!obj(tg))tg={};var o={},ch=false;R.on.forEach(function(x){if(x.today)o[x.P.id]=Math.round(x.today.m)});
  if(JSON.stringify(tg[R.today]||{})!==JSON.stringify(o)){tg[R.today]=o;ch=true}
  var lim=add(R.today,-60);Object.keys(tg).forEach(function(k){if(!okD(k)||k<lim){delete tg[k];ch=true}});if(ch)LSs(TGK,tg)}catch(e){}}
/* 曜日ごとの時間を、どの計画も間に合うように合わせる(土日は平日の2.5倍) */
function fitWeek(D,ST,T){var pat=[2.5,1,1,1,1,1,2.5],r15=function(v){return Math.ceil(v/15)*15};
  var mk=function(k){return pat.map(function(p){return Math.min(600,r15(k*p))})};
  var ok=function(w){var E=Object.assign({},D,{week:w});var R=compute(E,ST,T);return R.on.every(function(x){return x.state==="wait"||x.R<=0||(isFinite(x.u)&&x.u<=1.0001)})};
  if(!ok(mk(240)))return mk(240);var lo=0,hi=240;for(var i=0;i<24;i++){var m=(lo+hi)/2;if(ok(mk(m)))hi=m;else lo=m}
  var w=mk(hi);return w.map(function(v,i){return Math.max(pat[i]>1?30:15,v)})}
var PACE={ahead:["余裕あり","いまのペースなら、予定より早く仕上がります。"],ok:["順調","予定どおり進んでいます。"],slow:["少し遅れ","少しだけ遅れています。残りの日に振り分け直しました。"],
  late:["遅れ","このままだと間に合わないかもしれません。使える時間か、必要な時間を見直しましょう。"],done:["目標に到達","必要な時間に届きました。総復習と問題演習で仕上げましょう。"],
  none:["時間が未設定","曜日ごとに使える時間を入れてください。"],wait:["開始前","始める日から計画を立てます。"]};
function paceChip(x){var p=PACE[x.pace]||PACE.ok;return '<span class="pace '+x.pace+'">'+p[0]+'</span>'}
function prLink(x){var f=x.newQ>0?"new":x.wrong>0?"wrong":"all";if(x.today&&x.today.rev&&x.wrong>0)f="wrong";return "/practice/#s="+x.P.subj+"&f="+f}
function secLink(sid,c){return "/"+sid+"/#f-"+encodeURIComponent(c.k)}
function secName(c){var no=c.no?c.no.replace(/^Ch/,""):"";return (no?'<small>'+esc(no)+'</small>':'')+'<span>'+esc(c.t)+'</span>'}
/* 今日やることの1行(資格ごと) */
function todoHTML(x,mini){var z=x.today,s=x.s,h='';
  var items=z.secs.slice(0,mini?2:6),more=z.secs.length-items.length;
  var nq=z.qNew+z.qRev;if(nq<1&&z.qM>=x.s.qm*.6)nq=1;
  if(mini){var t=[];if(z.cont)t.push("続き: "+esc(z.cont.c.t));items.forEach(function(y){t.push((y.re?"見直し: ":"")+esc(y.c.t))});if(more>0)t.push("ほか"+more+"節");if(nq)t.push("問題 約"+nq+"問");
    return '<li class="pc" style="'+cv(s.id)+'"><b>'+esc(s.short)+'</b><span>'+(t.join("・")||"総復習")+'</span><small>'+K(z.m)+'</small></li>'}
  h+='<li class="pc" style="'+cv(s.id)+'"><div class="hd2"><b>'+esc(s.short)+'<em>'+esc(s.title)+'</em></b><small>'+K(z.m)+(z.rev?"・総復習":"")+'</small></div>';
  var L='';if(z.cont)L+='<li><a href="'+secLink(s.id,z.cont.c)+'"><i class="tg">続き</i>'+secName(z.cont.c)+'</a></li>';
  items.forEach(function(y){L+='<li><a href="'+secLink(s.id,y.c)+'">'+(y.re?'<i class="tg re">見直し</i>':'<i class="tg">読む</i>')+secName(y.c)+'</a></li>'});
  if(more>0)L+='<li class="more">ほか '+more+' 節</li>';
  if(nq)L+='<li><a href="'+prLink(x)+'"><i class="tg q">問題</i><span>約'+nq+'問'+(z.rev?'(間違えた問題・まだ解いていない問題を中心に)':z.qNew>=nq?'(まだ解いていない・間違えた問題から)':'(2周目の復習)')+'</span></a></li>';
  if(!L)L='<li class="more">間違えた問題としおりを付けた問題を中心に、総復習しましょう。</li>';
  h+='<ul>'+L+'</ul><div class="acts">'+(z.secs.length||z.cont?'<a href="'+secLink(s.id,(z.cont||z.secs[0]).c)+'">テキストを開く</a>':'')+(nq?'<a href="'+prLink(x)+'">トレーニングで解く</a>':'')+'<a href="/'+s.id+'/#quiz">問題集</a></div></li>';
  return h}
function meter(done,tgt){var r=tgt>0?Math.min(100,Math.round(done/tgt*100)):done>0?100:0;return '<div class="pl-meter" role="progressbar" aria-valuemin="0" aria-valuemax="100" aria-valuenow="'+r+'"><i style="width:'+r+'%"></i></div>'}
/* ==== ページ ==== */
var PG=null;
function page(){var root=document.getElementById("pl-root");if(!root)return;
  PG={root:root,D:load(),ST:null,remote:false,form:null,open:{},T:today(),ai:null};
  root.innerHTML='<div id="pl-ask"></div><div id="pl-main"><div class="ld" role="status"><span class="ld-f" aria-hidden="true"><img src="brand/raf-face.webp" alt="" width="44" height="44"></span><small>計画を立てています…</small></div></div><div id="pl-form"></div><div id="pl-side"></div>';
  var ids=SUBJ.map(function(s){return s.id});
  loadStats(ids,false).then(function(st){if(!PG.remote)PG.ST=st;draw();if(location.hash==="#new"||!PG.D.plans.some(function(p){return !p.res}))openForm("new")});
  loadStats(ids,true).then(function(st){PG.ST=st;PG.remote=true;draw()});
  /* アカウントからの読み込み(fam-ls)が遅れて終わったときは、計画を読み直す */
  var raw0=localStorage.getItem(KEY),n=0,tk=setInterval(function(){n++;if(!document.getElementById("pl-root")||n>40){clearInterval(tk);return}
    var r=null;try{r=localStorage.getItem(KEY)}catch(e){}if(r!==raw0){raw0=r;if(!PG.form){PG.D=load();draw()}}},1500);
  try{var c=window.claude;(c&&c.use?c.use("sample"):Promise.resolve(null)).then(function(x){PG.ai=x||false;drawSide()},function(){PG.ai=false;drawSide()})}catch(e){PG.ai=false}
  addEventListener("ls-theme",function(){if(document.getElementById("pl-root"))draw()});
  root.addEventListener("click",onClick);root.addEventListener("change",onChange);root.addEventListener("input",onInput)}
function draw(){if(!PG||!PG.ST)return;PG.T=today();var R=compute(PG.D,PG.ST,PG.T);PG.R=R;recordTg(R);drawAsk(R);drawMain(R);drawSide();if(PG.form)formInfo()}
function drawAsk(R){var el=document.getElementById("pl-ask");if(!el)return;
  el.innerHTML=R.list.filter(function(x){return x.state==="ask"}).map(function(x){var P=x.P,s=x.s;
    return '<section class="bx pl-res pc" style="'+cv(s.id)+'" data-pid="'+P.id+'"><p class="bx-k">試験の結果<span>'+ymdJ(P.exam)+'</span></p><h3 class="bx-t sm"><b class="sj">'+esc(s.short)+'</b> '+esc(s.title)+'の試験はどうでしたか?</h3>'+
      '<p class="bx-s">結果を教えてください。合格なら「合格」の印を付けます(テキスト一覧の合格の印・庭の仲間にも反映されます)。</p>'+
      '<div class="pf-btns"><button type="button" class="bx-go pri" data-res="pass">合格した</button><button type="button" class="bx-go" data-res="fail">不合格だった</button><button type="button" class="bx-go" data-res="skip">受けなかった・日が変わった</button></div></section>'}).join("")}
function drawMain(R){var el=document.getElementById("pl-main");if(!el)return;var T=R.today,h='';
  var live=R.list.filter(function(x){return x.state!=="fin"&&x.state!=="ask"});
  if(!live.length){el.innerHTML='<section class="bx pl-empty"><img src="chars/rou-smile.webp" alt="" width="64" height="64"><div><h3 class="bx-t sm">まだ計画がありません</h3><p class="bx-s">資格と受験予定日を入れると、今日から試験の日までの勉強の予定と、毎日の「今日やること」を出します。</p></div></section>'+addBtn();return}
  /* 今日やること */
  var exams=live.filter(function(x){return x.state==="exam"});
  h+='<section class="bx pl-today" aria-labelledby="h-td"><p class="bx-k" id="h-td">今日やること<span>'+mdw(T)+'</span></p>';
  exams.forEach(function(x){h+='<p class="pl-exam pc" style="'+cv(x.s.id)+'"><b>'+esc(x.s.short)+'</b> 今日は試験の日です。落ち着いて、がんばってください!</p>'});
  if(R.todo.length){var dn=R.todaySec/60;
    h+='<h3 class="bx-t">目安 '+K(R.todayMin)+'</h3>'+meter(dn,R.todayMin)+'<p class="bx-s">今日 '+K(dn)+' 勉強しました'+(dn>=R.todayMin?'。今日の目安は達成です!':'(あと '+K(R.todayMin-dn)+')')+
      (R.todayMin>(+R.week[dow(T)]||0)+1?'。使える時間('+K(+R.week[dow(T)]||0)+')より多めの目安です':'')+'</p><ul class="td-list">'+R.todo.map(function(x){return todoHTML(x)}).join("")+'</ul>';
    var lt=0,la=0;R.on.forEach(function(x){lt+=x.lastT;la+=x.lastA});
    if(lt>0)h+='<p class="bx-s pl-last">この1週間: 目安 '+K(lt)+' に対して '+K(la)+'。'+(la>=lt?'予定どおり進んでいます。':'足りなかった '+K(lt-la)+' は、残りの日に振り分け直しました。')+'</p>'}
  else if(!exams.length){var w=R.on.filter(function(x){return x.state==="wait"});
    h+='<h3 class="bx-t sm">'+(w.length&&!R.on.some(function(x){return x.state==="on"})?'計画は '+md(w.reduce(function(a,x){return x.P.start<a?x.P.start:a},"9999-99-99"))+' から始まります':(+R.week[dow(T)]||0)?'今日の目安は終わっています':'今日はお休みの日です')+'</h3><p class="bx-s">'+((+R.week[dow(T)]||0)?'必要な時間に届いているか、今日の分がありません。気になるところの復習をどうぞ。':'曜日ごとの時間で、今日は0分にしています。少しでも進めたら、そのぶん先の日が楽になります。')+'</p>'}
  h+='</section>';
  /* 2週間の予定 */
  h+=stripHTML(R);
  /* 計画ごと */
  live.slice().sort(function(a,b){return a.P.exam<b.P.exam?-1:1}).forEach(function(x){h+=planHTML(x,R)});
  h+=addBtn();
  el.innerHTML=h}
function addBtn(){return '<div class="pl-add"><button type="button" class="bx-go pri" data-act="new"'+(PG&&PG.form?' hidden':'')+'>＋ 計画を追加</button></div>'}
function stripHTML(R){var T=R.today,st=wk(T),cells='',max=1,map={};R.days.forEach(function(d){map[d.d]=d;if(d.tot>max)max=d.tot});
  var tg=LSj(TGK,{});if(!obj(tg))tg={};var exams={};R.list.forEach(function(x){if(x.state!=="fin")(exams[x.P.exam]=exams[x.P.exam]||[]).push(x)});
  for(var i=0;i<14;i++){var d=add(st,i),c=map[d],cls=d===T?" now":d<T?" past":"",inner='',lab='';
    if(d<T){var a=0;R.list.forEach(function(x){if(x.state!=="fin")a+=(x.st.days[d]||0)/60});var g=0;if(obj(tg[d]))Object.keys(tg[d]).forEach(function(k){g+=+tg[d][k]||0});
      lab=a>=1?K(a):'—';if(g>0&&a>=g)cls+=" met";inner='<i class="act" style="height:'+Math.min(100,Math.round(a/Math.max(max,g,1)*100))+'%"></i>'}
    else if(c){lab=c.tot>=1?K(c.tot):'休み';inner=c.parts.map(function(p){return '<i class="pc" style="'+cv(p.x.s.id)+';height:'+Math.max(4,Math.round(p.m/max*100))+'%"></i>'}).join("")}
    else lab='';
    var ex=exams[d]?'<em class="ex pc" style="'+cv(exams[d][0].s.id)+'">試験</em>':'';
    cells+='<li class="'+cls.trim()+'"><span class="dw">'+WD[dow(d)]+'</span><span class="dt">'+pd(d).getDate()+'</span><div class="cb">'+inner+'</div><small>'+lab+'</small>'+ex+'</li>'}
  return '<section class="bx pl-strip" aria-labelledby="h-st"><p class="bx-k" id="h-st">2週間の予定<span>'+md(st)+'〜'+md(add(st,13))+'</span></p><ol class="strip">'+cells+'</ol><p class="bx-s">棒の色は資格ごとの時間。過ぎた日は勉強した時間で、目安に届いた日は緑になります。</p></section>'}
function bar(lbl,now,tot,exp,unit){var r=tot>0?Math.min(100,now/tot*100):0,e=tot>0&&exp!=null?Math.min(100,exp/tot*100):null;
  return '<div class="pb"><div class="pbh"><span>'+lbl+'</span><span>'+now+(tot?' / '+tot:'')+unit+'</span></div><div class="pbb"><i style="width:'+r.toFixed(1)+'%"></i>'+(e!=null&&e>0.5?'<b style="left:'+e.toFixed(1)+'%" title="予定ではここまで"></b>':'')+'</div></div>'}
function planHTML(x,R){var P=x.P,s=x.s,h='',open=PG.open[P.id];
  h+='<section class="bx pl-card pc" style="'+cv(s.id)+'" data-pid="'+P.id+'"><div class="pc-h"><b class="sj">'+esc(s.short)+'</b><div><h3>'+esc(s.title)+'</h3><p>'+ymdJ(P.exam)+'('+WD[dow(P.exam)]+') <span class="st'+(P.fixed?' fx':'')+'">'+(P.fixed?'申込済み':'予定')+'</span></p></div>'+
    '<div class="cd">'+(x.state==="exam"?'<b>今日</b>':'<small>あと</small><b>'+x.left+'</b><small>日</small>')+'</div></div>';
  if(x.state==="on"||x.state==="wait"){var pc=PACE[x.pace]||PACE.ok;
    h+='<p class="pc-p">'+paceChip(x)+'<span>'+pc[1]+'</span></p>';
    var hn=Math.round((x.doneH+x.todaySec/3600)*10)/10;
    h+='<div class="pbs">'+bar("読んだ節",x.nRead,x.secsN,x.exp>0?x.eR:null,"節")+bar("解いた問題",x.ans,x.qn,x.exp>0?x.eQ:null,"問")+bar("勉強時間",hn,P.goalH,x.exp>0?x.eH:null,"時間")+'</div>'+
      '<p class="bx-s pc-n">'+(x.state==="wait"?md(P.start)+' から開始・':'')+'残り '+HR(x.remainH)+'・1日あたり約 '+K(x.needPerDay)+(x.rv?'・総復習は '+md(x.revStart)+' から':'')+(x.exp>0?'・目盛りは予定ではここまで':'')+'</p>';
    h+='<div class="pf-btns"><button type="button" class="bx-go" data-act="weeks" aria-expanded="'+(open?"true":"false")+'">'+(open?'週ごとの計画を閉じる':'週ごとの計画')+'</button><button type="button" class="bx-go" data-act="edit">変更・削除</button></div>';
    if(open)h+=weeksHTML(x,R)}
  else h+='<div class="pf-btns"><button type="button" class="bx-go" data-act="edit">変更・削除</button></div>';
  return h+'</section>'}
function weeksHTML(x,R){var cur=wk(R.today),ws=x.weeks,more=PG.open[x.P.id]==="all",show=more?ws:ws.slice(0,5);
  if(!ws.length)return '<p class="bx-s">試験の日までの日がありません。</p>';
  return '<ul class="wk-list">'+show.map(function(w){var t=[];if(w.secs)t.push('読む '+w.secs+'節');if(w.re)t.push('見直し '+w.re+'節');if(w.q)t.push('問題 '+w.q+'問');if(w.qr)t.push('復習 '+w.qr+'問');
    var dn='';if(w.k===cur){var a=0;for(var d=w.k;d<=R.today;d=add(d,1))a+=(x.st.days[d]||0)/60;dn='<small class="dn">今週ここまで '+K(a)+'</small>'}
    return '<li class="'+(w.k===cur?'cur ':'')+(w.rev?'rev':'')+'"><div class="wh"><span>'+md(w.from)+'〜'+md(w.to)+(w.rev?' <i>総復習</i>':'')+'</span><b>'+K(w.m)+'</b></div><p>'+(t.join('・')||'見直しと問題演習')+'</p>'+dn+'</li>'}).join("")+'</ul>'+
    (ws.length>5?'<button type="button" class="pl-more" data-act="wall">'+(more?'最初の5週だけにする':'すべての週を見る('+ws.length+'週)')+'</button>':'')}
function drawSide(){var el=document.getElementById("pl-side");if(!el||!PG||!PG.ST)return;var D=PG.D,h='';
  h+='<section class="bx pl-set" aria-labelledby="h-wkset"><p class="bx-k" id="h-wkset">曜日ごとに使える時間<span class="saved" id="pl-saved" hidden>保存しました</span></p><p class="bx-s">すべての計画で共通です。勉強できない日は0分に。計画が複数あるときは、この時間を試験の日の近さと残りの量で分けます。</p>'+weekSel(D.week,"wd")+
    '<div class="pf-btns"><button type="button" class="bx-go" data-act="fit">必要な時間に合わせる</button></div></section>';
  var fin=PG.R?PG.R.list.filter(function(x){return x.state==="fin"}):[];
  h+=aiHTML();
  if(fin.length)h+='<section class="bx pl-fin"><p class="bx-k">終わった計画</p><ul>'+fin.map(function(x){var r=x.P.res;return '<li class="pc" style="'+cv(x.s.id)+'" data-pid="'+x.P.id+'"><b class="sj">'+esc(x.s.short)+'</b><span>'+ymdJ(x.P.exam)+'</span><em class="rs '+r+'">'+(r==="pass"?'合格':r==="fail"?'不合格':'受けなかった')+'</em><button type="button" class="x" data-act="delfin" aria-label="この記録を消す">×</button></li>'}).join("")+'</ul></section>';
  el.innerHTML=h}
function weekSel(w,attr){var o='';for(var m=0;m<=600;m+=15)o+=m+",";var ms=o.split(",").filter(Boolean).map(Number);
  return '<div class="wkin">'+w.map(function(v,i){return '<label>'+WD[i]+'<select data-'+attr+'="'+i+'" aria-label="'+WD[i]+'曜日に使える時間">'+ms.map(function(m){return '<option value="'+m+'"'+(m===v?' selected':'')+'>'+Math.floor(m/60)+':'+p2(m%60)+'</option>'}).join("")+(ms.indexOf(v)<0?'<option value="'+v+'" selected>'+K(v)+'</option>':'')+'</select></label>'}).join("")+'</div>'}
var saveT=0;
function saved(){var e=document.getElementById("pl-saved");if(!e)return;e.hidden=false;clearTimeout(saveT);saveT=setTimeout(function(){e.hidden=true},1600)}
function commit(){save(PG.D);draw();saved()}
/* ---- 計画の追加・変更のフォーム ---- */
function openForm(id){if(!PG||!PG.ST)return;var D=PG.D,T=PG.T,P=id==="new"?null:D.plans.filter(function(p){return p.id===id})[0];if(id!=="new"&&!P)return;
  var used={};D.plans.forEach(function(p){if(!p.res)used[p.subj]=1});
  var pass=LSj("cs-subj-passed",{});if(!obj(pass))pass={};
  var def=P||{subj:(subjs().filter(function(s){return !used[s.id]&&!pass[s.id]})[0]||subjs()[0]).id,exam:add(T,60),fixed:false,start:"",revD:7,qs:40,baseH:0};
  if(!P&&PG.pre){Object.assign(def,PG.pre);PG.pre=null}
  var s0=SB(def.subj);PG.form={id:id,goalTouched:!!P||def.goalH!=null};
  var el=document.getElementById("pl-form");
  var rv=REV.indexOf(def.revD)<0?REV.concat([def.revD]).sort(function(a,b){return a-b}):REV,qs=QS.indexOf(def.qs)<0?QS.concat([def.qs]).sort(function(a,b){return a-b}):QS;
  el.innerHTML='<section class="bx pl-form" aria-labelledby="h-form"><p class="bx-k" id="h-form">'+(P?'計画を変更':'計画を作る')+'</p><div class="pf">'+
    '<label>資格<select id="f-subj"'+(P?' disabled':'')+'>'+subjs().map(function(s){return '<option value="'+s.id+'"'+(s.id===def.subj?' selected':'')+'>'+esc(s.title)+(used[s.id]&&(!P||P.subj!==s.id)?'(計画あり)':pass[s.id]?'(合格済み)':'')+'</option>'}).join("")+'</select></label>'+
    '<label>受験予定日<input type="date" id="f-exam" min="'+add(T,1)+'" value="'+(def.exam>T?def.exam:add(T,30))+'"></label>'+
    '<div class="lb">受験日の状態<div class="seg2" role="radiogroup" aria-label="受験日の状態"><button type="button" role="radio" data-fx="0" aria-checked="'+(!def.fixed)+'">まだ予定</button><button type="button" role="radio" data-fx="1" aria-checked="'+(!!def.fixed)+'">申込済み(確定)</button></div><span class="hint">試験を申し込んだら「申込済み」に。日が変わったら、あとから変えられます</span></div>'+
    '<label>勉強を始める日(任意)<input type="date" id="f-start" value="'+esc(def.start||"")+'"><span class="hint">空のときは今日から</span></label>'+
    '<details class="pf-more"'+(P?' open':'')+'><summary>くわしい設定</summary><div class="pf">'+
    '<label>合格までに必要な勉強時間(合計)<span class="hint" id="f-goal-h"></span><span><input type="number" id="f-goal" min="1" max="3000" step="5" inputmode="numeric" value="'+(def.goalH!=null?def.goalH:s0.h)+'"> 時間</span></label>'+
    '<label>この記録をつける前に勉強した時間<span class="hint" id="f-base-h">ほかの教材や前回の受験の勉強など。これまでの勉強時間に足します</span><span><input type="number" id="f-base" min="0" max="3000" step="1" inputmode="numeric" value="'+def.baseH+'"> 時間</span></label>'+
    '<label>総復習にあてる期間<span class="hint">本試験の前のこの期間は、問題演習と見直しを中心にします</span><select id="f-rev">'+rv.map(function(v){return '<option value="'+v+'"'+(v===def.revD?' selected':'')+'>'+(v?v+'日':'なし')+'</option>'}).join("")+'</select></label>'+
    '<label>問題演習の割合<span class="hint">毎日の時間のうち、問題を解く時間の割合</span><select id="f-qs">'+qs.map(function(v){return '<option value="'+v+'"'+(v===def.qs?' selected':'')+'>'+v+'%</option>'}).join("")+'</select></label>'+
    '</div></details><div class="pf-info" id="f-info" aria-live="polite"></div>'+
    '<div class="pf-btns"><button type="button" class="bx-go pri" data-act="fsave">'+(P?'変更を保存':'この計画を作る')+'</button><button type="button" class="bx-go" data-act="fcancel">やめる</button>'+(P?'<button type="button" class="bx-go del" data-act="fdel">この計画を削除</button>':'')+'</div></div></section>';
  var b=PG.root.querySelector('[data-act="new"]');if(b)b.hidden=true;
  formInfo();
  setTimeout(function(){try{el.scrollIntoView({block:"start",behavior:"smooth"})}catch(e){}},60)}
function formVal(){var g=function(i){return document.getElementById(i)};if(!g("f-subj"))return null;var f=PG.form;
  var fx=PG.root.querySelector('.seg2 [aria-checked="true"]');
  return {id:f.id==="new"?"":f.id,subj:g("f-subj").value,exam:g("f-exam").value,fixed:!!(fx&&fx.dataset.fx==="1"),start:g("f-start").value,goalH:+g("f-goal").value,baseH:+g("f-base").value,revD:+g("f-rev").value,qs:+g("f-qs").value}}
/* 試しにこの内容で立てたときの、使える時間と必要な時間 */
function formInfo(){var v=formVal(),el=document.getElementById("f-info");if(!v||!el)return;var s=SB(v.subj),T=PG.T,gh=document.getElementById("f-goal-h");
  if(gh)gh.textContent="目安: "+s.h+"時間くらい(人によって違います)";
  if(!okD(v.exam)||v.exam<=T){el.innerHTML='<p class="warn">受験予定日は、明日以降の日を入れてください。</p>';return}
  if(v.start&&okD(v.start)&&v.start>=v.exam){el.innerHTML='<p class="warn">始める日は、受験予定日より前にしてください。</p>';return}
  var E=trial(v),R=compute(E.D,PG.ST,T),x=R.on.filter(function(y){return y.P.id===E.id})[0];if(!x){el.innerHTML='';return}
  var cap=x.A/60,need=x.remainH,days=diff(x.from,v.exam);
  el.innerHTML='<p>試験まで <b>'+diff(T,v.exam)+'日</b>(勉強する日 '+days+'日)・これまでの勉強 '+HR(x.doneH)+'</p><p>必要な残りの時間 <b>'+HR(need)+'</b>・この資格に使える時間 約'+HR(cap)+'</p>'+
    (need>0&&(!isFinite(x.u)||x.u>1.0001)?(PG.D.wk||PG.D.plans.some(function(p){return !p.res})?'<p class="warn">曜日ごとに使える時間では足りません。下の「必要な時間に合わせる」で増やすか、必要な時間を見直してください。</p>':'<p class="ok">作るときに、曜日ごとに使える時間を必要な分に合わせます(あとで変えられます)。</p>'):need<=0?'<p class="ok">必要な時間にもう届いています。総復習の計画になります。</p>':'<p class="ok">いまの使える時間で間に合います(1日あたり約'+K(x.needPerDay)+')。</p>')}
function trial(v){var D=JSON.parse(JSON.stringify(PG.D)),id=v.id||"tmp";D.plans=D.plans.filter(function(p){return p.id!==id});
  var old=PG.D.plans.filter(function(p){return p.id===v.id})[0]||{};
  var p=normP(Object.assign({},old,{id:id,subj:v.subj,exam:v.exam,fixed:v.fixed,start:v.start&&okD(v.start)?v.start:"",goalH:v.goalH,baseH:v.baseH,revD:v.revD,qs:v.qs,res:""}),{});
  D.plans.push(p);return {D:norm(D),id:p.id}}
function closeForm(){PG.form=null;var el=document.getElementById("pl-form");if(el)el.innerHTML='';var b=PG.root.querySelector('[data-act="new"]');if(b)b.hidden=false}
function formSave(){var v=formVal();if(!v)return;var T=PG.T;
  if(!okD(v.exam)||v.exam<=T){formInfo();return}if(v.start&&(!okD(v.start)||v.start>=v.exam)){formInfo();return}
  var D=PG.D,P=D.plans.filter(function(p){return p.id===v.id})[0],isNew=!P;
  if(isNew){P={id:"p"+Date.now().toString(36)+Math.random().toString(36).slice(2,5),subj:v.subj,at:Date.now()};D.plans.push(P)}
  var dateCh=P.exam&&P.exam!==v.exam;
  Object.assign(P,{exam:v.exam,fixed:v.fixed,start:v.start&&okD(v.start)?v.start:"",goalH:Math.round(clamp(v.goalH,1,3000)),baseH:Math.round(clamp(v.baseH,0,3000)),revD:Math.round(clamp(v.revD,0,60)),qs:Math.round(clamp(v.qs,10,90)),res:""});
  D.plans=norm(D).plans;P=D.plans.filter(function(p){return p.subj===v.subj&&p.exam===v.exam&&!p.res})[0]||P;
  /* 作った日(と日を変えた日)のようすを控える: 「予定ではここまで」の起点 */
  if(isNew||dateCh||!P.snap){var R0=compute(D,PG.ST,T),x0=R0.list.filter(function(y){return y.P.id===P.id})[0];
    if(x0)P.snap={d:T,h:Math.round((x0.doneH+x0.todaySec/3600)*100)/100,r:x0.nRead,a:x0.ans}}
  var note='';if(!D.wk&&isNew&&D.plans.filter(function(p){return !p.res}).length===1){D.week=fitWeek(D,PG.ST,T);D.wk=1;note='曜日ごとに使える時間を、必要な時間に合わせて入れました。下の「曜日ごとに使える時間」で変えられます。'}
  closeForm();commit();
  if(note){var m=document.getElementById("pl-main");if(m){var p=document.createElement("p");p.className="pl-note";p.textContent=note;m.prepend(p)}}
  var c=PG.root.querySelector('.pl-card[data-pid="'+P.id+'"]');if(c)setTimeout(function(){try{c.scrollIntoView({block:"center",behavior:"smooth"});c.classList.add("here");setTimeout(function(){c.classList.remove("here")},2000)}catch(e){}},80)}
function setRes(pid,res){var D=PG.D,P=D.plans.filter(function(p){return p.id===pid})[0];if(!P)return;
  if(res==="skip"){openForm(pid);return}
  P.res=res;P.resAt=Date.now();
  if(res==="pass"){var ps=LSj("cs-subj-passed",{});if(!obj(ps))ps={};if(!ps[P.subj]){ps[P.subj]=Date.now();LSs("cs-subj-passed",ps)}}
  commit();
  var el=document.getElementById("pl-ask");if(!el)return;var s=SB(P.subj),n=document.createElement("section");n.className="bx pl-res done pc";n.setAttribute("style",cv(P.subj));
  n.innerHTML=res==="pass"?'<img src="chars/rou-smile.webp" alt="" width="56" height="56"><div><h3 class="bx-t sm">'+esc(s.title)+'、合格おめでとうございます!</h3><p class="bx-s">テキスト一覧に「合格」の印を付けました。庭にも、新しい仲間が来るかもしれません。</p></div>':
    '<img src="chars/rou-normal.webp" alt="" width="56" height="56"><div><h3 class="bx-t sm">おつかれさまでした</h3><p class="bx-s">次の受験日を決めたら、もう一度計画を立てましょう。これまでの記録はそのまま使えます。</p><div class="pf-btns"><button type="button" class="bx-go pri" data-act="again" data-subj="'+P.subj+'" data-goal="'+P.goalH+'">次の受験日で計画を作る</button></div></div>';
  el.prepend(n)}
/* ---- 画面の操作 ---- */
function onClick(e){var t=e.target;if(!t.closest)return;var b=t.closest("[data-act],[data-res],[data-fx]");if(!b)return;
  var card=b.closest("[data-pid]"),pid=card?card.dataset.pid:"",a=b.dataset.act;
  if(b.dataset.res){setRes(pid,b.dataset.res);return}
  if(b.dataset.fx!=null){PG.root.querySelectorAll(".seg2 [data-fx]").forEach(function(x){x.setAttribute("aria-checked",String(x===b))});return}
  if(a==="new"){openForm("new");return}
  if(a==="again"){PG.pre={subj:b.dataset.subj,goalH:+b.dataset.goal||undefined};var s=b.closest(".pl-res");if(s)s.remove();openForm("new");return}
  if(a==="edit"){openForm(pid);return}
  if(a==="weeks"){PG.open[pid]=PG.open[pid]?0:1;drawMain(PG.R);return}
  if(a==="wall"){PG.open[pid]=PG.open[pid]==="all"?1:"all";drawMain(PG.R);return}
  if(a==="fcancel"){closeForm();return}
  if(a==="fsave"){formSave();return}
  if(a==="fdel"){var f=PG.form;if(!f||!confirm("この計画を削除しますか?(学習の記録は消えません)"))return;PG.D.plans=PG.D.plans.filter(function(p){return p.id!==f.id});closeForm();commit();return}
  if(a==="delfin"){PG.D.plans=PG.D.plans.filter(function(p){return p.id!==pid});commit();return}
  if(a==="fit"){PG.D.week=fitWeek(PG.D,PG.ST,PG.T);PG.D.wk=1;commit();return}
  if(a==="wa-go"){weekly(b);return}
  if(a==="ai-go"){consult(b);return}
  if(a==="ai-ex"){var q=document.getElementById("ai-q");if(q){q.value=b.textContent;q.focus()}return}
  if(a==="ai-use"){useAI();return}
  if(a==="ai-no"){var c=PG.root.querySelector(".ai-chg");if(c)c.remove();PG.aiChg=null;return}}
function onChange(e){var t=e.target;
  if(t.dataset&&t.dataset.wd!=null){PG.D.week[+t.dataset.wd]=+t.value;PG.D.wk=1;commit();return}
  if(t.id==="f-subj"){var s=SB(t.value),g=document.getElementById("f-goal");if(g&&!PG.form.goalTouched)g.value=s.h}
  if(t.id==="f-goal")PG.form.goalTouched=true;
  if(t.closest&&t.closest(".pl-form"))formInfo()}
function onInput(e){var t=e.target;if(t.closest&&t.closest(".pl-form")){if(t.id==="f-goal")PG.form.goalTouched=true;formInfo()}}
/* ---- AI(クラウドちゃんに相談・今週のアドバイス) ---- */
var AIERR={not_granted:"AIの利用が許可されていません。",sampling_disabled:"AIの利用が許可されていません。",not_declared:"AIの利用が許可されていません。",rate_limited:"少し時間をおいてから、もう一度どうぞ。",cancelled:"止めました。",invalid_json:"うまく答えを受け取れませんでした。もう一度どうぞ。"};
function aiErr(e){return AIERR[e&&e.code]||"AIにつながりませんでした。もう一度どうぞ。"}
function say(t){return '<div class="ai-say"><img src="chars/rou-smile.webp" alt="" width="40" height="40"><div class="bub">'+esc(t)+'</div></div>'}
function clean(t){return String(t||"").replace(/\*\*|__|`|^#+\s*/gm,"").trim()}
var EXQ=["平日は30分しか取れない","土日はしっかり3時間ずつやりたい","試験日が1週間延びた","このペースで間に合う?","来週は忙しいので少し減らしたい"];
function aiHTML(){if(PG.ai==null)return "";var R=PG.R;
  if(!PG.ai)return '<section class="bx ai-box"><p class="bx-k">クラウドちゃんに相談</p><p class="ai-off">AIのアシストは、この画面では使えません(claude.ai の中で開くと使えます)。</p></section>';
  if(!R||!R.on.length)return "";
  var A=LSj(AIK,{});if(!obj(A))A={};var w=wk(PG.T);
  return '<section class="bx ai-box" aria-labelledby="h-wa"><p class="bx-k" id="h-wa">今週のアドバイス<span>週に1回</span></p>'+(A.wk===w&&A.text?say(A.text)+'<p class="bx-s">'+mdw(A.day||w)+'にもらったアドバイスです。</p>':'<p class="bx-s">先週の勉強と今週の計画を見て、クラウドちゃんがひとことアドバイスします。</p><div class="pf-btns"><button type="button" class="bx-go pri" data-act="wa-go">今週のアドバイスをもらう</button></div><div id="wa-out"></div>')+'</section>'+
   '<section class="bx ai-box" aria-labelledby="h-ai"><p class="bx-k" id="h-ai">クラウドちゃんに相談<span>計画の見直し</span></p><p class="bx-s">「平日は30分しか取れない」などと書くと、計画の数字の案を出します。案を使うかどうかは自分で選べます。</p><div class="ai-ex">'+EXQ.map(function(q){return '<button type="button" data-act="ai-ex">'+esc(q)+'</button>'}).join("")+'</div>'+
   '<textarea id="ai-q" maxlength="400" placeholder="相談したいこと" aria-label="相談したいこと"></textarea><div class="pf-btns"><button type="button" class="bx-go pri" data-act="ai-go">相談する</button></div><div id="ai-out">'+(A.last&&A.last.reply?'<p class="bx-s">前回の相談: '+esc(A.last.q)+'</p>'+say(A.last.reply):'')+'</div></section>'}
var RULE="あなたは IT 系資格(Salesforce 認定資格・情報処理技術者試験など)の受験生の学習計画を手伝う「クラウドちゃん」(やさしい先生)です。試験の中身には触れず、勉強の計画・時間の使い方・続け方だけを、短く、やさしい話し言葉で答えます。Markdown・箇条書きの記号・絵文字は使いません。";
function ctx(){var R=PG.R,D=PG.D,T=PG.T,L=[],a=0;
  L.push("今日: "+T+"("+WD[dow(T)]+")");
  L.push("曜日ごとに使える時間(分・日〜土、すべての計画で共通): "+D.week.join(", "));
  var d7=[];for(var i=1;i<=14;i++){var d=add(T,-i),m=0;R.list.forEach(function(x){if(x.state!=="fin")m+=(x.st.days[d]||0)/60});a+=m;if(i<=7)d7.push(mdw(d)+" "+Math.round(m)+"分")}
  L.push("直近7日の勉強時間: "+d7.join("、")+"/直近14日の合計: "+Math.round(a)+"分");
  R.list.filter(function(x){return x.state==="on"||x.state==="wait"||x.state==="exam"}).forEach(function(x){var P=x.P;
    L.push("計画[id="+P.id+"] "+x.s.title+": 受験日 "+P.exam+"("+(P.fixed?"申込済み":"予定")+"・あと"+x.left+"日)"+(P.start?"・開始日 "+P.start:"")+"/必要な合計時間 "+P.goalH+"時間・これまで "+x.doneH.toFixed(1)+"時間(うち記録より前 "+P.baseH+"時間)・残り "+x.remainH.toFixed(1)+"時間/総復習 "+P.revD+"日・問題演習の割合 "+P.qs+"%/ペース: "+(PACE[x.pace]||[""])[0]+"/節 "+x.nRead+"/"+x.secsN+"・問題 "+x.ans+"/"+x.qn+"(間違えたまま "+x.wrong+")"+(x.today?"/今日の目安 "+Math.round(x.today.m)+"分":"")+(x.lastT?"/先週の目安 "+Math.round(x.lastT)+"分 → 実際 "+Math.round(x.lastA)+"分":""))});
  return L.join("\n")}
async function weekly(b){var out=document.getElementById("wa-out");b.disabled=true;b.textContent="考えています…";
  try{var r=await PG.ai([{role:"user",content:RULE+"\n\n# いまの計画と記録\n"+ctx()+"\n\n# お願い\n先週の勉強ぶりと今週の計画を見て、今週の過ごし方のアドバイスを150字くらいで1つください。できていることを1つほめ、今週いちばん大事なことを1つ伝えてください。答えの文だけを書いてください。"}],{cache:false});
    var t=clean(r&&r.text).slice(0,400);if(!t)throw {code:"invalid_json"};var A=LSj(AIK,{});if(!obj(A))A={};A.wk=wk(PG.T);A.day=PG.T;A.text=t;LSs(AIK,A);drawSide()}
  catch(e){b.disabled=false;b.textContent="今週のアドバイスをもらう";if(out)out.innerHTML='<p class="ai-err">'+esc(aiErr(e))+'</p>'}}
async function consult(b){var q=document.getElementById("ai-q"),out=document.getElementById("ai-out"),t=q?q.value.trim():"";if(!t){q&&q.focus();return}
  b.disabled=true;b.textContent="考えています…";out.innerHTML='<p class="bx-s">クラウドちゃんが考えています…(数十秒かかることがあります)</p>';
  var ids=PG.R.list.filter(function(x){return x.state==="on"||x.state==="wait"||x.state==="exam"}).map(function(x){return x.P.id});
  try{if(!PG.ai.json)throw {code:"invalid_json"};
    var j=await PG.ai.json(RULE+"\n\n# いまの計画と記録\n"+ctx()+"\n\n# 相談\n"+t+"\n\n# 答え方\nJSON だけを返してください。形: {\"reply\": \"相談への答え(200字以内)\", \"change\": 変える設定のオブジェクト または null}\n"+
      "change に入れられる項目(変えるものだけ入れる): week(日曜から土曜まで7つの、使える時間(分・15分きざみ・0〜600)の配列), plans(計画の id をキー、値はその計画で変える項目のオブジェクト。項目は goalH(必要な合計時間・整数), baseH(記録より前に勉強した時間・整数), revD(総復習の日数 0〜60), qs(問題演習の割合% 10〜90), exam(受験日 YYYY-MM-DD・今日より後), start(始める日 YYYY-MM-DD または空文字))\n"+
      "計画の id: "+ids.join(", ")+"\n相談が設定を変える必要のないもの(質問など)なら change は null。reply では、変える案があればその理由も短く伝えてください。",{cache:false});
    var rep=clean(j&&j.reply).slice(0,600)||"(答えが空でした)",chg=aiCheck(j&&j.change);
    var A=LSj(AIK,{});if(!obj(A))A={};A.last={q:t.slice(0,200),reply:rep,at:Date.now()};LSs(AIK,A);
    PG.aiChg=chg;out.innerHTML=say(rep)+(chg?chgHTML(chg):'')}
  catch(e){out.innerHTML='<p class="ai-err">'+esc(aiErr(e))+'</p>'}
  finally{b.disabled=false;b.textContent="相談する"}}
function aiCheck(c){if(!obj(c))return null;var o={},D=PG.D,T=PG.T;
  if(Array.isArray(c.week)&&c.week.length===7&&c.week.every(function(v){return isFinite(+v)&&+v>=0&&+v<=960})){var w=c.week.map(function(v){return Math.round(+v/15)*15});if(w.join()!==D.week.join())o.week=w}
  if(obj(c.plans)){var ps={};Object.keys(c.plans).forEach(function(id){var P=D.plans.filter(function(p){return p.id===id&&!p.res})[0],v=c.plans[id];if(!P||!obj(v))return;var r={};
    if(isFinite(+v.goalH)&&+v.goalH>=1&&+v.goalH<=3000&&Math.round(+v.goalH)!==P.goalH)r.goalH=Math.round(+v.goalH);
    if(isFinite(+v.baseH)&&+v.baseH>=0&&+v.baseH<=3000&&Math.round(+v.baseH)!==P.baseH)r.baseH=Math.round(+v.baseH);
    if(isFinite(+v.revD)&&+v.revD>=0&&+v.revD<=60&&Math.round(+v.revD)!==P.revD)r.revD=Math.round(+v.revD);
    if(isFinite(+v.qs)&&+v.qs>=10&&+v.qs<=90&&Math.round(+v.qs)!==P.qs)r.qs=Math.round(+v.qs);
    if(okD(v.exam)&&v.exam>T&&v.exam!==P.exam)r.exam=v.exam;
    if(typeof v.start==="string"&&(v.start===""||okD(v.start))&&v.start!==P.start&&(!v.start||v.start<(r.exam||P.exam)))r.start=v.start;
    if(Object.keys(r).length)ps[id]=r});if(Object.keys(ps).length)o.plans=ps}
  return Object.keys(o).length?o:null}
function chgHTML(c){var L=[],D=PG.D,f=function(w){return w.map(function(v,i){return WD[i]+K(v)}).join(" ")};
  if(c.week)L.push("曜日ごとの時間: "+f(c.week)+"(いま: "+f(D.week)+")");
  Object.keys(c.plans||{}).forEach(function(id){var P=D.plans.filter(function(p){return p.id===id})[0],v=c.plans[id],n=SB(P.subj).short+" ";
    if("goalH" in v)L.push(n+"必要な時間: "+P.goalH+"時間 → "+v.goalH+"時間");if("baseH" in v)L.push(n+"記録より前の時間: "+P.baseH+"時間 → "+v.baseH+"時間");
    if("revD" in v)L.push(n+"総復習: "+P.revD+"日 → "+v.revD+"日");if("qs" in v)L.push(n+"問題演習の割合: "+P.qs+"% → "+v.qs+"%");
    if("exam" in v)L.push(n+"受験日: "+P.exam+" → "+v.exam);if("start" in v)L.push(n+"始める日: "+(P.start||"今日から")+" → "+(v.start||"今日から"))});
  return '<div class="ai-chg"><b>クラウドちゃんの案</b><ul>'+L.map(function(x){return '<li>'+esc(x)+'</li>'}).join("")+'</ul><div class="pf-btns"><button type="button" class="bx-go pri" data-act="ai-use">この案を使う'+ARR+'</button><button type="button" class="bx-go" data-act="ai-no">使わない</button></div></div>'}
function useAI(){var c=PG.aiChg;if(!c)return;var D=PG.D;if(c.week){D.week=c.week;D.wk=1}
  Object.keys(c.plans||{}).forEach(function(id){var P=D.plans.filter(function(p){return p.id===id})[0];if(P){var dc=c.plans[id].exam&&c.plans[id].exam!==P.exam;Object.assign(P,c.plans[id]);if(dc)P.snap=null}});
  D.plans=norm(D).plans;D.plans.forEach(function(P){if(!P.snap&&!P.res){var R0=compute(D,PG.ST,PG.T),x0=R0.list.filter(function(y){return y.P.id===P.id})[0];if(x0)P.snap={d:PG.T,h:Math.round((x0.doneH+x0.todaySec/3600)*100)/100,r:x0.nRead,a:x0.ans}}});
  PG.aiChg=null;var out=document.getElementById("ai-out");commit();out=document.getElementById("ai-out");if(out)out.insertAdjacentHTML("beforeend",'<p class="ai-ok"><b>案を使いました。</b>計画と設定に反映しています。</p>')}
/* ==== ホームの「今日の計画」 ==== */
function home(){var el=document.getElementById("bx-plan");if(!el)return;var D=load(),live=D.plans.filter(function(p){return !p.res});
  if(!live.length){el.innerHTML='<p class="bx-k">学習計画</p><h3 class="bx-t sm">受験日から、計画を立てませんか</h3><p class="bx-s">資格と受験予定日を入れると、試験の日までの勉強の予定と、毎日の「今日やること」を出します。</p><a class="bx-go" href="/plan/#new">計画を立てる'+ARR+'</a>';el.classList.add("cta");return}
  el.classList.remove("cta");
  if(!el.innerHTML)el.innerHTML='<p class="bx-k">今日の計画</p><p class="bx-s">計画を読み込み中…</p>';
  var ids=[];live.forEach(function(p){if(ids.indexOf(p.subj)<0)ids.push(p.subj)});
  var go=function(ST){if(!document.getElementById("bx-plan"))return;var R=compute(load(),ST);recordTg(R);homeDraw(el,R)};
  loadStats(ids,false).then(go);loadStats(ids,true).then(go)}
function homeDraw(el,R){var T=R.today,h='<p class="bx-k">今日の計画<a href="/plan/">計画を見る</a></p>';
  var ask=R.list.filter(function(x){return x.state==="ask"}),ex=R.list.filter(function(x){return x.state==="exam"});
  ask.forEach(function(x){h+='<p class="hp-ask pc" style="'+cv(x.s.id)+'"><b>'+esc(x.s.short)+'</b> '+md(x.P.exam)+'の試験の結果を教えてください<a href="/plan/">結果を入れる'+ARR+'</a></p>'});
  ex.forEach(function(x){h+='<p class="hp-ask pc" style="'+cv(x.s.id)+'"><b>'+esc(x.s.short)+'</b> 今日は試験の日です。がんばって!</p>'});
  if(R.todo.length){var dn=R.todaySec/60;h+='<h3 class="bx-t">目安 '+K(R.todayMin)+'</h3>'+meter(dn,R.todayMin)+'<p class="bx-s">今日 '+K(dn)+(dn>=R.todayMin?'。今日の目安は達成です!':'(あと '+K(R.todayMin-dn)+')')+'</p><ul class="hp-l">'+R.todo.map(function(x){return todoHTML(x,true)}).join("")+'</ul>'}
  else if(R.on.length&&!ex.length)h+='<h3 class="bx-t sm">'+((+R.week[dow(T)]||0)?'今日の目安は終わっています':'今日はお休みの日です')+'</h3>';
  if(R.on.length)h+='<ul class="hp-pace">'+R.on.map(function(x){return '<li class="pc" style="'+cv(x.s.id)+'"><b>'+esc(x.s.short)+'</b>'+paceChip(x)+'<small>試験まで あと'+x.left+'日</small></li>'}).join("")+'</ul>';
  h+='<a class="bx-go pri" href="/plan/">今日の計画を見る'+ARR+'</a>';el.innerHTML=h}
return {page:page,home:home,compute:compute,load:load,norm:norm,fitWeek:fitWeek,loadStats:loadStats,SUBJ:SUBJ};
})();
FAMP.plan=function(){FAMP.texts();csPlan.page()};
