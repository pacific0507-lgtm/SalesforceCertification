"""庭の仲間の「くわしい画面」(カード)を足す。
  - 開く場所: 草の庭の「新しい仲間が庭に来ました」の名前・アイコン、学習の記録/全画面の「庭の仲間」一覧の各行
  - 中身: 大きな絵・名前・空の印・プロフィール・仲間になった条件(まだなら「あと〇〇」)・仲間になった日・
          眠る時刻・ひとこと(3つ)・特別なかけあいがある仲間・お気に入りの☆
  - まだ仲間になっていない子はシルエットと条件だけ(名前・せりふは出さない)
  公開先では body が作り直されるため、CSS はスクリプトで document.head に入れる。
使い方: python3 patch_pal_card.py <index.html> <出力>
"""
import sys
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count: sys.exit(f"置換対象が {n} 件(期待 {count} 件): {old[:90]!r}")
    s = s.replace(old, new)
# 一覧の行から開く
rep("""return '<li class="'+(ok?"on":"lk")+(fv?" fav":"")+'">'+csPalIcon(P.id,ok?"":"sil")+'<div>""",
    """return '<li class="'+(ok?"on":"lk")+(fv?" fav":"")+'" data-palcard="'+P.id+'" tabindex="0" role="button" aria-label="'+(ok?P.nm:"まだ仲間になっていない子")+'のくわしい説明">'+csPalIcon(P.id,ok?"":"sil")+'<div>""")
# 新しい仲間のお知らせから開く
rep("""  return '<p class="gd-new" role="status">'+csPalIcon(nw[0])+'<span><b>新しい仲間が庭に来ました'+(nw.length>1?'('+nw.length+'匹)':'')+'</b>'+(nm.length>4?nm.slice(0,4).join("・")+" ほか":nm.join("・"))+'</span></p>'}catch(e){return ""}}""",
    """  var nb=nw.slice(0,4).map(function(id,i){return '<button type="button" class="gd-new-nm" data-palcard="'+id+'">'+nm[i]+'</button>'}).join("・");
  return '<p class="gd-new" role="status"><button type="button" class="gd-new-ic" data-palcard="'+nw[0]+'" aria-label="'+nm[0]+'のくわしい説明">'+csPalIcon(nw[0])+'</button><span><b>新しい仲間が庭に来ました'+(nw.length>1?'('+nw.length+'匹)':'')+'</b>'+nb+(nm.length>4?" ほか":"")+'<small class="gd-new-h">名前を押すと、くわしく見られます</small></span></p>'}catch(e){return ""}}""")
JS = r'''
/* ==庭の仲間のくわしい画面== */
function csPalBed(id){var P=CS_PALMAP[id];if(P&&P.zz)return P.zz;var h=0;for(var i=0;i<id.length;i++)h=(h*31+id.charCodeAt(i))>>>0;return [21.5+(h%8)*0.25,6+((h>>3)%5)*0.25]}
function csPalHM(x){x=((x%24)+24)%24;var h=Math.floor(x),m=Math.round((x-h)*60);if(m===60){h=(h+1)%24;m=0}return h+":"+(m<10?"0":"")+m}
function csPalCardClose(){var o=document.getElementById("pc-ov");if(!o)return;o.classList.remove("in");setTimeout(function(){o.remove()},200)}
function csPalCard(id){try{var P=CS_PALMAP[id];if(!P)return;csPalCardClose();var o0=document.getElementById("pc-ov");if(o0)o0.remove();
  var S=window.__csPalSt||{on:[],st:{}},ok=S.on.indexOf(id)>=0,e=function(t){return String(t).replace(/[&<>"]/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]})};
  var seen={};try{seen=JSON.parse(localStorage.getItem(CS_PALSEEN)||"{}")||{}}catch(x){}
  var h='<div class="pc-hd"><div class="pc-art">'+csPalIcon(id,ok?"":"sil")+'</div><div class="pc-tt"><b>'+(ok?e(P.nm):"？？？")+'</b>'+(P.sky&&ok?'<i class="gp-sk">空</i>':'')+'</div>';
  if(ok){var fv=!!csPalFav()[id];h+='<ul class="pc-favl"><li'+(fv?' class="fav"':'')+'><button type="button" class="gp-fav pc-fav" data-palfav="'+id+'" aria-pressed="'+fv+'" aria-label="'+e(P.nm)+'をお気に入りにする">'+(fv?"★":"☆")+'</button></li></ul>'}
  h+='</div>';
  if(ok){h+='<p class="pc-pf">'+e(P.pf)+'</p>';
    var ln=(P.ln||[]).slice();for(var i=ln.length-1;i>0;i--){var j=Math.floor(Math.random()*(i+1)),t=ln[i];ln[i]=ln[j];ln[j]=t}
    if(ln.length)h+='<div class="pc-sec"><h3>ひとこと</h3><div class="pc-lns">'+ln.slice(0,3).map(function(l){return '<p class="pc-ln">'+e(l).replace(/\n/g,"<br>")+'</p>'}).join("")+'</div></div>'}
  var dt=ok&&seen[id]?new Date(+seen[id]):null,lf=ok?"":(typeof csPalLeft==="function"?csPalLeft(P,S.st):"");
  var rows=[[ok?"仲間になった条件":"仲間になる条件",e(P.ct)+(lf?'<br><em>'+e(lf)+'</em>':'')]];
  if(dt&&!isNaN(dt))rows.push(["仲間になった日",dt.getFullYear()+"年"+(dt.getMonth()+1)+"月"+dt.getDate()+"日"]);
  if(ok){var bw=csPalBed(id),day=bw[0]<bw[1];rows.push(["眠る時刻",(day?"昼に眠る子です。":"")+csPalHM(bw[0])+"ごろ寝て、"+csPalHM(bw[1])+"ごろ起きます"]);
    var fr=[];(typeof CS_PALPAIR!=="undefined"?CS_PALPAIR:[]).forEach(function(p){var o=p[0]===id?p[1]:p[1]===id?p[0]:null;if(o&&fr.indexOf(o)<0)fr.push(o)});
    if(fr.length)rows.push(["なかよしの仲間",fr.map(function(o){var Q=CS_PALMAP[o];if(!Q)return "";var on=S.on.indexOf(o)>=0;return on?'<button type="button" class="pc-fr" data-palcard="'+o+'">'+csPalIcon(o)+e(Q.nm)+'</button>':'<span class="pc-fr lk">'+csPalIcon(o,"sil")+'？？？</span>'}).join("")+'<small>庭で近くにいると、特別なかけあいをします</small>'])}
  h+='<dl class="pc-dl">'+rows.map(function(r){return '<div><dt>'+r[0]+'</dt><dd>'+r[1]+'</dd></div>'}).join("")+'</dl>';
  if(!ok)h+='<p class="pc-lk">まだ仲間になっていません。条件を満たすと庭にやって来ます。</p>';
  var ov=document.createElement("div");ov.id="pc-ov";ov.className="pc-ov";
  ov.innerHTML='<div class="pc-scrim" data-pcx></div><div class="pc-sh" role="dialog" aria-modal="true" aria-label="'+(ok?e(P.nm):"まだ仲間になっていない子")+'のくわしい説明"><button type="button" class="pc-x" data-pcx aria-label="閉じる">×</button><div class="pc-bd">'+h+'</div></div>';
  document.body.appendChild(ov);requestAnimationFrame(function(){ov.classList.add("in")});try{ov.querySelector(".pc-x").focus({preventScroll:true})}catch(x){}
}catch(err){}}
document.addEventListener("click",function(ev){var t=ev.target;if(!t||!t.closest)return;
  if(t.closest("[data-pcx]")){ev.preventDefault();csPalCardClose();return}
  if(t.closest("[data-palfav]"))return;var c=t.closest("[data-palcard]");if(c){ev.preventDefault();ev.stopPropagation();csPalCard(c.getAttribute("data-palcard"))}},true);
document.addEventListener("keydown",function(ev){if(ev.key==="Escape"&&document.getElementById("pc-ov")){ev.stopPropagation();csPalCardClose();return}
  var t=ev.target;if((ev.key==="Enter"||ev.key===" ")&&t&&t.matches&&t.matches("li[data-palcard]")){ev.preventDefault();csPalCard(t.getAttribute("data-palcard"))}},true);
(function(){if(document.getElementById("cs-pal-card"))return;var st=document.createElement("style");st.id="cs-pal-card";st.textContent=__PCCSS__;document.head.appendChild(st)})();
'''
CSS = """
.pc-ov{position:fixed;inset:0;z-index:9000;display:flex;align-items:flex-end;justify-content:center}
.pc-scrim{position:absolute;inset:0;background:rgba(0,0,0,.42);opacity:0;transition:opacity .2s}
.pc-ov.in .pc-scrim{opacity:1}
.pc-sh{position:relative;width:min(520px,100%);max-height:calc(100dvh - 40px - env(safe-area-inset-top,0px));display:flex;flex-direction:column;background:var(--paper,#fff);color:var(--ink,#1a1a1a);border-radius:22px 22px 0 0;box-shadow:0 -12px 40px rgba(0,0,0,.25);transform:translateY(24px);opacity:0;transition:transform .22s,opacity .22s;padding-bottom:env(safe-area-inset-bottom,0px)}
.pc-ov.in .pc-sh{transform:none;opacity:1}
@media (min-width:700px){.pc-ov{align-items:center}.pc-sh{border-radius:22px}}
.pc-x{position:absolute;top:10px;right:10px;width:38px;height:38px;border-radius:50%;border:1px solid var(--line,#ddd);background:var(--paper,#fff);color:var(--sub,#666);font-size:20px;line-height:1;cursor:pointer;z-index:2}
.pc-bd{overflow-y:auto;-webkit-overflow-scrolling:touch;overscroll-behavior:contain;padding:22px 20px 20px}
.pc-hd{display:flex;align-items:center;gap:14px;padding-right:40px}
.pc-art{flex:none;width:92px;height:92px;border-radius:50%;background:color-mix(in srgb,var(--ok,#3a3) 14%,var(--paper,#fff));display:grid;place-items:center}
.pc-art svg{width:78px;height:78px;overflow:visible}
.pc-art svg.sil g{filter:brightness(0) opacity(.35)}
.pc-tt{flex:1;min-width:0;display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.pc-tt b{font-size:22px;letter-spacing:-.01em}
.pc-favl{list-style:none;margin:0;padding:0;flex:none}
.pc-favl li{display:block}
.pc-fav{position:static!important;width:42px;height:42px;border-radius:12px;border:1px solid var(--line,#ddd);background:var(--paper,#fff);color:var(--sub,#777);font-size:21px;line-height:1;cursor:pointer;display:grid;place-items:center}
.pc-fav[aria-pressed=true]{color:#e0a100;border-color:#e0a100;background:color-mix(in srgb,#e0a100 10%,var(--paper,#fff))}
.pc-pf{margin:14px 0 0;font-size:14.5px;line-height:1.8}
.pc-sec h3,.pc-dl dt{font-size:12px;font-weight:700;color:var(--sub,#666);margin:16px 0 6px;letter-spacing:.04em}
.pc-lns{display:flex;flex-direction:column;gap:8px}
.pc-ln{margin:0;align-self:flex-start;max-width:92%;background:var(--sun-soft,#fff6d8);border-radius:14px 14px 14px 4px;padding:8px 12px;font-size:14px;line-height:1.6;text-align:left}
.pc-dl{margin:6px 0 0}
.pc-dl>div{border-top:1px solid var(--line,#eee);padding:2px 0 8px}
.pc-dl dd{margin:0;font-size:14px;line-height:1.7}
.pc-dl em{font-style:normal;font-weight:700;color:var(--brand,#1d4a6e)}
.pc-dl small{display:block;font-size:12px;color:var(--sub,#666);margin-top:4px}
.pc-fr{display:inline-flex;align-items:center;gap:4px;margin:2px 6px 2px 0;padding:3px 10px 3px 4px;border:1px solid var(--line,#ddd);border-radius:999px;background:var(--surface,#fafafa);color:inherit;font:inherit;font-size:13px;cursor:pointer}
.pc-fr svg{width:24px;height:24px;overflow:visible}
.pc-fr.lk{cursor:default;color:var(--sub,#888)}
.pc-fr svg.sil g{filter:brightness(0) opacity(.35)}
.pc-lk{margin:14px 0 0;font-size:13.5px;color:var(--sub,#666)}
li[data-palcard]{cursor:pointer}
.gd-new-nm,.gd-new-ic{border:0;background:none;padding:0;margin:0;font:inherit;color:inherit;cursor:pointer}
.gd-new-nm{text-decoration:underline;text-underline-offset:3px;font-weight:700;color:var(--brand,inherit)}
.gd-new-h{display:block;font-size:11.5px;color:var(--sub,#777);margin-top:2px}
"""
import json
s = s.replace("</head>", "<script>" + JS.replace("__PCCSS__", json.dumps(CSS)) + "</script></head>") if False else s
# 庭の処理と同じスクリプトの中(CS_PALS などが見える場所)に入れる: 「新しい仲間のお知らせ」の関数の直前
rep("/* 新しい仲間のお知らせ(1回だけ) */", JS.replace("__PCCSS__", json.dumps(CSS)).replace("</", "<\\/") + "\n/* 新しい仲間のお知らせ(1回だけ) */")
open(out, "w", encoding="utf-8").write(s); print("ok")
