"""問題集で、問題ごとの「科目A」「科目B」(データの km)を問題番号の横に表示し、絞込に「科目A・B」の欄を足す。
  km を持つ科目(基本情報技術者・情報セキュリティマネジメント)だけ欄を出す。km のない科目は今までどおり。
使い方: python3 patch_kamoku.py <index.html> <出力>
"""
import sys
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count: sys.exit(f"置換対象が {n} 件(期待 {count} 件): {old[:90]!r}")
    s = s.replace(old, new)
# データの km を読む
rep('xs:d.xs||""};', 'xs:d.xs||"",km:d.km||""};')
# 問題番号の横に表示
rep("""<span class="qn">問'+dno(q)+'</span>""", """<span class="qn">問'+dno(q)+'</span>'+(q.km?'<span class="qt qkm">'+esc(q.km)+'</span>':"")+'""")
# 状態の初期値
rep('vf:"all",cx:"all",', 'vf:"all",cx:"all",km:"all",')
# 絞り込み(baseOk と buildDeck)
rep('if(S.cx!=="all"&&String(q.c)!==S.cx)return false;', 'if(S.cx!=="all"&&String(q.c)!==S.cx)return false;\n  if((S.km||"all")!=="all"&&q.km!==S.km)return false;', 2)
# 選択肢の件数(dimOpts)
rep('if(g("cx")!=="all"&&String(q.c)!==g("cx"))return false;', 'if(g("cx")!=="all"&&String(q.c)!==g("cx"))return false;\n    if((g("km")||"all")!=="all"&&q.km!==g("km"))return false;')
rep('M={selCat:"cat",selFeat:"feat",selYr:"yr",', 'M={selCat:"cat",selFeat:"feat",selKm:"km",selYr:"yr",')
# 欄(出題回の上)
rep('<select id=\\"selYr\\" aria-label=\\"出題年度\\"><\\/select>', '<select id=\\"selKm\\" aria-label=\\"科目A・B\\" hidden><\\/select>\\n   <select id=\\"selYr\\" aria-label=\\"出題年度\\"><\\/select>')
rep('  sy.value=S.yr;', '''  sy.value=S.yr;
  (function(){var sk=$("#selKm");if(!sk)return;var kc={};Q.forEach(function(q){if(q.km)kc[q.km]=(kc[q.km]||0)+1});var kk=Object.keys(kc).sort();sk.hidden=kk.length<2;
    var sig=kk.map(function(k){return k+kc[k]}).join("|");if(sk.dataset.sig!==sig){sk.innerHTML='<option value="all">すべて</option>'+kk.map(function(k){return '<option value="'+esc(k)+'">'+esc(k)+"("+kc[k]+"問)</option>"}).join("");sk.dataset.sig=sig}
    if(Q.length&&(S.km||"all")!=="all"&&!kc[S.km]){S.km="all";buildDeck()}sk.value=S.km||"all"})();''')
rep('$("#selYr").onchange=function(){S.yr=this.value;S.pos=0;buildDeck();saveQ();renderAll()};',
    '$("#selYr").onchange=function(){S.yr=this.value;S.pos=0;buildDeck();saveQ();renderAll()};\nif($("#selKm"))$("#selKm").onchange=function(){S.km=this.value;S.pos=0;buildDeck();saveQ();renderAll()};')
rep('var FLL={selCat:"Chapter",selFeat:"項目",', 'var FLL={selCat:"Chapter",selFeat:"項目",selKm:"科目A・B",')
rep('if(S.cx!=="all")parts.push(', 'if((S.km||"all")!=="all")parts.push(S.km);\n  if(S.cx!=="all")parts.push(')
rep('$("#selYr").innerHTML="";', '$("#selYr").innerHTML="";if($("#selKm")){$("#selKm").innerHTML="";$("#selKm").dataset.sig=""}', 2)
open(out, "w", encoding="utf-8").write(s); print("ok")
