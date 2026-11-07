"""生えた草で「庭」や「山」が育っていく要素を追加する。
  - ホーム(きょうの一歩): 「草の庭」カード。学習した日ごとに草が1本ずつ生え、日数で 空き地 → 芽 → 草むら → 庭 → 花の庭 → 丘 → 山 → 山脈 と育つ
  - 学習の記録: 「草の庭」のくわしい表示。大きな庭のイラスト、次の段階までの進み具合、草の種類ごとの本数
使い方: python3 patch_garden.py <index.html> <出力>   (patch_grass.py の CS_GRASS・csGrassKind を使う)
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
/* ==草の庭: 学習した日・解いた問題数・勉強時間で草が生え、庭・丘・山と育つ。空は時間帯と季節で変わる== */
var CS_STAGES=[[0,"まだ空き地","1節読むか1問解くと、最初の芽が出ます"],[1,"芽が出た","草が少しずつ生えてきました"],[7,"小さな草むら","草が集まってきました"],[15,"草の庭","庭らしくなってきました"],[30,"花の庭","花が咲きそろう庭になりました"],[60,"小さな丘","草が積もって丘ができました"],[100,"草の山","ついに山になりました"],[200,"緑の山脈","山が連なる大自然です"],[300,"小さな林","木が育ちはじめました"],[400,"深い森","森が広がりました"],[500,"森の湖","森の奥に湖ができました"],[650,"虹の谷","谷に虹がかかりました"],[800,"雲海の高原","雲の上まで緑が届きました"],[1000,"緑の楽園","どこまでも緑が続く楽園です"]];
var CS_GNAMES=["芝","双葉","花","草むら","若葉","つくし","たんぽぽ","ススキ","四つ葉"];
/* 草の本数: 学習した日に1本、さらにこれまでに解いた問題10問ごとに1本、勉強時間30分ごとに1本 */
function csGardenDays(days){var ks=Object.keys(days||{}).filter(function(k){var d=days[k];return d&&(d.q||d.r||d.t)}).sort(),out=[],q=0,t=0,nq=0,nt=0;
  ks.forEach(function(k){var d=days[k];if(d.q||d.r)out.push(k);q+=+d.q||0;t+=+d.t||0;while(Math.floor(q/10)>nq){nq++;out.push(k+"#q"+nq)}while(Math.floor(t/1800)>nt){nt++;out.push(k+"#t"+nt)}});return out}
function csStage(n){var k=0;for(var i=0;i<CS_STAGES.length;i++)if(n>=CS_STAGES[i][0])k=i;return k}
function csGardenSVG(list,W,H){var n=list.length,st=csStage(n),g="";
  /* 空: 端末の時刻で 朝焼け・昼・夕焼け・夜(星と月)、月で季節(春は花びら・夏は入道雲・秋は落ち葉・冬は雪) */
  var SK=csSkyNow(),uid="g"+Math.floor(Math.random()*1e9),SC={dawn:["#f4a988","#fde2c4"],day:["#8fcaf0","#e2f3fb"],dusk:["#ee8559","#f8cf96"],night:["#16233f","#34466e"]}[SK.tod];
  var sky='<defs><linearGradient id="'+uid+'" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="'+SC[0]+'"/><stop offset="1" stop-color="'+SC[1]+'"/></linearGradient></defs><rect width="'+W+'" height="'+H+'" fill="url(#'+uid+')" class="gd-sky2"/>';
  var rnd=function(i){var x=Math.sin(i*99.13+W)*43758.5453;return x-Math.floor(x)};
  if(SK.tod==="night"){for(var si=0;si<22;si++)sky+='<circle cx="'+(rnd(si)*W).toFixed(1)+'" cy="'+(rnd(si+50)*H*0.5).toFixed(1)+'" r="'+(0.6+rnd(si+90)*1.1).toFixed(2)+'" class="gd-star" style="animation-delay:'+(rnd(si+7)*3).toFixed(2)+'s"/>';
    sky+='<circle cx="'+(W*0.16)+'" cy="'+(H*0.17)+'" r="'+(H*0.075)+'" fill="#fdf3c4"/><circle cx="'+(W*0.16+H*0.035)+'" cy="'+(H*0.15)+'" r="'+(H*0.068)+'" fill="'+SC[0]+'"/>'}
  if(SK.season==="summer")[[0.62,0.2,1],[0.3,0.12,0.7]].forEach(function(c){var cx=W*c[0],cy=H*c[1],k=c[2]*H*0.07;sky+='<g class="gd-cu"><circle cx="'+cx+'" cy="'+(cy+k)+'" r="'+(k*1.3)+'"/><circle cx="'+(cx-k*1.4)+'" cy="'+(cy+k*1.4)+'" r="'+k+'"/><circle cx="'+(cx+k*1.5)+'" cy="'+(cy+k*1.3)+'" r="'+(k*1.1)+'"/><rect x="'+(cx-k*2.4)+'" y="'+(cy+k*1.4)+'" width="'+(k*5)+'" height="'+(k*0.9)+'" rx="'+(k*0.45)+'"/></g>'});
  if(st>=5)g+='<path d="M0 '+(H*0.62)+' Q'+(W*0.25)+' '+(H*0.28)+' '+(W*0.5)+' '+(H*0.6)+' T'+W+' '+(H*0.58)+' V'+H+' H0Z" class="gd-hill"/>';
  if(st>=6)g+='<path d="M'+(W*0.18)+' '+(H*0.66)+' L'+(W*0.42)+' '+(H*0.14)+' L'+(W*0.66)+' '+(H*0.66)+'Z" class="gd-mt"/><path d="M'+(W*0.36)+' '+(H*0.27)+' L'+(W*0.42)+' '+(H*0.14)+' L'+(W*0.48)+' '+(H*0.27)+'Z" fill="#fff" opacity=".85"/>';
  if(st>=7)g+='<path d="M'+(W*0.55)+' '+(H*0.68)+' L'+(W*0.78)+' '+(H*0.22)+' L'+W+' '+(H*0.6)+' V'+(H*0.7)+'Z" class="gd-mt2"/>';
  /* 300本からの段階: 林・森・湖・虹・雲海・楽園 */
  if(st>=12)g='<path d="M0 '+(H*0.3)+' Q'+(W*0.2)+' '+(H*0.22)+' '+(W*0.4)+' '+(H*0.3)+' T'+(W*0.8)+' '+(H*0.28)+' T'+W+' '+(H*0.3)+' V'+(H*0.38)+' H0Z" class="gd-cloud"/>'+g;
  if(st>=11)g='<path d="M'+(W*0.12)+' '+(H*0.66)+' A'+(W*0.38)+' '+(H*0.55)+' 0 0 1 '+(W*0.88)+' '+(H*0.66)+'" class="gd-rb gd-rb1"/><path d="M'+(W*0.16)+' '+(H*0.66)+' A'+(W*0.34)+' '+(H*0.49)+' 0 0 1 '+(W*0.84)+' '+(H*0.66)+'" class="gd-rb gd-rb2"/><path d="M'+(W*0.2)+' '+(H*0.66)+' A'+(W*0.3)+' '+(H*0.43)+' 0 0 1 '+(W*0.8)+' '+(H*0.66)+'" class="gd-rb gd-rb3"/>'+g;
  if(st>=13)g='<circle cx="'+(W*0.9)+'" cy="'+(H*0.16)+'" r="'+(H*0.09)+'" class="gd-sun"/>'+g;
  if(st>=8){var tn=st>=9?9:4;for(var ti=0;ti<tn;ti++){var tx=W*(0.06+ti*(0.88/(tn-1||1))),ty=H*(0.6+((ti*37)%7)/100),tr=H*(0.07+((ti*13)%4)/100);g+='<path d="M'+tx.toFixed(1)+' '+(ty-tr*2.4).toFixed(1)+' L'+(tx+tr).toFixed(1)+' '+ty.toFixed(1)+' L'+(tx-tr).toFixed(1)+' '+ty.toFixed(1)+'Z" class="gd-tree"/><rect x="'+(tx-1.5).toFixed(1)+'" y="'+ty.toFixed(1)+'" width="3" height="'+(tr*0.5).toFixed(1)+'" class="gd-trunk"/>'}}
  var lk=st>=10?'<ellipse cx="'+(W*0.7)+'" cy="'+(H*0.76)+'" rx="'+(W*0.15)+'" ry="'+(H*0.055)+'" class="gd-lake"/>':'';
  g+='<rect y="'+(H*0.64)+'" width="'+W+'" height="'+(H*0.36)+'" class="gd-ground"/>'+lk;
  var shown=list.slice(-90);
  shown.forEach(function(day,i){var h=csGrassHash(day+"#g"),x=8+(h%1000)/1000*(W-28),y=H*0.62+((h>>>10)%1000)/1000*(H*0.3),sc=0.55+((h>>>20)%100)/100*0.25;
    g+='<g transform="translate('+x.toFixed(1)+','+y.toFixed(1)+') scale('+sc.toFixed(2)+') translate(-20,-31)">'+CS_GRASS[csGrassKind(day)]+'</g>'});
  if(!n)g+='<text x="'+W/2+'" y="'+(H*0.82)+'" text-anchor="middle" class="gd-empty">ここに草が生えていきます</text>';
  var fx="";
  if(SK.season==="spring"||SK.season==="autumn"||SK.season==="winter"){var cnt=SK.season==="winter"?26:22;for(var fi=0;fi<cnt;fi++){var fxp=(rnd(fi+200)*W).toFixed(1),fyp=(rnd(fi+300)*H*0.8).toFixed(1),dl=(rnd(fi+400)*6).toFixed(2),du=(5+rnd(fi+500)*5).toFixed(2);
    var shp=SK.season==="winter"?'<circle r="'+(1+rnd(fi+600)*1.4).toFixed(2)+'" fill="#fff"/>':SK.season==="spring"?'<ellipse rx="3.4" ry="2.1" fill="#f5a3bb"/>':'<path d="M0 -3 Q3 0 0 3 Q-3 0 0 -3Z" fill="'+(fi%2?"#e07a3a":"#c94f2c")+'"/>';
    fx+='<g transform="translate('+fxp+','+fyp+')"><g class="gd-fall" style="animation-delay:-'+dl+'s;animation-duration:'+du+'s">'+shp+'</g></g>'}}
  if(SK.season==="winter")fx='<rect y="'+(H*0.64)+'" width="'+W+'" height="'+(H*0.36)+'" fill="#fff" opacity=".14"/>'+fx;
  if(SK.season==="autumn")fx='<rect y="'+(H*0.64)+'" width="'+W+'" height="'+(H*0.36)+'" fill="#e3a35a" opacity=".16"/>'+fx;
  if(SK.tod==="night")fx+='<rect width="'+W+'" height="'+H+'" fill="#0b1630" opacity=".22"/>';
  else if(SK.tod==="dusk"||SK.tod==="dawn")fx+='<rect width="'+W+'" height="'+H+'" fill="#f08a4b" opacity=".08"/>';
  var lbl={dawn:"朝",day:"昼",dusk:"夕方",night:"夜"}[SK.tod]+"・"+{spring:"春",summer:"夏",autumn:"秋",winter:"冬"}[SK.season];
  return '<svg class="garden" viewBox="0 0 '+W+' '+H+'" role="img" aria-label="これまでに生えた草 '+n+'本('+lbl+'の庭)">'+sky+g+fx+'</svg>'}
function csSkyNow(){var o=window.__csSky||{},d=new Date(),h=d.getHours(),m=d.getMonth()+1;
  return {tod:o.tod||(h<5||h>=19?"night":h<8?"dawn":h<16?"day":h<19?"dusk":"night"),season:o.season||(m>=3&&m<=5?"spring":m>=6&&m<=8?"summer":m>=9&&m<=11?"autumn":"winter")}}
function csGarden(el,s){try{if(!el||!s)return;var list=csGardenDays(s.days),n=list.length,st=csStage(n),nx=CS_STAGES[st+1];
  el.innerHTML='<p class="bx-k">草の庭<span>'+n+'本</span></p>'+csGardenSVG(list,340,150)+'<p class="gd-st"><b>'+CS_STAGES[st][1]+'</b>'+(nx?'<small>あと'+(nx[0]-n)+'本で「'+nx[1]+'」</small>':'<small>最高の段階です</small>')+'</p><a class="bx-go" href="/record/#garden-d">草の庭をくわしく見る</a>'}catch(e){}}
function csGardenDetail(days){try{var el=document.getElementById("garden-detail");if(!el)return;var list=csGardenDays(days),n=list.length,st=csStage(n),cur=CS_STAGES[st],nx=CS_STAGES[st+1];
  var pct=nx?Math.round((n-cur[0])/(nx[0]-cur[0])*100):100,cnt=[0,0,0,0,0,0,0,0,0];list.forEach(function(d){cnt[csGrassKind(d)]++});
  var h=csGardenSVG(list,340,190)+'<div class="gd-now"><b>'+cur[1]+'</b><span>'+cur[2]+'</span></div>';
  h+='<div class="gd-prog"><div class="l"><span>'+(nx?'次の段階「'+nx[1]+'」まで':'最高の段階')+'</span><span>'+n+(nx?' / '+nx[0]:'')+'本</span></div><div class="bar"><i style="width:'+Math.max(0,Math.min(100,pct))+'%"></i></div></div>';
  h+='<p class="gd-h">生えた草の種類</p><ul class="gd-kinds">'+CS_GNAMES.map(function(nm,k){return '<li class="'+(cnt[k]?"":"z")+'"><svg viewBox="0 0 40 40" aria-hidden="true"><circle cx="20" cy="20" r="19" class="gs-bg"/>'+CS_GRASS[k]+'</svg><span>'+nm+'</span><b>'+cnt[k]+'</b></li>'}).join("")+'</ul>';
  h+='<p class="gd-h">育ち方</p><ol class="gd-steps">'+CS_STAGES.map(function(x,i){return '<li class="'+(i<=st?"on":"")+(i===st?" cur":"")+'"><b>'+x[0]+'本〜</b>'+x[1]+'</li>'}).join("")+'</ol><p class="bx-s">1節読むか1問解いた日に、草が1本生えます。さらに、これまでに解いた問題10問ごとに1本、勉強時間30分ごとに1本生えます。草の種類はランダムに決まり、まれに四つ葉のクローバーが生えます。</p>';
  el.innerHTML=h}catch(e){}}
'''
rep("FAMP.home=function(){", JS + "\nFAMP.home=function(){")
# ホームの「草の庭をくわしく見る」で、学習の記録の草の庭まで移る(リンクは /record/#garden-d)
rep("FAMP.record=function(){", "FAMP.record=function(){if(location.hash===\"#garden-d\"){var gdN=0;(function gdGo(){var el=document.getElementById(\"garden-d\"),d=document.getElementById(\"garden-detail\");"
    "if(!el||!d||!d.children.length){if(gdN++<40)setTimeout(gdGo,150);return}el.classList.remove(\"rv\");el.classList.add(\"in\");"
    "var h=document.querySelector(\"header.hd,.hd\"),off=(h?h.getBoundingClientRect().height:60)+12;window.scrollTo(0,el.getBoundingClientRect().top+scrollY-off)})()}")
rep("Kt(Z(`#bx-rank`,e),s)", "Kt(Z(`#bx-rank`,e),s),csGarden(Z(`#bx-garden`,e),s)", 2)
rep("let[f,p]=je(t);$(`#cal-say`)", "csGardenDetail(e.days);let[f,p]=je(t);$(`#cal-say`)")
CSS = """
/* 草の庭 */
.garden{display:block;width:100%;height:auto;border-radius:12px;overflow:hidden}
.garden .gd-sky{fill:color-mix(in srgb,#bfe3f5 55%,var(--paper))}
.garden .gd-star{fill:#fff;animation:gdTw 3s ease-in-out infinite alternate}
@keyframes gdTw{from{opacity:.35}to{opacity:1}}
.garden .gd-cu{fill:#fff;opacity:.9}
.garden .gd-fall{animation:gdFall 7s linear infinite}
@keyframes gdFall{0%{transform:translate(0,-30px) rotate(0)}50%{transform:translate(6px,15px) rotate(140deg)}100%{transform:translate(-4px,60px) rotate(300deg);opacity:0}}
.garden .gd-ground{fill:color-mix(in srgb,#9fd27a 55%,var(--paper))}
.garden .gd-hill{fill:color-mix(in srgb,#7cc35a 60%,var(--paper))}
.garden .gd-mt{fill:color-mix(in srgb,#4f9a4a 75%,var(--paper))}
.garden .gd-mt2{fill:color-mix(in srgb,#3d7f3c 70%,var(--paper))}
.garden .gd-tree{fill:#2f7a3b}
.garden .gd-trunk{fill:#7a5a3a}
.garden .gd-lake{fill:#6fb6e8;opacity:.85}
.garden .gd-rb{fill:none;stroke-width:4;opacity:.55}
.garden .gd-rb1{stroke:#f08a8a}
.garden .gd-rb2{stroke:#f2c94c}
.garden .gd-rb3{stroke:#7cc5f0}
.garden .gd-cloud{fill:#fff;opacity:.75}
.garden .gd-sun{fill:#f6c343}
.garden .gd-empty{font-size:12px;fill:var(--sub)}
.gd-st{display:flex;align-items:baseline;gap:8px;flex-wrap:wrap;margin:8px 0 0}
.gd-st b{font-size:16px}.gd-st small{color:var(--sub);font-size:12.5px}
#bx-garden,#bx-rank{grid-column:1/-1}
#bx-garden .bx-go{margin-top:8px;font-size:13px;padding:7px 14px;align-self:flex-start}
.gd-now{display:flex;flex-direction:column;gap:2px;margin:10px 0 6px}.gd-now b{font-size:18px}.gd-now span{color:var(--sub);font-size:13px}
.gd-prog .l{display:flex;justify-content:space-between;font-size:12.5px;color:var(--sub)}
.gd-prog .bar{height:8px;border-radius:99px;background:var(--line);overflow:hidden;margin-top:4px}.gd-prog .bar i{display:block;height:100%;background:var(--ok);border-radius:99px}
.gd-h{font-size:12.5px;font-weight:700;color:var(--sub);margin:14px 0 6px;letter-spacing:.06em}
.gd-kinds{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(130px,1fr));gap:6px}
.gd-kinds li{display:flex;align-items:center;gap:6px;background:var(--bg);border-radius:10px;padding:5px 8px;font-size:12.5px}
.gd-kinds li svg{width:26px;height:26px;flex:none}.gd-kinds li span{flex:1;min-width:0;white-space:nowrap}.gd-kinds li b{font-variant-numeric:tabular-nums}
.gd-kinds li.z{opacity:.4}
.gd-kinds .gs-bg{fill:color-mix(in srgb,var(--ok,#2a9765) 14%,var(--paper,#fff))}
.gd-steps{list-style:none;margin:0 0 8px;padding:0;display:grid;grid-template-columns:repeat(2,1fr);gap:4px 10px;font-size:12.5px;color:var(--sub)}
.gd-steps li b{display:inline-block;min-width:4.5em;font-weight:600}
.gd-steps li.on{color:var(--ink)}.gd-steps li.cur{font-weight:800;color:var(--ok)}
"""
lines = s.split("\n"); l = lines[4]
j = l.index("window.FAMD=") + len("window.FAMD="); F, end = json.JSONDecoder().raw_decode(l[j:])
for k in ("home", "record"): F["pages"][k]["css"] += CSS
hm = F["pages"]["home"]["markup"]; a = '<article class="bx rv" id="bx-rank" aria-label="いまの称号"></article>'
assert hm.count(a) == 1; F["pages"]["home"]["markup"] = hm.replace(a, a + '\n     <article class="bx rv" id="bx-garden" aria-label="草の庭"></article>')
rm = F["pages"]["record"]["markup"]; b = '<section class="bx rv" id="time"'
assert rm.count(b) == 1; F["pages"]["record"]["markup"] = rm.replace(b, '<section class="bx rv" id="garden-d" aria-labelledby="h-garden"><p class="bx-k" id="h-garden">草の庭<span>これまでに生えた草</span></p><div id="garden-detail"></div></section>\n   ' + b)
lines[4] = l[:j] + json.dumps(F, ensure_ascii=False).replace("</", "<\\/") + l[j+end:]
s = "\n".join(lines)
open(out, "w", encoding="utf-8").write(s); print("ok")
