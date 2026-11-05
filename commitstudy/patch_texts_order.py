"""テキスト一覧の科目の並びを、ユーザーごとに好きに変えられるようにする。合格した科目に印も付けられる。
  - 一覧の上の「並べ替え・合格の印」を押すと編集モード。各科目に ↑ ↓ と「合格」のボタンが出る。終えるときは画面下の中央に追従する「完了」
  - ↑↓で動かすと、入れ替わったカードがすべるように動き、動かしたカードが光る
  - 並び(cs-subj-order)と合格(cs-subj-passed)はアカウントに同期(fam-ls)
  - 合格した科目は、カードに「合格」の印が付く
使い方: python3 patch_texts_order.py <index.html> <出力>
"""
import json, sys
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count: sys.exit(f"置換対象が {n} 件(期待 {count} 件): {old[:90]!r}")
    s = s.replace(old, new)
def jesc(t): return json.dumps(t, ensure_ascii=False)[1:-1].replace("</", "<\\/")
JS = r'''
/* ==テキスト一覧: 科目の並べ替えと合格の印(ユーザーごと)== */
function csTextsExtra(){var n=0;(function wait(){var list=document.querySelector("#groups .grp .list");
  if(!list||!list.querySelector(".tx[data-id]")||(!window.__famLsReady&&n<40)){if(n++<60)setTimeout(wait,200);return}
  var LSg=function(k,d){try{var v=JSON.parse(localStorage.getItem(k));return v==null?d:v}catch(e){return d}},LSs=function(k,v){try{localStorage.setItem(k,JSON.stringify(v))}catch(e){}};
  var cards=function(){return [].slice.call(list.querySelectorAll(".tx[data-id]"))};
  function applyOrder(){var ord=LSg("cs-subj-order",[]);if(!ord.length)return;var cs=cards(),pos={};ord.forEach(function(id,i){pos[id]=i});
    cs.sort(function(a,b){var x=pos[a.dataset.id],y=pos[b.dataset.id];return (x==null?999:x)-(y==null?999:y)}).forEach(function(c){list.appendChild(c)})}
  function paint(){var P=LSg("cs-subj-passed",{}),ed=list.classList.contains("ed");
    cards().forEach(function(c,i,all){var id=c.dataset.id,box=c.querySelector(".tx-ed");
      if(!box){box=document.createElement("div");box.className="tx-ed";c.appendChild(box)}
      c.classList.toggle("passed",!!P[id]);
      var b=c.querySelector(".pass-b");if(P[id]&&!b){b=document.createElement("span");b.className="pass-b";b.textContent="合格";var tt=c.querySelector(".tt");(tt||c).appendChild(b)}else if(!P[id]&&b)b.remove();
      box.innerHTML=ed?'<button type="button" data-mv="-1"'+(i===0?" disabled":"")+' aria-label="上へ">↑</button><button type="button" data-mv="1"'+(i===all.length-1?" disabled":"")+' aria-label="下へ">↓</button><button type="button" class="pz" data-pass aria-pressed="'+(!!P[id])+'">'+(P[id]?"合格済み":"合格した")+'</button>':""})}
  if(!document.getElementById("tx-edbtn")){var bar=document.createElement("div");bar.className="tx-edbar";
    bar.innerHTML='<button type="button" id="tx-edbtn" aria-pressed="false">並べ替え・合格の印</button>';list.parentElement.insertBefore(bar,list);
    var top=bar.querySelector("button"),done=document.createElement("button");done.type="button";done.id="tx-done";done.className="tx-done";done.textContent="完了";done.hidden=true;document.body.appendChild(done);
    var setEd=function(on){list.classList.toggle("ed",on);top.setAttribute("aria-pressed",String(on));top.hidden=on;done.hidden=!on;paint()};
    top.onclick=function(){setEd(true)};done.onclick=function(){setEd(false)};
    /* 別の画面へ移ったら、下の完了ボタンを片付ける */
    var mo=setInterval(function(){if(!document.body.contains(list)){done.remove();clearInterval(mo)}},500)}
  list.addEventListener("click",function(e){var b=e.target.closest(".tx-ed button");if(!b)return;e.preventDefault();e.stopPropagation();var c=b.closest(".tx"),id=c.dataset.id;
    if(b.dataset.mv){var cs=cards(),i=cs.indexOf(c),j=i+(+b.dataset.mv);if(j<0||j>=cs.length)return;var ids=cs.map(function(x){return x.dataset.id});var t=ids[i];ids[i]=ids[j];ids[j]=t;LSs("cs-subj-order",ids);
      /* 動いたことがわかるように: 入れ替わった2枚を元の位置からすべらせ、動かしたカードを光らせる */
      var y0=new Map(cs.map(function(x){return [x,x.getBoundingClientRect().top]}));applyOrder();
      cards().forEach(function(x){var dy=y0.get(x)-x.getBoundingClientRect().top;if(!dy)return;x.style.transition="none";x.style.transform="translateY("+dy+"px)";x.style.zIndex=x===c?"2":"1";void x.offsetWidth;
        x.style.transition="transform .42s cubic-bezier(.2,.75,.2,1)";x.style.transform="";setTimeout(function(){x.style.transition="";x.style.zIndex=""},450)});
      c.classList.remove("tx-moved");void c.offsetWidth;c.classList.add("tx-moved");setTimeout(function(){c.classList.remove("tx-moved")},1100);
      setTimeout(function(){var r=c.getBoundingClientRect(),bot=window.innerHeight-130;if(r.top<80||r.bottom>bot)c.scrollIntoView({block:"center",behavior:"smooth"})},430)}
    else if(b.hasAttribute("data-pass")){var P=LSg("cs-subj-passed",{});if(P[id])delete P[id];else P[id]=Date.now();LSs("cs-subj-passed",P)}
    paint()});
  applyOrder();paint()})()}
(function(){var o=FAMP.texts;FAMP.texts=function(){o();if(document.body.dataset.page==="text")csTextsExtra()}})();
'''
rep("FAMP.record=function(){", JS + "\nFAMP.record=function(){")
CSS = """
/* 科目の並べ替え・合格の印 */
.tx-edbar{display:flex;justify-content:flex-end;margin:0 0 8px}
.tx-edbar button{font:inherit;font-size:13px;font-weight:700;color:var(--sub);background:var(--paper);border:1px solid var(--line);border-radius:999px;padding:5px 14px;cursor:pointer}
.tx-edbar button[aria-pressed=true]{background:var(--brand);border-color:var(--brand);color:var(--brand-ink)}
.tx-done{position:fixed;left:50%;transform:translateX(-50%);bottom:calc(96px + env(safe-area-inset-bottom,0px));z-index:70;font:inherit;font-size:15px;font-weight:800;color:var(--brand-ink);background:var(--brand);border:0;border-radius:999px;padding:12px 40px;box-shadow:0 10px 28px -10px rgba(0,0,0,.45);cursor:pointer}
.tx-done[hidden]{display:none}
@media (min-width:900px){.tx-done{bottom:28px}}
.list.ed{padding-bottom:70px}
.tx.tx-moved{animation:txMoved 1.1s ease-out}
@keyframes txMoved{0%{box-shadow:0 0 0 3px var(--brand),0 12px 30px -12px rgba(0,0,0,.35)}100%{box-shadow:0 0 0 0 transparent}}
.tx{position:relative}
.tx-ed{grid-column:1/-1;display:flex;gap:8px;justify-content:flex-end}
.tx-ed:empty{display:none}
.tx-ed button{font:inherit;font-size:14px;font-weight:700;min-width:44px;height:38px;border-radius:10px;border:1px solid var(--line);background:var(--paper);color:var(--ink);cursor:pointer}
.tx-ed button:disabled{opacity:.35;cursor:default}
.tx-ed .pz{padding:0 14px}
.tx-ed .pz[aria-pressed=true]{background:var(--sun);border-color:var(--sun);color:#2b1900}
.tx.passed{border-color:var(--sun)!important;box-shadow:0 0 0 2px color-mix(in srgb,var(--sun) 55%,transparent)}
.pass-b{display:inline-block;vertical-align:2px;margin-left:8px;font-size:11.5px;font-weight:800;line-height:1.6;color:#2b1900;background:var(--sun);border-radius:999px;padding:0 9px;letter-spacing:.06em;white-space:nowrap}
"""
lines = s.split("\n"); l = lines[4]
j = l.index("window.FAMD=") + len("window.FAMD="); F, end = json.JSONDecoder().raw_decode(l[j:])
F["pages"]["texts"]["css"] += CSS
lines[4] = l[:j] + json.dumps(F, ensure_ascii=False).replace("</", "<\\/") + l[j+end:]
s = "\n".join(lines)
rep("`cs-guide-seen`]", "`cs-guide-seen`,`cs-subj-order`,`cs-subj-passed`]")
open(out, "w", encoding="utf-8").write(s); print("ok")
