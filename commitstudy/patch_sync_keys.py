"""端末の中だけに保存していた次の記録も、アカウント(fam-ls)に同期する(2026-11-02)
  iPhone のアプリを開き直すと端末の保存が消えることがあり、お便りの「読みました」が戻るなどしていた。
  - ls-letter-v1  お便りの「読みました」
  - ls-letters-v1 これまでのお便り
  - ls-news-seen-v2 更新情報の既読
  - cs-term-known-v1 用語カードの「覚えた」
  - cs-review-v1  トレーニングの「今日の復習」の予定
  - cs-practice-v1 トレーニングの絞り込み・出し方の選択
使い方: python3 patch_sync_keys.py <index.html> <出力>
"""
import sys
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
old = "var W=[`ls-badges-v1`,`ls-goro-known-v1`,`ls-goro-pos-v1`,`ls-stamps-seen`]"
new = "var W=[`ls-badges-v1`,`ls-goro-known-v1`,`ls-goro-pos-v1`,`ls-stamps-seen`,`ls-letter-v1`,`ls-letters-v1`,`ls-news-seen-v2`,`cs-term-known-v1`,`cs-review-v1`,`cs-practice-v1`]"
n = s.count(old)
if n != 1: sys.exit(f"置換対象が {n} 件")
s = s.replace(old, new)
open(out, "w", encoding="utf-8").write(s); print("ok")
