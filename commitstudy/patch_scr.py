"""テキストの「実際の画面」(screens/apply_screens.py が入れる figure.scr)を表示する。
  - 画像は data-scr に置き、表示するときに famURL() で公開先の URL にして src に入れる(本文は後から描かれるので MutationObserver で見張る)
  - 画像を押すと、画面いっぱいに拡大(横にスクロール・ピンチで拡大できる)。×・背景・Esc で閉じる
  公開先では body が作り直されるため、CSS はスクリプトで document.head に入れる。
使い方: python3 patch_scr.py <index.html> <出力>
"""
import sys, json
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
css = (".scr-g{margin:18px 0 14px;padding:12px 12px 10px;border:1px solid var(--line);border-radius:14px;background:var(--surface)}"
       ".scr-h{margin:0 0 8px;font-size:14px;font-weight:800;display:flex;align-items:center;gap:6px}"
       ".scr-h::before{content:\"\";width:16px;height:12px;border:2px solid currentColor;border-radius:3px;opacity:.7}"
       "figure.scr{margin:0 0 12px}"
       ".scr-z{display:block;width:100%;padding:0;margin:0;border:1px solid var(--line);border-radius:10px;overflow:hidden;background:#fff;cursor:zoom-in}"
       ".scr-z img{display:block;width:100%;height:auto}"
       "figure.scr figcaption{margin-top:6px;font-size:13px;line-height:1.7;color:var(--ink)}"
       "figure.scr figcaption b{font-weight:800}"
       ".scr-src{margin:2px 0 0;font-size:11.5px;color:var(--muted,#777);line-height:1.6}"
       ".scr-ov{position:fixed;inset:0;z-index:9500;background:rgba(0,0,0,.88);overflow:auto;-webkit-overflow-scrolling:touch;display:flex;align-items:flex-start;justify-content:flex-start}"
       ".scr-ov img{display:block;width:auto;max-width:none;height:auto;margin:auto;padding:56px 8px 24px;box-sizing:content-box}"
       "@media (min-width:900px){.scr-ov img{max-width:calc(100vw - 32px)}}"
       ".scr-ov .scr-x{position:fixed;top:calc(10px + env(safe-area-inset-top,0px));right:10px;width:42px;height:42px;border-radius:50%;border:0;background:rgba(255,255,255,.18);color:#fff;font-size:22px;line-height:1;cursor:pointer;z-index:2}"
       ".scr-ov .scr-cap{position:fixed;left:12px;top:calc(18px + env(safe-area-inset-top,0px));right:64px;color:#fff;font-size:13px;font-weight:700;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}")
JS = r'''(function(){if(window.__csScr)return;window.__csScr=1;
var st=document.createElement("style");st.id="cs-scr";st.textContent=__CSS__;document.head.appendChild(st);
function fix(root){try{(root||document).querySelectorAll("img[data-scr]:not([src])").forEach(function(im){var p=im.getAttribute("data-scr");im.src=window.famURL?window.famURL(p):p})}catch(e){}}
new MutationObserver(function(ms){for(var i=0;i<ms.length;i++){if(ms[i].addedNodes.length){fix(document);return}}}).observe(document.documentElement,{childList:true,subtree:true});
document.addEventListener("DOMContentLoaded",function(){fix(document)});
function close(){var o=document.getElementById("scr-ov");if(o)o.remove()}
document.addEventListener("click",function(e){var t=e.target;if(!t||!t.closest)return;
  var z=t.closest(".scr-z");if(z){e.preventDefault();e.stopPropagation();var im=z.querySelector("img");if(!im)return;close();
    var o=document.createElement("div");o.id="scr-ov";o.className="scr-ov";o.setAttribute("role","dialog");o.setAttribute("aria-label","画面の拡大");
    var cap=(z.closest("figure")&&z.closest("figure").querySelector("figcaption b"));
    o.innerHTML='<p class="scr-cap"></p><button type="button" class="scr-x" aria-label="閉じる">×</button>';o.querySelector(".scr-cap").textContent=cap?cap.textContent:"";
    var big=document.createElement("img");big.src=im.currentSrc||im.src;big.alt=im.alt;o.appendChild(big);document.body.appendChild(o);
    try{o.querySelector(".scr-x").focus({preventScroll:true})}catch(x){}return}
  if(t.closest(".scr-x")||(t.id==="scr-ov")){e.preventDefault();close()}},true);
document.addEventListener("keydown",function(e){if(e.key==="Escape")close()});
})();'''
js = "<script>" + JS.replace("__CSS__", json.dumps(css)) + "</script>"
if s.count("</head>") != 1: sys.exit("</head> が1件ではない")
s = s.replace("</head>", js + "</head>")
open(out, "w", encoding="utf-8").write(s); print("ok")
