"""テキスト一覧の科目のグループを、資格の種類で「Salesforce」「情報処理技術者試験」「その他」に分ける。
  科目のない グループは出さない。並べ替え・合格の印(patch_texts_order.py)は各グループの中で動く(グループに data-k を付ける)。
  新しい科目を足すときは、下の3つの並びのどれかに科目IDを足す(「その他」は衛生管理者など)。
使い方: python3 patch_texts_groups.py <index.html> <出力>
"""
import sys
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
def rep(a, b):
    global s
    n = s.count(a)
    if n != 1: sys.exit(f"{n} 件: {a[:90]}")
    s = s.replace(a, b)
rep("K=[{title:`Salesforce・情報処理技術者試験`,ids:csOrd([`d360`,`mcadmin`,`afsales`,`afsvc`,`afspec`,`mulepa`,`fe`,`sg`])}]",
    "K=[{title:`Salesforce`,ids:csOrd([`d360`,`mcadmin`,`afsales`,`afsvc`,`afspec`,`mulepa`])},{title:`情報処理技術者試験`,ids:csOrd([`fe`,`sg`])},{title:`その他`,ids:csOrd([`eisei1`])}]")
rep("i.className=`grp`,i.innerHTML=`<h2></h2><div class=\"list\"></div>`,G(`h2`,i).textContent=r.title,",
    "i.className=`grp`,i.dataset.k=`1`,i.innerHTML=`<h2></h2><div class=\"list\"></div>`,G(`h2`,i).textContent=r.title,")
rep("M(s,()=>s.querySelectorAll(`.bar i`).forEach(e=>e.style.width=e.dataset.w+`%`))}),n.appendChild(i)})",
    "M(s,()=>s.querySelectorAll(`.bar i`).forEach(e=>e.style.width=e.dataset.w+`%`))}),G(`.list`,i).children.length&&n.appendChild(i)})")
open(out, "w", encoding="utf-8").write(s); print("ok")
