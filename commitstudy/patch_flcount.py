"""問題集の「絞込」パネルに、絞り込んだ結果が何問になったかを出す(社労士版と同じ「全N問中 M問に絞り込み中」)。
  モードの下に置き、絞り込みや状態を変えるたびに更新する。0問のときは朱色。
  公開先では body が作り直されるため、CSS はスクリプトで document.head に入れる。
使い方: python3 patch_flcount.py <index.html> <出力>
"""
import sys
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count: sys.exit(f"置換対象が {n} 件(期待 {count} 件): {old[:90]!r}")
    s = s.replace(old, new)
rep('<button type=\\"button\\" data-mode=\\"exam\\">模擬試験<\\/button><\\/div>\\n  <div class=\\"mp-h\\">絞り込み<\\/div>',
    '<button type=\\"button\\" data-mode=\\"exam\\">模擬試験<\\/button><\\/div>\\n  <p class=\\"fl-count\\" id=\\"flCount\\" role=\\"status\\" aria-live=\\"polite\\"><\\/p>\\n  <div class=\\"mp-h\\">絞り込み<\\/div>')
rep('  try{dimOpts()}catch(e){}', '''  try{dimOpts()}catch(e){}
  try{(function(){var el=byId("flCount");if(!el)return;var A=ans(),n=Q.length,m=Q.filter(function(q){return baseOk(q)&&stOk(q,S.filter,A)}).length;
    el.innerHTML="全"+n+"問中 <b>"+m+"問</b>"+(m===n?"":"に絞り込み中");el.classList.toggle("zero",!m)})()}catch(e){}''')
css = ".fl-count{margin:16px 0 -6px;padding:10px 12px;border-radius:10px;background:var(--surface);border:1px solid var(--line);font-size:14px}.fl-count b{font-size:18px;color:var(--accent)}.fl-count.zero b{color:var(--shu)}.fl-count:empty{display:none}"
js = "<script>(function(){if(document.getElementById('cs-flcount'))return;var st=document.createElement('style');st.id='cs-flcount';st.textContent='" + css + "';document.head.appendChild(st)})();</script>"
rep("</head>", js + "</head>")
open(out, "w", encoding="utf-8").write(s); print("ok")
