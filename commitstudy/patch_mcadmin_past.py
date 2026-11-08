"""科目 Marketing Cloud Administrator(mcadmin)に過去問を足したので、出典の絞り込みに「過去問」を加える(mulepa と同じ)。
  出典の先頭が「オリジナル」ならオリジナル問題、それ以外は過去問。過去問を先に並べる。
使い方: python3 patch_mcadmin_past.py <index.html> <出力>
"""
import sys
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count: sys.exit(f"置換対象が {n} 件(期待 {count} 件): {old[:90]!r}")
    s = s.replace(old, new)
rep('mcadmin:{"key": "sr-mcadmin", "quizKey": "sr-mcadmin-quiz-v1", "legacyPrefs": null, "srcs": [{"k": "orig", "label": "オリジナル問題(公式ヘルプにもとづく)"}]',
    'mcadmin:{"key": "sr-mcadmin", "quizKey": "sr-mcadmin-quiz-v1", "legacyPrefs": null, "srcs": [{"k": "past", "label": "過去問"}, {"k": "orig", "label": "オリジナル問題(公式ヘルプにもとづく)", "re": "^オリジナル"}]')
rep('if(id==="afsales"||id==="afspec"||id==="mulepa"||id==="fe"||id==="sg")return /^オリジナル/.test(s)?"orig":"past";',
    'if(id==="afsales"||id==="afspec"||id==="mulepa"||id==="fe"||id==="sg"||id==="mcadmin")return /^オリジナル/.test(s)?"orig":"past";')
open(out, "w", encoding="utf-8").write(s); print("ok")
