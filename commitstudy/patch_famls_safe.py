"""アカウントに写している端末の記録(fam-ls: バッジ・お知らせ済みのバッジ・学習計画・覚えたカード・トレーニングの設定など)を、
読み込みが遅いときや失敗したときにも、端末の分だけで上書きしない・「バッジ獲得!」を取り済みのバッジで出さないようにする
(社労士版 2026-11-17 の直しに合わせたもの)。
  これまで:
    - 開いたときの読み込みが1回失敗すると、その回は二度と読み直さず、アカウントと合わせないままだった。
    - 失敗しても「読み終えた」の印(window.__famLsReady)を立てていたので、端末の記録が消えていた iPhone では、
      取り済みのバッジを「今とった」と判定して「バッジ獲得!」を出していた。
    - 新しい端末(端末の記録が空)で読み込みが遅いと、読み終える前に画面が書いた初めの値(トレーニングの絞り込みなど)が
      「端末の方が新しい」とみなされ、アカウントの値を上書きしていた。
  直し方:
    - 開いたときの読み込みは3回まで試す(1.5秒・3秒あけて)。それでもだめなら30秒後にもう一度読み直す。
      読み終えて合わせるまでは、これまでどおりアカウントへは保存しない(保存は必ず読み直して合わせてから)。
    - 「読み終えた」の印は、読み終えて合わせたとき(アカウントにつながっていないときも)だけ立てる。
      失敗したときはバッジのお知らせを出さない(csBadgeGate は印を最長20秒待ち、立たなければ出さない)。
    - 開いたときに端末になかった鍵へ、読み終える前に書いた値は時刻0とし、アカウントに値があればそちらを使う
      (画面が初めの値を書いても上書きしない。開いたときに端末にあった鍵を変えたとき・読み込みをあきらめたあとに書いたときは、これまでどおり新しい方)。
    - 更新情報の既読(ls-news-seen-v2: 読んだ件数)と使い方を見た時刻(cs-guide-seen)は、大きい方を使う(上の時刻0で既読が戻らないように)。
使い方: python3 patch_famls_safe.py <index.html> <出力>
"""
import sys
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count: sys.exit(f"置換対象が {n} 件(期待 {count} 件): {old[:90]!r}")
    s = s.replace(old, new)

# 1) 既読の件数・使い方を見た時刻は大きい方(sync_lib.js の famMerge。埋め込み済みのライブラリを直す)
rep('} else { if (c && typeof c.v === "string" && (lv == null || (+c.ts || 0) > lts)) {',
    '} else if (e === "ls-news-seen-v2" || e === "cs-guide-seen") { if (lv == null && !(c && typeof c.v === "string")) return; '
    'var mx = String(Math.max(+lv || 0, c ? +c.v || 0 : 0)); if (mx !== lv) io.set(e, mx); '
    'out[nm] = { v: mx, ts: Math.max(lts, c ? +c.ts || 0 : 0) || now() }; '
    '} else { if (c && typeof c.v === "string" && (lv == null || (+c.ts || 0) > lts)) {')

# 2) 読み終える前に、端末になかった鍵へ書いた値は時刻0(アカウントの値を優先)
rep('Q.push((k,v,o)=>{if(W.includes(k)){let t=X();t[k]=CSQ.now(),',
    'let AB={};try{W.forEach(k=>{J(k)==null&&(AB[k]=1)})}catch{}'
    'Q.push((k,v,o)=>{if(W.includes(k)){let t=X();t[k]=!e&&!window.__famLsFail&&AB[k]?0:CSQ.now(),')

# 3) 開いたときの読み込み: 3回まで試し、だめなら30秒後にもう一度。「読み終えた」の印は合わせたときだけ
rep('let r=(async()=>{try{let t=await Z();if(!t)return;let D=t.db.doc(`data/users/`+t.id+`/fam-ls`);let r=await D.get(),k=r&&r.exists&&r.data().keys||{},m=CSQ.famMerge(W,k,io);e=D;(m.changed||P)&&await D.set({keys:m.keys,ts:CSQ.now()})}catch{}})().finally(()=>{window.__famLsReady=1});',
    'let L=async()=>{let t=await Z();if(!t)return;let D=t.db.doc(`data/users/`+t.id+`/fam-ls`);let r=await D.get(),k=r&&r.exists&&r.data().keys||{},m=CSQ.famMerge(W,k,io);e=D;window.__famLsReady=1;window.__famLsFail=0;'
    'try{(m.changed||P)&&await D.set({keys:m.keys,ts:CSQ.now()})}catch{n()}},'
    'r=(async()=>{for(let i=0;;i++){try{await L();window.__famLsReady=1;return}catch{}if(i>=2)break;await new Promise(x=>setTimeout(x,1500*(i+1)))}'
    'window.__famLsFail=1;setTimeout(()=>{e||L().catch(()=>{})},3e4)})();')
open(out, "w", encoding="utf-8").write(s); print("ok")
