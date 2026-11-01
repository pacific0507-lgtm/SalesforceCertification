"""キャラの掛け合いを、全員左(アイコン左・吹き出し右)にそろえる。
使い方: python3 patch_talk_left.py <index.html> <出力>
"""
import json, sys
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
def jesc(t): return json.dumps(t, ensure_ascii=False)[1:-1].replace("</", "<\\/")
anchor = jesc("body.review .co.talk{display:none}\n")
add = jesc("/* 掛け合いは全員左にそろえる */\n.tk.rou{flex-direction:row}\n.tk.rou .bub::before{left:-7px;right:auto;transform:rotate(45deg)}\n")
assert s.count(anchor) == 1
s = s.replace(anchor, anchor + add)
open(out, "w", encoding="utf-8").write(s); print("ok")
