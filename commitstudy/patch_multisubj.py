"""CommitStudy に科目 Marketing Cloud Engagement Administrator (mcadmin) を追加できるようにするパッチ。
  - エンジンの設定(CFG)を科目ごとに切り替える(Data 360 の設定はそのまま)
  - テンプレートの Data 360 固有の文字(見出し・説明・参考リンク・問題集の注記)を科目ごとにする
  - 科目リスト(ホーム・科目一覧・学習記録・ルーター)に mcadmin を登録する
使い方: python3 patch_multisubj.py <index.html> <出力>
"""
import json, re, sys
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count: sys.exit(f"置換対象が {n} 件(期待 {count} 件): {old[:90]!r}")
    s = s.replace(old, new)

# ---- FAMD(consts とテンプレート)----
lines = s.split("\n"); l = lines[4]
j = l.index("window.FAMD=") + len("window.FAMD="); F, end = json.JSONDecoder().raw_decode(l[j:])
t = F["subject"]
# 参考リンク: Data 360 のリストを consts に移し、テンプレートは %%REFS%%
m = re.search(r'<ul class="refs">\n(.*?)</ul>', t, re.S); d360refs = m.group(1)
t = t.replace(m.group(0), '<ul class="refs">%%REFS%%</ul>')
F["consts"]["d360"]["refs"] = d360refs
# 見出しと説明・問題集の注記は科目ごと(JSで差し替え)。Data 360 の文はそのまま既定値として残す
t = t.replace('<h1>Salesforce Data 360</h1>', '<h1 id="subj-h1">Salesforce Data 360</h1>', 1)
t = t.replace('<p class="sub">Data 360 コンサルタント認定試験の学習テキストと問題集です。', '<p class="sub" id="subj-sub">Data 360 コンサルタント認定試験の学習テキストと問題集です。', 1)
t = t.replace('<footer>問題は、過去問と、Salesforce公式のTrailheadの確認問題', '<footer id="subj-qfoot">問題は、過去問と、Salesforce公式のTrailheadの確認問題', 1)
assert 'id="subj-h1"' in t and 'id="subj-sub"' in t and 'id="subj-qfoot"' in t
MCREFS = "\n".join(f'<li><a href="{u}" target="_blank" rel="noopener noreferrer">{n}</a></li>' for n, u in [
    ("Marketing Cloud Engagement Administrator 資格(Trailhead)", "https://trailhead.salesforce.com/credentials/marketingcloudadministrator"),
    ("Study for the Marketing Cloud Engagement Administrator Exam(Trailhead)", "https://trailhead.salesforce.com/content/learn/trails/study-for-the-marketing-cloud-administrator-exam"),
    ("Marketing Cloud Engagement Setup(Salesforce ヘルプ)", "https://help.salesforce.com/s/articleView?id=mktg.mc_overview_administration.htm&type=5"),
]) + "\n"
F["consts"]["mcadmin"] = {"tab": "Marketing Cloud Administrator | CommitStudy", "bar": "Marketing Cloud Administrator テキスト+問題集",
    "h1": "Marketing Cloud Administrator", "refs": MCREFS, "ai": "Marketing Cloud Engagement", "prefix": "sr-mcadmin", "pal": "orange"}
F["subject"] = t
lines[4] = l[:j] + json.dumps(F, ensure_ascii=False).replace("</", "<\\/") + l[j+end:]
s = "\n".join(lines)

# ---- エンジン: CFG を科目ごとに ----
i = s.index("var CFG=") + len("var CFG="); C, cend = json.JSONDecoder().raw_decode(s[i:])
MC = {
 "key": "sr-mcadmin", "quizKey": "sr-mcadmin-quiz-v1", "legacyPrefs": None,
 "srcs": [{"k": "orig", "label": "オリジナル問題(公式ヘルプにもとづく)"}],
 "cx": ["デジタルマーケティング", "サブスクライバーとデータ", "セットアップ", "チャネル", "メンテナンス"], "cxLabel": "出題範囲",
 "pal": "orange",
 "aiRole": "あなたは、Salesforce Marketing Cloud Engagement Administrator 認定試験の学習を手伝う講師です。相手は初学者です。下の【テキスト】を主な根拠に、日本語で答えてください。",
 "aiqRole": "あなたはSalesforce Marketing Cloud Engagement Administrator 認定試験の問題作成者です。",
 "sub": "Marketing Cloud Engagement Administrator 認定試験の学習テキストと問題集です。読みながら、わからないところをその場でAI先生に質問できます。本文の文字を選ぶとマーカーを引けて、自分用のメモも残せます。各項目の末尾から、その項目の問題にも進めます。",
 "h1": "Marketing Cloud Administrator",
 "qfoot": "問題は、Trailhead の資格対策モジュールの出題範囲と Salesforce 公式ヘルプをもとに作ったオリジナル問題です。根拠にした公式ページを各問題に付けています。画面や仕様はリリースで変わるため、最新の公式情報で確認してください。",
}
NEWCFG = "var CFG=(function(){var B=" + json.dumps(C, ensure_ascii=False) + ",S={mcadmin:" + json.dumps(MC, ensure_ascii=False) + "};var id=(window.FAMV&&FAMV.id)||\"d360\";return Object.assign({},B,S[id]||{})})()"
s = s[:i-len("var CFG=")] + NEWCFG + s[i+cend:]
# 見出し・説明・注記の差し替え(テキストの起動時に1回)
rep("function dimOpts(){", 'try{if(CFG.h1){var _h=byId("subj-h1");if(_h)_h.textContent=CFG.h1}if(CFG.sub){var _s=byId("subj-sub");if(_s)_s.textContent=CFG.sub}if(CFG.qfoot){var _f=byId("subj-qfoot");if(_f)_f.textContent=CFG.qfoot}}catch(e){}\nfunction dimOpts(){')

# ---- 科目リスト ----
D360 = "{id:`d360`,short:`D360`,title:`Data 360 コンサルタント`,pal:`navy`,color:`#24345e`,name:`紺`,stage:`public`}"
MCE = "{id:`mcadmin`,short:`MCA`,title:`Marketing Cloud Administrator`,pal:`orange`,color:`#b5560f`,name:`オレンジ`,stage:`public`}"
n = s.count(D360); assert n >= 3, n
s = s.replace(D360, D360 + "," + MCE)
rep("ids:[`d360`]", "ids:[`d360`,`mcadmin`]")
rep("$=[`d360`]", "$=[`d360`,`mcadmin`]")
open(out, "w", encoding="utf-8").write(s); print("ok", n)
