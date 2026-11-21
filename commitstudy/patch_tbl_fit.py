"""テキスト・問題の表を読みやすくする(社労士版 2026-11-14・11-18 の直しに合わせたもの)。
  1. 表の見出しが少し遅れて付いてくるのを直す(patch_sticky_thead.py の作り直し)。
     これまでは、スクロールのたびに JS で見出しの写しを動かしていたので、画面が先に動いて見出しが1コマ遅れた。
     いまはブラウザの sticky(スクロールと同じコマで動く)で付ける。表は横にスクロールする囲み(.tw / .qb-tw)の中にあり、
     その中では sticky が上に付かないので、囲みと表をまとめた .tf-wrap の先頭に見出しの写し(.tf-sh)を置く。
     写しは高さを打ち消して元の見出しにぴったり重なり、表が上へ流れると上のメニュー(.mbar)の下で止まり、表の下端で一緒に上へ抜ける。
     写しを見せるのは元の見出しがメニューの下に隠れたときだけ。列の幅・色は元の表から測って合わせ(表の大きさが変わるたびに測り直す)、
     横のスクロールは囲みに合わせる。
     写しのマスには文字を入れず、CSS(::before の content)で元の見出しの文字を出す。マーカー・検索・用語のリンク・選んだ文字の数え方など、
     本文の文字をたどる処理に写しが入らないようにするため。
  2. スマホで表の中の文字が1〜2文字ずつ改行されて読みにくいのを直す(テキストの表)。
     - 短いマス(空白を除いて10文字まで)は折り返さない(.tf-nw)
     - 長いマスは、左右の余白を含めて 8〜9 文字分の最低の幅(21文字以上は9文字分)。行の見出し(tbody th)でも折り返す(.tf-wr)
     入りきらない分は、表の囲み(.tw)の中で横にスクロールする。文字は変えない。
  「テキストのこの場所」の写し(data-csclone)の中では、見出しの写しは出さない。節の地図・場所のひとことでは .tf-wrap も「表」として扱う。
  公開先では body が作り直されるため、CSS はスクリプトで document.head に入れ、表が増えたら(MutationObserver)そのつど整える。
使い方: python3 patch_tbl_fit.py <index.html> <出力>
"""
import sys, json
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count: sys.exit(f"置換対象が {n} 件(期待 {count} 件): {old[:90]!r}")
    s = s.replace(old, new)

# これまでの見出しの追従(patch_sticky_thead.py の <script>)を外す
i = s.find("<script>(function(){if(window.__csSth)return;")
j = s.find("</script>", i)
if i < 0 or j < 0 or s.count("window.__csSth") != 2: sys.exit("patch_sticky_thead の script が見つかりません")
s = s[:i] + s[j + len("</script>"):]
# 節の地図・場所のひとこと: 囲み(.tf-wrap)も「表」
rep('if(c.contains("tw")||t==="TABLE")', 'if(c.contains("tw")||c.contains("tf-wrap")||t==="TABLE")', 2)

css = (".tf-nw{white-space:nowrap!important}.tf-wr{white-space:normal!important}"
       ".tf-wrap{position:relative;display:flow-root;padding-top:1px}"
       ".tf-wrap>.tf-sh{position:sticky;top:var(--tf-top,0px);z-index:5;overflow:hidden!important;margin:0 1px!important;padding:0!important;border:0!important;border-radius:0!important;"
       "background:none!important;visibility:hidden;pointer-events:none;box-shadow:0 1px 0 var(--line),0 6px 10px -8px rgba(0,0,0,.35)}"
       ".tf-wrap.tf-on>.tf-sh{visibility:visible}"
       "[data-csclone] .tf-wrap>.tf-sh{visibility:hidden!important}"
       ".tf-sh table{table-layout:fixed;margin:0!important;border-collapse:collapse}"
       ".tf-sh th,.tf-sh td{box-sizing:border-box}"
       ".tf-sh [data-tft]::before{content:attr(data-tft);white-space:pre-line}")
JS = r"""(function(){if(window.__csTblFit)return;window.__csTblFit=1;
var st=document.createElement('style');st.id='cs-tbl-fit';st.textContent=__CSS__;document.head.appendChild(st);
var de=document.documentElement,S={top:-1,list:[],vis:[]},io=null,ro=null,mbRO=null,mb0=null,raf=0;
function len(t){return String(t||'').replace(/\s+/g,'').length}
/* 2. テキストの表のマスの折り返し */
function fit(tb){if(tb.dataset.tf)return;tb.dataset.tf='1';
  Array.prototype.forEach.call(tb.querySelectorAll('th,td'),function(c){var n=len(c.textContent);if(!n)return;
    if(n<=10)c.classList.add('tf-nw');else{c.classList.add('tf-wr');c.style.minWidth=(n<=20?8:9)+'em'}})}
/* 1. 見出しの追従 */
function measure(){var b=document.getElementById('mbar')||document.querySelector('.mbar'),r=b?b.getBoundingClientRect():null;
  var t=r&&r.height&&r.bottom>0?Math.max(0,Math.round(r.bottom)):0;if(t!==S.top){S.top=t;de.style.setProperty('--tf-top',t+'px')}
  if(b!==mb0&&window.ResizeObserver){if(mbRO)mbRO.disconnect();mb0=b;if(b){mbRO=new ResizeObserver(function(){measure();check()});mbRO.observe(b)}}}
function check(){for(var i=0;i<S.vis.length;i++)S.vis[i].on()}
function bgOf(el){var bg=getComputedStyle(el).backgroundColor;
  while((!bg||bg==='transparent'||/rgba\([^)]*,\s*0\)$/.test(bg))&&el.parentElement){el=el.parentElement;bg=getComputedStyle(el).backgroundColor}return bg}
function txt(c){var t=c.innerText;if(t==null||t==='')t=c.textContent;return String(t||'').replace(/\n{2,}/g,'\n').trim()}
function stick(tb){if(tb.dataset.th||!tb.tHead||!tb.tHead.rows.length)return;
  var tw=tb.parentElement;if(!tw||tw.children.length!==1||!(tw.classList.contains('tw')||tw.classList.contains('qb-tw')))return;
  tb.dataset.th='1';
  var wrap=document.createElement('div');wrap.className='tf-wrap';tw.parentNode.insertBefore(wrap,tw);
  var sh=document.createElement('div');sh.className=tw.className+' tf-sh';sh.setAttribute('aria-hidden','true');
  var ct=document.createElement('table');ct.className=tb.className;var th=document.createElement('thead');ct.appendChild(th);sh.appendChild(ct);
  var oc=[],cc=[];Array.prototype.forEach.call(tb.tHead.rows,function(r){var nr=document.createElement('tr');th.appendChild(nr);
    Array.prototype.forEach.call(r.cells,function(c){var d=document.createElement(c.tagName.toLowerCase());d.className=c.className;
      if(c.colSpan>1)d.colSpan=c.colSpan;if(c.rowSpan>1)d.rowSpan=c.rowSpan;nr.appendChild(d);oc.push(c);cc.push(d)})});
  wrap.appendChild(sh);wrap.appendChild(tw);
  var mb=parseFloat(getComputedStyle(tw).marginBottom)||0;
  var x={wrap:wrap,tb:tb,size:function(){var hr=tb.tHead.getBoundingClientRect();if(!hr.width)return;
      ct.style.width=tb.getBoundingClientRect().width.toFixed(2)+'px';
      for(var i=0;i<oc.length;i++){var w=oc[i].getBoundingClientRect().width.toFixed(2)+'px',cs=getComputedStyle(oc[i]);cc[i].style.width=cc[i].style.minWidth=cc[i].style.maxWidth=w;
        cc[i].setAttribute('data-tft',txt(oc[i]));cc[i].style.backgroundColor=bgOf(oc[i]);cc[i].style.color=cs.color;cc[i].style.borderBottom=cs.borderBottom;
        cc[i].style.textAlign=cs.textAlign;cc[i].style.verticalAlign=cs.verticalAlign;cc[i].style.padding=cs.padding;cc[i].style.fontSize=cs.fontSize;cc[i].style.fontWeight=cs.fontWeight;cc[i].style.lineHeight=cs.lineHeight;cc[i].style.height=oc[i].getBoundingClientRect().height.toFixed(2)+'px'}
      var h=hr.height;sh.style.height=h.toFixed(2)+'px';sh.style.marginBottom=(-h-1).toFixed(2)+'px';
      /* 写しが表の下端より下へはみ出さないよう、囲みの下端を見出しの高さぶん上げ、その分をまとめの囲みの外の余白で戻す(並びは変わらない) */
      tw.style.marginBottom=(-h).toFixed(2)+'px';wrap.style.marginBottom=(mb+h).toFixed(2)+'px';sh.scrollLeft=tw.scrollLeft},
    on:function(){wrap.classList.toggle('tf-on',tb.tHead.getBoundingClientRect().top<S.top-0.5)}};
  tw.addEventListener('scroll',function(){sh.scrollLeft=tw.scrollLeft},{passive:true});
  S.list.push(x);wrap.__tf=x;if(ro)ro.observe(tb);x.size();if(io)io.observe(wrap)}
function prune(){S.list=S.list.filter(function(x){if(x.wrap.isConnected)return true;if(io)io.unobserve(x.wrap);if(ro)ro.unobserve(x.tb);return false});
  S.vis=S.vis.filter(function(x){return x.wrap.isConnected})}
function scan(){raf=0;try{prune();measure();
  Array.prototype.forEach.call(document.querySelectorAll('#chapters .tw > table'),function(tb){if(!tb.closest('[data-csclone]'))fit(tb)});
  Array.prototype.forEach.call(document.querySelectorAll('#chapters .tw > table, .qb-tw > table'),function(tb){if(!tb.closest('[data-csclone]'))stick(tb)});
  check()}catch(e){}}
function req(){if(!raf)raf=requestAnimationFrame(scan)}
if(window.IntersectionObserver)io=new IntersectionObserver(function(es){es.forEach(function(e){var x=e.target.__tf;if(!x)return;var k=S.vis.indexOf(x);
  if(e.isIntersecting){if(k<0)S.vis.push(x)}else{if(k>=0)S.vis.splice(k,1);e.target.classList.remove('tf-on')}});check()});
if(window.ResizeObserver)ro=new ResizeObserver(function(es){es.forEach(function(e){var w=e.target.closest&&e.target.closest('.tf-wrap');if(w&&w.__tf)w.__tf.size()})});
window.addEventListener('scroll',check,{passive:true});
window.addEventListener('resize',function(){measure();S.list.forEach(function(x){x.size()});check()});
new MutationObserver(function(ms){for(var i=0;i<ms.length;i++){var a=ms[i].addedNodes;for(var j=0;j<a.length;j++){var n=a[j];if(n.nodeType===1&&(n.tagName==='TABLE'||n.querySelector&&n.querySelector('table'))){req();return}}}}).observe(de,{childList:true,subtree:true});
req();setInterval(req,3000);
})();"""
js = "<script>" + JS.replace("__CSS__", json.dumps(css)) + "</script>"
if s.count("</head>") != 1: sys.exit("</head> が1件ではない")
s = s.replace("</head>", js + "</head>")
open(out, "w", encoding="utf-8").write(s); print("ok")
