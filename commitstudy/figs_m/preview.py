"""図の確認用。python3 preview.py <specモジュール.py> <出力フォルダ> [sec ...]
  spec を読み込み、各図を iPhone 幅(390px 画面・本文320px)と PC 幅(本文 520px)で PNG にし、警告を表示する。ライト/ダーク両方。"""
import sys, os, importlib.util, json, subprocess
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
import lib
spec, outd = sys.argv[1], sys.argv[2]; only = sys.argv[3:]
lib.FIGS.clear()
m = importlib.util.spec_from_file_location("spec", spec); mod = importlib.util.module_from_spec(m); m.loader.exec_module(mod)
os.makedirs(outd, exist_ok=True)
CSS = open(os.path.join(here, "fig.css"), encoding="utf-8").read()
items = []
for sec, fn in lib.FIGS.items():
    if only and sec not in only: continue
    h = fn(); items.append((sec, h))
warn_all = []
pages = []
for sec, h in items:
    for theme in ("light", "dark"):
        pages.append((sec, theme, f'<!doctype html><meta charset="utf-8"><style>{CSS}</style><body class="{theme}"><div class="col">{h}</div></body>'))
js = r'''
const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();const pages=JSON.parse(fs.readFileSync(process.argv[2]));
for(const [sec,theme,html,out] of pages){for(const [w,tag] of [[390,'phone'],[1100,'pc']]){const p=await b.newPage({viewport:{width:w,height:900}});await p.setContent(html);
const r=await p.evaluate(()=>{const out=[];const svg=document.querySelector('svg');const vb=svg.viewBox.baseVal;const rects=[...svg.querySelectorAll('rect')].map(r=>r.getBBox());
svg.querySelectorAll('text').forEach(t=>{const bb=t.getBBox();if(!bb.width)return;if(bb.x<vb.x-1||bb.x+bb.width>vb.x+vb.width+1||bb.y<vb.y-1||bb.y+bb.height>vb.y+vb.height+1)out.push('図の外: '+t.textContent);
const cx=bb.x+bb.width/2,cy=bb.y+bb.height/2;const c=rects.filter(r=>cx>=r.x&&cx<=r.x+r.width&&cy>=r.y&&cy<=r.y+r.height).sort((a,b)=>a.width*a.height-b.width*b.height)[0];
if(c&&(bb.x<c.x+2||bb.x+bb.width>c.x+c.width-2))out.push('箱からはみ出し: '+t.textContent+' ('+Math.round(bb.width)+' / 箱'+Math.round(c.width)+')')});
const s=svg.getBoundingClientRect();out.push('表示 '+Math.round(s.width)+'x'+Math.round(s.height)+'px');return out});
await p.screenshot({path:out+'-'+tag+'.png',fullPage:true});if(tag==='phone'&&theme==='light')console.log(sec+': '+r.join(' / '));await p.close()}}
await b.close()})();'''
jf = os.path.join(outd, "_pages.json")
json.dump([[s, t, h, os.path.join(outd, f"{s}-{t}")] for s, t, h in pages], open(jf, "w"))
open(os.path.join(outd, "_shot.js"), "w").write(js)
print("\n".join(lib.WARN) or "警告なし(文字幅の目安・箱の重なり)")
import re
subprocess.run(["node", os.path.join(outd, "_shot.js"), jf], check=True)
