"""ホームの「お便り」「更新情報の帯」「はじめての方へ」の既読を、アカウントの記録(fam-ls)を読み終えてから判定する。
  iPhone でアプリを開き直したり、公開し直した版を開いたりすると端末の保存が消えることがあり、
  アカウントの記録を読み終える前に判定して、「読みました」を押したお便りなどがまた出ていた。
  (アカウントの記録の読み込みは patch_badge_toast.py で window.__famLsReady を立てる。最長8秒待つ)
使い方: python3 patch_home_wait.py <index.html> <出力>
"""
import sys
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count: sys.exit(f"置換対象が {n} 件(期待 {count} 件): {old[:90]!r}")
    s = s.replace(old, new)
rep("function Nt(e,t,n){if(!e)return;", "function Nt(e,t,n){if(!e)return;if(!window.__famLsReady&&(Nt.w=(Nt.w||0)+1)<=40){e.hidden=!0;return void setTimeout(()=>Nt(e,t,n),200)}")
rep("tn($(`#news-banner`))", "(function w(k){window.__famLsReady||k>40?tn($(`#news-banner`)):setTimeout(()=>w(k+1),200)})(0)")
rep('var seen=null;try{seen=localStorage.getItem("cs-guide-seen")}catch(e){}', 'csGuideCta()}catch(e){}}\nfunction csGuideCta(){try{if(!window.__famLsReady&&(csGuideCta.w=(csGuideCta.w||0)+1)<=40)return void setTimeout(csGuideCta,200);var lead=document.querySelector(".hero .lead");\n  var seen=null;try{seen=localStorage.getItem("cs-guide-seen")}catch(e){}')
open(out, "w", encoding="utf-8").write(s); print("ok")
