"""下のタブ(メニューバー)を、端末の OS に合わせた形にする。
  - iPhone / iPad(iOS・iPadOS。Safari・Chrome・claude.ai のアプリはどれも同じ WebKit なので同じ形):
      最新の iOS のタブバーのように、画面の端から少し離して浮かべた丸いバー。すりガラス(backdrop-filter)で後ろが透け、
      選んでいるタブは色の付いたカプセルで示す。ホームインジケーターの上に置く
  - Android(Chrome など): Material 3 のナビゲーションバー。画面の幅いっぱいで、選んでいるタブはアイコンの後ろの横長の
      カプセル(アクティブインジケーター)で示し、文字は下に置く
  - そのほか(PC など)はこれまでどおり
  html に os-ios / os-android のクラスを付けて切り替える。--vb-hide(patch_vbottom.py が測る、画面の下で切れている分)だけ持ち上げる。
  公開先では body が作り直されるため、CSS はスクリプトで document.head に入れる。
使い方: python3 patch_tabbar_os.py <index.html> <出力>
"""
import sys, json
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
css = (
 # ---- iOS: 浮かべたすりガラスのバー ----
 "html.os-ios .tabbar{left:12px!important;right:12px!important;bottom:calc(max(10px,env(safe-area-inset-bottom,0px) - 6px) + var(--vb-hide,0px))!important;"
 "padding:6px!important;border:1px solid color-mix(in srgb,var(--line) 70%,transparent)!important;border-radius:32px;"
 "background:color-mix(in srgb,var(--paper) 72%,transparent)!important;-webkit-backdrop-filter:blur(22px) saturate(180%);backdrop-filter:blur(22px) saturate(180%);"
 "box-shadow:0 12px 32px -14px rgba(0,0,0,.35),inset 0 1px 0 rgba(255,255,255,.35)}"
 "html.os-ios .tabbar a{border-radius:26px;padding:6px 0 5px;font-size:10.5px;font-weight:600}"
 "html.os-ios .tabbar .tb-ind{border-radius:26px;background:color-mix(in srgb,var(--brand) 16%,transparent)!important;box-shadow:none!important}"
 "html.os-ios .tabbar a[aria-current=page]{color:var(--brand)!important}"
 "html.os-ios body{padding-bottom:calc(96px + var(--vb-hide,0px) + env(safe-area-inset-bottom,0px))!important}"
 # ---- Android: Material 3 のナビゲーションバー ----
 "html.os-android .tabbar{left:0!important;right:0!important;bottom:var(--vb-hide,0px)!important;padding:10px 6px calc(12px + env(safe-area-inset-bottom,0px))!important;"
 "border-top:0!important;border-radius:0;background:color-mix(in srgb,var(--brand) 7%,var(--paper))!important;-webkit-backdrop-filter:none;backdrop-filter:none;box-shadow:0 -1px 0 color-mix(in srgb,var(--line) 60%,transparent)}"
 "html.os-android .tabbar .tb-ind{display:none!important}"
 "html.os-android .tabbar a{gap:4px;padding:0;font-size:12px;font-weight:500;border-radius:0;color:var(--sub)}"
 "html.os-android .tabbar a svg{box-sizing:content-box;padding:4px 20px;border-radius:16px;transition:background .2s}"
 "html.os-android .tabbar a[aria-current=page]{color:var(--ink)!important;font-weight:700}"
 "html.os-android .tabbar a[aria-current=page] svg{background:color-mix(in srgb,var(--brand) 20%,transparent);color:var(--brand);transform:none!important}"
 "html.os-android body{padding-bottom:calc(84px + var(--vb-hide,0px) + env(safe-area-inset-bottom,0px))!important}"
)
JS = r"""(function(){if(window.__csTbOS)return;window.__csTbOS=1;
try{var ua=navigator.userAgent||"",ios=/iPhone|iPad|iPod/.test(ua)||(/Macintosh/.test(ua)&&navigator.maxTouchPoints>1),and=/Android/.test(ua);
  document.documentElement.classList.add(ios?"os-ios":and?"os-android":"os-other")}catch(e){}
var st=document.createElement("style");st.id="cs-tabbar-os";st.textContent=__CSS__;document.head.appendChild(st);})();"""
js = "<script>" + JS.replace("__CSS__", json.dumps(css)) + "</script>"
if s.count("</head>") != 1: sys.exit("</head> が1件ではない")
s = s.replace("</head>", js + "</head>")
open(out, "w", encoding="utf-8").write(s); print("ok")
