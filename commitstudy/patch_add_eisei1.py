"""CommitStudy に科目 第一種衛生管理者(eisei1)を登録するパッチ(rebuild.sh の最後で当てる)。知人向けで一般公開はしない。
  - FAMD.consts と エンジンの CFG(科目ごとの設定)に eisei1 を追加。出典の絞り込みは「過去問(公表問題)」と「オリジナル問題」、
    出題範囲の絞り込みは5つの試験科目(c = 0〜4)
  - 科目リスト(ホーム・テキスト一覧・学習記録・ニュース・移動パネル・トレーニング・ルーター)に、情報セキュリティマネジメントの後ろに追加
  - 科目の並び(csFirstSubj)・トレーニングの出典(srcOf)・資格の種類(その他。CS_KIND と並び順の K にも明示)にも追加
  - 出題回の絞り込みで「令和8年10月公表」の形の回を認める(第二種の問題も同じ回にまとめる)。新しい回から並べる
  - 法改正の注記(データの lw)を、問題集とトレーニングで解説のあとに「法改正の注記」の枠で出す
  学習計画の科目リストは plan/plan.js にじかに書いてある
使い方: python3 patch_add_eisei1.py <index.html> <出力>
"""
import json, sys
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count: sys.exit(f"置換対象が {n} 件(期待 {count} 件): {old[:90]!r}")
    s = s.replace(old, new)
# 略称は「衛生」と「1種」の間に幅0の改行位置を入れ、狭い枠では2行に折り返す(AF​Service と同じ)
ID, SHORT, TITLE, PAL, COLOR, NAME = "eisei1", "衛生​1種", "第一種衛生管理者", "gray", "#3d4650", "グレー"

# ---- FAMD.consts ----
lines = s.split("\n"); li = [i for i, l in enumerate(lines) if "window.FAMD=" in l]
assert len(li) == 1, li
l = lines[li[0]]
j = l.index("window.FAMD=") + len("window.FAMD="); F, end = json.JSONDecoder().raw_decode(l[j:])
REFS = "\n".join(f'<li><a href="{u}" target="_blank" rel="noopener noreferrer">{n}</a></li>' for n, u in [
    ("第一種衛生管理者(安全衛生技術試験協会)", "https://www.exam.or.jp/introduction/h_shokai502"),
    ("公表試験問題(安全衛生技術試験協会)", "https://www.exam.or.jp/lckohyo"),
    ("e-Gov 法令検索(労働安全衛生法)", "https://laws.e-gov.go.jp/law/347AC0000000057"),
]) + "\n"
F["consts"][ID] = {"tab": "第一種衛生管理者 | CommitStudy", "bar": "第一種衛生管理者 テキスト+問題集",
    "h1": "第一種衛生管理者", "refs": REFS, "ai": "第一種衛生管理者", "prefix": "sr-" + ID, "pal": PAL}
lines[li[0]] = l[:j] + json.dumps(F, ensure_ascii=False).replace("</", "<\\/") + l[j+end:]
s = "\n".join(lines)

# ---- エンジンの CFG ----
CFG = {
 "key": "sr-" + ID, "quizKey": "sr-" + ID + "-quiz-v1", "legacyPrefs": None,
 "srcs": [{"k": "past", "label": "過去問(公表問題・出題回つき)"}, {"k": "orig", "label": "オリジナル問題(法令・公式資料にもとづく)", "re": "^オリジナル"}],
 "cx": ["関係法令(有害業務)", "労働衛生(有害業務)", "関係法令(有害業務以外)", "労働衛生(有害業務以外)", "労働生理"], "cxLabel": "試験科目",
 "pal": PAL,
 "aiRole": "あなたは、第一種衛生管理者免許試験の学習を手伝う講師です。相手は初学者です。下の【テキスト】を主な根拠に、日本語で答えてください。法令は2026年11月時点で施行されているものにもとづいて説明し、改正があった点はそのことも伝えてください。",
 "aiqRole": "あなたは第一種衛生管理者免許試験の問題作成者です。問題は5肢択一で作ってください。",
 "sub": "第一種衛生管理者免許試験の学習テキストと問題集です(問題は5肢択一)。試験は44問・3時間・400点で、科目ごとに40%以上かつ全体で60%以上が合格の基準です。問題集には、オリジナル問題と、公表問題(過去問)10回分を出題回つきで収録しています。読みながら、わからないところをその場でAI先生に質問できます。",
 "h1": "第一種衛生管理者",
 "qfoot": "問題は、法令と公式資料をもとに作ったオリジナル問題(5肢択一)と、安全衛生技術試験協会の公表問題(令和4年4月〜令和8年10月公表の10回分と、第二種だけの問題)です。公表問題の正解は公表された正答のとおりです。その後の法改正が関わる問題には、解説のあとに「法改正の注記」を付けています。",
}
rep(',S={afsvc:', ',S={' + ID + ':' + json.dumps(CFG, ensure_ascii=False) + ',afsvc:')

# ---- 科目リスト(情報セキュリティマネジメントの後ろに足す) ----
SG = "{id:`sg`,short:`SG`,title:`情報セキュリティマネジメント`,pal:`pink`,color:`#a8336d`,name:`ピンク`,stage:`public`}"
NEW = "{id:`" + ID + "`,short:`" + SHORT + "`,title:`" + TITLE + "`,pal:`" + PAL + "`,color:`" + COLOR + "`,name:`" + NAME + "`,stage:`public`}"
n = s.count(SG); assert n >= 3, n
s = s.replace(SG, SG + "," + NEW)
# 移動パネル(JSON形式)
rep('{"id":"sg","short":"SG","title":"情報セキュリティマネジメント","color":"#a8336d"}',
    '{"id":"sg","short":"SG","title":"情報セキュリティマネジメント","color":"#a8336d"},{"id":"' + ID + '","short":"' + SHORT + '","title":"' + TITLE + '","color":"' + COLOR + '"}')
# トレーニング
rep('{id:"sg",short:"SG",title:"情報セキュリティマネジメント",color:"#a8336d"}',
    '{id:"sg",short:"SG",title:"情報セキュリティマネジメント",color:"#a8336d"},{id:"' + ID + '",short:"' + SHORT + '",title:"' + TITLE + '",color:"' + COLOR + '"}')
# トレーニングの出典(オリジナル・過去問)
rep('if(id==="d360"||id==="afsales"||', 'if(id==="d360"||id==="' + ID + '"||id==="afsales"||')
# 科目の並び(最初の科目の名前)・ルーター
rep('sg:"情報セキュリティマネジメント"};var id=csOrd', 'sg:"情報セキュリティマネジメント",' + ID + ':"第一種衛生管理者"};var id=csOrd')
rep("`fe`,`sg`];async", "`fe`,`sg`,`" + ID + "`];async")
# 資格の種類は「その他」(載っていない科目もその他になるが、明示しておく)
rep('sg:"ipa"},CS_KINDL', 'sg:"ipa",' + ID + ':"etc"},CS_KINDL')
rep('fe:1,sg:1}', 'fe:1,sg:1,' + ID + ':2}')

# ---- 出題回: 「令和8年10月公表」の形 ----
rep('function yrOf(q){\n  if(!q)return "";',
    'function yrOf(q){\n  if(!q)return "";var mk=/^((?:令和|平成)(?:元|\\d+)年\\d+月公表)/.exec(String(q.exam||q.src||""));if(mk)return mk[1];')
rep('function yrKey(y){',
    'function yrKey(y){var mk=/^(令和|平成)(元|\\d+)年(\\d+)月公表$/.exec(String(y||""));if(mk)return ((mk[1]==="令和"?2018:1988)+(mk[2]==="元"?1:+mk[2]))*100+(+mk[3]);')

# ---- 法改正の注記(lw) ----
rep('xs:d.xs||"",km:d.km||""};', 'xs:d.xs||"",km:d.km||"",lw:d.lw||""};')
rep('h+=histHtml(q)+(q.t==="mc"?mcMeta(q)',
    'if(q.lw)h+=\'<div class="lawnote" role="note"><h4>法改正の注記</h4><p>\'+esc(q.lw)+"</p></div>";\n    h+=histHtml(q)+(q.t==="mc"?mcMeta(q)')
# トレーニング
rep('ex:d.ex||d.e||"",sec:sec', 'ex:d.ex||d.e||"",lw:d.lw||"",sec:sec')
rep("h+='<div class=\"tq-ex\"><b>解説</b><p>'+esc(q.ex)+'</p></div>';",
    "h+='<div class=\"tq-ex\"><b>解説</b><p>'+esc(q.ex)+'</p></div>';if(q.lw)h+='<div class=\"lawnote\" role=\"note\"><h4>法改正の注記</h4><p>'+esc(q.lw)+'</p></div>';")
CSS = (".lawnote{margin:12px 0;padding:10px 14px;border-radius:12px;border:1px solid color-mix(in srgb,#b7791f 45%,transparent);"
       "background:color-mix(in srgb,#b7791f 10%,var(--surface,#fff));border-left:4px solid #b7791f}"
       ".lawnote h4{margin:0 0 4px;font-size:12.5px;letter-spacing:.08em;color:#8a5a00}"
       ".lawnote p{margin:0;font-size:14px;line-height:1.8;overflow-wrap:anywhere}"
       "html[data-theme=dark] .lawnote h4,.dark .lawnote h4{color:#e0b453}"
       "@media (prefers-color-scheme:dark){html:not([data-theme=light]) .lawnote h4{color:#e0b453}}")
JS = "<script>(function(){if(document.getElementById('cs-lawnote'))return;var st=document.createElement('style');st.id='cs-lawnote';st.textContent=" + json.dumps(CSS) + ";document.head.appendChild(st)})();</script>"
if s.count("</head>") != 1: sys.exit("</head> が1件ではない")
s = s.replace("</head>", JS + "</head>")
open(out, "w", encoding="utf-8").write(s); print("ok", n)
