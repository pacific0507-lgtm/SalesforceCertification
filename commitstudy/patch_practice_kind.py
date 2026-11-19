"""トレーニングの「科目」の上に「種類」(すべて / Salesforce / 情報処理 / その他)の絞り込みを足す。問題と用語カードの両方。
  種類を選ぶと、科目のボタンがその種類の科目だけになり、「すべて」はその種類の全科目になる。
  科目のない種類のボタンは出さない。選んだ種類は ST.kind / ST.gkind(cs-practice-v1)に残す。
  種類の分け方はテキスト一覧(patch_texts_groups.py)と同じ。新しい科目は CS_KIND に足す(載っていない科目は「その他」)。
使い方: python3 patch_practice_kind.py <index.html> <出力>
"""
import sys
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
def rep(a, b):
    global s
    n = s.count(a)
    if n != 1: sys.exit(f"{n} 件: {a[:90]}")
    s = s.replace(a, b)
rep('function subjItems(){return [{v:"all",l:"すべて"}].concat(SUBJ.map(function(s){return {v:s.id,l:s.short}}))}',
    'var CS_KIND={d360:"sf",mcadmin:"sf",afsales:"sf",afsvc:"sf",afspec:"sf",mulepa:"sf",fe:"ipa",sg:"ipa"},CS_KINDL=[["sf","Salesforce"],["ipa","情報処理"],["etc","その他"]];\n'
    'function kindOf(id){return CS_KIND[id]||"etc"}\n'
    'function kindSubj(k){return SUBJ.filter(function(s){return !k||k==="all"||kindOf(s.id)===k})}\n'
    'function kindItems(){var has={};SUBJ.forEach(function(s){has[kindOf(s.id)]=1});return [{v:"all",l:"すべて"}].concat(CS_KINDL.filter(function(k){return has[k[0]]}).map(function(k){return {v:k[0],l:k[1]}}))}\n'
    'function kindRow(id,before){var b=$(before);if(!b||document.getElementById(id))return;var lab=b.previousElementSibling,p=document.createElement("p");p.className="flt-l";p.textContent="種類";var d=document.createElement("div");d.className="flt";d.id=id;b.parentNode.insertBefore(p,lab&&lab.classList.contains("flt-l")?lab:b);b.parentNode.insertBefore(d,lab&&lab.classList.contains("flt-l")?lab:b)}\n'
    'function subjItems(k){return [{v:"all",l:"すべて"}].concat(kindSubj(k).map(function(s){return {v:s.id,l:s.short}}))}')
rep('function subjList(){return ST.subj==="all"?SUBJ.map(function(s){return s.id}):[ST.subj]}',
    'function subjList(){return ST.subj==="all"?kindSubj(ST.kind).map(function(s){return s.id}):[ST.subj]}\n'
    'function subjTag(){return ST.subj==="all"&&ST.kind&&ST.kind!=="all"?"k:"+ST.kind:ST.subj}')
rep('function snapKey(){return ST.subj+"|"', 'function snapKey(){return subjTag()+"|"')
rep('return "cs-practice-pos:"+ST.subj+":"', 'return "cs-practice-pos:"+subjTag()+":"')
rep('chips($("#f-subj"),subjItems(),ST.subj,',
    'kindRow("f-kind","#f-subj");if(ST.kind&&ST.kind!=="all"&&!kindItems().some(function(k){return k.v===ST.kind}))ST.kind="all";\n'
    '  chips($("#f-kind"),kindItems(),ST.kind||"all",function(v){ST.kind=v;if(ST.subj!=="all"&&v!=="all"&&kindOf(ST.subj)!==v)ST.subj="all";save();resetSnap();refreshQ(true)});\n'
    '  chips($("#f-subj"),subjItems(ST.kind),ST.subj,')
rep('chips($("#g-subj"),subjItems(),ST.gsubj,',
    'kindRow("g-kind","#g-subj");if(ST.gkind&&ST.gkind!=="all"&&!kindItems().some(function(k){return k.v===ST.gkind}))ST.gkind="all";\n'
    '  chips($("#g-kind"),kindItems(),ST.gkind||"all",function(v){ST.gkind=v;if(ST.gsubj!=="all"&&v!=="all"&&kindOf(ST.gsubj)!==v)ST.gsubj="all";save();TI=0;renderTerms(true)});\n'
    '  chips($("#g-subj"),subjItems(ST.gkind),ST.gsubj,')
rep('var ids=ST.gsubj==="all"?SUBJ.map(function(s){return s.id}):[ST.gsubj];',
    'var ids=ST.gsubj==="all"?kindSubj(ST.gkind).map(function(s){return s.id}):[ST.gsubj];')
open(out, "w", encoding="utf-8").write(s); print("ok")
