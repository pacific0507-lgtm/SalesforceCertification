"""公表時期が違う同じ過去問を1問にまとめたもの(第一種衛生管理者。build_eisei1.py が問題のデータに s2・al を入れる)を、アプリで扱う。
  - s2: ほかの回の出典(例 ["令和7年10月公表 問1", "令和5年10月公表 問1"])。
    出題回の絞り込みは、yrOf(q)(残した問題の回)に加えて s2 のどの回を選んでも出す(yrHas)。出題回ごとの問題数(yc)も各回に数える
    答え合わせのあとの出典の行に「(同じ問題: 令和7年10月公表 問1・令和5年10月公表 問1)」を足し、出典のタグは「過去問 令和8年4月公表 問1 ほか2回」にする
    トレーニングの出典のタグも同じ(トレーニングには出題回の絞り込みはない)
  - al: まとめて消した問題の番号。番号(QMAP)で引いたときは残した問題を返す(解答ログ・AI先生の質問・トレーニングの未取り込みの結果など)。
    回答履歴(hist)は、残した問題に記録がなければ、消した問題の記録を写す(しおりは付け替える)。ほかの端末で解いた記録はその端末の数として
    合わせるので(CSQ.reconcile)、写すのは1回だけで、二重には数えない
使い方: python3 patch_pastq_same.py <index.html> <出力>
"""
import sys
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count: sys.exit(f"置換対象が {n} 件(期待 {count} 件): {old[:90]!r}")
    s = s.replace(old, new)

# ---- 問題のデータ(normQ)に s2・al を通す ----
rep('xs:d.xs||"",km:d.km||"",lw:d.lw||""};',
    'xs:d.xs||"",km:d.km||"",lw:d.lw||"",s2:Array.isArray(d.s2)?d.s2.map(String):[],al:Array.isArray(d.al)?d.al.map(Number):[]};')

# ---- 出題回: s2 の回でも出す ----
rep('function yrOf(q){',
    'function yrHas(q,y){if(yrOf(q)===y)return true;var a=q&&q.s2||[];for(var i=0;i<a.length;i++)if(yrOf({src:a[i]})===y)return true;return false}\n'
    'function yrsOf(q){var r=[],y=yrOf(q);if(y)r.push(y);(q&&q.s2||[]).forEach(function(t){var z=yrOf({src:t});if(z&&r.indexOf(z)<0)r.push(z)});return r}\n'
    'function yrOf(q){')
rep('yrOf(q)!==S.yr', '!yrHas(q,S.yr)', 2)
rep('yrOf(q)!==g("yr")', '!yrHas(q,g("yr"))')
rep('yrOf(q)===S.yr)', 'yrHas(q,S.yr))')
rep('var yc={};Q.forEach(function(q){var y=yrOf(q);if(y)yc[y]=(yc[y]||0)+1});',
    'var yc={};Q.forEach(function(q){yrsOf(q).forEach(function(y){yc[y]=(yc[y]||0)+1})});')
rep('Q.forEach(function(q){if(q.yr&&YRS.indexOf(q.yr)<0)YRS.push(q.yr)});',
    'Q.forEach(function(q){yrsOf(q).forEach(function(y){if(YRS.indexOf(y)<0)YRS.push(y)})});')

# ---- 消した問題の番号は、残した問題を指す ----
rep('Q=arr;QMAP={};Q.forEach(function(q){QMAP[q.n]=q});orderQ();',
    'Q=arr;QMAP={};Q.forEach(function(q){QMAP[q.n]=q});Q.forEach(function(q){(q.al||[]).forEach(function(o){if(!QMAP[o])QMAP[o]=q})});orderQ();')
# 回答履歴・しおりを引き継ぐ(問題を読み込んだときと、ほかの端末の記録を合わせたとき)
rep('prepQ(arr);qState=state;takePend(false);',
    'prepQ(arr);qState=state;takePend(false);qAlias();')
rep('function qRedraw(){', '''function qAlias(){var ch=false;if(!S.hist||typeof S.hist!=="object")S.hist={};if(!Array.isArray(S.bm))S.bm=[];
  Q.forEach(function(q){(q.al||[]).forEach(function(o){
    var h=S.hist[o];if(h&&(+h.n||0)>0&&!S.hist[q.n]){S.hist[q.n]=JSON.parse(JSON.stringify(h));ch=true}
    var i=S.bm.indexOf(o);if(i>=0){S.bm.splice(i,1);if(S.bm.indexOf(q.n)<0)S.bm.push(q.n);ch=true}})});
  if(ch)try{localStorage.setItem(QK,JSON.stringify(S))}catch(e){}
  return ch}
function qRedraw(){qAlias();''')

# ---- 表示: 出典の行とタグ ----
rep('if(q.src)h+=\'<br><small>\'+esc(q.src)+"</small>";',
    'if(q.src)h+=\'<br><small>\'+esc(q.src)+(q.s2&&q.s2.length?\'<span class="s2note">(同じ問題: \'+esc(q.s2.join("・"))+")</span>":"")+"</small>";')
rep('lb="過去問"+(m&&!/^過去問/.test(m)?" "+(m.length>28?m.slice(0,28)+"…":m):"")}',
    'lb="過去問"+(m&&!/^過去問/.test(m)?" "+(m.length>28?m.slice(0,28)+"…":m):"");if(q.s2&&q.s2.length){lb+=" ほか"+q.s2.length+"回";t+="(同じ問題: "+q.s2.join("・")+")"}}')
rep('sm.textContent=(q.exam||q.src||"")+" ・ "', 'sm.textContent=(q.exam||q.src||"")+(q.s2&&q.s2.length?" ほか"+q.s2.length+"回":"")+" ・ "')
# トレーニング
rep('label:d.s||"",', 'label:d.s||"",s2:Array.isArray(d.s2)?d.s2.map(String):[],')
rep('lb="過去問"+(m&&!/^過去問/.test(m)?" "+(m.length>24?m.slice(0,24)+"…":m):"");k="past"}',
    'lb="過去問"+(m&&!/^過去問/.test(m)?" "+(m.length>24?m.slice(0,24)+"…":m):"");k="past";if(q.s2&&q.s2.length){lb+=" ほか"+q.s2.length+"回";t+="(同じ問題: "+q.s2.join("・")+")"}}')
open(out, "w", encoding="utf-8").write(s); print("ok")
