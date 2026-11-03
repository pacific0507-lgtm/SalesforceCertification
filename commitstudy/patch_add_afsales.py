"""CommitStudy に科目 Agentforce Sales コンサルタント(afsales)を登録するパッチ(patch_multisubj.py で科目切り替えの仕組みが入った版に当てる)
  - FAMD.consts と エンジンの CFG(科目ごとの設定)に afsales を追加
  - 科目リスト(ホーム・テキスト一覧・学習記録・ニュース・移動パネル・トレーニング・ルーター)に追加
使い方: python3 patch_add_afsales.py <index.html> <出力>
"""
import json, sys
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count: sys.exit(f"置換対象が {n} 件(期待 {count} 件): {old[:90]!r}")
    s = s.replace(old, new)
# 略称は「AF」と「Sales」の間に幅0の改行位置を入れ、狭い枠では2行に折り返す
ID, SHORT, TITLE, PAL, COLOR, NAME = "afsales", "AF\u200bSales", "Agentforce Sales コンサルタント", "teal", "#0b6e7c", "青緑"

# ---- FAMD.consts ----
lines = s.split("\n"); l = lines[4]
j = l.index("window.FAMD=") + len("window.FAMD="); F, end = json.JSONDecoder().raw_decode(l[j:])
REFS = "\n".join(f'<li><a href="{u}" target="_blank" rel="noopener noreferrer">{n}</a></li>' for n, u in [
    ("Agentforce Sales Consultant 資格(Trailhead)", "https://trailhead.salesforce.com/credentials/salescloudconsultant"),
    ("Agentforce Sales(Sales Cloud)ヘルプ", "https://help.salesforce.com/s/articleView?id=sales.sales_core.htm&type=5"),
    ("Salesforce Architects", "https://architect.salesforce.com/"),
]) + "\n"
F["consts"][ID] = {"tab": "Agentforce Sales コンサルタント | CommitStudy", "bar": "Agentforce Sales コンサルタント テキスト+問題集",
    "h1": "Agentforce Sales コンサルタント", "refs": REFS, "ai": "Agentforce Sales", "prefix": "sr-" + ID, "pal": PAL}
lines[4] = l[:j] + json.dumps(F, ensure_ascii=False).replace("</", "<\\/") + l[j+end:]
s = "\n".join(lines)

# ---- エンジンの CFG ----
CFG = {
 "key": "sr-" + ID, "quizKey": "sr-" + ID + "-quiz-v1", "legacyPrefs": None,
 "srcs": [{"k": "past", "label": "過去問"}, {"k": "orig", "label": "オリジナル問題(公式ヘルプにもとづく)", "re": "^オリジナル"}],
 "cx": ["セールスライフサイクル", "コンサルティングと導入戦略", "実践", "データ管理", "予測AIと生成AI"], "cxLabel": "出題範囲",
 "pal": PAL,
 "aiRole": "あなたは、Salesforce Certified Agentforce Sales Consultant(旧 Sales Cloud Consultant)認定試験の学習を手伝う講師です。相手は初学者です。下の【テキスト】を主な根拠に、日本語で答えてください。",
 "aiqRole": "あなたはSalesforce Certified Agentforce Sales Consultant 認定試験の問題作成者です。",
 "sub": "Agentforce Sales コンサルタント(旧 Sales Cloud コンサルタント)認定試験の学習テキストと問題集です。読みながら、わからないところをその場でAI先生に質問できます。本文の文字を選ぶとマーカーを引けて、自分用のメモも残せます。各項目の末尾から、その項目の問題にも進めます。",
 "h1": "Agentforce Sales コンサルタント",
 "qfoot": "問題は、過去問(解答を公式情報で検証し、必要なものは修正済み)と、試験の出題範囲と Salesforce 公式ヘルプをもとに作ったオリジナル問題です。根拠にした公式ページを各問題に付けています。画面や仕様はリリースで変わるため、最新の公式情報で確認してください。",
}
rep(',S={mcadmin:', ',S={' + ID + ':' + json.dumps(CFG, ensure_ascii=False) + ',mcadmin:')

# ---- 科目リスト ----
MCE = "{id:`mcadmin`,short:`MCA`,title:`Marketing Cloud Administrator`,pal:`orange`,color:`#b5560f`,name:`オレンジ`,stage:`public`}"
NEW = "{id:`" + ID + "`,short:`" + SHORT + "`,title:`" + TITLE + "`,pal:`" + PAL + "`,color:`" + COLOR + "`,name:`" + NAME + "`,stage:`public`}"
n = s.count(MCE); assert n >= 3, n
s = s.replace(MCE, MCE + "," + NEW)
rep("ids:[`d360`,`mcadmin`]", "ids:[`d360`,`mcadmin`,`" + ID + "`]")
rep("$=[`d360`,`mcadmin`]", "$=[`d360`,`mcadmin`,`" + ID + "`]")
# 移動パネル(JSON形式)
rep('{"id":"mcadmin","short":"MCA","title":"Marketing Cloud Administrator","color":"#b5560f"}',
    '{"id":"mcadmin","short":"MCA","title":"Marketing Cloud Administrator","color":"#b5560f"},{"id":"' + ID + '","short":"' + SHORT + '","title":"' + TITLE + '","color":"' + COLOR + '"}')
# トレーニング
rep('{id:"mcadmin",short:"MCA",title:"Marketing Cloud Administrator",color:"#b5560f"}',
    '{id:"mcadmin",short:"MCA",title:"Marketing Cloud Administrator",color:"#b5560f"},{id:"' + ID + '",short:"' + SHORT + '",title:"' + TITLE + '",color:"' + COLOR + '"}')
rep('if(id==="mcadmin")return "orig";', 'if(id==="mcadmin")return "orig";if(id==="' + ID + '")return /^オリジナル/.test(s)?"orig":"past";')
rep('var SRCN={past:"過去問",th:"Trailhead",orig:"オリジナル"};', 'var SRCN={past:"過去問",th:"Trailhead",orig:"オリジナル"};', 1)
# テキスト一覧の科目カードの略称は1行固定だったので、改行位置(幅0)で折り返せるようにする(D360・MCA は1語なので変わらない)
def jesc(t): return json.dumps(t, ensure_ascii=False)[1:-1].replace("</", "<\\/")
old = jesc("@media(max-width:600px){.tx .sh{font-size:18px!important")
assert s.count(old) >= 1, "テキスト一覧の略称のCSSが見つからない"
s = s.replace(jesc(".tx .sh{font-size:22px!important;white-space:nowrap;letter-spacing:-.03em}"), jesc(".tx .sh{font-size:22px!important;white-space:normal;overflow-wrap:normal;letter-spacing:-.03em}"))
open(out, "w", encoding="utf-8").write(s); print("ok", n)
