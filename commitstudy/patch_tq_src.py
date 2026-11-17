"""トレーニングの問題の見出し(「D360 問422 データアクション」の行)に、出典の種類のタグを出す(問題集の見出しと同じ色分け)。
  過去問(回と番号つき。例「過去問 v2026-09-21 Q1」「過去問 令和5年度 問1」)・オリジナル・Trailhead
  公開先では body が作り直されるため、CSS はスクリプトで document.head に入れる。
使い方: python3 patch_tq_src.py <index.html> <出力>
"""
import sys, json
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count: sys.exit(f"置換対象が {n} 件(期待 {count} 件): {old[:90]!r}")
    s = s.replace(old, new)
rep("""var h='<p class="bx-k tq-h"><span class="tq-sj" style="--gc:'+sj.color+'">'+esc(sj.short)+'</span> 問'+q.d+""",
    """var h='<p class="bx-k tq-h"><span class="tq-sj" style="--gc:'+sj.color+'">'+esc(sj.short)+'</span> 問'+q.d+tqSrc(q)+""")
rep("function renderQ(){",
    """function tqSrc(q){try{var k=q.src,t=String(q.label||""),lb;
  if(k==="th")lb="Trailhead";else if(k==="orig")lb="オリジナル";
  else{var m=t.replace(/(基本情報技術者試験|情報セキュリティマネジメント試験|公開問題|科目[AB])\\s*/g,"").replace(/\\s+/g," ").replace(/^ | $/g,"");lb="過去問"+(m&&!/^過去問/.test(m)?" "+(m.length>24?m.slice(0,24)+"…":m):"");k="past"}
  return ' <span class="tq-src tq-src-'+k+'" title="出典: '+esc(t)+'">'+esc(lb)+'</span>'}catch(e){return ""}}
function renderQ(){""")
css = (".tq-src{display:inline-block;border-radius:6px;padding:0 7px;font-size:11.5px;font-weight:700;line-height:1.7;letter-spacing:0;white-space:nowrap;max-width:100%;overflow:hidden;text-overflow:ellipsis;vertical-align:middle}"
       ".tq-src-past{background:color-mix(in srgb,#d97706 15%,var(--surface,#fff));color:color-mix(in srgb,#b45309 85%,var(--ink))}"
       ".tq-src-orig{background:color-mix(in srgb,#16a34a 14%,var(--surface,#fff));color:color-mix(in srgb,#15803d 85%,var(--ink))}"
       ".tq-src-th{background:color-mix(in srgb,#2563eb 13%,var(--surface,#fff));color:color-mix(in srgb,#1d4ed8 85%,var(--ink))}")
js = "<script>(function(){if(document.getElementById('cs-tq-src'))return;var st=document.createElement('style');st.id='cs-tq-src';st.textContent=" + json.dumps(css) + ";document.head.appendChild(st)})();</script>"
if s.count("</head>") != 1: sys.exit("</head> が1件ではない")
s = s.replace("</head>", js + "</head>")
open(out, "w", encoding="utf-8").write(s); print("ok")
