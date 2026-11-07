"""問題文の表・〔見出し〕・プログラムを見やすく表示する(IPA の問題用)。
  書式のきまりは qfmt.js(csQF)。問題集(.qq)とトレーニング(.tq-q)の問題文に使う。
  表やプログラムの枠を入れるため、問題文の要素を p から div に変える。
使い方: python3 patch_qfmt.py <index.html> <出力>
"""
import sys, os, json
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count: sys.exit(f"置換対象が {n} 件(期待 {count} 件): {old[:90]!r}")
    s = s.replace(old, new)
js = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "qfmt.js"), encoding="utf-8").read()
js = js.replace('if(typeof module!=="undefined")module.exports=csQF;', '')
css = """.qb-l{display:block;overflow-wrap:break-word}
.qb-sp{height:.7em}
.qb-cap{margin:14px 0 6px;font-size:14px;font-weight:700;color:var(--brand,var(--accent,#333));line-height:1.5}
.qb-cap small{display:block;font-size:12px;font-weight:500;color:var(--sub,var(--muted,#666))}
.qb-tw{margin:2px 0 12px;max-width:100%;overflow:hidden}
.qb-t{width:calc(100% - 1px);max-width:100%;min-width:0;table-layout:fixed;border-collapse:collapse;font-size:13.5px;line-height:1.55;font-weight:500;white-space:normal}
.qb-t th,.qb-t td{white-space:normal;min-width:0;width:auto;word-break:break-word;border:1px solid var(--line);padding:5px 7px;text-align:left;vertical-align:top;overflow-wrap:anywhere}
.qb-t th{background:var(--accent-soft);font-weight:700}
.qb-t.qb-c5{font-size:12.5px}
.qb-t.qb-c5 th,.qb-t.qb-c5 td{padding:4px 5px}
.qb-t.qb-c7{font-size:11px;line-height:1.45}
.qb-t.qb-c7 th,.qb-t.qb-c7 td{padding:3px 3px}
.qb-code{margin:4px 0 12px;padding:10px 12px;border:1px solid var(--line);border-radius:10px;background:rgba(128,128,128,.13);color:var(--ink,inherit);font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,"Osaka-Mono","MS Gothic",monospace;font-size:13px;line-height:1.65;font-weight:500;white-space:pre-wrap;overflow-wrap:anywhere}
.qb-cl{min-height:1.65em}
.qb-ce{height:.8em}
.qb-box{margin:2px 0 12px;padding:8px 12px;border:1px solid var(--line);border-radius:10px;font-size:14.5px;line-height:1.7;font-weight:500}
.qb-box .qb-tw,.qb-box .qb-code{margin:6px 0}"""
# 公開先ではこのファイル全体が claude.ai のページの body の中に入り、科目を開くと body が作り直されるため、
# <style> をここに置くと消える。document.head に入れる(head は作り直されない)
add = "(function(){if(document.getElementById('cs-qfmt'))return;var st=document.createElement('style');st.id='cs-qfmt';st.textContent=" + json.dumps(css + "\n.qq,.mcb span,.tq-b span,.exp p,.tq-ex p{white-space:pre-wrap}") + ";document.head.appendChild(st)})();"
rep('</head>', '<script>' + js + add + '</script></head>')
rep("""h+='<p class="qq" id="q'+q.n+'-qq" data-title="'+esc(qTitle(q))+'">'+(revealed?ronHtml(q.q,q.kq,q.a==="×"?"rn-ng":"rn-ok",true):esc(q.q))+"</p>";""",
    """h+='<div class="qq" id="q'+q.n+'-qq" data-title="'+esc(qTitle(q))+'">'+csQF(revealed?ronHtml(q.q,q.kq,q.a==="×"?"rn-ng":"rn-ok",true):esc(q.q))+"</div>";""")
rep("""h+='<p class="tq-q">'+esc(q.q)+'</p>';""", """h+='<div class="tq-q">'+csQF(esc(q.q))+'</div>';""")
open(out, "w", encoding="utf-8").write(s); print("ok")
