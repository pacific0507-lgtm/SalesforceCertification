"""問題集の「しおり(問題集)」で、ボタンや一覧の問題番号を、画面の問題番号(絞り込み中の番号)にそろえる。
  これまでは内部の通し番号(q.n)を出していたため、「いまの問題(問271)」のように表示中の番号と食い違っていた。
  一覧の小さい字の出典も、過去問の回(src)を出す。
使い方: python3 patch_qbm_no.py <index.html> <出力>
"""
import sys
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count: sys.exit(f"置換対象が {n} 件(期待 {count} 件): {old[:90]!r}")
    s = s.replace(old, new)
rep('h.textContent=q0&&S.bm.indexOf(q0.n)>=0?"いまの問題(問"+q0.n+")のしおりを外す":"いまの問題"+(q0?"(問"+q0.n+")":"")+"にしおりを付ける"',
    'h.textContent=q0&&S.bm.indexOf(q0.n)>=0?"いまの問題(問"+dno(q0)+")のしおりを外す":"いまの問題"+(q0?"(問"+dno(q0)+")":"")+"にしおりを付ける"')
rep('d.setAttribute("aria-label","しおりを外す: 問"+q.n);', 'd.setAttribute("aria-label","しおりを外す: 問"+dno(q));')
rep('sm.textContent=(q.exam||"")+" ・ "+dk(q.s)', 'sm.textContent=(q.exam||q.src||"")+" ・ "+dk(q.s)')
open(out, "w", encoding="utf-8").write(s); print("ok")
