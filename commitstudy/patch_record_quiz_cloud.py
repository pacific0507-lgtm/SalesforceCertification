"""記録ページなどで、問題集の記録(解いた問題・のべ回答・正解率)を端末のブラウザだけでなく
アカウント(クラウド)の問題集の記録からも読み、新しいほうを使う。
使い方: python3 patch_record_quiz_cloud.py <index.html> <出力>
"""
import sys
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
def rep(old, new, count):
    global s
    n = s.count(old)
    if n != count: sys.exit(f"置換対象が {n} 件(期待 {count} 件): {old[:80]!r}")
    s = s.replace(old, new)
rep("r[i].answered=Object.keys(a.hist).length);",
    "r[i].answered=Object.keys(a.hist).length,r[i].hist=a.hist,r[i].hts=+a.ts||0);", 3)
rep("e.name===`quiz`&&e.ts&&t.push({id:e.subject_id,mode:`quiz`,ts:+e.ts})",
    "e.name===`quiz`&&e.ts&&t.push({id:e.subject_id,mode:`quiz`,ts:+e.ts}),e.name===`quiz`&&r[e.subject_id]&&(()=>{let q=null;try{q=e.data&&e.data.json?JSON.parse(e.data.json):e.data}catch{}"
    "let k=r[e.subject_id],qt=q&&(+q.ts||+e.ts)||0;q&&q.hist&&qt>=(k.hts||0)&&(k.hist=q.hist,k.hts=qt,k.answered=Object.keys(q.hist).length)})()", 3)
rep("r=(()=>{try{return JSON.parse(localStorage.getItem(`sr-`+t.id+`-quiz-v1`)||`null`)}catch{return null}})(),i=r&&r.hist||{}",
    "r=(()=>{try{return JSON.parse(localStorage.getItem(`sr-`+t.id+`-quiz-v1`)||`null`)}catch{return null}})(),i=(e.perSubj&&e.perSubj[t.id]&&e.perSubj[t.id].hist)||r&&r.hist||{}", 1)
open(out, "w", encoding="utf-8").write(s); print("ok")
