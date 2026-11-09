"""問題の下の「回答履歴」に、トレーニングで解いた回答も出す。
  これまでトレーニングの回答は回数の記録(hist)にだけ入り、日時つきの記録(log)に入らなかったため、
  「直近が不正解」で絞り込んだ問題でも回答履歴が空のことがあった。
  - 取り込み(takePend)のときに log にも足す(m:"train")。トレーニングの画面(practice.js の addHist)も同じように足す
  - 回答履歴ではトレーニングの回答に「トレーニング」と付け、選んだ答えがない記録はその欄を出さない
  - 前の版で解いた分など、日時の残っていない回数があれば、その数を添える
使い方: python3 patch_hist_train.py <index.html> <出力>
"""
import sys
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count: sys.exit(f"置換対象が {n} 件(期待 {count} 件): {old[:90]!r}")
    s = s.replace(old, new)
rep('if((+x.t||0)>=(+h.t||0)){h.l=x.ok?"o":"x";h.t=x.t}});',
    'if((+x.t||0)>=(+h.t||0)){h.l=x.ok?"o":"x";h.t=x.t}\n    if(!Array.isArray(S.log))S.log=[];S.log.push({i:q.n,m:"train",s:[],c:x.ok?1:0,t:+x.t||0})});\n  if(Array.isArray(S.log)){S.log.sort(function(a,b){return (a.t||0)-(b.t||0)});if(S.log.length>2000)S.log=S.log.slice(-2000)}')
rep('''  var H=(S.log||[]).filter(function(x){return x.i===q.n});
  if(!H.length)return "";
  var ok=H.filter(function(x){return x.c}).length;
  var h='<div class="hist"><div class="hist-h">回答履歴(正解 <b class="ok">'+ok+'</b>回・不正解 <b class="ng">'+(H.length-ok)+'</b>回)</div><ol class="hist-l">';''',
    '''  var H=(S.log||[]).filter(function(x){return x.i===q.n}),hh=(S.mode!=="exam"&&typeof histOf==="function")?histOf(q.n):null,more=hh?Math.max(0,(+hh.n||0)-H.length):0;
  if(!H.length&&!more)return "";
  var ok=H.filter(function(x){return x.c}).length,okAll=ok+(more?Math.max(0,Math.min(more,(+hh.c||0)-ok)):0),nAll=H.length+more;
  var h='<div class="hist"><div class="hist-h">回答履歴(正解 <b class="ok">'+okAll+'</b>回・不正解 <b class="ng">'+(nAll-okAll)+'</b>回)</div><ol class="hist-l">';''')
rep('''<span class="hd">'+fmtT(x.t)+(x.m==="exam"?" 模試":"")+'</span><span class="hs">選んだ答え: '+esc(hSelTxt(q,x.s))+"</span></li>"''',
    '''<span class="hd">'+fmtT(x.t)+(x.m==="exam"?" 模試":x.m==="train"?" トレーニング":"")+'</span>'+(x.s&&x.s.length?'<span class="hs">選んだ答え: '+esc(hSelTxt(q,x.s))+"</span>":"")+"</li>"''')
rep('''  h+="</ol>";if(H.length>10)h+='<div style="margin-top:4px">新しい10件を表示しています。</div>';''',
    '''  h+="</ol>";if(H.length>10)h+='<div style="margin-top:4px">新しい10件を表示しています。</div>';
  if(more)h+='<div style="margin-top:4px">このほか、日時の残っていない記録が'+more+'回あります(前の版やトレーニングで解いた分など)。</div>';''')
# トレーニング(practice.js の addHist。patch_sync_merge で書き換え済みの形)も log に足す
rep('CSQ.reconcile(st,CSQ.dev());st.ts=Math.max(CSQ.now(),(+st.ts||0)+1);return true}',
    'if(!Array.isArray(st.log))st.log=[];st.log.push({i:+n,m:"train",s:[],c:ok?1:0,t:t});st.log.sort(function(x,y){return (x.t||0)-(y.t||0)});if(st.log.length>2000)st.log=st.log.slice(-2000);CSQ.reconcile(st,CSQ.dev());st.ts=Math.max(CSQ.now(),(+st.ts||0)+1);return true}')
open(out, "w", encoding="utf-8").write(s); print("ok")
