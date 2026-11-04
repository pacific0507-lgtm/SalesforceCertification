"""問題集(各科目の問題の画面)に「問題 / 用語カード」の切り替えを付け、用語カードもここで使えるようにする。
  - 切り替えは問題の画面の一番上・中央。状態は科目ごとに保存(cs-tc-<科目>)
  - 用語カードにすると、メニューの「絞込」は用語カード用(Chapter・項目・状態・ランダム)に、
    「問題一覧」(スマホはメニュー、PC は左の一覧)は用語カードの一覧に切り替わる
  - カードは押すと裏返る。「まだ」「覚えた」、前へ・次へ、「テキストの該当箇所で確認する」(本文でその語句が出てくる箇所へ。見つからなければ項目の先頭へ)
  - 覚えたかどうかは、トレーニングの用語カードと同じ cs-term-known-v1(アカウントに同期)
使い方: python3 patch_qv_terms.py <index.html> <出力>
"""
import sys
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count: sys.exit(f"置換対象が {n} 件(期待 {count} 件): {old[:90]!r}")
    s = s.replace(old, new)

JS = r'''/* ==問題集の中の用語カード(問題 / 用語カードの切り替え)== */
var TC={on:false,cat:"all",feat:"all",st:"all",rnd:false,i:0},TCK="cs-term-known-v1",TCL=[],TCALL=null,TCFLIP=false,TCID=(window.FAMV&&FAMV.id)||GO_CUR;
function tcLS(k,d){try{var v=JSON.parse(localStorage.getItem(k));return v==null?d:v}catch(e){return d}}
function tcSave(){try{localStorage.setItem("cs-tc-"+TCID,JSON.stringify(TC))}catch(e){}}
function tcKey(c){return TCID+":"+c.s+":"+c.t}
function tcKnown(){return tcLS(TCK,{})}
function tcSecOrd(sec){var no=String(dk(sec)).split("·").pop(),m=/(\d+)/.exec(no);return (+chOfS(sec)||0)*1000+(m?+m[1]:999)}
function tcLoad(){if(TCALL)return TCALL;var u=window.famURL?famURL("data/"+TCID+"/terms.json"):"data/"+TCID+"/terms.json";
  TCALL=fetch(u).then(function(r){return r.ok?r.json():[]}).catch(function(){return []}).then(function(rows){
    var list=(rows||[]).map(function(r,i){return {s:r.s,t:r.t,d:r.d,i:i}});
    list.sort(function(a,b){return (tcSecOrd(a.s)-tcSecOrd(b.s))||(a.i-b.i)});list.forEach(function(c,i){c.n=i+1});return list});return TCALL}
function tcBase(all){return all.filter(function(c){return (TC.cat==="all"||String(chOfS(c.s))===String(TC.cat))&&(TC.feat==="all"||c.s===TC.feat)})}
function tcPass(c,K){return TC.st==="all"||(TC.st==="todo"?!K[tcKey(c)]:!!K[tcKey(c)])}
function tcBuild(keep){return tcLoad().then(function(all){var K=tcKnown(),cur=TCL[TC.i];TCL=tcBase(all).filter(function(c){return tcPass(c,K)});
  if(TC.rnd){for(var i=TCL.length-1;i>0;i--){var j=Math.floor(Math.random()*(i+1)),t=TCL[i];TCL[i]=TCL[j];TCL[j]=t}}
  if(keep&&cur){var k=TCL.indexOf(cur);if(k>=0)TC.i=k}if(TC.i>=TCL.length)TC.i=0;return all})}
function tcSet(on){if(!!on===TC.on&&document.body.classList.contains("tc-on")===!!on)return;TC.on=!!on;tcSave();document.body.classList.toggle("tc-on",TC.on);tcTabs();
  var sh=$("#qside .toc-h span"),so=byId("qside-open"),nt=$("#qside .qside-note");if(sh)sh.textContent=TC.on?"用語カード一覧":"問題一覧";if(so)so.textContent=TC.on?"用語カード一覧を開く":"問題一覧を開く";if(nt)nt.textContent=TC.on?"番号でそのカードへ・項目名でその項目だけにする":"番号でジャンプ・項目名でその項目だけを解く";
  var lt=$("#p-list .mp-top span");if(lt)lt.textContent=TC.on?"用語カード一覧":"問題一覧";var lh=$("#p-list .mp-h");if(lh)lh.textContent=TC.on?"番号を押すとそのカードへ・項目名を押すとその項目だけにする":"番号を押すとジャンプ・項目名を押すとその項目だけで解く";
  if(TC.on)tcBuild(true).then(tcRender)}
function tcTabs(){var t=byId("tcTabs");if(!t)return;tcLoad().then(function(all){t.innerHTML='<button type="button" role="tab" data-tc-tab="q" aria-selected="'+!TC.on+'">問題<small>'+(Q.length||"")+'問</small></button><button type="button" role="tab" data-tc-tab="c" aria-selected="'+TC.on+'">用語カード<small>'+all.length+'枚</small></button>';t.hidden=!all.length})}
function tcRender(){if(!TC.on)return;tcLoad().then(function(all){var K=tcKnown(),base=tcBase(all),known=base.filter(function(c){return K[tcKey(c)]}).length;
  /* 絞り込み */
  var sc=byId("tcCat"),sf=byId("tcFeat"),ss=byId("tcSt"),cr=byId("tcRnd");
  if(sc){var chs={};all.forEach(function(c){var k=String(chOfS(c.s));chs[k]=(chs[k]||0)+1});
    sc.innerHTML='<option value="all">Chapter: すべて('+all.length+'枚)</option>'+Object.keys(chs).sort(function(a,b){return a-b}).map(function(k){return '<option value="'+k+'">Chapter '+k+' '+esc(CHT[k]||"")+'('+chs[k]+'枚)</option>'}).join("");sc.value=TC.cat;
    var fs={},fo=[];all.forEach(function(c){if(TC.cat!=="all"&&String(chOfS(c.s))!==String(TC.cat))return;if(!fs[c.s]){fs[c.s]=0;fo.push(c.s)}fs[c.s]++});
    sf.innerHTML='<option value="all">項目: すべて</option>'+fo.map(function(k){return '<option value="'+esc(k)+'">'+esc(dk(k))+' '+esc(TITLES[k]||"")+'('+fs[k]+'枚)</option>'}).join("");if(TC.feat!=="all"&&!fs[TC.feat])TC.feat="all";sf.value=TC.feat;
    var L={all:"すべて",todo:"まだ覚えていない",known:"覚えた"};[].slice.call(ss.options).forEach(function(o){o.textContent="状態: "+L[o.value]+"("+base.filter(function(c){var m=!!K[tcKey(c)];return o.value==="all"||(o.value==="todo"?!m:m)}).length+"枚)"});ss.value=TC.st;cr.checked=TC.rnd}
  /* まとめ */
  var parts=[TC.cat==="all"?"全Chapter":"Chapter "+TC.cat+" "+(CHT[TC.cat]||"")];if(TC.feat!=="all")parts.push(dk(TC.feat)+" "+(TITLES[TC.feat]||""));if(TC.st!=="all")parts.push(TC.st==="todo"?"まだ覚えていない":"覚えた");if(TC.rnd)parts.push("ランダム");
  var sm=byId("tcSum");if(sm)sm.innerHTML='<span>'+esc(parts.join(" / "))+'</span><span class="tc-kn">覚えた '+known+' / '+base.length+'枚</span>';
  /* カード */
  var cd=byId("tcCard"),pos=byId("tcPos");TCFLIP=false;if(cd.classList.contains("on")){cd.style.transition="none";cd.classList.remove("on");void cd.offsetWidth;cd.style.transition=""}
  if(!TCL.length){cd.innerHTML='<div class="tc-f"><p class="tc-empty">'+(TC.st==="todo"&&base.length?"この範囲のカードは、すべて「覚えた」になっています。":"この絞り込みのカードはありません。")+'</p></div>';pos.textContent="";byId("tcGo").hidden=true;byId("tcAct").hidden=true}
  else{var c=TCL[TC.i],m=!!K[tcKey(c)];
    cd.innerHTML='<div class="tc-f"><p class="tc-sec"><b>'+esc(dk(c.s))+'</b>'+esc(TITLES[c.s]||"")+(m?'<span class="tc-ok">覚えた</span>':"")+'</p><h3>'+esc(c.t)+'</h3><p class="tc-hint">押すと説明が出ます</p></div><div class="tc-b"><p class="tc-t">'+esc(c.t)+'</p><p class="tc-d">'+esc(c.d)+'</p></div>';
    pos.textContent=(TC.i+1)+" / "+TCL.length;byId("tcGo").hidden=false;byId("tcAct").hidden=false;
    var kb=$('#tcAct [data-k="known"]');if(kb)kb.setAttribute("aria-pressed",String(m))}
  tcGrid(all,K)})}
function tcGrid(all,K){var cur=TCL[TC.i],inL={};TCL.forEach(function(c){inL[c.n]=1});var h="",ch=null,groups=[],g=null;
  all.forEach(function(c){if(!g||g.s!==c.s){g={s:c.s,cs:[]};groups.push(g)}g.cs.push(c)});
  groups.forEach(function(g){var k=String(chOfS(g.s));if(k!==ch){ch=k;var n=all.filter(function(c){return String(chOfS(c.s))===k}).length;h+='<div class="gl-ch"><span>Chapter '+k+' '+esc(CHT[k]||"")+'</span><small>'+n+'枚</small></div>'}
    var kn=g.cs.filter(function(c){return K[tcKey(c)]}).length,here=cur&&cur.s===g.s,no=String(dk(g.s)).split("·").pop();
    h+='<div class="gl-it'+(here?" here":"")+'"><button type="button" class="gl-h" data-tc-feat="'+esc(g.s)+'" title="この項目だけにする"><span class="gl-t"><i>'+esc(no)+'</i>'+esc(TITLES[g.s]||"")+(here?'<span class="hb">いまここ</span>':"")+'</span><span class="gl-n"><b>'+g.cs.length+'</b>枚 ・ 覚えた <b>'+kn+'</b></span></button>'+
      '<div class="gl-bar" aria-hidden="true"><i style="width:'+(kn/g.cs.length*100)+'%"></i></div><div class="cells">'+g.cs.map(function(c){return '<button type="button" class="cell'+(K[tcKey(c)]?" ok":"")+(cur===c?" cur":"")+(inL[c.n]?"":" dim")+'" data-tc-n="'+c.n+'" title="'+esc(c.t)+'">'+c.n+'</button>'}).join("")+'</div></div>'});
  ["tcCells","tcCells2"].forEach(function(id){var e=byId(id);if(e)e.innerHTML=h})}
function tcMove(d){if(!TCL.length)return;TC.i=(TC.i+d+TCL.length)%TCL.length;tcSave();tcRender()}
function tcFlip(){if(!TCL.length)return;TCFLIP=!TCFLIP;byId("tcCard").classList.toggle("on",TCFLIP)}
function tcMark(known){var c=TCL[TC.i];if(!c)return;var K=tcKnown();if(known)K[tcKey(c)]=Date.now();else delete K[tcKey(c)];try{localStorage.setItem(TCK,JSON.stringify(K))}catch(e){}
  if(TC.st!=="all"){tcBuild(false).then(tcRender)}else tcMove(1)}
/* 用語の語句がある箇所(本文の段落・箇条書き・表)を探す。見つからなければ null(呼び出し側で項目へ) */
function tcCands(t){var out=[],add=function(x){x=String(x||"").trim();if(x.length>=2&&out.indexOf(x)<0)out.push(x)};add(t);
  var m=/^(.*?)[(（]([^()（）]+)[)）]\s*$/.exec(t);if(m){add(m[1]);m[2].split(/[、,・/]|旧称?\s*|→/).forEach(add)}
  t.split(/\s*(?:と|・|\/|／|、)\s*/).forEach(function(x){add(x.replace(/[(（].*$/,""))});
  out.sort(function(a,b){return b.length-a.length});
  /* 見つからないときの予備: 「の」などで区切った語(長い順) */
  var sub=[];t.replace(/[「」『』]/g,"").replace(/[(（][^()（）]*[)）]/g," ").split(/の|を|が|と|・|\s+/).forEach(function(x){x=x.trim();if(x.length>=3&&out.indexOf(x)<0&&sub.indexOf(x)<0)sub.push(x)});
  return out.concat(sub.sort(function(a,b){return b.length-a.length}))}
function tcTermRange(sec,t){var root=byId("f-"+sec);if(!root)return null;var cs=tcCands(t);
  var nodes=[],w=document.createTreeWalker(root,NodeFilter.SHOW_TEXT,{acceptNode:function(n){var p=n.parentElement;if(!p||!n.nodeValue.trim())return NodeFilter.FILTER_REJECT;if(p.closest("figure,svg,button,.qx-b,.done-row,h3,script,style"))return NodeFilter.FILTER_REJECT;return NodeFilter.FILTER_ACCEPT}});
  while(w.nextNode())nodes.push(w.currentNode);
  for(var i=0;i<cs.length;i++){var c=cs[i],lc=c.toLowerCase();
    /* 会話(たとえ話)より本文を優先 */
    for(var pass=0;pass<2;pass++)for(var j=0;j<nodes.length;j++){var n=nodes[j],inTalk=!!n.parentElement.closest(".co.talk");if(pass===0&&inTalk||pass===1&&!inTalk)continue;
      var k=n.nodeValue.toLowerCase().indexOf(lc);if(k>=0){var r=document.createRange();r.setStart(n,k);r.setEnd(n,k+c.length);return r}}}
  return null}
function tcShowTerm(c){var r=tcTermRange(c.s,c.t);if(!r)return false;hold(1200);
  var b=r.getBoundingClientRect(),top=window.scrollY+b.top-Math.max(90,window.innerHeight*0.3);window.scrollTo(0,Math.max(0,top));
  try{if(window.CSS&&CSS.highlights&&window.Highlight){CSS.highlights.set("qx",new Highlight(r));clearTimeout(qxT);qxT=setTimeout(function(){CSS.highlights.delete("qx")},4500)}}catch(e){}
  var bl=qxBlock(r);if(bl){bl.classList.remove("qx-flash");void bl.offsetWidth;bl.classList.add("qx-flash");setTimeout(function(){bl.classList.remove("qx-flash")},2700)}
  return true}
function tcInit(){var qi=byId("qv-in");if(!qi||byId("tcTabs"))return;try{var sv=tcLS("cs-tc-"+TCID,null);if(sv)for(var k in TC)if(k in sv)TC[k]=sv[k]}catch(e){}
  var st=document.createElement("style");st.textContent=TCCSS;document.head.appendChild(st);
  var tb=document.createElement("div");tb.className="fmt-tabs tc-tabs";tb.id="tcTabs";tb.setAttribute("role","tablist");tb.setAttribute("aria-label","問題と用語カードの切り替え");tb.hidden=true;qi.insertBefore(tb,qi.firstChild);
  var v=document.createElement("div");v.id="tcv";v.innerHTML='<div class="tc-sum" id="tcSum"></div><div class="tc-card" id="tcCard" role="button" tabindex="0" aria-label="カード(押すと裏返る)"></div>'+
    '<div class="tc-act" id="tcAct"><button type="button" class="tc-nv" id="tcPrev">‹ 前へ</button><span class="tc-mid"><button type="button" data-k="again">まだ</button><button type="button" data-k="known">覚えた</button></span><button type="button" class="tc-nv" id="tcNext">次へ ›</button></div>'+
    '<p class="tc-pos" id="tcPos"></p><p class="tc-links"><button type="button" class="tc-go" id="tcGo">テキストの該当箇所で確認する</button></p><p class="hint">キー操作: スペース・Enter で裏返す、← → で前へ・次へ、K で覚えた</p>';
  tb.after(v);
  var ps=byId("p-set");ps=ps&&(ps.querySelector(".mp-scroll")||ps);if(ps){var hs=[].slice.call(ps.children),cut=hs.findIndex(function(e){return e.classList.contains("mp-h")&&e.textContent==="保存"});hs.slice(0,cut<0?hs.length:cut).forEach(function(e){e.classList.add("q-flt")});
    var w=document.createElement("div");w.id="tcSet";w.innerHTML='<div class="mp-h">用語カードの絞り込み</div><div class="fl"><select id="tcCat" aria-label="Chapter"></select><select id="tcFeat" aria-label="テキストの項目"></select><select id="tcSt" aria-label="状態"><option value="all"></option><option value="todo"></option><option value="known"></option></select><label class="chk"><input type="checkbox" id="tcRnd">ランダムに出す</label></div>';
    ps.insertBefore(w,ps.children[cut<0?ps.children.length:cut]||null);
    w.addEventListener("change",function(e){var t=e.target;if(t.id==="tcCat"){TC.cat=t.value;TC.feat="all"}else if(t.id==="tcFeat")TC.feat=t.value;else if(t.id==="tcSt")TC.st=t.value;else if(t.id==="tcRnd")TC.rnd=t.checked;TC.i=0;tcSave();tcBuild(false).then(tcRender)})}
  var cl=byId("cells");if(cl){var c1=document.createElement("div");c1.id="tcCells";cl.after(c1)}
  var qc=byId("qcells");if(qc){var c2=document.createElement("div");c2.id="tcCells2";qc.after(c2)}
  document.addEventListener("click",function(e){var t=e.target.closest("[data-tc-tab],[data-tc-n],[data-tc-feat]");if(!t)return;e.preventDefault();e.stopPropagation();
    if(t.dataset.tcTab){tcSet(t.dataset.tcTab==="c");window.scrollTo(0,0);return}
    if(t.dataset.tcN){var n=+t.dataset.tcN,k=TCL.findIndex(function(c){return c.n===n});if(k<0){TC.cat="all";TC.feat="all";TC.st="all";return tcBuild(false).then(function(){TC.i=TCL.findIndex(function(c){return c.n===n});tcSave();tcRender();closeP()})}TC.i=k;tcSave();tcRender();closeP();return}
    if(t.dataset.tcFeat){TC.cat=String(chOfS(t.dataset.tcFeat));TC.feat=t.dataset.tcFeat;TC.i=0;tcSave();tcBuild(false).then(function(){tcRender();closeP()})}},true);
  byId("tcCard").addEventListener("click",tcFlip);
  byId("tcPrev").onclick=function(){tcMove(-1)};byId("tcNext").onclick=function(){tcMove(1)};
  byId("tcAct").querySelector(".tc-mid").addEventListener("click",function(e){var b=e.target.closest("button[data-k]");if(b)tcMark(b.dataset.k==="known")});
  byId("tcGo").onclick=function(){var c=TCL[TC.i];if(!c)return;closeP();setView("text");setTimeout(function(){if(!tcShowTerm(c))jump("f-"+c.s)},60)};
  window.addEventListener("keydown",function(e){if(!TC.on||view!=="quiz"||curP||e.metaKey||e.ctrlKey||e.altKey||e.target.closest&&e.target.closest("input,textarea,select,[contenteditable]"))return;
    var k=e.key;if(k===" "||k==="Enter"){if(e.target.closest&&e.target.closest("button,a")&&e.target.id!=="tcCard")return;tcFlip()}else if(k==="ArrowRight")tcMove(1);else if(k==="ArrowLeft")tcMove(-1);else if(k==="k"||k==="K")tcMark(true);else if(/^[1-9]$/.test(k)){}else return;e.preventDefault();e.stopImmediatePropagation()},true);
  var _gq=goQuiz;goQuiz=function(sec){tcSet(false);return _gq.apply(this,arguments)};
  var _jt=jumpTo;jumpTo=function(id){if(TC.on)tcSet(false);return _jt.apply(this,arguments)};
  document.body.classList.toggle("tc-on",TC.on);tcTabs();if(TC.on){var _o=TC.on;TC.on=false;tcSet(_o)}
  if(location.hash==="#terms"){tcSet(true);if(view!=="quiz")setView("quiz")}
  /* トレーニングの用語カードから来たとき: その語句の箇所へ */
  try{var jp=JSON.parse(sessionStorage.getItem("cs-term-jump")||"null");if(jp&&jp.subj===TCID&&Date.now()-jp.ts<60000){sessionStorage.removeItem("cs-term-jump");var tries=0;(function tj(){if(view==="text"&&tcShowTerm(jp))return;if(++tries<40)setTimeout(tj,200)})()}}catch(e){}}
var TCCSS='/*用語カード(問題集)*/\n.tc-tabs{margin:0 auto 14px;max-width:420px}\n.tc-tabs button{display:flex;align-items:center;justify-content:center;gap:6px}\n.tc-tabs button small{font-size:12px;font-weight:600;opacity:.8}\n.tc-tabs button[aria-selected=true]{background:var(--accent);color:var(--accent-ink)}\n'+
 '#tcv,#tcSet,#tcCells,#tcCells2{display:none}\nbody.tc-on #tcv,body.tc-on #tcSet,body.tc-on #tcCells,body.tc-on #tcCells2{display:block}\nbody.tc-on .q-flt,body.tc-on #fmtTabs,body.tc-on #selv,body.tc-on #qv-in>.tbrow,body.tc-on #card,body.tc-on #actions,body.tc-on #qtext,body.tc-on #hint,body.tc-on #subj-qfoot,body.tc-on #cells,body.tc-on #qcells,body.tc-on #p-list .legend{display:none!important}\n'+
 '.tc-sum{display:flex;flex-wrap:wrap;justify-content:space-between;gap:4px 12px;font-size:13px;color:var(--muted);margin:0 0 10px}\n.tc-kn{font-weight:700;color:var(--ok)}\n'+
 '#tcv{perspective:1600px}\n.tc-card{position:relative;display:grid;min-height:240px;transition:transform .7s cubic-bezier(.2,.7,.2,1);transform-style:preserve-3d;cursor:pointer;outline-offset:3px}\n.tc-card.on{transform:rotateY(180deg)}\n.tc-card>div{grid-area:1/1;align-self:stretch;backface-visibility:hidden;-webkit-backface-visibility:hidden;border:1px solid var(--line);border-radius:16px;background:var(--surface);padding:22px 20px;box-shadow:0 18px 40px -28px rgba(0,0,0,.35)}\n.tc-card .tc-b{transform:rotateY(180deg);background:var(--yama-soft);border-color:color-mix(in srgb,var(--yama) 35%,var(--line))}\n@media(prefers-reduced-motion:reduce){.tc-card{transition:none}}\n'+
 '.tc-sec{margin:0 0 18px;font-size:12.5px;color:var(--muted);display:flex;flex-wrap:wrap;align-items:center;gap:6px}\n.tc-sec b{color:var(--accent);font-weight:800}\n.tc-ok{font-size:11.5px;font-weight:800;color:var(--ok);background:var(--ok-soft);border-radius:999px;padding:0 8px}\n'+
 '.tc-f h3{margin:26px 0 22px;font-size:22px;line-height:1.5;text-align:center;font-weight:800}\n.tc-hint{margin:0;text-align:center;font-size:12.5px;color:var(--muted)}\n.tc-t{margin:0 0 12px;font-weight:800;font-size:16px;color:var(--accent)}\n.tc-d{margin:0;font-size:15.5px;line-height:1.9}\n.tc-empty{margin:60px 0;text-align:center;color:var(--muted)}\n'+
 '.tc-act{display:grid;grid-template-columns:minmax(0,1fr) auto minmax(0,1fr);align-items:center;gap:10px;margin-top:14px}\n.tc-act[hidden]{display:none}\n.tc-act button{font:inherit;font-weight:700;font-size:14px;border:1px solid var(--line);background:var(--surface);color:var(--ink);border-radius:999px;padding:8px 14px;cursor:pointer;white-space:nowrap}\n.tc-act .tc-nv:first-child{justify-self:start}\n.tc-act .tc-nv:last-child{justify-self:end}\n.tc-mid{display:flex;gap:8px}\n.tc-mid [data-k=known]{background:var(--ok);border-color:var(--ok);color:#fff}\n.tc-mid [data-k=known][aria-pressed=true]{box-shadow:0 0 0 3px var(--ok-soft)}\n'+
 '.tc-pos{text-align:center;font-size:13px;color:var(--muted);margin:10px 0 0}\n.tc-links{text-align:center;margin:12px 0 0}\n.tc-go{font:inherit;font-weight:700;font-size:14px;color:var(--accent);background:var(--accent-soft);border:1px solid var(--accent);border-radius:999px;padding:8px 16px;cursor:pointer}\n.tc-go[hidden]{display:none}\n#tcv .hint{text-align:center;margin-top:14px}\n'+
 '#tcCells .cell.dim,#tcCells2 .cell.dim{opacity:.4}\n#tcCells .gl-bar u,#tcCells2 .gl-bar u{display:none}\n@media(max-width:520px){.tc-act button{padding:8px 11px;font-size:13.5px}.tc-f h3{font-size:20px}}\n';
setTimeout(tcInit,0);
window.__tcDbg={load:tcLoad,range:tcTermRange,render:tcRender,st:function(){return {TC:TC,TCL:TCL}}};
'''
rep("function gridOut(h){", JS + "function gridOut(h){")
# 一覧の描き直しのたびに、用語カードの一覧も最新に(問題の一覧は隠れたまま)
rep("function renderAll(){renderToolbar();", 'function renderAll(){if(typeof TC!=="undefined"&&TC&&TC.on)setTimeout(tcRender,0);renderToolbar();')
open(out, "w", encoding="utf-8").write(s); print("ok")
