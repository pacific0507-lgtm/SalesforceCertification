"""下のタブ・問題集のボタンなどが画面の下に埋もれる件の続き(patch_vbottom.py の直し。社労士版 2026-11-17・11-18 に合わせたもの)。
  1. 開き直したときも、前に測った位置で最初から上げる。
     これまでは、画面に触れたときに測った枠の上端(screenY - clientY)を sessionStorage(cs-vb-top)だけに控えていたので、
     開き直すと一度画面に触れるまで上がらなかった。画面の大きさと向きごとに localStorage(cs-vb-top-<長辺>x<短辺><P|L>)にも控え、開いたときから使う。
  2. iPhone のホーム画面に追加したアイコンから開くと、2回に1回ほど枠の高さが上の時計の部分(47px)だけ多く渡され、枠が画面のいちばん下まで伸びて、
     下のタブがホームバーのところに埋もれる(画面の外にははみ出していないので、これまでの測り方では 0 だった)。
     ホーム画面から開いたとき(navigator.standalone / display-mode: standalone)は、枠の下端(上端 + 枠の高さ)を、正しく開いた回の下端とくらべる:
     - 枠が画面の下端まで届いていない回を「正しい下端」として、画面の大きさと向きごとに覚える(cs-vb-ref-…)
     - 届いている回は、覚えた下端より伸びた分だけ上げる。まだ覚えていなければ 47px 上げる(社労士版の作成者の iPhone で測った差)
     ブラウザ・ふつうの Claude アプリで開いているときは、これまでどおり画面の外にはみ出した分だけ上げる。
使い方: python3 patch_vb_ref.py <index.html> <出力>
"""
import sys
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count: sys.exit(f"置換対象が {n} 件(期待 {count} 件): {old[:90]!r}")
    s = s.replace(old, new)

rep("var TK='cs-vb-top',top0=null;try{var sv=+sessionStorage.getItem(TK);if(sv>0&&sv<400)top0=sv}catch(x){}",
    "var TK='cs-vb-top',top0=null;"
    "function sk(p){return p+Math.max(screen.width,screen.height)+'x'+Math.min(screen.width,screen.height)+(window.innerWidth>window.innerHeight?'L':'P')}"
    "try{var sv=+sessionStorage.getItem(TK)||+localStorage.getItem(sk('cs-vb-top-'));if(sv>0&&sv<400)top0=sv}catch(x){}"
    "var SA=!!(navigator.standalone||(window.matchMedia&&matchMedia('(display-mode: standalone)').matches));")
rep("function tcalc(){if(top0==null){tV=0;return}var h=top0+window.innerHeight-scrH();tV=(h>=2&&h<=200)?h:0}",
    "function tcalc(){if(top0==null){tV=0;return}var bot=top0+window.innerHeight,sh=scrH(),ref=0,h;"
    "if(!SA){h=bot-sh;tV=(h>=2&&h<=200)?h:0;return}"
    "try{ref=+localStorage.getItem(sk('cs-vb-ref-'))||0}catch(x){}"
    "if(bot<sh-2){if(bot>sh-200&&(!ref||Math.abs(bot-ref)>1)){try{localStorage.setItem(sk('cs-vb-ref-'),String(Math.round(bot)))}catch(x){}}h=0}"
    "else h=ref?bot-ref:47;"
    "tV=(h>=2&&h<=200)?h:0}")
rep("try{sessionStorage.setItem(TK,String(d))}catch(x){}",
    "try{sessionStorage.setItem(TK,String(d));localStorage.setItem(sk('cs-vb-top-'),String(d))}catch(x){}")
open(out, "w", encoding="utf-8").write(s); print("ok")
