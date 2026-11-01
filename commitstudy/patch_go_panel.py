"""テキスト画面のメニューの「ホーム」を、社労士版と同じ移動パネル(ホーム・テキスト一覧・ほかの科目)にする。
使い方: python3 patch_go_panel.py <index.html> <出力>   (go_panel.css を同じフォルダに置く)
"""
import json, os, sys
here = os.path.dirname(os.path.abspath(__file__))
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count: sys.exit(f"置換対象が {n} 件(期待 {count} 件): {old[:90]!r}")
    s = s.replace(old, new)
def jesc(t): return json.dumps(t, ensure_ascii=False)[1:-1].replace("</", "<\\/")
css = open(os.path.join(here, "go_panel.css"), encoding="utf-8").read()
rep(jesc("body.review .co.talk{display:none}\n"), jesc("body.review .co.talk{display:none}\n" + css))
HOME = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/></svg><span>ホーム</span>'
rep(jesc('<a class="mb" href="/" aria-label="ホームへ">' + HOME + '</a>'), jesc('<button class="mb" type="button" data-p="go" aria-expanded="false">' + HOME + '</button>'))
rep(jesc(' <section class="mpanel" id="p-view" hidden aria-label="表示設定">\n </section>\n'),
    jesc(' <section class="mpanel" id="p-view" hidden aria-label="表示設定">\n </section>\n <section class="mpanel" id="p-go" hidden aria-label="移動"><div id="go-list"></div></section>\n'))
rep('var PN=["toc","bm","note","find","view","more","list","set","qbm"];', 'var PN=["toc","bm","note","find","view","go","more","list","set","qbm"];')
rep('else if(n==="set")renderToolbar();else if(n==="list")', 'else if(n==="set")renderToolbar();else if(n==="go")renderGo();else if(n==="list")')
GO = r'''
/* ==移動パネル== メニューバーの「ホーム」: ホーム・テキスト一覧・ほかの科目へ(社労士版と同じ) */
var GO_CUR=(window.FAMV&&FAMV.id)||"d360",GO_LIST=[{"id":"d360","short":"D360","title":"Data 360 コンサルタント","color":"#24345e"},{"id":"mcadmin","short":"MCA","title":"Marketing Cloud Administrator","color":"#b5560f"}];
function renderGo(){
  var box=byId("go-list");if(!box)return;
  var e=function(s){return String(s).replace(/[&<>"]/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]})};
  var cell=function(x){var me=x.id===GO_CUR;return '<a class="go-s'+(me?" cur":"")+'" href="/'+x.id+'/"'+(me?' aria-current="page"':"")+' style="--gc:'+e(x.color)+'"><b>'+e(x.short)+'</b><small>'+e(x.title)+(me?"(いまの画面)":"")+'</small></a>'};
  box.innerHTML='<div class="go-top"><a class="go-a" href="/"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/></svg>ホーム</a>'+
    '<a class="go-a" href="/texts/#'+e(GO_CUR)+'"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 5.5C5.5 4 8.5 4 12 6c3.5-2 6.5-2 9-.5V19c-2.5-1.5-5.5-1.5-9 .5-3.5-2-6.5-2-9-.5z"/><path d="M12 6v13.5"/></svg>テキスト一覧</a></div>'+
    '<div class="mp-h">科目</div><div class="go-grid">'+GO_LIST.map(cell).join("")+'</div>';
}
'''
rep("function dimOpts(){", GO + "function dimOpts(){")
open(out, "w", encoding="utf-8").write(s); print("ok")
