# mcadmin Trailhead クイズ メモ

収集日: 2026-11-10。`out.json` は 32 問(要確認 1 問)。

## 使ったモジュール

公式の試験対策トレイル「Study for the Marketing Cloud Engagement Administrator Exam」
(https://trailhead.salesforce.com/content/learn/trails/study-for-the-marketing-cloud-administrator-exam、
認定資格ページ /credentials/marketingcloudadministrator からリンク)に入っているモジュールは次の2つだけでした。

1. marketing-cloud-admin-certification-prep-setup-and-data(準備: Marketing Cloud Engagement アドミニストレーター: セットアップ、データ)
   - get-started-with-the-marketing-cloud-administrator-certification-prep(クイズ 2 問)
   - study-up-on-setup(2 問)
   - review-subscriber-data-management(2 問)
2. marketing-cloud-admin-certification-prep-marketing-channels-maintenance(認定試験の準備: … マーケティング、チャネル、メンテナンス)
   - study-up-on-digital-marketing(2 問)
   - review-channel-management(2 問)
   - keep-up-with-maintenance(2 問)

この2つは試験の配点やトピックを問うクイズだけなので、上記の対策ユニットの「Related Badges(関連バッジ)」表で
公式に紹介されているモジュールも対象にしました。

3. mrkt_cloud_basics(Marketing Cloud Engagement の基本): study-up-on-setup と keep-up-with-maintenance の関連バッジ
   - mrkt_cloud_basics_get_started(2 問中 1 問を採用)
   - mrkt_cloud_basics_most(2 問中 1 問を採用)
   - mrkt_cloud_basics_products(2 問)
4. journey-builder-basics(Journey Builder の基本): review-channel-management の関連バッジ
   - get-started-with-journey-builder / configure-journey-builder-access / send-a-single-message-with-journey-builder(各 2 問)
5. marketing-cloud-data-management(Marketing Cloud Engagement データ管理): review-subscriber-data-management の関連バッジ
   - design-your-mc-data-model / build-your-data-model / move-your-data / collect-data-with-a-send-log / query-data-with-sql(各 2 問)

### 使わなかったもの
- customer-data-management-modern-marketers(review-subscriber-data-management の関連バッジ): CDP と一般的な顧客データの話で、
  試験の範囲(Engagement の設定)から外れるため除外。
- mrkt_cloud_basics_get_started Q1(第4次産業革命とは何か)と mrkt_cloud_basics_most Q2(Marketing Cloud Engagement サービスの
  導入支援の受け方): 試験範囲と関係が薄いため除外。
- 各モジュールの末尾にある 16 進数 ID のユニット(…/8a49f3e3…、…/986a31f2…、…_badge)は 404 またはバッジのページでクイズなし。
- 対策ユニット内の「Exam Practice Questions」「Flashcards」は外部の対話ツールで、HTML に問題が入っていないため対象外。

## 変換のルール
- 問題文と選択肢は公式の日本語版(/ja/content/learn/…)。英語を qe/oe に入れた。
- 「B と C」「A と C」「A と B」のような組み合わせの選択肢は、ビルド時に選択肢がシャッフルされると意味が崩れるため削除し、
  a を複数正解にした(試験対策の開始 Q1 → a [1,2]、デジタルマーケティング計画 Q1 → a [0,2]、送信ログ Q1 → a [0,1])。
  oe からも同じ選択肢を削除。
- 日本語版で「True / False」のまま英語だった正誤問題は「正しい / 誤り」にそろえた(oe は英語のまま)。
- 試験の配点・トピックを問う 10 問と受験規約の 1 問は、本文に対応する箇所がないため x は空。f は内容の近い節
  (セットアップ→account、購読者データ→subscribers、デジタルマーケティング→products、チャネル管理→email、
  メンテナンス→maintenance、受験規約・合格点→products)にした。

## 要確認
- 試験対策の開始 Q2(合格点): ユニット本文には合格点の記載がなく、"Curious about the logistics of the exam? Check out the exam guide."
  とだけある。受験ガイドや Trailhead Academy の試験ページはスクリプトで描画され、curl では本文が取れなかった。
  a は 67% と推定で入れてある。公式の受験ガイドで確認が必要。

## 根拠(ユニット本文の英語の文)

### 準備: セットアップ、データ
- 試験対策の開始 Q1: "Use Salesforce-approved study materials available on Trailhead to prepare for your certification exam, including certification exam guides, trailmixes/trails, …" / "Submit a case with the Certification Security Team if you see any activity that undermines exam security"
- 試験対策の開始 Q2: 要確認(上記)。
- セットアップ Q1: "…the setup section of the Salesforce Marketing Cloud Engagement Administrator exam, which makes up 38% of the overall exam."
- セットアップ Q2: "This section of the exam tests these topics. Configuring business units, permissions, and security / Configuring integrations / Marketing Cloud Engagement extension products / Setup features"
- 購読者データ Q1: "…the subscriber data management section …, which makes up 18% of the overall exam."
- 購読者データ Q2: "Profile center and preference attributes / Data quality and mail management / Contact model"

### 認定試験の準備: マーケティング、チャネル、メンテナンス
- デジタルマーケティング Q1: "…the digital marketing section …, which makes up 13% of the overall exam."
- デジタルマーケティング Q2: "Security best practices for data / Product offerings / Digital marketing compliance"
- チャネル管理 Q1: "…the channel management section …, which makes up 16% of the overall exam."
- チャネル管理 Q2: "Mobile Studio configurations / Email Studio configurations / Advertising Studio configurations / Journey Builder configurations"
- メンテナンス Q1: "…the maintenance section …, which makes up 15% of the overall exam."
- メンテナンス Q2: "Data cleanup / Reports / Other Marketing Cloud products / Managing Marketing Cloud accounts"
- (試験対策の開始ユニットにも "Digital marketing proficiency: 13% / Subscriber data management: 18% / Setup: 38% / Channel management 16% / Maintenance: 15%" とある)

### Marketing Cloud Engagement の基本
- get_started Q2: 製品表に "Email Studio" "Journey Builder" "Mobile Studio" がそれぞれ製品として載っている("Now let's take a look at the individual products.")。
- most Q1: "consider how Marketing Cloud Engagement can empower you to: Know your customers. … Personalize with intelligence. … Engage across the entire journey." 成功の条件は "Tip 4: Determine Your Success Criteria" で事前に決めるもの。
- products Q1: "Marketing Cloud Connect integrates Marketing Cloud Engagement across the Customer Success Platform" と、Agentforce Sales / Agentforce Service との連携例。
- products Q2: "This site is Salesforce Marketing Cloud Engagement's community home for real-time information on system performance and security."

### Journey Builder の基本
- アクセス権 Q1: "Responsive: Tailors the customer journey based on real-time events like purchases, mobile app downloads, reading an email, or closed service cases."
- アクセス権 Q2: "Select Marketing Cloud Engagement Channel Manager or Marketing Cloud Engagement Content Editor/Publisher."
- 使用開始 Q1: "Journey Folders: Store journeys in folders so they're easy to find. You can organize your journeys immediately after creating and saving them…"
- 使用開始 Q2: Flow Control Activities として Wait、Split、Join(と Wait Until)が説明されている。
- 1 通のメッセージ Q1: "Click Schedule and choose whether you want to send the journey immediately or at a scheduled date and time."
- 1 通のメッセージ Q2: "Click Validate to make sure every part of your journey is correct."

### Marketing Cloud Engagement データ管理
- データモデルの設計 Q1: "A DBOR is the source of truth for subscriber opt-in status and general info about that subscriber."
- データモデルの設計 Q2: "…foreign keys are used to connect data between two unique tables or sources."
- データモデルの構築 Q1: "Remember, the attributes need to be the same data type in order to make the connection."
- データモデルの構築 Q2: "Maggie sets the cardinality to one-to-many, since a customer can have multiple purchases."
- データの移動 Q1: "Marketing Cloud Engagement removes files from the SFTP and the safehouse after 21 days."
- データの移動 Q2: "…if the encrypted file is on an external FTP. In Automation Studio, you add an additional File Transfer activity to the workflow. The first one moves the file to the safehouse, the second one decrypts the file."
- 送信ログ Q1: "if you have an Enterprise 2.0 account, determine if you want to have the send log in the enterprise account or in the individual child accounts." / "we strongly recommend you use a data retention policy on your send logs"
- 送信ログ Q2: "While you can add new fields later to the send log, it is better to add all possible required fields at the beginning, since historical data can't be added after the send log has been created."
- SQL Q1: "Just remember, you won't be able to make changes to these precreated data views."
- SQL Q2: "Queries time-out after 30 minutes, and the more data to process, the more likely the query can time out."

## 重複
32 問の中に同じことを問う問題はなかった(配点の問題はセクションごとに別の内容)。
