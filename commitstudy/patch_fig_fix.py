"""図まわりの修正(2026-11-02)
  1. スマホで、図の説明文(figcaption)の「問題 N」ボタンが横に長く伸びる不具合を直す。
     原因: 横スクロールの図で `.fig.wide svg{min-width:540px}` が、ボタンの中のアイコン(svg)にも当たっていた
  2. 図の文字が枠からはみ出していたところを直す(データ変換・ストリーミングインサイトの図)
使い方: python3 patch_fig_fix.py <index.html> <出力> <d360 chapters.json> <出力chapters.json>
"""
import json, sys
src, out, chs, chout = sys.argv[1:5]
s = open(src, encoding="utf-8").read()
def rep(t, old, new, count=1):
    n = t.count(old)
    if n != count: sys.exit(f"置換対象が {n} 件(期待 {count} 件): {old[:90]!r}")
    return t.replace(old, new)
def jesc(t): return json.dumps(t, ensure_ascii=False)[1:-1].replace("</", "<\\/")
anchor = "body.review .co.talk{display:none}\n"
CSS = "/* 図の中のボタンのアイコンは、図の最小幅を当てない */\n.fig .qx-b svg,.fig button svg{min-width:0!important;max-width:none;width:12px;height:12px}\n"
s = rep(s, jesc(anchor), jesc(anchor + CSS))
open(out, "w", encoding="utf-8").write(s)

ch = json.load(open(chs, encoding="utf-8"))
FIX = [
    # データ変換: 真ん中の枠を広げ、文字を少し小さく(矢印もそれに合わせる)
    ('<rect class="gby" x="270" y="80" width="100" height="60" rx="10"/>', '<rect class="gby" x="262" y="80" width="116" height="60" rx="10"/>'),
    ('<text class="gts" x="320" y="123.6" text-anchor="middle" font-size="11.0">バッチ/ストリーミング</text>', '<text class="gts" x="320" y="123.6" text-anchor="middle" font-size="10" style="font-size:10px">バッチ/ストリーミング</text>'),
    ('x1="246" y1="110" x2="266" y2="110" marker-end="url(#ftransform-mk_aa)"', 'x1="246" y1="110" x2="258" y2="110" marker-end="url(#ftransform-mk_aa)"'),
    ('x1="372" y1="110" x2="392" y2="110" marker-end="url(#ftransform-mk_aa)"', 'x1="380" y1="110" x2="392" y2="110" marker-end="url(#ftransform-mk_aa)"'),
    # ストリーミングインサイト: 右の赤い枠を広げる
    ('<rect class="gbr" x="500" y="100" width="128" height="60" rx="10"/>', '<rect class="gbr" x="492" y="100" width="144" height="60" rx="10"/>'),
    ('x1="236" y1="175" x2="496" y2="131" stroke-dasharray="5 4" marker-end="url(#fsi-mk_ar)"', 'x1="236" y1="175" x2="488" y2="132" stroke-dasharray="5 4" marker-end="url(#fsi-mk_ar)"'),
]
for c in ch:
    h = c["data"]["html"]
    for a, b in FIX:
        if a in h: h = h.replace(a, b)
    c["data"]["html"] = h
allh = "".join(c["data"]["html"] for c in ch)
for a, b in FIX:
    if allh.count(b) != 1: sys.exit("未適用: " + a[:80])
json.dump(ch, open(chout, "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
