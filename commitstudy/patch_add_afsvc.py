"""CommitStudy に科目 Agentforce Service コンサルタント(afsvc)を登録するパッチ(rebuild.sh の最後のほうで当てる)
  - FAMD.consts と エンジンの CFG(科目ごとの設定)に afsvc を追加
  - 科目リスト(ホーム・テキスト一覧・学習記録・ニュース・移動パネル・トレーニング・ルーター)に、Agentforce Sales の後ろに追加
  - 科目の並び(csFirstSubj)・テキスト一覧のグループ・トレーニングの出典(srcOf)にも追加
  学習計画の科目リストは plan/plan.js にじかに書いてある
使い方: python3 patch_add_afsvc.py <index.html> <出力>
"""
import json, sys
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count: sys.exit(f"置換対象が {n} 件(期待 {count} 件): {old[:90]!r}")
    s = s.replace(old, new)
# 略称は「AF」と「Service」の間に幅0の改行位置を入れ、狭い枠では2行に折り返す(AF​Sales と同じ)
ID, SHORT, TITLE, PAL, COLOR, NAME = "afsvc", "AF​Service", "Agentforce Service コンサルタント", "brown", "#7a4b2b", "茶"

# ---- FAMD.consts ----
lines = s.split("\n"); li = [i for i, l in enumerate(lines) if "window.FAMD=" in l]
assert len(li) == 1, li
l = lines[li[0]]
j = l.index("window.FAMD=") + len("window.FAMD="); F, end = json.JSONDecoder().raw_decode(l[j:])
REFS = "\n".join(f'<li><a href="{u}" target="_blank" rel="noopener noreferrer">{n}</a></li>' for n, u in [
    ("Agentforce Service Consultant 資格(Trailhead)", "https://trailhead.salesforce.com/credentials/servicecloudconsultant"),
    ("試験ガイド(Salesforce ヘルプ)", "https://help.salesforce.com/s/articleView?id=005298989&type=1"),
    ("Agentforce Service(Salesforce ヘルプ)", "https://help.salesforce.com/s/articleView?id=service.service_cloud.htm&type=5"),
]) + "\n"
F["consts"][ID] = {"tab": "Agentforce Service コンサルタント | CommitStudy", "bar": "Agentforce Service コンサルタント テキスト+問題集",
    "h1": "Agentforce Service コンサルタント", "refs": REFS, "ai": "Agentforce Service", "prefix": "sr-" + ID, "pal": PAL}
lines[li[0]] = l[:j] + json.dumps(F, ensure_ascii=False).replace("</", "<\\/") + l[j+end:]
s = "\n".join(lines)

# ---- エンジンの CFG ----
CFG = {
 "key": "sr-" + ID, "quizKey": "sr-" + ID + "-quiz-v1", "legacyPrefs": None,
 "srcs": [{"k": "orig", "label": "オリジナル問題(公式ヘルプにもとづく)", "re": "^オリジナル"}, {"k": "th", "label": "Trailhead のクイズ", "re": "^Trailhead"}],
 "cx": ["業界知識", "導入戦略", "ソリューション設計", "ナレッジ管理", "受付・対話チャネル", "ケース管理", "コンタクトセンター分析", "インテグレーション"], "cxLabel": "出題範囲",
 "pal": PAL,
 "aiRole": "あなたは、Salesforce Certified Agentforce Service Consultant(旧 Service Cloud Consultant)認定試験の学習を手伝う講師です。相手は初学者です。下の【テキスト】を主な根拠に、日本語で答えてください。",
 "aiqRole": "あなたはSalesforce Certified Agentforce Service Consultant 認定試験の問題作成者です。問題は4択で作ってください。",
 "sub": "Agentforce Service コンサルタント(旧 Service Cloud コンサルタント)認定試験の学習テキストと問題集です(問題は4択)。試験は60問・105分・合格ライン78%です。読みながら、わからないところをその場でAI先生に質問できます。本文の文字を選ぶとマーカーを引けて、自分用のメモも残せます。各項目の末尾から、その項目の問題にも進めます。",
 "h1": "Agentforce Service コンサルタント",
 "qfoot": "問題は、試験の出題範囲と Salesforce 公式ヘルプをもとに作ったオリジナル問題(4択)と、Trailhead のモジュールのクイズです。根拠にした公式ページを各問題に付けています。画面や仕様はリリースで変わるため、最新の公式情報で確認してください。",
}
rep(',S={sg:', ',S={' + ID + ':' + json.dumps(CFG, ensure_ascii=False) + ',sg:')

# ---- 科目リスト(Agentforce Sales の後ろに足す) ----
AFS = "{id:`afsales`,short:`AF​Sales`,title:`Agentforce Sales コンサルタント`,pal:`teal`,color:`#0b6e7c`,name:`青緑`,stage:`public`}"
NEW = "{id:`" + ID + "`,short:`" + SHORT + "`,title:`" + TITLE + "`,pal:`" + PAL + "`,color:`" + COLOR + "`,name:`" + NAME + "`,stage:`public`}"
n = s.count(AFS); assert n >= 3, n
s = s.replace(AFS, AFS + "," + NEW)
# 移動パネル(JSON形式)
rep('{"id":"afsales","short":"AF​Sales","title":"Agentforce Sales コンサルタント","color":"#0b6e7c"}',
    '{"id":"afsales","short":"AF​Sales","title":"Agentforce Sales コンサルタント","color":"#0b6e7c"},{"id":"' + ID + '","short":"' + SHORT + '","title":"' + TITLE + '","color":"' + COLOR + '"}')
# トレーニング
rep('{id:"afsales",short:"AF​Sales",title:"Agentforce Sales コンサルタント",color:"#0b6e7c"}',
    '{id:"afsales",short:"AF​Sales",title:"Agentforce Sales コンサルタント",color:"#0b6e7c"},{id:"' + ID + '",short:"' + SHORT + '",title:"' + TITLE + '",color:"' + COLOR + '"}')
# トレーニングの出典(オリジナル・Trailhead)
rep('if(id==="d360"||id==="afsales"||', 'if(id==="d360"||id==="afsales"||id==="' + ID + '"||')
# 科目の並び(最初の科目の名前)・テキスト一覧のグループ・ルーター
rep('afsales:"Agentforce Sales",', 'afsales:"Agentforce Sales",' + ID + ':"Agentforce Service",')
rep("`afsales`,`afspec`", "`afsales`,`" + ID + "`,`afspec`", 2)
open(out, "w", encoding="utf-8").write(s); print("ok", n)
