"""問題集の問題の見出し(問N の行)に出典を出し、見分けやすくする。
  - 出典のタグ: 過去問(回と番号つき。例「過去問 v2026-09-21 Q1」「過去問 令和8年度 問3」)・オリジナル・Trailhead を色分け
  - これまで全部が同じ丸枠だったのを、役割ごとに見た目を変える
      問N: これまでどおり濃い四角 / 出典・科目A/B: 色つきのタグ / Chapter・出題範囲: 枠なしの灰色の文字(・で区切る) / 何問目: 右寄せの小さな数字
  公開先では body が作り直されるため、CSS はスクリプトで document.head に入れる。
使い方: python3 patch_qhead.py <index.html> <出力>
"""
import sys, json
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count: sys.exit(f"置換対象が {n} 件(期待 {count} 件): {old[:90]!r}")
    s = s.replace(old, new)
rep('''<div class="qh"><span class="qn">問'+dno(q)+'</span>'+(q.km?'<span class="qt qkm">'+esc(q.km)+'</span>':"")+'<span class="qt">'+esc(CATN[catOf(q.s)]||"その他")+'</span><span class="qt">'+(S.pos+1)+" / "+deck.length+' 問目</span>'+(q.exam?'<span class="qt">'+esc(q.exam)+'</span>':"")+(q.t==="mc"&&CFG.cx&&typeof q.c==="number"?'<span class="qt">'+esc(CFG.cx[q.c]||"")+'</span>':"")+''',
    '''<div class="qh"><span class="qn">問'+dno(q)+'</span>'+qhSrc(q)+(q.km?'<span class="qt qkm qtag">'+esc(q.km)+'</span>':"")+'<span class="qt qt-ch">'+esc(CATN[catOf(q.s)]||"その他")+'</span>'+(q.t==="mc"&&CFG.cx&&typeof q.c==="number"&&CFG.cx[q.c]&&String(CATN[catOf(q.s)]||"").indexOf(CFG.cx[q.c])<0?'<span class="qt qt-cx">'+esc(CFG.cx[q.c])+'</span>':"")+(q.exam?'<span class="qt qt-cx">'+esc(q.exam)+'</span>':"")+'<span class="qt qt-pos">'+(S.pos+1)+" / "+deck.length+'</span>'+''')
# 出典のタグを作る関数(問題の画面の処理と同じ場所に置く)
rep("function isPast(q){return srcOf(q)===\"past\"}",
    '''function isPast(q){return srcOf(q)==="past"}
function qhSrc(q){try{if(!CFG.srcs)return "";var k=srcOf(q),t=String(q&&q.src||""),lb;
  if(k==="past"){var m=t.replace(/(基本情報技術者試験|情報セキュリティマネジメント試験|公開問題|科目[AB])\\s*/g,"").replace(/\\s+/g," ").replace(/^ | $/g,"");lb="過去問"+(m&&!/^過去問/.test(m)?" "+(m.length>28?m.slice(0,28)+"…":m):"")}
  else if(k==="th")lb="Trailhead";else if(k==="orig")lb="オリジナル";else{var r=CFG.srcs.filter(function(x){return x.k===k})[0];lb=r?r.label:k}
  return '<span class="qt qtag qsrc qsrc-'+k+'" title="出典: '+esc(t)+'">'+esc(lb)+'</span>'}catch(e){return ""}}''')
css = (".qh{align-items:center;gap:6px 8px}"
       ".qh .qt{border:0;border-radius:0;padding:0;background:none;font-size:12.5px;color:var(--muted)}"
       ".qh .qt-ch+.qt-cx::before{content:\"・\";margin-right:2px;color:var(--line)}"
       ".qh .qt-pos{margin-left:auto;font-family:var(--f-mono);font-size:12px;color:var(--muted);white-space:nowrap}"
       ".qh .qtag{border-radius:6px;padding:1px 8px;font-size:12px;font-weight:700;line-height:1.6;white-space:nowrap;max-width:100%;overflow:hidden;text-overflow:ellipsis}"
       ".qh .qsrc-past{background:color-mix(in srgb,#d97706 15%,var(--surface));color:color-mix(in srgb,#b45309 85%,var(--ink))}"
       ".qh .qsrc-orig{background:color-mix(in srgb,#16a34a 14%,var(--surface));color:color-mix(in srgb,#15803d 85%,var(--ink))}"
       ".qh .qsrc-th{background:color-mix(in srgb,#2563eb 13%,var(--surface));color:color-mix(in srgb,#1d4ed8 85%,var(--ink))}"
       ".qh .qkm{background:color-mix(in srgb,var(--ink) 9%,var(--surface));color:var(--ink)}"
       ".qh .qstar{margin-left:4px}")
js = "<script>(function(){if(document.getElementById('cs-qhead'))return;var st=document.createElement('style');st.id='cs-qhead';st.textContent=" + json.dumps(css) + ";document.head.appendChild(st)})();</script>"
if s.count("</head>") != 1: sys.exit("</head> が1件ではない")
s = s.replace("</head>", js + "</head>")
open(out, "w", encoding="utf-8").write(s); print("ok")
