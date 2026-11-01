"""絞り込みの選択肢から「Chapter:」「出題年度:」などの見出しを外し、各選択欄の左にラベルを置く。
使い方: python3 patch_fl_labels.py <index.html> <出力>
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
CSS = """
/* 絞り込み: 左にどの絞り込みか、右に選んでいる値 */
.flr{display:grid;grid-template-columns:6.2em minmax(0,1fr);align-items:center;gap:8px}
.flr>span{font-size:13px;font-weight:700;color:var(--muted);line-height:1.35}
.flr select{width:100%}
.flr:has(>select[hidden]){display:none}
"""
anchor = "body.review .co.talk{display:none}\n"
rep(jesc(anchor), jesc(anchor + CSS))
JS = r'''
/* 絞り込みの各選択欄に見出しを付け、選択肢の文字からは見出しを外す */
var FLL={selCat:"Chapter",selFeat:"項目",selYr:"出題年度",selSrc:"出典",selV:"検証状況",selCx:"",selFilter:"状態"};
function flLabels(){
  Object.keys(FLL).forEach(function(id){var el=byId(id);if(!el)return;
    if(!el.parentElement.classList.contains("flr")){var w=document.createElement("div");w.className="flr";var sp2=document.createElement("span");sp2.textContent=FLL[id]||CFG.cxLabel||"試験セクション";sp2.id=id+"-l";el.parentElement.insertBefore(w,el);w.appendChild(sp2);w.appendChild(el);el.setAttribute("aria-labelledby",sp2.id)}
    $$("option",el).forEach(function(o){var t=o.textContent,u=t.replace(/^(Chapter|項目|出題年度|出典|検証状況|出題範囲|試験セクション|状態)[:：]\s*/,"");if(u!==t)o.textContent=u})});
}
'''
rep("function dimOpts(){", JS + "function dimOpts(){")
rep("  try{dimOpts()}catch(e){}\n}", "  try{dimOpts()}catch(e){}\n  try{flLabels()}catch(e){}\n}")
open(out, "w", encoding="utf-8").write(s); print("ok")
