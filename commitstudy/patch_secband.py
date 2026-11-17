"""テキストの上のメニューに「いまの節の表示」の細い帯を足す(別のアプリから移植)。
  - 上のメニュー(#mbar)のボタンの列のすぐ下に、高さ22pxの帯(11.5px・太さ600・薄い色・上に1pxの線)。
  - 左に「Chapter 2 取り込む > 1 データストリーム」(章・節の番号はこのアプリの見出しの書き方のまま)。1行で、はみ出す分は「…」。
    画面の幅が760px未満のときは、章は番号だけ(「Chapter 2」)にして、節の名前に場所を空ける。
  - 右に「3 / 88」(等幅の字・アクセントの色)。全体の数は、すべての節(data-sec のある項目)を数える。
    いまの番号は、読んでいる位置(メニューの下端+24px)より上に頭がある最後の節が、全体の何番目か。
    節でないところ(「このテキストの使い方」・章のまとめ・練習問題(AI先生)など)を読んでいるときは「– / 88」にし、左は章だけにする。
  - スクロール(requestAnimationFrame でまとめる)・画面の大きさの変化で計算し直し、文字が変わったときだけ書き換える。
  - 帯を押すと目次を開く(メニューの「目次」と同じ openP("toc"))。
  - テキストの画面だけに出す(問題集では出さない。ホーム・トレーニングなどの画面には上のメニューがない)。
  - 表示の設定に「いまの節の表示: 表示する/表示しない」(prefs.secb、はじめは表示する)。表示しないときは帯ごと消え、メニューは元の高さに戻る。
  メニューの高さが22px増える分は、メニューの高さ(--barh、ResizeObserver で測っている)に合わせて動かす:
  - 本文の上の余白(body の padding-top)と「節の地図」の上端は、もともと --barh を使っているのでそのまま。
  - 目次などで項目・章へ移るとき(scrollIntoView)の scroll-margin-top を 72px から「--barh + 14px」にする(帯がないときは今と同じ 72px)。
  - PC の左の目次(nav.toc、sticky)の top と高さも --barh に合わせる。
  - マーカー・メモ・論点などのPC用の吹き出しが上に逃げるときの上限(66px)を、メニューの下端+8px にする。
  - 表の見出しの追従(patch_sticky_thead.py)は、毎回 #mbar の下端を測っているので、帯の下にそのまま付く。
  公開先では body が作り直されるため、CSS はスクリプトで document.head に入れる。
使い方: python3 patch_secband.py <index.html> <出力>
"""
import sys, json
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count: sys.exit(f"置換対象が {n} 件(期待 {count} 件): {old[:90]!r}")
    s = s.replace(old, new)

CSS = r"""
#cs-secb{display:flex;align-items:center;gap:10px;height:22px;box-sizing:border-box;margin:0;padding:0 max(12px,env(safe-area-inset-right,0px)) 0 max(12px,env(safe-area-inset-left,0px));border-top:1px solid var(--line);font-family:var(--f-body);font-size:11.5px;font-weight:600;line-height:21px;color:var(--muted);cursor:pointer;-webkit-tap-highlight-color:transparent;-webkit-user-select:none;user-select:none;overflow:hidden}
@media(hover:hover) and (pointer:fine){#cs-secb:hover{background:var(--accent-soft)}}
#cs-secb:focus-visible{outline:2px solid var(--accent);outline-offset:-2px}
#cs-secb .secb-l{flex:1 1 auto;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
#cs-secb .secb-l i{font-style:normal;opacity:.7;margin:0 .35em}
#cs-secb .secb-n{flex:none;font-family:var(--f-mono);font-weight:600;color:var(--accent);white-space:nowrap;font-variant-numeric:tabular-nums}
body.view-q #cs-secb,body.secb-off #cs-secb,#cs-secb[hidden]{display:none}
#tv .chap,#tv .feat{scroll-margin-top:calc(var(--barh,58px) + 14px)}
@media(min-width:980px){#tv nav.toc{top:calc(var(--barh,58px) + 8px);max-height:calc(100vh - var(--barh,58px) - 24px)}}
"""

JS = r"""
/* ==いまの節の表示== メニューの下の細い帯に「章 > 節」と「n / 全体」を出す(押すと目次) */
function secbTop(){var b=0;try{b=bar.getBoundingClientRect().bottom}catch(e){}return Math.max(66,(b||58)+8)}
(function(){
  if(window.__secbAC){try{window.__secbAC.abort()}catch(e){}}
  var ac=window.AbortController?new AbortController():null;window.__secbAC=ac;var LO=ac?{passive:true,signal:ac.signal}:{passive:true};
  var old=byId("cs-secb");if(old)old.remove();
  var inn=bar&&bar.querySelector(".mbar-in");if(!inn)return;
  var el=document.createElement("div");el.id="cs-secb";el.setAttribute("role","button");el.tabIndex=0;
  el.innerHTML='<span class="secb-l"></span><span class="secb-n"></span>';
  inn.parentNode.insertBefore(el,inn.nextSibling);
  var L=el.firstChild,N=el.lastChild,raf=0,lastL=null,lastN=null,lastA="",list=[],secs=0,listT=0;
  var narrow=null;try{narrow=matchMedia("(max-width:759.98px)")}catch(e){}
  function txt(h){if(!h)return "";var c=h.cloneNode(true);$$(".no,.tag,.kz,button,.star",c).forEach(function(x){x.remove()});return c.textContent.replace(/\s+/g," ").trim()}
  /* 本文の章(.chap)と項目(.feat)を上から順に。節(data-sec)には全体の中の番号と見出しを付けておく */
  function build(){var es=$$("#tv .chap[id],#tv .feat[id]").filter(function(e){return !e.closest(".csloc")}),n=0;
    list=es.map(function(e){var o={e:e,c:e.classList.contains("chap")};
      if(o.c){o.t=titleOf(e);var m=/^(Chapter\s*\d+|第\s*\d+\s*章|Ch\s*\d+)/.exec(o.t);o.s=m?m[1]:o.t}
      else if(e.dataset.sec){n++;o.i=n;var h=e.querySelector(":scope>h3"),no=h&&h.querySelector(".no");o.t=((no?no.textContent.trim().replace(/^Ch\s*\d+\s*[·・.\-]\s*/,"")+" ":"")+(txt(h)||TITLES[e.dataset.sec]||"")).trim()}
      return o});
    secs=n;listT=Date.now()}
  function stale(){return !list.length||!list[0].e.isConnected||!list[list.length-1].e.isConnected||Date.now()-listT>3000}
  function upd(){raf=0;
    if(view==="quiz"||body.classList.contains("secb-off"))return;
    if(stale())build();
    if(!secs){if(!el.hidden)el.hidden=true;return}
    if(el.hidden)el.hidden=false;
    var line=0;try{line=bar.getBoundingClientRect().bottom}catch(e){}line=Math.max(0,line)+24;
    var ch=null,last=null;
    for(var i=0;i<list.length;i++){var r=list[i].e.getBoundingClientRect();if(!r.height&&!r.width)continue;if(r.top>line)break;last=list[i];if(list[i].c)ch=list[i]}
    var sm=!!(narrow&&narrow.matches),cl=ch?(sm?ch.s:ch.t):"",sec=last&&!last.c&&last.i?last:null;
    var l=sec?(cl?esc(cl)+"<i>&gt;</i>":"")+esc(sec.t):(cl?esc(cl):"目次を開く");
    var n=(sec?sec.i:"–")+" / "+secs;
    if(l!==lastL){lastL=l;L.innerHTML=l}
    if(n!==lastN){lastN=n;N.textContent=n}
    var a="いまの節: "+(sec?((ch?ch.t+" ":"")+sec.t+"("+sec.i+" / "+secs+")"):((ch?ch.t+" ":"")+"(節の外)"))+"。押すと目次を開く";
    if(a!==lastA){lastA=a;el.setAttribute("aria-label",a)}}
  function req(){if(!raf)raf=requestAnimationFrame(upd)}
  function go(e){if(e)e.preventDefault();openP(curP==="toc"?null:"toc")}
  el.addEventListener("click",go);
  el.addEventListener("keydown",function(e){if(e.key==="Enter"||e.key===" ")go(e)});
  window.addEventListener("scroll",req,LO);window.addEventListener("resize",function(){listT=0;req()},LO);
  if(narrow&&narrow.addEventListener)narrow.addEventListener("change",function(){lastL=null;req()},ac?{signal:ac.signal}:false);
  var iv=setInterval(function(){if(!el.isConnected){clearInterval(iv);return}req()},1000);
  window.__secbUpd=function(){listT=0;lastL=lastN=null;req()};
  req();
})();
"""

# 0) PC用の吹き出しが上に逃げるときの上限を、メニューの下端に合わせる(本体を入れる前に)
rep("Math.max(66,", "Math.max(secbTop(),", 5)
# 1) 本体(節の地図と同じ場所に)
rep("function qxBlock(r){", JS.strip() + "\nfunction qxBlock(r){")
# 2) 表示の設定「いまの節の表示」
rep('csmap:"on",pv:2', 'csmap:"on",secb:"on",pv:2')
rep('body.classList.toggle("csmap-off",prefs.csmap==="off");',
    'body.classList.toggle("csmap-off",prefs.csmap==="off");body.classList.toggle("secb-off",prefs.secb==="off");if(window.__secbUpd)window.__secbUpd();')
CSMAP = 'data-k=\\"csmap\\"><button type=\\"button\\" data-v=\\"on\\">表示する<\\/button><button type=\\"button\\" data-v=\\"off\\">表示しない<\\/button><\\/div>'
rep(CSMAP, CSMAP + '\\n  <div class=\\"mp-h t-only\\">いまの節の表示(メニューの下)<\\/div><div class=\\"seg t-only\\" data-k=\\"secb\\"><button type=\\"button\\" data-v=\\"on\\">表示する<\\/button><button type=\\"button\\" data-v=\\"off\\">表示しない<\\/button><\\/div>')

js = "<script>(function(){if(document.getElementById('cs-secb-css'))return;var st=document.createElement('style');st.id='cs-secb-css';st.textContent=" + json.dumps(CSS.strip()) + ";document.head.appendChild(st)})();</script>"
if s.count("</head>") != 1: sys.exit("</head> が1件ではない")
s = s.replace("</head>", js + "</head>")
open(out, "w", encoding="utf-8").write(s); print("ok")
