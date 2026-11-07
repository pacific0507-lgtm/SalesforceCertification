"""CommitStudy に科目 情報セキュリティマネジメント(sg)を登録するパッチ(patch_add_fe.py を当てた版に当てる)
  - FAMD.consts と エンジンの CFG(科目ごとの設定)に sg を追加
  - 科目リスト(ホーム・テキスト一覧・学習記録・ニュース・移動パネル・トレーニング・ルーター)に追加
使い方: python3 patch_add_sg.py <index.html> <出力>
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
ID, SHORT, TITLE, PAL, COLOR, NAME = "sg", "SG", "情報セキュリティマネジメント", "pink", "#a8336d", "ピンク"

# ---- FAMD.consts ----
lines = s.split("\n"); l = lines[4]
j = l.index("window.FAMD=") + len("window.FAMD="); F, end = json.JSONDecoder().raw_decode(l[j:])
REFS = "\n".join(f'<li><a href="{u}" target="_blank" rel="noopener noreferrer">{n}</a></li>' for n, u in [
    ("情報セキュリティマネジメント試験(IPA)", "https://www.ipa.go.jp/shiken/kubun/sg.html"),
    ("試験要綱・シラバス(IPA)", "https://www.ipa.go.jp/shiken/syllabus/gaiyou.html"),
    ("公開問題(IPA)", "https://www.ipa.go.jp/shiken/mondai-kaiotu/sg_fe/koukai/index.html"),
]) + "\n"
F["consts"][ID] = {"tab": "情報セキュリティマネジメント | CommitStudy", "bar": "情報セキュリティマネジメント テキスト+問題集",
    "h1": "情報セキュリティマネジメント", "refs": REFS, "ai": "情報セキュリティマネジメント", "prefix": "sr-" + ID, "pal": PAL}
lines[4] = l[:j] + json.dumps(F, ensure_ascii=False).replace("</", "<\\/") + l[j+end:]
s = "\n".join(lines)

# ---- エンジンの CFG ----
CFG = {
 "key": "sr-" + ID, "quizKey": "sr-" + ID + "-quiz-v1", "legacyPrefs": None,
 "srcs": [{"k": "past", "label": "IPA 公開問題(出典つき)"}, {"k": "orig", "label": "オリジナル問題(シラバスと公式資料にもとづく)", "re": "^オリジナル"}],
 "cx": ["情報セキュリティの基礎と脅威", "情報セキュリティ技術", "情報セキュリティ管理", "情報セキュリティ対策とセキュリティ実装技術", "法務", "関連分野", "科目B 事例形式の考え方"], "cxLabel": "出題範囲",
 "pal": PAL,
 "aiRole": "あなたは、情報セキュリティマネジメント試験の学習を手伝う講師です。相手は初学者です。下の【テキスト】を主な根拠に、日本語で答えてください。相手は初学者です。下の【テキスト】を主な根拠に、日本語で答えてください。",
 "aiqRole": "あなたは情報セキュリティマネジメント試験の問題作成者です。問題は四肢択一で作ってください。",
 "sub": "情報セキュリティマネジメント試験の学習テキストと問題集です(問題は4択)。シラバスの分類に沿って科目A・科目Bを学べます。読みながら、わからないところをその場でAI先生に質問できます。本文の文字を選ぶとマーカーを引けて、自分用のメモも残せます。",
 "h1": "情報セキュリティマネジメント",
 "qfoot": "問題は、IPA の公開問題・サンプル問題(出典を各問題に明記)と、シラバスと公式資料をもとに作ったオリジナル問題(4択)です。公開問題は IPA が公表しているものを、許諾不要の範囲で使っています。",
}
rep(',S={fe:', ',S={' + ID + ':' + json.dumps(CFG, ensure_ascii=False) + ',fe:')

# ---- 科目リスト(fe の後ろに足す) ----
AFS = "{id:`fe`,short:`FE`,title:`基本情報技術者`,pal:`olive`,color:`#55691a`,name:`オリーブ`,stage:`public`}"
NEW = "{id:`" + ID + "`,short:`" + SHORT + "`,title:`" + TITLE + "`,pal:`" + PAL + "`,color:`" + COLOR + "`,name:`" + NAME + "`,stage:`public`}"
n = s.count(AFS); assert n >= 3, n
s = s.replace(AFS, AFS + "," + NEW)
rep("$=[`d360`,`mcadmin`,`afsales`,`afspec`,`mulepa`,`fe`]", "$=[`d360`,`mcadmin`,`afsales`,`afspec`,`mulepa`,`fe`,`" + ID + "`]")
rep('{"id":"fe","short":"FE","title":"基本情報技術者","color":"#55691a"}',
    '{"id":"fe","short":"FE","title":"基本情報技術者","color":"#55691a"},{"id":"' + ID + '","short":"' + SHORT + '","title":"' + TITLE + '","color":"' + COLOR + '"}')
rep('{id:"fe",short:"FE",title:"基本情報技術者",color:"#55691a"}',
    '{id:"fe",short:"FE",title:"基本情報技術者",color:"#55691a"},{id:"' + ID + '",short:"' + SHORT + '",title:"' + TITLE + '",color:"' + COLOR + '"}')
rep('if(id==="afsales"||id==="afspec"||id==="mulepa"||id==="fe")return /^オリジナル/.test(s)?"orig":"past";', 'if(id==="afsales"||id==="afspec"||id==="mulepa"||id==="fe"||id==="' + ID + '")return /^オリジナル/.test(s)?"orig":"past";')
# テキスト一覧のグループ: 見出しを「Salesforce・情報処理技術者試験」にして、IPA の2科目も同じ並べ替えの対象に入れる
rep("K=[{title:`Salesforce`,ids:[`d360`,`mcadmin`,`afsales`,`afspec`,`mulepa`]}]", "K=[{title:`Salesforce・情報処理技術者試験`,ids:[`d360`,`mcadmin`,`afsales`,`afspec`,`mulepa`,`fe`,`sg`]}]")
open(out, "w", encoding="utf-8").write(s); print("ok", n)
