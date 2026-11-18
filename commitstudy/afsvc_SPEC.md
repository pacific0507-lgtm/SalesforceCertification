# 仕様: Agentforce Service コンサルタント(Salesforce Certified Agentforce Service Consultant、旧 Service Cloud Consultant)のテキスト+問題集(日本語)

CommitStudy(Salesforce認定資格の学習アプリ)に、Agentforce Service Consultant 試験(Service-Con-201)の科目を追加します。
あなたは1つの章を担当し、各項目(節)の本文HTMLと、その本文にひも付いた4択問題を作ります。
担当する章の項目(ID・見出し・タグ・内容・問題数)は `/home/user/SalesforceCertification/commitstudy/afsvc/manuscript/plan.json` に書いてあります。ID・番号・見出し・問題数はそのとおりにしてください(見出しは表記の微調整だけ可)。

## 試験の範囲(出題範囲。合計100%)
出典: 公式試験ガイド「Salesforce Certified Agentforce Service Consultant Exam Guide」(https://help.salesforce.com/s/articleView?id=005298989&type=1 、Trailhead の https://trailhead.salesforce.com/help?article=Salesforce-Certified-Service-Cloud-Consultant-Exam-Guide から転送。2026-11-17 に確認)
1. Industry Knowledge 12%: コンタクトセンターの主要指標・KPI(平均処理時間、初回解決率、回避率など)に影響する要因/顧客が望む成果を実現するうえでのリスク・メリット・ビジネス課題
2. Implementation Strategies 12%: シナリオに応じたコンサルティングの進め方/デプロイとトレーニングの戦略/データ移行・データ品質・データガバナンス・大量データの考慮点
3. Agentforce Service Solution Design 15%: サービス担当者の体験(Service Console・レイアウト・Dynamic Forms・レコードページ)の設計と制約・トレードオフ/顧客体験の設計と制約・トレードオフ/データのセキュリティとコンプライアンス要件を満たす設計
4. Knowledge Management 12%: ナレッジ記事のライフサイクル、ナレッジ中心のサービス(KCS)、Salesforce Knowledge の設定/サービス支援とセルフサービスに使うナレッジの設定
5. Intake and Interaction Channels 13%: 受付チャネル(Email-to-Case、Web-to-Case など)の選び方と設計/対話チャネル(Messaging・Enhanced Chat・音声・SMS・ソーシャル・Slack など)のユースケースと機能/チャネル構成の設計の考慮点とベストプラクティス(Omni-Channel のルーティングを含む)/顧客サービスでのAIエージェントの適切な使い方/エージェント型サービス(Agentforce Service Agent)の機能・ユースケース・設定手順
6. Case Management 13%: 要件・KPIに合わせた、作成からクローズまでのケース管理の設計/Experience Cloud サイト・Agentforce・Knowledge によるケースの回避(デフレクション)/エンタイトルメント・マイルストン・資産・営業時間・SLA の機能・ユースケース・設定/Agentforce Service の自動化機能の使い分け
7. Contact Center Analytics 13%: 立場の違う関係者ごとに、必要な情報を出すレポートとダッシュボードを作る
8. Integrations 10%: Agentforce Service の主要なインテグレーション(サードパーティのソリューション、外部データソースへの接続)のユースケースと考慮点
試験の形式: 60問(採点対象)+採点対象外 最大5問、105分、合格ライン78%(英語版・日本語版とも)、受験料 30,000円(再受験 15,000円、税別)、前提資格は Salesforce 認定 Platform アドミニストレーター。出題は Summer '25 リリース準拠。シナリオ型が中心。

## 調べ方(必須)
- 事実はすべて公式情報で確認する。`mcp__Salesforce-Docs-MCP__salesforce_docs_search`(ToolSearch で "select:mcp__Salesforce-Docs-MCP__salesforce_docs_search,mcp__Salesforce-Docs-MCP__salesforce_docs_fetch" を読み込む)で help.salesforce.com の Agentforce Service(collection: admin/service)・Agentforce(admin/ai)のページを探す。必要なら WebFetch で help.salesforce.com・trailhead.salesforce.com・architect.salesforce.com の本文を読んでよい。
- 推測で書かない。確認できなかったことは本文に書かない。
- 製品名は現在の公式名を使う。改名されたものは初出で「旧称」も添える。2026-11 時点で確認した名前:
  - Agentforce Service(旧 Service Cloud)
  - Agentforce Service Agent(顧客対応のAIエージェント。Einstein Bots は 2026-08-17 から保守モード。新規導入は Agentforce を推奨)
  - Agentforce Builder のトピックは 2026年4月から「サブエージェント(subagents)」と呼ばれる(機能は同じ)。初出で「サブエージェント(旧称トピック)」と書く
  - Enhanced Chat(旧 Messaging for In-App and Web)。従来の Chat(Legacy Chat)は 2026-02-14 に提供終了
  - Partner Contact Center(旧 Service Cloud Voice / Salesforce Voice with Telephony Providers。Amazon Connect などの外部コンタクトセンターと連携)
  - Agentforce Contact Center(Salesforce に組み込まれたコンタクトセンター。Agentforce Contact Center Voice は旧 Salesforce Voice (Native Telephony))
  - Agentforce Field Service and Operations(旧 Field Service)
  - Data 360(旧 Data Cloud)
  - Omni-Channel、Omni-Channel フロー、Omni Supervisor、Service Console、Salesforce Knowledge(Lightning Knowledge)、Unified Knowledge、エンタイトルメント管理(Entitlements/Milestones)、Experience Cloud、Einstein for Service(Service Replies、Work Summaries、Einstein Case Classification、Einstein Article Recommendations など)、Customer Service Incident Management、Slack のスウォーミング(Swarming)
  - 公式ドキュメントは「エージェント(agent)」と区別するため、人の担当者を「サービス担当者(service rep)」と呼ぶ。本文もこれに合わせる。
- 画面名は英語か日本語の公式表記のまま「 」で書いてよい。
- 本文には、試験に出やすい制限値・既定値(公式に書かれているもの)も入れる。

## 本文HTMLの書き方
見本: /tmp/claude-0/-home-user-SalesforceCertification/1fccc70c-a3a7-5e8a-825b-fb3720fd8239/scratchpad/afs/work/reference_sections.html(Data 360 の2項目。構造と文体を合わせる。図(figure)は不要。図はあとで別に作る)。このファイルがない場合は、`/home/user/SalesforceCertification/commitstudy/afsales/manuscript/out_ch1.json` の最初の2項目の html を見本にする。
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
- 各項目につき plan.json の問題数。4択(正解1つ。「2つ選択」の問題は全体の1〜2割まで、そのときは問題文末に「(2つ選択)」)。
- 試験と同じく、シナリオ型(「あるコンタクトセンターは…したい。コンサルタントは何を推奨すべきですか?」)を半分以上に。
- 誤りの選択肢も、もっともらしいSalesforceの機能名・用語にする。
- `ex`(解説): 2〜4文。正解の理由と、紛らわしい選択肢がなぜ違うか。
- `u`: 根拠にした公式ページのURL(help.salesforce.com か trailhead.salesforce.com)。
- `x`: **その問題の論点が書かれている本文の1要素の文字列そのもの**。同じ項目の html の中の <li> 1つ、<p> 1つ、または表の1行(<tr> の各セルの文字をつなげたもの)の、タグを除いた全文と完全一致させる。本文に論点がない問題は作らない(先に本文に書く)。
- 問題文・選択肢・解説はすべて日本語。

## 出力
ファイル `/home/user/SalesforceCertification/commitstudy/afsvc/manuscript/out_ch<章番号>.json` に次の形で書く(UTF-8、JSON):
{"chapter": <章番号>, "chapter_title": "...", "chapter_sub": "章の説明1文", "sections": [
  {"id": "<指定のID>", "no": "Ch<章>·<連番>", "title": "日本語の見出し", "tag": "英語名(短く)", "html": "...",
   "questions": [{"q": "...", "o": ["...","...","...","..."], "a": [正解のindex(0始まり)], "ex": "...", "u": "https://...", "x": "..."}]}
]}
chapter_title・chapter_sub も plan.json のものを使う。
書いたら自分で検証する: すべての x が、その項目の html からタグを除いた <li>/<p>/<tr> の文字列のどれかと完全一致すること、a が範囲内であること。
