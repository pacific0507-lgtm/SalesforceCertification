"""CommitStudy(Data 360)の問題集を、社労士版(LaughStudy 家族版)の仕様に合わせるパッチ。
  1. 問題の並びをテキストの項目順にし、表示する番号(問N)は1から通し番号にする(記録は元の番号のまま)
  2. PC幅(980px以上)で問題集の左に問題一覧を常に出す(折りたたみ可)。本文は最大860pxで中央、前へ/答え/次へを中央にまとめる
  3. 問題一覧・しおり・回答履歴・ノートなどの「問N」表記も通し番号にそろえる
4択や検証状況など、Data 360 独自の試験形式の部分には手を入れない。
使い方: python3 patch_quiz_like_sharoushi.py <index.html> <出力先>
"""
import json, sys

src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()

def rep(old, new, count=1, where=None):
    global s
    n = s.count(old)
    if n != count:
        sys.exit(f"置換対象が {n} 件(期待 {count} 件): {old[:80]!r}")
    s = s.replace(old, new)

def jesc(t):
    """FAMD(JSON文字列)の中に埋め込まれているテンプレート用のエスケープ"""
    return json.dumps(t, ensure_ascii=False)[1:-1].replace("</", "<\\/")

# ---- テンプレート(HTML/CSS) ----
QSIDE_CSS = """
/* 問題集のPC版: 左に問題一覧(テキストの目次と同じく折りたためる)・前へ/次へを中央にまとめる(社労士版と同じ) */
.qside,.qside-open{display:none}
@media(min-width:980px){
  #qv{display:grid;grid-template-columns:290px minmax(0,1fr);gap:36px;max-width:1280px}
  #qv-in{max-width:860px;width:100%;justify-self:center}
  .qside{display:block;position:sticky;top:66px;align-self:start;max-height:calc(100vh - 82px);overflow:auto;font-size:14px;padding-right:4px}
  .qside-note{margin:0 0 8px 8px;font-size:12.5px;color:var(--muted)}
  .qside .gl-ch{font-size:13px;top:30px}
  .qside .cells{grid-template-columns:repeat(auto-fill,minmax(36px,1fr));gap:5px}
  .qside .cell{padding:4px 0;font-size:12px}
  body.view-q:not(.qlc) .mb[data-p=list]{display:none}
  body.qlc #qv{grid-template-columns:minmax(0,1fr);max-width:900px}
  body.qlc .qside{display:none}
  body.qlc.view-q .qside-open{display:block;position:fixed;left:0;top:50%;transform:translateY(-50%);z-index:30;writing-mode:vertical-rl;background:var(--accent);color:var(--accent-ink);border:0;border-radius:0 10px 10px 0;padding:14px 7px;font-weight:700;font-size:14px;cursor:pointer;box-shadow:0 4px 14px rgba(0,0,0,.2)}
  .ans{grid-template-columns:repeat(2,minmax(0,210px));justify-content:center;gap:14px}
  .qact{display:flex;justify-content:center;align-items:center;gap:14px}
  .qact>.nv:first-child,.qact>.nv:last-child{justify-self:auto}
}
"""
anchor = "body.review .co.talk{display:none}\n"
rep(jesc(anchor), jesc(anchor + QSIDE_CSS))

QSIDE_HTML = ('<div id="qv">\n'
  ' <aside class="qside" id="qside" aria-label="問題一覧"><div class="toc-h"><span>問題一覧</span><button type="button" class="chip" id="qside-fold" aria-label="問題一覧を折りたたむ">« 折りたたむ</button></div>'
  '<p class="qside-note">番号でジャンプ・項目名でその項目だけを解く</p><div id="qcells"></div></aside>\n'
  ' <button type="button" class="qside-open" id="qside-open">問題一覧を開く</button>\n'
  ' <div id="qv-in">')
rep(jesc('<div id="qv">\n <div id="qv-in">'), jesc(QSIDE_HTML))

# ---- エンジン(JS) ----
# 表示設定: 問題一覧の折りたたみ
rep('pm:CFG.pm!==false,tocc:false,talk:"on"', 'pm:CFG.pm!==false,tocc:false,qlc:false,talk:"on"')
rep('body.classList.toggle("tocc",!!prefs.tocc);body.classList.toggle("talk-off",prefs.talk==="off");',
    'body.classList.toggle("tocc",!!prefs.tocc);body.classList.toggle("qlc",!!prefs.qlc);body.classList.toggle("talk-off",prefs.talk==="off");')
rep('$("#toc-fold").onclick=function(){prefs.tocc=true;savePrefs();applyPrefs()};\n',
    '$("#toc-fold").onclick=function(){prefs.tocc=true;savePrefs();applyPrefs()};\n'
    '$("#qside-fold").onclick=function(){prefs.qlc=true;savePrefs();applyPrefs()};\n'
    '$("#qside-open").onclick=function(){prefs.qlc=false;savePrefs();applyPrefs();renderGrid()};\n')

# 並び順と通し番号
rep('  Q=arr;QMAP={};Q.forEach(function(q){QMAP[q.n]=q});\n  YRS=[];',
    '  Q=arr;QMAP={};Q.forEach(function(q){QMAP[q.n]=q});orderQ();\n  YRS=[];')
rep('function updateCounts(){',
    '/* 問題はテキストの項目順に並べ、表示する番号(d)は1から通しで振る。記録は元の番号(n)で持つので、問題を追加しても記録はずれない(社労士版と同じ) */\n'
    'function secRank(s){var ks=secKeys(),i=ks.indexOf(s);return i>=0?i:9e12}\n'
    'function orderQ(){var r={};Q.forEach(function(q){if(!(q.s in r))r[q.s]=secRank(q.s)});\n'
    '  Q.sort(function(a,b){return r[a.s]-r[b.s]||a.n-b.n});Q.forEach(function(q,i){q.d=i+1})}\n'
    'function qd(n){var q=QMAP[n];return q&&q.d?q.d:n}\n'
    'function updateCounts(){')
# 旧い並び(元の番号順)で覚えていた位置を、新しい並びでも同じ問題にする
rep('  }).map(function(q){return q.n});\n  if(S.shuffleQ)shuffle(ids);\n  deck=ids;',
    '  }).map(function(q){return q.n});\n'
    '  if(S.ordv!==2&&Q.length&&Object.keys(TITLES).length){if(!S.shuffleQ){var old=ids.slice().sort(function(a,b){return a-b}),keep=old[S.pos];if(keep!=null){var ki=ids.indexOf(keep);if(ki>=0)S.pos=ki}}S.ordv=2}\n'
    '  if(S.shuffleQ)shuffle(ids);\n  deck=ids;')
rep('  initText();buildScope();updateCounts();\n  buildDeck();render();renderAll();',
    '  initText();buildScope();updateCounts();\n'
    '  var keepN=S.ordv===2?deck[S.pos]:null;orderQ();\n'
    '  buildDeck();if(keepN!=null&&!S.shuffleQ){var kp=deck.indexOf(keepN);if(kp>=0)S.pos=kp}render();renderAll();')

# 問題一覧: 通し番号・左の問題一覧にも出す
rep("""title="'+esc(q.exam||"")+'">'+q.n+"</button>";""", """title="'+esc(q.exam||"")+'">'+q.d+"</button>";""")
rep('  $("#cells").innerHTML=h;\n}', '  gridOut(h);\n}\n'
    'function gridOut(h){$("#cells").innerHTML=h;var qc=$("#qcells");if(qc){qc.innerHTML=h;var hr=qc.querySelector(".gl-it.here");var sd=$("#qside");'
    'if(hr&&sd&&sd.offsetParent){var t=hr.offsetTop-sd.clientHeight/3;if(Math.abs(sd.scrollTop-t)>sd.clientHeight/2)sd.scrollTop=Math.max(0,t)}}}')

# 「問N」の表記を通し番号に
rep("""<span class="qn">問'+q.n+'</span>""", """<span class="qn">問'+q.d+'</span>""")
rep('(qaSrc(x)==="quiz"&&x.qn?"問"+x.qn+" ":"")', '(qaSrc(x)==="quiz"&&x.qn?"問"+qd(x.qn)+" ":"")')
rep('var ids=(S.bm||[]).filter(function(n){return QMAP[n]}).slice().sort(function(a,b){return a-b});',
    'var ids=(S.bm||[]).filter(function(n){return QMAP[n]}).slice().sort(function(a,b){return qd(a)-qd(b)});')
rep('document.createTextNode("問"+q.n+" "+(q.q.length>40', 'document.createTextNode("問"+q.d+" "+(q.q.length>40')
rep("""data-act="rgo" data-id="'+q.n+'">問'+q.n+" \"""", """data-act="rgo" data-id="'+q.n+'">問'+q.d+" \"""")
rep("""class="hq">問'+x.i+" \"""", """class="hq">問'+qd(x.i)+" \"""")
rep('function qTitle(q){return "問"+q.n+', 'function qTitle(q){return "問"+q.d+')
rep("""data-n="'+q.n+'"><small><span>問'+q.n+'</span>""", """data-n="'+q.n+'"><small><span>問'+q.d+'</span>""")
rep('title:"問"+n+(q?(q.exam?', 'title:"問"+qd(n)+(q?(q.exam?')
rep('return "【この問題】問"+q.n+"\\n"', 'return "【この問題】問"+q.d+"\\n"')

open(out, "w", encoding="utf-8").write(s)
print("ok")
