/* 問題文の書式(IPA の問題用)。esc() 済みの文字列を受け取り、HTML を返す。
  1行ずつ見て、次のように組み立てる。
  - 〔見出し〕(注記) の行 → 見出しのラベル(注記は小さく添える)。括弧の中に「｜」があればその括弧は表の見出し行
    (見出し行の中に括弧を書くときは、見出し行を次の行に書く)。空の括弧「()」は、続く表に見出し行がないことを表す
  - 〔見出し〕の次の行が空行 → 本文の節の見出し(枠を作らず、空行は詰める)
  - 「｜」を含む行が続くところ → 表(1行目が見出し行)。見出し行のあとに「---」だけの行はなくてよい。
    セルの前後の半角空白は除き、全角空白(字下げ)は残す。セルの中の「。・」「 ・」では改行する(箇条書き)。
    表は画面の幅に収める(はみ出さない)。列が5つ以上・7つ以上の表は字を小さくする
  - 〔プログラム〕〔SQL 文〕の直後から、次の見出しまたは(次の行がプログラムでない)空行まで → プログラムの枠(等幅・字下げそのまま。長い行は折り返し、折り返した行は字下げの位置より少し右から続ける)
  - 「○」や全角空白で始まる行が続くところ → プログラムの枠
  - 〔図…〕などそのほかの見出しの直後から、空行・次の見出しまで → 囲みの枠
    (枠の中では、全角空白で始まる行だけが続くところは字下げした行のまま。「○」「大域:」の行を含めばプログラムの枠)
  - 空行 → 段落の区切り
  見出しのない行(本文)はそのまま。改行のない短い文は何も変えない。 */
function csQF(h){
  if(typeof h!=="string"||(h.indexOf("\n")<0&&h.indexOf("｜")<0&&h.indexOf("〔")<0))return h;
  var L=h.split("\n"),o=[],i=0;
  var cap=function(l){return /^〔[^〕]+〕/.test(l)};
  var bar=function(l){return l.indexOf("｜")>=0};
  var code=function(l){return /^(○|　|大域[:：])/.test(l)};
  var cell=function(x){return x==null?"":x.replace(/^ +| +$/g,"").replace(/(。| )・/g,"$1<br>・")};
  var pre=function(a){return '<div class="qb-code">'+a.map(function(z){var m=z.match(/^[\u3000 ]*/)[0],n=0;for(var k=0;k<m.length;k++)n+=m.charAt(k)===" "?0.5:1;
    return z===""?'<div class="qb-ce"></div>':'<div class="qb-cl" style="padding-left:'+(n+1.5)+'em;text-indent:-1.5em">'+z.slice(m.length)+"</div>"}).join("")+"</div>"};
  var tbl=function(rows,noHead){
    var n=0;rows.forEach(function(r){n=Math.max(n,r.length)});
    var t='<div class="qb-tw"><table class="qb-t'+(n>=7?" qb-c7":n>=5?" qb-c5":"")+'">';
    rows.forEach(function(r,k){var tag=k===0&&rows.length>1&&!noHead?"th":"td";t+="<tr>";
      for(var j=0;j<n;j++){var c=cell(r[j]);t+="<"+tag+">"+c+"</"+tag+">"}t+="</tr>"});
    return t+"</table></div>"};
  var takeRows=function(){var rows=[];while(i<L.length&&bar(L[i])&&!cap(L[i])){rows.push(L[i].split("｜"));i++}return rows};
  while(i<L.length){
    var l=L[i];
    if(cap(l)){
      var m=l.match(/^〔([^〕]+)〕(.*)$/),title=m[1],rest=m[2].trim(),head=null,note=[],noHead=false;
      /* 括弧の中に「｜」があれば表の見出し行、なければ注記 */
      rest=rest.replace(/[(（]([^()（）]*)[)）]/g,function(_,x){if(x==="")noHead=true;else if(x.indexOf("｜")>=0&&!head){var k=x.indexOf("。");if(k>=0){note.push(x.slice(k+1));x=x.slice(0,k)}head=x.split("｜")}else note.push(x);return ""}).trim();
      if(rest&&bar(rest)&&!head){head=rest.split("｜");rest=""}
      if(rest)note.push(rest);
      o.push('<div class="qb-cap"><span>'+title+"</span>"+(note.length?"<small>"+note.join(" ")+"</small>":"")+"</div>");
      i++;
      if(head){o.push(tbl([head].concat(takeRows())));continue}
      if(i<L.length&&bar(L[i])){o.push(tbl(takeRows(),noHead));continue}
      if(i<L.length&&L[i]===""){i++;continue}
      var isC=/プログラム|SQL|擬似/.test(title),b=[];while(i<L.length&&!cap(L[i])&&(L[i]!==""||(isC&&i+1<L.length&&code(L[i+1])))){b.push(L[i]);i++}
      if(!b.length)continue;
      if(isC||b.every(code))o.push(pre(b));
      else{var x="",j2=0;
        while(j2<b.length){if(bar(b[j2])){var rr=[];while(j2<b.length&&bar(b[j2])){rr.push(b[j2].split("｜"));j2++}x+=tbl(rr)}
          else if(code(b[j2])){var cc=[];while(j2<b.length&&code(b[j2])){cc.push(b[j2]);j2++}
            x+=cc.some(function(z){return !/^　/.test(z)})?pre(cc):cc.map(function(z){return '<div class="qb-l">'+z+"</div>"}).join("")}
          else{x+='<div class="qb-l">'+b[j2]+"</div>";j2++}}
        o.push('<div class="qb-box">'+x+"</div>")}
      continue}
    if(bar(l)){o.push(tbl(takeRows()));continue}
    if(code(l)){var c=[];while(i<L.length&&(code(L[i])||(L[i]===""&&i+1<L.length&&code(L[i+1])))){c.push(L[i]);i++}o.push(pre(c));continue}
    o.push(l===""?'<div class="qb-sp"></div>':'<div class="qb-l">'+l+"</div>");i++}
  return o.join("")}
if(typeof module!=="undefined")module.exports=csQF;
