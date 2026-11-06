"""問題集の「絞込」で、過去問を回(出題日)ごとに絞れるようにする(例: v2026-08-04)。
  社労士版の「出題年度」の欄を使い回す。出典の文字(exam)の先頭が v2026-08-04 / v2026(日付不明の回)/ Sales-Con-201 のものを回として扱う。
  回のある科目だけ欄を出し、見出しは「出題回」。新しい回から順に並べ、各回の問題数を添える。
使い方: python3 patch_exam_rounds.py <index.html> <出力>
"""
import sys
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count: sys.exit(f"置換対象が {n} 件(期待 {count} 件): {old[:90]!r}")
    s = s.replace(old, new)
rep('function yrOf(q){\n  if(!q)return "";',
    'function yrOf(q){\n  if(!q)return "";var mv=/^(v\\d{4}(?:-\\d\\d-\\d\\d)?|Sales-Con-201)(?=\\s|$)/.exec(String(q.exam||q.src||""));if(mv)return mv[1];')
rep('function yrKey(y){',
    'function yrKey(y){var mv=/^v(\\d{4})(?:-(\\d\\d)-(\\d\\d))?$/.exec(String(y||""));if(mv)return +(mv[1]+(mv[2]||"00")+(mv[3]||"00"));if(y==="Sales-Con-201")return 1;')
rep('if(!YRS.length)YRS=YR_ALL.slice();', 'if(!YRS.length&&CFG.years)YRS=YR_ALL.slice();')
rep('$("#selYr").hidden=!CFG.years;', '$("#selYr").hidden=!(CFG.years||YRS.length);')
rep("""sy.innerHTML='<option value="all">出題年度: すべて</option>'+YRS.map(function(y){var n=yc[y]||0;return '<option value="'+y+'">出題年度: '+y""",
    """sy.innerHTML='<option value="all">'+(CFG.years?"出題年度":"出題回")+': すべて</option>'+YRS.map(function(y){var n=yc[y]||0;return '<option value="'+y+'">'+(CFG.years?"出題年度":"出題回")+': '+y""")
rep('selYr:"出題年度",selSrc:"出典"', 'selYr:CFG.years?"出題年度":"出題回",selSrc:"出典"')
# 選択肢の文字から見出し「出題回:」を外す(ほかの欄と同じ見た目に)
rep('u=t.replace(/^(Chapter|項目|出題年度|出典|', 'u=t.replace(/^(Chapter|項目|出題年度|出題回|出典|')
open(out, "w", encoding="utf-8").write(s); print("ok")
