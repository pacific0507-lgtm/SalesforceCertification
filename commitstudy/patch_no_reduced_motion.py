"""端末の「視差効果を減らす」(prefers-reduced-motion)の設定で動きを止める指定を、すべて外す(どの端末でも同じ動きにする)。
使い方: python3 patch_no_reduced_motion.py <index.html> <出力>
"""
import re, sys
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
# @media(prefers-reduced-motion:reduce){ ...{...}... } を丸ごと取り除く(中は1段の入れ子まで)
pat = re.compile(r"@media\s*\(\s*prefers-reduced-motion\s*:\s*reduce\s*\)\s*\{(?:[^{}]*\{[^{}]*\})*[^{}]*\}")
s, n = pat.subn("", s)
left = len(re.findall(r"prefers-reduced-motion", s))
if left: sys.exit(f"取り除けなかった指定が {left} 件")
open(out, "w", encoding="utf-8").write(s); print("ok", n)
