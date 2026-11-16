"""学習計画(/plan/)を追加する(社労士版の「学習計画」をもとに、複数の資格・受験日に対応)。
  - 下のタブ(5つに)・PC の上のメニュー・メニューのサイトマップに「計画」(学習計画)を足す。テキスト画面の移動パネルにも足す
  - 計画は 資格+受験予定日(まだ予定/申込済み)+始める日(任意)。いくつでも作れて、変更・削除できる。試験の日を過ぎたら結果を聞き、合格なら cs-subj-passed に印
  - 今日から試験の日までの日ごとの時間を、曜日ごとに使える時間から、残りの時間(必要な時間 − これまでの勉強時間)・試験の日の近さで資格ごとに分け、
    まだ読んでいない節・理解した印のない節・まだ解いていない/間違えた問題を割り当てる。週ごとの計画・今日やること・2週間の予定・ペースを出す
  - クラウドちゃんに相談(AI が設定の数字の案を JSON で出し、使うかは自分で選ぶ)と、週に1回のアドバイス。AI が使えないときは案内だけ
  - ホームの「きょうの一歩」に「今日の計画」のカード(計画がないときは、計画を立てる案内)。ホームのカスタマイズで並べ替え・非表示ができる
  - トレーニングは /practice/#s=<科目>&f=<絞り込み> で、科目と絞り込みを選んだ状態で開ける
  - 保存は cs-plan-v1(アカウントに同期・鍵ごと新しい方)。今日の目安の控え cs-plan-tg-v1 と AI の答え cs-plan-ai-v1 は端末だけ
使い方: python3 patch_plan.py <index.html> <出力>   (同じフォルダの plan.js / plan.css を使う)
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
def rd(p): return open(os.path.join(here, p), encoding="utf-8").read()

MARKUP = '''
<main class="wrap">
 <header class="ph">
  <p class="eyebrow">学習計画</p>
  <h1>試験の日まで、迷わない。</h1>
  <p>資格と受験予定日を入れると、今日から試験の日までの勉強の予定と「今日やること」を出します。これまでの勉強時間と進み具合から立てるので、予定より遅れたり進んだりしても、残りの日に自動で振り分け直します。</p>
 </header>
 <div id="groups" hidden></div>
 <div id="pl-root"></div>
</main>
'''
HOME_CSS = """
/* ホームの「今日の計画」 */
.pc{--c:var(--c1,var(--brand));--cs:var(--s1,var(--brand-soft))}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]) .pc{--c:var(--c2,var(--brand));--cs:var(--s2,var(--brand-soft))}}
:root[data-theme=dark] .pc{--c:var(--c2,var(--brand));--cs:var(--s2,var(--brand-soft))}
#bx-plan:empty{display:none}
#bx-plan{gap:10px}
#bx-plan .bx-k a{letter-spacing:0;font-weight:700;color:var(--brand);text-decoration:none}
#bx-plan .bx-t.sm{font-size:17px}
#bx-plan .bx-go.pri{margin-left:0;align-self:flex-start}
#bx-plan.cta{border-style:dashed}
#bx-plan .pl-meter{height:9px;border-radius:9px;background:var(--bg);border:1px solid var(--line);overflow:hidden}
#bx-plan .pl-meter i{display:block;height:100%;background:var(--sun);border-radius:9px;transition:width .8s var(--ease)}
.pl-st{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin:10px 0 4px;padding:10px 14px;border-radius:12px;font-size:14px;line-height:1.5;border:1.5px solid}
.pl-st b{font-size:15px;font-weight:800;white-space:nowrap}
.pl-st.ok{background:color-mix(in srgb,#16a34a 14%,var(--paper));border-color:color-mix(in srgb,#16a34a 55%,var(--paper));color:color-mix(in srgb,#15803d 90%,var(--ink))}
.pl-st.near{background:color-mix(in srgb,#f59e0b 16%,var(--paper));border-color:color-mix(in srgb,#f59e0b 55%,var(--paper));color:color-mix(in srgb,#b45309 90%,var(--ink))}
.pl-st.todo{background:color-mix(in srgb,var(--brand) 9%,var(--paper));border-color:color-mix(in srgb,var(--brand) 35%,var(--paper));color:var(--ink)}
.hp-l,.hp-pace{list-style:none;margin:0;padding:0;display:grid;gap:6px}
.hp-l li{display:grid;grid-template-columns:auto minmax(0,1fr) auto;gap:8px;align-items:baseline;font-size:13.5px;line-height:1.55;padding:7px 10px;border-radius:12px;background:var(--bg);border-left:4px solid var(--c)}
.hp-l li b{color:var(--c);white-space:nowrap}
.hp-l li span{min-width:0;overflow-wrap:anywhere}
.hp-l li small{color:var(--sub);font-weight:700;white-space:nowrap}
.hp-pace li{display:flex;align-items:center;gap:8px;font-size:12.5px}
.hp-pace li b{color:var(--c);min-width:4.2em}
.hp-pace small{color:var(--sub)}
.hp-ask{margin:0;padding:8px 10px;border-radius:12px;background:var(--cs);font-size:13.5px;font-weight:700;line-height:1.6;display:flex;flex-wrap:wrap;align-items:center;gap:4px 8px}
.hp-ask b{color:var(--c)}
.hp-ask a{display:inline-flex;align-items:center;gap:4px;color:var(--ink);font-size:13px}
.hp-ask a svg,#bx-plan .bx-go svg{width:14px;height:14px}
#bx-plan .pace{flex:none;display:inline-block;border-radius:999px;padding:1px 9px;font-size:12px;font-weight:800;background:var(--bg);color:var(--ink);white-space:nowrap}
#bx-plan .pace.ahead,#bx-plan .pace.ok,#bx-plan .pace.done{background:color-mix(in srgb,var(--ok) 18%,var(--paper));color:var(--ok)}
#bx-plan .pace.slow{background:var(--sun-soft)}
#bx-plan .pace.late,#bx-plan .pace.none{background:color-mix(in srgb,var(--ng) 15%,var(--paper));color:var(--ng)}
"""

# 1) ページの部品(FAMD.pages.plan)とホームのカード
lines = s.split("\n")
idx = [i for i, l in enumerate(lines) if "window.FAMD=" in l]
if len(idx) != 1: sys.exit(f"FAMD の行が {len(idx)} 件")
l = lines[idx[0]]
j = l.index("window.FAMD=") + len("window.FAMD="); F, end = json.JSONDecoder().raw_decode(l[j:])
if "plan" in F["pages"]: sys.exit("plan のページがすでにある")
F["pages"]["plan"] = {"title": "学習計画", "bodyPage": "plan", "css": F["pages"]["texts"]["css"] + rd("plan.css"), "markup": MARKUP}
hm = F["pages"]["home"]["markup"]
CONT = 'aria-label="前回の続き">'
k = hm.find(CONT)
if hm.count(CONT) != 1: sys.exit("home の前回の続きが見つからない")
k = hm.index("</article>", k) + len("</article>")
F["pages"]["home"]["markup"] = hm[:k] + '\n     <article class="bx" id="bx-plan" aria-label="今日の計画"></article>' + hm[k:]
F["pages"]["home"]["css"] += HOME_CSS
lines[idx[0]] = l[:j] + json.dumps(F, ensure_ascii=False).replace("</", "<\\/") + l[j+end:]
s = "\n".join(lines)

# 2) 下のタブを5つに(全ページの CSS)
n = s.count(".tabbar{grid-template-columns:repeat(4,1fr)!important}")
if n < 7: sys.exit(f"タブの CSS が {n} 件")
rep(".tabbar{grid-template-columns:repeat(4,1fr)!important}", ".tabbar{grid-template-columns:repeat(5,1fr)!important}", n)

# 3) ルーターとメニュー(ヘッダー・下のタブ・サイトマップ。4つのページの部品それぞれ)
rep('"/spec/":`spec`}', '"/spec/":`spec`,"/plan/":`plan`}')
NAV = '{id:`plan`,href:`/plan/`,label:`学習計画`,short:`計画`,icon:`<rect x="4" y="5" width="16" height="15" rx="2.5"/><path d="M8 3v4M16 3v4M4 10h16M9 15l2 2 4-4"/>`},'
rep('{id:`record`,href:`/record/`,label:`学習の記録`', NAV + '{id:`record`,href:`/record/`,label:`学習の記録`', 4)

# 4) ページの処理
rep("FAMP.record=function(){", rd("plan.js") + "\n\nFAMP.record=function(){")
# 5) ホーム: 今日の計画のカード(ホームのカスタマイズのあと)
HC = "(function(){var o=FAMP.home;FAMP.home=function(){o();setTimeout(csHC.home,0)}})();"
rep(HC, HC + "\n(function(){var o=FAMP.home;FAMP.home=function(){o();setTimeout(function(){try{csPlan.home()}catch(e){}},0)}})();")
# 6) ホームのカスタマイズに「今日の計画」を足す(前回の続きの次。保存にない id は既定の位置に入る)
rep('ids:["cont","streak","rank","garden"],mv:1}', 'ids:["cont","plan","streak","rank","garden"],mv:1}')
rep('cont:["前回の続き",""],', 'cont:["前回の続き",""],plan:["今日の計画","学習計画の今日の目安とペース"],')
rep('cont:"#bx-cont",', 'cont:"#bx-cont",plan:"#bx-plan",')
rep('var MAIN=["cont"],', 'var MAIN=["cont","plan"],')
# 7) アカウントに同期する鍵
rep("`cs-badge-told`,`cs-home-layout`]", "`cs-badge-told`,`cs-home-layout`,`cs-plan-v1`]")
# 8) テキスト画面の移動パネル(メニューバーの「ホーム」)
GO = "学習の記録</a></div>'+"
rep(GO, "学習の記録</a>'+'<a class=\"go-a go-plan\" href=\"/plan/\"><svg viewBox=\"0 0 24 24\" aria-hidden=\"true\"><rect x=\"4\" y=\"5\" width=\"16\" height=\"15\" rx=\"2.5\"/><path d=\"M8 3v4M16 3v4M4 10h16M9 15l2 2 4-4\"/></svg>学習計画</a></div>'+")
GOCSS = ("(function(){if(document.getElementById('cs-go-plan'))return;var st=document.createElement('style');st.id='cs-go-plan';"
         "st.textContent='.go-top>.go-a.go-plan{grid-column:1/-1}';document.head.appendChild(st)})();\n")
rep("FAMP.plan=function(){", GOCSS + "FAMP.plan=function(){")
# 9) トレーニング: #s=<科目>&f=<絞り込み> で開く(計画の「トレーニングで解く」から)
rep('if(location.hash==="#terms")ST.tab="g";',
    'if(location.hash==="#terms")ST.tab="g";'
    'var hm=/^#s=([a-z0-9]+)(?:&f=([a-z]+))?$/.exec(location.hash||"");if(hm&&SUBJ.some(function(x){return x.id===hm[1]})){ST.subj=hm[1];ST.src="all";ST.tab="q";'
    'if(["all","review","wrong","new"].indexOf(hm[2])>=0)ST.flt=hm[2];try{save()}catch(e){}try{resetSnap()}catch(e){}}')
open(out, "w", encoding="utf-8").write(s); print("ok")
