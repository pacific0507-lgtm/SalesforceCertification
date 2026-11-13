"""トレーニングの「テキストで確認する」でテキストへ移ったあと、トレーニングへ戻れるようにする(社労士版と同じ「←〇〇に戻る」の帯)。
  戻ったときは、移る前と同じ状態にする: 同じ問題・選んだ選択肢・答え合わせ済みかどうか・「前へ」の履歴、
  用語カードなら同じカードと裏返し、全画面表示、スクロールの位置。
  - リンクに ?back=/practice/ を付ける(テキスト画面の左下に「← トレーニングに戻る」が出る。既存の仕組み ls-back-<科目>)
  - 押したときの状態を cs-practice-ret に残し、トレーニングを開いたときに3時間以内なら戻して消す
使い方: python3 patch_practice_return.py <index.html> <出力>
"""
import sys
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count: sys.exit(f"置換対象が {n} 件(期待 {count} 件): {old[:90]!r}")
    s = s.replace(old, new)
rep('var L={};function R(e)', 'var L={practice:`トレーニング`};function R(e)')
rep("href=\"/'+q.subj+'/#f-'", "href=\"/'+q.subj+'/?back=%2Fpractice%2F#f-'")
rep("href=\"/'+c.subj+'/#f-'", "href=\"/'+c.subj+'/?back=%2Fpractice%2F#f-'")
SAVE = ('function saveRet(){try{LS.set("cs-practice-ret",{ts:Date.now(),tab:ST.tab,focus:document.body.classList.contains("focus"),y:window.scrollY||0,'
        'q:CUR?{s:CUR.subj,n:CUR.n}:null,sel:SEL.slice(),done:!!DONE,back:BACK.map(function(b){return {s:b.subj,n:b.n}}),'
        'ti:TI,flip:!!FLIP,k:ST.subj+"|"+ST.src+"|"+ST.flt+"|"+ST.ord})}catch(x){}}\n')
rep('function bindQ(){var box=$("#qbox");box.addEventListener("click",function(e){var b=e.target.closest(".tq-b");if(b){choose(+b.dataset.i);return}',
    SAVE + 'function bindQ(){var box=$("#qbox");box.addEventListener("click",function(e){var b=e.target.closest(".tq-b");if(b){choose(+b.dataset.i);return}if(e.target.closest(".tq-links a[href*=\'?back=\']")){saveRet();return}')
rep('var a=e.target.closest("a");if(a){var c0=TL[TI];', 'var a=e.target.closest("a");if(a){if(/\\?back=/.test(a.getAttribute("href")||""))saveRet();var c0=TL[TI];')
RESTORE = '''  var RT=null;try{RT=LS.get("cs-practice-ret",null);LS.set("cs-practice-ret",null)}catch(x){}
  if(RT&&!(Date.now()-(+RT.ts||0)<108e5&&RT.k===ST.subj+"|"+ST.src+"|"+ST.flt+"|"+ST.ord))RT=null;
  if(RT&&(RT.tab==="g"||RT.tab==="q")){ST.tab=RT.tab;setTab(RT.tab)}
  var rq=refreshQ(true);
  if(RT)Promise.resolve(rq).then(function(){try{
    var find=function(o){if(!o)return null;var l=Q[o.s]||[];for(var i=0;i<l.length;i++)if(l[i].n===o.n)return l[i];return null};
    var q=find(RT.q);if(q){CUR=q;SEL=(RT.sel||[]).filter(function(i){return i>=0&&i<q.o.length});DONE=!!RT.done&&SEL.length>0;FIN=null;BACK=(RT.back||[]).map(find).filter(Boolean);
      if(ST.ord==="order")LS.set(posKey(),{s:q.subj,n:q.n});renderFilters();renderQ()}
    if(RT.tab==="g"&&typeof TL!=="undefined"&&TL.length){TI=Math.max(0,Math.min(TL.length-1,+RT.ti||0));drawCard();if(RT.flip){FLIP=true;$("#fc").classList.add("on")}}
    if(RT.focus)focusMode(true);
    var y=+RT.y||0;if(!RT.focus&&y>0){requestAnimationFrame(function(){window.scrollTo(0,y);setTimeout(function(){window.scrollTo(0,y)},120)})}
  }catch(x){}});
}
window.CSPractice={init:init};'''
rep('  refreshQ(true);\n}\nwindow.CSPractice={init:init};', RESTORE)
open(out, "w", encoding="utf-8").write(s); print("ok")
