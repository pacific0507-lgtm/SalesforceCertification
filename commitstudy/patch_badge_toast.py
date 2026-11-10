"""バッジ・トロフィーの「獲得!」のお知らせが、開くたびに出ていたのを、本当に新しく獲得したときだけにする。
  原因: iPhone でアプリを開き直すと端末の保存が消えることがあり、アカウントの記録(fam-ls)を読み終える前に
  バッジを計算すると、獲得済みのバッジを「今とった」と判定していた。
  - アカウントの記録との突き合わせでは、獲得日時は早い方を残す
  - お知らせは、アカウントの記録を読み終えてから、このページを開いたあとに獲得したものだけを出す(読み終えないうちは出さない)
  - 一度知らせたバッジは cs-badge-told(アカウントに同期)に控え、二度と出さない
使い方: python3 patch_badge_toast.py <index.html> <出力>
"""
import sys
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count: sys.exit(f"置換対象が {n} 件(期待 {count} 件): {old[:90]!r}")
    s = s.replace(old, new)
rep("let a=Object.assign({},i,r),s=Object.keys(a).length;s>Object.keys(r).length&&Y(e,JSON.stringify(a)),s>Object.keys(i).length&&(o=!0)",
    "let a=Object.assign({},i,r);Object.keys(i).forEach(k=>{+i[k]&&+r[k]&&+i[k]<+r[k]&&(a[k]=i[k])});let s=Object.keys(a).length;JSON.stringify(a)!==JSON.stringify(r)&&Y(e,JSON.stringify(a)),(s>Object.keys(i).length||Object.keys(a).some(k=>a[k]!==i[k]))&&(o=!0)")
rep("}catch{}})();return Promise.race([r,new Promise(e=>setTimeout(e,2500))])}",
    "}catch{}})().finally(()=>{window.__famLsReady=1});return Promise.race([r,new Promise(e=>setTimeout(e,2500))])}")
GATE = r'''
/* ==バッジ獲得のお知らせは、アカウントの記録を読み終えてから、このページを開いたあとに獲得したものだけ== */
window.__famStart=window.__famStart||Date.now();
function csBadgeGate(list,fn){var n=0;(function wait(){if(!window.__famLsReady){if(n++<100){setTimeout(wait,200);return}return}
  /* アカウントの記録を読み終えないうちは出さない(読み込みが遅いと、獲得済みのバッジを「今とった」と判定してしまうため)。
     一度知らせたバッジは cs-badge-told(アカウントに同期)に控え、二度と出さない */
  var b={},told={};try{b=JSON.parse(localStorage.getItem("ls-badges-v1")||"{}")||{}}catch(e){}try{told=JSON.parse(localStorage.getItem("cs-badge-told")||"{}")||{}}catch(e){}
  var lim=window.__famStart-60000,ch=false;Object.keys(b).forEach(function(k){if(!told[k]&&(+b[k]||0)<lim){told[k]=+b[k]||1;ch=true}});
  var f=list.filter(function(x){return (+b[x.id]||0)>=lim&&!told[x.id]});f.forEach(function(x){told[x.id]=Date.now();ch=true});
  if(ch)try{localStorage.setItem("cs-badge-told",JSON.stringify(told))}catch(e){}
  f.__ok=1;if(f.length)fn(f)})()}
'''
rep("FAMP.record=function(){", GATE + "\nFAMP.record=function(){")
rep("function bt(e){if(!e.length)return;", "function bt(e){if(!e.length)return;if(!e.__ok)return csBadgeGate(e,bt);")
rep("function De(e){if(!e.length)return;", "function De(e){if(!e.length)return;if(!e.__ok)return csBadgeGate(e,De);")
open(out, "w", encoding="utf-8").write(s); print("ok")
