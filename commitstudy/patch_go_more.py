"""テキスト画面の移動パネル(メニューバーの「ホーム」)に、「トレーニング」と「学習の記録」を足す(ホーム・テキスト一覧と同じ並びの2×2)。
使い方: python3 patch_go_more.py <index.html> <出力>
"""
import sys
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
old = "テキスト一覧</a></div>'+"
if s.count(old) != 1: sys.exit(f"置換対象が {s.count(old)} 件")
add = ("テキスト一覧</a>'+"
       "'<a class=\"go-a\" href=\"/practice/\"><svg viewBox=\"0 0 24 24\" aria-hidden=\"true\"><path d=\"M13 3L5 13.5h6L10 21l8-10.5h-6z\"/></svg>トレーニング</a>'+"
       "'<a class=\"go-a\" href=\"/record/\"><svg viewBox=\"0 0 24 24\" aria-hidden=\"true\"><path d=\"M4 20h16\"/><path d=\"M7 16v-5\"/><path d=\"M12 16V7\"/><path d=\"M17 16v-8\"/></svg>学習の記録</a></div>'+")
s = s.replace(old, add)
open(out, "w", encoding="utf-8").write(s); print("ok")
