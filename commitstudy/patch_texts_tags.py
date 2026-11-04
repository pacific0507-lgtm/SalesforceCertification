"""テキスト一覧の各科目のカードに、収録されている問題の種類(過去問・Trailhead・オリジナル)と数、用語カードの枚数をタグで出す。
  数は data/catalog.json(make_catalog.py で作る)から読む。
使い方: python3 patch_texts_tags.py <index.html> <出力>
"""
import json, sys
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count: sys.exit(f"置換対象が {n} 件(期待 {count} 件): {old[:90]!r}")
    s = s.replace(old, new)
JS = r'''
/* ==テキスト一覧: 科目ごとの収録内容のタグ== */
var CS_CAT=null;
function csTextsTags(){var n=0;(function wait(){var cs=document.querySelectorAll("#groups .tx[data-id]");if(!cs.length){if(n++<60)setTimeout(wait,200);return}
  (CS_CAT||(CS_CAT=fetch(window.famURL?famURL("data/catalog.json"):"data/catalog.json").then(function(r){return r.ok?r.json():{}}).catch(function(){return {}}))).then(function(cat){
    var L=[["past","過去問"],["th","Trailhead"],["orig","オリジナル"]];
    document.querySelectorAll("#groups .tx[data-id]").forEach(function(c){var m=cat[c.dataset.id];if(!m||c.querySelector(".tx-tags"))return;
      var h=L.filter(function(x){return m.n&&m.n[x[0]]}).map(function(x){return '<span class="tg tg-'+x[0]+'">'+x[1]+' <b>'+m.n[x[0]]+'</b>問</span>'}).join("");
      if(m.terms)h+='<span class="tg tg-terms">用語カード <b>'+m.terms+'</b>枚</span>';
      if(!h)return;var p=document.createElement("p");p.className="tx-tags";p.setAttribute("aria-label","収録内容");p.innerHTML=h;
      var pg=c.querySelector(".pg");if(pg)pg.insertBefore(p,pg.firstChild);else c.appendChild(p)})})})()}
(function(){var o=FAMP.texts;FAMP.texts=function(){o();if(document.body.dataset.page==="text")csTextsTags()}})();
'''
rep("FAMP.record=function(){", JS + "\nFAMP.record=function(){")
CSS = """
/* 収録内容のタグ */
.tx .pg p.tx-tags{display:flex;flex-wrap:wrap;gap:5px;margin:0 0 4px}
.tx-tags .tg{font-size:11.5px;font-weight:700;line-height:1.6;border-radius:999px;padding:0 9px;white-space:nowrap;border:1px solid var(--hair);color:var(--sub);background:var(--paper)}
.tx-tags .tg b{font-weight:800;color:var(--ink)}
.tx-tags .tg-past{background:var(--cs);border-color:transparent;color:var(--c)}
.tx-tags .tg-past b{color:var(--c)}
"""
lines = s.split("\n"); l = lines[4]
j = l.index("window.FAMD=") + len("window.FAMD="); F, end = json.JSONDecoder().raw_decode(l[j:])
F["pages"]["texts"]["css"] += CSS
lines[4] = l[:j] + json.dumps(F, ensure_ascii=False).replace("</", "<\\/") + l[j+end:]
s = "\n".join(lines)
open(out, "w", encoding="utf-8").write(s); print("ok")
