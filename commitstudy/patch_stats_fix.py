"""問題集の「その他」の成績(回答・正解・正答率・前回まで)が、スマホで縦に伸びるのを直す。
  「前回まで…」が長く折り返すと、横並びの他の札まで同じ高さに引き伸ばされていた。
  札は中身の高さにそろえ、「前回まで」は次の行に回す。
使い方: python3 patch_stats_fix.py <index.html> <出力>
"""
import json, sys
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
CSS = ('<style>/* 成績の札が伸びないように */.stats{flex-wrap:wrap;align-items:flex-start}'
       '.stats .stat{flex:0 0 auto}.stats .stat.hs{flex-basis:100%;max-width:100%;white-space:normal}</style>')
lines = s.split("\n"); l = lines[4]
j = l.index("window.FAMD=") + len("window.FAMD="); F, end = json.JSONDecoder().raw_decode(l[j:])
F["subject"] += CSS
lines[4] = l[:j] + json.dumps(F, ensure_ascii=False).replace("</", "<\\/") + l[j+end:]
s = "\n".join(lines)
open(out, "w", encoding="utf-8").write(s); print("ok")
