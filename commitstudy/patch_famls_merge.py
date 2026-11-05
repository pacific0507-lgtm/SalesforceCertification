"""アカウントに同期する端末の記録(fam-ls: 使い方を見た・ニュースを読んだ・用語カードを覚えた など)が消えることがあるのを直す。
  原因: 保存が「この端末にいまある分だけ」でアカウントの記録を丸ごと置き換えていた。iPhone で端末の記録が消えたあと、
        アカウントからの読み込みが終わる前に保存が走ると、端末にない記録(例: 使い方を見た)がアカウントからも消えていた。
  直し方: アカウントからの読み込みが終わるまで保存しない(終わってから、たまっていた分をまとめて保存)。
          保存はアカウントにある記録に端末の記録を重ねる形にし、端末にない記録は消さない。
使い方: python3 patch_famls_merge.py <index.html> <出力>
"""
import sys
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count: sys.exit(f"置換対象が {n} 件(期待 {count} 件): {old[:90]!r}")
    s = s.replace(old, new)
# 保存: アカウントの記録(読み込んだもの)に端末の分を重ねる。読み込み前は保存を保留
rep("n=()=>{e&&(clearTimeout(t),t=setTimeout(()=>{let t=X(),n={};W.forEach(",
    "P=!1,M={},n=()=>{if(!e){P=!0;return}clearTimeout(t),t=setTimeout(()=>{let t=X(),n=Object.assign({},M);W.forEach(")
rep("e.set({keys:n,ts:Date.now()}).catch(()=>{})},1500))};",
    "e.set({keys:n,ts:Date.now()}).then(()=>{M=n}).catch(()=>{})},1500)};")
# 読み込み: doc は読み込み後に e へ入れる
rep("e=t.db.doc(`data/users/`+t.id+`/fam-ls`);let r=await e.get(),i=r&&r.exists&&r.data().keys||{},a=X(),o=!1;",
    "let D=t.db.doc(`data/users/`+t.id+`/fam-ls`);let r=await D.get(),i=r&&r.exists&&r.data().keys||{},a=X(),o=!1;M=Object.assign({},i);")
rep("Y(G,JSON.stringify(a)),o&&n()}catch{}})()",
    "Y(G,JSON.stringify(a)),e=D,(o||P)&&n()}catch{}})()")
open(out, "w", encoding="utf-8").write(s); print("ok")
