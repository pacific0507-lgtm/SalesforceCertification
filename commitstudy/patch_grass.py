"""学習の記録のカレンダーとホームの週のスタンプを、いろいろな種類の「草」のイラストにする。
  日付ごとに8種類から決まる(同じ日はいつも同じ草)。まれに四つ葉のクローバー。
使い方: python3 patch_grass.py <index.html> <出力>
"""
import json, sys
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count: sys.exit(f"置換対象が {n} 件(期待 {count} 件): {old[:90]!r}")
    s = s.replace(old, new)
JS = r'''
/* ==草のスタンプ(日付ごとに種類が決まる)== */
var CS_GRASS=(function(){
  var G="#3f9d4a",L="#78c257",D="#2e7d3a";
  var bl=function(d,c){return '<path d="'+d+'" fill="'+(c||G)+'"/>'};
  return [
   /* 芝 */ bl("M12 31c1-7 0-12-2-16 4 3 6 9 5 16z")+bl("M18 31c0-9 1-15 3-20 1 6 1 13-0 20z",L)+bl("M24 31c1-6 3-11 7-14-2 5-3 9-3 14z"),
   /* 双葉 */ bl("M19.5 31V19h1v12z",D)+bl("M20 20c-1-5-6-7-10-6 1 4 5 7 10 6z",L)+bl("M20 19c1-5 6-7 10-6-1 4-5 7-10 6z"),
   /* 花つき */ bl("M19.5 31V17h1v14z",D)+bl("M20 25c-2-4-6-5-9-4 2 3 5 5 9 4z",L)+'<circle cx="20" cy="14" r="3" fill="#f4c430"/>'+'<g fill="#fff" stroke="#f4c430" stroke-width=".6"><circle cx="20" cy="9.5" r="2.4"/><circle cx="24.5" cy="14" r="2.4"/><circle cx="20" cy="18.5" r="2.4"/><circle cx="15.5" cy="14" r="2.4"/></g><circle cx="20" cy="14" r="2.2" fill="#f4c430"/>',
   /* 草むら */ bl("M9 31c1-5 1-9-1-12 3 2 5 6 4 12z",L)+bl("M14 31c0-7 1-12 3-16 0 5 0 11-1 16z")+bl("M20 31c-1-8 0-14 2-19 1 6 1 13 0 19z",D)+bl("M25 31c0-6 2-10 5-13-1 4-2 8-2 13z",L)+bl("M29 31c1-4 3-7 5-8-1 3-2 5-2 8z"),
   /* 若葉 */ bl("M19.5 31V21h1v10z",D)+bl("M20 22c-6-1-9-7-8-12 6 1 9 6 8 12z",L)+'<path d="M20 22c-2-3-4-6-6-10" stroke="#fff" stroke-width=".8" fill="none" opacity=".7"/>',
   /* つくし */ bl("M18.5 31V14h3v17z","#c9a36b")+'<ellipse cx="20" cy="12" rx="3.2" ry="5" fill="#a9824e"/>'+'<path d="M17 21h6M17 26h6" stroke="#7a5a33" stroke-width="1.2"/>'+bl("M12 31c1-5 0-8-2-11 3 2 5 6 4 11z",L),
   /* たんぽぽ */ bl("M19.5 31V18h1v13z",D)+bl("M20 28c-3-1-7-1-9-4 3 0 6 1 9 4z",G)+bl("M20 27c3-1 7-2 9-5-3 0-6 2-9 5z",L)+'<g fill="#f6c21c">'+[0,30,60,90,120,150,180,210,240,270,300,330].map(function(a){return '<ellipse cx="20" cy="9.5" rx="1.3" ry="4" transform="rotate('+a+' 20 14)"/>'}).join("")+'</g><circle cx="20" cy="14" r="2.4" fill="#e8a40c"/>',
   /* ススキ */ bl("M16 31c0-8 1-15 4-21 0 7-1 14-2 21z",L)+bl("M22 31c0-7 2-13 6-18-1 6-3 12-4 18z")+'<path d="M20 10c2 0 4 1 5 3M27 13c1 1 2 3 2 5" stroke="#d6b77a" stroke-width="2.4" stroke-linecap="round" fill="none"/>'
  ].concat([/* 四つ葉(まれ) */ bl("M19.5 31V21h1v10z",D)+'<g fill="#3f9d4a"><circle cx="16.5" cy="13.5" r="4"/><circle cx="23.5" cy="13.5" r="4"/><circle cx="16.5" cy="20.5" r="4"/><circle cx="23.5" cy="20.5" r="4"/></g><g fill="#78c257"><circle cx="16.5" cy="13.5" r="2"/><circle cx="23.5" cy="13.5" r="2"/><circle cx="16.5" cy="20.5" r="2"/><circle cx="23.5" cy="20.5" r="2"/></g>'])})();
function csGrass(day){var h=0,t=String(day||"");for(var i=0;i<t.length;i++)h=(h*31+t.charCodeAt(i))>>>0;h=(h^(h>>>7))>>>0;
  var k=h%23===0?8:h%8;return '<svg class="grass" viewBox="0 0 40 40" aria-hidden="true"><circle cx="20" cy="20" r="19" class="gs-bg"/><path d="M6 31h28" stroke="#8fbf6a" stroke-width="1.4" stroke-linecap="round"/>'+CS_GRASS[k]+'</svg>'}
'''
rep("FAMP.home=function(){", JS + "\nFAMP.home=function(){")
STAMP = '<span>`+(o?`<img src="brand/raf-face.webp" alt="" width="40" height="40">`:``)+`</span>'
n = s.count(STAMP)
if n < 1: sys.exit("週のスタンプが見つからない")
s = s.replace(STAMP, '<span>`+(o?csGrass(s):``)+`</span>')
rep('日の記録を見る"><img src="brand/raf-face.webp" alt="" width="40" height="40"><em>`+e+`</em>', '日の記録を見る">`+csGrass(o)+`<em>`+e+`</em>')
CSS = """
/* 草のスタンプ */
.grass{display:block}
.grass .gs-bg{fill:color-mix(in srgb,var(--ok,#2a9765) 14%,var(--paper,#fff))}
.stamps .grass{width:100%;height:100%}
.cal .d.on .grass{position:absolute;inset:6%;width:88%;height:88%;animation:pon .6s var(--spring) both;animation-delay:calc(var(--i) * 18ms)}
"""
lines = s.split("\n"); l = lines[4]
j = l.index("window.FAMD=") + len("window.FAMD="); F, end = json.JSONDecoder().raw_decode(l[j:])
for k in ("home", "record"): F["pages"][k]["css"] += CSS
lines[4] = l[:j] + json.dumps(F, ensure_ascii=False).replace("</", "<\\/") + l[j+end:]
s = "\n".join(lines)
open(out, "w", encoding="utf-8").write(s); print("ok", n)
