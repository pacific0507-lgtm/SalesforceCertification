"""ホーム画面を、ユーザーごとに好きにカスタマイズできるようにする。
  - ホームのいちばん下(とメニューの「表示」)の「ホームをカスタマイズ」で、編集シート(スマホは下から出るシート)を開く
  - まとまり(きょうの一歩・更新情報・3つの特徴・みんなで合格まで)と、きょうの一歩のカードを、表示/非表示と ↑↓ で並べ替えできる
    (カードは大きさに関係なく1つの並びで並べ替える。既定の並びのときは元の2列の形のまま、変えたときは列をほどいて並べる)
  - お便り・いちばん上のお知らせの帯・「使い方を見る」の案内は、表示/非表示だけ
  - 見出しの真ん中に大きく出るキャラ(クラウドちゃん・まなびん・コミットくん・ランダム)を選べる
  - 見出しと「ホームをカスタマイズ」のボタンは隠せない(いつでも元に戻せるように)
  - 並びと表示は CSS(head の <style id="hc-style">)の order / display だけで当てる。DOM は動かさないので、
    あとから非同期に描かれるカードや案内にも、そのまま効く。ホームを描くたびに当て直す
  - 保存は localStorage の cs-home-layout({v,order,hidden,chara,ts})。アカウントに同期(fam-ls、鍵ごと新しい方)
    知らない id は無視し、保存にない(あとから増えた)まとまりは既定の位置に表示する。壊れたデータは既定に戻す
使い方: python3 patch_home_custom.py <index.html> <出力>
"""
import json, sys
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count: sys.exit(f"置換対象が {n} 件(期待 {count} 件): {old[:90]!r}")
    s = s.replace(old, new)

JS = r'''
/* ==ホームのカスタマイズ(ユーザーごと。cs-home-layout)== */
var csHC=(function(){
  var KEY="cs-home-layout",P='body[data-page="home"] ';
  var G=[
    {k:"sec",h:"まとまりの順番",ids:["hero","today","news","points","closing"],mv:1},
    {k:"card",h:"きょうの一歩のカード",ids:["cont","daily","rev","streak","exam","rank","garden"],mv:1},
    {k:"ex",h:"そのほかの表示",ids:["letter","banner"],mv:0}];
  var N={hero:["見出しとキャラ","タイトル・紹介文・キャラ・「科目を選ぶ」"],today:["きょうの一歩","続き・今日の1問・復習などのカード"],news:["更新情報","さいきんの更新"],
    points:["3つの特徴","読みながら覚える・その場で問題・草が生える"],
    closing:["みんなで合格まで","締めのひとこと"],
    cont:["前回の続き",""],daily:["今日の1問",""],rev:["今日の復習",""],streak:["連続学習",""],exam:["本試験まで",""],rank:["いまの称号",""],garden:["草の庭",""],
    letter:["キャラからのお便り","届いたときだけ出ます"],banner:["いちばん上のお知らせ","新しい更新があるときの帯"],guide:["「使い方を見る」の案内","はじめての方への案内"]};
  var SEL={hero:"main>.hero",today:"#today",news:"main>section.news",points:"main>section.points",closing:"main>section.closing",
    cont:"#bx-cont",daily:"#bx-daily",rev:"#bx-rev",streak:"#bx-streak",exam:"#bx-exam",rank:"#bx-rank",garden:"#bx-garden",
    letter:"#bx-letter",banner:"main>.nbn-w",guide:"#guide-cta"};
  var CH=[["rou","クラウドちゃん","pose-rou-laugh"],["pote","まなびん","pose-pote-pc"],["pen","コミットくん","pose-pen-smile"],["rand","ランダム",""]];
  var FIG={rou:"a1",pote:"a2",pen:"a3"};
  /* スマホ(560px以下)では、学習を始めた人(body.ret)には自動で隠れていた2つ。表示にすると出す */
  var AUTO=["points","closing"];
  function autoOff(id){try{return AUTO.indexOf(id)>=0&&document.body.classList.contains("ret")&&matchMedia("(max-width:560px)").matches}catch(e){return false}}
  function isOn(L,id){return !L.hidden[id]&&(!!L.shown[id]||!autoOff(id))}
  function raw(){try{return localStorage.getItem(KEY)||""}catch(e){return ""}}
  /* 保存の中身をいつも正しい形に。知らない id は捨て、足りない id は既定の位置へ */
  function norm(d){if(!d||typeof d!=="object"||Array.isArray(d))d={};
    var ord=Array.isArray(d.order)?d.order.filter(function(x){return typeof x==="string"}):[],hid=(d.hidden&&typeof d.hidden==="object"&&!Array.isArray(d.hidden))?d.hidden:{};
    var shw=(d.shown&&typeof d.shown==="object"&&!Array.isArray(d.shown))?d.shown:{};
    var r={v:1,ts:+d.ts||0,order:{},hidden:{},shown:{},chara:"rou"};AUTO.forEach(function(id){if(shw[id]&&!hid[id])r.shown[id]=1});
    G.forEach(function(g){var seen={},l=[];ord.forEach(function(id){if(g.ids.indexOf(id)>=0&&!seen[id]){seen[id]=1;l.push(id)}});
      g.ids.forEach(function(id,i){if(seen[id])return;var at=0;for(var j=i-1;j>=0;j--){var p=l.indexOf(g.ids[j]);if(p>=0){at=p+1;break}}l.splice(at,0,id);seen[id]=1});
      r.order[g.k]=g.mv?l:g.ids.slice();g.ids.forEach(function(id){if(hid[id])r.hidden[id]=1})});
    if(CH.some(function(c){return c[0]===d.chara}))r.chara=d.chara;
    return r}
  function load(){var v=null;try{v=JSON.parse(raw())}catch(e){v=null}return norm(v)}
  function save(L){var o={v:1,order:[],hidden:{},chara:L.chara,ts:Date.now()};G.forEach(function(g){o.order=o.order.concat(L.order[g.k])});
    Object.keys(L.hidden).forEach(function(id){if(L.hidden[id])o.hidden[id]=1});o.shown={};Object.keys(L.shown||{}).forEach(function(id){if(L.shown[id])o.shown[id]=1});
    try{localStorage.setItem(KEY,JSON.stringify(o))}catch(e){}apply()}
  function same(a,b){return a.join()===b.join()}
  function css(L){var c=[],H=L.hidden,G0=G[0].ids,o=L.order;
    if(!same(o.sec,G0)){c.push(P+"main{display:flex;flex-direction:column}",P+"main>*{order:50}",P+"main>.nbn-w{order:-2}",P+"main>.hc-bar{order:100}");
      o.sec.forEach(function(id,i){c.push(P+SEL[id]+"{order:"+(i+1)+"}")})}
    var MAIN=["cont","daily"],SIDE=["rev","streak","exam","rank","garden"],cd=o.card;
    Object.keys(H).forEach(function(id){if(H[id]&&SEL[id])c.push(P+SEL[id]+"{display:none!important}")});
    Object.keys(L.shown||{}).forEach(function(id){if(L.shown[id]&&SEL[id])c.push("@media (max-width:560px){body.ret[data-page=\"home\"] "+SEL[id]+"{display:block!important}}")});
    var mainOff=MAIN.every(function(id){return H[id]}),sideOff=SIDE.every(function(id){return H[id]});
    if(same(cd,G[1].ids)){
      /* 既定の並び: 元の2列(大きいカード|小さいカード)のまま */
      if(mainOff)c.push(P+".bento>.col:not(.side){display:none}");
      if(sideOff)c.push(P+".bento>.col.side{display:none}");
      if(mainOff||sideOff)c.push(P+".bento{grid-template-columns:1fr}");
      if(mainOff&&!sideOff)c.push("@media (min-width:861px){"+P+".bento .col.side{grid-template-columns:1fr 1fr;grid-auto-flow:row dense}}");
      if(SIDE.some(function(id){return H[id]}))c.push("@media (max-width:860px){"+P+".bento .col.side>.bx{grid-column:1/-1}}");
    }else{
      /* 大きい・小さいに関係なく並べ替えたとき: 列をほどいて1つの並びにする。スマホは1列、PC は左上から順に2列(並べた順のとおりに見えるよう、横いっぱいのカードは作らない) */
      c.push(P+".bento{display:grid!important;grid-template-columns:1fr!important;grid-auto-flow:row}",P+".bento>.col{display:contents!important}",P+".bento .bx{grid-column:auto;min-width:0}");
      c.push("@media (min-width:861px){"+P+".bento{grid-template-columns:1fr 1fr!important;grid-auto-flow:row}}",P+".bento .bx{grid-column:auto!important}");
      cd.forEach(function(id,i){c.push(P+SEL[id]+"{order:"+(i+1)+"}")});
    }
    if(mainOff&&sideOff){c.push(P+"#bento{display:none!important}");
      c.push(H.letter?P+"#today{display:none!important}":"@supports selector(:has(*)){"+P+"#today:not(:has(#bx-letter:not([hidden]))){display:none!important}}")}
    var ch=L.chara;if(ch==="rand")ch=window.__hcRand||"rou";
    if(ch!=="rou"&&FIG[ch]){var big=FIG[ch],rest=["a1","a2","a3"].filter(function(x){return x!==big}),A=P+".art figure.";
      /* 真ん中=大きい席。残りの2人は左下と右下。大きい席の上に小さい2人が重なるように */
      c.push(A+big+"{width:58%;left:20%;top:16%;right:auto;bottom:auto;z-index:1}");
      c.push(A+rest[0]+"{width:34%;left:0;bottom:6%;top:auto;right:auto;z-index:2}");
      c.push(A+rest[1]+"{width:34%;right:0;bottom:12%;top:auto;left:auto;z-index:2}");
      c.push(P+".art .bubble,"+P+".art .hero-say{z-index:3}")}
    return c.join("\n")}
  var last=null;
  function apply(){try{var st=document.getElementById("hc-style");
      if(!st){st=document.createElement("style");st.id="hc-style";document.head.appendChild(st)}
      last=raw();var t=css(load());if(st.textContent!==t)st.textContent=t}catch(e){}}
  function esc(t){return String(t).replace(/[&<>"]/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]})}
  function rowsHTML(L){var h='<p class="hc-lead">変えるとすぐにホームに反映され、アカウントに保存されます。</p>';
    h+='<section class="hc-g"><h3>まんなかのキャラ</h3><div class="hc-ch" role="radiogroup" aria-label="まんなかのキャラ">'+CH.map(function(c){var on=L.chara===c[0];
      return '<button type="button" role="radio" data-ch="'+c[0]+'" aria-checked="'+on+'">'+(c[2]?'<img src="chars/'+c[2]+'.webp" alt="" width="40" height="40">':'<span class="hc-q" aria-hidden="true">?</span>')+'<span>'+c[1]+'</span></button>'}).join("")+'</div></section>';
    G.forEach(function(g){var l=L.order[g.k];h+='<section class="hc-g"><h3>'+g.h+'</h3><ol class="hc-l">';
      l.forEach(function(id,i){var on=isOn(L,id),n=N[id];
        h+='<li class="hc-r'+(on?"":" off")+'" data-id="'+id+'" data-g="'+g.k+'"><span class="hc-n"><b>'+esc(n[0])+'</b>'+(n[1]?'<small>'+esc(n[1])+'</small>':'')+'</span>'+
          '<button type="button" class="hc-sw" role="switch" aria-checked="'+on+'" aria-label="'+esc(n[0])+'を表示"><i></i></button>'+
          (g.mv?'<button type="button" class="hc-mv" data-mv="-1"'+(i===0?" disabled":"")+' aria-label="'+esc(n[0])+'を上へ">↑</button><button type="button" class="hc-mv" data-mv="1"'+(i===l.length-1?" disabled":"")+' aria-label="'+esc(n[0])+'を下へ">↓</button>':'')+'</li>'});
      if(g.k==="sec")h+='<li class="hc-r fx"><span class="hc-n"><b>「ホームをカスタマイズ」</b><small>いつもいちばん下に出ます</small></span><span class="hc-fx">固定</span></li>';
      h+='</ol></section>'});
    return h}
  function close(){var ov=document.getElementById("hc-ov");if(!ov)return;ov.classList.remove("in");setTimeout(function(){ov.remove()},220);
    var b=document.getElementById("hc-open");if(b)try{b.focus({preventScroll:true})}catch(e){}}
  function open(){if(document.getElementById("hc-ov"))return;var ov=document.createElement("div");ov.id="hc-ov";ov.className="hc-ov";
    ov.innerHTML='<div class="hc-scrim" data-x></div><div class="hc-sh" role="dialog" aria-modal="true" aria-labelledby="hc-t"><div class="hc-hd"><b id="hc-t">ホームをカスタマイズ</b><button type="button" class="hc-x" data-x aria-label="閉じる">×</button></div><div class="hc-bd"></div><div class="hc-ft"><button type="button" class="hc-reset">元に戻す</button><button type="button" class="hc-done" data-x>完了</button></div></div>';
    document.body.appendChild(ov);var bd=ov.querySelector(".hc-bd");
    function draw(focus){var y=bd.scrollTop;bd.innerHTML=rowsHTML(load());bd.scrollTop=y;
      if(focus){var el=bd.querySelector(focus);if(el&&!el.disabled)try{el.focus({preventScroll:true})}catch(e){}}}
    draw();
    ov.addEventListener("click",function(e){var t=e.target;
      if(t.closest("[data-x]")){close();return}
      if(t.closest(".hc-reset")){save(norm({}));draw();bd.scrollTop=0;return}
      var L=load(),c=t.closest("[data-ch]");
      if(c){L.chara=c.dataset.ch;if(L.chara==="rand")window.__hcRand=CH[Math.floor(Math.random()*3)][0];save(L);draw('[data-ch="'+L.chara+'"]');return}
      var r=t.closest(".hc-r[data-id]");if(!r)return;var id=r.dataset.id,g=r.dataset.g;
      if(t.closest(".hc-sw")){if(isOn(L,id)){L.hidden[id]=1;delete L.shown[id]}else{delete L.hidden[id];if(AUTO.indexOf(id)>=0)L.shown[id]=1}save(L);draw('.hc-r[data-id="'+id+'"] .hc-sw');return}
      var m=t.closest(".hc-mv");if(m){var l=L.order[g],i=l.indexOf(id),j=i+(+m.dataset.mv);if(i<0||j<0||j>=l.length)return;l[i]=l[j];l[j]=id;save(L);
        draw('.hc-r[data-id="'+id+'"] .hc-mv[data-mv="'+m.dataset.mv+'"]');
        var nr=bd.querySelector('.hc-r[data-id="'+id+'"]');if(nr){nr.classList.add("mv");setTimeout(function(){nr.classList.remove("mv")},900);
          var rb=nr.getBoundingClientRect(),bb=bd.getBoundingClientRect();if(rb.top<bb.top||rb.bottom>bb.bottom)nr.scrollIntoView({block:"nearest"})}}});
    ov.addEventListener("keydown",function(e){if(e.key==="Escape"){e.preventDefault();close()}});
    requestAnimationFrame(function(){ov.classList.add("in")});
    try{ov.querySelector(".hc-done").focus({preventScroll:true})}catch(e){}}
  var tick=0;
  function home(){try{window.__hcRand=CH[Math.floor(Math.random()*3)][0];apply();
      var b=document.getElementById("hc-open");if(b&&!b._hc){b._hc=1;b.addEventListener("click",open)}
      /* メニューの「表示」にも入口を足す */
      var seg=document.querySelector("#drawer .seg");if(seg&&!document.getElementById("hc-dr")){var d=document.createElement("button");d.type="button";d.id="hc-dr";d.className="hc-dr";d.textContent="ホームをカスタマイズ";
        seg.parentNode.insertBefore(d,seg.nextSibling);d.addEventListener("click",function(){var x=document.getElementById("dr-close");if(x)x.click();setTimeout(open,260)})}
      /* 別の端末から同期されたら当て直す(ホームにいるあいだだけ見る) */
      if(!tick)tick=setInterval(function(){if(!document.getElementById("hc-open")){clearInterval(tick);tick=0;return}if(raw()!==last)apply()},1500)}catch(e){}}
  apply();
  return {home:home,open:open,apply:apply,norm:norm}})();
(function(){var o=FAMP.home;FAMP.home=function(){o();setTimeout(csHC.home,0)}})();
'''
anchor = "(function(){var o=FAMP.home;FAMP.home=function(){o();setTimeout(csHeroGrass,0);setTimeout(csKusa,0)}})();"
rep(anchor, anchor + JS)

CSS = """
/* ホームのカスタマイズ */
.hc-bar{display:flex;justify-content:center;padding-top:28px;padding-bottom:8px}
.hc-open{display:inline-flex;align-items:center;gap:7px;font:inherit;font-size:13.5px;font-weight:700;color:var(--sub);background:var(--paper);border:1px solid var(--line);border-radius:999px;padding:9px 18px;cursor:pointer}
.hc-open svg{width:16px;height:16px;flex:none}
.hc-dr{display:block;width:100%;margin-top:10px;font:inherit;font-size:13.5px;font-weight:700;color:var(--ink);background:var(--paper);border:1px solid var(--line);border-radius:12px;padding:10px 12px;text-align:left;cursor:pointer}
.hc-ov{position:fixed;inset:0;z-index:80;display:flex;align-items:flex-end;justify-content:center}
.hc-scrim{position:absolute;inset:0;background:rgba(10,10,12,.42);opacity:0;transition:opacity .22s}
.hc-ov.in .hc-scrim{opacity:1}
.hc-sh{position:relative;display:flex;flex-direction:column;width:100%;max-width:520px;max-height:88vh;max-height:88dvh;background:var(--bg,var(--paper));color:var(--ink);border-radius:22px 22px 0 0;box-shadow:0 -12px 40px -16px rgba(0,0,0,.45);transform:translateY(100%);transition:transform .26s cubic-bezier(.2,.75,.2,1)}
.hc-ov.in .hc-sh{transform:none}
.hc-hd{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:16px 16px 10px;border-bottom:1px solid var(--line)}
.hc-hd b{font-size:17px}
.hc-x{font:inherit;font-size:22px;line-height:1;width:40px;height:40px;border-radius:50%;border:1px solid var(--line);background:var(--paper);color:var(--ink);cursor:pointer}
.hc-bd{flex:1;min-height:0;overflow-y:auto;-webkit-overflow-scrolling:touch;overscroll-behavior:contain;padding:4px 16px 12px}
.hc-lead{margin:10px 0 4px;font-size:12.5px;color:var(--sub);line-height:1.6}
.hc-g h3{margin:16px 0 8px;font-size:12.5px;letter-spacing:.08em;color:var(--sub)}
.hc-l{list-style:none;margin:0;padding:0;display:grid;gap:6px}
.hc-r{display:flex;align-items:center;gap:8px;background:var(--paper);border:1px solid var(--line);border-radius:14px;padding:8px 8px 8px 12px;transition:opacity .2s}
.hc-r.off .hc-n{opacity:.5}
.hc-r.fx{background:transparent;border-style:dashed}
.hc-r.mv{animation:hcMv .9s ease-out}
@keyframes hcMv{0%{box-shadow:0 0 0 3px var(--brand)}100%{box-shadow:0 0 0 0 transparent}}
.hc-n{flex:1;min-width:0;display:flex;flex-direction:column;gap:1px}
.hc-n b{font-size:14.5px;line-height:1.4}
.hc-n small{font-size:11.5px;color:var(--sub);line-height:1.45}
.hc-fx{font-size:11.5px;font-weight:700;color:var(--sub);padding:0 8px}
.hc-sw{flex:none;position:relative;width:50px;height:30px;border-radius:999px;border:0;padding:0;background:var(--line);cursor:pointer;transition:background .2s}
.hc-sw i{position:absolute;left:3px;top:3px;width:24px;height:24px;border-radius:50%;background:#fff;box-shadow:0 1px 3px rgba(0,0,0,.3);transition:transform .2s}
.hc-sw[aria-checked=true]{background:var(--ok,#2a9765)}
.hc-sw[aria-checked=true] i{transform:translateX(20px)}
.hc-mv{flex:none;font:inherit;font-size:15px;font-weight:700;width:40px;height:38px;border-radius:10px;border:1px solid var(--line);background:var(--paper);color:var(--ink);cursor:pointer}
.hc-mv:disabled{opacity:.3;cursor:default}
.hc-ch{display:grid;grid-template-columns:repeat(4,1fr);gap:6px}
.hc-ch button{display:flex;flex-direction:column;align-items:center;gap:4px;font:inherit;font-size:11.5px;font-weight:700;color:var(--ink);background:var(--paper);border:1.5px solid var(--line);border-radius:14px;padding:8px 2px;cursor:pointer;min-width:0}
.hc-ch button span:last-child{white-space:nowrap;letter-spacing:-.02em}
.hc-ch img,.hc-q{width:40px;height:40px;border-radius:50%;background:#fff;object-fit:cover}
.hc-q{display:flex;align-items:center;justify-content:center;font-size:18px;color:var(--sub);background:var(--line)}
.hc-ch button[aria-checked=true]{border-color:var(--brand);box-shadow:0 0 0 2px var(--brand)}
.hc-ft{display:flex;gap:10px;padding:12px 16px calc(12px + env(safe-area-inset-bottom,0px));border-top:1px solid var(--line)}
.hc-ft button{flex:1;font:inherit;font-size:15px;font-weight:800;border-radius:999px;padding:12px;cursor:pointer}
.hc-reset{color:var(--ink);background:var(--paper);border:1px solid var(--line)}
.hc-done{color:var(--brand-ink);background:var(--brand);border:0}
@media (min-width:761px){.hc-ov{align-items:center}.hc-sh{border-radius:22px;max-height:84vh;transform:translateY(24px);opacity:0;transition:transform .26s cubic-bezier(.2,.75,.2,1),opacity .2s}.hc-ov.in .hc-sh{opacity:1}}
"""
BAR = ('\n <div class="wrap hc-bar"><button type="button" class="hc-open" id="hc-open">'
       '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 6h10M18 6h2M4 12h4M12 12h8M4 18h12M20 18h0"/><circle cx="16" cy="6" r="2"/><circle cx="10" cy="12" r="2"/><circle cx="18" cy="18" r="2"/></svg>'
       'ホームをカスタマイズ</button></div>\n')
lines = s.split("\n")
idx = [i for i, l in enumerate(lines) if "window.FAMD=" in l]
if len(idx) != 1: sys.exit(f"FAMD の行が {len(idx)} 件")
l = lines[idx[0]]
j = l.index("window.FAMD=") + len("window.FAMD="); F, end = json.JSONDecoder().raw_decode(l[j:])
hm = F["pages"]["home"]["markup"]
if hm.count("</main>") != 1: sys.exit("home の </main> が見つからない")
F["pages"]["home"]["markup"] = hm.replace("</main>", BAR + "</main>")
F["pages"]["home"]["css"] += CSS
lines[idx[0]] = l[:j] + json.dumps(F, ensure_ascii=False).replace("</", "<\\/") + l[j+end:]
s = "\n".join(lines)
rep("`cs-badge-told`]", "`cs-badge-told`,`cs-home-layout`]")
open(out, "w", encoding="utf-8").write(s); print("ok")
