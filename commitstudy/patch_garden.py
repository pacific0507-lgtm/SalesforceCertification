"""生えた草で「庭」や「山」が育っていく要素を追加する。
  - ホーム(きょうの一歩): 「草の庭」カード。学習した日ごとに草が1本ずつ生え、日数で 空き地 → 芽 → 草むら → 庭 → 花の庭 → 丘 → 山 → 山脈 と育つ
  - 学習の記録: 「草の庭」のくわしい表示。大きな庭のイラスト、次の段階までの進み具合、草の種類ごとの本数
  - 空は 季節 × 時間帯 で演出が変わり(夜は落ち葉や蝶を出さない)、日付で決まる日替わりの演出(虹・渡り鳥・流れ星・花火・オーロラなど)が加わる
  - 庭の右上のボタンで全画面表示(×・Esc・ブラウザの戻るで閉じる)。庭をタップすると、季節と時間帯に合った演出がタップした場所に出る
  テスト用: window.__csSky={tod:"night",season:"autumn",variant:"shoot",day:"2026-11-07"} で時間帯・季節・日替わりの演出を固定できる
使い方: python3 patch_garden.py <index.html> <出力>   (patch_grass.py の CS_GRASS・csGrassKind・csGrassHash を使う)
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
/* 日替わりの演出: 季節×時間帯ごとに候補と重み。日付から決まるので、同じ日は同じ演出になる */
var CS_SKYV={spring:{dawn:[["none",3],["mist",2],["birds",2],["rainbow",1]],day:[["none",3],["birds",2],["rainbow",1],["fubuki",2],["balloon",1],["clouds",2]],dusk:[["none",3],["birds",2],["clouds",1]],night:[["none",3],["fullmoon",2],["shoot",2]]},
  summer:{dawn:[["none",2],["mist",2],["rainbow",1]],day:[["none",2],["rainbow",1],["birds",1],["balloon",1],["clouds",2]],dusk:[["none",2],["fireworks",2],["birds",1]],night:[["none",2],["fireworks",2],["shoot",2],["fullmoon",1],["milkyway",2]]},
  autumn:{dawn:[["none",3],["mist",2],["birds",1]],day:[["none",3],["birds",2],["rainbow",1],["clouds",1],["balloon",1]],dusk:[["none",2],["birds",3],["clouds",1]],night:[["none",3],["shoot",2],["clouds",1]]},
  winter:{dawn:[["none",3],["mist",1],["heavy",1]],day:[["none",3],["snowman",2],["heavy",1],["birds",1],["clear",2]],dusk:[["none",3],["snowman",1],["heavy",1]],night:[["none",4],["aurora",1],["shoot",2],["heavy",1],["fullmoon",1]]}};
var CS_SKYVN={mist:"朝もや",birds:"渡り鳥",rainbow:"雨上がりの虹",fubuki:"花吹雪",balloon:"気球",clouds:"流れる雲",fullmoon:"満月",shoot:"流れ星",fireworks:"遠くの花火",milkyway:"天の川",heavy:"大雪",snowman:"雪だるま",clear:"冬晴れ",aurora:"オーロラ"};
var CS_SKYBASE={spring:{dawn:"花びら",day:"花びらとちょう",dusk:"花びら",night:"夜桜"},summer:{dawn:"入道雲",day:"ひまわりと入道雲",dusk:"ほたる",night:"ほたる"},autumn:{dawn:"ススキ",day:"落ち葉と赤とんぼ",dusk:"赤とんぼ",night:"お月見"},winter:{dawn:"雪の朝",day:"雪",dusk:"雪",night:"雪の夜"}};
function csDayKey(d){d=d||new Date();return d.getFullYear()+"-"+("0"+(d.getMonth()+1)).slice(-2)+"-"+("0"+d.getDate()).slice(-2)}
function csSkyNow(){var o=window.__csSky||{},d=new Date(),h=d.getHours(),m=d.getMonth()+1,day=o.day||csDayKey(d);
  var tod=o.tod||(h<5||h>=19?"night":h<8?"dawn":h<16?"day":h<19?"dusk":"night"),season=o.season||(m>=3&&m<=5?"spring":m>=6&&m<=8?"summer":m>=9&&m<=11?"autumn":"winter");
  var L=((CS_SKYV[season]||CS_SKYV.spring)[tod])||[["none",1]],v=o.variant;
  if(!(v==="none"||CS_SKYVN[v])){var tot=0;L.forEach(function(x){tot+=x[1]});var r=csGrassHash(day+"|sky|"+season+tod)%tot;v=L[0][0];for(var i=0;i<L.length;i++){if(r<L[i][1]){v=L[i][0];break}r-=L[i][1]}}
  return {tod:tod,season:season,variant:v,day:day}}
function csSkyLabel(SK){var vn=SK.variant==="birds"&&SK.tod==="dusk"?"ねぐらへ帰る鳥":SK.variant==="clouds"&&SK.tod==="night"?"月にかかる雲":CS_SKYVN[SK.variant];
  return {dawn:"朝",day:"昼",dusk:"夕方",night:"夜"}[SK.tod]+"・"+{spring:"春",summer:"夏",autumn:"秋",winter:"冬"}[SK.season]+"(" +(vn||CS_SKYBASE[SK.season][SK.tod])+")"}
/* 庭の絵。opt.fs: 全画面用(草を多めに、空の演出も多めに)。地面より上の地形は高さ TH を基準に描くので、縦長の画面でも山が伸びすぎない */
function csGardenSVG(list,W,H,opt){opt=opt||{};var n=list.length,st=csStage(n),g="",SK=csSkyNow(),T=SK.tod,SE=SK.season,V=SK.variant,uid="g"+Math.floor(Math.random()*1e9);
  var TH=Math.min(H,W*0.6),HY=H-(TH*0.36+(H-TH)*0.4),u=TH/150,q=Math.min(1.7,Math.sqrt(u)),um=Math.min(u,2.2),F=function(v){return Math.round(v*10)/10},fk=opt.fs?2:1;
  var fy=function(f){return F(f<=0.64?HY-TH*(0.64-f):HY+(f-0.64)/0.36*(H-HY))};
  var sd=csGrassHash(SK.day)%997,rnd=function(i){var x=Math.sin(i*99.13+W+sd)*43758.5453;return x-Math.floor(x)};
  var night=T==="night",low=T==="dawn"||T==="dusk";
  var SC=night?(SE==="spring"?["#1c2143","#3b3d68"]:V==="aurora"?["#0d1730","#25365e"]:["#16233f","#34466e"]):T==="dawn"?["#f4a988","#fde2c4"]:T==="dusk"?["#ee8559","#f8cf96"]:{spring:["#9fd3f2","#eaf6fc"],summer:["#5fb4ee","#d9f0fb"],autumn:["#7cbbe8","#e4f1f8"],winter:[V==="clear"?"#86c3ee":"#b3d3e6","#eef5f9"]}[SE];
  var full=SE==="autumn"&&night||V==="fullmoon",mx=W*(full||SE==="spring"?0.78:0.16),my=F(HY*(full?0.3:0.27)),mr=(full?(SE==="autumn"?15:13):11.25)*um;
  var df='<defs><linearGradient id="'+uid+'" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="'+SC[0]+'"/><stop offset="1" stop-color="'+SC[1]+'"/></linearGradient>'
    +'<linearGradient id="'+uid+'o" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0b1630" stop-opacity=".04"/><stop offset="1" stop-color="#0b1630" stop-opacity=".3"/></linearGradient>'
    +'<radialGradient id="'+uid+'h"><stop offset="0" stop-color="#fff6d0" stop-opacity=".55"/><stop offset="1" stop-color="#fff6d0" stop-opacity="0"/></radialGradient>'
    +'<radialGradient id="'+uid+'r"><stop offset="0" stop-color="#ffd59a" stop-opacity=".7"/><stop offset="1" stop-color="#ffd59a" stop-opacity="0"/></radialGradient>'
    +'<filter id="'+uid+'b" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="'+F(2*u)+'"/></filter><filter id="'+uid+'c" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="'+F(6*u)+'"/></filter>'
    +'<linearGradient id="'+uid+'s" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="-34" y2="0"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>'
    +(night&&!full?'<mask id="'+uid+'m"><rect width="'+W+'" height="'+H+'" fill="#fff"/><circle cx="'+F(mx+mr*0.47)+'" cy="'+F(my-mr*0.27)+'" r="'+F(mr*0.9)+'" fill="#000"/></mask>':'')+'</defs>';
  var sk='<rect width="'+W+'" height="'+H+'" fill="url(#'+uid+')" class="gd-sky2"/>';
  /* --- 夜空: 天の川・オーロラ・星・月・流れ星 --- */
  if(night){
    if(V==="milkyway"){sk+='<ellipse cx="'+F(W/2)+'" cy="'+F(HY*0.4)+'" rx="'+F(W*0.8)+'" ry="'+F(12*u)+'" transform="rotate(-20 '+F(W/2)+' '+F(HY*0.4)+')" fill="#dfe6ff" opacity=".22" filter="url(#'+uid+'c)"/>';
      for(var mi=0;mi<34*fk;mi++){var mt=rnd(mi+1200),mxp=mt*W,myp=HY*0.4-(mxp-W/2)*0.364+(rnd(mi+1300)-0.5)*22*u;if(myp>0&&myp<HY*0.9)sk+='<circle cx="'+F(mxp)+'" cy="'+F(myp)+'" r="'+(0.4+rnd(mi+1400)*0.7).toFixed(2)+'" fill="#fff" opacity=".8"/>'}}
    if(V==="aurora")["#6ff0b0","#5fd6e0","#b48cf0"].forEach(function(c,k){var y=HY*(0.2+k*0.11);sk+='<path d="M-10 '+F(y)+' C'+F(W*0.25)+' '+F(y-14*u)+' '+F(W*0.5)+' '+F(y+12*u)+' '+F(W*0.75)+' '+F(y-8*u)+' S'+F(W+10)+' '+F(y+6*u)+' '+F(W+20)+' '+F(y)+'" fill="none" stroke="'+c+'" stroke-width="'+F((11-k*3)*u)+'" stroke-linecap="round" class="gd-au" style="animation-delay:-'+(k*1.7)+'s" filter="url(#'+uid+'b)"/>'});
    var ns=(22+(SE==="winter"?10:0))*fk;for(var si=0;si<ns;si++)sk+='<circle cx="'+F(rnd(si)*W)+'" cy="'+F(rnd(si+50)*HY*0.85)+'" r="'+((0.6+rnd(si+90)*1.1)*Math.min(q,1.3)).toFixed(2)+'" class="gd-star" style="animation-delay:'+(rnd(si+7)*3).toFixed(2)+'s"/>';
    if(full)sk+='<circle cx="'+F(mx)+'" cy="'+my+'" r="'+F(mr*2.8)+'" fill="url(#'+uid+'h)"/><circle cx="'+F(mx)+'" cy="'+my+'" r="'+F(mr)+'" fill="#fdf1c0"/><circle cx="'+F(mx-mr*0.32)+'" cy="'+F(my-mr*0.2)+'" r="'+F(mr*0.22)+'" fill="#ead592" opacity=".55"/><circle cx="'+F(mx+mr*0.35)+'" cy="'+F(my+mr*0.3)+'" r="'+F(mr*0.16)+'" fill="#ead592" opacity=".5"/><circle cx="'+F(mx+mr*0.1)+'" cy="'+F(my-mr*0.5)+'" r="'+F(mr*0.1)+'" fill="#ead592" opacity=".5"/>';
    else sk+='<circle cx="'+F(mx)+'" cy="'+my+'" r="'+F(mr)+'" fill="#fdf3c4" mask="url(#'+uid+'m)"/>';
    if(V==="shoot")for(var ki=0;ki<2*fk;ki++)sk+='<g transform="translate('+F(W*(0.25+0.45*rnd(700+ki)))+','+F(HY*(0.08+0.25*rnd(710+ki)))+') rotate(28) scale('+q.toFixed(2)+')"><g class="gd-shoot" style="animation-delay:'+(ki*3.7+0.8).toFixed(1)+'s"><line x1="0" y1="0" x2="-34" y2="0" stroke="url(#'+uid+'s)" stroke-width="1.6" stroke-linecap="round"/><circle r="1.3" fill="#fff"/></g></g>'}
  /* --- 朝日・夕日・夏の太陽 --- */
  if(low){var sx=F(W*(T==="dawn"?0.2:0.8)),sr=13*um,sy=st>=5?fy(T==="dawn"?0.36:0.5):F(HY-2*u);sk+='<circle cx="'+sx+'" cy="'+sy+'" r="'+F(sr*3.2)+'" fill="url(#'+uid+'r)"/><circle cx="'+sx+'" cy="'+sy+'" r="'+F(sr)+'" fill="'+(T==="dawn"?"#ffe3ad":"#ffad6b")+'"/>'}
  if(T==="day"&&SE==="summer"&&st<13)sk+='<circle cx="'+F(W*0.8)+'" cy="'+F(HY*0.2)+'" r="'+F(30*um)+'" fill="url(#'+uid+'r)"/><circle cx="'+F(W*0.8)+'" cy="'+F(HY*0.2)+'" r="'+F(10*um)+'" fill="#ffe27a"/>';
  if(V==="rainbow"&&st<11)sk+=[[0.38,0.55,"gd-rb1"],[0.34,0.49,"gd-rb2"],[0.3,0.43,"gd-rb3"]].map(function(a){return '<path d="M'+F(W*(0.55-a[0]))+' '+fy(0.66)+' A'+F(W*a[0])+' '+F(TH*a[1])+' 0 0 1 '+F(W*(0.55+a[0]))+' '+fy(0.66)+'" class="gd-rb gd-rbv '+a[2]+'"/>'}).join("");
  /* --- 夏の入道雲 --- */
  if(SE==="summer"&&!night)[[0.55,0.31,1],[0.27,0.19,0.7]].concat(opt.fs?[[0.1,0.45,0.8]]:[]).forEach(function(c){var cx=W*c[0],cy=HY*c[1],k=c[2]*10.5*um;sk+='<g class="gd-cu'+(T==="dusk"?" gd-cud":"")+'"><circle cx="'+F(cx)+'" cy="'+F(cy+k)+'" r="'+F(k*1.3)+'"/><circle cx="'+F(cx-k*1.4)+'" cy="'+F(cy+k*1.4)+'" r="'+F(k)+'"/><circle cx="'+F(cx+k*1.5)+'" cy="'+F(cy+k*1.3)+'" r="'+F(k*1.1)+'"/><rect x="'+F(cx-k*2.4)+'" y="'+F(cy+k*1.4)+'" width="'+F(k*5)+'" height="'+F(k*0.9)+'" rx="'+F(k*0.45)+'"/></g>'});
  /* --- 遠くの花火 --- */
  if(V==="fireworks"){var FC=["#ffd36b","#ff7aa8","#8fd3ff","#b6f28a","#ffb36b"];for(var wi=0;wi<3*fk;wi++){var fr=11*q*(0.75+0.5*rnd(720+wi)),rays="",col=FC[(wi+sd)%FC.length];
    for(var ra=0;ra<14;ra++){var an=ra/14*Math.PI*2,c1=Math.cos(an),s1=Math.sin(an);rays+='<line x1="'+F(c1*fr*0.25)+'" y1="'+F(s1*fr*0.25)+'" x2="'+F(c1*fr)+'" y2="'+F(s1*fr)+'"/><circle cx="'+F(c1*fr*1.12)+'" cy="'+F(s1*fr*1.12)+'" r="'+F(0.9*q)+'"/>'}
    sk+='<g transform="translate('+F(W*(0.15+0.7*rnd(730+wi)))+','+F(HY*(0.15+0.35*rnd(740+wi)))+')"><g class="gd-fw" style="animation-delay:'+(wi*1.35).toFixed(2)+'s;stroke:'+col+';fill:'+col+';stroke-width:'+F(1.1*q)+'">'+rays+'</g></g>'}}
  /* --- 流れる雲(秋の夜は月にかかる雲) --- */
  var ncl=V==="clouds"?3:opt.fs&&!night&&SE!=="summer"?2:0;for(var ci=0;ci<ncl;ci++){var cy2=F(HY*(night?0.22+0.08*ci:0.1+0.18*ci)),cs=((0.7+0.3*rnd(800+ci))*um).toFixed(2),du=50+ci*14;
    sk+='<g><animateTransform attributeName="transform" type="translate" from="'+F(-60*cs)+' '+cy2+'" to="'+F(W+60*cs)+' '+cy2+'" dur="'+du+'s" begin="-'+F(rnd(810+ci)*du)+'s" repeatCount="indefinite"/><g transform="scale('+cs+')" class="gd-dc"'+(V==="clouds"?'':' style="opacity:.55"')+'><ellipse rx="24" ry="6.5"/><ellipse cx="-8" cy="-4" rx="11" ry="7"/><ellipse cx="7" cy="-6" rx="12" ry="9"/></g></g>'}
  /* --- 渡り鳥(夕方はねぐらへ帰る鳥)・気球 --- */
  if(V==="birds"&&!night){var by=F(HY*(0.25+0.2*rnd(820))),bc=T==="dusk"?"#2b2230":"#3a4a5a",bs="";for(var bi=0;bi<(opt.fs?7:5);bi++)bs+='<g transform="translate('+(-bi*11)+','+((bi%2?5:-2)+bi*2)+')"><path class="gd-bird" style="animation-delay:-'+(bi*0.13).toFixed(2)+'s" d="M-5 0 Q-2.5 -3 0 0 Q2.5 -3 5 0" fill="none" stroke="'+bc+'" stroke-width="1.3" stroke-linecap="round"/></g>';
    sk+='<g><animateTransform attributeName="transform" type="translate" values="-30 '+by+';'+F(W+80)+' '+F(by-18*u)+';'+F(W+80)+' '+F(by-18*u)+'" keyTimes="0;.7;1" dur="24s" begin="-4s" repeatCount="indefinite"/><g transform="scale('+q.toFixed(2)+')">'+bs+'</g></g>'}
  if(V==="balloon"){var ly=F(HY*0.38);sk+='<g><animateTransform attributeName="transform" type="translate" from="-30 '+ly+'" to="'+F(W+30)+' '+F(HY*0.3)+'" dur="80s" begin="-30s" repeatCount="indefinite"/><g transform="scale('+(q*1.15).toFixed(2)+')"><g class="gd-bob"><path d="M0 -14 C9 -14 11 -4 6 3 L2 8 H-2 L-6 3 C-11 -4 -9 -14 0 -14Z" fill="#f08a5d"/><path d="M0 -14 C4 -14 4 -4 2 8 H-2 C-4 -4 -4 -14 0 -14Z" fill="#f6c343"/><path d="M-2 8 L-2.4 10.5 M2 8 L2.4 10.5" stroke="#8a5a3a" stroke-width=".6"/><rect x="-2.6" y="10.5" width="5.2" height="3.6" rx="1" fill="#8a5a3a"/></g></g></g>'}
  /* --- 地形: 段階で 丘・山・山脈・林・森・湖・虹・雲海・太陽 --- */
  var cap=SE==="winter"?0.36:0.27,cw=(cap-0.14)/0.52*0.24;
  if(st>=5)g+='<path d="M0 '+fy(0.62)+' Q'+F(W*0.25)+' '+fy(0.28)+' '+F(W*0.5)+' '+fy(0.6)+' T'+W+' '+fy(0.58)+' V'+H+' H0Z" class="gd-hill"/>';
  if(st>=6)g+='<path d="M'+F(W*0.18)+' '+fy(0.66)+' L'+F(W*0.42)+' '+fy(0.14)+' L'+F(W*0.66)+' '+fy(0.66)+'Z" class="gd-mt"/><path d="M'+F(W*(0.42-cw))+' '+fy(cap)+' L'+F(W*0.42)+' '+fy(0.14)+' L'+F(W*(0.42+cw))+' '+fy(cap)+'Z" fill="#fff" opacity=".85"/>';
  if(st>=7)g+='<path d="M'+F(W*0.55)+' '+fy(0.68)+' L'+F(W*0.78)+' '+fy(0.22)+' L'+W+' '+fy(0.6)+' V'+fy(0.7)+'Z" class="gd-mt2"/>'+(SE==="winter"?'<path d="M'+F(W*0.72)+' '+fy(0.34)+' L'+F(W*0.78)+' '+fy(0.22)+' L'+F(W*0.83)+' '+fy(0.32)+'Z" fill="#fff" opacity=".85"/>':'');
  if(st>=12)g='<path d="M0 '+fy(0.3)+' Q'+F(W*0.2)+' '+fy(0.22)+' '+F(W*0.4)+' '+fy(0.3)+' T'+F(W*0.8)+' '+fy(0.28)+' T'+W+' '+fy(0.3)+' V'+fy(0.38)+' H0Z" class="gd-cloud"/>'+g;
  if(st>=11&&!night)g=[[0.38,0.55,1],[0.34,0.49,2],[0.3,0.43,3]].map(function(a){return '<path d="M'+F(W*(0.5-a[0]))+' '+fy(0.66)+' A'+F(W*a[0])+' '+F(TH*a[1])+' 0 0 1 '+F(W*(0.5+a[0]))+' '+fy(0.66)+'" class="gd-rb gd-rb'+a[2]+'"/>'}).join("")+g;
  if(st>=13&&T==="day")g='<circle cx="'+F(W*0.8)+'" cy="'+fy(0.16)+'" r="'+F(13.5*um)+'" class="gd-sun"/>'+g;
  if(st>=8){var tn=st>=9?9:4;for(var ti=0;ti<tn;ti++){var tx=W*(0.06+ti*(0.88/(tn-1||1))),ty=fy(0.6+((ti*37)%7)/100),tr=TH*(0.07+((ti*13)%4)/100);g+='<path d="M'+F(tx)+' '+F(ty-tr*2.4)+' L'+F(tx+tr)+' '+ty+' L'+F(tx-tr)+' '+ty+'Z" class="gd-tree"/><rect x="'+F(tx-1.5*q)+'" y="'+ty+'" width="'+F(3*q)+'" height="'+F(tr*0.5)+'" class="gd-trunk"/>'}}
  var lk=st>=10?'<ellipse cx="'+F(W*0.7)+'" cy="'+fy(0.76)+'" rx="'+F(W*0.15)+'" ry="'+F((H-HY)*0.055/0.36)+'" class="gd-lake"/>':'';
  g+='<rect y="'+F(HY)+'" width="'+W+'" height="'+F(H-HY)+'" class="gd-ground"/>';
  /* 冬は雪の積もった地面、秋は色づいた地面 */
  if(SE==="winter"){var bh=(H-HY)*0.22,wv="";for(var wv1=0;wv1<6;wv1++)wv+=' q'+F(-W/12)+' '+F(bh*0.5)+' '+F(-W/6)+' 0';g+='<rect y="'+F(HY)+'" width="'+W+'" height="'+F(H-HY)+'" fill="#fff" opacity=".3"/><path d="M0 '+F(HY-1)+' H'+W+' V'+F(HY+bh)+wv+'Z" fill="#fff" opacity=".8"/>'}
  if(SE==="autumn")g+='<rect y="'+F(HY)+'" width="'+W+'" height="'+F(H-HY)+'" fill="#e3a35a" opacity=".16"/>';
  g+=lk;
  if(V==="rainbow"||(SE==="winter"&&(T==="dawn"||V==="clear")))for(var gi=0;gi<10*fk;gi++)g+='<g transform="translate('+F(rnd(gi+1500)*W)+','+fy(0.66+rnd(gi+1510)*0.3)+') scale('+q.toFixed(2)+')"><path class="gd-glint" style="animation-delay:'+(rnd(gi+1520)*2).toFixed(2)+'s" d="M0 -3 L.7 -.7 L3 0 L.7 .7 L0 3 L-.7 .7 L-3 0 L-.7 -.7Z" fill="'+(V==="rainbow"?"#d9f1ff":"#fff")+'"/></g>';
  /* --- 草 --- */
  var shown=list.slice(opt.fs?-200:-90),gs=opt.fs?Math.min(1.6,q):1;
  shown.forEach(function(day,i){var h=csGrassHash(day+"#g"),x=8*gs+(h%1000)/1000*(W-28*gs),y=fy(0.62+((h>>>10)%1000)/1000*0.3),sc=(0.55+((h>>>20)%100)/100*0.25)*gs;
    g+='<g transform="translate('+F(x)+','+y+') scale('+sc.toFixed(2)+') translate(-20,-31)">'+CS_GRASS[csGrassKind(day)]+'</g>'});
  if(!n)g+='<text x="'+F(W/2)+'" y="'+fy(0.82)+'" text-anchor="middle" class="gd-empty"'+(opt.fs?' style="font-size:'+F(12*q)+'px"':'')+'>ここに草が生えていきます</text>';
  /* --- 季節の草花や小物 --- */
  var bz=fy(0.97);
  if(SE==="summer"&&!night)[[0.035,1],[0.1,0.8],[0.955,0.95]].forEach(function(c,k){var hh=36*c[1],pt="";for(var pa=0;pa<10;pa++)pt+='<ellipse rx="2.1" ry="4.8" cy="-4.8" transform="rotate('+pa*36+')"/>';
    g+='<g transform="translate('+F(W*c[0])+','+bz+') scale('+q.toFixed(2)+')"><g class="gd-sway" style="animation-delay:-'+k*1.3+'s"><path d="M0 0 Q3 '+F(-hh/2)+' 0 '+F(-hh)+'" fill="none" stroke="#4f8a3a" stroke-width="1.6"/><ellipse cx="3.5" cy="'+F(-hh*0.45)+'" rx="4" ry="1.8" transform="rotate(-25 3.5 '+F(-hh*0.45)+')" fill="#5d9a45"/><g transform="translate(0,'+F(-hh)+')" class="gd-sfh'+(T==="dusk"?" d":"")+'">'+pt+'<circle r="3.4" fill="#7a4a1e"/></g></g></g>'});
  if(SE==="autumn")[0.025,0.08,0.93,0.975].concat(opt.fs?[0.5]:[]).forEach(function(x,k){var ss="";for(var sj=0;sj<4;sj++){var bx=(sj-1.5)*3,tx2=(sj-1.5)*7+(k%2?3:-3);ss+='<path class="gd-ss" d="M'+bx+' 0 Q'+F(bx+tx2*0.3)+' -20 '+F(tx2)+' '+(-36-sj%2*5)+'"/><path class="gd-sp" d="M'+F(tx2)+' '+(-36-sj%2*5)+' q'+(tx2>0?4:-4)+' 4 '+(tx2>0?6:-6)+' 11"/>'}
    g+='<g transform="translate('+F(W*x)+','+bz+') scale('+q.toFixed(2)+')"><g class="gd-sway" style="animation-delay:-'+(k*0.9).toFixed(1)+'s">'+ss+'</g></g>'});
  if(SE==="autumn"&&night)g+='<g transform="translate('+F(W*0.16)+','+fy(0.93)+') scale('+q.toFixed(2)+')"><path d="M-9 0 L9 0 L7 -4 L-7 -4Z" fill="#c9a06a"/><path d="M-4 0 V4 M4 0 V4" stroke="#a37b48" stroke-width="1.5"/><g fill="#fbf7ea" stroke="#d8cfb4" stroke-width=".4"><circle cx="-5.6" cy="-6.6" r="2.8"/><circle cx="0" cy="-6.6" r="2.8"/><circle cx="5.6" cy="-6.6" r="2.8"/><circle cx="-2.8" cy="-11.4" r="2.8"/><circle cx="2.8" cy="-11.4" r="2.8"/><circle cx="0" cy="-16.2" r="2.8"/></g></g>';
  if(V==="snowman")g+='<g transform="translate('+F(W*0.14)+','+fy(0.86)+') scale('+q.toFixed(2)+')"><path d="M-6 -16 L-14 -21 M6 -16 L14 -22 M-12 -20 L-14 -23" stroke="#7a5a3a" stroke-width="1.1" fill="none"/><circle cy="-7" r="9" fill="#fff" stroke="#c9d6e0" stroke-width=".6"/><circle cy="-21" r="6.2" fill="#fff" stroke="#c9d6e0" stroke-width=".6"/><rect x="-4.5" y="-31" width="9" height="5" rx="1" fill="#3e5a8a"/><rect x="-6" y="-27" width="12" height="1.6" rx=".8" fill="#3e5a8a"/><circle cx="-2" cy="-22" r=".8" fill="#333"/><circle cx="2" cy="-22" r=".8" fill="#333"/><path d="M0 -20.5 L5 -19.5 L0 -19Z" fill="#f08a3a"/><path d="M-5 -15.5 Q0 -13 5 -15.5" stroke="#d2462c" stroke-width="2" fill="none"/></g>';
  /* 春は桜の枝(左上から)。夜は夜桜として明るく光らせるので、夜の暗さを重ねた後に描く */
  var saku="";if(SE==="spring"){var BP=[[6,4],[13,9],[22,12],[31,15],[42,19],[52,23],[29,23],[37,30],[46,13],[57,11],[18,18],[63,20]],bl="",gl="";
    BP.forEach(function(p,k){var r=3.6+((k*7)%4)*0.4;bl+='<g transform="translate('+p[0]+','+p[1]+')"><circle r="'+r.toFixed(1)+'" class="gd-sk"/><circle r="1.1" fill="#e0708f"/></g>';gl+='<circle cx="'+p[0]+'" cy="'+p[1]+'" r="7"/>'});
    saku='<g transform="scale('+(q*(opt.fs?1.6:1.15)).toFixed(2)+')">'+(night?'<g fill="#ffd3e2" opacity=".45" filter="url(#'+uid+'b)">'+gl+'</g>':'')+'<path d="M-2 -2 C14 10 30 14 54 22 M24 13 C30 22 34 28 40 32 M38 18 C44 14 52 12 60 10" fill="none" stroke="'+(night?"#4a3640":"#6b4a44")+'" stroke-width="2.2" stroke-linecap="round"/>'+bl+'</g>'}
  /* --- 舞うもの: 花びら(春)・落ち葉(秋の昼〜夕方だけ)・雪(冬) --- */
  var fx="",lit="",cnt=0,kind="";
  if(SE==="spring"){kind="petal";cnt={dawn:10,day:V==="fubuki"?40:16,dusk:12,night:10}[T]}
  else if(SE==="autumn"&&!night){kind="leaf";cnt={dawn:8,day:16,dusk:10}[T]}
  else if(SE==="winter"){kind="snow";cnt=V==="heavy"?40:V==="clear"?0:{dawn:0,day:12,dusk:10,night:16}[T]}
  for(var fi=0;fi<cnt*fk;fi++){var fxp=F(rnd(fi+200)*W),fyp=F(rnd(fi+300)*fy(0.9)),dl=(rnd(fi+400)*6).toFixed(2),du2=(5+rnd(fi+500)*5).toFixed(2),big=V==="heavy"?1.4:1;
    var shp=kind==="snow"?'<circle r="'+((1+rnd(fi+600)*1.4)*big).toFixed(2)+'" fill="#fff"/>':kind==="petal"?'<ellipse rx="3.4" ry="2.1" fill="'+(night?"#ffe3ec":"#f5a3bb")+'"/>':'<path d="M0 -3 Q3 0 0 3 Q-3 0 0 -3Z" fill="'+(fi%3===0?"#e9b23c":fi%2?"#e07a3a":"#c94f2c")+'"/>';
    var it='<g transform="translate('+fxp+','+fyp+') scale('+q.toFixed(2)+')"><g class="gd-fall'+(V==="fubuki"&&fi%2?" gd-fall2":"")+'" style="animation-delay:-'+dl+'s;animation-duration:'+du2+'s">'+shp+'</g></g>';
    if(kind==="petal"&&night)lit+=it;else fx+=it}
  /* --- 生きもの: ちょう(春夏の朝昼)・赤とんぼ(秋の昼と夕方)・ほたる(夏の夕方と夜) --- */
  var nb=SE==="spring"?(T==="day"?2:T==="dawn"?1:0):SE==="summer"&&T==="day"?1:0;
  for(var bf=0;bf<nb*fk;bf++){var bfc=["#f6c343","#ffffff","#f5a3bb"][bf%3];fx+='<g transform="translate('+F(W*(0.2+0.5*rnd(900+bf)))+','+fy(0.58+0.15*rnd(910+bf))+') scale('+(q*1.4).toFixed(2)+')"><g><animateMotion path="M0 0 C14 -16 30 6 44 -8 S30 -26 10 -14 S-12 4 0 0" dur="'+(10+bf*3)+'s" begin="-'+bf*2+'s" repeatCount="indefinite"/><g class="gd-bf" style="animation-delay:-'+(bf*0.1).toFixed(1)+'s"><path d="M0 0 C-5 -6 -8 -1 -5 2Z M0 0 C5 -6 8 -1 5 2Z" fill="'+bfc+'" stroke="#8a7a5a" stroke-width=".4"/></g><ellipse rx=".7" ry="2.4" fill="#5a4a3a"/></g></g>'}
  var nd=SE==="autumn"?(T==="day"?3:T==="dusk"?2:0):0;
  for(var dfi=0;dfi<nd*fk;dfi++)fx+='<g transform="translate('+F(W*(0.08+0.4*rnd(950+dfi)))+','+fy(0.4+0.2*rnd(960+dfi))+') scale('+q.toFixed(2)+')"><g><animateMotion path="M0 0 C30 -10 50 10 80 -4 S120 -12 140 0 S60 18 0 0" rotate="auto" dur="'+(12+dfi*4)+'s" begin="-'+(dfi*3)+'s" repeatCount="indefinite"/><g class="gd-df"><ellipse cx="1" cy="-3.4" rx="1.3" ry="3.4" fill="#fff" opacity=".65"/><ellipse cx="1" cy="3.4" rx="1.3" ry="3.4" fill="#fff" opacity=".65"/><ellipse cx="-1.4" cy="-3" rx="1.1" ry="3" fill="#fff" opacity=".55"/><ellipse cx="-1.4" cy="3" rx="1.1" ry="3" fill="#fff" opacity=".55"/></g><line x1="-7" y1="0" x2="4" y2="0" stroke="#d2462c" stroke-width="1.6" stroke-linecap="round"/><circle cx="4.4" r="1.3" fill="#b8341f"/></g></g>';
  var nff=SE==="summer"?(night?14:T==="dusk"?6:0):0;
  for(var ff=0;ff<nff*fk;ff++)lit+='<g transform="translate('+F(rnd(ff+1000)*W)+','+fy(0.5+rnd(ff+1010)*0.45)+')"><g class="gd-ff" style="animation-delay:-'+(rnd(ff+1020)*6).toFixed(2)+'s;animation-duration:'+(4+rnd(ff+1030)*4).toFixed(2)+'s"><circle r="'+F(4*q)+'" fill="#e8ff8a" opacity=".28"/><circle r="'+F(1.3*q)+'" fill="#f6ffb8"/></g></g>';
  /* 朝もや */
  if(V==="mist")[0.62,0.7,0.8].forEach(function(f,k){fx+='<g><animateTransform attributeName="transform" type="translate" values="0 0;'+F((k%2?-18:18)*u)+' 0;0 0" dur="'+(18+k*5)+'s" repeatCount="indefinite"/><ellipse cx="'+F(W*(0.3+k*0.2))+'" cy="'+fy(f)+'" rx="'+F(W*0.45)+'" ry="'+F(7*u)+'" fill="#fff" opacity=".4" filter="url(#'+uid+'c)"/></g>'});
  /* 時間帯の色: 夜は下ほど暗く(星空はそのまま)、朝夕はほんのり暖色 */
  if(night)fx+='<rect width="'+W+'" height="'+H+'" fill="url(#'+uid+'o)"/>';
  else if(low)fx+='<rect width="'+W+'" height="'+H+'" fill="#f08a4b" opacity=".08"/>';
  if(night)fx+=lit+saku;else fx=saku+fx+lit;
  return '<svg class="garden gd-'+SE+(night?" gd-n":"")+'" viewBox="0 0 '+W+' '+H+'" data-tod="'+T+'" data-season="'+SE+'" data-v="'+V+'" data-hy="'+F(HY)+'" data-u="'+u.toFixed(3)+'" data-lake="'+(st>=10?1:0)+'" role="img" aria-label="これまでに生えた草 '+n+'本('+csSkyLabel(SK)+'の庭)。タップすると演出が出ます">'+df+sk+g+fx+'</svg>'}
/* ==タップの演出: タップした場所に、季節と時間帯に合った演出を1つ出す。まれに四つ葉・小さな虹・流星群== */
var CS_NS="http://www.w3.org/2000/svg",csTapLast="";
function csTapPick(c){var r=Math.random();if(r<0.025)return "clover";if(r<0.045)return c.n?"meteor":c.season==="winter"?"crystal":"rainbow";
  var P=[],add=function(k,w){if(w>0&&k!==csTapLast)P.push([k,w])},sp=c.season==="spring",su=c.season==="summer",au=c.season==="autumn",wi=c.season==="winter",n=c.n,dy=c.tod==="day"||c.tod==="dawn",dk=c.tod==="dusk",sky=c.sky;
  add("sprout",sky?0:wi?1:3);add("flowers",sky?0:(sp||su)&&!n?3:au&&dy?1:0);add("butterfly",(sp||su)&&dy?3:0);add("birds",n?0:sky?3:1.5);add("sparkle",2);
  add("ladybug",!sky&&dy&&!wi?2:0);add("ripple",sky?0:c.lake||su?2:1);add("snowpuff",wi?(sky?2:3):0);add("leaves",au&&!n?3:0);add("fireflies",su&&(n||dk)?4:sp&&n?1:0);
  add("firework",su&&(n||dk)?(sky?4:2):0);add("shooting",n?(sky?3:1):0);add("petals",sp?3:0);add("dragonfly",au&&!n?3:su&&dy?1:0);add("notes",dy?1.2:0);
  add("fluff",(sp||su)&&!n?2:0);add("crystal",wi?(n?3:2):0);add("rabbit",au&&n?2:n?0.5:0);
  var t=0;P.forEach(function(p){t+=p[1]});var x=Math.random()*t;for(var i=0;i<P.length;i++){if(x<P[i][1])return P[i][0];x-=P[i][1]}return "sparkle"}
function csFxEl(L,x,y,s,html){var g=document.createElementNS(CS_NS,"g");g.setAttribute("transform","translate("+x.toFixed(1)+","+y.toFixed(1)+") scale("+s.toFixed(2)+")");g.innerHTML="<g>"+html+"</g>";L.appendChild(g);return g.firstChild}
function csAn(el,fr,d,dl,ez){try{el.animate(fr,{duration:d,delay:dl||0,easing:ez||"ease-out",fill:"both"})}catch(e){}}
function csTf(x,y,sc,r){return "translate("+x.toFixed(1)+"px,"+y.toFixed(1)+"px) rotate("+(r||0).toFixed(0)+"deg) scale("+(sc==null?1:sc)+")"}
var CS_TAPFX={
  sprout:function(L,x,y,s){var cl=["#5aa83c","#73c04f","#3f8f35"];for(var i=0;i<7;i++){var ox=(i-3)*4.5+(Math.random()-0.5)*3,hh=10+Math.random()*9,bd=(Math.random()-0.5)*8,e=csFxEl(L,x+ox*s,y,s,'<path d="M-1.4 0 Q'+(bd*0.4).toFixed(1)+' '+(-hh*0.6).toFixed(1)+' '+bd.toFixed(1)+' '+(-hh).toFixed(1)+' Q'+(bd*0.4+1.6).toFixed(1)+' '+(-hh*0.5).toFixed(1)+' 1.4 0Z" fill="'+cl[i%3]+'"/>'+(i===3?'<circle cx="'+bd.toFixed(1)+'" cy="'+(-hh).toFixed(1)+'" r="2.4" fill="#fff"/><circle cx="'+bd.toFixed(1)+'" cy="'+(-hh).toFixed(1)+'" r="1" fill="#f6c343"/>':''));
    csAn(e,[{transform:"scale(1,0)",opacity:1,offset:0},{transform:"scale(1,1.2)",opacity:1,offset:0.25},{transform:"scale(1,1)",opacity:1,offset:0.75},{transform:"scale(1,1)",opacity:0,offset:1}],1900,i*40,"cubic-bezier(.3,1.4,.5,1)")}return 2300},
  flowers:function(L,x,y,s,c){var P=c.season==="autumn"?["#f29bb8","#ffffff","#d96aa0"]:c.season==="summer"?["#f6c343","#ff9a5a","#8fc8ff"]:["#f5a3bb","#ffffff","#f6c343","#b9a3f0"];for(var i=0;i<7;i++){var a=i/7*Math.PI*2,r=16+Math.random()*8,col=P[i%P.length],pe="";for(var k=0;k<5;k++)pe+='<circle cx="'+(Math.cos(k*1.2566)*2.6).toFixed(1)+'" cy="'+(Math.sin(k*1.2566)*2.6).toFixed(1)+'" r="2.2" fill="'+col+'"/>';
    var e=csFxEl(L,x,y,s,pe+'<circle r="1.5" fill="#f2a53a"/>');csAn(e,[{transform:csTf(0,0,0.1,0),opacity:1},{transform:csTf(Math.cos(a)*r,Math.sin(a)*r*0.7-6,1.1,90),opacity:1,offset:0.4},{transform:csTf(Math.cos(a)*r*1.1,Math.sin(a)*r*0.7-2,1,140),opacity:1,offset:0.8},{transform:csTf(Math.cos(a)*r*1.1,Math.sin(a)*r*0.7+2,0.8,160),opacity:0}],1800,i*30)}return 2100},
  butterfly:function(L,x,y,s){var P=["#f6c343","#ffffff","#f5a3bb","#8fc8ff"];for(var i=0;i<3;i++){var dx=(Math.random()-0.5)*140,dy=-60-Math.random()*60,e=csFxEl(L,x,y,s,'<g class="gd-bf"><path d="M0 0 C-6 -7 -9 -1 -6 2.4Z M0 0 C6 -7 9 -1 6 2.4Z" fill="'+P[(i+Math.floor(Math.random()*4))%4]+'" stroke="#8a7a5a" stroke-width=".4"/></g><ellipse rx=".8" ry="2.6" fill="#5a4a3a"/>');
    csAn(e,[{transform:csTf(0,0,0.4),opacity:0},{transform:csTf(dx*0.2+10,dy*0.25,1),opacity:1,offset:0.15},{transform:csTf(dx*0.5-12,dy*0.5,1),opacity:1,offset:0.5},{transform:csTf(dx,dy,0.8),opacity:0}],2400,i*120,"ease-in-out")}return 2800},
  birds:function(L,x,y,s,c){var dir=x<c.W/2?1:-1,col=c.tod==="dusk"?"#2b2230":"#3a4a5a";for(var i=0;i<5;i++){var e=csFxEl(L,x+(Math.random()-0.5)*16*s,y+(Math.random()-0.5)*8*s,s,'<path class="gd-bird" style="animation-delay:-'+(i*0.1).toFixed(1)+'s" d="M-5 0 Q-2.5 -3.4 0 0 Q2.5 -3.4 5 0" fill="none" stroke="'+col+'" stroke-width="1.4" stroke-linecap="round"/>');
    csAn(e,[{transform:csTf(0,0,0.6),opacity:0},{transform:csTf(dir*10,-8,1),opacity:1,offset:0.12},{transform:csTf(dir*(90+i*14),-(50+i*12),0.6),opacity:0}],2100,i*90,"ease-in")}return 2600},
  sparkle:function(L,x,y,s,c){var P=c.n?["#fff","#fff3b0","#cfe3ff"]:["#fff","#ffe27a","#fff6c8"],st='<path d="M0 -4 L1 -1 L4 0 L1 1 L0 4 L-1 1 L-4 0 L-1 -1Z" fill="FILL"/>';csAn(csFxEl(L,x,y,s,'<circle r="10" fill="#fff" opacity=".7"/>'),[{transform:"scale(.2)",opacity:0.9},{transform:"scale(1.4)",opacity:0}],600);
    for(var i=0;i<10;i++){var a=i/10*Math.PI*2+Math.random()*0.3,r=18+Math.random()*14,e=csFxEl(L,x,y,s,st.replace("FILL",P[i%3]));csAn(e,[{transform:csTf(0,0,0.3,0),opacity:1},{transform:csTf(Math.cos(a)*r,Math.sin(a)*r,1,180),opacity:1,offset:0.6},{transform:csTf(Math.cos(a)*r*1.15,Math.sin(a)*r*1.15,0.4,260),opacity:0}],1200,i*20)}return 1500},
  ladybug:function(L,x,y,s){var dir=Math.random()<0.5?1:-1,e=csFxEl(L,x,y,s,'<g transform="scale('+dir+',1)"><g class="gd-walk"><circle cx="4.6" r="2" fill="#2b2b2b"/><path d="M-4.5 0 A4.5 4.5 0 0 1 4 0 A4.5 4.5 0 0 1 -4.5 0Z" transform="scale(1,.95)" fill="#d93a2b"/><path d="M-4.5 0 H4" stroke="#2b2b2b" stroke-width=".6"/><circle cx="-1.6" cy="-2" r=".9" fill="#2b2b2b"/><circle cx="1.6" cy="-2" r=".9" fill="#2b2b2b"/><circle cx="-1.8" cy="2" r=".9" fill="#2b2b2b"/><circle cx="1.6" cy="2.1" r=".9" fill="#2b2b2b"/></g></g>');
    csAn(e,[{transform:csTf(0,0,0.2),opacity:0},{transform:csTf(0,0,1.15),opacity:1,offset:0.1},{transform:csTf(dir*24,-3,1.15),opacity:1,offset:0.55},{transform:csTf(dir*44,2,1.15),opacity:1,offset:0.85},{transform:csTf(dir*52,0,1.15),opacity:0}],3200,0,"linear");return 3400},
  ripple:function(L,x,y,s){for(var i=0;i<3;i++){var e=csFxEl(L,x,y,s,'<ellipse rx="10" ry="3.6" fill="none" stroke="#e8f6ff" stroke-width="1.5" vector-effect="non-scaling-stroke"/>');csAn(e,[{transform:"scale(.2)",opacity:0.95},{transform:"scale(3)",opacity:0}],1500,i*260)}
    csAn(csFxEl(L,x,y,s,'<circle r="1.8" fill="#e8f6ff"/>'),[{transform:"translate(0px,0px)",opacity:1},{transform:"translate(0px,-12px)",opacity:1,offset:0.4},{transform:"translate(0px,0px)",opacity:0}],700);return 2200},
  snowpuff:function(L,x,y,s){for(var i=0;i<16;i++){var a=-Math.PI*Math.random(),r=12+Math.random()*16,e=csFxEl(L,x,y,s,'<circle r="'+(1+Math.random()*1.8).toFixed(1)+'" fill="#fff" stroke="#dce8f2" stroke-width=".3"/>');
    csAn(e,[{transform:csTf(0,0,0.5),opacity:1},{transform:csTf(Math.cos(a)*r,Math.sin(a)*r,1),opacity:1,offset:0.35},{transform:csTf(Math.cos(a)*r*1.3,Math.sin(a)*r+18,1),opacity:0}],1700,i*15,"cubic-bezier(.2,.7,.4,1)")}return 2000},
  leaves:function(L,x,y,s){var P=["#e07a3a","#c94f2c","#e9b23c","#b8452a"];for(var i=0;i<10;i++){var a0=Math.random()*Math.PI*2,fr=[],k;for(k=0;k<=4;k++){var a=a0+k*1.5,r=4+k*7;fr.push({transform:csTf(Math.cos(a)*r,Math.sin(a)*r*0.5-k*10,1,k*120),opacity:k===4?0:1})}
    csAn(csFxEl(L,x,y,s,'<path d="M0 -3.4 Q3.4 0 0 3.4 Q-3.4 0 0 -3.4Z" fill="'+P[i%4]+'"/>'),fr,2100,i*40,"ease-in-out")}return 2500},
  fireflies:function(L,x,y,s){for(var i=0;i<9;i++){var dx=(Math.random()-0.5)*70,dy=-10-Math.random()*45,e=csFxEl(L,x,y,s,'<circle r="4" fill="#e8ff8a" opacity=".3"/><circle r="1.4" fill="#f6ffb8"/>');
    csAn(e,[{transform:csTf(0,0,0.4),opacity:0},{transform:csTf(dx*0.3,dy*0.3,1),opacity:1,offset:0.2},{transform:csTf(dx*0.6,dy*0.6,1),opacity:0.25,offset:0.45},{transform:csTf(dx*0.8,dy*0.8,1),opacity:1,offset:0.7},{transform:csTf(dx,dy,1),opacity:0}],2800,i*80,"ease-in-out")}return 3300},
  firework:function(L,x,y,s,c){var P=["#ffd36b","#ff7aa8","#8fd3ff","#b6f28a","#ffb36b"],c1=P[Math.floor(Math.random()*5)],c2=P[Math.floor(Math.random()*5)],by=c.sky?y:Math.max(12*s,y-60*s),sy=Math.min(c.H-2,by+70*s);
    csAn(csFxEl(L,x,sy,s,'<circle r="1.3" fill="#fff3c0"/><line y1="0" y2="8" stroke="#fff3c0" stroke-width=".8" opacity=".6"/>'),[{transform:"translate(0px,0px)",opacity:1},{transform:"translate(0px,"+((by-sy)/s).toFixed(1)+"px)",opacity:1,offset:0.95},{transform:"translate(0px,"+((by-sy)/s).toFixed(1)+"px)",opacity:0}],450,0,"ease-out");
    csAn(csFxEl(L,x,by,s,'<circle r="5" fill="#fff3c0"/>'),[{transform:"scale(.2)",opacity:0},{transform:"scale(1.2)",opacity:0.9,offset:0.3},{transform:"scale(1.6)",opacity:0}],600,430);
    for(var i=0;i<20;i++){var a=i/20*Math.PI*2,r=(i%2?20:28),e=csFxEl(L,x,by,s,'<circle r="1.5" fill="'+(i%2?c1:c2)+'"/>');csAn(e,[{transform:csTf(0,0,0.5),opacity:0},{transform:csTf(Math.cos(a)*r*0.3,Math.sin(a)*r*0.3,1),opacity:1,offset:0.1},{transform:csTf(Math.cos(a)*r,Math.sin(a)*r,1),opacity:1,offset:0.55},{transform:csTf(Math.cos(a)*r*1.08,Math.sin(a)*r+10,0.6),opacity:0}],1500,450,"cubic-bezier(.1,.8,.3,1)")}return 2200},
  shooting:function(L,x,y,s){var id="t"+Math.floor(Math.random()*1e9),e=csFxEl(L,x,y,s,'<defs><linearGradient id="'+id+'" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="-40" y2="0"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient></defs><g transform="rotate(26)"><g class="gd-sh"><line x1="0" x2="-40" stroke="url(#'+id+')" stroke-width="2" stroke-linecap="round"/><circle r="1.8" fill="#fff"/></g></g>');
    csAn(e.querySelector(".gd-sh"),[{transform:"translate(-20px,0px)",opacity:0},{transform:"translate(10px,0px)",opacity:1,offset:0.2},{transform:"translate(110px,0px)",opacity:0}],1100,0,"ease-in");return 1400},
  petals:function(L,x,y,s,c){for(var i=0;i<12;i++){var a=Math.random()*Math.PI*2,r=10+Math.random()*14,e=csFxEl(L,x,y,s,'<ellipse rx="3.4" ry="2.1" fill="'+(c.n?"#ffe3ec":i%3?"#f5a3bb":"#fbd0dc")+'"/>');
    csAn(e,[{transform:csTf(0,0,0.4,0),opacity:1},{transform:csTf(Math.cos(a)*r,Math.sin(a)*r-12,1,120),opacity:1,offset:0.3},{transform:csTf(Math.cos(a)*r+18,Math.sin(a)*r+16,1,320),opacity:0}],2300,i*25,"ease-out")}return 2600},
  dragonfly:function(L,x,y,s){var dir=Math.random()<0.5?1:-1,e=csFxEl(L,x,y,s,'<g transform="scale('+dir+',1)"><g class="gd-df"><ellipse cx="1" cy="-3.6" rx="1.4" ry="3.6" fill="#fff" opacity=".7"/><ellipse cx="1" cy="3.6" rx="1.4" ry="3.6" fill="#fff" opacity=".7"/><ellipse cx="-1.5" cy="-3.2" rx="1.2" ry="3.2" fill="#fff" opacity=".6"/><ellipse cx="-1.5" cy="3.2" rx="1.2" ry="3.2" fill="#fff" opacity=".6"/></g><line x1="-8" x2="4" stroke="#d2462c" stroke-width="1.8" stroke-linecap="round"/><circle cx="4.6" r="1.5" fill="#b8341f"/></g>');
    csAn(e,[{transform:csTf(0,6,0.4),opacity:0},{transform:csTf(0,-6,1.1),opacity:1,offset:0.15},{transform:csTf(dir*5,-9,1.1),opacity:1,offset:0.4},{transform:csTf(-dir*2,-7,1.1),opacity:1,offset:0.55},{transform:csTf(dir*170,-50,1.1),opacity:0}],2400,0,"ease-in-out");return 2700},
  notes:function(L,x,y,s){var P=["#e0708f","#4f8fd0","#5aa83c","#e9a23c"],N=["♪","♫","♪"];for(var i=0;i<3;i++){var e=csFxEl(L,x+(i-1)*8*s,y,s,'<text font-size="12" text-anchor="middle" fill="'+P[(i+Math.floor(Math.random()*4))%4]+'" stroke="#fff" stroke-width="2" paint-order="stroke" font-weight="700">'+N[i]+'</text>');
    csAn(e,[{transform:csTf(0,0,0.5,-10),opacity:0},{transform:csTf(-6,-14,1,8),opacity:1,offset:0.3},{transform:csTf(6,-28,1,-8),opacity:1,offset:0.65},{transform:csTf(-2,-42,0.9,4),opacity:0}],1900,i*180,"ease-in-out")}return 2500},
  fluff:function(L,x,y,s){var head="";for(var k=0;k<14;k++){var a=k/14*Math.PI*2;head+='<line x2="'+(Math.cos(a)*5).toFixed(1)+'" y2="'+(Math.sin(a)*5).toFixed(1)+'" stroke="#fff" stroke-width=".6"/>'}
    var h=csFxEl(L,x,y,s,'<path d="M0 0 V14" stroke="#7aa65a" stroke-width="1"/><circle r="5.4" fill="#fff" opacity=".55"/>'+head);csAn(h,[{transform:"translate(0px,-14px) scale(.2)",opacity:0},{transform:"translate(0px,-14px) scale(1)",opacity:1,offset:0.15},{transform:"translate(0px,-14px) scale(1)",opacity:1,offset:0.6},{transform:"translate(0px,-14px) scale(1)",opacity:0}],2400);
    for(var i=0;i<10;i++){var dx=20+Math.random()*60,dy=-30-Math.random()*50,e=csFxEl(L,x,y-14*s,s,'<path d="M0 0 V4" stroke="#d9cfb0" stroke-width=".5"/><path d="M0 0 L-2.2 -2.2 M0 0 L0 -3 M0 0 L2.2 -2.2" stroke="#fff" stroke-width=".6"/>');
    csAn(e,[{transform:csTf(0,0,1,0),opacity:0},{transform:csTf(2,-2,1,0),opacity:1,offset:0.2},{transform:csTf(dx*0.5,dy*0.4,1,15),opacity:1,offset:0.55},{transform:csTf(dx,dy,1,-10),opacity:0}],2600,400+i*60,"ease-in-out")}return 3400},
  crystal:function(L,x,y,s){var arm="";for(var k=0;k<6;k++)arm+='<g transform="rotate('+k*60+')"><path d="M0 0 V-11 M0 -5 L-3 -8 M0 -5 L3 -8 M0 -8 L-2 -10 M0 -8 L2 -10" stroke="#fff" stroke-width="1.1" stroke-linecap="round" fill="none"/></g>';
    csAn(csFxEl(L,x,y,s,'<circle r="13" fill="#cfe8ff" opacity=".16"/>'+arm),[{transform:"scale(.1) rotate(0deg)",opacity:0},{transform:"scale(1.1) rotate(60deg)",opacity:1,offset:0.3},{transform:"scale(1) rotate(90deg)",opacity:1,offset:0.7},{transform:"scale(1.2) rotate(120deg)",opacity:0}],1900,0,"ease-out");
    return CS_TAPFX.sparkle(L,x,y,s*0.8,{n:true})},
  rabbit:function(L,x,y,s){var dir=Math.random()<0.5?1:-1,e=csFxEl(L,x,y,s,'<g transform="scale('+(-dir)+',1)"><ellipse cx="2" cy="-4" rx="6" ry="4.4" fill="#fbfbf6"/><circle cx="-4" cy="-8" r="3.4" fill="#fbfbf6"/><ellipse cx="-4.4" cy="-14" rx="1.2" ry="4" transform="rotate(-10 -4.4 -14)" fill="#fbfbf6"/><ellipse cx="-2.4" cy="-14" rx="1.2" ry="4" transform="rotate(12 -2.4 -14)" fill="#fbfbf6"/><circle cx="7.6" cy="-5" r="1.6" fill="#fff"/><circle cx="-5.4" cy="-8.4" r=".6" fill="#c0475e"/></g>'),fr=[],k;
    for(k=0;k<=6;k++)fr.push({transform:csTf(dir*k*12,k%2?-12:0,1),opacity:k===0?0:k===6?0:1});csAn(e,fr,2600,0,"linear");return 2800},
  clover:function(L,x,y,s,c){var lf="";for(var k=0;k<4;k++)lf+='<path transform="rotate('+(k*90+45)+')" d="M0 0 C-6 -4 -7 -11 -2.6 -11 C-1 -11 0 -9.4 0 -8.4 C0 -9.4 1 -11 2.6 -11 C7 -11 6 -4 0 0Z" fill="#43a347" stroke="#2e7a34" stroke-width=".6"/>';
    csAn(csFxEl(L,x,y,s,'<circle r="22" fill="#fff4b0" opacity=".55"/>'),[{transform:"scale(.2)",opacity:0},{transform:"scale(1.2)",opacity:0.8,offset:0.3},{transform:"scale(1.4)",opacity:0}],2600);
    csAn(csFxEl(L,x,y,s,'<path d="M0 0 Q2 8 1 14" stroke="#2e7a34" stroke-width="1.4" fill="none"/>'+lf),[{transform:"scale(.1) rotate(-90deg)",opacity:0},{transform:"scale(1.3) rotate(10deg)",opacity:1,offset:0.25},{transform:"scale(1.2) rotate(0deg)",opacity:1,offset:0.8},{transform:"scale(1.2) rotate(0deg)",opacity:0}],3400,0,"cubic-bezier(.3,1.4,.5,1)");
    csTapLabel(L,x,y-24*s,s,"四つ葉のクローバー！",c);CS_TAPFX.sparkle(L,x,y,s*1.3,c);return 3600},
  rainbow:function(L,x,y,s,c){var a="";[["#f08a8a",22],["#f2c94c",18],["#7cc5f0",14]].forEach(function(r){a+='<path d="M'+(-r[1])+' 0 A'+r[1]+' '+r[1]+' 0 0 1 '+r[1]+' 0" fill="none" stroke="'+r[0]+'" stroke-width="3.4" stroke-linecap="round" pathLength="1" stroke-dasharray="1" class="gd-rbd"/>'});
    var e=csFxEl(L,x,y,s,a);e.querySelectorAll(".gd-rbd").forEach(function(p,i){csAn(p,[{strokeDashoffset:1},{strokeDashoffset:0}],900,i*120,"ease-out")});csAn(e,[{opacity:1,offset:0},{opacity:1,offset:0.75},{opacity:0,offset:1}],3000);
    csTapLabel(L,x,y-30*s,s,"小さな虹",c);return 3200},
  meteor:function(L,x,y,s,c){for(var i=0;i<7;i++)(function(i){setTimeout(function(){if(L.isConnected)CS_TAPFX.shooting(L,x+(Math.random()-0.6)*90*s,y+(Math.random()-0.6)*40*s,s*(0.7+Math.random()*0.5))},i*230)})(i);csTapLabel(L,x,y-22*s,s,"流星群",c);return 3200}};
function csTapLabel(L,x,y,s,t,c){var e=csFxEl(L,x,Math.max(14*s,y),s,'<text class="gd-fxl'+(c&&c.n?" n":"")+'" text-anchor="middle">'+t+'</text>');csAn(e,[{transform:"translate(0px,6px)",opacity:0},{transform:"translate(0px,0px)",opacity:1,offset:0.15},{transform:"translate(0px,-2px)",opacity:1,offset:0.8},{transform:"translate(0px,-6px)",opacity:0}],3000)}
function csGardenTap(sv,e,force){try{var vb=sv.viewBox.baseVal,m=sv.getScreenCTM();if(!m||!vb)return;var pt=sv.createSVGPoint();pt.x=e.clientX;pt.y=e.clientY;pt=pt.matrixTransform(m.inverse());
  var W=vb.width,H=vb.height,x=Math.max(6,Math.min(W-6,pt.x)),y=Math.max(6,Math.min(H-4,pt.y)),u=+sv.getAttribute("data-u")||1,s=Math.min(1.8,Math.sqrt(u));
  var c={tod:sv.getAttribute("data-tod"),season:sv.getAttribute("data-season"),n:sv.getAttribute("data-tod")==="night",sky:y<(+sv.getAttribute("data-hy")||H*0.64)-4,lake:sv.getAttribute("data-lake")==="1",W:W,H:H};
  var k=force&&CS_TAPFX[force]?force:csTapPick(c);csTapLast=k;
  var ls=sv.querySelectorAll(".gd-tapfx");if(ls.length>6)ls[0].remove();
  var L=document.createElementNS(CS_NS,"g");L.setAttribute("class","gd-tapfx");L.setAttribute("data-fx",k);sv.appendChild(L);
  var d=CS_TAPFX[k](L,x,y,s,c)||2500;setTimeout(function(){L.remove()},d+300);return k}catch(x){}}
/* ==全画面: 画面の縦横比で庭を描き直す。×・Esc・ブラウザの戻るで閉じる== */
var csFS=null,CS_FSI='<svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 9V4h5M20 9V4h-5M4 15v5h5M20 15v5h-5"/></svg>';
function csGardenWrap(svg){return '<div class="gd-wrap">'+svg+'<button type="button" class="gd-fsb" aria-label="草の庭を全画面で見る" title="全画面で見る">'+CS_FSI+'</button></div>'}
function csFSDraw(){if(!csFS)return;var list=window.__csGardenList||[],vw=window.innerWidth||390,vh=window.innerHeight||700,k=Math.max(1,vw/900),W=Math.round(vw/k),H=Math.round(vh/k),n=list.length,st=csStage(n);
  csFS.w=vw;csFS.h=vh;csFS.el.innerHTML=csGardenSVG(list,W,H,{fs:1})+'<button type="button" class="gd-fs-x" aria-label="全画面を閉じる"><svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg></button><p class="gd-fs-cap"><b>'+CS_STAGES[st][1]+'<span>草 '+n+'本</span></b><span>'+csSkyLabel(csSkyNow())+'</span><small>庭をタップすると、いろいろな演出が出ます</small></p>'}
function csGardenFS(btn){if(csFS)return;var o=document.createElement("div");o.className="gd-fs";o.setAttribute("role","dialog");o.setAttribute("aria-modal","true");o.setAttribute("aria-label","草の庭(全画面)");
  csFS={el:o,btn:btn,hist:false,ov:document.documentElement.style.overflow};document.body.appendChild(o);csFSDraw();document.documentElement.style.overflow="hidden";
  try{history.pushState({gdfs:1},"");csFS.hist=true}catch(x){}
  try{o.querySelector(".gd-fs-x").focus({preventScroll:true})}catch(x){}requestAnimationFrame(function(){o.classList.add("on")})}
function csGardenFSClose(fromPop){if(!csFS)return;var f=csFS;csFS=null;document.documentElement.style.overflow=f.ov||"";f.el.remove();if(f.hist&&!fromPop){try{history.back()}catch(x){}}try{f.btn&&f.btn.focus({preventScroll:true})}catch(x){}}
(function(){var rt=0;
  document.addEventListener("click",function(e){var t=e.target;if(!t||!t.closest)return;var b=t.closest(".gd-fsb");if(b){e.preventDefault();e.stopPropagation();csGardenFS(b);return}
    if(t.closest(".gd-fs-x")){e.preventDefault();csGardenFSClose();return}var sv=t.closest("svg.garden");if(sv)csGardenTap(sv,e)});
  document.addEventListener("keydown",function(e){if(e.key==="Escape"&&csFS){e.preventDefault();csGardenFSClose()}});
  window.addEventListener("popstate",function(){if(csFS)csGardenFSClose(true)});
  window.addEventListener("resize",function(){if(!csFS)return;clearTimeout(rt);rt=setTimeout(function(){if(csFS&&(Math.abs(csFS.w-window.innerWidth)>30||Math.abs(csFS.h-window.innerHeight)>60))csFSDraw()},200)})})();
function csGarden(el,s){try{if(!el||!s)return;var list=csGardenDays(s.days),n=list.length,st=csStage(n),nx=CS_STAGES[st+1];window.__csGardenList=list;
  el.innerHTML='<p class="bx-k">草の庭<span>'+n+'本</span></p>'+csGardenWrap(csGardenSVG(list,340,150))+'<p class="gd-st"><b>'+CS_STAGES[st][1]+'</b>'+(nx?'<small>あと'+(nx[0]-n)+'本で「'+nx[1]+'」</small>':'<small>最高の段階です</small>')+'</p><a class="bx-go" href="/record/#garden-d">草の庭をくわしく見る</a>'}catch(e){}}
function csGardenDetail(days){try{var el=document.getElementById("garden-detail");if(!el)return;var list=csGardenDays(days),n=list.length,st=csStage(n),cur=CS_STAGES[st],nx=CS_STAGES[st+1];window.__csGardenList=list;
  var pct=nx?Math.round((n-cur[0])/(nx[0]-cur[0])*100):100,cnt=[0,0,0,0,0,0,0,0,0];list.forEach(function(d){cnt[csGrassKind(d)]++});
  var h=csGardenWrap(csGardenSVG(list,340,190))+'<div class="gd-now"><b>'+cur[1]+'</b><span>'+cur[2]+'</span></div>';
  h+='<div class="gd-prog"><div class="l"><span>'+(nx?'次の段階「'+nx[1]+'」まで':'最高の段階')+'</span><span>'+n+(nx?' / '+nx[0]:'')+'本</span></div><div class="bar"><i style="width:'+Math.max(0,Math.min(100,pct))+'%"></i></div></div>';
  h+='<p class="gd-h">生えた草の種類</p><ul class="gd-kinds">'+CS_GNAMES.map(function(nm,k){return '<li class="'+(cnt[k]?"":"z")+'"><svg viewBox="0 0 40 40" aria-hidden="true"><circle cx="20" cy="20" r="19" class="gs-bg"/>'+CS_GRASS[k]+'</svg><span>'+nm+'</span><b>'+cnt[k]+'</b></li>'}).join("")+'</ul>';
  h+='<p class="gd-h">育ち方</p><ol class="gd-steps">'+CS_STAGES.map(function(x,i){return '<li class="'+(i<=st?"on":"")+(i===st?" cur":"")+'"><b>'+x[0]+'本〜</b>'+x[1]+'</li>'}).join("")+'</ol><p class="bx-s">1節読むか1問解いた日に、草が1本生えます。さらに、これまでに解いた問題10問ごとに1本、勉強時間30分ごとに1本生えます。草の種類はランダムに決まり、まれに四つ葉のクローバーが生えます。空は季節と時間帯で変わり、日によって虹や流れ星などが見られます。右上のボタンで全画面になり、庭をタップすると演出が出ます。</p>';
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
.garden{display:block;width:100%;height:auto;border-radius:12px;overflow:hidden;cursor:pointer;touch-action:manipulation;-webkit-tap-highlight-color:transparent;-webkit-user-select:none;user-select:none}
.garden .gd-sky{fill:color-mix(in srgb,#bfe3f5 55%,var(--paper))}
.garden .gd-star{fill:#fff;animation:gdTw 3s ease-in-out infinite alternate}
@keyframes gdTw{from{opacity:.35}to{opacity:1}}
.garden .gd-cu{fill:#fff;opacity:.9}.garden .gd-cud{fill:#ffe0cc}
.garden .gd-fall{animation:gdFall 7s linear infinite}
.garden .gd-fall2{animation-name:gdFall2}
@keyframes gdFall{0%{transform:translate(0,-30px) rotate(0)}50%{transform:translate(6px,15px) rotate(140deg)}100%{transform:translate(-4px,60px) rotate(300deg);opacity:0}}
@keyframes gdFall2{0%{transform:translate(-30px,-24px) rotate(0)}50%{transform:translate(20px,10px) rotate(160deg)}100%{transform:translate(70px,44px) rotate(340deg);opacity:0}}
.garden .gd-ground{fill:color-mix(in srgb,#9fd27a 55%,var(--paper))}
.garden .gd-hill{fill:color-mix(in srgb,#7cc35a 60%,var(--paper))}
.garden .gd-mt{fill:color-mix(in srgb,#4f9a4a 75%,var(--paper))}
.garden .gd-mt2{fill:color-mix(in srgb,#3d7f3c 70%,var(--paper))}
.garden .gd-tree{fill:#2f7a3b}
.garden .gd-trunk{fill:#7a5a3a}
.garden .gd-lake{fill:#6fb6e8;opacity:.85}
.garden.gd-autumn .gd-hill{fill:color-mix(in srgb,#cfa24e 60%,var(--paper))}
.garden.gd-autumn .gd-mt{fill:color-mix(in srgb,#b8743f 75%,var(--paper))}
.garden.gd-autumn .gd-mt2{fill:color-mix(in srgb,#9a5a36 70%,var(--paper))}
.garden.gd-autumn .gd-tree{fill:#c4572b}
.garden.gd-winter .gd-hill{fill:color-mix(in srgb,#e4edf2 85%,var(--paper))}
.garden.gd-winter .gd-mt{fill:color-mix(in srgb,#c3d4df 85%,var(--paper))}
.garden.gd-winter .gd-mt2{fill:color-mix(in srgb,#aec2d0 85%,var(--paper))}
.garden.gd-winter .gd-tree{fill:#3e6f55}
.garden.gd-winter .gd-lake{fill:#cfe6f2}
.garden .gd-rb{fill:none;stroke-width:4;opacity:.55}
.garden .gd-rbv{opacity:.32}
.garden .gd-rb1{stroke:#f08a8a}
.garden .gd-rb2{stroke:#f2c94c}
.garden .gd-rb3{stroke:#7cc5f0}
.garden .gd-cloud{fill:#fff;opacity:.75}
.garden .gd-sun{fill:#f6c343}
.garden .gd-empty{font-size:12px;fill:var(--sub)}
.garden .gd-shoot{opacity:0;animation:gdShoot 8s linear infinite}
@keyframes gdShoot{0%{transform:translate(-10px,0);opacity:0}2%{opacity:1}11%{transform:translate(70px,0);opacity:0}100%{transform:translate(70px,0);opacity:0}}
.garden .gd-fw{opacity:0;animation:gdFw 4.2s ease-out infinite}
@keyframes gdFw{0%{transform:scale(.15);opacity:0}6%{opacity:1}35%{transform:scale(1);opacity:.85}55%{transform:scale(1.08);opacity:0}100%{transform:scale(1.08);opacity:0}}
.garden .gd-au{animation:gdAu 6s ease-in-out infinite alternate}
@keyframes gdAu{from{transform:translateX(-8px);opacity:.28}to{transform:translateX(8px);opacity:.6}}
.garden .gd-dc{fill:#fff;opacity:.85}.garden.gd-n .gd-dc{fill:#59648a;opacity:.7}
.garden .gd-bird,.garden .gd-tapfx .gd-bird{animation:gdFlap .34s ease-in-out infinite alternate}
@keyframes gdFlap{from{transform:scaleY(1)}to{transform:scaleY(-.5)}}
.garden .gd-bf{animation:gdBf .22s ease-in-out infinite alternate}
@keyframes gdBf{from{transform:scaleX(1)}to{transform:scaleX(.25)}}
.garden .gd-df{animation:gdDf .12s linear infinite alternate}
@keyframes gdDf{from{opacity:1}to{opacity:.45}}
.garden .gd-ff{animation:gdFf 6s ease-in-out infinite alternate}
@keyframes gdFf{0%{opacity:.1;transform:translate(0,0)}30%{opacity:1}50%{transform:translate(6px,-8px);opacity:.9}70%{opacity:.2}100%{opacity:.85;transform:translate(-5px,-3px)}}
.garden .gd-sway{animation:gdSway 4s ease-in-out infinite alternate}
@keyframes gdSway{from{transform:rotate(-3deg)}to{transform:rotate(3deg)}}
.garden .gd-bob{animation:gdBob 3s ease-in-out infinite alternate}
@keyframes gdBob{from{transform:translateY(-2px)}to{transform:translateY(2px)}}
.garden .gd-glint{animation:gdGl 2.2s ease-in-out infinite alternate}
@keyframes gdGl{from{opacity:0;transform:scale(.4)}to{opacity:1;transform:scale(1)}}
.garden .gd-walk{animation:gdBob .25s linear infinite alternate}
.garden .gd-sfh{fill:#f6c343}.garden .gd-sfh.d{fill:#e8a83a}
.garden .gd-sk{fill:#f8c3d3}.garden.gd-n .gd-sk{fill:#ffdce8}
.garden .gd-ss{fill:none;stroke:#b39d62;stroke-width:1.1;stroke-linecap:round}.garden .gd-sp{fill:none;stroke:#efe0b6;stroke-width:3;stroke-linecap:round}
.garden.gd-n .gd-ss{stroke:#4f587a}.garden.gd-n .gd-sp{stroke:#d6daee}
.garden .gd-tapfx{pointer-events:none}
.garden .gd-fxl{font-size:9px;font-weight:800;fill:#2b3a33;stroke:#fff;stroke-width:3px;paint-order:stroke;stroke-linejoin:round}
.garden .gd-fxl.n{fill:#fff;stroke:#1b2440}
.gd-wrap{position:relative}
.gd-fsb{position:absolute;top:8px;right:8px;width:36px;height:36px;border-radius:50%;border:0;padding:0;display:grid;place-items:center;background:rgba(255,255,255,.8);color:#26372e;box-shadow:0 1px 4px rgba(0,0,0,.2);cursor:pointer;-webkit-backdrop-filter:blur(4px);backdrop-filter:blur(4px)}
.gd-fsb:hover{background:#fff}.gd-fsb:focus-visible{outline:2px solid var(--ok,#2a9765);outline-offset:2px}
.gd-fs{position:fixed;inset:0;z-index:9000;background:#0b1630;opacity:0;transition:opacity .25s ease}
.gd-fs.on{opacity:1}
.gd-fs .garden{width:100%;height:100%;border-radius:0}
.gd-fs-x{position:absolute;top:calc(12px + env(safe-area-inset-top));right:calc(12px + env(safe-area-inset-right));width:44px;height:44px;border-radius:50%;border:0;padding:0;display:grid;place-items:center;background:rgba(255,255,255,.85);color:#1f2a24;box-shadow:0 2px 8px rgba(0,0,0,.25);cursor:pointer}
.gd-fs-x:focus-visible{outline:2px solid #fff;outline-offset:2px}
.gd-fs-cap{position:absolute;left:calc(12px + env(safe-area-inset-left));bottom:calc(12px + env(safe-area-inset-bottom));margin:0;max-width:calc(100% - 24px);box-sizing:border-box;padding:8px 12px;border-radius:12px;background:rgba(255,255,255,.86);color:#1f2a24;display:flex;flex-direction:column;gap:1px;font-size:12.5px;line-height:1.45;pointer-events:none;box-shadow:0 2px 8px rgba(0,0,0,.18)}
.gd-fs-cap b{font-size:15px}.gd-fs-cap b span{font-weight:600;font-size:12.5px;margin-left:8px;color:#4a5a52}.gd-fs-cap small{color:#4a5a52;font-size:11.5px}
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
