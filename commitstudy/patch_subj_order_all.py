"""テキスト一覧で並べ替えた科目の順番(cs-subj-order)を、科目が並ぶほかの場所すべてに反映する。
  - ホーム・テキスト一覧・学習の記録・更新情報のメニューや科目の一覧(各ページの科目リストの取得関数)
  - テキストのメニューバー「ホーム」の移動パネルの科目
  - トレーニングの科目の絞り込みと、「すべて」で順番に解くときの科目の順
使い方: python3 patch_subj_order_all.py <index.html> <出力>
"""
import sys
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count: sys.exit(f"置換対象が {n} 件(期待 {count} 件): {old[:90]!r}")
    s = s.replace(old, new)
HELP = ('window.FAMP={};\n/* 科目の並び(ユーザーごと)。cs-subj-order にない科目は元の順で後ろへ */\n'
        'window.csOrdCmp=function(){var o=[];try{o=JSON.parse(localStorage.getItem("cs-subj-order"))||[]}catch(e){}var p={};o.forEach(function(id,i){p[id]=i});'
        'return function(a,b){var x=p[a.id!=null?a.id:a],y=p[b.id!=null?b.id:b];return (x==null?999:x)-(y==null?999:y)}};\n'
        'window.csOrd=function(a){return a.slice().sort(window.csOrdCmp())};\n'
        'window.csFirstSubj=function(){var T={d360:"Data 360",mcadmin:"Marketing Cloud Administrator",afsales:"Agentforce Sales",afspec:"Agentforce スペシャリスト"};var id=csOrd(Object.keys(T))[0];return {id:id,t:T[id]}};\n')
rep("window.FAMP={};\n", HELP)
rep(".filter(e=>!window.FAM_SUBJ||window.FAM_SUBJ.includes(e.id))}", ".filter(e=>!window.FAM_SUBJ||window.FAM_SUBJ.includes(e.id)).sort(window.csOrdCmp())}", 4)
rep('<a class="bx-go pri" href="/d360/#text">Data 360 の第1章を読む', '<a class="bx-go pri" href="/`+csFirstSubj().id+`/#text">`+csFirstSubj().t+` の第1章を読む')
rep("GO_LIST.map(cell)", "csOrd(GO_LIST).map(cell)")
rep("ids:[`d360`,`mcadmin`,`afsales`,`afspec`]}]", "ids:csOrd([`d360`,`mcadmin`,`afsales`,`afspec`])}]")
i = s.index("var SUBJ=[{id:\"d360\""); j = s.index("];", i) + 2
s = s[:i] + s[i:j] + "SUBJ=csOrd(SUBJ);" + s[j:]
open(out, "w", encoding="utf-8").write(s); print("ok")
