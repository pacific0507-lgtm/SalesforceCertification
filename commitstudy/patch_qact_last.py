"""問題集の最後の問題で「結果を見る」ボタンが、スマホで中央の「答え合わせ」に重なるのを直す。
  最後の問題(ボタンが「結果を見る」になるとき)だけ、幅が狭い画面では 中央のボタンを1段目、前へ/結果を見るを2段目に並べる。
使い方: python3 patch_qact_last.py <index.html> <出力>
"""
import json, sys
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count: sys.exit(f"置換対象が {n} 件(期待 {count} 件): {old[:90]!r}")
    s = s.replace(old, new)
rep("""' nv" type="button" data-act="skip">'+(last?"結果を見る":"次へ ▶")""", """' nv'+(last?" nv-res":"")+'" type="button" data-act="skip">'+(last?"結果を見る":"次へ ▶")""")
rep("""'<button class="btn nv" type="button" data-act="next">'+(last?"結果を見る":"次へ ▶")""", """'<button class="btn nv'+(last?" nv-res":"")+'" type="button" data-act="next">'+(last?"結果を見る":"次へ ▶")""")
CSS = ('<style>/* 最後の問題: 結果を見るが重ならないように */@media (max-width:460px){'
       '#actions.qact:has(.nv-res){display:grid;grid-template-columns:1fr 1fr;grid-template-areas:"c c" "p n";row-gap:12px}'
       '#actions.qact:has(.nv-res)>.nv:first-child{grid-area:p;justify-self:start}'
       '#actions.qact:has(.nv-res)>.qcen{grid-area:c}'
       '#actions.qact:has(.nv-res)>.nv-res{grid-area:n;justify-self:end}}</style>')
lines = s.split("\n"); l = lines[4]
j = l.index("window.FAMD=") + len("window.FAMD="); F, end = json.JSONDecoder().raw_decode(l[j:])
F["subject"] += CSS
lines[4] = l[:j] + json.dumps(F, ensure_ascii=False).replace("</", "<\\/") + l[j+end:]
s = "\n".join(lines)
open(out, "w", encoding="utf-8").write(s); print("ok")
