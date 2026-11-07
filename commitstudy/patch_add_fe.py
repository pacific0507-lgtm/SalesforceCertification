"""CommitStudy に科目 基本情報技術者(fe)を登録するパッチ(patch_add_mulepa.py を当てた版に当てる)。テキスト一覧では「情報処理技術者試験(IPA)」のグループに入れる
  - FAMD.consts と エンジンの CFG(科目ごとの設定)に fe を追加
  - 科目リスト(ホーム・テキスト一覧・学習記録・ニュース・移動パネル・トレーニング・ルーター)に追加
使い方: python3 patch_add_fe.py <index.html> <出力>
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
ID, SHORT, TITLE, PAL, COLOR, NAME = "fe", "FE", "基本情報技術者", "olive", "#55691a", "オリーブ"

# ---- FAMD.consts ----
lines = s.split("\n"); l = lines[4]
j = l.index("window.FAMD=") + len("window.FAMD="); F, end = json.JSONDecoder().raw_decode(l[j:])
REFS = "\n".join(f'<li><a href="{u}" target="_blank" rel="noopener noreferrer">{n}</a></li>' for n, u in [
    ("基本情報技術者試験(IPA)", "https://www.ipa.go.jp/shiken/kubun/fe.html"),
    ("試験要綱・シラバス(IPA)", "https://www.ipa.go.jp/shiken/syllabus/gaiyou.html"),
    ("公開問題(IPA)", "https://www.ipa.go.jp/shiken/mondai-kaiotu/sg_fe/koukai/index.html"),
]) + "\n"
F["consts"][ID] = {"tab": "基本情報技術者 | CommitStudy", "bar": "基本情報技術者 テキスト+問題集",
    "h1": "基本情報技術者", "refs": REFS, "ai": "基本情報技術者", "prefix": "sr-" + ID, "pal": PAL}
lines[4] = l[:j] + json.dumps(F, ensure_ascii=False).replace("</", "<\\/") + l[j+end:]
s = "\n".join(lines)

# ---- エンジンの CFG ----
CFG = {
 "key": "sr-" + ID, "quizKey": "sr-" + ID + "-quiz-v1", "legacyPrefs": None,
 "srcs": [{"k": "past", "label": "IPA 公開問題(出典つき)"}, {"k": "orig", "label": "オリジナル問題(シラバスと公式資料にもとづく)", "re": "^オリジナル"}],
 "cx": ["基礎理論", "アルゴリズムとプログラミング", "コンピュータ構成要素とハードウェア", "システム構成要素とソフトウェア", "ユーザーインタフェース・情報メディア・データベース", "ネットワーク", "セキュリティ", "開発技術", "プロジェクトマネジメント・サービスマネジメント", "システム戦略と経営戦略", "企業と法務", "科目B 対策"], "cxLabel": "出題範囲",
 "pal": PAL,
 "aiRole": "あなたは、基本情報技術者試験の学習を手伝う講師です。相手は初学者です。下の【テキスト】を主な根拠に、日本語で答えてください。相手は初学者です。下の【テキスト】を主な根拠に、日本語で答えてください。",
 "aiqRole": "あなたは基本情報技術者試験(科目A)の問題作成者です。問題は四肢択一で作ってください。",
 "sub": "基本情報技術者試験の学習テキストと問題集です(問題は4択)。シラバスの分類に沿って科目A・科目Bを学べます。読みながら、わからないところをその場でAI先生に質問できます。本文の文字を選ぶとマーカーを引けて、自分用のメモも残せます。",
 "h1": "基本情報技術者",
 "qfoot": "問題は、IPA の公開問題・サンプル問題(出典を各問題に明記)と、シラバスと公式資料をもとに作ったオリジナル問題(4択)です。公開問題は IPA が公表しているものを、許諾不要の範囲で使っています。",
}
rep(',S={mulepa:', ',S={' + ID + ':' + json.dumps(CFG, ensure_ascii=False) + ',mulepa:')

# ---- 科目リスト(mulepa の後ろに足す) ----
AFS = "{id:`mulepa`,short:`Mule\u200bPA`,title:`MuleSoft Platform Architect`,pal:`blue`,color:`#2456a6`,name:`青`,stage:`public`}"
NEW = "{id:`" + ID + "`,short:`" + SHORT + "`,title:`" + TITLE + "`,pal:`" + PAL + "`,color:`" + COLOR + "`,name:`" + NAME + "`,stage:`public`}"
n = s.count(AFS); assert n >= 3, n
s = s.replace(AFS, AFS + "," + NEW)
rep("$=[`d360`,`mcadmin`,`afsales`,`afspec`,`mulepa`]", "$=[`d360`,`mcadmin`,`afsales`,`afspec`,`mulepa`,`" + ID + "`]")
rep('{"id":"mulepa","short":"Mule\u200bPA","title":"MuleSoft Platform Architect","color":"#2456a6"}',
    '{"id":"mulepa","short":"Mule\u200bPA","title":"MuleSoft Platform Architect","color":"#2456a6"},{"id":"' + ID + '","short":"' + SHORT + '","title":"' + TITLE + '","color":"' + COLOR + '"}')
rep('{id:"mulepa",short:"Mule\u200bPA",title:"MuleSoft Platform Architect",color:"#2456a6"}',
    '{id:"mulepa",short:"Mule\u200bPA",title:"MuleSoft Platform Architect",color:"#2456a6"},{id:"' + ID + '",short:"' + SHORT + '",title:"' + TITLE + '",color:"' + COLOR + '"}')
rep('if(id==="afsales"||id==="afspec"||id==="mulepa")return /^オリジナル/.test(s)?"orig":"past";', 'if(id==="afsales"||id==="afspec"||id==="mulepa"||id==="' + ID + '")return /^オリジナル/.test(s)?"orig":"past";')
open(out, "w", encoding="utf-8").write(s); print("ok", n)
