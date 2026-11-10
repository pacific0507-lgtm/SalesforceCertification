"""Trailhead のモジュールのクイズ(出典が「Trailhead:」で始まる問題)を、問題集・トレーニングの出典の絞り込みで「Trailhead のクイズ」として分ける。
  対象: Marketing Cloud Administrator・Agentforce Sales・Agentforce スペシャリスト・MuleSoft Platform Architect。
  あわせて、トレーニングの出典(srcOf)で Marketing Cloud の問題がすべて「オリジナル」扱いになっていたのを直す(過去問を足したあとも残っていた)。
使い方: python3 patch_trailhead_src.py <index.html> <出力>
"""
import sys
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count: sys.exit(f"置換対象が {n} 件(期待 {count} 件): {old[:90]!r}")
    s = s.replace(old, new)
TH = ', {"k": "th", "label": "Trailhead のクイズ", "re": "^Trailhead"}'
for sid, lab in (("mcadmin", "公式ヘルプ"), ("afsales", "公式ヘルプ"), ("afspec", "公式ヘルプ"), ("mulepa", "公式ドキュメント")):
    old = sid + ':{"key": "sr-' + sid + '", "quizKey": "sr-' + sid + '-quiz-v1", "legacyPrefs": null, "srcs": [{"k": "past", "label": "過去問"}, {"k": "orig", "label": "オリジナル問題(' + lab + 'にもとづく)", "re": "^オリジナル"}]'
    rep(old, old[:-1] + TH + "]")
rep('if(id==="mcadmin")return "orig";if(id==="afsales"||id==="afspec"||id==="mulepa"||id==="fe"||id==="sg"||id==="mcadmin")return /^オリジナル/.test(s)?"orig":"past";',
    'if(id==="afsales"||id==="afspec"||id==="mulepa"||id==="fe"||id==="sg"||id==="mcadmin")return /^オリジナル/.test(s)?"orig":/^Trailhead/.test(s)?"th":"past";')
open(out, "w", encoding="utf-8").write(s); print("ok")
