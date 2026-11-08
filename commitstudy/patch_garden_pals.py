"""草の庭に「庭の仲間」(達成した成果でやって来る小さな生きもの)を追加する。
  - 23種類。合格した科目(7科目それぞれ)・庭の段階・連続学習・学習した日数・解いた問題数・覚えた用語カード・勉強時間・バッジで仲間になる
    (どれも、すでにある記録 = 日ごとの記録・cs-subj-passed・cs-term-known-v1・ls-badges-v1 から数える)
  - 仲間になった中から、最大10匹をランダムに選んで庭に出す(ページを開くたびに選び直す)。庭のカード・学習の記録の庭・全画面のどれにも出る
  - 歩く・跳ねる・きょろきょろする・座る。夜は眠って「z」を出し、冬はマフラーを巻く。タップすると跳ねて、名前とひとことを出す(庭の演出は出さない)
  - 学習の記録の草の庭と全画面に「庭の仲間」の一覧(まだの仲間はシルエットと条件・あと何問など)
  - 新しい仲間が来たら、ホームの草の庭カード(または学習の記録の草の庭)に1回だけお知らせを出す。お知らせ済みは cs-pals-seen(アカウントに同期)
  テスト用: window.__csPalAll=1 ですべての仲間を出せる候補にする
使い方: python3 patch_garden_pals.py <index.html> <出力>   (patch_garden.py の後に当てる)
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
/* ==庭の仲間: 達成した成果で生きものが庭にやって来る。最大10匹をランダムに表示== */
var CS_PALS_MAX=10,CS_PALSEEN="cs-pals-seen";
var CS_PALS=[
 {id:"mebuki",nm:"めぶき",pf:"最初の草といっしょに生まれた芽の子。頭の双葉がごきげんのしるし",c:["grass",1],ct:"草を1本生やす",ln:["きょうも のびのび","おひさま すき","いっしょに育とうね"]},
 {id:"koron",nm:"ころん",pf:"庭のすみで見つかった小石の子。のんびり屋で、こけの帽子がお気に入り",c:["q",1],ct:"問題を1問解く",ln:["ころころ…","あわてない あわてない","1問ずつね"]},
 {id:"fumi",nm:"ふみ",pf:"しおりのリボンを付けたおもちの子。読みかけのページを覚えている",c:["r",1],ct:"テキストを1節読む",ln:["つづきは ここから","よみもの だいすき","ふむふむ"]},
 {id:"mittsun",nm:"みっつん",pf:"まんまるが3つつながったいも虫の子。3日続くと、ひとつ増えた気がする",c:["best",3],ct:"3日続けて学習する",ln:["にょきにょき","みっか つづいたね","いち、に、さん！"]},
 {id:"hidamari",nm:"ひだまり",pf:"1週間ぶんのおひさまを集めた子。そばにいると、ぽかぽかする",c:["best",7],ct:"7日続けて学習する",ln:["ぽかぽか〜","1週間えらい！","ひなたぼっこしよ"]},
 {id:"donguri",nm:"どんぐりん",pf:"草の庭に転がってきたどんぐりの子。帽子をほめられると照れる",c:["grass",15],ct:"庭を「草の庭」(草15本)まで育てる",ln:["ぼうし にあう？","ころがってきたよ","庭、ひろくなったね"]},
 {id:"hanamaru",nm:"はなまる",pf:"花の庭で咲いた花の子。がんばった日は花びらが1枚ふえる",c:["grass",30],ct:"庭を「花の庭」(草30本)まで育てる",ln:["はなまる あげる！","いいにおい","さいたよ〜"]},
 {id:"poko",nm:"ぽこ",pf:"丘のふもとに生えたきのこの子。雨の次の日は、ちょっと背がのびる",c:["grass",60],ct:"庭を「小さな丘」(草60本)まで育てる",ln:["ぽこっ","しめった土がすき","にょきっとね"]},
 {id:"yamabiko",nm:"やまびこ",pf:"草の山から下りてきた山の子。呼ぶと同じことばで返してくれる",c:["grass",100],ct:"庭を「草の山」(草100本)まで育てる",ln:["やっほー！","…やっほー…","てっぺん みえた？"]},
 {id:"fuwawa",nm:"ふわわ",pf:"30日ぶんの空から下りてきた雲の子。ねむくなると少し小さくなる",c:["days",30],ct:"学習した日を30日にする",ln:["ふわ〜","空からきたの","30日、すごいね"]},
 {id:"mameta",nm:"まめた",pf:"答えを1つずつ覚えて芽を出した豆の子。頭の芽がくるん",c:["q",100],ct:"問題を100問解く",ln:["まめに がんばる！","100問だよ","め、でたよ"]},
 {id:"ichimochi",nm:"いちもち",pf:"500問のごほうびにやって来た、いちごをのせたおもちの子",c:["q",500],ct:"問題を500問解く",ln:["あまずっぱい！","もちもち","500問おめでとう"]},
 {id:"nijimaru",nm:"にじまる",pf:"1000問を越えた庭にだけ現れる、小さな虹をかぶった子",c:["q",1000],ct:"問題を1000問解く",ln:["にじ、みえる？","1000問のしるし","きらきら〜"]},
 {id:"kotonoha",nm:"ことのは",pf:"覚えた用語が集まって生まれた、いちょうの葉の子。物知り",c:["known",30],ct:"用語カードを30枚「覚えた」にする",ln:["それ、しってる！","ことば あつめ","ひらひら〜"]},
 {id:"chikutaku",nm:"ちくたく",pf:"勉強した時間をおなかの時計で数えている子。10時間たまるとやって来る",c:["t",36000],ct:"勉強時間を合計10時間にする",ln:["ちくたく","いま なんじ？","じかん、たまったね"]},
 {id:"kirari",nm:"きらり",pf:"バッジの光から生まれた、小さな羽の子。ほめられると光る",c:["badges",5],ct:"バッジを5個もらう",ln:["きらーん","バッジ ぴかぴか","とべるかな？"]},
 {id:"kururin",nm:"くるりん",pf:"Data 360 合格の記念に来た、わっかをまとう子。ぐるっと一周見わたすのが得意",c:["pass","d360"],ct:"Data 360 コンサルタントに合格する",ln:["ぐるっと いっしゅう","データ まとめたよ","合格おめでとう！"]},
 {id:"futon",nm:"ふうとん",pf:"Marketing Cloud 合格の記念に来た封筒の子。届けたい気持ちでいっぱい",c:["pass","mcadmin"],ct:"Marketing Cloud Administrator に合格する",ln:["おとどけです！","メール きてるよ","合格おめでとう！"]},
 {id:"chobitai",nm:"ちょびタイ",pf:"Agentforce Sales 合格の記念に来た、ちょうネクタイの子。あいさつが上手",c:["pass","afsales"],ct:"Agentforce Sales コンサルタントに合格する",ln:["よろしくおねがいします！","商談まとまったよ","合格おめでとう！"]},
 {id:"pikon",nm:"ぴこん",pf:"Agentforce スペシャリスト合格の記念に来た子。ひらめくとアンテナが光る",c:["pass","afspec"],ct:"Agentforce スペシャリストに合格する",ln:["ぴこーん！","おてつだい するよ","合格おめでとう！"]},
 {id:"musubin",nm:"むすびん",pf:"MuleSoft 合格の記念に来た、わっかを2つつないだ子。だれとでもつながれる",c:["pass","mulepa"],ct:"MuleSoft Platform Architect に合格する",ln:["つながった！","なかよくしよ","合格おめでとう！"]},
 {id:"kakumochi",nm:"かくもち",pf:"基本情報技術者 合格の記念に来た、しかくいおもちの子。0と1が好き",c:["pass","fe"],ct:"基本情報技術者に合格する",ln:["ぜろ、いち、ぜろ","かくかく","合格おめでとう！"]},
 {id:"mamorun",nm:"まもるん",pf:"情報セキュリティマネジメント 合格の記念に来た子。小さな盾で庭を守る",c:["pass","sg"],ct:"情報セキュリティマネジメントに合格する",ln:["まもるよ！","パスワード だいじ","合格おめでとう！"]}];
/* ---- 絵: 足元が (0,0)、上が負。顔は少し右向き(歩く向きに合わせて左右を反転する) ---- */
function cpR(v){return Math.round(v*100)/100}
function cpF(x,y,o,k){var s='<g transform="translate('+cpR(x+1.2*(k||1))+','+y+') scale('+(k||1)+')">';
  if(o.sleep)s+='<path d="M-4.3 0 q1.1 1 2.2 0 M2.1 0 q1.1 1 2.2 0" fill="none" stroke="#3a2e2a" stroke-width=".9" stroke-linecap="round"/>';
  else s+='<g class="gp-eye"><circle cx="-3.2" r="1.15" fill="#3a2e2a"/><circle cx="3.2" r="1.15" fill="#3a2e2a"/><circle cx="-3.55" cy="-.42" r=".38" fill="#fff"/><circle cx="2.85" cy="-.42" r=".38" fill="#fff"/></g><path d="M-.9 1.6 q.9 .9 1.8 0" fill="none" stroke="#3a2e2a" stroke-width=".7" stroke-linecap="round"/>';
  return s+'<ellipse cx="-5.5" cy="2" rx="1.7" ry="1" fill="#ff7f9a" opacity=".55"/><ellipse cx="5.5" cy="2" rx="1.7" ry="1" fill="#ff7f9a" opacity=".55"/></g>'}
function cpFt(c,w){w=w||3.6;return '<ellipse cx="'+(-w)+'" cy="-.7" rx="2.5" ry="1.4" fill="'+c+'"/><ellipse cx="'+w+'" cy="-.7" rx="2.5" ry="1.4" fill="'+c+'"/>'}
function cpB(cx,cy,r,f,st){return '<circle cx="'+cx+'" cy="'+cy+'" r="'+r+'" fill="'+f+'" stroke="'+st+'" stroke-width=".8"/>'}
/* [絵, マフラーの高さ, マフラーの半幅(0は巻かない), 頭のてっぺん] */
var CS_PALART={
 mebuki:[function(o){return cpFt("#6aa84f")+'<ellipse cy="-8.5" rx="9" ry="8.5" fill="#b4e296" stroke="#6aa84f" stroke-width=".8"/><path d="M0 -16.6 q.6 -2.4 0 -4.4" fill="none" stroke="#5a9a3e" stroke-width="1.1" stroke-linecap="round"/><path d="M0 -20.6 q-5.4 -3.4 -7 .4 q4.2 1.6 7 -.4Z M0 -20.6 q5.4 -3.4 7 .4 q-4.2 1.6 -7 -.4Z" fill="#6cc04a"/>'+cpF(0,-8,o)},-4.6,8.2,-24],
 koron:[function(o){return '<ellipse cy="-6.8" rx="10.5" ry="6.8" fill="#d8d0c3" stroke="#a39a8c" stroke-width=".8"/><circle cx="-6.5" cy="-4" r=".7" fill="#b8ae9f"/><circle cx="7.4" cy="-3.2" r=".6" fill="#b8ae9f"/><circle cx="2.4" cy="-12.9" r="1.7" fill="#86bd5e"/><circle cx="4.6" cy="-13.5" r="2.2" fill="#7fb85a"/><circle cx="6.9" cy="-12.6" r="1.7" fill="#86bd5e"/>'+cpF(0,-6.4,o)},-2.6,9.4,-17],
 fumi:[function(o){return '<path d="M-10 0 Q-11.2 -12.6 0 -13.4 Q11.2 -12.6 10 0Z" fill="#fff4dc" stroke="#dcc396" stroke-width=".8"/><path d="M-7.6 -10.6 V-3.4 l1.2 -1.3 l1.2 1.3 V-11.6Z" fill="#e05a6a"/>'+cpF(0,-6.2,o)},-2.4,9.6,-17],
 mittsun:[function(o){return '<circle cx="-8.2" cy="-1.2" r="1" fill="#6aa84f"/><circle cx="-2.6" cy="-1" r="1" fill="#6aa84f"/><circle cx="3" cy="-.9" r="1.1" fill="#6aa84f"/><circle cx="7.4" cy="-.9" r="1.1" fill="#6aa84f"/>'+cpB(-8,-4.4,4,"#a6d97a","#6aa84f")+cpB(-2.6,-5.2,4.7,"#b0de86","#6aa84f")+cpB(4.6,-7,6.4,"#bde592","#6aa84f")+'<path d="M2.6 -12.8 L1.4 -16 M7 -12.8 L8.2 -16" stroke="#6aa84f" stroke-width=".8" stroke-linecap="round"/><circle cx="1.4" cy="-16.2" r="1" fill="#f2a33c"/><circle cx="8.2" cy="-16.2" r="1" fill="#f2a33c"/>'+cpF(4.2,-7,o,.78)},0,0,-20],
 hidamari:[function(o){var r="";for(var i=0;i<8;i++){var a=i*Math.PI/4;r+='<circle cx="'+cpR(Math.cos(a)*9.4)+'" cy="'+cpR(-10+Math.sin(a)*9.4)+'" r="2.3" fill="#ffe28f"/>'}return cpFt("#e8a92e",3)+r+cpB(0,-10,8,"#ffd457","#e8a92e")+cpF(0,-10,o)},-5,6.2,-23],
 donguri:[function(o){return cpFt("#9a6232",3.2)+'<ellipse cy="-8.2" rx="7.4" ry="8.2" fill="#d39457" stroke="#9a6232" stroke-width=".8"/><path d="M-8.4 -12 Q0 -21.4 8.4 -12 Q0 -10 -8.4 -12Z" fill="#7a5230"/><circle cx="-3.4" cy="-14.6" r=".6" fill="#a37850"/><circle cx="0" cy="-16" r=".6" fill="#a37850"/><circle cx="3.4" cy="-14.6" r=".6" fill="#a37850"/><circle cx="-1.6" cy="-13" r=".6" fill="#a37850"/><circle cx="1.8" cy="-13" r=".6" fill="#a37850"/><rect x="-.8" y="-20.6" width="1.6" height="3.2" rx=".8" fill="#5e3d22"/>'+cpF(0,-6.6,o,.9)},-3.4,7,-23],
 hanamaru:[function(o){var p="";for(var i=0;i<6;i++){var a=i*Math.PI/3-Math.PI/2;p+='<circle cx="'+cpR(Math.cos(a)*6.7)+'" cy="'+cpR(-11+Math.sin(a)*6.7)+'" r="4.3" fill="#f8b0ca" stroke="#e07a9f" stroke-width=".7"/>'}return '<ellipse cx="-4" cy="-1.2" rx="3.4" ry="1.5" transform="rotate(-18 -4 -1.2)" fill="#6cb84a"/><ellipse cx="4" cy="-1.2" rx="3.4" ry="1.5" transform="rotate(18 4 -1.2)" fill="#6cb84a"/>'+p+cpB(0,-11,5.8,"#fff3d6","#e9c98a")+cpF(0,-11,o,.72)},0,0,-23],
 poko:[function(o){return '<rect x="-5.6" y="-9.6" width="11.2" height="9.6" rx="4" fill="#fff1dc" stroke="#d8bf98" stroke-width=".8"/><path d="M-11 -8.4 Q-10.4 -20.4 0 -20.4 Q10.4 -20.4 11 -8.4 Q0 -6.4 -11 -8.4Z" fill="#e8574a" stroke="#c43f34" stroke-width=".8"/><circle cx="-5" cy="-14.2" r="1.8" fill="#fff"/><circle cx="2" cy="-17.2" r="1.5" fill="#fff"/><circle cx="6.2" cy="-12" r="1.6" fill="#fff"/><circle cx="-1" cy="-11.6" r="1.1" fill="#fff"/>'+cpF(0,-4.2,o,.72)},0,0,-21],
 yamabiko:[function(o){return cpFt("#3f8a3c",4.2)+'<path d="M-11 -.6 Q-11.2 -2.6 -9.4 -5.4 L-2.4 -18 Q0 -21.4 2.4 -18 L9.4 -5.4 Q11.2 -2.6 11 -.6Z" fill="#86c873" stroke="#4f9a4a" stroke-width=".8" stroke-linejoin="round"/><path d="M-3.7 -15.4 L-2.4 -18 Q0 -21.4 2.4 -18 L3.7 -15.4 L1.8 -14 L0 -15.6 L-1.8 -14Z" fill="#fff"/>'+cpF(0,-6.8,o,.9)},-2.8,9.4,-22],
 fuwawa:[function(o){var sh='<circle cx="-5.2" cy="-6" r="5.2"/><circle cx="0" cy="-9.8" r="6.6"/><circle cx="5.6" cy="-6.4" r="5"/><rect x="-9.4" y="-6.4" width="19" height="6.4" rx="3.2"/>';return '<g fill="#b8c7d9" stroke="#b8c7d9" stroke-width="1.6">'+sh+'</g><g fill="#fdfdff">'+sh+'</g>'+cpF(0,-6.6,o)},0,0,-18],
 mameta:[function(o){return cpFt("#c9a64e",3.2)+'<ellipse cy="-8.2" rx="7.6" ry="8.4" transform="rotate(-10 0 -8.2)" fill="#f3d993" stroke="#c9a64e" stroke-width=".8"/><path d="M-1.4 -16.4 q-.6 -3.4 2.2 -4.4 q2 -.6 1.8 1.4" fill="none" stroke="#7fb14a" stroke-width="1.1" stroke-linecap="round"/><ellipse cx="-3.6" cy="-19.4" rx="2.6" ry="1.3" transform="rotate(20 -3.6 -19.4)" fill="#8fc45a"/>'+cpF(0,-7.6,o,.92)},-3.6,7.2,-22],
 ichimochi:[function(o){return '<path d="M-10.6 0 Q-11.6 -13 0 -13.6 Q11.6 -13 10.6 0Z" fill="#fff4f4" stroke="#e6cfc9" stroke-width=".8"/><path d="M-4.4 -12.6 Q-5 -18.8 0 -20.2 Q5 -18.8 4.4 -12.6 Q0 -11 -4.4 -12.6Z" fill="#ef5866"/><circle cx="-1.8" cy="-16.4" r=".45" fill="#ffe2a8"/><circle cx="1.6" cy="-17.2" r=".45" fill="#ffe2a8"/><circle cx="0" cy="-14.4" r=".45" fill="#ffe2a8"/><circle cx="2.4" cy="-14.2" r=".45" fill="#ffe2a8"/><path d="M-4.6 -12.4 l2.2 -1.4 l1 1.6 l1.4 -1.8 l1.4 1.8 l1 -1.6 l2.2 1.4 Q0 -10.8 -4.6 -12.4Z" fill="#6cb84a"/>'+cpF(0,-6,o)},-2.4,9.8,-22],
 nijimaru:[function(o){return cpFt("#aab0d6")+cpB(0,-8.6,8.6,"#fbfbff","#c3c8e4")+[["#f08a8a",9.6],["#f2c94c",8.2],["#7cc5f0",6.8]].map(function(a){return '<path d="M'+(-a[1])+' -13 A'+a[1]+' '+a[1]+' 0 0 1 '+a[1]+' -13" fill="none" stroke="'+a[0]+'" stroke-width="1.5" stroke-linecap="round"/>'}).join("")+cpF(0,-7.6,o)},-4.4,8.2,-24],
 kotonoha:[function(o){return '<path d="M0 -2 V.4" stroke="#b58a24" stroke-width="1.2" stroke-linecap="round"/><path d="M-.8 -2.2 C-9.6 -5.6 -12.2 -13.6 -10.4 -19 Q-5.6 -22.4 -1.6 -18.8 L0 -16.6 L1.6 -18.8 Q5.6 -22.4 10.4 -19 C12.2 -13.6 9.6 -5.6 .8 -2.2Z" fill="#f7d04d" stroke="#d6a52a" stroke-width=".8" stroke-linejoin="round"/><path d="M0 -3 L-6 -17 M0 -3 L6 -17" stroke="#e6b83a" stroke-width=".5" fill="none"/>'+cpF(0,-10.4,o,.86)},0,0,-21],
 chikutaku:[function(o){return cpFt("#6fa9cc")+cpB(-5.8,-16.4,2.8,"#f4cd57","#c99a2a")+cpB(5.8,-16.4,2.8,"#f4cd57","#c99a2a")+cpB(0,-8.6,8.6,"#b3dcf2","#6fa9cc")+'<circle cx="1.6" cy="-3.9" r="2.7" fill="#fff" stroke="#6fa9cc" stroke-width=".6"/><path d="M1.6 -3.9 V-5.7 M1.6 -3.9 H2.9" stroke="#3a4a5a" stroke-width=".5" stroke-linecap="round"/>'+cpF(0,-10.6,o)},0,0,-21],
 kirari:[function(o){return cpFt("#a58fd8")+'<ellipse cx="-9.4" cy="-11.4" rx="3.6" ry="2.1" transform="rotate(-28 -9.4 -11.4)" fill="#fff" stroke="#c8bfe6" stroke-width=".7"/><ellipse cx="9.4" cy="-11.4" rx="3.6" ry="2.1" transform="rotate(28 9.4 -11.4)" fill="#fff" stroke="#c8bfe6" stroke-width=".7"/>'+cpB(0,-8.6,8.2,"#ddd2f7","#a58fd8")+'<path class="gp-glow" d="M0 -22.6 L.9 -20 L3.4 -19.2 L.9 -18.4 L0 -15.8 L-.9 -18.4 L-3.4 -19.2 L-.9 -20Z" fill="#ffd84d"/>'+cpF(0,-8.6,o)},-4.4,7.8,-24],
 kururin:[function(o){return cpFt("#4f63a0")+'<ellipse cy="-9" rx="13" ry="3.6" transform="rotate(-12 0 -9)" fill="none" stroke="#e9b93a" stroke-width="1.6"/>'+cpB(0,-9,8.2,"#a3b5e8","#5a6eae")+'<path d="M-13 -9 A13 3.6 0 0 0 13 -9" transform="rotate(-12 0 -9)" fill="none" stroke="#f2c94c" stroke-width="1.6"/>'+cpF(0,-11.2,o,.9)},0,0,-22],
 futon:[function(o){return cpFt("#e08a3c",4.4)+'<rect x="-10" y="-15.4" width="20" height="14.4" rx="3.6" fill="#fff8ec" stroke="#e0a060" stroke-width=".8"/><path d="M-9 -14.4 L0 -8.2 L9 -14.4" fill="none" stroke="#e0a060" stroke-width=".9" stroke-linejoin="round"/><path d="M0 -7 C-2.2 -8.6 -1.8 -10.4 -.7 -10.4 C-.2 -10.4 0 -10 0 -9.7 C0 -10 .2 -10.4 .7 -10.4 C1.8 -10.4 2.2 -8.6 0 -7Z" fill="#ef7a4a"/>'+cpF(0,-4.4,o,.82)},0,0,-19],
 chobitai:[function(o){return cpFt("#3f9a9e")+cpB(0,-9,8.6,"#8ad3d3","#3f9a9e")+'<path d="M-.4 -2.6 L-4.6 -4.6 L-4.6 -.6Z M.4 -2.6 L4.6 -4.6 L4.6 -.6Z" fill="#e8574a"/><circle cy="-2.6" r="1.2" fill="#c43f34"/>'+cpF(0,-10.2,o)},0,0,-21],
 pikon:[function(o){return cpFt("#8a63c4")+'<path d="M0 -15.6 L1.6 -20.6" stroke="#8a63c4" stroke-width=".9" stroke-linecap="round"/><circle class="gp-glow" cx="1.8" cy="-21.8" r="3.6" fill="#fff2a8" opacity=".55"/><circle cx="1.8" cy="-21.8" r="1.9" fill="#ffd84d"/>'+'<ellipse cy="-8" rx="8.6" ry="8" fill="#cbb2ee" stroke="#8a63c4" stroke-width=".8"/>'+cpF(0,-8,o)},-4,8,-25],
 musubin:[function(o){return cpFt("#4f7fc4")+'<circle cx="-2" cy="-19.6" r="2.8" fill="none" stroke="#4f7fc4" stroke-width="1.4"/><circle cx="2" cy="-19.6" r="2.8" fill="none" stroke="#f2a33c" stroke-width="1.4"/>'+cpB(0,-8.6,8.6,"#9cc0ef","#4f7fc4")+cpF(0,-8.6,o)},-4.4,8.2,-24],
 kakumochi:[function(o){return cpFt("#7f9a3a")+'<path d="M0 -16.8 V-19.6" stroke="#6a8a2a" stroke-width="1" stroke-linecap="round"/><rect x="-4.4" y="-22.8" width="3.4" height="3.4" rx=".6" fill="#8fbf3a"/><rect x="1" y="-22.8" width="3.4" height="3.4" rx=".6" fill="#8fbf3a"/><rect x="-9" y="-17" width="18" height="16.4" rx="5" fill="#d6e8a4" stroke="#7f9a3a" stroke-width=".8"/>'+cpF(0,-9,o)},-4.4,8.6,-24],
 mamorun:[function(o){return cpFt("#c45a8c")+cpB(0,-8.6,8.4,"#f5b0cf","#c45a8c")+'<path d="M-8 -12.4 Q0 -21.8 8 -12.4 Q0 -14.2 -8 -12.4Z" fill="#cfd8e2" stroke="#8d9aa8" stroke-width=".7"/><rect x="-.7" y="-20.6" width="1.4" height="3" rx=".7" fill="#e8574a"/><g transform="translate(-8.4,-5.6)"><path d="M0 -4.2 L3.8 -3 Q3.8 2 0 4.2 Q-3.8 2 -3.8 -3Z" fill="#fff" stroke="#8d9aa8" stroke-width=".7"/><path d="M0 -2.2 V2.2 M-1.8 -.4 H1.8" stroke="#c45a8c" stroke-width=".9"/></g>'+cpF(.4,-8.2,o)},0,0,-22]};
var CS_PALSCARF=["#e05a5a","#4f7fc4","#f2a33c","#3f9a6e","#b05ac4"];
function csPalArt(id,o){var a=CS_PALART[id];if(!a)return "";var s=a[0](o||{});
  if(o&&o.winter&&a[2]){var y=a[1],w=a[2],c=CS_PALSCARF[id.length%CS_PALSCARF.length];s+='<path d="M'+(-w)+' '+cpR(y-1.4)+' Q0 '+cpR(y+1.6)+' '+w+' '+cpR(y-1.4)+' L'+w+' '+cpR(y+1)+' Q0 '+cpR(y+4)+' '+(-w)+' '+cpR(y+1)+'Z" fill="'+c+'"/><path d="M'+cpR(-w*0.45)+' '+cpR(y+1.6)+' l-1.4 4.4 l2.2 .4 l.9 -4.2Z" fill="'+c+'" opacity=".85"/>'}
  return s}
function csPalIcon(id,cls){return '<svg viewBox="-14 -26 28 28" class="'+(cls||"")+'" aria-hidden="true"><g>'+csPalArt(id,{})+'</g></svg>'}
/* ---- 条件: すでにある記録から数える ---- */
function csPalLS(k,d){try{var v=JSON.parse(localStorage.getItem(k));return v==null?d:v}catch(e){return d}}
function csPalStats(days){days=days||{};var q=0,r=0,t=0,sd=0,best=0,run=0,prev=null;
  Object.keys(days).sort().forEach(function(k){var d=days[k]||{},dr=Array.isArray(d.r)?d.r.length:+d.r||0;q+=+d.q||0;r+=dr;t+=+d.t||0;
    if(+d.q||dr){sd++;var dt=new Date(k+"T00:00:00").getTime();run=prev!=null&&Math.round((dt-prev)/864e5)===1?run+1:1;prev=dt;if(run>best)best=run}});
  var cnt=function(o){return o&&typeof o==="object"?Object.keys(o).filter(function(k){return o[k]}).length:0},ps=csPalLS("cs-subj-passed",{});
  return {q:q,r:r,t:t,days:sd,best:best,grass:csGardenDays(days).length,known:cnt(csPalLS("cs-term-known-v1",{})),badges:cnt(csPalLS("ls-badges-v1",{})),passed:ps&&typeof ps==="object"?ps:{}}}
function csPalOk(P,st){if(window.__csPalAll)return true;var c=P.c;return c[0]==="pass"?!!st.passed[c[1]]:(+st[c[0]]||0)>=c[1]}
function csPalLeft(P,st){var c=P.c;if(c[0]==="pass")return "";var l=c[1]-(+st[c[0]]||0);if(l<=0)return "";
  if(c[0]==="t"){var m=Math.ceil(l/60),h=Math.floor(m/60);return "あと"+(h?h+"時間":"")+(m%60?m%60+"分":"")}
  return "あと"+l+{q:"問",r:"節",grass:"本",best:"日",days:"日",known:"枚",badges:"個"}[c[0]]}
/* 仲間になった中から最大10匹をランダムに選ぶ。位置・動き方も決めておき、カード・くわしい表示・全画面で同じ顔ぶれにする */
function csPalsPrep(days){try{var st=csPalStats(days),on=CS_PALS.filter(function(P){return csPalOk(P,st)}).map(function(P){return P.id}),sig=on.join(","),pk=window.__csPalPick;
  window.__csPalSt={st:st,on:on};
  if(!pk||pk.sig!==sig){var ids=on.slice();for(var i=ids.length-1;i>0;i--){var j=Math.floor(Math.random()*(i+1)),x=ids[i];ids[i]=ids[j];ids[j]=x}ids=ids.slice(0,CS_PALS_MAX);
    var k=ids.length,sl=ids.map(function(_,i){return i});for(i=k-1;i>0;i--){j=Math.floor(Math.random()*(i+1));x=sl[i];sl[i]=sl[j];sl[j]=x}
    var BH=["walk","walk","walk","hop","look","sit"];
    window.__csPalPick={sig:sig,items:ids.map(function(id,i){return {id:id,xf:(sl[i]+0.5+(Math.random()-0.5)*0.5)/k,yf:sl[i]%2?0.83+Math.random()*0.07:0.7+Math.random()*0.07,
      bh:BH[Math.floor(Math.random()*BH.length)],du:(12+Math.random()*10).toFixed(1),dl:(Math.random()*20).toFixed(1),dx:12+Math.random()*12,f:Math.random()<0.5?1:-1,ln:Math.floor(Math.random()*3)}})}}
  }catch(e){}}
/* 庭の絵の中に仲間を描く(csGardenSVG から呼ぶ)。夜は眠り、冬はマフラー */
function csPalsSVG(W,H,fy,q,SK,opt,nb){var pk=window.__csPalPick;if(!pk||!pk.items.length)return "";
  var sc=opt.fs?Math.min(2.2,q*1.3):Math.max(1.3,q*1.15),night=SK.tod==="night",o={sleep:night,winter:SK.season==="winter"},out=[];
  pk.items.forEach(function(it,i){var a=CS_PALART[it.id];if(!a)return;var x=12*sc+it.xf*(W-24*sc),y=+fy(nb?(opt.fs?Math.min(it.yf,0.9):it.yf):Math.min(it.yf,0.71)),dx=it.dx,f=it.f,bh=night?"sleep":it.bh;
    if(f<0)dx=-dx;if(x+dx*sc>W-10*sc||x+dx*sc<10*sc)dx=-dx;
    if(bh==="walk")f=dx<0?-1:1;
    var mv=bh==="walk"?' class="gp-mv" style="--dx:'+cpR(dx)+'px;--f:'+f+';animation-duration:'+it.du+'s;animation-delay:-'+it.dl+'s"':bh==="look"?' class="gp-lk" style="animation-duration:'+(it.du/2).toFixed(1)+'s;animation-delay:-'+it.dl+'s"':f<0?' style="transform:scaleX(-1)"':'';
    var inn=bh==="walk"?"gp-b":bh==="hop"?"gp-hp":"gp-br",zz=night?'<g class="gp-zz" transform="translate(5,'+(a[3]+1)+')"><text class="gp-z">z</text><text class="gp-z gp-z2" x="4" y="-3">z</text></g>':'';
    out.push([y,'<g class="gd-pal'+(night?" zz":"")+'" data-pal="'+it.id+'" data-ln="'+it.ln+'" transform="translate('+cpR(x)+','+cpR(y)+') scale('+cpR(sc)+')"><g'+mv+'><ellipse rx="8" ry="1.7" fill="#203018" opacity=".14"/><g class="'+inn+'" style="animation-delay:-'+(i*0.37).toFixed(2)+'s"><g class="gp-t">'+csPalArt(it.id,o).replace('class="gp-eye"','class="gp-eye" style="animation-delay:-'+(i*1.3).toFixed(1)+'s"')+'</g></g>'+zz+'<rect x="-12" y="'+(a[3]-2)+'" width="24" height="'+(-a[3]+4)+'" fill="#000" fill-opacity="0"/></g></g>'])});
  out.sort(function(a,b){return a[0]-b[0]});return '<g class="gd-pals-l">'+out.map(function(x){return x[1]}).join("")+'</g>'}
/* タップ: 跳ねて、ハートと名前・ひとことの吹き出し(眠っているときは、むにゃむにゃ) */
function csPalTap(pl){try{var sv=pl.ownerSVGElement,id=pl.getAttribute("data-pal"),P=CS_PALS.filter(function(x){return x.id===id})[0];if(!sv||!P)return;
  var t=pl.querySelector(".gp-t"),sleep=pl.classList.contains("zz"),m=sv.getScreenCTM(),vb=sv.viewBox.baseVal;if(!m||!vb)return;
  if(sleep)csAn(t,[{transform:"rotate(0deg)"},{transform:"rotate(-8deg)",offset:.25},{transform:"rotate(7deg)",offset:.6},{transform:"rotate(0deg)"}],600,0,"ease-in-out");
  else csAn(t,[{transform:"translateY(0px) scale(1,1)"},{transform:"translateY(0px) scale(1.14,.84)",offset:.15},{transform:"translateY(-9px) scale(.92,1.1)",offset:.45},{transform:"translateY(0px) scale(1.08,.9)",offset:.75},{transform:"translateY(0px) scale(1,1)"}],650,0,"ease-out");
  var r=t.getBoundingClientRect(),iv=m.inverse(),pt=sv.createSVGPoint();pt.x=r.left+r.width/2;pt.y=r.top;pt=pt.matrixTransform(iv);
  var W=vb.width,u=+sv.getAttribute("data-u")||1,s=Math.min(1.8,Math.max(1.2,Math.sqrt(u))),x=pt.x,y=pt.y,n=sv.getAttribute("data-tod")==="night";
  sv.querySelectorAll(".gd-palbub").forEach(function(e){e.remove()});
  var L=document.createElementNS(CS_NS,"g");L.setAttribute("class","gd-tapfx gd-palbub");sv.appendChild(L);
  if(!sleep)for(var k=0;k<2;k++)csAn(csFxEl(L,x+(k?6:-4)*s,y,s,'<path d="M0 2.6 C-4.5 -.6 -3.6 -4.4 -1.4 -4.4 C-.5 -4.4 0 -3.6 0 -3 C0 -3.6 .5 -4.4 1.4 -4.4 C3.6 -4.4 4.5 -.6 0 2.6Z" fill="#ff6f91"/>'),[{transform:"translate(0px,0px) scale(.3)",opacity:0},{transform:"translate(0px,-6px) scale(1)",opacity:1,offset:.25},{transform:"translate("+(k?4:-3)+"px,-22px) scale(.8)",opacity:0}],1300,k*180,"ease-out");
  var cnt=+pl.getAttribute("data-tc")||0;pl.setAttribute("data-tc",cnt+1);
  var line=sleep?(cnt%2?"すやすや…":"むにゃむにゃ…"):P.ln[((+pl.getAttribute("data-ln")||0)+cnt)%P.ln.length];
  var g=document.createElementNS(CS_NS,"g");L.appendChild(g);g.innerHTML='<path class="gp-bt"/><rect class="gp-bb" rx="6" ry="6"/><text class="gp-bx" text-anchor="middle" y="3.2"><tspan class="gp-bn">'+P.nm+'</tspan> '+line+'</text>';
  var tx=g.querySelector("text"),tw=60;try{tw=tx.getComputedTextLength()}catch(e){}var bw=tw+12,bh=15,sy=Math.max(bh*s/2+2,y-(sleep?10:16)*s),bx=Math.max(bw*s/2+3,Math.min(W-bw*s/2-3,x));
  if(bx+bw*s/2>W-48)sy=Math.max(sy,54);g.setAttribute("transform","translate("+cpR(bx)+","+cpR(sy)+") scale("+cpR(s)+")");var rc=g.querySelector("rect");rc.setAttribute("x",cpR(-bw/2));rc.setAttribute("y",-bh/2);rc.setAttribute("width",cpR(bw));rc.setAttribute("height",bh);
  var dx=Math.max(-bw/2+6,Math.min(bw/2-6,(x-bx)/s));g.querySelector(".gp-bt").setAttribute("d","M"+cpR(dx-3)+" "+(bh/2-1)+" L"+cpR(dx)+" "+(bh/2+4)+" L"+cpR(dx+3)+" "+(bh/2-1)+"Z");
  if(n)g.setAttribute("class","n");
  csAn(g.firstChild.parentNode,[{opacity:0},{opacity:1,offset:.08},{opacity:1,offset:.85},{opacity:0}],2600,0,"linear");
  setTimeout(function(){L.remove()},2700)}catch(e){}}
/* ---- 一覧(学習の記録の草の庭・全画面) ---- */
function csPalsList(){var S=window.__csPalSt;if(!S)return "";var st=S.st,on=S.on;
  return '<ul class="gd-pals">'+CS_PALS.map(function(P){var ok=on.indexOf(P.id)>=0,lf=ok?"":csPalLeft(P,st);
    return '<li class="'+(ok?"on":"lk")+'">'+csPalIcon(P.id,ok?"":"sil")+'<div><b>'+(ok?P.nm:"？？？")+'</b>'+(ok?'<span>'+P.pf+'</span>':'')+'<small>'+(ok?"仲間になった条件: ":"")+P.ct+(lf?'(<em>'+lf+'</em>)':'')+'</small></div></li>'}).join("")+'</ul>'}
function csPalsHead(){var S=window.__csPalSt;return S?'仲間 <b>'+S.on.length+'</b> / '+CS_PALS.length+'匹':''}
function csPalsDetails(){return '<details class="gd-palsd" id="garden-pals"><summary><span class="gd-palsd-k">庭の仲間</span><span class="gd-palsd-n">'+csPalsHead()+'</span></summary><p class="gd-palsd-s">合格した科目や学習の成果で、庭に仲間がやって来ます。庭にいるのは、仲間の中からランダムに選んだ最大10匹です(ページを開くたびに入れ替わります)。タップすると反応します。</p>'+csPalsList()+'</details>'}
/* 新しい仲間のお知らせ(1回だけ) */
function csPalsNotice(){try{var S=window.__csPalSt;if(!S||!S.on.length)return "";var seen=csPalLS(CS_PALSEEN,{});if(!seen||typeof seen!=="object")seen={};
  var nw=S.on.filter(function(id){return !seen[id]});if(!nw.length)return "";var now=Date.now();S.on.forEach(function(id){if(!seen[id])seen[id]=now});
  try{localStorage.setItem(CS_PALSEEN,JSON.stringify(seen))}catch(e){}
  var nm=nw.map(function(id){return CS_PALS.filter(function(P){return P.id===id})[0].nm});
  return '<p class="gd-new" role="status">'+csPalIcon(nw[0])+'<span><b>新しい仲間が庭に来ました'+(nw.length>1?'('+nw.length+'匹)':'')+'</b>'+(nm.length>4?nm.slice(0,4).join("・")+" ほか":nm.join("・"))+'</span></p>'}catch(e){return ""}}
/* 全画面: 左上の「庭の仲間」ボタンで一覧を開く */
function csPalsFSBtn(){var S=window.__csPalSt;return S?'<button type="button" class="gd-fs-pb" aria-haspopup="dialog">庭の仲間 <b>'+S.on.length+'</b>/'+CS_PALS.length+'</button>':''}
function csPalsSheet(open){if(!csFS)return;var el=csFS.el.querySelector(".gd-fs-pals");if(el)el.remove();if(!open)return;
  el=document.createElement("div");el.className="gd-fs-pals";el.setAttribute("role","dialog");el.setAttribute("aria-label","庭の仲間");
  el.innerHTML='<div class="gd-fs-ph"><b>庭の仲間</b><span>'+csPalsHead()+'</span><button type="button" class="gd-fs-pc" aria-label="一覧を閉じる"><svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg></button></div><div class="gd-fs-pbd"><p class="gd-palsd-s">庭にいるのは、仲間の中からランダムに選んだ最大10匹です。</p>'+csPalsList()+'</div>';
  csFS.el.appendChild(el);try{el.querySelector(".gd-fs-pc").focus({preventScroll:true})}catch(x){}}
document.addEventListener("click",function(e){var t=e.target;if(!t||!t.closest)return;if(t.closest(".gd-fs-pb")){e.preventDefault();csPalsSheet(true);return}if(t.closest(".gd-fs-pc")){e.preventDefault();csPalsSheet(false)}});
'''
rep("FAMP.home=function(){setTimeout(csHomeExtra,0);", JS + "\nFAMP.home=function(){setTimeout(csHomeExtra,0);")
# 庭の絵に仲間を描く(草・季節の小物の後、桜の枝・舞うもの・夜の暗さの前)
rep("/* 春は桜の枝(左上から)", "g+=csPalsSVG(W,H,fy,q,SK,opt,n);\n  /* 春は桜の枝(左上から)")
# 仲間をタップしたときは、庭の演出を出さずに仲間が反応する
rep('var sv=t.closest("svg.garden");if(sv)csGardenTap(sv,e)})', 'var pl=t.closest(".gd-pal");if(pl){csPalTap(pl);return}var sv=t.closest("svg.garden");if(sv)csGardenTap(sv,e)})')
# 全画面に「庭の仲間」ボタン
rep("""<p class="gd-fs-cap"><b>'+CS_STAGES[st][1]""", """'+csPalsFSBtn()+'<p class="gd-fs-cap"><b>'+CS_STAGES[st][1]""")
rep("<small>庭をタップすると、いろいろな演出が出ます</small>", "<small>庭をタップすると演出が出ます。仲間をタップすると反応します</small>")
# Esc は一覧を先に閉じる
rep('if(e.key==="Escape"&&csFS){e.preventDefault();csGardenFSClose()}', 'if(e.key==="Escape"&&csFS){e.preventDefault();if(csFS.el.querySelector(".gd-fs-pals")){csPalsSheet(false);return}csGardenFSClose()}')
# ホームのカード: 仲間を選び、新しい仲間のお知らせ
rep("function csGarden(el,s){try{if(!el||!s)return;", "function csGarden(el,s){try{if(!el||!s)return;csPalsPrep(s.days);")
rep("""</p><a class="bx-go" href="/record/#garden-d">草の庭をくわしく見る</a>'""", """</p>'+csPalsNotice()+'<a class="bx-go" href="/record/#garden-d">草の庭をくわしく見る</a>'""")
# 学習の記録: お知らせと「庭の仲間」の一覧
rep('function csGardenDetail(days){try{var el=document.getElementById("garden-detail");if(!el)return;', 'function csGardenDetail(days){try{var el=document.getElementById("garden-detail");if(!el)return;csPalsPrep(days);')
rep("""'<div class="gd-now"><b>'+cur[1]+'</b><span>'+cur[2]+'</span></div>';""", """csPalsNotice()+'<div class="gd-now"><b>'+cur[1]+'</b><span>'+cur[2]+'</span></div>';""")
rep("""h+='<p class="gd-h">生えた草の種類</p>""", """h+=csPalsDetails();h+='<p class="gd-h">生えた草の種類</p>""")
rep("右上のボタンで全画面になり、庭をタップすると演出が出ます。</p>", "右上のボタンで全画面になり、庭をタップすると演出が出ます。合格した科目や学習の成果に応じて、庭に仲間(生きもの)がやって来ます。</p>")
# お知らせ済みの仲間をアカウントに同期する
rep("`cs-subj-passed`,`cs-term-bm-v1`]", "`cs-subj-passed`,`cs-term-bm-v1`,`cs-pals-seen`]")
CSS = """
/* 庭の仲間 */
/* 夜の暗さ・舞う花びらなどが上に重なっても、仲間をタップできるように(ほかはタップを庭そのものへ通す) */
.garden *{pointer-events:none}
.garden .gd-pal,.garden .gd-pal *{pointer-events:auto}
.garden .gd-pal{cursor:pointer}
.garden .gp-mv{animation:gpWalk 16s linear infinite}
@keyframes gpWalk{0%,8%{transform:translateX(0) scaleX(var(--f))}42%,50%{transform:translateX(var(--dx)) scaleX(var(--f))}50.5%,58%{transform:translateX(var(--dx)) scaleX(calc(var(--f) * -1))}92%,99.5%{transform:translateX(0) scaleX(calc(var(--f) * -1))}100%{transform:translateX(0) scaleX(var(--f))}}
.garden .gp-b{animation:gpBob .34s ease-in-out infinite alternate}
@keyframes gpBob{from{transform:translateY(0)}to{transform:translateY(-1.1px)}}
.garden .gp-lk{animation:gpLook 4s linear infinite}
@keyframes gpLook{0%,45%{transform:scaleX(1)}47%,95%{transform:scaleX(-1)}97%,100%{transform:scaleX(1)}}
.garden .gp-hp{animation:gpHop 2.8s ease-in-out infinite}
@keyframes gpHop{0%,55%,100%{transform:translateY(0) scale(1,1)}61%{transform:translateY(0) scale(1.1,.88)}70%{transform:translateY(-7px) scale(.94,1.07)}78%{transform:translateY(0) scale(1.08,.9)}84%{transform:translateY(0) scale(1,1)}}
.garden .gp-br{animation:gpBr 3.2s ease-in-out infinite alternate}
.garden .zz .gp-br{animation-duration:4.4s}
@keyframes gpBr{from{transform:scale(1,1)}to{transform:scale(1.04,.95)}}
.garden .gp-eye{transform-box:fill-box;transform-origin:center;animation:gpBlink 4.6s linear infinite}
@keyframes gpBlink{0%,92%,97%,100%{transform:scaleY(1)}94.5%{transform:scaleY(.1)}}
.garden .gp-glow{animation:gpGlow 1.8s ease-in-out infinite alternate}
@keyframes gpGlow{from{opacity:.35}to{opacity:1}}
.garden .gp-z{font-size:7.5px;font-weight:800;fill:#fff;stroke:#2a3352;stroke-width:1.4px;paint-order:stroke;opacity:0;animation:gpZ 3s ease-out infinite}
.garden .gp-z2{animation-delay:1.5s}
@keyframes gpZ{0%{opacity:0;transform:translate(0,0) scale(.6)}20%{opacity:1}100%{opacity:0;transform:translate(4px,-9px) scale(1.1)}}
.garden .gd-palbub .gp-bb{fill:#fff;stroke:#c9d6cc;stroke-width:.6}
.garden .gd-palbub .gp-bt{fill:#fff}
.garden .gd-palbub .gp-bx{font-size:8.5px;font-weight:700;fill:#2b3a33}
.garden .gd-palbub .gp-bn{fill:#2a9765;font-weight:800}
.garden .gd-palbub .n .gp-bb,.garden .gd-palbub .n .gp-bt{fill:#26304f;stroke:#5a6690}
.garden .gd-palbub .n .gp-bx{fill:#fff}.garden .gd-palbub .n .gp-bn{fill:#ffe27a}
.gd-new{display:flex;align-items:center;gap:8px;margin:8px 0 0;padding:6px 10px;border-radius:12px;background:color-mix(in srgb,#f6c343 22%,var(--paper,#fff));font-size:12.5px;line-height:1.45;animation:gdNew .6s ease-out both}
.gd-new svg{width:34px;height:34px;flex:none}.gd-new b{display:block;font-size:13px}
@keyframes gdNew{from{opacity:0;transform:translateY(4px)}to{opacity:1;transform:none}}
.gd-palsd{margin:12px 0 4px;border:1px solid var(--line);border-radius:12px;background:var(--bg)}
.gd-palsd summary{list-style:none;display:flex;align-items:center;gap:8px;padding:10px 12px;cursor:pointer;font-size:14px}
.gd-palsd summary::-webkit-details-marker{display:none}
.gd-palsd summary::after{content:"";width:8px;height:8px;border-right:2px solid var(--sub);border-bottom:2px solid var(--sub);transform:rotate(45deg);margin-left:auto;transition:transform .2s}
.gd-palsd[open] summary::after{transform:rotate(-135deg)}
.gd-palsd-k{font-weight:800}.gd-palsd-n{color:var(--sub);font-size:12.5px}.gd-palsd-n b{color:var(--ok);font-size:14px}
.gd-palsd-s{margin:0 12px 8px;font-size:12px;color:var(--sub);line-height:1.6}
.gd-pals{list-style:none;margin:0;padding:0 8px 8px;display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:6px}
.gd-pals li{text-align:left;display:flex;align-items:center;gap:8px;padding:6px 8px;border-radius:10px;background:var(--paper,#fff)}
.gd-pals li svg{width:46px;height:46px;flex:none;border-radius:50%;background:color-mix(in srgb,#9fd27a 30%,var(--paper,#fff))}
.gd-pals li svg.sil{background:color-mix(in srgb,var(--sub,#888) 14%,var(--paper,#fff))}
.gd-pals li svg.sil>g{filter:brightness(0);opacity:.26}
.gd-pals li div{flex:1;text-align:left;min-width:0;display:flex;flex-direction:column;gap:1px;font-size:12px;line-height:1.5}
.gd-pals li b{font-size:13.5px}.gd-pals li span{color:var(--ink)}.gd-pals li small{color:var(--sub);font-size:11.5px}
.gd-pals li em{font-style:normal;color:var(--ok);font-weight:700}
.gd-pals li.lk b{color:var(--sub)}
.gd-fs-pb{position:absolute;top:calc(12px + env(safe-area-inset-top));left:calc(12px + env(safe-area-inset-left));height:40px;padding:0 14px;border-radius:99px;border:0;background:rgba(255,255,255,.88);color:#1f2a24;font:inherit;font-size:13px;font-weight:700;box-shadow:0 2px 8px rgba(0,0,0,.22);cursor:pointer}
.gd-fs-pb b{color:#2a9765}
.gd-fs-pals{position:absolute;left:0;right:0;bottom:0;max-height:78%;display:flex;flex-direction:column;background:#f6faf4;color:#1f2a24;border-radius:18px 18px 0 0;box-shadow:0 -4px 18px rgba(0,0,0,.25);padding-bottom:env(safe-area-inset-bottom);animation:gdSheet .25s ease-out both;--paper:#fff;--bg:#f6faf4;--ink:#1f2a24;--sub:#5a6a62;--ok:#2a9765;--line:#dfe8dc}
@keyframes gdSheet{from{transform:translateY(40px);opacity:0}to{transform:none;opacity:1}}
.gd-fs-ph{display:flex;align-items:center;gap:10px;padding:12px 12px 8px 16px}
.gd-fs-ph b{font-size:16px}.gd-fs-ph span{color:#5a6a62;font-size:12.5px}.gd-fs-ph span b{font-size:14px;color:#2a9765}
.gd-fs-pc{margin-left:auto;width:40px;height:40px;border-radius:50%;border:0;background:#e6eee3;color:#1f2a24;display:grid;place-items:center;cursor:pointer}
.gd-fs-pbd{overflow:auto;-webkit-overflow-scrolling:touch;padding:0 4px 12px}
.gd-fs-pbd .gd-palsd-s{margin:0 12px 8px}
"""
lines = s.split("\n"); li = [i for i, x in enumerate(lines) if x.startswith("<script>window.FAMD=")]; assert len(li) == 1; li = li[0]; l = lines[li]
j = l.index("window.FAMD=") + len("window.FAMD="); F, end = json.JSONDecoder().raw_decode(l[j:])
for k in ("home", "record"): F["pages"][k]["css"] += CSS
lines[li] = l[:j] + json.dumps(F, ensure_ascii=False).replace("</", "<\\/") + l[j+end:]
s = "\n".join(lines)
open(out, "w", encoding="utf-8").write(s); print("ok")
