# 仕様: Agentforce Sales コンサルタント(Salesforce Certified Agentforce Sales Consultant、旧 Sales Cloud Consultant)のテキスト+問題集(日本語)

CommitStudy(Salesforce認定資格の学習アプリ)に、Agentforce Sales Consultant 試験(Sales-Con-201)の科目を追加します。
あなたは1つの章を担当し、各項目(節)の本文HTMLと、その本文にひも付いた4択問題を作ります。

## 試験の範囲(出題範囲。合計100%)
1. Sales Lifecycle 20%: ビジネス要件・指標・KPI・課題に合う Agentforce Sales のソリューションを選ぶ/一般的な営業・マーケティングプロセスと導入の考慮点/Agentforce Sales の機能と関連製品(Sales Engagement、Salesforce Inbox(Einstein Activity Capture)、Enterprise Territory Management、売上予測(Collaborative Forecasts)、Sales の Einstein、生成AI・予測AI)の使い分け/ビジネス成果と営業KPIをレポート・ダッシュボードにする
2. Consulting and Implementation Strategies 25%: 導入前(UX・コミュニケーション・トレーニング・変革管理・成功指標)/導入中(リリース・デプロイの考慮点)/導入後(定着率の低さ・要件変化・ユーザーアクセス管理・継続的改善)/プロジェクト管理ライフサイクル/ディスカバリーワークショップ・要件分析・ソリューション定義・ユースケースの優先順位付け
3. Practical Application of Agentforce Sales Expertise 24%: リード→商談→見積→成約のエンドツーエンドの営業プロセス/宣言型ツールの限界と、カスタム開発・AppExchange・他製品・生産性ツール(メール連携、Slack、Salesforce モバイルアプリ)/セキュリティモデル(共有ルール、ロール階層、取引先チーム・商談チーム、権限セット、権限セットグループ)/商談商品・商品・価格表・見積・複数通貨/キャンペーン・リード・商談のさまざまな業務シナリオ
4. Data Management 18%: データ移行とインテグレーションのユースケースと考慮点/ソリューションのスケーラビリティ(大量データ、データスキューなど)/営業データの品質管理
5. Predictive and Generative AI 13%: Agentforce Sales の生成AIツール/予測AIツール/AIの倫理的課題と Salesforce の信頼できるAIの原則
試験の形式: 60問(採点対象)+採点対象外 最大5問、105分、合格ライン73%、シナリオ型が中心。

## 調べ方(必須)
- 事実はすべて公式情報で確認する。`mcp__Salesforce-Docs-MCP__salesforce_docs_search`(ToolSearch で "select:mcp__Salesforce-Docs-MCP__salesforce_docs_search,mcp__Salesforce-Docs-MCP__salesforce_docs_fetch" を読み込む)で help.salesforce.com の Sales Cloud / Agentforce Sales のページを探す。必要なら WebFetch で help.salesforce.com・trailhead.salesforce.com・architect.salesforce.com の本文を読んでよい。
- 推測で書かない。確認できなかったことは本文に書かない。製品名は現在の公式名(Agentforce Sales(旧 Sales Cloud)、Einstein Activity Capture、Enterprise Territory Management、Collaborative Forecasts、Pipeline Inspection、Agentforce の各エージェント など)。改名されたものは初出で「旧称」も添える。画面名は英語か日本語の公式表記のまま「 」で書いてよい。
- 本文には、試験に出やすい制限値・既定値(公式に書かれているもの)も入れる。

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
- 各項目につき指定の問題数。4択(正解1つ。「2つ選択」の問題は全体の1〜2割まで、そのときは問題文末に「(2つ選択)」)。
- 試験と同じく、シナリオ型(「ある会社は…したい。コンサルタントは何を推奨すべきですか?」)を半分以上に。
- 誤りの選択肢も、もっともらしいSalesforceの機能名・用語にする。
- `ex`(解説): 2〜4文。正解の理由と、紛らわしい選択肢がなぜ違うか。
- `u`: 根拠にした公式ページのURL(help.salesforce.com か trailhead.salesforce.com)。
- `x`: **その問題の論点が書かれている本文の1要素の文字列そのもの**。同じ項目の html の中の <li> 1つ、<p> 1つ、または表の1行(<tr> の各セルの文字をつなげたもの)の、タグを除いた全文と完全一致させる。本文に論点がない問題は作らない(先に本文に書く)。
- 問題文・選択肢・解説はすべて日本語。

## 出力
ファイル `/home/user/SalesforceCertification/commitstudy/afsales/manuscript/out_ch<章番号>.json` に次の形で書く(UTF-8、JSON):
{"chapter": <章番号>, "chapter_title": "...", "chapter_sub": "章の説明1文", "sections": [
  {"id": "<指定のID>", "no": "Ch<章>·<連番>", "title": "日本語の見出し", "tag": "英語名(短く)", "html": "...",
   "questions": [{"q": "...", "o": ["...","...","...","..."], "a": [正解のindex(0始まり)], "ex": "...", "u": "https://...", "x": "..."}]}
]}
書いたら自分で検証する: すべての x が、その項目の html からタグを除いた <li>/<p>/<tr> の文字列のどれかと完全一致すること、a が範囲内であること。
