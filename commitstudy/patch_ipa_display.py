"""IPA の問題(基本情報・情報セキュリティ)を正しく表示するための修正。
  1. (改行の表示は patch_qfmt.py に移した)
  2. 選択肢の記号を J まで(科目B には選択肢が9〜10個の問題がある)
  3. 出題回の絞り込みで、旧形式のデータ(出典が src に入る)でも「令和N年度」をまとめ、サンプル問題は「サンプル問題」、修了試験は「令和N年度 修了試験」にまとめる
使い方: python3 patch_ipa_display.py <index.html> <出力>
"""
import sys
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count: sys.exit(f"置換対象が {n} 件(期待 {count} 件): {old[:90]!r}")
    s = s.replace(old, new)
rep('LETM="ABCDEFGH"', 'LETM="ABCDEFGHIJ"')
rep('"ABCDEFGH".charAt(i)', '"ABCDEFGHIJ".charAt(i)', 2)
rep('var e=String(q.exam||"").replace(/[０-９]/g', 'var e=String(q.exam||q.src||"").replace(/[０-９]/g')
rep('var i=e.indexOf("年度");if(i<0)return "";', 'if(e.indexOf("サンプル問題")>=0)return "サンプル問題";var i=e.indexOf("年度");if(i<0)return "";')
# 改行の表示(pre-wrap)は patch_qfmt.py が document.head に入れる(body に置くと科目を開いたときに消えるため)
# 修了試験(科目A免除の修了認定に係る試験)は、公開問題と分けて「令和N年度 修了試験」にまとめる
rep('  return era+num+"年度";\n}', '  return era+num+"年度"+(e.indexOf("修了認定")>=0?" 修了試験":"");\n}')
open(out, "w", encoding="utf-8").write(s); print("ok")
