"""CommitStudy に科目 MuleSoft Platform Architect(mulepa)を登録するパッチ(patch_add_afspec.py を当てた版に当てる)
  - FAMD.consts と エンジンの CFG(科目ごとの設定)に mulepa を追加
  - 科目リスト(ホーム・テキスト一覧・学習記録・ニュース・移動パネル・トレーニング・ルーター)に追加
使い方: python3 patch_add_mulepa.py <index.html> <出力>
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
ID, SHORT, TITLE, PAL, COLOR, NAME = "mulepa", "Mule\u200bPA", "MuleSoft Platform Architect", "blue", "#2456a6", "青"

# ---- FAMD.consts ----
lines = s.split("\n"); l = lines[4]
j = l.index("window.FAMD=") + len("window.FAMD="); F, end = json.JSONDecoder().raw_decode(l[j:])
REFS = "\n".join(f'<li><a href="{u}" target="_blank" rel="noopener noreferrer">{n}</a></li>' for n, u in [
    ("MuleSoft Platform Architect 資格(Trailhead)", "https://trailhead.salesforce.com/credentials/mulesoftplatformarchitecti"),
    ("MuleSoft ドキュメント(日本語)", "https://docs.mulesoft.com/ja/general/"),
    ("Anypoint Platform(MuleSoft ドキュメント)", "https://docs.mulesoft.com/general/"),
]) + "\n"
F["consts"][ID] = {"tab": "MuleSoft Platform Architect | CommitStudy", "bar": "MuleSoft Platform Architect テキスト+問題集",
    "h1": "MuleSoft Platform Architect", "refs": REFS, "ai": "MuleSoft", "prefix": "sr-" + ID, "pal": PAL}
lines[4] = l[:j] + json.dumps(F, ensure_ascii=False).replace("</", "<\\/") + l[j+end:]
s = "\n".join(lines)

# ---- エンジンの CFG ----
CFG = {
 "key": "sr-" + ID, "quizKey": "sr-" + ID + "-quiz-v1", "legacyPrefs": None,
 "srcs": [{"k": "orig", "label": "オリジナル問題(公式ドキュメントにもとづく)", "re": "^オリジナル"}, {"k": "past", "label": "過去問"}],
 "cx": ["アプリケーションネットワークの基本", "組織とプラットフォームの基盤", "API の設計と共有", "API 実装の設計", "デプロイ", "API のガバナンス", "非機能要件と監視"], "cxLabel": "出題範囲",
 "pal": PAL,
 "aiRole": "あなたは、Salesforce Certified MuleSoft Platform Architect 認定試験の学習を手伝う講師です。相手は初学者です。下の【テキスト】を主な根拠に、日本語で答えてください。",
 "aiqRole": "あなたはSalesforce Certified MuleSoft Platform Architect 認定試験の問題作成者です。問題は4択で作ってください。",
 "sub": "MuleSoft Platform Architect 認定試験の学習テキストと問題集です(問題は4択)。読みながら、わからないところをその場でAI先生に質問できます。本文の文字を選ぶとマーカーを引けて、自分用のメモも残せます。各項目の末尾から、その項目の問題にも進めます。",
 "h1": "MuleSoft Platform Architect",
 "qfoot": "問題は、試験の出題範囲と MuleSoft の公式ドキュメントをもとに作ったオリジナル問題(4択)です。根拠にした公式ページを各問題に付けています。画面や仕様はリリースで変わるため、最新の公式情報で確認してください。",
}
rep(',S={afspec:', ',S={' + ID + ':' + json.dumps(CFG, ensure_ascii=False) + ',afspec:')

# ---- 科目リスト(Agentforce スペシャリストの後ろに足す) ----
AFS = "{id:`afspec`,short:`AF\u200bSpec`,title:`Agentforce スペシャリスト`,pal:`purple`,color:`#6b3fa0`,name:`紫`,stage:`public`}"
NEW = "{id:`" + ID + "`,short:`" + SHORT + "`,title:`" + TITLE + "`,pal:`" + PAL + "`,color:`" + COLOR + "`,name:`" + NAME + "`,stage:`public`}"
n = s.count(AFS); assert n >= 3, n
s = s.replace(AFS, AFS + "," + NEW)
rep("ids:[`d360`,`mcadmin`,`afsales`,`afspec`]", "ids:[`d360`,`mcadmin`,`afsales`,`afspec`,`" + ID + "`]")
rep("$=[`d360`,`mcadmin`,`afsales`,`afspec`]", "$=[`d360`,`mcadmin`,`afsales`,`afspec`,`" + ID + "`]")
rep('{"id":"afspec","short":"AF\u200bSpec","title":"Agentforce スペシャリスト","color":"#6b3fa0"}',
    '{"id":"afspec","short":"AF\u200bSpec","title":"Agentforce スペシャリスト","color":"#6b3fa0"},{"id":"' + ID + '","short":"' + SHORT + '","title":"' + TITLE + '","color":"' + COLOR + '"}')
rep('{id:"afspec",short:"AF\u200bSpec",title:"Agentforce スペシャリスト",color:"#6b3fa0"}',
    '{id:"afspec",short:"AF\u200bSpec",title:"Agentforce スペシャリスト",color:"#6b3fa0"},{id:"' + ID + '",short:"' + SHORT + '",title:"' + TITLE + '",color:"' + COLOR + '"}')
rep('if(id==="afsales"||id==="afspec")return /^オリジナル/.test(s)?"orig":"past";', 'if(id==="afsales"||id==="afspec"||id==="' + ID + '")return /^オリジナル/.test(s)?"orig":"past";')
open(out, "w", encoding="utf-8").write(s); print("ok", n)
