# 仕様: Agentforce スペシャリスト(Salesforce Certified Agentforce Specialist)のテキスト+問題集(日本語)

CommitStudy(Salesforce認定資格の学習アプリ)に、Agentforce Specialist 試験の科目を追加します。
あなたは1つの章を担当し、各項目(節)の本文HTMLと、その本文にひも付いた **3択** 問題を作ります。

## 試験の範囲(Spring '26 の出題範囲。合計100%)
1. AI Agents 35%: Agentforce のエージェントの概念と種類、Agentforce Builder(旧 Agent Builder)でのエージェント作成、トピック・指示(インストラクション)・アクション、標準アクションとカスタムアクション(フロー・Apex・プロンプトテンプレート)、Atlas 推論エンジン、標準エージェント(Agentforce Service Agent など)、チャネルへの展開(Messaging・Experience Cloud・Slack など)
2. Prompt Engineering 20%: Prompt Builder、プロンプトテンプレートの種類、グラウンディング(差し込み項目・関連リスト・フロー・Apex・Data 360 のデータ)、プロンプトのベストプラクティス、モデルの選択(Einstein Studio/Model Builder、BYOLLM)
3. Data 360 Fundamentals 20%: Agentforce のための Data 360(旧 Data Cloud)、データライブラリ(RAG)、検索インデックス・ベクトル検索・リトリーバー、データの取り込みと統合の基礎、データの権限
4. Testing, Deployment & Maintenance 10%: Agentforce Testing Center(テストセンター)とテストの考え方、Sandbox での開発とデプロイ、バージョン管理、継続的な改善
5. Governance & Observability 10%: Einstein Trust Layer、監査とフィードバックのデータ、エージェントの分析・モニタリング、権限・ライセンス・ガードレール
6. Multi-Agent Orchestration 5%: 複数のエージェントの連携(エージェント間の受け渡し、Agent API など、公式に確認できる範囲)
試験の形式(第三者情報): 60問(採点対象)+採点対象外 最大5問、105分、合格ライン72%。シナリオ型が中心。

## 調べ方(必須)
- 事実はすべて公式情報で確認する。`mcp__Salesforce-Docs-MCP__salesforce_docs_search`(ToolSearch で "select:mcp__Salesforce-Docs-MCP__salesforce_docs_search,mcp__Salesforce-Docs-MCP__salesforce_docs_fetch" を読み込む)で help.salesforce.com の Agentforce / Einstein / Data 360 のページ(Agentforce Builder、Prompt Builder、Testing Center、Einstein Trust Layer など)を探す。必要なら WebFetch で help.salesforce.com・trailhead.salesforce.com・architect.salesforce.com の本文を読んでよい。
- 推測で書かない。確認できなかったことは本文に書かない。製品名は現在の公式名(Agentforce Sales(旧 Sales Cloud)、Einstein Activity Capture、Enterprise Territory Management、Collaborative Forecasts、Pipeline Inspection、Agentforce の各エージェント など)。改名されたものは初出で「旧称」も添える。画面名は英語か日本語の公式表記のまま「 」で書いてよい。
- 本文には、試験に出やすい制限値・既定値(公式に書かれているもの)も入れる。Agentforce は改名・仕様変更が多いので、現在の公式名と、初出での旧称(例: Agent Builder → Agentforce Builder、Einstein Copilot → Agentforce)を必ず確認する。

## 本文HTMLの書き方
見本: /tmp/claude-0/-home-user-SalesforceCertification/1fccc70c-a3a7-5e8a-825b-fb3720fd8239/scratchpad/afs/work/reference_sections.html(Data 360 の2項目。構造と文体を合わせる。図(figure)は不要。図はあとで別に作る)
各項目の `html` は、<article> と <h3> を除いた中身。次の順で並べる:
1. `<div class="co talk">…</div>` キャラの掛け合い(4〜6行)。
   - 話者: `<p class="tk pote"><b class="who">まなびん</b>…</p>`(学習者・くだけた口調)、`<p class="tk rou"><b class="who">クラウドちゃん</b>…</p>`(先生・です/ます)、`<p class="tk pen"><b class="who">コミットくん</b>…</p>`(ロボット・「〜だ」、短く、ときどきプログラミングのたとえ)。
   - 表情は任意で `data-f="smile|eager|sad|surprise|sweat|think|wink"` を p に付ける。
   - **項目ごとに掛け合いの型を変える**(出題して間違える/ボケとツッコミ/学習者が先に説明する/なぞなぞ/2人だけ/たとえ話のリレー/専門用語をかみ砕く など)。毎回「質問→説明→補足→なるほど」にしない。
2. `<p class="one">` その機能を一言で説明する1〜2文。
3. `<div class="co tips"><p><b class="lab">たとえるなら</b>…</p></div>` 身近なたとえ。
4. 本体: `<h4>見出し</h4>` と `<ul>`/`<ol class="steps">`/表 `<div class="tw"><table><thead><tr><th>…</th></tr></thead><tr><td>…</td></tr></table></div>` を組み合わせる。知識は1つの <li> に1つ。
5. 必要なら2つ目の掛け合い `<div class="co talk t2">…</div>`(2〜3行、補足)。
6. `<div class="co memo"><p><b class="lab">試験ポイント</b></p><ul><li>…</li></ul></div>` 試験に出やすい点を3〜5個。
- 文体: です/ます。1文は短く。専門用語は初出で一言説明。Markdown記号は使わない。<b> は強調に少しだけ。
- 1項目の本文はおよそ 900〜1600 字(掛け合いを除く)。

## 問題の書き方
- 各項目につき指定の問題数。**3択**(選択肢はちょうど3つ、正解は1つ。「2つ選択」の問題は作らない)。
- 試験と同じく、シナリオ型(「ある会社は…したい。コンサルタントは何を推奨すべきですか?」)を半分以上に。
- 誤りの選択肢も、もっともらしいSalesforceの機能名・用語にする。
- `ex`(解説): 2〜4文。正解の理由と、紛らわしい選択肢がなぜ違うか。
- `u`: 根拠にした公式ページのURL(help.salesforce.com か trailhead.salesforce.com)。
- `x`: **その問題の論点が書かれている本文の1要素の文字列そのもの**。同じ項目の html の中の <li> 1つ、<p> 1つ、または表の1行(<tr> の各セルの文字をつなげたもの)の、タグを除いた全文と完全一致させる。本文に論点がない問題は作らない(先に本文に書く)。
- 問題文・選択肢・解説はすべて日本語。

## 出力
ファイル `/home/user/SalesforceCertification/commitstudy/afspec/manuscript/out_ch<章番号>.json` に次の形で書く(UTF-8、JSON):
{"chapter": <章番号>, "chapter_title": "...", "chapter_sub": "章の説明1文", "sections": [
  {"id": "<指定のID>", "no": "Ch<章>·<連番>", "title": "日本語の見出し", "tag": "英語名(短く)", "html": "...",
   "questions": [{"q": "...", "o": ["...","...","..."], "a": [正解のindex(0始まり)], "ex": "...", "u": "https://...", "x": "..."}]}
]}
書いたら自分で検証する: すべての x が、その項目の html からタグを除いた <li>/<p>/<tr> の文字列のどれかと完全一致すること、a が範囲内であること。
