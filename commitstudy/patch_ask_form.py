"""AI先生の質問欄(テキストの各項目・問題の解説の下)で、送信ボタンが入力欄の下(左)に落ちていたのを、社労士版と同じく右に並べる。
使い方: python3 patch_ask_form.py <index.html> <出力>
"""
import json, sys
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
def jesc(t): return json.dumps(t, ensure_ascii=False)[1:-1].replace("</", "<\\/")
old = jesc(".ask form{display:flex;gap:8px;align-items:flex-end;flex-wrap:wrap}")
new = jesc(".ask form{display:flex;gap:8px;align-items:flex-end;flex-wrap:nowrap}.ask form textarea{flex:1 1 auto;min-width:0;width:auto}.ask form button{flex:none}")
n = s.count(old)
if n != 1: sys.exit(f"置換対象が {n} 件")
s = s.replace(old, new)
open(out, "w", encoding="utf-8").write(s); print("ok")
