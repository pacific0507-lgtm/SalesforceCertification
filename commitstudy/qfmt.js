/* 問題文の書式(IPA の問題用)。esc() 済みの文字列を受け取り、HTML を返す。
  1行ずつ見て、次のように組み立てる。
  - 〔見出し〕(注記) の行 → 見出しのラベル(注記は小さく添える)
  - 「｜」を含む行が続くところ → 表(1行目が見出し行)。見出し行のあとに「---」だけの行はなくてよい
  - 〔プログラム〕〔SQL 文〕の直後から、次の見出しまたは(次の行がプログラムでない)空行まで → プログラムの枠(等幅・字下げそのまま)
  - 「○」や全角空白で始まる行が続くところ → プログラムの枠
  - 〔図…〕などそのほかの見出しの直後から、空行・次の見出しまで → 囲みの枠
  - 空行 → 段落の区切り
  見出しのない行(本文)はそのまま。改行のない短い文は何も変えない。 */
function csQF(h){
  if(typeof h!=="string"||(h.indexOf("\n")<0&&h.indexOf("｜")<0&&h.indexOf("〔")<0))return h;
  var L=h.split("\n"),o=[],i=0;
  var cap=function(l){return /^〔[^〕]+〕/.test(l)};
  var bar=function(l){return l.indexOf("｜")>=0};
  var code=function(l){return /^(○|　|大域[:：])/.test(l)};
  var tbl=function(rows){
    var n=0;rows.forEach(function(r){n=Math.max(n,r.length)});
    var t='<div class="qb-tw"><table class="qb-t">';
    rows.forEach(function(r,k){var tag=k===0&&rows.length>1?"th":"td";t+="<tr>";
      for(var j=0;j<n;j++)t+="<"+tag+">"+(r[j]==null?"":r[j].trim())+"</"+tag+">";t+="</tr>"});
    return t+"</table></div>"};
  var takeRows=function(){var rows=[];while(i<L.length&&bar(L[i])){rows.push(L[i].split("｜"));i++}return rows};
  while(i<L.length){
    var l=L[i];
    if(cap(l)){
      var m=l.match(/^〔([^〕]+)〕(.*)$/),title=m[1],rest=m[2].trim(),head=null,note=[];
      /* 括弧の中に「｜」があれば表の見出し行、なければ注記 */
      rest=rest.replace(/[(（]([^()（）]*)[)）]/g,function(_,x){if(x.indexOf("｜")>=0&&!head){var k=x.indexOf("。");if(k>=0){note.push(x.slice(k+1));x=x.slice(0,k)}head=x.split("｜")}else note.push(x);return ""}).trim();
      if(rest&&bar(rest)&&!head){head=rest.split("｜");rest=""}
      if(rest)note.push(rest);
      o.push('<div class="qb-cap"><span>'+title+"</span>"+(note.length?"<small>"+note.join(" ")+"</small>":"")+"</div>");
      i++;
      if(head){o.push(tbl([head].concat(takeRows())));continue}
      if(i<L.length&&bar(L[i])){o.push(tbl(takeRows()));continue}
      var isC=/プログラム|SQL|擬似/.test(title),b=[];while(i<L.length&&!cap(L[i])&&(L[i]!==""||(isC&&i+1<L.length&&code(L[i+1])))){b.push(L[i]);i++}
      if(!b.length)continue;
      if(isC||b.every(code))o.push('<pre class="qb-code">'+b.join("\n")+"</pre>");
      else{var x="",j2=0;
        while(j2<b.length){if(bar(b[j2])){var rr=[];while(j2<b.length&&bar(b[j2])){rr.push(b[j2].split("｜"));j2++}x+=tbl(rr)}
          else if(code(b[j2])){var cc=[];while(j2<b.length&&code(b[j2])){cc.push(b[j2]);j2++}x+='<pre class="qb-code">'+cc.join("\n")+"</pre>"}
          else{x+='<div class="qb-l">'+b[j2]+"</div>";j2++}}
        o.push('<div class="qb-box">'+x+"</div>")}
      continue}
    if(bar(l)){o.push(tbl(takeRows()));continue}
    if(code(l)){var c=[];while(i<L.length&&(code(L[i])||(L[i]===""&&i+1<L.length&&code(L[i+1])))){c.push(L[i]);i++}o.push('<pre class="qb-code">'+c.join("\n")+"</pre>");continue}
    o.push(l===""?'<div class="qb-sp"></div>':'<div class="qb-l">'+l+"</div>");i++}
  return o.join("")}
if(typeof module!=="undefined")module.exports=csQF;
