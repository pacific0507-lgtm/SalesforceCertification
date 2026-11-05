# 仕様: MuleSoft Platform Architect(Salesforce Certified MuleSoft Platform Architect)のテキスト+問題集(日本語)

CommitStudy(Salesforce認定資格の学習アプリ)に、MuleSoft Platform Architect 試験(旧 MuleSoft Certified Platform Architect - Level 1)の科目を追加します。
あなたは1つの章を担当し、各項目(節)の本文HTMLと、その本文にひも付いた **4択** 問題を作ります。

## 試験の範囲(公式の試験ガイドの出題分野。配分は情報源で食い違うため、本文には配分の数字を書かない)
- アプリケーションネットワークの基本(アプリケーションネットワーク、API 主導の接続、System / Process / Experience API、C4E)
- 組織とプラットフォームの基盤(Anypoint Platform の構成、コントロールプレーンとランタイムプレーン、ビジネスグループ・環境・アクセス管理)
- API の設計と共有(API 仕様 RAML / OAS、Design Center、モック、Anypoint Exchange、バージョン管理)
- API 実装の設計(Mule アプリケーション、APIkit、ドメインモデル、イベント駆動・非同期、信頼性・冪等性・キャッシュ)
- デプロイの選択肢とデプロイ(CloudHub 2.0・CloudHub(1.0)・Runtime Fabric・顧客ホスト、ワーカー/レプリカ、VPC/プライベートスペース、CI/CD)
- API のガバナンス(API Manager、自動検出、プロキシ、Flex Gateway、API ポリシー、SLA 層、クライアントアプリケーション、API Governance)
- 非機能要件と監視(可用性・スケーラビリティ・性能、Anypoint Monitoring、API 分析、アラート、Anypoint Visualizer)
試験の形式(第三者情報): 60問・120分・合格ライン70%。シナリオ型が中心。

## 調べ方(必須)
- 事実はすべて公式情報で確認する。主な情報源は MuleSoft の公式ドキュメント docs.mulesoft.com(日本語版 docs.mulesoft.com/ja/ もある)と、trailhead.salesforce.com の MuleSoft のモジュール。WebFetch で本文を読む。`mcp__Salesforce-Docs-MCP__salesforce_docs_search`(ToolSearch で "select:mcp__Salesforce-Docs-MCP__salesforce_docs_search,mcp__Salesforce-Docs-MCP__salesforce_docs_fetch" を読み込む。collection は "mulesoft/..." の形、collection://list で一覧)も使える。
- 推測で書かない。確認できなかったことは本文に書かない。製品名・画面名は公式の名前(Anypoint Platform、Anypoint Exchange、API Manager、Runtime Manager、Design Center、Anypoint Monitoring、Anypoint Visualizer、Anypoint MQ、Runtime Fabric、CloudHub 2.0、Flex Gateway、API Governance など)。日本語ドキュメントに公式の訳語があればそれを使い、初出は「日本語(英語)」で書く。改名・後継(例: CloudHub → CloudHub 2.0、ワーカー → レプリカ、Mule ゲートウェイ → Flex Gateway など)は、公式に確認できた範囲で初出に添える。
- 本文には、試験に出やすい制限値・既定値(公式に書かれているもの。例: vCore のサイズ、レプリカ数、ポリシーの既定の動き)も入れる。CloudHub(1.0)と CloudHub 2.0 で違う点は混同しないよう、どちらの話かを明記する。

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
- 各項目につき指定の問題数。**4択**(選択肢はちょうど4つ、正解は1つ。「2つ選択」の問題は作らない)。
- 試験と同じく、シナリオ型(「ある会社は…したい。アーキテクトは何を推奨すべきですか?」)を半分以上に。
- 誤りの選択肢も、もっともらしい MuleSoft / Anypoint Platform の機能名・用語にする。
- `ex`(解説): 2〜4文。正解の理由と、紛らわしい選択肢がなぜ違うか。
- `u`: 根拠にした公式ページのURL(docs.mulesoft.com か trailhead.salesforce.com)。
- `x`: **その問題の論点が書かれている本文の1要素の文字列そのもの**。同じ項目の html の中の <li> 1つ、<p> 1つ、または表の1行(<tr> の各セルの文字をつなげたもの)の、タグを除いた全文と完全一致させる。本文に論点がない問題は作らない(先に本文に書く)。
- 問題文・選択肢・解説はすべて日本語。

## 出力
ファイル `/home/user/SalesforceCertification/commitstudy/mulepa/manuscript/out_ch<章番号>.json` に次の形で書く(UTF-8、JSON):
{"chapter": <章番号>, "chapter_title": "...", "chapter_sub": "章の説明1文", "sections": [
  {"id": "<指定のID>", "no": "Ch<章>·<連番>", "title": "日本語の見出し", "tag": "英語名(短く)", "html": "...",
   "questions": [{"q": "...", "o": ["...","...","...","..."], "a": [正解のindex(0始まり)], "ex": "...", "u": "https://...", "x": "..."}]}
]}
書いたら自分で検証する: すべての x が、その項目の html からタグを除いた <li>/<p>/<tr> の文字列のどれかと完全一致すること、a が範囲内であること。
