"""問題集を開き直したとき、前回見ていた「問題そのもの」から再開する(2026-11-02)
  これまでは前回の「何番目(S.pos)」だけを覚えていたため、「未回答」などの絞り込みで開き直すと
  解いた問題が抜けて並びが詰まり、前回より先の問題(例: 5/35 → 開き直すと 5/29)から始まっていた。
  - 保存のたびに、いま表示している問題の番号を S.curN に控える(開き直して前回の問題に戻るまでは上書きしない)
  - 開き直したとき(本文の読み込み後・アカウントの記録の読み込み後・画面に戻ったとき)は、絞り込みを計算し直した並びの中で
    S.curN の位置へ移る。その問題が絞り込みから外れていても(解いて「未回答」から抜けたなど)、並びのテキスト順の位置に残して同じ問題を開く(2026-11-05)
使い方: python3 patch_quiz_pos.py <index.html> <出力>
"""
import sys
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count: sys.exit(f"置換対象が {n} 件(期待 {count} 件): {old[:90]!r}")
    s = s.replace(old, new)
rep("function saveQ(){S.ts=Date.now();",
    "var posOK=false;\n"
    "function restorePos(){if(!Q.length)return;if(S.shuffleQ||S.curN==null){posOK=true;return}var i=deck.indexOf(S.curN);\n"
    "  if(i<0){var ord={};Q.forEach(function(q,k){ord[q.n]=k});var r=ord[S.curN];if(r==null)return;i=deck.findIndex(function(n){return ord[n]>r});if(i<0)i=deck.length;deck.splice(i,0,S.curN)}S.pos=i;posOK=true}\n"
    "function saveQ(){S.ts=Date.now();if(posOK&&deck&&deck.length&&deck[S.pos]!=null)S.curN=deck[S.pos];")
rep("buildDeck();if(keepN!=null&&!S.shuffleQ){var kp=deck.indexOf(keepN);if(kp>=0)S.pos=kp}render();",
    "buildDeck();if(keepN!=null&&!S.shuffleQ){var kp=deck.indexOf(keepN);if(kp>=0)S.pos=kp}restorePos();render();")
rep("try{localStorage.setItem(QK,JSON.stringify(S))}catch(e){}buildDeck();renderAll()}",
    "try{localStorage.setItem(QK,JSON.stringify(S))}catch(e){}buildDeck();restorePos();renderAll()}")
rep("    takePend(true);buildDeck();renderAll();try{mountQx()}catch(e){}}).catch(function(){})}",
    "    takePend(true);buildDeck();restorePos();renderAll();try{mountQx()}catch(e){}}).catch(function(){})}")
# 問題の読み込み直後・キャッシュからの表示・クラウドの未反映分の取り込み後にも、前回の問題へ(それまでは curN を上書きしない)
rep("buildDeck();updateCounts();renderAll();try{mountQx", "buildDeck();restorePos();updateCounts();renderAll();try{mountQx")
rep("buildDeck();updateCounts();\n(async function(){var ", "buildDeck();restorePos();updateCounts();\n(async function(){var ")
rep("if(takePend(true)){buildDeck();renderAll()}", "if(takePend(true)){buildDeck();restorePos();renderAll()}")
open(out, "w", encoding="utf-8").write(s); print("ok")
