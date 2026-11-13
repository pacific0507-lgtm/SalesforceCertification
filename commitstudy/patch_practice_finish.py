"""トレーニングで「今日の復習」「間違えた問題」「まだ解いていない」を解き終えても、同じ問題がくり返し出続けた(ループした)のを直す。
  原因: 絞り込んだ並びを固定したうえで、「次へ」で最後の問題から先頭へ戻っていた。並びは端末にも残るので、開き直しても同じ問題が出た。
  直し方(絞り込みが「すべて」以外のとき):
    - 「次へ」は、固定した並びの中で、いまの位置より後にある「まだ条件に当てはまる問題」(今日の復習なら、まだ復習日が来ている問題)へ進む。
      先頭には戻らない。ランダムでも、まだ当てはまる問題からだけ選ぶ
    - 残りがなくなったら「解き終えました」を出し、「はじめから」(並びを作り直す)を押せるようにする
    - 端末に残った並びに、もう当てはまる問題が1問もなければ、並びを作り直す(翌日に開くと、その日の復習になる)
  「前へ」で解き終えた問題に戻るのは、これまでどおりできる。
使い方: python3 patch_practice_finish.py <index.html> <出力>
"""
import sys
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count: sys.exit(f"置換対象が {n} 件(期待 {count} 件): {old[:90]!r}")
    s = s.replace(old, new)
# 条件にまだ当てはまるか
rep('function liveDeck(){',
    'function liveOk(q){if(ST.flt==="wrong")return isWrong(q);if(ST.flt==="new")return isNew(q);if(ST.flt==="review")return isDue(q);return true}\nvar FIN=null;\nfunction liveDeck(){')
# 端末に残った並びに当てはまる問題がなければ作り直す
rep('var l=sv.ids.map(function(id){return m[id]}).filter(Boolean);if(l.length){SNAP={k:k,list:l};return l}}',
    'var l=sv.ids.map(function(id){return m[id]}).filter(Boolean);if(l.length&&l.some(liveOk)){SNAP={k:k,list:l};return l}}')
rep('function resetSnap(){SNAP=null;LS.set(SNK,null)}',
    'function resetSnap(){SNAP=null;FIN=null;LS.set(SNK,null);try{LS.set(posKey(),null)}catch(e){}}')
# 選ぶ: 絞り込み中は、まだ当てはまる問題だけ。順番は保存した位置から後ろへ
rep('''function pick(){
  var d=deck();if(!d.length)return null;
  if(ST.ord==="random"){var c=d.filter(function(q){return RECENT.indexOf(q.subj+q.n)<0});if(!c.length)c=d;return c[Math.floor(Math.random()*c.length)]}
  {var pos=LS.get(posKey(),null),i=0;if(pos){var k=d.findIndex(function(q){return q.subj===pos.s&&q.n===pos.n});if(k>=0)i=k}return d[i]}''',
'''function pick(){
  var d=deck();FIN=null;if(!d.length)return null;var flt=ST.flt!=="all";
  if(ST.ord==="random"){var a=flt?d.filter(liveOk):d;if(!a.length){FIN=d.length;return null}var c=a.filter(function(q){return RECENT.indexOf(q.subj+q.n)<0&&q!==CUR});if(!c.length)c=a;return c[Math.floor(Math.random()*c.length)]}
  {var pos=LS.get(posKey(),null),i=0;if(pos&&pos.fin&&flt){FIN=d.length;return null}if(pos){var k=d.findIndex(function(q){return q.subj===pos.s&&q.n===pos.n});if(k>=0)i=k}
   if(flt){for(var j=i;j<d.length;j++)if(liveOk(d[j]))return d[j];FIN=d.length;return null}return d[i]}''')
# 進む: 絞り込み中は先頭に戻らない
rep('function advance(){if(!CUR)return;if(ST.ord==="order"){var d=deck(),i=d.indexOf(CUR),nx=d[(i+1)%d.length];if(nx)LS.set(posKey(),{s:nx.subj,n:nx.n})}',
    'function advance(){if(!CUR)return;if(ST.ord==="order"){var d=deck(),i=d.indexOf(CUR),nx=null;if(ST.flt!=="all"){for(var j=i+1;j<d.length;j++)if(liveOk(d[j])){nx=d[j];break}if(!nx)LS.set(posKey(),{fin:1})}else nx=d[(i+1)%d.length];if(nx)LS.set(posKey(),{s:nx.subj,n:nx.n})}')
# 解き終えたときの表示
rep('''  if(!CUR){box.innerHTML='<p class="bx-k">問題</p><p>'+''',
    '''  if(!CUR&&FIN){var fl={review:"今日の復習",wrong:"間違えた問題",new:"まだ解いていない問題"}[ST.flt]||"この絞り込みの問題";box.innerHTML='<p class="bx-k">問題</p><p class="tq-fin">'+fl+'を、すべて解き終えました('+FIN+'問)。おつかれさまでした。</p><p class="bx-s">'+(ST.flt==="review"?"正解した問題は次の復習日に、間違えた問題は翌日に、また今日の復習に入ります。":"「はじめから」で、いまの条件に当てはまる問題で並びを作り直します。")+'</p><div class="tq-act"><button type="button" class="bx-btn" id="tq-prev"'+(BACK.length||deck().length?"":" disabled")+'>前へ</button><button type="button" class="bx-go pri" id="tq-restart">はじめから</button></div>';return}
  if(!CUR){box.innerHTML='<p class="bx-k">問題</p><p>'+''')
# 「はじめから」と、解き終えた画面からの「前へ」
rep('else if(e.target.closest("#tq-prev"))prev(',
    'else if(e.target.closest("#tq-restart")){resetSnap();refreshQ(true)}else if(e.target.closest("#tq-prev"))prev(')
rep('function prev(){if(!CUR)return;var t=null;',
    'function prev(){var t=null;if(!CUR){if(!FIN)return;var d0=deck();t=BACK.length?BACK.pop():d0[d0.length-1];if(!t)return;if(ST.ord==="order")LS.set(posKey(),{s:t.subj,n:t.n});FIN=null;CUR=t;SEL=[];DONE=false;renderFilters();renderQ();return}')
open(out, "w", encoding="utf-8").write(s); print("ok")
