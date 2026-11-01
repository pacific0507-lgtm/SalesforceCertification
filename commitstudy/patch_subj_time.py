"""学習の記録「科目ごとの進み具合」に、科目ごとの累計の勉強時間をはっきり出す。
  - 各科目の行に「勉強した時間(累計)」を常に表示(スマホでも1行で見える)
  - PCで科目の行が崩れていたのを直す(クラス名 x がメニューの閉じるボタン .x のスタイルと重なっていた → sx に変更)
  - 科目を押したときの「くわしい記録」に 累計・この7日・この30日 を並べる
使い方: python3 patch_subj_time.py <index.html> <出力>
"""
import json, sys
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count: sys.exit(f"置換対象が {n} 件(期待 {count} 件): {old[:90]!r}")
    s = s.replace(old, new)
def jesc(t): return json.dumps(t, ensure_ascii=False)[1:-1].replace("</", "<\\/")

rep('<div class="l x"><span>勉強した時間</span><span>`+Y(e.perSubj[t.id].t||0)+`</span></div><p class="mini">理解 `+t.d+`節・問題 `+t.a+` / `+t.qs+`問・`+Y(e.perSubj[t.id].t||0)+`</p>',
    '<div class="l tm"><span>勉強した時間(累計)</span><span>`+Y(e.perSubj[t.id].t||0)+`</span></div><p class="mini">理解 `+t.d+`節・問題 `+t.a+` / `+t.qs+`問</p>')
rep('<span>勉強した時間: この7日 `+Y(d(7))+` ・ この30日 `+Y(d(30))+`</span>',
    '<span>勉強した時間: 累計 `+Y(e.perSubj[t.id]&&e.perSubj[t.id].t||0)+` ・ この7日 `+Y(d(7))+` ・ この30日 `+Y(d(30))+`</span>')
CSS = "\n/* 科目ごとの累計の勉強時間(どの幅でも表示) */\n.subj .r .l.tm{margin-top:4px;padding-top:6px;border-top:1px dashed var(--line);font-size:13px;color:var(--ink);font-weight:700}\n.subj .r .l.tm span:last-child{color:var(--c);font-variant-numeric:tabular-nums}\n"
rep(jesc("\n.subj{display:grid;gap:0}"), jesc(CSS + "\n.subj{display:grid;gap:0}"))
rep('class="l x"', 'class="l sx"', 2)
rep('class="bar x"', 'class="bar sx"', 2)
rep('.subj .r .x{display:none}', '.subj .r .sx{display:none}')
open(out, "w", encoding="utf-8").write(s); print("ok")
