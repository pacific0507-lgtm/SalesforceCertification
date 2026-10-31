"""CommitStudy 修正パッチ(2026-11-01)
  1. 絞り込み中(例: 出典=過去問)は、絞り込んだ問題だけで 1 から通し番号を振り直し、一覧にも絞り込み中の問題だけを出す
  2. テーマ(ライト/ダーク/自動)を sr-theme にも保存し、起動部分(家族版と共通)からの復元を受け取る(社労士版と同じ)
  3. 横長の図(<figure> の 960 幅の図)が小さくならないよう、figure の余白をなくし、スマホでは横スクロールにする
使い方: python3 patch_fix_20261101.py <index.html> <chapters.json> <出力 index.html> <出力 chapters.json>
"""
import json, sys
src, chs, out, outc = sys.argv[1:5]
s = open(src, encoding="utf-8").read()

def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count:
        sys.exit(f"置換対象が {n} 件(期待 {count} 件): {old[:90]!r}")
    s = s.replace(old, new)

def jesc(t):
    return json.dumps(t, ensure_ascii=False)[1:-1].replace("</", "<\\/")

# 1. 絞り込み後の通し番号
rep('function qd(n){var q=QMAP[n];return q&&q.d?q.d:n}',
    '/* 表示する番号: 絞り込み中は、絞り込んだ問題だけで1から振る(buildDeck で作る)。絞り込みなしなら全体の通し番号と同じ */\n'
    'var DNO={},DFIL=false;function dno(q){return q?(DNO[q.n]||q.d||q.n):""}\n'
    'function qd(n){var q=QMAP[n];return q?dno(q):n}')
rep('  if(S.shuffleQ)shuffle(ids);\n  deck=ids;',
    '  DNO={};ids.forEach(function(n,i){DNO[n]=i+1});DFIL=ids.length!==Q.length;\n'
    '  if(S.shuffleQ)shuffle(ids);\n  deck=ids;')
rep("""title="'+esc(q.exam||"")+'">'+q.d+"</button>";""", """title="'+esc(q.exam||"")+'">'+dno(q)+"</button>";""")
rep('  Q.forEach(function(q){var g=gm[q.s];if(!g){g=gm[q.s]={s:q.s,qs:[]};groups.push(g)}g.qs.push(q)});\n  groups.sort(function(a,b){var x=order.indexOf(a.s)',
    '  var inD={};deck.forEach(function(n){inD[n]=1});\n'
    '  Q.forEach(function(q){if(DFIL&&!inD[q.n])return;var g=gm[q.s];if(!g){g=gm[q.s]={s:q.s,qs:[]};groups.push(g)}g.qs.push(q)});\n  groups.sort(function(a,b){var x=order.indexOf(a.s)')
rep("""<span class="qn">問'+q.d+'</span>""", """<span class="qn">問'+dno(q)+'</span>""")
rep('document.createTextNode("問"+q.d+" "+(q.q.length>40', 'document.createTextNode("問"+dno(q)+" "+(q.q.length>40')
rep("""data-act="rgo" data-id="'+q.n+'">問'+q.d+" \"""", """data-act="rgo" data-id="'+q.n+'">問'+dno(q)+" \"""")
rep('function qTitle(q){return "問"+q.d+', 'function qTitle(q){return "問"+dno(q)+')
rep("""data-n="'+q.n+'"><small><span>問'+q.d+'</span>""", """data-n="'+q.n+'"><small><span>問'+dno(q)+'</span>""")
rep('return "【この問題】問"+q.d+"\\n"', 'return "【この問題】問"+dno(q)+"\\n"')

# 2. テーマ
rep('  if(prefs.theme==="light"||prefs.theme==="dark")r.setAttribute("data-theme",prefs.theme);else r.removeAttribute("data-theme");',
    '  (function(){var t=null;try{t=localStorage.getItem("sr-theme")}catch(e){}if(t==="light"||t==="dark"||t==="auto")prefs.theme=t;else if(prefs.theme==="light"||prefs.theme==="dark"){try{localStorage.setItem("sr-theme",prefs.theme)}catch(e){}}})();'
    'if(prefs.theme==="light"||prefs.theme==="dark")r.setAttribute("data-theme",prefs.theme);else r.removeAttribute("data-theme");')
rep('prefs[k]=(k==="zoom"||k==="lh")?+v:v;savePrefs();applyPrefs()}})});',
    'prefs[k]=(k==="zoom"||k==="lh")?+v:v;if(k==="theme"){try{localStorage.setItem("sr-theme",v==="light"||v==="dark"?v:"auto")}catch(e){}}savePrefs();applyPrefs()}})});')
rep('$$(".sw").forEach(function(x){x.onclick=function(){var k=x.dataset.k;prefs[k]=!prefs[k];savePrefs();applyPrefs()}});',
    '$$(".sw").forEach(function(x){x.onclick=function(){var k=x.dataset.k;prefs[k]=!prefs[k];savePrefs();applyPrefs()}});\nwindow.__srThemeSync=applyPrefs;')
# クラウドの設定を読み込んだとき、テーマも sr-theme に写す
rep('prefs.ts=+pd.ts||0;try{localStorage.setItem(PK,JSON.stringify(prefs))}catch(e){}applyPrefs()}',
    'prefs.ts=+pd.ts||0;try{localStorage.setItem(PK,JSON.stringify(prefs));if(prefs.theme==="light"||prefs.theme==="dark"||prefs.theme==="auto")localStorage.setItem("sr-theme",prefs.theme)}catch(e){}applyPrefs()}')

# 3. 図
anchor = ".fig.wide svg{min-width:540px}"
rep(jesc(anchor), jesc(anchor + ".fig.wide.xl svg{min-width:640px}"))
rep(jesc("/* ===== 図 ===== */\n"), jesc("/* ===== 図 ===== */\n.feat figure{margin:18px 0}\n"))
open(out, "w", encoding="utf-8").write(s)

d = json.load(open(chs, encoding="utf-8")); n = 0
for c in d:
    h = c["data"]["html"]; n += h.count('<figure><div class="fig">')
    c["data"]["html"] = h.replace('<figure><div class="fig">', '<figure><div class="fig wide xl">')
if n != 3: sys.exit(f"図の置換が {n} 件")
json.dump(d, open(outc, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print("ok")
