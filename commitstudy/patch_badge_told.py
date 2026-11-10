"""バッジのお知らせ済みの控え(cs-badge-told)を、アカウントに同期する鍵に加える(patch_badge_toast.py の csBadgeGate が使う)。
使い方: python3 patch_badge_told.py <index.html> <出力>
"""
import sys
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
old = "`cs-pals-seen`,`cs-pals-fav`]"
if s.count(old) != 1: sys.exit(f"置換対象が {s.count(old)} 件")
s = s.replace(old, "`cs-pals-seen`,`cs-pals-fav`,`cs-badge-told`]")
open(out, "w", encoding="utf-8").write(s); print("ok")
