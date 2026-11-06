"""2台の端末や2つのタブで学習すると、記録が巻き戻ったり消えたりするのを直す。
  原因: 問題集の回答履歴・理解した/しおり・マーカーとメモ・学習の記録(解いた数)・端末の記録(fam-ls)を、
        書類ごと「この画面にある分」で丸ごと上書きしていた。ほかの端末の分が消え、消した記録がほかの端末の古い控えで戻り、
        2台で解いた数は合計ではなく大きい方になっていた。時計のずれた端末の記録がいつまでも勝つこともあった。
  直し方(sync_lib.js = window.CSQ をページの先頭に埋め込む):
    - アカウントへ保存する前に必ず読み直して合わせる(読む→合わせる→保存)
    - 項目ごとに更新時刻を持ち、消した・リセットした印も時刻で残す(ほかの端末の古い控えで復活しない)
    - 時刻は「この端末の時計」と「これまでに見た一番新しい時刻+1」の大きい方
    - 解いた数は端末ごとに持ち、合計を表示する
    - 同じ端末のほかのタブで記録が変わったら(storage イベント)、画面の位置や絞り込みはそのままで中身だけ合わせる
    - 端末の保存容量がいっぱいのときは、テキストと問題の控えを消して保存し直し、それでもだめなら知らせる
  これまでの形式の記録(端末・アカウント)は、そのまま読み込んで新しい形に移す(消さない)。
使い方: python3 patch_sync_merge.py <index.html> <出力>
"""
import os, sys
here = os.path.dirname(os.path.abspath(__file__))
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count: sys.exit(f"置換対象が {n} 件(期待 {count} 件): {old[:90]!r}")
    s = s.replace(old, new)

# 0) ライブラリ(4行目のテーマの script の後ろへ。行の数は変えない)
lib = open(os.path.join(here, "sync_lib.js"), encoding="utf-8").read()
if "</script" in lib or "//" in lib.replace("://", ""): sys.exit("sync_lib.js に </script または // コメントがあります")
lines = s.split("\n")
if not lines[4].startswith("<script>window.FAMD="): sys.exit("5行目が FAMD ではありません")
lines[3] = lines[3] + "<script>" + " ".join(l.strip() for l in lib.split("\n")) + "</script>"
s = "\n".join(lines)

# ===== 1) 問題集の回答履歴(<科目>-quiz / sr-<科目>-quiz-v1) =====
QLIB = r'''
var QSH=null,QF=["hist","hd","hr","answers","at","bm","bt","pa","log","ts"],qBusy=false,qAgain=false;
function bmObj(a){var o={};(a||[]).forEach(function(n){o[n]=1});return o}
function qShadow(){QSH={a:CSQ.clone(S.answers||{}),bm:bmObj(S.bm)}}
function qStamp(){if(!QSH){qShadow();CSQ.reconcile(S,CSQ.dev());return}if(!S.at||typeof S.at!=="object")S.at={};
  Object.keys(S.answers||{}).concat(Object.keys(QSH.a||{})).forEach(function(m){if(!S.at[m])S.at[m]={};CSQ.stamp((S.answers||{})[m],QSH.a[m],S.at[m])});
  if(!S.bt||typeof S.bt!=="object")S.bt={};CSQ.stamp(bmObj(S.bm),QSH.bm,S.bt);CSQ.reconcile(S,CSQ.dev());qShadow()}
function qFresh(r){return fresh(Object.assign({},JSON.parse(JSON.stringify(qdef)),r))}
function qTake(o){var b=CSQ.qBody(S);QF.forEach(function(k){if(o[k]!==undefined)S[k]=o[k]});if(!S.answers.study)S.answers.study={};if(!S.answers.exam)S.answers.exam={};qShadow();return b!==CSQ.qBody(S)}
function qLocal(){try{localStorage.setItem(QK,JSON.stringify(S))}catch(e){}}
function qRedraw(){buildDeck();restorePos();renderAll();try{mountQx()}catch(e){}}
function qRemote(qs){var r=null;try{r=qs.exists&&qs.data().json?JSON.parse(qs.data().json):null}catch(e){}return r&&r.answers?qFresh(r):null}
function qSync(){if(!qcloud)return;if(qBusy){qAgain=true;return}qBusy=true;
  qcloud.get().then(function(qs){var rem=qRemote(qs),ch=false;qStamp();
    if(rem){ch=qTake(CSQ.qMerge(S,S,rem));if(ch)qLocal()}
    if(!rem||CSQ.qBody(rem)!==CSQ.qBody(S)){S.ts=Math.max(+S.ts||0,CSQ.now());qLocal();return qcloud.set({json:JSON.stringify(S),ts:S.ts}).then(function(){return ch})}
    return ch})
  .then(function(ch){syncOk("quiz");if(ch)qRedraw()},function(){syncFail("quiz")})
  .then(function(){qBusy=false;if(qAgain){qAgain=false;qSync()}})}
window.addEventListener("storage",function(e){if(e.key!==QK||!e.newValue)return;var r=null;try{r=JSON.parse(e.newValue)}catch(x){}if(!r||!r.answers)return;r=qFresh(r);
  qStamp();if(qTake(CSQ.qMerge(S,S,r)))qRedraw();if(CSQ.qBody(r)!==CSQ.qBody(S))qLocal()});
'''
rep("S=fresh(S);\n", "S=fresh(S);\n" + QLIB + "qStamp();\n")
rep('function saveQ(){S.ts=Date.now();if(posOK&&deck&&deck.length&&deck[S.pos]!=null)S.curN=deck[S.pos];try{localStorage.setItem(QK,JSON.stringify(S))}catch(e){}\n'
    '  if(qcloud){clearTimeout(saveQ.t);saveQ.t=setTimeout(function(){try{qcloud.set({json:JSON.stringify(S),ts:S.ts}).then(function(){syncOk("quiz")},function(){syncFail("quiz")})}catch(e){syncFail("quiz")}},1500)}}',
    'function saveQ(){S.ts=CSQ.now();if(posOK&&deck&&deck.length&&deck[S.pos]!=null)S.curN=deck[S.pos];qStamp();qLocal();\n'
    '  if(qcloud){clearTimeout(saveQ.t);saveQ.t=setTimeout(qSync,1500)}}')
rep('''  qcloud.get().then(function(qs){var rem=null;try{rem=qs.exists&&qs.data().json?JSON.parse(qs.data().json):null}catch(e){}
    if(!(rem&&rem.answers&&(rem.ts||0)>(S.ts||0)))return;
    S=fresh(Object.assign({},qdef,rem));if(!S.answers.study)S.answers.study={};if(!S.answers.exam)S.answers.exam={};
    try{localStorage.setItem(QK,JSON.stringify(S))}catch(e){}
    takePend(true);buildDeck();restorePos();renderAll();try{mountQx()}catch(e){}}).catch(function(){})}''',
    '''  qSync();if(takePend(true))qRedraw()}''')
# 読み込み: 画面の状態は、アカウントの方が新しければそちら(これまでどおり)。中身は両方を合わせる
rep('''      if(rem&&(rem.ts||0)>(S.ts||0)&&rem.answers){S=fresh(Object.assign({},qdef,rem));if(!S.answers.study)S.answers.study={};if(!S.answers.exam)S.answers.exam={};try{localStorage.setItem(QK,JSON.stringify(S))}catch(e){}buildDeck();restorePos();renderAll()}
      else{qcloud.set({json:JSON.stringify(S),ts:S.ts||Date.now()}).catch(function(){});renderToolbar()}''',
    '''      if(rem&&rem.answers){rem=qFresh(rem);qStamp();
        if((rem.ts||0)>(S.ts||0)){S=CSQ.qMerge(rem,S,rem);if(!S.answers.study)S.answers.study={};if(!S.answers.exam)S.answers.exam={};qShadow();qLocal();buildDeck();restorePos();renderAll()}
        else{if(qTake(CSQ.qMerge(S,S,rem))){qLocal();buildDeck();restorePos();renderAll()}else renderToolbar()}
        if(CSQ.qBody(rem)!==CSQ.qBody(S)){S.ts=Math.max(+S.ts||0,CSQ.now());qLocal();qcloud.set({json:JSON.stringify(S),ts:S.ts}).catch(function(){})}}
      else{qStamp();S.ts=S.ts||CSQ.now();qcloud.set({json:JSON.stringify(S),ts:S.ts}).catch(function(){});renderToolbar()}''')
# リセット: 履歴を消した印(hr)。ほかの端末の、リセットより前の数は数えない
rep('armReset=false;S.answers[S.mode]={};S.hist={};', 'armReset=false;S.answers[S.mode]={};S.hist={};S.hd={};S.hr=CSQ.now();')
rep('h.n++;if(a.correct)h.c++;h.l=a.correct?"o":"x";h.t=Date.now();', 'h.n++;if(a.correct)h.c++;h.l=a.correct?"o":"x";h.t=CSQ.now();')
# 復元: 復元した内容を正にする(それより前のほかの端末の数は数えない)
rep('S=fresh(Object.assign({},JSON.parse(JSON.stringify(qdef)),r.quiz));',
    'S=fresh(Object.assign({},JSON.parse(JSON.stringify(qdef)),r.quiz));S.hr=CSQ.now();S.hd={};S.hd["r"+S.hr]={e:S.hr,q:JSON.parse(JSON.stringify(S.hist||{}))};')

# ===== 2) 理解した・しおり・続きの位置(<科目>-study) =====
rep('return {ts:+s.ts||0,last:(s.last&&s.last.id)?s.last:null,marks:(s.marks&&typeof s.marks==="object")?s.marks:{},done:(s.done&&typeof s.done==="object")?normDone(s.done):{}}}',
    'return {ts:+s.ts||0,last:(s.last&&s.last.id)?s.last:null,marks:(s.marks&&typeof s.marks==="object")?s.marks:{},done:(s.done&&typeof s.done==="object")?normDone(s.done):{},it:{d:(s.it&&s.it.d)||{},m:(s.it&&s.it.m)||{}}}}')
rep('function writeLocal(){try{localStorage.setItem(KEY,JSON.stringify(state))}catch(e){}}',
    'function writeLocal(){stStamp();try{localStorage.setItem(KEY,JSON.stringify(state))}catch(e){}}\n'
    'var STSH=null;function stShadow(){STSH={d:CSQ.clone(state.done||{}),m:CSQ.clone(state.marks||{})}}\n'
    'function stStamp(){if(!state.it)state.it={d:{},m:{}};if(!STSH){stShadow();return}CSQ.stamp(state.done,STSH.d,state.it.d);CSQ.stamp(state.marks,STSH.m,state.it.m);stShadow()}\n'
    'function stMerge(a,b){a=norm(a);b=norm(b);var d=CSQ.mapMerge(a.done,a.it.d,b.done,b.it.d),m=CSQ.mapMerge(a.marks,a.it.m,b.marks,b.it.m),la=a.last,lb=b.last;CSQ.seen(b.ts);\n'
    '  return {ts:Math.max(a.ts,b.ts),last:!la?lb:!lb?la:((+lb.ts||0)>(+la.ts||0)?lb:la),marks:m.v,done:d.v,it:{d:d.t,m:m.t}}}\n'
    'function stBody(x){return JSON.stringify([x.done,x.marks,x.last,x.it])}\n'
    'function stTake(m){var ch=stBody(m)!==stBody(state);if(ch){state=m;stShadow();try{localStorage.setItem(KEY,JSON.stringify(state))}catch(e){}}return ch}\n'
    'window.addEventListener("storage",function(e){if(e.key!==KEY||!e.newValue)return;var r;try{r=JSON.parse(e.newValue)}catch(x){return}if(!r||typeof r!=="object")return;stStamp();if(stTake(stMerge(state,r)))render()});')
rep('function touch(){state.ts=Date.now();writeLocal()}', 'function touch(){state.ts=CSQ.now();writeLocal()}')
rep('  try{await doc.set(JSON.parse(JSON.stringify(state)));setStore(true)}catch(e){setStore(false)}',
    '  try{stStamp();var sg=await doc.get(),rm=sg.exists?norm(sg.data()):null;if(rm&&stTake(stMerge(state,rm)))render();\n'
    '    if(!rm||stBody(rm)!==stBody(state))await doc.set(JSON.parse(JSON.stringify(state)));setStore(true)}catch(e){setStore(false)}')
rep('''    if(s.exists){var rm=norm(s.data());
      if(rm.ts>state.ts){state=rm;writeLocal();render();lastKey="";again()}
      else if(state.ts>rm.ts)scheduleSave(0);
    }else if(state.ts)scheduleSave(0);''',
    '''    if(s.exists){var rm=norm(s.data());stStamp();var nw=rm.ts>state.ts;
      if(stTake(stMerge(state,rm))||nw){render();if(nw){lastKey="";again()}}
      if(stBody(rm)!==stBody(state))scheduleSave(0);
    }else if(state.ts)scheduleSave(0);''')
rep('var local=readLocal();if(local)state=norm(local);', 'var local=readLocal();if(local)state=norm(local);stShadow();')

# ===== 3) マーカーとメモ(<科目>-notes) =====
rep('memo:(s.memo&&typeof s.memo==="object")?s.memo:{}}}',
    'memo:(s.memo&&typeof s.memo==="object")?s.memo:{},it:{hl:(s.it&&s.it.hl)||{},memo:(s.it&&s.it.memo)||{}}}}')
rep('try{notes=nNorm(JSON.parse(localStorage.getItem(NK)))}catch(e){}',
    'try{notes=nNorm(JSON.parse(localStorage.getItem(NK)))}catch(e){}\n'
    'var NSH=null;function nShadow(){NSH={hl:CSQ.clone(notes.hl||{}),memo:CSQ.clone(notes.memo||{})}}nShadow();\n'
    'function nStamp(){if(!notes.it)notes.it={hl:{},memo:{}};CSQ.stamp(notes.hl,NSH.hl,notes.it.hl);CSQ.stamp(notes.memo,NSH.memo,notes.it.memo);nShadow()}\n'
    'function nMerge(a,b){a=nNorm(CSQ.clone(a));b=nNorm(CSQ.clone(b));var h=CSQ.mapMerge(a.hl,a.it.hl,b.hl,b.it.hl),m=CSQ.mapMerge(a.memo,a.it.memo,b.memo,b.it.memo);CSQ.seen(b.ts);return {ts:Math.max(a.ts,b.ts),hl:h.v,memo:m.v,it:{hl:h.t,memo:m.t}}}\n'
    'function nBody(x){return JSON.stringify([x.hl,x.memo,x.it])}\n'
    'function nTake(m){var ch=nBody(m)!==nBody(notes);if(ch){notes=m;nShadow();try{localStorage.setItem(NK,JSON.stringify(notes))}catch(e){}applyHL();refreshMemos();updNoteBadge()}return ch}\n'
    'window.addEventListener("storage",function(e){if(e.key!==NK||!e.newValue)return;var r;try{r=JSON.parse(e.newValue)}catch(x){return}if(!r||typeof r!=="object")return;nStamp();nTake(nMerge(notes,r))});')
rep('function nPush(){clearTimeout(nSaveT);if(!ndoc||!nDirty)return;nDirty=false;try{ndoc.set(JSON.parse(JSON.stringify(notes))).then(function(){setNoteStore(true)},function(){nDirty=true;setNoteStore(false)})}catch(e){setNoteStore(false)}}',
    'function nPush(){clearTimeout(nSaveT);if(!ndoc||!nDirty)return;nDirty=false;nStamp();try{ndoc.get().then(function(sg){var rm=sg.exists?nNorm(sg.data()):null;if(rm)nTake(nMerge(notes,rm));\n'
    '  if(!rm||nBody(rm)!==nBody(notes))return ndoc.set(JSON.parse(JSON.stringify(notes)))}).then(function(){setNoteStore(true)},function(){nDirty=true;setNoteStore(false)})}catch(e){setNoteStore(false)}}')
rep('  notes.ts=Date.now();try{localStorage.setItem(NK,JSON.stringify(notes))}catch(e){}',
    '  notes.ts=CSQ.now();nStamp();try{localStorage.setItem(NK,JSON.stringify(notes))}catch(e){}')
rep('''    if(s.exists){var rm=nNorm(s.data());
      if(rm.ts>notes.ts){notes=rm;try{localStorage.setItem(NK,JSON.stringify(notes))}catch(e){}applyHL();refreshMemos()}
      else if(notes.ts>rm.ts)nd.set(JSON.parse(JSON.stringify(notes))).catch(function(){});
    }else if(notes.ts)nd.set(JSON.parse(JSON.stringify(notes))).catch(function(){});''',
    '''    if(s.exists){var rm=nNorm(s.data());nStamp();nTake(nMerge(notes,rm));
      if(nBody(rm)!==nBody(notes))nd.set(JSON.parse(JSON.stringify(notes))).catch(function(){});
    }else if(notes.ts)nd.set(JSON.parse(JSON.stringify(notes))).catch(function(){});''')

# ===== 4) AIの練習問題で間違えた問題(<科目>-aiwrong): 「すべて消す」の印(clr) =====
rep('function mergeAi(a,b){var seen={},m=[];(a||[]).concat(b||[]).forEach(function(w){if(w&&w.q&&!seen[w.q]){seen[w.q]=1;m.push(w)}});return m.slice(-200)}',
    'function aiClr(){try{return +localStorage.getItem(AK+"-clr")||0}catch(e){return 0}}\n'
    'function aiSeeClr(c){c=+c||0;if(c>aiClr()){try{localStorage.setItem(AK+"-clr",String(c))}catch(e){}}CSQ.seen(c)}\n'
    'function mergeAi(a,b){var c=aiClr(),seen={},m=[];(a||[]).concat(b||[]).forEach(function(w){if(w&&w.q&&!seen[w.q]&&!(c&&(+w.t||0)<=c)){seen[w.q]=1;m.push(w)}});return m.slice(-200)}')
rep('function saveW(a){a=a.slice(-200);try{localStorage.setItem(AK,JSON.stringify(a))}catch(e){}if(aiDoc){try{aiDoc.set({list:a,ts:Date.now()}).catch(function(){})}catch(e){}}}',
    'function saveW(a){a=mergeAi([],a);try{localStorage.setItem(AK,JSON.stringify(a))}catch(e){}if(aiDoc){try{aiDoc.get().then(function(sg){var d=(sg.exists&&sg.data())||{};aiSeeClr(d.clr);\n'
    '  var m=mergeAi(Array.isArray(d.list)?d.list:[],loadW());try{localStorage.setItem(AK,JSON.stringify(m))}catch(e){}\n'
    '  if(JSON.stringify(m)!==JSON.stringify(d.list||null)||(+d.clr||0)!==aiClr())return aiDoc.set({list:m,ts:CSQ.now(),clr:aiClr()})}).then(function(){renderW()}).catch(function(){})}catch(e){}}}')
rep('''  var d=cdoc("aiwrong"),s=await d.get(),rem=(s.exists&&s.data()&&Array.isArray(s.data().list))?s.data().list:[];
  var m=mergeAi(rem,loadW());
  try{localStorage.setItem(AK,JSON.stringify(m))}catch(e){}
  if(m.length!==rem.length)await d.set({list:m,ts:Date.now()});''',
    '''  var d=cdoc("aiwrong"),s=await d.get(),rem=(s.exists&&s.data()&&Array.isArray(s.data().list))?s.data().list:[];aiSeeClr(s.exists&&s.data()&&s.data().clr);
  var m=mergeAi(rem,loadW());
  try{localStorage.setItem(AK,JSON.stringify(m))}catch(e){}
  if(JSON.stringify(m)!==JSON.stringify(rem)||(+(s.exists&&s.data()&&s.data().clr)||0)!==aiClr())await d.set({list:m,ts:CSQ.now(),clr:aiClr()});''')
rep('w.push({q:q,a:LETM.charAt(ai)+". "+opts[ai],e:ex});', 'w.push({q:q,a:LETM.charAt(ai)+". "+opts[ai],e:ex,t:CSQ.now()});')
rep('w.push({q:q,a:ansv,e:ex});', 'w.push({q:q,a:ansv,e:ex,t:CSQ.now()});')
rep('$("#w-clear").onclick=function(){saveW([]);renderW()};',
    '$("#w-clear").onclick=function(){try{localStorage.setItem(AK+"-clr",String(CSQ.now()))}catch(e){}saveW([]);renderW()};')

# ===== 5) 学習の記録(<科目>-act / sr-<科目>-act-v1): 端末ごとの数の合計 =====
i = s.find("function N(e){let n=`sr-`+e+`-act-v1`")
j = s.find("async function P(e){", i)
if i < 0 or j < 0 or s.count("function N(e){let n=`sr-`+e+`-act-v1`") != 1: sys.exit("N() が見つかりません")
s = s[:i] + ("function N(e){let n=`sr-`+e+`-act-v1`,r={ts:0,d:{}};const rd=()=>{try{let x=JSON.parse(localStorage.getItem(n));return x&&x.d?x:null}catch{return null}};{let x=rd();x&&(r=x)}"
    "let i=e=>(e<10?`0`:``)+e,a=()=>{let e=new Date;return e.getFullYear()+`-`+i(e.getMonth()+1)+`-`+i(e.getDate())},o=null,s=null,B=!1,A=!1,"
    "w=()=>{try{localStorage.setItem(n,JSON.stringify(r))}catch{}},"
    "c=async()=>{clearTimeout(s),s=null;if(!o)return;if(B){A=!0;return}B=!0;try{let g=await o.get(),t=g.exists?g.data():null;r=CSQ.actMerge(CSQ.actMerge(r,rd()),t);w();"
    "(!t||CSQ.actDays(t)!==CSQ.actDays(r))&&await o.set(JSON.parse(JSON.stringify(r)))}catch{}B=!1;A&&(A=!1,c())},"
    "l=e=>{w();o&&(e?(clearTimeout(s),s=setTimeout(c,3e3)):s||=setTimeout(c,3e5))};"
    "return t().then(async({db:t,uid:i})=>{t&&(o=t.doc(`data/users/`+i+`/`+e+`-act`),await c())}),"
    "document.addEventListener(`visibilitychange`,()=>{document.visibilityState===`hidden`&&s&&c()}),"
    "addEventListener(`storage`,e=>{e.key===n&&(r=CSQ.actMerge(r,rd()))}),"
    "{add(e,t){r=CSQ.actMerge(r,rd());let d=a();if(e===`r`){let x=CSQ.dayNorm(r.d[d]||(r.d[d]={q:0,c:0,r:[],v:{}}));if(x.r.indexOf(t)>=0)return;x.r.length<80&&x.r.push(t),r.ts=CSQ.now(),l(!0)}"
    "else e===`t`?(CSQ.actBump(r,d,`t`,t),l(!1)):(CSQ.actBump(r,d,e,1),l(!0))}}}") + s[j:]

# ===== 6) トレーニング(/practice/) =====
rep('  var key=q.subj+":q"+q.n,now=Date.now();', '  var key=q.subj+":q"+q.n,now=CSQ.now();')
rep('var dd=act.d[today()]||(act.d[today()]={q:0,c:0,r:[],t:0});var ca=CLOUD_ACT[q.subj];if(ca){dd.q=Math.max(+dd.q||0,+ca.q||0);dd.c=Math.max(+dd.c||0,+ca.c||0);dd.t=Math.max(+dd.t||0,+ca.t||0)}dd.q=(+dd.q||0)+1;if(ok)dd.c=(+dd.c||0)+1;dd.t=(+dd.t||0)+sec;act.ts=now;LS.set(ak,act);',
    'CSQ.actBump(act,today(),"q",1);if(ok)CSQ.actBump(act,today(),"c",1);CSQ.actBump(act,today(),"t",sec);LS.set(ak,act);')
rep('if(t>=(+h.t||0)){h.l=ok?"o":"x";h.t=t}st.ts=Math.max(Date.now(),(+st.ts||0)+1);return true}',
    'if(t>=(+h.t||0)){h.l=ok?"o":"x";h.t=t}CSQ.reconcile(st,CSQ.dev());st.ts=Math.max(CSQ.now(),(+st.ts||0)+1);return true}')
rep('''  try{var cl=await cloud;if(!cl)return;var d=cdoc(cl,id+"-act"),s=await d.get(),rem=s.exists?s.data():{d:{}},loc=LS.get("sr-"+id+"-act-v1",{d:{}}),out={d:{},ts:Date.now()};
    [rem.d||{},loc.d||{}].forEach(function(src){Object.keys(src).forEach(function(k){var a=src[k]||{},b=out.d[k]||(out.d[k]={q:0,c:0,t:0,r:[]});["q","c","t"].forEach(function(f){b[f]=Math.max(+b[f]||0,+a[f]||0)});(a.r||[]).forEach(function(x){if(b.r.indexOf(x)<0)b.r.push(x)})})});
    await d.set(out)}catch(e){}''',
    '''  try{var cl=await cloud;if(!cl)return;var d=cdoc(cl,id+"-act"),s=await d.get(),rem=s.exists?s.data():null,out=CSQ.actMerge(LS.get("sr-"+id+"-act-v1",{d:{}}),rem);
    LS.set("sr-"+id+"-act-v1",out);if(!rem||CSQ.actDays(rem)!==CSQ.actDays(out))await d.set(JSON.parse(JSON.stringify(out)))}catch(e){}''')
# 用語カード: ほかのタブ・同期で変わった分を消さないよう、押すたびに読み直す
rep('if(k.dataset.k==="known")KNOWN[tkey(c)]=Date.now();', 'KNOWN=LS.get(TKN,{});if(k.dataset.k==="known")KNOWN[tkey(c)]=Date.now();')
rep('function bindTerms(){', 'window.addEventListener("storage",function(e){if(e.key===TKN)KNOWN=LS.get(TKN,{})});\nfunction bindTerms(){')

# ===== 7) 端末の記録(fam-ls): 項目ごとに合わせる =====
rep('Storage.prototype.setItem=function(t,n){let r=e.apply(this,arguments);try{!q&&this===window.localStorage&&Q.forEach(e=>e(t,String(n)))}catch{}return r}',
    'Storage.prototype.setItem=function(t,n){let o=null;try{!q&&this===window.localStorage&&W.includes(t)&&(o=this.getItem(t))}catch{}let r=e.apply(this,arguments);try{!q&&this===window.localStorage&&Q.forEach(e=>e(t,String(n),o))}catch{}return r}')
i = s.find("function re(){let e=null,t=null,P=!1,M={},")
j = s.find("return Promise.race([r,new Promise(e=>setTimeout(e,2500))])}", i)
if i < 0 or j < 0: sys.exit("re() が見つかりません")
j += len("return Promise.race([r,new Promise(e=>setTimeout(e,2500))])}")
s = s[:i] + ("function re(){let e=null,t=null,P=!1,B=!1,A=!1,io={get:J,set:Y,ts:X,setTs:o=>Y(G,JSON.stringify(o))},"
    "y=async()=>{if(B){A=!0;return}B=!0;try{let r=await e.get(),k=r&&r.exists&&r.data().keys||{},m=CSQ.famMerge(W,k,io);m.changed&&await e.set({keys:m.keys,ts:CSQ.now()})}catch{}B=!1;A&&(A=!1,n())},"
    "n=()=>{if(!e){P=!0;return}clearTimeout(t),t=setTimeout(y,1500)};"
    "Q.push((k,v,o)=>{if(W.includes(k)){let t=X();t[k]=CSQ.now(),Y(G,JSON.stringify(t)),CSQ.famStamp(k,o,v,Y),n()}});"
    "let r=(async()=>{try{let t=await Z();if(!t)return;let D=t.db.doc(`data/users/`+t.id+`/fam-ls`);let r=await D.get(),k=r&&r.exists&&r.data().keys||{},m=CSQ.famMerge(W,k,io);e=D;(m.changed||P)&&await D.set({keys:m.keys,ts:CSQ.now()})}catch{}})().finally(()=>{window.__famLsReady=1});"
    "return Promise.race([r,new Promise(e=>setTimeout(e,2500))])}") + s[j:]

open(out, "w", encoding="utf-8").write(s); print("ok")
