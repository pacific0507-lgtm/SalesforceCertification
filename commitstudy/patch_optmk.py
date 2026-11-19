"""選択肢に「○ △ ×」の自分用の印を付けられるようにする(社労士版の択一と同じ)。
  - 問題集(4択・5択・2つ選択・組合せ)とトレーニングの選択肢の右下に、○(正しいと思う)・△(迷っている)・×(誤りだと思う)の小さなボタン。
    もう一度押すと消える。×を付けた選択肢は文字に取り消し線(消去法)。
  - 選択肢のボタンの中には入れず(ボタンの入れ子にしない)、選択肢を包む div の右下に重ねる。印を押しても選択肢は選ばれない。
    選択肢の文の終わりに印の幅の空き(span.omk-sp)を入れるので、短い文は同じ行に、長い文は次の行の右端に印が来る。
  - 印は答える前だけ。答え合わせ(模擬試験は採点)をすると隠れ、その問題の印は消える(「もう一度解く」で、まっさらな印から解き直す)。
  - 保存は cs-optmk-v1 {"<科目>:<問題番号>": {"<選択肢の番号>": "o"|"t"|"x"}}。アカウントに同期(fam-ls)。問題集とトレーニングで共通。
  - 選択肢の下に「選択肢の ○ △ × は自分用の印です(消去法に使えます)」を、初めて印を使うまで出す(cs-optmk-hint、端末だけ)。
  公開先では body が作り直されるため、CSS と共通の処理はスクリプトで document.head / window に入れる。
使い方: python3 patch_optmk.py <index.html> <出力>
"""
import sys, json
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count: sys.exit(f"置換対象が {n} 件(期待 {count} 件): {old[:90]!r}")
    s = s.replace(old, new)

css = (
 ".omr{position:relative;min-width:0}"
 ".omr>.tq-b{width:100%;box-sizing:border-box}"
 # 選択肢の文の終わりに印の幅の空き(omk-sp)を入れ、印をそこへ重ねる。短い文は同じ行に、長い文は次の行の右に入る
 ".omk-sp{display:inline-block;width:114px;height:30px;margin-left:8px;vertical-align:bottom}"
 ".omk{position:absolute;right:15px;bottom:12px;display:flex;gap:6px}"
 ".omr>.tq-b~.omk{right:15px;bottom:11px}"
 ".omk button{width:34px;height:30px;padding:0;border-radius:8px;border:1px solid var(--line);"
 "background:var(--surface,var(--paper,#fff));color:var(--muted,var(--sub,#666));font:inherit;font-size:13px;font-weight:700;line-height:1;cursor:pointer;"
 "-webkit-tap-highlight-color:transparent;touch-action:manipulation}"
 ".omk button:hover{border-color:var(--accent,var(--brand,#333))}"
 ".omk button[aria-pressed=\"true\"]{background:var(--accent,var(--brand,#333));border-color:var(--accent,var(--brand,#333));color:var(--accent-ink,var(--paper,#fff))}"
 ".omk button:focus-visible{outline:2px solid var(--accent,var(--brand,#333));outline-offset:2px}"
 ".omr.x-out>button>span{text-decoration:line-through;text-decoration-thickness:1px;color:var(--muted,var(--sub,#666));opacity:.75}"
 ".omk-hint{margin:8px 2px 0;font-size:12.5px;line-height:1.6;color:var(--muted,var(--sub,#666))}"
)

js = r"""(function(){
if(window.csOmk)return;
var K="cs-optmk-v1",HK="cs-optmk-hint",LB={o:"正しいと思う",t:"迷っている",x:"誤りだと思う"},CH={o:"○",t:"△",x:"×"};
function all(){try{var v=JSON.parse(localStorage.getItem(K)||"{}");return v&&typeof v==="object"?v:{}}catch(e){return {}}}
function put(v){try{localStorage.setItem(K,JSON.stringify(v))}catch(e){}}
function key(sj,n){return String(sj)+":"+String(n)}
function used(){try{return !!localStorage.getItem(HK)}catch(e){return true}}
window.csOmk={
  get:function(sj,n){var m=all()[key(sj,n)];return m&&typeof m==="object"?m:{}},
  clear:function(sj,n){var v=all(),k=key(sj,n);if(v[k]){delete v[k];put(v)}},
  grp:function(sj,n,i,lab){var m=this.get(sj,n)[i]||"",h='<span class="omk" role="group" aria-label="'+lab+'に印を付ける">';
    ["o","t","x"].forEach(function(k){h+='<button type="button" data-omk="'+k+'" data-s="'+sj+'" data-n="'+n+'" data-i="'+i+'" aria-pressed="'+(m===k)+'" aria-label="'+LB[k]+'" title="'+LB[k]+'">'+CH[k]+"</button>"});
    return h+"</span>"},
  hint:function(){return used()?"":'<p class="omk-hint">選択肢の ○ △ × は自分用の印です(消去法に使えます)</p>'}
};
/* 印のボタン: 選択肢の選択やほかのクリック処理に渡さない(window の捕捉段階で止める) */
window.addEventListener("click",function(e){var b=e.target&&e.target.closest&&e.target.closest(".omk button[data-omk]");if(!b)return;
  e.stopPropagation();e.preventDefault();
  var sj=b.dataset.s,n=b.dataset.n,i=b.dataset.i,k=b.dataset.omk,v=all(),q=key(sj,n),m=v[q]&&typeof v[q]==="object"?v[q]:{};
  if(m[i]===k)delete m[i];else m[i]=k;
  if(Object.keys(m).length)v[q]=m;else delete v[q];put(v);
  var g=b.parentNode;Array.prototype.forEach.call(g.querySelectorAll("button[data-omk]"),function(x){x.setAttribute("aria-pressed",String(m[i]===x.dataset.omk))});
  var r=g.closest(".omr");if(r)r.classList.toggle("x-out",m[i]==="x");
  try{localStorage.setItem(HK,"1")}catch(x){}
  Array.prototype.forEach.call(document.querySelectorAll(".omk-hint"),function(x){x.parentNode.removeChild(x)});
},true);
/* 印にフォーカスがあるときの Enter・スペースは、答え合わせ・次へに使わない(ボタンを押す動作だけにする) */
window.addEventListener("keydown",function(e){if((e.key==="Enter"||e.key===" ")&&e.target&&e.target.closest&&e.target.closest(".omk"))e.stopPropagation()},true);
var st=document.createElement("style");st.id="cs-optmk";st.textContent=__CSS__;document.head.appendChild(st);
})();""".replace("__CSS__", json.dumps(css, ensure_ascii=False))
if s.count("</head>") != 1: sys.exit("</head> が1件ではない")
s = s.replace("</head>", "<script>" + js + "</script></head>")

# ---- 問題集(mcAns) ----
rep('var od=orderOf(q),sel=Array.isArray(a.sel)?a.sel:[],dis=revealed||(S.mode==="exam"&&S.examDone),h="";',
    'var od=orderOf(q),sel=Array.isArray(a.sel)?a.sel:[],dis=revealed||(S.mode==="exam"&&S.examDone),h="",SJ=(window.FAMV&&FAMV.id)||"d360",MK=dis?null:csOmk.get(SJ,q.n);if(dis)csOmk.clear(SJ,q.n);')
old_b = ("""    h+='<button type="button" class="'+c+'" data-act="mopt" data-i="'+i+'"'+(dis?" disabled":"")+' aria-pressed="'+on+'"><b>'+LETM.charAt(pos)+'</b><span>'+esc(q.o[i])+(S.en&&q.oe&&q.oe[i]?'<em>'+esc(q.oe[i])+"</em>":"")+"</span>"+(revealed&&ok?'<i class="mk">正解</i>':"")+"</button>";\n"""
         "  });\n  return h+\"</div>\";\n}")
new_b = ("""    h+='<div class="omr'+(MK?" has-mk":"")+(MK&&MK[i]==="x"?" x-out":"")+'"><button type="button" class="'+c+'" data-act="mopt" data-i="'+i+'"'+(dis?" disabled":"")+' aria-pressed="'+on+'"><b>'+LETM.charAt(pos)+'</b><span>'+esc(q.o[i])+(S.en&&q.oe&&q.oe[i]?'<em>'+esc(q.oe[i])+"</em>":"")+(MK?'<i class="omk-sp" aria-hidden="true"></i>':"")+"</span>"+(revealed&&ok?'<i class="mk">正解</i>':"")+"</button>"+(MK?csOmk.grp(SJ,q.n,i,LETM.charAt(pos)):"")+"</div>";\n"""
         "  });\n  return h+\"</div>\"+(MK?csOmk.hint():\"\");\n}")
rep(old_b, new_b)

# ---- トレーニング(renderQ) ----
rep("""  h+='<div class="tq-o" role="group" aria-label="選択肢">'+q.o.map(function(o,i){""",
    """  var MK=DONE?null:csOmk.get(q.subj,q.n);if(DONE)csOmk.clear(q.subj,q.n);\n  h+='<div class="tq-o" role="group" aria-label="選択肢">'+q.o.map(function(o,i){""")
rep("""    return '<button type="button" class="'+c+'" data-i="'+i+'"'+(DONE?" disabled":"")+'><b>'+"ABCDEFGHIJ".charAt(i)+'</b><span>'+esc(o)+'</span></button>'}).join("")+'</div>';""",
    """    return '<div class="omr'+(MK?" has-mk":"")+(MK&&MK[i]==="x"?" x-out":"")+'"><button type="button" class="'+c+'" data-i="'+i+'"'+(DONE?" disabled":"")+'><b>'+"ABCDEFGHIJ".charAt(i)+'</b><span>'+esc(o)+(MK?'<i class="omk-sp" aria-hidden="true"></i>':"")+'</span></button>'+(MK?csOmk.grp(q.subj,q.n,i,"ABCDEFGHIJ".charAt(i)):"")+'</div>'}).join("")+'</div>'+(MK?csOmk.hint():"");""")

# ---- アカウントに同期 ----
rep("`cs-home-layout`,`cs-plan-v1`]", "`cs-home-layout`,`cs-plan-v1`,`cs-optmk-v1`]")
open(out, "w", encoding="utf-8").write(s); print("ok")
