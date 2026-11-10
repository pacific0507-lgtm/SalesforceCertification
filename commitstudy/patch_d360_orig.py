"""Data 360 の出典の絞り込みに「オリジナル問題」を足し、トレーニングの出典(srcOf)でも d360 のオリジナル問題を分ける。
  あわせて、問題の並びの出典の絞り込みで「オリジナル」に Trailhead の問題が混ざっていたのを直す。
使い方: python3 patch_d360_orig.py <index.html> <出力>
"""
import sys
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
def rep(old, new):
    global s
    if s.count(old) != 1: sys.exit(f"置換対象が {s.count(old)} 件: {old[:80]!r}")
    s = s.replace(old, new)
rep('"srcs": [{"k": "past", "label": "過去問"}, {"k": "th", "label": "Trailhead(公式の確認問題)", "re": "^Trailhead"}], "quizKey": "sr-d360-quiz-v1"',
    '"srcs": [{"k": "past", "label": "過去問"}, {"k": "orig", "label": "オリジナル問題(公式ヘルプにもとづく)", "re": "^オリジナル"}, {"k": "th", "label": "Trailhead(公式の確認問題)", "re": "^Trailhead"}], "quizKey": "sr-d360-quiz-v1"')
rep('if(id==="afsales"||id==="afspec"||id==="mulepa"||id==="fe"||id==="sg"||id==="mcadmin")return /^オリジナル/',
    'if(id==="d360"||id==="afsales"||id==="afspec"||id==="mulepa"||id==="fe"||id==="sg"||id==="mcadmin")return /^オリジナル/')
# 問題の並び(buildDeck)で「オリジナル」を選ぶと過去問以外(Trailhead も)が入っていたのを、件数(baseOk)と同じ判定にそろえる
rep('if(S.src!=="all"){var so=srcOf(q);if(S.src==="orig"?so==="past":so!==S.src)return false}',
    'if(S.src!=="all"){var so=srcOf(q);if(CFG.srcs?so!==S.src:(S.src==="orig"?so==="past":so!==S.src))return false}')
rep('問題は、過去問と、Salesforce公式のTrailheadの確認問題を日本語で収録しています。',
    '問題は、過去問と、Salesforce公式のTrailheadの確認問題、公式ヘルプにもとづくオリジナル問題を日本語で収録しています。')
open(out, "w", encoding="utf-8").write(s); print("ok")
