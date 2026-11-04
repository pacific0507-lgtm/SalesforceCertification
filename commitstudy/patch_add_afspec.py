"""CommitStudy に科目 Agentforce スペシャリスト(afspec)を登録するパッチ(patch_add_afsales.py を当てた版に当てる)
  - FAMD.consts と エンジンの CFG(科目ごとの設定)に afsales を追加
  - 科目リスト(ホーム・テキスト一覧・学習記録・ニュース・移動パネル・トレーニング・ルーター)に追加
使い方: python3 patch_add_afspec.py <index.html> <出力>
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
ID, SHORT, TITLE, PAL, COLOR, NAME = "afspec", "AF\u200bSpec", "Agentforce スペシャリスト", "purple", "#6b3fa0", "紫"

# ---- FAMD.consts ----
lines = s.split("\n"); l = lines[4]
j = l.index("window.FAMD=") + len("window.FAMD="); F, end = json.JSONDecoder().raw_decode(l[j:])
REFS = "\n".join(f'<li><a href="{u}" target="_blank" rel="noopener noreferrer">{n}</a></li>' for n, u in [
    ("Agentforce Specialist 資格(Trailhead)", "https://trailhead.salesforce.com/credentials/agentforcespecialist"),
    ("Agentforce(Salesforce ヘルプ)", "https://help.salesforce.com/s/articleView?id=ai.copilot_intro.htm&type=5"),
    ("Prompt Builder(Salesforce ヘルプ)", "https://help.salesforce.com/s/articleView?id=ai.prompt_builder_about.htm&type=5"),
]) + "\n"
F["consts"][ID] = {"tab": "Agentforce スペシャリスト | CommitStudy", "bar": "Agentforce スペシャリスト テキスト+問題集",
    "h1": "Agentforce スペシャリスト", "refs": REFS, "ai": "Agentforce", "prefix": "sr-" + ID, "pal": PAL}
lines[4] = l[:j] + json.dumps(F, ensure_ascii=False).replace("</", "<\\/") + l[j+end:]
s = "\n".join(lines)

# ---- エンジンの CFG ----
CFG = {
 "key": "sr-" + ID, "quizKey": "sr-" + ID + "-quiz-v1", "legacyPrefs": None,
 "srcs": [{"k": "orig", "label": "オリジナル問題(公式ヘルプにもとづく)", "re": "^オリジナル"}, {"k": "past", "label": "過去問"}],
 "cx": ["AIエージェント", "プロンプトエンジニアリング", "Data 360 の基礎", "テスト・デプロイ・保守", "ガバナンスと可観測性", "マルチエージェント"], "cxLabel": "出題範囲",
 "pal": PAL,
 "aiRole": "あなたは、Salesforce Certified Agentforce Specialist 認定試験の学習を手伝う講師です。相手は初学者です。下の【テキスト】を主な根拠に、日本語で答えてください。",
 "aiqRole": "あなたはSalesforce Certified Agentforce Specialist 認定試験の問題作成者です。問題は3択で作ってください。",
 "sub": "Agentforce スペシャリスト認定試験の学習テキストと問題集です(問題は3択)。読みながら、わからないところをその場でAI先生に質問できます。本文の文字を選ぶとマーカーを引けて、自分用のメモも残せます。各項目の末尾から、その項目の問題にも進めます。",
 "h1": "Agentforce スペシャリスト",
 "qfoot": "問題は、試験の出題範囲と Salesforce 公式ヘルプをもとに作ったオリジナル問題(3択)です。根拠にした公式ページを各問題に付けています。画面や仕様はリリースで変わるため、最新の公式情報で確認してください。",
}
rep(',S={afsales:', ',S={' + ID + ':' + json.dumps(CFG, ensure_ascii=False) + ',afsales:')

# ---- 科目リスト(Agentforce Sales の後ろに足す) ----
AFS = "{id:`afsales`,short:`AF\u200bSales`,title:`Agentforce Sales コンサルタント`,pal:`teal`,color:`#0b6e7c`,name:`青緑`,stage:`public`}"
NEW = "{id:`" + ID + "`,short:`" + SHORT + "`,title:`" + TITLE + "`,pal:`" + PAL + "`,color:`" + COLOR + "`,name:`" + NAME + "`,stage:`public`}"
n = s.count(AFS); assert n >= 3, n
s = s.replace(AFS, AFS + "," + NEW)
rep("ids:[`d360`,`mcadmin`,`afsales`]", "ids:[`d360`,`mcadmin`,`afsales`,`" + ID + "`]")
rep("$=[`d360`,`mcadmin`,`afsales`]", "$=[`d360`,`mcadmin`,`afsales`,`" + ID + "`]")
rep('{"id":"afsales","short":"AF\u200bSales","title":"Agentforce Sales コンサルタント","color":"#0b6e7c"}',
    '{"id":"afsales","short":"AF\u200bSales","title":"Agentforce Sales コンサルタント","color":"#0b6e7c"},{"id":"' + ID + '","short":"' + SHORT + '","title":"' + TITLE + '","color":"' + COLOR + '"}')
rep('{id:"afsales",short:"AF\u200bSales",title:"Agentforce Sales コンサルタント",color:"#0b6e7c"}',
    '{id:"afsales",short:"AF\u200bSales",title:"Agentforce Sales コンサルタント",color:"#0b6e7c"},{id:"' + ID + '",short:"' + SHORT + '",title:"' + TITLE + '",color:"' + COLOR + '"}')
rep('if(id==="afsales")return /^オリジナル/.test(s)?"orig":"past";', 'if(id==="afsales"||id==="' + ID + '")return /^オリジナル/.test(s)?"orig":"past";')
open(out, "w", encoding="utf-8").write(s); print("ok", n)
