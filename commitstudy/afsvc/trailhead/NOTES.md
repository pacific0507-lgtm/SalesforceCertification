# Trailhead モジュールのクイズ: Agentforce Service コンサルタント (afsvc)

出題元: 公式 trailmix「Prepare for Your Agentforce Service Consultant Certification」(https://trailhead.salesforce.com/users/strailhead/trailmixes/prepare-for-your-salesforce-service-cloud-consultant-credential、資格ページ https://trailhead.salesforce.com/credentials/servicecloudconsultant からリンク)のモジュールとトレイル内のモジュール。一覧と選定は modules.md を参照。

- 問題数: 196(うち 要確認 7、日本語版がなく自分で訳したもの 10)
- 問題文と選択肢は公式の日本語版(/ja/)を使い、英語を qe/oe に入れた。日本語版がない(英語のまま表示される)ユニットは、日本語を自分で訳した(下の一覧で「日本語版なし・訳」と表示)。
- 正解は Trailhead の HTML に含まれないので、各ユニットの本文から判断した。根拠の文を下に引用した(本文中のインタラクティブ解説や同じモジュールの別の単元から引いたものはそう注記した)。
- ハンズオン(Challenge/assessment)のユニットとプロジェクト・スーパーバッジは対象外。
- ほかの科目(afsales・afspec)でクイズを使ったモジュール(large-data-volumes、sales_admin_duplicate_management、agentforce-service-agent-quick-look、retrieval-augmented-generation-quick-look)は、同じクイズが科目をまたいで重複しないよう使っていない。
- 近い内容の重複クイズは見つからなかった(英語の問題文と選択肢で、この科目内とほかの科目の trailhead/out.json を比較)。WhatsApp for Agentforce Service の「メッセージングコンポーネントで拡張する」Q1 と Q2 は選択肢が同じだが、問う内容(直近の注文のリスト/空いている時間枠)と正解が違うので両方残した。
- f はモジュール(一部はユニット)ごとに manuscript/plan.json の最も近い節を割り当てた。x は原稿(manuscript/out_ch*.json)の節の本文に明確に対応する文がある場合だけ入れ、ほかは空にした(x あり 15 問)。
- 2026-11-18 に各ユニットのページ(/ja/ と英語版)から取得。

## 使ったモジュールとユニット


### Advanced Salesforce Release Readiness Strategies
https://trailhead.salesforce.com/ja/content/learn/modules/advanced-salesforce-release-readiness-strategies

- Master the Release Readiness Process (master-the-release-readiness-process): クイズ 2問(日本語版なし・訳)
- Select and Prioritize Features (select-and-prioritize-features): ハンズオンのため対象外
- Test New Features Before a Release (test-new-features-before-a-release): クイズ 2問(日本語版なし・訳)
- Communicate New Features to Users (communicate-new-features-to-users): クイズ 2問(日本語版なし・訳)

### Agentforce Service の管理(Agentforce Service Administration)
https://trailhead.salesforce.com/ja/content/learn/modules/service_lex

- サービスコンソールを理解する (service_lex_cloud): クイズ 2問
- Agentforce Service の管理 (service_lex_connect): クイズ 2問
- ケース管理の自動化 (service_lex_case_manage): ハンズオンのため対象外
- 基本的なサービスチャネルを作成する (service_lex_channels): クイズ 2問

### Agentforce Service の基本(Agentforce Service Basics)
https://trailhead.salesforce.com/ja/content/learn/modules/service-cloud-platform-quick-look

- Agentforce Service 入門 (get-to-know-the-service-cloud-platform): クイズ 2問
- エージェンティックエクスペリエンスでケースをより迅速に解決する (resolve-cases-faster): クイズ 2問
- インテリジェントなオムニチャネルサービスを提供する (deliver-omnichannel-service): クイズ 2問

### Agentforce Service: クイックルック(Agentforce Service: Quick Look)
https://trailhead.salesforce.com/ja/content/learn/modules/servicecloud-quick-look

- インテリジェントなサービスのために AI と担当者を統合する (servicecloud-quick-look-1): クイズ 2問

### プロジェクト管理のベストプラクティス(Best Practices for Project Management)
https://trailhead.salesforce.com/ja/content/learn/modules/best-practices-for-project-management

- 要件の収集 (gather-requirements): クイズ 2問
- 活動、スケジュール、コストの計画 (plan-the-activities-schedule-and-cost): クイズ 2問
- リスクの管理 (manage-risk): クイズ 2問
- プロジェクトのパフォーマンスの管理 (manage-project-performance): クイズ 2問

### カスタマーサービスインシデント管理の基本(Customer Service Incident Management Basics)
https://trailhead.salesforce.com/ja/content/learn/modules/customer-service-incident-management-basics

- カスタマーサービスインシデント管理をはじめる (get-started-with-customer-service-incident-management): クイズ 2問
- カスタマーサービスインシデント管理を設定する (set-up-customer-service-incident-management): クイズ 2問
- インシデントについてのスウォームを作成する (create-and-swarm-on-an-incident): クイズ 2問
- 継続的な改善をめざす (aim-for-constant-improvement): クイズ 2問

### カスタマーサービスインシデント管理: クイックルック(Customer Service Incident Management: Quick Look)
https://trailhead.salesforce.com/ja/content/learn/modules/customer-service-incident-management-quick-look

- サービス障害に対処して、お客様の信頼を得る (address-disruptions-and-build-customer-trust): クイズ 2問

### サービス向けの Einstein 記事レコメンデーション(Einstein Article Recommendations for Service)
https://trailhead.salesforce.com/ja/content/learn/modules/einstein-article-recommendations-for-service

- Einstein 記事レコメンデーションについて知る (get-to-know-einstein-article-recommendations): クイズ 2問
- 記事レコメンデーションを使い始める (start-using-article-recommendations): クイズ 2問
- 記事レコメンデーションを向上させる (improve-einsteins-recommendations): クイズ 2問

### Einstein ボットの基礎(Einstein Bots Basics)
https://trailhead.salesforce.com/ja/content/learn/modules/service_bots_basics

- Einstein ボットの概要 (learn-about-einstein-bots): クイズ 2問
- ボットコンテンツの計画 (plan-your-bot-content): クイズ 2問
- Einstein ボットの前提条件と有効化 (enable-einstein-bots): クイズ 2問

### サービス向けの Einstein 分類アプリケーション(Einstein Classification Apps for Service)
https://trailhead.salesforce.com/ja/content/learn/modules/service_case_class

- Einstein 分類アプリケーションについて知る (learn-about-einstein-case-classification): クイズ 2問
- 分類アプリケーションのためのデータの準備 (prepare-your-data-for-case-classification): クイズ 2問
- Einstein 分類アプリケーションの有効化 (turn-on-einstein-case-classification): クイズ 2問

### Einstein サービス返信(Einstein Service Replies)
https://trailhead.salesforce.com/ja/content/learn/modules/einstein-service-replies

- サービスと生成 AI のメリットについて学ぶ (learn-the-benefits-of-service-and-generative-ai): クイズ 2問
- Einstein サービスチャット返信を設定して使用する (configure-and-use-service-replies-for-chat): クイズ 2問

### Einstein for Service のロールアウト戦略(Einstein for Service Rollout Strategies)
https://trailhead.salesforce.com/ja/content/learn/modules/einstein-for-service-rollout-strategies

- 人工知能を使用してサービスを向上させる (use-artificial-intelligence-to-improve-service): クイズ 2問
- ロールアウト戦略を作成する (create-a-rollout-strategy): クイズ 2問
- Einstein に向けた準備 (get-ready-for-einstein-service): クイズ 2問

### 拡張チャットの最適化(Enhanced Chat Optimization)
https://trailhead.salesforce.com/ja/content/learn/modules/messaging-optimization-for-in-app-and-web

- エンドユーザーを確認して、メッセージング履歴を共有する (verify-end-user-share-msg-history): クイズ 2問
- 情報を収集してエンドユーザーを迅速にサポートする (collect-information-to-help-end-users): クイズ 2問
- チャットボタンをいつ、どのように表示するかを決定する (decide-when-and-how-to-present-the-chat-button): クイズ 2問
- 構造化コンテンツをエンドユーザーに送信する (send-structured-content-to-end-users): クイズ 2問
- 顧客とメッセージをやり取りする (message-with-a-customer): クイズ 2問

### Lightning Experience の エンタイトルメント管理(Entitlement Management for Lightning Experience)
https://trailhead.salesforce.com/ja/content/learn/modules/entitlement-management-for-lightning-experience

- エンタイトルメント入門 (get-started-with-entitlements): ハンズオンのため対象外
- マイルストーンの設定 (set-up-milestones): クイズ 2問
- 顧客のケースでのエンタイトルメントの使用 (use-entitlements-in-customer-cases): クイズ 2問
- 作業指示でのエンタイトルメントの使用 (use-entitlements-with-work-orders): クイズ 2問

### Improved Service with Agentforce Commerce and Agentforce Service Integration
https://trailhead.salesforce.com/ja/content/learn/modules/improved-service-commerce-and-service-cloud

- Increase Service Excellence with Agentforce Commerce (increase-service-excellence-with-commerce-cloud): クイズ 2問(日本語版なし・訳)
- Improve Service with AI Agents (improve-returns-with-ai-agents): クイズ 2問(日本語版なし・訳)

### AI 向けのナレッジグラウンディング: クイックルック(Knowledge Grounding for AI: Quick Look)
https://trailhead.salesforce.com/ja/content/learn/modules/knowledge-grounding-for-ai-quick-look

- 大規模言語モデル向けにナレッジコンテンツを最適化する (optimize-knowledge-content-for-large-language-models): クイズ 2問

### ナレッジ検索の基本(Knowledge Search Basics)
https://trailhead.salesforce.com/ja/content/learn/modules/knowledge_search_basics

- Salesforce ナレッジの検索 (knowledge_search_basics_search): クイズ 3問
- 最適な検索オプションの選択 (knowledge_search_basics_choose): クイズ 3問
- 検索のカスタマイズの設定 (knowledge_search_basics_setup): クイズ 3問
- 分析を使用したより適切な判断 (knowledge_search_basics_make): クイズ 3問

### Agentforce Service のナレッジセンターサービス(Knowledge-Centered Service with Agentforce Service)
https://trailhead.salesforce.com/ja/content/learn/modules/knowledgecentered-service-in-lightning-knowledge

- ナレッジセンターサービスの使用開始 (get-started-with-knowledgecentered-service): クイズ 2問
- 記事の状況の管理 (manage-article-states): クイズ 2問
- KCS ユーザー向けの Lightning Knowledge の設定 (set-up-lightning-knowledge-for-kcs-users): クイズ 2問
- 記事検索と品質監査の最適化 (optimize-article-search-and-quality-audits): クイズ 2問
- 進化ループを使用したプロセスの改良 (use-evolve-loop-to-improve-your-process): クイズ 2問

### Lightning Knowledge への移行(Lightning Knowledge Migration)
https://trailhead.salesforce.com/ja/content/learn/modules/lightning-knowledge-migration

- Lightning Knowledge の機能の活用 (harness-the-power-of-lightning-knowledge): クイズ 2問
- 移行の計画 (plan-the-migration): クイズ 2問
- Sandbox へのテスト移行の実行 (perform-a-test-migration-to-a-sandbox): クイズ 2問
- Lightning Knowledge の設定 (set-up-lightning-knowledge): クイズ 2問
- 本番への移行 (migrate-into-production): クイズ 2問

### パートナーコンタクトセンター(Partner Contact Center)
https://trailhead.salesforce.com/ja/content/learn/modules/service-cloud-voice

- パートナーコンタクトセンターについて学ぶ (service-voice-learn): クイズ 2問
- パートナーコンタクトセンターの導入を計画する (service-voice-prepare): クイズ 3問

### パートナーコンタクトセンターの設定: クイックルック(Partner Contact Center Setup: Quick Look)
https://trailhead.salesforce.com/ja/content/learn/modules/service-cloud-voice-setup-quick-look

- パートナーコンタクトセンターの導入準備 (prepare-for-a-voice-implementation): クイズ 2問

### Salesforce のアジャイルの基礎(Salesforce Agile Basics)
https://trailhead.salesforce.com/ja/content/learn/modules/salesforce-agile-basics

- Salesforce がアジャイルを採用した理由の理解 (understand-why-salesforce-adopted-agile): クイズ 5問
- アジャイルの基本の学習 (learn-the-basics-of-agile): クイズ 3問
- リーンの原則の実践方法 (learn-to-use-lean-principles): クイズ 4問

### サービスの Salesforce フロー(Salesforce Flow for Service)
https://trailhead.salesforce.com/ja/content/learn/modules/service_lightning_flow_for_service

- サービスの Salesforce フローについて (learn-about-lightning-flow-for-service): クイズ 2問
- Salesforce フローと RecordAction について (tools-lightning-flow-for-service): クイズ 2問
- サービスの Salesforce フローの設定 (setup-lightning-flow-for-service): ハンズオンのため対象外

### Salesforce Knowledge の基本(Salesforce Knowledge Basics)
https://trailhead.salesforce.com/ja/content/learn/modules/lightning-knowledge-basics

- Knowledge 入門 (get-started-with-lightning-knowledge): クイズ 2問
- Salesforce 知識ベースを準備する (prepare-the-kb-for-success): クイズ 2問
- 簡単な知識ベースの設定 (set-up-a-simple-knowledge-base): クイズ 2問

### Salesforce メッセージング(Salesforce Messaging)
https://trailhead.salesforce.com/ja/content/learn/modules/salesforce-messaging

- メッセージングについて学ぶ (learn-about-messaging): クイズ 2問
- チャネルを使用してお客様にエンゲージする (engage-customers-using-channels): クイズ 2問
- 基本的なメッセージング実装を拡張する (enhance-a-basic-messaging-implementation): クイズ 2問

### Salesforce リリース準備状況戦略(Salesforce Release Readiness Strategies)
https://trailhead.salesforce.com/ja/content/learn/modules/sf_releases

- Salesforce のリリースプロセスを理解する (sf_releases_start): クイズ 2問
- Sandbox プレビューで早期アクセスを利用する (sf-releases-sandbox-preview): クイズ 2問
- 新機能の検索、有効化、コミュニケーション (sf_releases_strategy): クイズ 2問

### システム管理者向けの Salesforce アンケート(Salesforce Surveys for Admins)
https://trailhead.salesforce.com/ja/content/learn/modules/salesforce-surveys-for-admins

- アンケートを翻訳する (translate-your-surveys): ハンズオンのため対象外
- ケースの開始時や終了時にアンケートへの招待を送信する (surveys-case-scenario): クイズ 2問
- アンケートへの招待を自動化する (automate-your-survey-invitations): ハンズオンのため対象外
- 回答を分析する (analyze-your-survey-responses): ハンズオンのため対象外

### Salesforce でのスクラムと Kanban(Scrum and Kanban at Salesforce)
https://trailhead.salesforce.com/ja/content/learn/modules/scrum-and-kanban-at-salesforce

- スクラムについて (learn-about-scrum): クイズ 3問
- スクラムワークフローの要素 (learn-the-elements-of-the-scrum-workflow): クイズ 3問
- スクラムの実装 (implement-scrum): クイズ 3問
- Kanban について (learn-about-kanban): クイズ 3問
- 最適なワークフローの選択 (choose-the-best-workflow): クイズ 3問

### Service 設定アシスタント: クイックルック(Service Setup Assistant: Quick Look)
https://trailhead.salesforce.com/ja/content/learn/modules/service-setup-assistant-quick-look

- コンタクトセンターを設定する (set-up-your-contact-center-instantly): クイズ 2問

### Slack スウォーミング(Slack Swarming)
https://trailhead.salesforce.com/ja/content/learn/modules/swarming-with-slack-basics

- スウォーミングでカスタマーサービスを変革する (swarming-for-customer-success): クイズ 2問
- Slack スウォームを管理する (manage-a-swarm): クイズ 2問

### サービス向け Slack(Slack for Service)
https://trailhead.salesforce.com/ja/content/learn/modules/slack-first-service

- サービス向け Slack を知る (discover-slack-first-service): クイズ 2問
- Slack ファーストな考え方をサービスチームに取り入れる計画を作成する (create-a-plan-to-bring-slack-first-thinking-to-your-service-team): クイズ 2問

### Agentforce Service 向け WhatsApp(WhatsApp for Agentforce Service)
https://trailhead.salesforce.com/ja/content/learn/modules/whatsapp-for-service-cloud

- WhatsApp を使ってみる (get-started-with-whatsapp): クイズ 2問
- WhatsApp チャネルを細かく調整する (fine-tune-your-whatsapp-channel): クイズ 2問
- WhatsApp をメッセージングコンポーネントで拡張する (extend-whatsapp-with-messaging-components): クイズ 2問
- WhatsApp でお客様をサポートする (help-customers-in-whatsapp): クイズ 2問

### 使わなかったモジュール(ほかの科目で使用済み)

- Large Data Volumes (large-data-volumes)、Duplicate Management (sales_admin_duplicate_management): afsales で使用済み
- Agentforce for Service (agentforce-service-agent-quick-look)、Retrieval Augmented Generation: Quick Look (retrieval-augmented-generation-quick-look): afspec で使用済み
- trailmix のプロジェクト(Create a Process for Managing Support Cases、Build an Experience Cloud Site with Knowledge and Enhanced Chat、Set Up Case Escalation and Entitlements)、ヘルプ記事・PDF・記事、Trailhead Academy の有料コースはクイズがないので対象外

## 正解と根拠

### 1. Trailhead: Advanced Salesforce Release Readiness Strategies / Master the Release Readiness Process Q1
- 問題: Salesforce のメジャーリリースの新機能を実装するメリットはどれですか?
- 正解: A と C(a=[3])
- 根拠(ユニット本文・英語版): 「Deliver new functionality your users want without the need for custom code or third-party apps. / Simplify or enhance customizations in your backlog.」
- v: 要確認 / f: deploy
- 要確認の理由: 本文は3つ目のメリットとして「feature debt(棚上げされたイノベーション)の蓄積を防ぐ」も挙げる。選択肢 B は「undeployed feature licenses による future debt」と言い換えられており、別物とみなして A と C とした。
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/advanced-salesforce-release-readiness-strategies/master-the-release-readiness-process

### 2. Trailhead: Advanced Salesforce Release Readiness Strategies / Master the Release Readiness Process Q2
- 問題: リリースノートについて正しい説明はどれですか?
- 正解: リリースノートは頻繁に変わる生きた文書なので、Release Notes Changes の節で更新を定期的に確認するとよい。(a=[2])
- 根拠(ユニット本文・英語版): 「Release Notes Changes / Explore this living document with regular updates and changes during the course of each release cycle. You can find a link to the change log on the How to Use the Releases Notes page. We recommend that you review this section on a regular basis.」
- v: Trailhead のユニット本文で確認 / f: deploy
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/advanced-salesforce-release-readiness-strategies/master-the-release-readiness-process

### 3. Trailhead: Advanced Salesforce Release Readiness Strategies / Test New Features Before a Release Q1
- 問題: 自動化できないテストはどれですか?
- 正解: ユーザー受け入れテスト(UAT)(a=[3])
- 根拠(ユニット本文・英語版): 「User acceptance tests (UAT) give end users the opportunity to accept or reject the final feature delivery. / When you change your source code and push it to a source control repository (such as Git), your CI tool executes the scripts you’ve written for your unit, integration, functional, and UI tests.」
- v: Trailhead のユニット本文で確認 / f: deploy
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/advanced-salesforce-release-readiness-strategies/test-new-features-before-a-release

### 4. Trailhead: Advanced Salesforce Release Readiness Strategies / Test New Features Before a Release Q2
- 問題: 回帰テストの目的は何ですか?
- 正解: 変更後も既存のコードが動き続けることを確認する。(a=[0])
- 根拠(ユニット本文・英語版): 「It’s important to bear in mind that any modifications to the codebase may inadvertently introduce regressions (that is, changes that negatively impact existing functionality).」
- v: Trailhead のユニット本文で確認 / f: deploy
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/advanced-salesforce-release-readiness-strategies/test-new-features-before-a-release

### 5. Trailhead: Advanced Salesforce Release Readiness Strategies / Communicate New Features to Users Q1
- 問題: 新機能を、使う場面の中でユーザーに説明するのに最も適したコミュニケーションチャネルはどれですか?
- 正解: アプリ内ガイダンス(a=[2])
- 根拠(ユニット本文・英語版): 「In-App Prompt / Tell users what’s new, in context, at the right time.」
- v: Trailhead のユニット本文で確認 / f: deploy
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/advanced-salesforce-release-readiness-strategies/communicate-new-features-to-users

### 6. Trailhead: Advanced Salesforce Release Readiness Strategies / Communicate New Features to Users Q2
- 問題: Salesforce の実装のロードマップを作る目的は何ですか?
- 正解: A と B(a=[3])
- 根拠(ユニット本文・英語版): 「The roadmap is a tool to support two main objectives. / Get buy-in. / Plan. More use cases and complex functionality means more moving parts to coordinate. The roadmap helps identify high-level interdependencies and keep everyone on track.」
- v: Trailhead のユニット本文で確認 / f: deploy
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/advanced-salesforce-release-readiness-strategies/communicate-new-features-to-users

### 7. Trailhead: Agentforce Service の管理 / サービスコンソールを理解する Q1
- 問題: サービス担当者がメインペインでレコードを処理しながら、折りたたみ可能なサイドバーでケースのリストを確認できるコンソールの部分はどれですか?
- 正解: 分割ビュー(a=[1])
- 根拠(ユニット本文・日本語版): 「分割ビューでは、ケースのリストを折りたたみ可能なサイドバーとして開いたまま、メインペインでレコードを処理できます。」
- v: Trailhead のユニット本文で確認 / f: console
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/service_lex/service_lex_cloud

### 8. Trailhead: Agentforce Service の管理 / サービスコンソールを理解する Q2
- 問題: ケースを作成するとき、サービス担当者は顧客の問題に関する具体的なメモをどこに追加すべきですか?
- 正解: [Description (説明)] 項目(a=[3])
- 根拠(ユニット本文・日本語版): 「Description (説明): 具体的で詳細なメモを入力します。」
- v: Trailhead のユニット本文で確認 / f: console
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/service_lex/service_lex_cloud

### 9. Trailhead: Agentforce Service の管理 / Agentforce Service の管理 Q1
- 問題: 反復作業を減らすための知識ベースとマクロの実装は、サービスの設定のどのフェーズで行いますか?
- 正解: 生産性と効率性(a=[0])
- 根拠(ユニット本文・日本語版): 「生産性ツール: 担当者の反復作業をどのように削減するのか? マクロ、クイックテキスト、履歴を有効化してクリックを減らします。」
- v: Trailhead のユニット本文で確認 / f: deploy
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/service_lex/service_lex_connect

### 10. Trailhead: Agentforce Service の管理 / Agentforce Service の管理 Q2
- 問題: Salesforce Go の主な機能を正しく説明しているのはどれですか?
- 正解: 機能を見つけることを含め、実装業務を簡単に管理できるよう設計されている。(a=[1])
- 根拠(ユニット本文・日本語版): 「Salesforce Go は管理者にとって最も頼れるツールです。実装業務を簡単に管理できるよう設計されています。」
- v: Trailhead のユニット本文で確認 / f: deploy
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/service_lex/service_lex_connect

### 11. Trailhead: Agentforce Service の管理 / 基本的なサービスチャネルを作成する Q1
- 問題: メール-to-ケースの実装中に、メールアプリケーションを設定するためにシステム管理者が Salesforce からコピーする必要があるものは何ですか?
- 正解: メール転送アドレス(a=[2])
- 根拠(ユニット本文・日本語版): 「表示されたメール転送アドレスをコピーします。メールアドレスを、メールアプリケーションの適切なメール転送項目に貼り付けます。」
- v: Trailhead のユニット本文で確認 / f: intake / x: 「ルーティングアドレス(例: support@自社ドメイン)を設定し、メールシステムから Salesforce が発行するメールサービスアドレスへ転送します。指定のアドレスが宛先・CC・BCCのどれかにあればケースが作られます。」
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/service_lex/service_lex_channels

### 12. Trailhead: Agentforce Service の管理 / 基本的なサービスチャネルを作成する Q2
- 問題: Web-to-ケース HTML ジェネレーターの目的は何ですか?
- 正解: Web 開発者が公開する顧客向け Web フォームの HTML コードを提供する。(a=[1])
- 根拠(ユニット本文・日本語版): 「HTML コードをコピーし、Web サイトで公開するために Web 開発者に送信します。」
- v: Trailhead のユニット本文で確認 / f: intake
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/service_lex/service_lex_channels

### 13. Trailhead: Agentforce Service の基本 / Agentforce Service 入門 Q1
- 問題: Agentforce Service が Service Cloud から進化したことを示す根本的な変化は何ですか?
- 正解: AI、データ、CRM を統合してインテリジェントなエクスペリエンスを提供する。(a=[2])
- 根拠(ユニット本文・日本語版): 「Agentforce Service は、人工知能 (AI)、データ、CRM を統合して、サービスのあり方を大きく変えます。」
- v: Trailhead のユニット本文で確認 / f: outcome / x: 「Agentforce Service(旧 Service Cloud)は、AI、データ、CRMを組み合わせ、AIエージェントとサービス担当者が協力して対応するサービス製品群です。」
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/service-cloud-platform-quick-look/get-to-know-the-service-cloud-platform

### 14. Trailhead: Agentforce Service の基本 / Agentforce Service 入門 Q2
- 問題: Agentforce Service で、AI エージェントは主にどのようにサービスエクスペリエンスに貢献しますか?
- 正解: 定型的な問い合わせに対応し、即座に回答する。(a=[2])
- 根拠(ユニット本文・日本語版): 「定型的な問い合わせに対応し、即座に回答する。」
- v: Trailhead のユニット本文で確認 / f: outcome
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/service-cloud-platform-quick-look/get-to-know-the-service-cloud-platform

### 15. Trailhead: Agentforce Service の基本 / エージェンティックエクスペリエンスでケースをより迅速に解決する Q1
- 問題: サービスコンソールから Slack スウォームを開始する主な目的は何ですか?
- 正解: リアルタイムのケース解決に適切なエキスパートを専用チャンネルに集める。(a=[2])
- 根拠(ユニット本文・日本語版): 「担当者はいろいろなアプリケーションを切り替えて回答を探すのではなく、サービスコンソールの統合ビューから直接 Slack スウォームを開始できます。これにより、業務の流れの中で支援できる AI としての Slackbot を含む適切なエキスパートが、ケースにリンクされた専用の Slack チャンネルに集まります。」
- v: Trailhead のユニット本文で確認 / f: slack
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/service-cloud-platform-quick-look/resolve-cases-faster

### 16. Trailhead: Agentforce Service の基本 / エージェンティックエクスペリエンスでケースをより迅速に解決する Q2
- 問題: Service Assistant がサービス担当者を支援するために実行するタスクはどれですか?
- 正解: 担当者に関連データをプロアクティブに表示し、返信を作成する。(a=[1])
- 根拠(ユニット本文・日本語版): 「Service Assistant はバックグラウンドで動作し、関連データをプロアクティブに表示したり、返信を作成したり、長い会話スレッドを要約したりするため、担当者は数秒で状況を把握できます。」
- v: Trailhead のユニット本文で確認 / f: automation
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/service-cloud-platform-quick-look/resolve-cases-faster

### 17. Trailhead: Agentforce Service の基本 / インテリジェントなオムニチャネルサービスを提供する Q1
- 問題: 拡張オムニチャネルは、どのようにしてケースの割り当てを勘に頼らずに行えるようにしますか?
- 正解: 問題解決に必要なスキルに基づいて作業項目を割り当てる。(a=[2])
- 根拠(ユニット本文・日本語版): 「たとえば「請求のエキスパート」や「スペイン語が堪能」といった、顧客の問題解決に必要な正確なスキルに基づいて作業項目を自動的に割り当てることで、担当者の選定を勘に頼らずに行えます。」
- v: Trailhead のユニット本文で確認 / f: routing
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/service-cloud-platform-quick-look/deliver-omnichannel-service

### 18. Trailhead: Agentforce Service の基本 / インテリジェントなオムニチャネルサービスを提供する Q2
- 問題: スーパーバイザー向け Command Center は、サービスリーダー向けにどの AI 関連メトリクスを追跡しますか?
- 正解: 自律型 AI エージェントの解決率と効率(a=[2])
- 根拠(ユニット本文・日本語版): 「未対応の作業、顧客の待ち時間、サービス担当者のパフォーマンスを確認でき、自律型 AI エージェントの解決率や効率も追跡できます。」
- v: Trailhead のユニット本文で確認 / f: analytics
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/service-cloud-platform-quick-look/deliver-omnichannel-service

### 19. Trailhead: Agentforce Service: クイックルック / インテリジェントなサービスのために AI と担当者を統合する Q1
- 問題: Agentforce Service でのカスタマーサポートに対する統合アプローチの主な利点は何ですか?
- 正解: 担当者がすべての顧客履歴を参照できる統合コンソールが提供される。(a=[3])
- 根拠(ユニット本文・日本語版): 「Agentforce Service では統合コンソールが提供され、サービス担当者はお客様の履歴、納入商品の詳細、過去のやり取りなどのすべてを 1 つのビューで把握できます。」
- v: Trailhead のユニット本文で確認 / f: outcome
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/servicecloud-quick-look/servicecloud-quick-look-1

### 20. Trailhead: Agentforce Service: クイックルック / インテリジェントなサービスのために AI と担当者を統合する Q2
- 問題: Agentforce Service では、AI エージェントとサービス担当者の間でどのようなワークフローが意図されていますか?
- 正解: AI エージェントは定型タスクを実行し、複雑なケースをサービス担当者に引き継ぐ。(a=[2])
- 根拠(ユニット本文・日本語版): 「AI エージェントは Web、メッセージング、音声チャネルにわたって、定型的な質問を自律的に解決できます。ケースが複雑すぎる場合は、AI はシームレスにサービス担当者に引き継ぎ、担当者に会話のサマリーを提供します。」
- v: Trailhead のユニット本文で確認 / f: outcome / x: 「複雑な案件は、会話の要約を付けてサービス担当者に引き継ぎます。」
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/servicecloud-quick-look/servicecloud-quick-look-1

### 21. Trailhead: プロジェクト管理のベストプラクティス / 要件の収集 Q1
- 問題: 正誤問題: 範囲、スケジュール、コストは、いずれかの変更が他に影響するため、トリプル制約と呼ばれている。
- 正解: 正しい(a=[0])
- 根拠(ユニット本文・日本語版): 「範囲、スケジュール、コストは、しばしばトリプル制約と呼ばれます。/ 範囲の変更は、プロジェクトスケジュールとコストに影響します。」
- v: Trailhead のユニット本文で確認 / f: engage
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/best-practices-for-project-management/gather-requirements

### 22. Trailhead: プロジェクト管理のベストプラクティス / 要件の収集 Q2
- 問題: スコープクリープとは何ですか?
- 正解: 承認のない許可されていない変更によってプロジェクトが失敗する原因(a=[0])
- 根拠(ユニット本文・日本語版): 「プロジェクトでの迂回はスコープクリープにつながります。スコープクリープはプロジェクトが失敗する主な原因です。」
- v: Trailhead のユニット本文で確認 / f: engage / x: 「承認のない変更の積み重ね(スコープクリープ)は、失敗の大きな原因です。」
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/best-practices-for-project-management/gather-requirements

### 23. Trailhead: プロジェクト管理のベストプラクティス / 活動、スケジュール、コストの計画 Q1
- 問題: 作業分解構造 (WBS) とは何ですか?
- 正解: プロジェクトの範囲を視覚的に表示するツール(a=[3])
- 根拠(ユニット本文・日本語版): 「範囲は、作業分解構造 (WBS) と呼ばれる一般的なツールで取り込みます。」
- v: Trailhead のユニット本文で確認 / f: engage
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/best-practices-for-project-management/plan-the-activities-schedule-and-cost

### 24. Trailhead: プロジェクト管理のベストプラクティス / 活動、スケジュール、コストの計画 Q2
- 問題: ガントチャートとは何ですか?
- 正解: プロジェクトスケジュールの作成によく使用されるツール(a=[2])
- 根拠(ユニット本文・日本語版): 「ガントチャートは、プロジェクトスケジュールを作成するために最もよく使用されるツールです。」
- v: Trailhead のユニット本文で確認 / f: engage
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/best-practices-for-project-management/plan-the-activities-schedule-and-cost

### 25. Trailhead: プロジェクト管理のベストプラクティス / リスクの管理 Q1
- 問題: リスクレジスターでどのようなことができますか?
- 正解: A と B(a=[3])
- 根拠(ユニット本文・日本語版): 「最初のステップは、潜在的なリスクを特定することです。通常こうしたリスクはリスクレジスターに登録されます。/ 手法に関係なく、重要なのはプロジェクトスポンサー、主要なステークホルダー、分野のエキスパートがプロセスに関わり、特定のリスクの所有権を持つことです。」
- v: Trailhead のユニット本文で確認 / f: engage
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/best-practices-for-project-management/manage-risk

### 26. Trailhead: プロジェクト管理のベストプラクティス / リスクの管理 Q2
- 問題: リスク姿勢とは何ですか?
- 正解: リスクに対する全体的な態度(a=[0])
- 根拠(ユニット本文・日本語版): 「リスク態度 (認知) では、リスクテイカーからリスク回避者まで、リスクに対する全体的な態度を定義します。」
- v: Trailhead のユニット本文で確認 / f: engage
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/best-practices-for-project-management/manage-risk

### 27. Trailhead: プロジェクト管理のベストプラクティス / プロジェクトのパフォーマンスの管理 Q1
- 問題: アーンドバリュー分析とは何ですか?
- 正解: プロジェクトのコストに対して完了した作業を計算する手法(a=[0])
- 根拠(ユニット本文・日本語版): 「ざっくりと言えば、プロジェクトコストに対して特定の時点で完了した作業の計算です。」
- v: Trailhead のユニット本文で確認 / f: engage
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/best-practices-for-project-management/manage-project-performance

### 28. Trailhead: プロジェクト管理のベストプラクティス / プロジェクトのパフォーマンスの管理 Q2
- 問題: アーンドバリュー指標によって何が判断されますか?
- 正解: プロジェクトが予定どおりに予算内で進んでいるかどうか(a=[2])
- 根拠(ユニット本文・日本語版): 「プロジェクトのパフォーマンスレポートで提示されたアーンドバリュー指標から、ステークホルダーはプロジェクトが予定どおりに予算内で進んでいるかどうかを把握できます。」
- v: Trailhead のユニット本文で確認 / f: engage / x: 「進捗はアーンドバリューで測ります。コスト差異は EV − AC、スケジュール差異は EV − PV で、マイナスなら予算超過やスケジュールの遅れです。」
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/best-practices-for-project-management/manage-project-performance

### 29. Trailhead: カスタマーサービスインシデント管理の基本 / カスタマーサービスインシデント管理をはじめる Q1
- 問題: カスタマーサービスインシデント管理を使用したインシデントのフェーズは何ですか?
- 正解: インシデントを認識する、根本原因を見つける、修正するための変更要求を作成する。(a=[1])
- 根拠(ユニット本文・日本語版): 「最初に、インシデントが発生します。関連するケースが入ってくるようになり、チームはどれだけのお客様が影響を受けているかを認識します。/ 次に、問題フェーズでは、エキスパートチームが集まり、問題の根本原因を調べます。/ 最後に、チームは問題を解決するために必要なステップを説明する変更要求レコードを作成します。」
- v: Trailhead のユニット本文で確認 / f: slack
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/customer-service-incident-management-basics/get-started-with-customer-service-incident-management

### 30. Trailhead: カスタマーサービスインシデント管理の基本 / カスタマーサービスインシデント管理をはじめる Q2
- 問題: Ursa Major では、重要度 1 にランク付けされるインシデントの要因はどれですか?
- 正解: A と C(a=[4])
- 根拠(ユニット本文・日本語版): 「早急に修正しなければより大きな損害が発生する可能性があり、複数のお客様に影響を及ぼしているため、Ursa Major ではこれを緊急インシデントとみなします。」
- v: Trailhead のユニット本文で確認 / f: slack
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/customer-service-incident-management-basics/get-started-with-customer-service-incident-management

### 31. Trailhead: カスタマーサービスインシデント管理の基本 / カスタマーサービスインシデント管理を設定する Q1
- 問題: Service Cloud を持っていても、カスタマーサービスインシデント管理の追加ライセンスを購入する必要がある。
- 正解: False(a=[1])
- 根拠(ユニット本文・日本語版): 「カスタマーサービスインシデント管理は Service Cloud に含まれています。」
- v: Trailhead のユニット本文で確認 / f: slack
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/customer-service-incident-management-basics/set-up-customer-service-incident-management

### 32. Trailhead: カスタマーサービスインシデント管理の基本 / カスタマーサービスインシデント管理を設定する Q2
- 問題: Ursa Major ではカスタマーサービスインシデント管理のためにどの関連リストをケースレコードページに追加しますか?
- 正解: [Case Related Issues (ケース関連の問題)] と [Related Change Requests (関連変更要求)](a=[1])
- 根拠(ユニット本文・日本語版): 「そのため、Maria は、エージェントが使用するケースページレイアウトに [Case Related Issues (ケース関連の問題)] と [Related Change Requests (関連変更要求)] を追加する必要があります。」
- v: Trailhead のユニット本文で確認 / f: slack
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/customer-service-incident-management-basics/set-up-customer-service-incident-management

### 33. Trailhead: カスタマーサービスインシデント管理の基本 / インシデントについてのスウォームを作成する Q1
- 問題: インシデントについてスウォームを行うのはどのような場合ですか?
- 正解: エキスパートの協力が必要な場合(a=[0])
- 根拠(ユニット本文・日本語版): 「問題の根本原因はわかりませんが、回避策がないことはわかっているため、インシデントについて Slack でスウォームを開始して、この問題の解決のために社内のエキスパートの協力を得ます。」
- v: 要確認 / f: slack
- 要確認の理由: 本文の見出しは「根本原因を特定するためのスウォーム」で、選択肢 C「根本原因を見つける必要がある場合」も本文に近い。本文の文「社内のエキスパートの協力を得ます」から A とした。
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/customer-service-incident-management-basics/create-and-swarm-on-an-incident

### 34. Trailhead: カスタマーサービスインシデント管理の基本 / インシデントについてのスウォームを作成する Q2
- 問題: 問題の根本原因を特定したら、何を行いますか?
- 正解: 改善プランを含む変更要求を作成する。(a=[1])
- 根拠(ユニット本文・日本語版): 「Gertrude は問題の修正に必要な手順を保存するために変更要求を作成します。次に、問題の修正に必要な基本要件を含む改善プランを作成します。」
- v: Trailhead のユニット本文で確認 / f: slack
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/customer-service-incident-management-basics/create-and-swarm-on-an-incident

### 35. Trailhead: カスタマーサービスインシデント管理の基本 / 継続的な改善をめざす Q1
- 問題: Ursa Major はカスタマーサービスインシデント管理を拡張するためにどのように管理パッケージを使用しますか?
- 正解: A と C(a=[3])
- 根拠(ユニット本文・日本語版): 「そこで、優秀なシステム管理者の Maria に Incident Management Reports & Dashboard 管理パッケージをインストールするように依頼します。/ Maria は Ada に同じプロセスを使用してパートナーインテグレーションなどの他の管理パッケージをインストールできると言います。」
- v: Trailhead のユニット本文で確認 / f: slack
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/customer-service-incident-management-basics/aim-for-constant-improvement

### 36. Trailhead: カスタマーサービスインシデント管理の基本 / 継続的な改善をめざす Q2
- 問題: [Close Change Request & Related Issues (変更要求および関連問題をクローズ)] フローを使用すると、何がクローズされますか?
- 正解: A と B(a=[4])
- 根拠(ユニット本文・日本語版): 「Maria は変更要求と関連問題 (ケース、問題、インシデント) をクローズするためにフローを使用することを提案します。」
- v: Trailhead のユニット本文で確認 / f: slack / x: 「サンプルフローの「Change Case Owner to Incident Owner」は、インシデントに関連付けたケースの所有者をインシデントの所有者に変えます。「Close Change Request & Related Issues」は、変更要求と、関連するケース・問題・インシデントをまとめてクローズします。」
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/customer-service-incident-management-basics/aim-for-constant-improvement

### 37. Trailhead: カスタマーサービスインシデント管理: クイックルック / サービス障害に対処して、お客様の信頼を得る Q1
- 問題: インシデント管理のメリットの 1 つはどれですか?
- 正解: 解決に向けて、フィールド技術者を派遣できる。(a=[3])
- 根拠(ユニット本文・日本語版): 「Field Service を使用して作業員を派遣する。オフサイトや客先で解決する必要がある場合は、フィールドサービス作業員をスケジュールします。」
- v: Trailhead のユニット本文で確認 / f: slack
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/customer-service-incident-management-quick-look/address-disruptions-and-build-customer-trust

### 38. Trailhead: カスタマーサービスインシデント管理: クイックルック / サービス障害に対処して、お客様の信頼を得る Q2
- 問題: インシデント管理でお客様に最新情報を通知する 1 つの方法はどれですか?
- 正解: インシデントキューにあるケースに自動対応する。(a=[1])
- 根拠(ユニット本文・日本語版): 「既存のケースと受信ケースを自動的に分類してインシデントキューに転送し、影響を受けたお客様を追跡して自動対応できるようにします。」
- v: Trailhead のユニット本文で確認 / f: slack
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/customer-service-incident-management-quick-look/address-disruptions-and-build-customer-trust

### 39. Trailhead: サービス向けの Einstein 記事レコメンデーション / Einstein 記事レコメンデーションについて知る Q1
- 問題: Einstein 記事レコメンデーションのメリットの 1 つはどれですか?
- 正解: エージェントが過剰に検索することがなくなるものと思われる。(a=[1])
- 根拠(ユニット本文・日本語版): 「Einstein は何百件、あるいは何十万件もの記事を数秒のうちに検索できるため、エージェントの時間と労力を節約できます。」
- v: Trailhead のユニット本文で確認 / f: kcs
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/einstein-article-recommendations-for-service/get-to-know-einstein-article-recommendations

### 40. Trailhead: サービス向けの Einstein 記事レコメンデーション / Einstein 記事レコメンデーションについて知る Q2
- 問題: Einstein 記事レコメンデーションのどのような点によってケースサイクルが短縮される可能性がありますか?
- 正解: AI を使用して関連性の高いナレッジ記事を表示するため、エージェントが手動で検索する必要がなくなる。(a=[2])
- 根拠(ユニット本文・日本語版): 「Einstein 記事レコメンデーションは AI を使用して、お客様のケースに関連するナレッジ記事を推奨し、エージェントがお客様からの問い合わせに効率的に対応できるようにします。」
- v: Trailhead のユニット本文で確認 / f: kcs
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/einstein-article-recommendations-for-service/get-to-know-einstein-article-recommendations

### 41. Trailhead: サービス向けの Einstein 記事レコメンデーション / 記事レコメンデーションを使い始める Q1
- 問題: 推奨記事と Einstein 記事レコメンデーションの違いは何ですか?
- 正解: A と C(a=[3])
- 根拠(ユニット本文・日本語版): 「他方、Einstein 記事レコメンデーションは過去のケースのデータを使用して、数秒のうちにより正確なレコメンデーションを生成します。/ 中でも Einstein 記事レコメンデーションは、AI を使用して時間の経過とともにその機能を高めていきます。」
- v: Trailhead のユニット本文で確認 / f: kcs / x: 「Einstein Article Recommendations は過去の添付実績から推奨します。キーワードだけの Suggested Articles との違いが問われます。」
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/einstein-article-recommendations-for-service/start-using-article-recommendations

### 42. Trailhead: サービス向けの Einstein 記事レコメンデーション / 記事レコメンデーションを使い始める Q2
- 問題: 関連性スコアはエージェントにどのような形で役立ちますか?
- 正解: どの記事がお客様の問題の解決に最も役立つ可能性が高いかをエージェントが把握できる。(a=[0])
- 根拠(ユニット本文・日本語版): 「Einstein 記事レコメンデーションの関連性スコアからエージェントは、記事がお客様のケースにどのくらい関連しているかを知ることができます。」
- v: Trailhead のユニット本文で確認 / f: kcs
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/einstein-article-recommendations-for-service/start-using-article-recommendations

### 43. Trailhead: サービス向けの Einstein 記事レコメンデーション / 記事レコメンデーションを向上させる Q1
- 問題: Einstein によって推奨されたものではないナレッジ記事をケースの解決に使用する場合にエージェントがすべきことは何ですか?
- 正解: 記事をケースに添付する。(a=[0])
- 根拠(ユニット本文・日本語版): 「できる限り記事をケースに添付する。エージェントがケースに対応中に記事を参照した場合は、その記事をケースに添付することをお勧めします。」
- v: Trailhead のユニット本文で確認 / f: kcs
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/einstein-article-recommendations-for-service/improve-einsteins-recommendations

### 44. Trailhead: サービス向けの Einstein 記事レコメンデーション / 記事レコメンデーションを向上させる Q2
- 問題: Einstein 記事レコメンデーションに関する次の文のうち、正しいものはどれですか?
- 正解: Einstein は Salesforce 知識ベースにある記事のみを推奨する。(a=[1])
- 根拠(ユニット本文・日本語版): 「知識ベースを継続的に拡大する。蓄積されている記事が増えれば、Einstein が添付や学習する対象が増大します。Einstein は、公開されたその日のうちに新しい記事を推奨できます。」
- v: Trailhead のユニット本文で確認 / f: kcs
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/einstein-article-recommendations-for-service/improve-einsteins-recommendations

### 45. Trailhead: Einstein ボットの基礎 / Einstein ボットの概要 Q1
- 問題: チャットボットとは何ですか?
- 正解: 人間の会話をシミュレーションするアプリケーション(a=[2])
- 根拠(ユニット本文・日本語版): 「チャットボットとは、人間の会話を音声またはテキストメッセージでシミュレーションするアプリケーションです。」
- v: Trailhead のユニット本文で確認 / f: agents
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/service_bots_basics/learn-about-einstein-bots

### 46. Trailhead: Einstein ボットの基礎 / Einstein ボットの概要 Q2
- 問題: チャットボットの利点は次のどれですか?
- 正解: ケースデフレクション、待機時間の短縮、NLU によるインテリジェントな応答(a=[0])
- 根拠(ユニット本文・日本語版): 「迅速なケースデフレクション / NLU によるインテリジェントな応答」
- v: Trailhead のユニット本文で確認 / f: agents
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/service_bots_basics/learn-about-einstein-bots

### 47. Trailhead: Einstein ボットの基礎 / ボットコンテンツの計画 Q1
- 問題: ボットを作成する前に知っておくことが重要な用語はどれですか?
- 正解: 変数、ダイアログ、ダイアログ Intent、エンティティ(a=[4])
- 根拠(ユニット本文・日本語版): 「ダイアログ Intent は、お客様がボットとやり取りを行う理由です。/ エンティティは、お客様から収集するデータの種類です。/ 変数とは、お客様から収集した特定のデータを保存するコンテナのことです。各変数はエンティティに関連付ける必要があります。」
- v: Trailhead のユニット本文で確認 / f: agents
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/service_bots_basics/plan-your-bot-content

### 48. Trailhead: Einstein ボットの基礎 / ボットコンテンツの計画 Q2
- 問題: ボットコンテンツを計画するとき、計画の質問で焦点を当てることが重要なトピックはどれですか?
- 正解: コンテキスト、個性、会話の設計(a=[0])
- 根拠(ユニット本文・日本語版): 「ボットのコンテキストを定義する / ボットに個性を与える」
- v: Trailhead のユニット本文で確認 / f: agents
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/service_bots_basics/plan-your-bot-content

### 49. Trailhead: Einstein ボットの基礎 / Einstein ボットの前提条件と有効化 Q1
- 問題: ボットを設定するにはどのライセンスが必要ですか?
- 正解: Service Cloud(a=[3])
- 根拠(ユニット本文・日本語版): 「Ursa Major Solar が Salesforce から Service Cloud ライセンスを取得していることを確認します (Trailhead Playground には不要です)。」
- v: Trailhead のユニット本文で確認 / f: agents
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/service_bots_basics/enable-einstein-bots

### 50. Trailhead: Einstein ボットの基礎 / Einstein ボットの前提条件と有効化 Q2
- 問題: Einstein ボットを有効にするにはどうすればよいですか?
- 正解: Einstein ボットの設定ページで切り替えスイッチをクリックする。(a=[0])
- 根拠(ユニット本文・日本語版): 「Einstein ボットの横にある切り替えスイッチをクリックします。」
- v: Trailhead のユニット本文で確認 / f: agents
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/service_bots_basics/enable-einstein-bots

### 51. Trailhead: サービス向けの Einstein 分類アプリケーション / Einstein 分類アプリケーションについて知る Q1
- 問題: Einstein 分類アプリケーションは何を実行しますか?
- 正解: 過去のインテリジェンスに基づいて、エージェントやチームに項目値を推奨する AI(a=[0])
- 根拠(ユニット本文・日本語版): 「「分類」するための予測インテリジェンスが適用されます。つまり、クローズケースの値に基づいてケースの項目値が提案されます。」
- v: Trailhead のユニット本文で確認 / f: automation
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/service_case_class/learn-about-einstein-case-classification

### 52. Trailhead: サービス向けの Einstein 分類アプリケーション / Einstein 分類アプリケーションについて知る Q2
- 問題: Service Cloud の設定において、ケース分類の設定が最後のステップであるのはなぜですか?
- 正解: AI を実装する前に、情報の取得方法とケース作業の割り当て方法を決定するために明確なケース管理プロセスが必要であるため(a=[0])
- 根拠(ユニット本文・日本語版): 「Einstein は賢く、ケースの分類の助けにはなりますが、Ursa Major Solar のケースを管理するビジネスプロセスを定義することはできません。それは Maria の仕事です。そこで、まず適切な情報を取得する方法と各ケースに誰が取り組むべきかを決定し、必須項目、通知設定、割り当てルール、ルーティングを設定します。」
- v: Trailhead のユニット本文で確認 / f: automation
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/service_case_class/learn-about-einstein-case-classification

### 53. Trailhead: サービス向けの Einstein 分類アプリケーション / 分類アプリケーションのためのデータの準備 Q1
- 問題: Einstein 分類アプリケーション用のクローズケースデータはどのようにして準備しますか?
- 正解: 予測するケース項目に正確な値が入力され、各項目に 400 件以上 (多ければ多いほどよい) のサンプルがあることを確認する。(a=[1])
- 根拠(ユニット本文・日本語版): 「効率的な予測モデルの作成にはクローズケースデータの正確性が極めて重要であることから、予測する項目に正しい値が入力されていることを確認しておくことが大切です。/ 項目の値を予測する場合、Einstein はその項目に値が設定されているクローズケース を 400 件以上必要とします。」
- v: Trailhead のユニット本文で確認 / f: automation
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/service_case_class/prepare-your-data-for-case-classification

### 54. Trailhead: サービス向けの Einstein 分類アプリケーション / 分類アプリケーションのためのデータの準備 Q2
- 問題: 次のうち、モデルにバイアスがかかる可能性があるものはどれですか?
- 正解: A と C(a=[3])
- 根拠(ユニット本文・日本語版): 「データが極端に簡略化されていたり、ラベル付けや分類が間違っていたりする場合は、測定バイアスが生じます。/ データセット内のある特性、要因、集団が過多あるいは過少になることがあります。」
- v: Trailhead のユニット本文で確認 / f: automation
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/service_case_class/prepare-your-data-for-case-classification

### 55. Trailhead: サービス向けの Einstein 分類アプリケーション / Einstein 分類アプリケーションの有効化 Q1
- 問題: エージェントがケース分類のおすすめを参照できるようにする実装手順はどれですか?
- 正解: コンソールユーザーに「Einstein ケース分類ユーザー」権限セットを割り当てる。(a=[3])
- 根拠(ユニット本文・日本語版): 「エージェントが Einstein ケース分類の項目予測を表示して操作できるようにするには、「Einstein ケース分類ユーザー」権限セットを割り当てます。」
- v: Trailhead のユニット本文で確認 / f: automation
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/service_case_class/turn-on-einstein-case-classification

### 56. Trailhead: サービス向けの Einstein 分類アプリケーション / Einstein 分類アプリケーションの有効化 Q2
- 問題: 分類の信頼性レベルとは何ですか?
- 正解: 信頼性レベルは、項目値の最適なおすすめが正しいものである確率を表す。(a=[2])
- 根拠(ユニット本文・日本語版): 「予測の信頼性レベルは、項目の推奨値が正しいものである確率を表します。」
- v: Trailhead のユニット本文で確認 / f: automation
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/service_case_class/turn-on-einstein-case-classification

### 57. Trailhead: Einstein サービス返信 / サービスと生成 AI のメリットについて学ぶ Q1
- 問題: 生成 AI は、どのような方法でカスタマーサービスの対応を向上させますか?
- 正解: コンテキストに応じた応答を瞬時に提示する。(a=[0])
- 根拠(ユニット本文・日本語版): 「昨今の AI は、大規模言語モデルを使用して、テキストや画像などのコンテンツをすぐさま生成できます。サービスのワークフローに AI 機能を組み込めば、お客様は必要な回答をすぐに得ることができ、エージェントは関係構築に注力できます。」
- v: Trailhead のユニット本文で確認 / f: automation
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/einstein-service-replies/learn-the-benefits-of-service-and-generative-ai

### 58. Trailhead: Einstein サービス返信 / サービスと生成 AI のメリットについて学ぶ Q2
- 問題: サービス返信はライブチャットチャネルでしか使用できない。
- 正解: 誤り(a=[1])
- 根拠(ユニット本文・日本語版): 「メッセージングチャネルやチャットチャネルで会話中、Einstein サービス返信はエージェントの応答のドラフトを作成します。」
- v: Trailhead のユニット本文で確認 / f: automation
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/einstein-service-replies/learn-the-benefits-of-service-and-generative-ai

### 59. Trailhead: Einstein サービス返信 / Einstein サービスチャット返信を設定して使用する Q1
- 問題: サービス返信を Einstein データライブラリでグラウンディングするのはなぜですか?
- 正解: 最も関連性の高い情報に基づく返信を取得するため(a=[0])
- 根拠(ユニット本文・日本語版): 「データライブラリを使用すると、ナレッジ記事またはアップロードされたファイルから関連情報がプロンプトに追加されるため、Einstein がどのデータに基づいて回答を作成すればよいのかがわかり、最適な結果を得ることができます。」
- v: Trailhead のユニット本文で確認 / f: automation
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/einstein-service-replies/configure-and-use-service-replies-for-chat

### 60. Trailhead: Einstein サービス返信 / Einstein サービスチャット返信を設定して使用する Q2
- 問題: Einstein サービス返信を使用すると、メッセージングセッションのサービスエージェントの効率がどのように高まりますか?
- 正解: お客様のメッセージのコンテキストに基づいて事前に作成された返信を提案する。(a=[1])
- 根拠(ユニット本文・日本語版): 「お客様から詳しい情報を収集した後で、Einstein は割り当てられたデータライブラリのナレッジ記事に記載されていた設定とトラブルシューティングのプロトコルに基づいて、さらに複雑な返信を提案します。」
- v: Trailhead のユニット本文で確認 / f: automation
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/einstein-service-replies/configure-and-use-service-replies-for-chat

### 61. Trailhead: Einstein for Service のロールアウト戦略 / 人工知能を使用してサービスを向上させる Q1
- 問題: Einstein for Service はエージェントをどのような方法で支援しますか?
- 正解: Einstein は、エージェントが問題解決に要する時間を短縮できる機能の集合体である。(a=[0])
- 根拠(ユニット本文・日本語版): 「Einstein はエージェントとお客様の両方にガイダンスを提示して効率性を高め、問題解決に要する時間を短縮できます。」
- v: Trailhead のユニット本文で確認 / f: automation
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/einstein-for-service-rollout-strategies/use-artificial-intelligence-to-improve-service

### 62. Trailhead: Einstein for Service のロールアウト戦略 / 人工知能を使用してサービスを向上させる Q2
- 問題: チームが Einstein for Service を使用した場合の利点はどれですか?
- 正解: 数秒でデータベース全体から答えを見つけ出すことができる。(a=[1])
- 根拠(ユニット本文・日本語版): 「Einstein は驚異的な処理能力を備えているため、わずか数秒でデータベース全体を検索して答えを見つけ出すことができます。」
- v: Trailhead のユニット本文で確認 / f: automation
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/einstein-for-service-rollout-strategies/use-artificial-intelligence-to-improve-service

### 63. Trailhead: Einstein for Service のロールアウト戦略 / ロールアウト戦略を作成する Q1
- 問題: ロールアウト戦略の 3 つのフェーズは何ですか?
- 正解: 有効化前、有効化、有効化後。(a=[3])
- 根拠(ユニット本文・日本語版): 「そして、製品のロールアウトの推奨フェーズの概要を示します。/ 有効化前 / イネーブルメント / 有効化後」
- v: Trailhead のユニット本文で確認 / f: automation
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/einstein-for-service-rollout-strategies/create-a-rollout-strategy

### 64. Trailhead: Einstein for Service のロールアウト戦略 / ロールアウト戦略を作成する Q2
- 問題: 各自に適した Einstein for Service の機能を判断する最適な方法はどれですか?
- 正解: 最大の課題と目標を上げ、Einstein for Service の機能と照らし合わせる。(a=[0])
- 根拠(ユニット本文・日本語版): 「見つかった課題を Einstein for Service の上記のソリューションと照らし合わせ、課題の解決につながると思われる機能を検討します。」
- v: Trailhead のユニット本文で確認 / f: automation
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/einstein-for-service-rollout-strategies/create-a-rollout-strategy

### 65. Trailhead: Einstein for Service のロールアウト戦略 / Einstein に向けた準備 Q1
- 問題: Einstein for Service でデータが極めて重要なのはなぜですか?
- 正解: Einstein が学習するためには経時的なデータ収集が必要であるため。(a=[0])
- 根拠(ユニット本文・日本語版): 「Einstein は機械学習を使用しますが、機械学習の良し悪しは経時的なデータの収集に左右されます。」
- v: Trailhead のユニット本文で確認 / f: automation
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/einstein-for-service-rollout-strategies/get-ready-for-einstein-service

### 66. Trailhead: Einstein for Service のロールアウト戦略 / Einstein に向けた準備 Q2
- 問題: ロールアウト戦略を開始するときに考慮すべき点は何ですか?
- 正解: まず選定したユーザーグループに機能をテストしてもらい、フィードバックに基づいて対策を講じる。(a=[1])
- 根拠(ユニット本文・日本語版): 「最初に「スーパーユーザー」にロールアウトする。/ まず選定したユーザーグループに機能をテストしてもらい、フィードバックに基づいて対策を講じる。」
- v: Trailhead のユニット本文で確認 / f: automation
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/einstein-for-service-rollout-strategies/get-ready-for-einstein-service

### 67. Trailhead: 拡張チャットの最適化 / エンドユーザーを確認して、メッセージング履歴を共有する Q1
- 問題: 次のうち、ユーザー検証を追加することの利点でないものはどれですか?
- 正解: エンドユーザーに会話後のアンケートを送信する。(a=[2])
- 根拠(ユニット本文・日本語版): 「顧客の ID を検証するセキュアなトークンを使用して、データプライバシーを最大化します。/ 複数のデバイス間での継続的な会話を可能にします。/ Web の拡張チャットの会話履歴への顧客のアクセス権を拡張します。」
- v: Trailhead のユニット本文で確認 / f: messaging
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/messaging-optimization-for-in-app-and-web/verify-end-user-share-msg-history

### 68. Trailhead: 拡張チャットの最適化 / エンドユーザーを確認して、メッセージング履歴を共有する Q2
- 問題: ユーザー検証はバックグラウンドでどのように処理されますか?
- 正解: エンドユーザーが Web サイトやモバイルアプリケーションにログインすると、JSON Web トークンが割り当てられる。JSON Web キーにより JSON Web トークンが検証され、エンドユーザーがログアウトするまでメッセージング履歴が表示される。(a=[0])
- 根拠(ユニット本文・日本語版): 「ユーザー検証では、JSON Web キーを使用して、Web サイトやモバイルアプリケーションへのログイン時にエンドユーザーに割り当てられる JSON Web トークンが検証されます。/ ログアウトしてから再度ログインしても、履歴は保持されます。」
- v: Trailhead のユニット本文で確認 / f: messaging
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/messaging-optimization-for-in-app-and-web/verify-end-user-share-msg-history

### 69. Trailhead: 拡張チャットの最適化 / 情報を収集してエンドユーザーを迅速にサポートする Q1
- 問題: 次のうち、事前チャット項目データの転送先にできないのはどれですか?
- 正解: 音声チャネル(a=[3])
- 根拠(ユニット本文・日本語版): 「この対象は、エージェントが参照できるようにメッセージングセッションレコードにデータを保存する、または収集されたデータに基づいて顧客をサポートするためにボットを使用するといった簡単なものでかまいません。/ 事前チャットデータを使用して、サポートを行うのに最適なエージェントに作業を転送します。」
- v: Trailhead のユニット本文で確認 / f: messaging
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/messaging-optimization-for-in-app-and-web/collect-information-to-help-end-users

### 70. Trailhead: 拡張チャットの最適化 / 情報を収集してエンドユーザーを迅速にサポートする Q2
- 問題: 次のうち、オムニフローでサポートできない事前チャットデータの使用方法はどれですか?
- 正解: 事前チャットフォームをカスタマイズする。(a=[2])
- 根拠(ユニット本文・日本語版): 「事前チャットデータを使用して、オブジェクトを更新します。/ 事前チャットデータを使用して、サポートを行うのに最適なエージェントに作業を転送します。/ 事前チャットデータを使用して、やり取りを検索し、レコードにリンクします。」
- v: Trailhead のユニット本文で確認 / f: messaging
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/messaging-optimization-for-in-app-and-web/collect-information-to-help-end-users

### 71. Trailhead: 拡張チャットの最適化 / チャットボタンをいつ、どのように表示するかを決定する Q1
- 問題: Web の拡張チャットリリースに営業時間を追加すると、どうなりますか?
- 正解: 営業時間外は Web ページにチャットボタンが表示されない。(a=[1])
- 根拠(ユニット本文・日本語版): 「Web の拡張チャット: 営業時間外はチャットボタンが表示されません。」
- v: Trailhead のユニット本文で確認 / f: messaging
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/messaging-optimization-for-in-app-and-web/decide-when-and-how-to-present-the-chat-button

### 72. Trailhead: 拡張チャットの最適化 / チャットボタンをいつ、どのように表示するかを決定する Q2
- 問題: 次のうち、チャットボタンの表示/非表示 API を使用している場合にできない操作はどれですか?
- 正解: リリースに関連付けられた営業時間を上書きする。(a=[0])
- 根拠(ユニット本文・日本語版): 「表示/非表示 API を使用することで、Ursa Major は Web サイトの右下隅のチャットボタンを非表示にできます。/ 表示/非表示 API を使用すると、Ursa Major の Web 開発者は、既存の会話の継続が許可されているページのチャットボタンを非表示にできます。」
- v: 要確認 / f: messaging
- 要確認の理由: 本文には API で営業時間を上書きできるかどうかの記述がない。選択肢 D「リリースに営業時間を追加する」も API の機能ではないため、どちらを正解とするかは推定。
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/messaging-optimization-for-in-app-and-web/decide-when-and-how-to-present-the-chat-button

### 73. Trailhead: 拡張チャットの最適化 / 構造化コンテンツをエンドユーザーに送信する Q1
- 問題: 次のうち、エージェントが送信できないメッセージングコンポーネントはどれですか?
- 正解: 自動応答(a=[2])
- 根拠(ユニット本文・日本語版): 「エージェントがエンドユーザーにさまざまなメッセージングコンポーネントを無限に送信できるように思えるかもしれませんが、組織から自動的に送信できるメッセージングコンポーネントは、拡張チャット向けの自動レスポンスコンポーネントとアプリ内の拡張チャット向けの通知コンポーネントの 2 種類しかありません。」
- v: Trailhead のユニット本文で確認 / f: messaging
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/messaging-optimization-for-in-app-and-web/send-structured-content-to-end-users

### 74. Trailhead: 拡張チャットの最適化 / 構造化コンテンツをエンドユーザーに送信する Q2
- 問題: 次の文のうち、誤っているものはどれですか?
- 正解: 自動レスポンスでは、顧客は自分より先に何人の他の顧客がキューで待機しているかがわかる。(a=[3])
- 根拠(ユニット本文・日本語版): 「自動レスポンスをトリガーできるチャット会話には 4 つのポイントがあります。/ 会話を終了 / エンドユーザーにエージェントが会話を終了したことを通知します。必要に応じて、会話後のアンケートを送信します。」
- v: Trailhead のユニット本文で確認 / f: messaging
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/messaging-optimization-for-in-app-and-web/send-structured-content-to-end-users

### 75. Trailhead: 拡張チャットの最適化 / 顧客とメッセージをやり取りする Q1
- 問題: 次のうち、拡張会話ツールバーでエージェントが実行できない操作はどれですか?
- 正解: 動的メッセージングコンポーネントを送信する。(a=[3])
- 根拠(ユニット本文・日本語版): 「ここで、エージェントは下部にあるメッセージの作成に役立つツールバーと上部にあるチャットを無効化または終了するためのボタンを利用できます (2)。拡張会話コンポーネントの右側では、エージェントは、[Actions & Recommendations (アクション & おすすめ)]、[After Conversation Work (会話後作業)]、動的メッセージングコンポーネントをトリガーするフローなど、システム管理者によって使用できるように選択されたツールで作業できます (3)。」
- v: Trailhead のユニット本文で確認 / f: messaging
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/messaging-optimization-for-in-app-and-web/message-with-a-customer

### 76. Trailhead: 拡張チャットの最適化 / 顧客とメッセージをやり取りする Q2
- 問題: 拡張チャットのエージェントがエンドユーザーに応答するために使用できないツールはどれですか?
- 正解: 音声メモ(a=[2])
- 根拠(ユニット本文・日本語版): 「まずは、拡張会話コンポーネントのツールバーのデフォルトで利用可能な機能から始めましょう。/ テキストと絵文字を送信する / クイックテキストを送信する / 画像、動画、ファイルを送信する」
- v: Trailhead のユニット本文で確認 / f: messaging
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/messaging-optimization-for-in-app-and-web/message-with-a-customer

### 77. Trailhead: Lightning Experience の エンタイトルメント管理 / マイルストーンの設定 Q1
- 問題: マイルストーンとは?
- 正解: 会社のサポートプロセスに必要なステップ(a=[1])
- 根拠(ユニット本文・日本語版): 「前にも述べたとおり、マイルストーンは、サポートプロセスに必要なステップを表します。」
- v: Trailhead のユニット本文で確認 / f: entitle
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/entitlement-management-for-lightning-experience/set-up-milestones

### 78. Trailhead: Lightning Experience の エンタイトルメント管理 / マイルストーンの設定 Q2
- 問題: ケーストリガーは自動的に何を実行しますか?
- 正解: 適切なエンタイトルメントを新しいケースに追加する(a=[3])
- 根拠(ユニット本文・日本語版): 「Apex トリガーを使用しないと、エンタイトルメントは新しいケースに自動的に追加されません。/ 取引先責任者に有効なエンタイトルメントがある場合、そのエンタイトルメントがケースに追加されます。」
- v: Trailhead のユニット本文で確認 / f: entitle / x: 「Web-to-Case や Email-to-Case で作成されたケースには、エンタイトルメントが自動では付きません。自動で付ける仕組みを別に用意します。」
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/entitlement-management-for-lightning-experience/set-up-milestones

### 79. Trailhead: Lightning Experience の エンタイトルメント管理 / 顧客のケースでのエンタイトルメントの使用 Q1
- 問題: マイルストーントラッカーでは担当者に何が表示されますか?
- 正解: A と B(a=[3])
- 根拠(ユニット本文・日本語版): 「マイルストーントラッカーには次の項目が表示されるため、担当者はサポートの期限に備えることができます。/ 有効なマイルストーンが目標日に達するまでの残り時間 / 期限切れのマイルストーンが目標日を過ぎてからの経過時間 / 今後のマイルストーンのリスト」
- v: Trailhead のユニット本文で確認 / f: entitle
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/entitlement-management-for-lightning-experience/use-entitlements-in-customer-cases

### 80. Trailhead: Lightning Experience の エンタイトルメント管理 / 顧客のケースでのエンタイトルメントの使用 Q2
- 問題: システム管理者がエンタイトルメントプロセスの複数のバージョンを作成して維持するにはどうすればよいでしょうか?
- 正解: エンタイトルメントのバージョン管理を有効にする。(a=[2])
- 根拠(ユニット本文・日本語版): 「エンタイトルメントプロセスの複数のバージョンを作成して管理できるようにする場合は、エンタイトルメントのバージョン管理を有効にします。」
- v: Trailhead のユニット本文で確認 / f: entitle / x: 「エンタイトルメントプロセスを有効にしたあとは、マイルストンの削除やマイルストンアクションの作成ができません。変えるときは、エンタイトルメントのバージョン管理で新しいバージョンを作ります。」
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/entitlement-management-for-lightning-experience/use-entitlements-in-customer-cases

### 81. Trailhead: Lightning Experience の エンタイトルメント管理 / 作業指示でのエンタイトルメントの使用 Q1
- 問題: 作業指示の用途は?
- 正解: 顧客の商品に必要な作業の追跡(a=[1])
- 根拠(ユニット本文・日本語版): 「Ursa Major では作業指示を使用して、顧客が購入した商品に対して実行する必要のある作業を追跡しています。」
- v: Trailhead のユニット本文で確認 / f: entitle
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/entitlement-management-for-lightning-experience/use-entitlements-with-work-orders

### 82. Trailhead: Lightning Experience の エンタイトルメント管理 / 作業指示でのエンタイトルメントの使用 Q2
- 問題: 作業種別から作業指示が作成されると、自動的に何が実行されますか?
- 正解: 作業指示に重要な情報が記入される。(a=[0])
- 根拠(ユニット本文・日本語版): 「Ursa Major では、作業種別を使用して作業指示を作成すると、作業の予想所要時間、サービスクルーに必要なスキル、作業の完了に必要な商品など、いくつかの重要な情報が自動的に入力されます。」
- v: Trailhead のユニット本文で確認 / f: entitle
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/entitlement-management-for-lightning-experience/use-entitlements-with-work-orders

### 83. Trailhead: Improved Service with Agentforce Commerce and Agentforce Service Integration / Increase Service Excellence with Agentforce Commerce Q1
- 問題: Order Management System(OMS)は、サービスコンソールでサービス担当者に何を提供できますか?
- 正解: 注文した商品、注文日、支払方法などの注文の内容(a=[0])
- 根拠(ユニット本文・英語版): 「Contents of the order, such as the products ordered, the order date, cost of the order, and the payment method used」
- v: Trailhead のユニット本文で確認 / f: integ
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/improved-service-commerce-and-service-cloud/increase-service-excellence-with-commerce-cloud

### 84. Trailhead: Improved Service with Agentforce Commerce and Agentforce Service Integration / Increase Service Excellence with Agentforce Commerce Q2
- 問題: Agentforce Service と Agentforce Commerce を統合すると、顧客にはどのようなメリットがありますか?
- 正解: より速く正確な注文の追跡、簡単な返品、すべての接点での一貫したサポート(a=[1])
- 根拠(ユニット本文・英語版): 「From within their Service Console, a service rep can efficiently process returns and replacements and view loyalty and warranty information. / Now they can process service requests more quickly, providing better post-purchase customer experiences and building customer loyalty.」
- v: Trailhead のユニット本文で確認 / f: integ
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/improved-service-commerce-and-service-cloud/increase-service-excellence-with-commerce-cloud

### 85. Trailhead: Improved Service with Agentforce Commerce and Agentforce Service Integration / Improve Service with AI Agents Q1
- 問題: AI エージェントは、顧客とのやり取りにどう応答するかをどのように決めますか?
- 正解: アクションと指示を含む、あらかじめ定義されたトピックを参照する。(a=[1])
- 根拠(ユニット本文・英語版): 「After it determines what a customer wants, it selects predefined topics that tell it how to handle the customer interaction. The topics contain actions the agent can perform and instructions which tell the agent how to make decisions.」
- v: Trailhead のユニット本文で確認 / f: agents
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/improved-service-commerce-and-service-cloud/improve-returns-with-ai-agents

### 86. Trailhead: Improved Service with Agentforce Commerce and Agentforce Service Integration / Improve Service with AI Agents Q2
- 問題: Ursa Major のリコールの対象外の商品を顧客が返品しようとすると、どうなりますか?
- 正解: エージェントはリコールの対象外であることを伝え、通常の返品として処理する。(a=[0])
- 根拠(ユニット本文・英語版): 「If it’s not covered by the recall, the AI agent informs the customer accordingly and starts the standard return topic.(本文中のインタラクティブ解説より)」
- v: Trailhead のユニット本文で確認 / f: agents
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/improved-service-commerce-and-service-cloud/improve-returns-with-ai-agents

### 87. Trailhead: AI 向けのナレッジグラウンディング: クイックルック / 大規模言語モデル向けにナレッジコンテンツを最適化する Q1
- 問題: 生成 AI のグラウンディングについての最も適切な説明はどれですか?
- 正解: AI モデルを信頼できる情報源につなぐこと(a=[3])
- 根拠(ユニット本文・日本語版): 「グラウンディングとは、AI モデルを信頼できる情報ソースに結び付けて、AI 機能の精度と関連性を高めることを意味します。」
- v: Trailhead のユニット本文で確認 / f: kcs
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/knowledge-grounding-for-ai-quick-look/optimize-knowledge-content-for-large-language-models

### 88. Trailhead: AI 向けのナレッジグラウンディング: クイックルック / 大規模言語モデル向けにナレッジコンテンツを最適化する Q2
- 問題: 正誤問題: ナレッジセンターサービス (KCS) はナレッジ管理に関する業界標準のベストプラクティス集である。
- 正解: 正しい(a=[0])
- 根拠(ユニット本文・日本語版): 「ナレッジセンターサービス (KCS) プリンシプルは、ナレッジ管理に関する業界標準のベストプラクティス集です。」
- v: Trailhead のユニット本文で確認 / f: kcs
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/knowledge-grounding-for-ai-quick-look/optimize-knowledge-content-for-large-language-models

### 89. Trailhead: ナレッジ検索の基本 / Salesforce ナレッジの検索 Q1
- 問題: Salesforce ナレッジの検索の最適化が必要な理由は?
- 正解: 上記のすべて(a=[3])
- 根拠(ユニット本文・日本語版): 「時間とお金の両方を節約するには、検索を最適化します。/ サービス担当は時間を大幅に節約し、顧客に関連性の高い記事をより迅速に提供できるようになります。検索にいくつかの簡単な変更を行うだけで」
- v: Trailhead のユニット本文で確認 / f: kcs
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/knowledge_search_basics/knowledge_search_basics_search

### 90. Trailhead: ナレッジ検索の基本 / Salesforce ナレッジの検索 Q2
- 問題: 検索の関連性はどのように判断されますか?
- 正解: 検索語の頻度、順序、ユニーク性などの要素の数(a=[1])
- 根拠(ユニット本文・日本語版): 「検索語の頻度、順序、ユニーク性を少々」
- v: Trailhead のユニット本文で確認 / f: kcs
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/knowledge_search_basics/knowledge_search_basics_search

### 91. Trailhead: ナレッジ検索の基本 / Salesforce ナレッジの検索 Q3
- 問題: 見出語化の利点とは?
- 正解: 記事で使用される検索語の正確なバリエーションを使用しなくても多数の結果が返される。(a=[2])
- 根拠(ユニット本文・日本語版): 「見出語化は、検索語のバリエーションを識別して返します。/ 見出語化では、ユーザーの言い回しが完全に正確でない場合でも結果を得ることができます。」
- v: Trailhead のユニット本文で確認 / f: kcs
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/knowledge_search_basics/knowledge_search_basics_search

### 92. Trailhead: ナレッジ検索の基本 / 最適な検索オプションの選択 Q1
- 問題: スニペット、強調表示、オートコンプリートはどこで有効にできますか?
- 正解: ナレッジの設定(a=[2])
- 根拠(ユニット本文・日本語版): 「スニペットと強調表示を有効にするには、[ナレッジの設定] で [検索結果内で関連する記事のテキストを強調表示] をオンにします。/ タイトル検索とキーワード検索両方のオートコンプリートを有効にするには、[ナレッジの設定] で [タイトル検索をオートコンプリート] と [キーワード検索をオートコンプリート] をオンにします。」
- v: Trailhead のユニット本文で確認 / f: kcs
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/knowledge_search_basics/knowledge_search_basics_choose

### 93. Trailhead: ナレッジ検索の基本 / 最適な検索オプションの選択 Q2
- 問題: 検索のスニペットが生成される方法は?
- 正解: メール、ロングテキストエリア、リッチテキストエリア、テキストエリア項目から(a=[1])
- 根拠(ユニット本文・日本語版): 「検索の強調表示とスニペットは、メール、ロングテキストエリア、リッチテキストエリア、テキストエリア項目から生成されます。」
- v: Trailhead のユニット本文で確認 / f: kcs
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/knowledge_search_basics/knowledge_search_basics_choose

### 94. Trailhead: ナレッジ検索の基本 / 最適な検索オプションの選択 Q3
- 問題: オートコンプリートにはどのような種類がありますか?
- 正解: 上記のすべて(a=[3])
- 根拠(ユニット本文・日本語版): 「ナレッジ検索のオートコンプリートには、記事や質問のタイトル用とキーワード検索用の 2 つのフレーバーがあります。」
- v: Trailhead のユニット本文で確認 / f: kcs
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/knowledge_search_basics/knowledge_search_basics_choose

### 95. Trailhead: ナレッジ検索の基本 / 検索のカスタマイズの設定 Q1
- 問題: 昇格済み検索語を作成するときに必要な処理は?
- 正解: 上記のすべて(a=[3])
- 根拠(ユニット本文・日本語版): 「一般的なサポートの問題に対応する記事の場合、その記事に昇格済み用語と呼ばれるキーワードを関連付けることができます。/ 最良の結果を得るには、昇格済み用語を選択的に使用します。つまり、昇格済み用語および用語あたりの昇格済み記事の数を制限して作成します。」
- v: 要確認 / f: kcs
- 要確認の理由: 本文は「昇格済み用語および用語あたりの昇格済み記事の数を制限」と書き、選択肢の「用語あたりのキーワード数を制限」とは表現が異なる。選択肢の作りから「上記のすべて」とした。
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/knowledge_search_basics/knowledge_search_basics_setup

### 96. Trailhead: ナレッジ検索の基本 / 検索のカスタマイズの設定 Q2
- 問題: [設定] のどこでシノニムグループを作成できますか?
- 正解: シノニム(a=[2])
- 根拠(ユニット本文・日本語版): 「[設定] から、[クイック検索] ボックスに「シノニム」と入力します。[カスタマイズ] | [検索] で [シノニム] を選択します。」
- v: Trailhead のユニット本文で確認 / f: kcs
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/knowledge_search_basics/knowledge_search_basics_setup

### 97. Trailhead: ナレッジ検索の基本 / 検索のカスタマイズの設定 Q3
- 問題: 関連記事の推奨機能をカスタマイズするために選択できるケース項目は?
- 正解: 使用可能な短いテキスト項目を 5 個まで選択できる。(a=[0])
- 根拠(ユニット本文・日本語版): 「使用可能な短いテキスト項目を 5 個まで選択できます。」
- v: Trailhead のユニット本文で確認 / f: kcs
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/knowledge_search_basics/knowledge_search_basics_setup

### 98. Trailhead: ナレッジ検索の基本 / 分析を使用したより適切な判断 Q1
- 問題: [設定] のどこでナレッジ検索活動レポートの作成を開始しますか?
- 正解: レポートタイプ(a=[0])
- 根拠(ユニット本文・日本語版): 「[設定] から、[クイック検索] ボックスに「レポートタイプ」と入力し、[作成] で [レポートタイプ] を選択します。」
- v: Trailhead のユニット本文で確認 / f: reports
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/knowledge_search_basics/knowledge_search_basics_make

### 99. Trailhead: ナレッジ検索の基本 / 分析を使用したより適切な判断 Q2
- 問題: より適切なシノニムグループと昇格済み検索語を作成するには、ナレッジ検索活動レポートのどの項目を使用しますか?
- 正解: 検索語(a=[1])
- 根拠(ユニット本文・日本語版): 「作成したレポートを見てみましょう。[検索語] 項目があります。上位 20 件 (または 100 件) の語に焦点を絞ります。同じことを指しているためまとめることができる語はあるでしょうか?」
- v: Trailhead のユニット本文で確認 / f: kcs
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/knowledge_search_basics/knowledge_search_basics_make

### 100. Trailhead: ナレッジ検索の基本 / 分析を使用したより適切な判断 Q3
- 問題: ナレッジ検索活動レポートをどのように使用して記事を改善できますか?
- 正解: [平均クリック順位] 項目と [クリックされた記事タイトル] 項目を使用して、アクセス数が上位の記事と下位の記事を判断し、その記事に集中的に取り組む。(a=[3])
- 根拠(ユニット本文・日本語版): 「ここでは検索語から離れて、レポートのもう 1 つの列 [平均クリック順位] を見てみましょう。/ [クリックされた記事タイトル] 項目は、上位 10 件と下位 10 件の記事を確認するために使用できます。」
- v: Trailhead のユニット本文で確認 / f: kcs
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/knowledge_search_basics/knowledge_search_basics_make

### 101. Trailhead: Agentforce Service のナレッジセンターサービス / ナレッジセンターサービスの使用開始 Q1
- 問題: KCS® 手法を使用することで、どのようなメリットがありますか?
- 正解: A と B(a=[4])
- 根拠(ユニット本文・日本語版): 「KCS 手法を採用している企業は、その多大なメリットを実感しています。時間とともにカスタマーエクスペリエンスが向上して、従業員の離職率が低下し、新規従業員を対象とするトレーニング時間が減少します。」
- v: Trailhead のユニット本文で確認 / f: kcs
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/knowledgecentered-service-in-lightning-knowledge/get-started-with-knowledgecentered-service

### 102. Trailhead: Agentforce Service のナレッジセンターサービス / ナレッジセンターサービスの使用開始 Q2
- 問題: エージェントが記事を改善したいと思った場合、何をすべきですか?
- 正解: フラグを設定するか、修正する。(a=[0])
- 根拠(ユニット本文・日本語版): 「記事が存在するものの、改善を要する場合は、エージェントが修正するか、フラグを設定します。」
- v: Trailhead のユニット本文で確認 / f: kcs
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/knowledgecentered-service-in-lightning-knowledge/get-started-with-knowledgecentered-service

### 103. Trailhead: Agentforce Service のナレッジセンターサービス / 記事の状況の管理 Q1
- 問題: 記事の状況は何によって決まりますか?
- 正解: B と C(a=[4])
- 根拠(ユニット本文・日本語版): 「記事に対するチームの確信度はどのくらいか? / 誰が記事を参照できるか?」
- v: Trailhead のユニット本文で確認 / f: kcs
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/knowledgecentered-service-in-lightning-knowledge/manage-article-states

### 104. Trailhead: Agentforce Service のナレッジセンターサービス / 記事の状況の管理 Q2
- 問題: 通常、地域の法律に関する記事に適用されるのはどの種のガバナンスですか?
- 正解: コンプライアンスベース(a=[0])
- 根拠(ユニット本文・日本語版): 「コンプライアンスベースの記事の多くは、ポリシー、法律、規制に関するトピックを説明するものです。」
- v: Trailhead のユニット本文で確認 / f: kcs
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/knowledgecentered-service-in-lightning-knowledge/manage-article-states

### 105. Trailhead: Agentforce Service のナレッジセンターサービス / KCS ユーザー向けの Lightning Knowledge の設定 Q1
- 問題: KCS 候補者が記事に設定できるのはどの検証状況ですか?
- 正解: 作業進行中(a=[0])
- 根拠(ユニット本文・日本語版): 「記事を「作業進行中」または「未検証」として保存することもできます。」
- v: Trailhead のユニット本文で確認 / f: kcs
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/knowledgecentered-service-in-lightning-knowledge/set-up-lightning-knowledge-for-kcs-users

### 106. Trailhead: Agentforce Service のナレッジセンターサービス / KCS ユーザー向けの Lightning Knowledge の設定 Q2
- 問題: KCS のロールをサポートするために使用できるものはどれですか?
- 正解: A または B(a=[3])
- 根拠(ユニット本文・日本語版): 「KCS の新しいロールと責務を導入するために、Maria は当初、Ada のリストの KCS ロールごとにプロファイルを作成することを検討しました。/ そこで、全エージェントに使用するユーザーレコードに 2 つのカスタム項目を作成することにします。」
- v: Trailhead のユニット本文で確認 / f: kcs
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/knowledgecentered-service-in-lightning-knowledge/set-up-lightning-knowledge-for-kcs-users

### 107. Trailhead: Agentforce Service のナレッジセンターサービス / 記事検索と品質監査の最適化 Q1
- 問題: エージェントが記事を見つけやすくするにはどうすればよいですか?
- 正解: A と B(a=[4])
- 根拠(ユニット本文・日本語版): 「Maria が検索とデータカテゴリを最適化して、エージェントがケースに適した記事を見つけられるようにしています。さらに、推奨記事を有効にしたため、エージェントが検索自体を行う必要性が大幅に減少しました。」
- v: Trailhead のユニット本文で確認 / f: kcs
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/knowledgecentered-service-in-lightning-knowledge/optimize-article-search-and-quality-audits

### 108. Trailhead: Agentforce Service のナレッジセンターサービス / 記事検索と品質監査の最適化 Q2
- 問題: KCS コーチが行うことはどれですか?
- 正解: 記事の品質を監視する。(a=[0])
- 根拠(ユニット本文・日本語版): 「記事の品質と、エージェントが新しいプロセスをどの程度使用しているかを監視するうえで鍵となるのが、月 1 回の品質監査です。」
- v: Trailhead のユニット本文で確認 / f: kcs
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/knowledgecentered-service-in-lightning-knowledge/optimize-article-search-and-quality-audits

### 109. Trailhead: Agentforce Service のナレッジセンターサービス / 進化ループを使用したプロセスの改良 Q1
- 問題: 検索ギャップとは何ですか?
- 正解: 検索時に必要な記事が見つからないこと(a=[0])
- 根拠(ユニット本文・日本語版): 「ただし、見つからないことがあります。/ Ada は、こうした検索ギャップを調べ、検索されにくい記事を検出されやすくする方法を検討するつもりです。」
- v: Trailhead のユニット本文で確認 / f: kcs
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/knowledgecentered-service-in-lightning-knowledge/use-evolve-loop-to-improve-your-process

### 110. Trailhead: Agentforce Service のナレッジセンターサービス / 進化ループを使用したプロセスの改良 Q2
- 問題: 記事をケースに添付する必要がある状況はどれですか?
- 正解: 記事がケースの解決に役立つ場合(a=[2])
- 根拠(ユニット本文・日本語版): 「ケースの中には記事がなくても解決できるものもありますが、記事がある場合にはエージェントに利用してもらいたいと Ada は考えています。」
- v: Trailhead のユニット本文で確認 / f: kcs
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/knowledgecentered-service-in-lightning-knowledge/use-evolve-loop-to-improve-your-process

### 111. Trailhead: Lightning Knowledge への移行 / Lightning Knowledge の機能の活用 Q1
- 問題: Ursa Major が Lightning Knowledge へのアップグレードを希望する理由は何ですか?
- 正解: B と C(a=[4])
- 根拠(ユニット本文・日本語版): 「ドラッグしてファイルを添付する。/ スマートフォン、タブレット、デスクトップなどのすべてのデバイスからナレッジにアクセスし、レコードタイプを使用してデバイスごとに異なるレイアウトを指定する。」
- v: Trailhead のユニット本文で確認 / f: knowledge / x: 「Lightning Knowledge では、従来の記事タイプの代わりにレコードタイプで記事の種類(FAQ、手順書、ポリシーなど)を分けます。レコードタイプが記事の内容とレイアウトを決めます。」
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/lightning-knowledge-migration/harness-the-power-of-lightning-knowledge

### 112. Trailhead: Lightning Knowledge への移行 / Lightning Knowledge の機能の活用 Q2
- 問題: Lightning Knowledge にアップグレードすると、サービスチームにとってどのような利点がありますか?
- 正解: A と B(a=[3])
- 根拠(ユニット本文・日本語版): 「さまざまな検索条件でリストビューを作成することによって記事を管理する (記事が誰に割り当てられているかの表示など)。/ たとえば、改善された検索、グローバル検索、そして 6 つ以上のファイルを記事に添付できることなどです。」
- v: Trailhead のユニット本文で確認 / f: knowledge
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/lightning-knowledge-migration/harness-the-power-of-lightning-knowledge

### 113. Trailhead: Lightning Knowledge への移行 / 移行の計画 Q1
- 問題: 移行後に変更される項目はどれですか?
- 正解: 記事番号(a=[2])
- 根拠(ユニット本文・日本語版): 「ハードコードされたアプリケーションの標準自動採番データ型に関する制限により、記事番号が変更されます。」
- v: Trailhead のユニット本文で確認 / f: knowledge
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/lightning-knowledge-migration/plan-the-migration

### 114. Trailhead: Lightning Knowledge への移行 / 移行の計画 Q2
- 問題: 移行後、記事へのアクセスはどのようにして制御しますか?
- 正解: B と C(a=[4])
- 根拠(ユニット本文・日本語版): 「システム管理者は、ユーザープロファイルと権限セットを設定して記事へのアクセス権を制御します。」
- v: Trailhead のユニット本文で確認 / f: knowledge
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/lightning-knowledge-migration/plan-the-migration

### 115. Trailhead: Lightning Knowledge への移行 / Sandbox へのテスト移行の実行 Q1
- 問題: データ移行の概要で、黄色のフラグは何を意味しますか?
- 正解: その項目が 100% 移行されなかった。(a=[2])
- 根拠(ユニット本文・日本語版): 「問題がある場合は、黄色の警告フラグが表示されます。」
- v: Trailhead のユニット本文で確認 / f: knowledge
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/lightning-knowledge-migration/perform-a-test-migration-to-a-sandbox

### 116. Trailhead: Lightning Knowledge への移行 / Sandbox へのテスト移行の実行 Q2
- 問題: 移行を受け入れる前に更新する必要があるカスタマイズはどれですか?
- 正解: 古い記事タイプに基づいて作成されたカスタマイズ(a=[0])
- 根拠(ユニット本文・日本語版): 「まず、記事タイプを参照するすべてのカスタマイズを更新する必要があります。」
- v: Trailhead のユニット本文で確認 / f: knowledge
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/lightning-knowledge-migration/perform-a-test-migration-to-a-sandbox

### 117. Trailhead: Lightning Knowledge への移行 / Lightning Knowledge の設定 Q1
- 問題: 移行後に変更が必要なのはどれですか?
- 正解: B と C(a=[4])
- 根拠(ユニット本文・日本語版): 「連動選択リストと数式は移行されないので、チェックリストに含まれるそれらを修正します。」
- v: Trailhead のユニット本文で確認 / f: knowledge
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/lightning-knowledge-migration/set-up-lightning-knowledge

### 118. Trailhead: Lightning Knowledge への移行 / Lightning Knowledge の設定 Q2
- 問題: Lightning Knowledge では、どのようにして権限が決定されますか?
- 正解: ユーザープロファイル(a=[1])
- 根拠(ユニット本文・日本語版): 「Salesforce Classic のナレッジでは、権限は記事アクションを使用して決定されていました。移行後、権限はユーザープロファイルと権限セットを使用して決定されます。」
- v: Trailhead のユニット本文で確認 / f: knowledge
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/lightning-knowledge-migration/set-up-lightning-knowledge

### 119. Trailhead: Lightning Knowledge への移行 / 本番への移行 Q1
- 問題: Salesforce サポートは、Maria の本番組織での移行の準備が整っていることをどのような方法で判断しますか?
- 正解: 一連の質問をする。(a=[0])
- 根拠(ユニット本文・日本語版): 「サポートチームは、準備が整っていることを確認するために、Maria に一連の質問をします。」
- v: Trailhead のユニット本文で確認 / f: knowledge
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/lightning-knowledge-migration/migrate-into-production

### 120. Trailhead: Lightning Knowledge への移行 / 本番への移行 Q2
- 問題: Maria はどのような方法で本番組織を移行しますか?
- 正解: 移行前作業を実行し、移行し、移行後作業を実行する。(a=[1])
- 根拠(ユニット本文・日本語版): 「Maria は、Sandbox 組織で実行したのと同じ手順を本番組織ですべて実行します。」
- v: Trailhead のユニット本文で確認 / f: knowledge
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/lightning-knowledge-migration/migrate-into-production

### 121. Trailhead: パートナーコンタクトセンター / パートナーコンタクトセンターについて学ぶ Q1
- 問題: パートナーコンタクトセンターとは
- 正解: テレフォニー、デジタルで行った会話、CRM などの機能を 1 か所で提供する Salesforce の通話オプション。(a=[2])
- 根拠(ユニット本文・日本語版): 「テレフォニー、顧客データ、デジタルチャネルを統合してすべてを 1 つのプラットフォーム、つまり Agentforce Service プラットフォームに表示できる。」
- v: Trailhead のユニット本文で確認 / f: messaging
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/service-cloud-voice/service-voice-learn

### 122. Trailhead: パートナーコンタクトセンター / パートナーコンタクトセンターについて学ぶ Q2
- 問題: Service Cloud パートナーコンタクトセンターの主な利点はどれですか?
- 正解: リアルタイムのトランスクリプト、強化されたデータ収集、AI、可視化(a=[1])
- 根拠(ユニット本文・日本語版): 「複数の通話トランスクリプトを他のデジタルチャネルと並列してリアルタイムに表示できる。/ 電話での会話をケースと取引先責任者に結びつけることで、データの収集と可視性を改善できる。」
- v: Trailhead のユニット本文で確認 / f: messaging
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/service-cloud-voice/service-voice-learn

### 123. Trailhead: パートナーコンタクトセンター / パートナーコンタクトセンターの導入を計画する Q1
- 問題: パートナーコンタクトセンターを使用するために新しいトレーニングを作成する必要がある理由はどれですか?
- 正解: コンソールのオムニチャネルモジュールを使用して電話を受けたりかけたりする方法をサービス担当者とマネージャーが理解できるようにするため(a=[3])
- 根拠(ユニット本文・日本語版): 「はい、コンソールフッターにある Salesforce コールセンターのソフトフォンから電話を受ける場合と異なり、オムニチャネルウィジェットではより簡単に電話を受けることができます。また、スーパーバイザーと担当者を対象として、オムニスーパーバイザーでのコーチングの使用方法と受講方法をトレーニングする必要があります。」
- v: Trailhead のユニット本文で確認 / f: messaging
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/service-cloud-voice/service-voice-prepare

### 124. Trailhead: パートナーコンタクトセンター / パートナーコンタクトセンターの導入を計画する Q2
- 問題: Voice をサービスチームにロールアウトする前に行う必要があるものはどれですか?
- 正解: ブランド言語をチームに再確認させる(a=[1])
- 根拠(ユニット本文・日本語版): 「Maria は、サービス担当者が Voice の使用に移行する際に、会社のブランドを適切に反映したお客様への対応方法を理解していることを確認する必要があります。/ Ursa Major Solar のブランドを反映した語調についてチームに再度周知する。」
- v: Trailhead のユニット本文で確認 / f: messaging
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/service-cloud-voice/service-voice-prepare

### 125. Trailhead: パートナーコンタクトセンター / パートナーコンタクトセンターの導入を計画する Q3
- 問題: パートナーコンタクトセンターには、どのようなテレフォニーパートナーシップオプションがありますか?
- 正解: Amazon Connect またはそのほかのコンタクトセンターパートナー(a=[1])
- 根拠(ユニット本文・日本語版): 「Maria は、Amazon Connect を使用するパートナーコンタクトセンターを実装できます。または、将来的に別のテレフォニープロバイダーを使用することもできます。Voice を実装しても、Ursa Major Solar が特定の Salesforce パートナーシップに縛られることはありません。」
- v: Trailhead のユニット本文で確認 / f: messaging
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/service-cloud-voice/service-voice-prepare

### 126. Trailhead: パートナーコンタクトセンターの設定: クイックルック / パートナーコンタクトセンターの導入準備 Q1
- 問題: Voice の実装を準備するには、どのタスクを完了させる必要がありますか?
- 正解: Voice の概念と制限事項を確認する。(a=[2])
- 根拠(ユニット本文・日本語版): 「Voice の制約と制限事項を確認する。」
- v: Trailhead のユニット本文で確認 / f: messaging
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/service-cloud-voice-setup-quick-look/prepare-for-a-voice-implementation

### 127. Trailhead: パートナーコンタクトセンターの設定: クイックルック / パートナーコンタクトセンターの導入準備 Q2
- 問題: Voice を設定する際に重要な手順はどれですか?
- 正解: ポーティング要求をできるだけ稼動開始日に先立って行う。(a=[1])
- 根拠(ユニット本文・日本語版): 「ポーティング要求をできるだけ稼動開始日に先立って行う。」
- v: Trailhead のユニット本文で確認 / f: messaging
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/service-cloud-voice-setup-quick-look/prepare-for-a-voice-implementation

### 128. Trailhead: Salesforce のアジャイルの基礎 / Salesforce がアジャイルを採用した理由の理解 Q1
- 問題: Salesforce がアジャイルプロセスを採用した理由は何ですか?
- 正解: 自社の成長を支える適切なプロセスが必要であったため(a=[2])
- 根拠(ユニット本文・日本語版): 「Salesforce では、コミュニケーションの問題や成長に伴う痛みの拡大を解決する方法を模索していたため、アジャイルはうってつけの手法でした。」
- v: Trailhead のユニット本文で確認 / f: engage
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/salesforce-agile-basics/understand-why-salesforce-adopted-agile

### 129. Trailhead: Salesforce のアジャイルの基礎 / Salesforce がアジャイルを採用した理由の理解 Q2
- 問題: アジャイルアプローチの主なメリットは何ですか?
- 正解: チームが現在の知識に基づいて継続的に適応することができる。(a=[3])
- 根拠(ユニット本文・日本語版): 「新しい業務の進め方を習得したチームは、プロセスを反復させ、ワークフローや製品に関する新しい情報を学び取りながら進行させることが可能になりました。」
- v: Trailhead のユニット本文で確認 / f: engage
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/salesforce-agile-basics/understand-why-salesforce-adopted-agile

### 130. Trailhead: Salesforce のアジャイルの基礎 / Salesforce がアジャイルを採用した理由の理解 Q3
- 問題: Salesforce でスクラムはどのように定義されていますか?
- 正解: チームが各自の成果物やプロセスを所有できる適応型のフレームワーク(a=[1])
- 根拠(ユニット本文・日本語版): 「スクラムは、製品の何が機能して何が機能しないかを判断し、それに応じて変更を行う、柔軟なフレームワークを提供します。スクラムを使用すると、取り組んでいる業務について全員が所有権を有し、期待を共有するようになります。」
- v: Trailhead のユニット本文で確認 / f: engage
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/salesforce-agile-basics/understand-why-salesforce-adopted-agile

### 131. Trailhead: Salesforce のアジャイルの基礎 / Salesforce がアジャイルを採用した理由の理解 Q4
- 問題: 「完了の定義」とは何を意味しますか?
- 正解: 「完了の定義」とは、予定していたことをすべて終了したため、今後予想外のことが起こらないことを保証するものである。(a=[1])
- 根拠(ユニット本文・日本語版): 「Salesforce の完了の定義は、業務が本当に完了したとみなされるために、チームが実行すべき事項を定めた一連のガイドラインです。」
- v: Trailhead のユニット本文で確認 / f: engage
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/salesforce-agile-basics/understand-why-salesforce-adopted-agile

### 132. Trailhead: Salesforce のアジャイルの基礎 / Salesforce がアジャイルを採用した理由の理解 Q5
- 問題: アジャイルプロセスを選択する 1 つの理由は何ですか?
- 正解: チームのプロジェクトに不明の要素が多々あり、途中で判明した内容に適応させる必要がある。(a=[1])
- 根拠(ユニット本文・日本語版): 「どちらのプロセスを選ぶかは、作業項目の開始時点で判明している事項、あるいは判明していない事項に左右されます。/ 何かを試して、どのように機能するかを確認し、新たに学んだ内容を踏まえて方向を転じられるようにしたい。」
- v: Trailhead のユニット本文で確認 / f: engage
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/salesforce-agile-basics/understand-why-salesforce-adopted-agile

### 133. Trailhead: Salesforce のアジャイルの基礎 / アジャイルの基本の学習 Q1
- 問題: アジャイル宣言の最も大切な部分の 1 つであるのはどれですか?
- 正解: 動くソフトウェア(a=[0])
- 根拠(ユニット本文・日本語版): 「包括的なドキュメントよりも動くソフトウェアを、」
- v: Trailhead のユニット本文で確認 / f: engage / x: 「アジャイルソフトウェア開発宣言は、包括的な文書よりも動くソフトウェアに、計画に従うことよりも変化への対応に価値を置きます。」
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/salesforce-agile-basics/learn-the-basics-of-agile

### 134. Trailhead: Salesforce のアジャイルの基礎 / アジャイルの基本の学習 Q2
- 問題: アジャイルの原則および手法について正しい文はどれですか?
- 正解: アジャイルの手法は、人々がフレームワークをアジャイルかつリーンな方法で設定するために役立つ。(a=[1])
- 根拠(ユニット本文・日本語版): 「サンデーのカラフルなトッピングと同様に、人々がフレームワークをアジャイルかつリーンな方法で設定できるようにする、アジャイルの手法、リーンの手法、そして技術的な手法は多数あります。」
- v: Trailhead のユニット本文で確認 / f: engage
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/salesforce-agile-basics/learn-the-basics-of-agile

### 135. Trailhead: Salesforce のアジャイルの基礎 / アジャイルの基本の学習 Q3
- 問題: どのような場合に、チームが本物のアジャイルであることがわかりますか?
- 正解: チームが製品やプロセスを改善および進化させている場合(a=[0])
- 根拠(ユニット本文・日本語版): 「プロセスや製品を進化させるために、継続的に学習して向上しているか?」
- v: Trailhead のユニット本文で確認 / f: engage
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/salesforce-agile-basics/learn-the-basics-of-agile

### 136. Trailhead: Salesforce のアジャイルの基礎 / リーンの原則の実践方法 Q1
- 問題: 品質を組み込むにはどうすればよいですか?
- 正解: 全員が品質に対して責任を担うようにする。(a=[1])
- 根拠(ユニット本文・日本語版): 「けれども現在は、品質に対する責任を誰か 1 人が担うのではなく、全員が品質に対する所有権を有します。」
- v: Trailhead のユニット本文で確認 / f: engage
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/salesforce-agile-basics/learn-to-use-lean-principles

### 137. Trailhead: Salesforce のアジャイルの基礎 / リーンの原則の実践方法 Q2
- 問題: 無駄を省くことの例はどれですか?
- 正解: 業務の開始にあたってチームが必要な事項を揃えられるように、チームの準備の定義を作成する。(a=[4])
- 根拠(ユニット本文・日本語版): 「私たちは、時間を無駄にすることがないように、準備の定義という標準を定めています。」
- v: Trailhead のユニット本文で確認 / f: engage
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/salesforce-agile-basics/learn-to-use-lean-principles

### 138. Trailhead: Salesforce のアジャイルの基礎 / リーンの原則の実践方法 Q3
- 問題: リーンの原則で、Ohana 文化を反映するものはどれですか?
- 正解: 人々を尊重する(a=[2])
- 根拠(ユニット本文・日本語版): 「チームの成功が実現するのは、お互いを尊重し、協力して取り組むときです。/ Salesforce の顧客や組織の成功にとって、Ohana 文化は不可欠であると私たちは考えています。」
- v: Trailhead のユニット本文で確認 / f: engage
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/salesforce-agile-basics/learn-to-use-lean-principles

### 139. Trailhead: Salesforce のアジャイルの基礎 / リーンの原則の実践方法 Q4
- 問題: Salesforce でリーンの原則がアジャイルプロセスにどのように影響するかを表すものはどれですか?
- 正解: 品質管理エンジニアとエンジニアの役割を融合させて、全員が品質を重視するようにした。(a=[1])
- 根拠(ユニット本文・日本語版): 「私たちが実践したことの 1 つは、技術製品組織内の品質管理エンジニアという職務を排除し、「ハイブリッドエンジニア」という職務を新設したことです。」
- v: Trailhead のユニット本文で確認 / f: engage
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/salesforce-agile-basics/learn-to-use-lean-principles

### 140. Trailhead: サービスの Salesforce フロー / サービスの Salesforce フローについて Q1
- 問題: サービスの Salesforce フローはどのような形でサービス担当者の役に立ちますか?
- 正解: C と D(a=[4])
- 根拠(ユニット本文・日本語版): 「担当者がステップをクリックするとフローやクイックアクションが起動し、何と言い、何をすべきかを確認できます。/ 担当者が一時停止中のフローを見つけて再開しやすくなる。」
- v: Trailhead のユニット本文で確認 / f: automation
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/service_lightning_flow_for_service/learn-about-lightning-flow-for-service

### 141. Trailhead: サービスの Salesforce フロー / サービスの Salesforce フローについて Q2
- 問題: 次のシナリオのうち、銀行におけるサービスの Salesforce フローの適切な使用事例はどれですか?
- 正解: お客様が融資の申し込みをしたときに、サービス担当者が信用実績チェックを実行し、申請書に記入して処理する。(a=[1])
- 根拠(ユニット本文・日本語版): 「担当者がページを開いたときに、アクション & おすすめコンポーネントにステップのリストが表示されます。ステップをクリックすると、フローなど厄介な作業をしてくれるアクションが起動します。担当者はこのリストに従って作業を進めます。」
- v: Trailhead のユニット本文で確認 / f: automation
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/service_lightning_flow_for_service/learn-about-lightning-flow-for-service

### 142. Trailhead: サービスの Salesforce フロー / Salesforce フローと RecordAction について Q1
- 問題: RecordAction とは何ですか?
- 正解: RecordAction により、フローまたはクイックアクションがレコードに関連付けられる。(a=[1])
- 根拠(ユニット本文・日本語版): 「技術的な説明のように聞こえますが、RecordAction とは単に、フローやクイックアクションなど、レコードに関連付けられているアクションのことです。」
- v: Trailhead のユニット本文で確認 / f: automation
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/service_lightning_flow_for_service/tools-lightning-flow-for-service

### 143. Trailhead: サービスの Salesforce フロー / Salesforce フローと RecordAction について Q2
- 問題: プロセスの自動化ツールを使用して、サービスの Salesforce フローを設定するにはどうすればよいですか?
- 正解: Flow Builder を使用してフローを作成し、アクション & おすすめリリースまたはプロセス内でそのフローを指定する。(a=[3])
- 根拠(ユニット本文・日本語版): 「RecordAction を作成する前に、レコードに関連付けるフローやクイックアクションを作成します。/ RecordAction には (API 以外に) 2 つの作成方法があります。アクション & おすすめリリースで設定する方法と、Flow Builder で RecordAction を使用したフロープロセスを作成する方法です。」
- v: Trailhead のユニット本文で確認 / f: automation
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/service_lightning_flow_for_service/tools-lightning-flow-for-service

### 144. Trailhead: Salesforce Knowledge の基本 / Knowledge 入門 Q1
- 問題: 知識ベースとは何ですか?
- 正解: 組織の役立つ情報を保存するための 1 つのリポジトリ(a=[0])
- 根拠(ユニット本文・日本語版): 「知識ベースでは、組織の知識がリポジトリに格納されます。」
- v: Trailhead のユニット本文で確認 / f: knowledge
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/lightning-knowledge-basics/get-started-with-lightning-knowledge

### 145. Trailhead: Salesforce Knowledge の基本 / Knowledge 入門 Q2
- 問題: 知識ベースで生産性を向上する方法はどれですか?
- 正解: 重要な情報を 1 か所で取得して統合する。(a=[3])
- 根拠(ユニット本文・日本語版): 「次に同じ質問をされたときに、他の担当者でも、知識ベースで記事を検索して用意された回答を提供できます。」
- v: Trailhead のユニット本文で確認 / f: knowledge
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/lightning-knowledge-basics/get-started-with-lightning-knowledge

### 146. Trailhead: Salesforce Knowledge の基本 / Salesforce 知識ベースを準備する Q1
- 問題: 担当者がケースを解決するときに最適な記事が提案されるようにするには、どうしたらよいですか?
- 正解: ケースとレコードタイプのわかりやすいデータカテゴリを作成する。(a=[1])
- 根拠(ユニット本文・日本語版): 「データカテゴリグループやデータカテゴリを定義するときには、分類がユーザーに明確であるようにします。」
- v: 要確認 / f: knowledge
- 要確認の理由: 本文はデータカテゴリをわかりやすく定義するベストプラクティスの説明で、「最適な記事が提案される」こととの関係は直接書かれていない。ほかの選択肢が明らかに誤りなので選んだ。
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/lightning-knowledge-basics/prepare-the-kb-for-success

### 147. Trailhead: Salesforce Knowledge の基本 / Salesforce 知識ベースを準備する Q2
- 問題: 記事の寄稿者に必要なナレッジ権限は何ですか?
- 正解: 「記事の管理」権限とナレッジに対する「参照」、「作成」、「編集」、および「公開」権限。(a=[2])
- 根拠(ユニット本文・日本語版): 「寄稿者 / 専門分野のエキスパートなどの高度な Knowledge ユーザーは商品に関する豊富な知識を持ち、記事の標準を理解しています。 / 記事を作成、編集、公開します。 / 「記事の管理」権限とナレッジに対する「参照」、「作成」、「編集」、および「公開」権限」
- v: Trailhead のユニット本文で確認 / f: knowledge
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/lightning-knowledge-basics/prepare-the-kb-for-success

### 148. Trailhead: Salesforce Knowledge の基本 / 簡単な知識ベースの設定 Q1
- 問題: Salesforce Go を使用して Knowledge の何を設定できますか?
- 正解: 記事のカテゴリ(a=[1])
- 根拠(ユニット本文・日本語版): 「Salesforce Go では、自動的にナレッジを有効化し、記事の著者にライセンスを割り当て、最初のデータグループとカテゴリを設定できます。」
- v: Trailhead のユニット本文で確認 / f: knowledge
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/lightning-knowledge-basics/set-up-a-simple-knowledge-base

### 149. Trailhead: Salesforce Knowledge の基本 / 簡単な知識ベースの設定 Q2
- 問題: 記事の概要はどこに表示されますか?
- 正解: 検索結果(a=[3])
- 根拠(ユニット本文・日本語版): 「概要は検索結果に表示されます。」
- v: Trailhead のユニット本文で確認 / f: knowledge
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/lightning-knowledge-basics/set-up-a-simple-knowledge-base

### 150. Trailhead: Salesforce メッセージング / メッセージングについて学ぶ Q1
- 問題: 正誤問題: メッセージングを使用するメリットの 1 つは、お客様とサービス担当の両方の柔軟性や調整が向上することである。
- 正解: 正しい(a=[0])
- 根拠(ユニット本文・日本語版): 「セルフサービスのオプションにより、お客様がサービスエクスペリエンスを柔軟に調整できる。/ サービス担当が自動化によって空いた時間を複雑なサービスの問題に費やすことができる。」
- v: Trailhead のユニット本文で確認 / f: messaging
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/salesforce-messaging/learn-about-messaging

### 151. Trailhead: Salesforce メッセージング / メッセージングについて学ぶ Q2
- 問題: メッセージングチャネルとは何ですか?
- 正解: お客様からの連絡手段。(a=[1])
- 根拠(ユニット本文・日本語版): 「お客様からの連絡手段。Facebook Messenger、WhatsApp、SMS テキスト、LINE、拡張チャットはすべて、お客様に連絡するためにすでに使用している可能性があるメッセージングチャネルの例です。」
- v: Trailhead のユニット本文で確認 / f: messaging / x: 「対話チャネルは、お客様とリアルタイムまたは非同期で会話する手段です。Messaging(Enhanced Chat、WhatsApp、SMS など)と音声があり、チャネルごとの特性と制約に合わせて選びます。」
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/salesforce-messaging/learn-about-messaging

### 152. Trailhead: Salesforce メッセージング / チャネルを使用してお客様にエンゲージする Q1
- 問題: Web サイトやモバイルアプリケーションにメッセージを追加する目的で設定するのはどの種別のチャネルですか?
- 正解: 拡張チャット(a=[3])
- 根拠(ユニット本文・日本語版): 「Service Cloud メッセージングのチャネルは次のとおりです。」
- v: 要確認 / f: messaging
- 要確認の理由: 本文のチャネル一覧は表形式で、拡張チャットの説明文(Web サイトやモバイルアプリへの追加)を抽出テキストから確認できなかった。一般的な製品知識から判断。
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/salesforce-messaging/engage-customers-using-channels

### 153. Trailhead: Salesforce メッセージング / チャネルを使用してお客様にエンゲージする Q2
- 問題: メッセージングセッションの転送方法を選定するのはどのツールですか?
- 正解: オムニチャネル(a=[3])
- 根拠(ユニット本文・日本語版): 「メッセージングチャネルのルーティングを設定する。/ オムニチャネルは、お客様のメッセージをキュー、フロー、適任のサービス担当に転送します。」
- v: Trailhead のユニット本文で確認 / f: routing
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/salesforce-messaging/engage-customers-using-channels

### 154. Trailhead: Salesforce メッセージング / 基本的なメッセージング実装を拡張する Q1
- 問題: 時間セレクターコンポーネントはどのような用途に最適ですか?
- 正解: 予定やサービス依頼をスケジュールする場合(a=[3])
- 根拠(ユニット本文・日本語版): 「予定をスケジュールする。」
- v: Trailhead のユニット本文で確認 / f: messaging
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/salesforce-messaging/enhance-a-basic-messaging-implementation

### 155. Trailhead: Salesforce メッセージング / 基本的なメッセージング実装を拡張する Q2
- 問題: 正誤問題: オムニチャネルフローは、一度に 1 つのメッセージングチャネルにのみ関連付けることができる。
- 正解: 誤り(a=[1])
- 根拠(ユニット本文・日本語版): 「Flow Builder でフローを作成して、1 つ以上のメッセージングチャネルに割り当てることができます。」
- v: Trailhead のユニット本文で確認 / f: routing
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/salesforce-messaging/enhance-a-basic-messaging-implementation

### 156. Trailhead: Salesforce リリース準備状況戦略 / Salesforce のリリースプロセスを理解する Q1
- 問題: Salesforce リリースはいつ行われますか?
- 正解: Spring、Summer、Winter(a=[1])
- 根拠(ユニット本文・日本語版): 「Salesforce では、多数の革新的な機能を、年に 3 回 Spring、Summer、Winter の季節ごとのリリースで提供しています。」
- v: Trailhead のユニット本文で確認 / f: deploy / x: 「Salesforce のリリースは年3回(Spring、Summer、Winter)で、自動で適用されます。」
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/sf_releases/sf_releases_start

### 157. Trailhead: Salesforce リリース準備状況戦略 / Salesforce のリリースプロセスを理解する Q2
- 問題: エディション情報、重要な注記、新機能を有効化する手順を含め、新機能の詳細を学ぶためのベストプラクティスとは?
- 正解: リリースノート(a=[0])
- 根拠(ユニット本文・日本語版): 「絶対になくてはならないリソースは、リリースノートです。リリースノートは、ほぼすべての Salesforce 製品のリリースに含まれている機能に関する詳細が記載された正式な信頼できる情報源です。(同じモジュールの単元「新機能の検索、有効化、コミュニケーション」より)」
- v: Trailhead のユニット本文で確認 / f: deploy
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/sf_releases/sf_releases_start

### 158. Trailhead: Salesforce リリース準備状況戦略 / Sandbox プレビューで早期アクセスを利用する Q1
- 問題: プレビュー Sandbox でリリースにアクセスするには、どうしたらよいですか?
- 正解: Sandbox プレビュー期日の前に、Sandbox がプレビューインスタンスにあることを確認する。(a=[1])
- 根拠(ユニット本文・日本語版): 「プレビューインスタンスにある Sandbox には早期アップグレードが適用されます。/ ただし、Sandbox プレビュー期間中 (通常は本番リリースの 4 ～ 6 週間前) に更新された Sandbox は、非プレビューインスタンスに移動します。」
- v: Trailhead のユニット本文で確認 / f: deploy / x: 「Sandbox は本番の4〜6週間前にアップグレードされます(Sandbox プレビュー)。プレビュー用の Sandbox を少なくとも1つ残し、締切日のあとは更新しないでおきます。」
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/sf_releases/sf-releases-sandbox-preview

### 159. Trailhead: Salesforce リリース準備状況戦略 / Sandbox プレビューで早期アクセスを利用する Q2
- 問題: プレビュー Sandbox を使用する利点は何ですか?
- 正解: B と C(a=[3])
- 根拠(ユニット本文・日本語版): 「使用する機能を有効にする方法を学ぶ。/ リリース前に機能の有効化と設定の練習をし、ユーザーへのロールアウトを準備する。」
- v: Trailhead のユニット本文で確認 / f: deploy
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/sf_releases/sf-releases-sandbox-preview

### 160. Trailhead: Salesforce リリース準備状況戦略 / 新機能の検索、有効化、コミュニケーション Q1
- 問題: 組織に利益をもたらす、すべての新機能をすばやく特定する方法はどれですか?
- 正解: [Feature Impact (機能の影響)] 条件を使用して、[Enabled for Users (ユーザーで有効)] 機能と [Admins must Enable (システム管理者による有効化が必要)] 機能を見つける。(a=[1])
- 根拠(ユニット本文・日本語版): 「リリースノートを読む際には、[機能の影響] 条件を使用すれば、次の 2 種類の機能をすばやく見つけることができます。/ 自動有効機能を特定するには、[機能の影響] 条件を使用して [ユーザーで有効] を選択します。/ 簡易有効機能を特定するには、[機能の影響] 条件を使用して、[システム管理者による有効化が必要] を選択します。」
- v: Trailhead のユニット本文で確認 / f: deploy
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/sf_releases/sf_releases_strategy

### 161. Trailhead: Salesforce リリース準備状況戦略 / 新機能の検索、有効化、コミュニケーション Q2
- 問題: 関係者やユーザーに新しいリリースについて伝えるときのベストプラクティスはどれですか?
- 正解: A と B(a=[4])
- 根拠(ユニット本文・日本語版): 「すべてのリリース準備状況リソースを詳しく学ぶ時間がない場合は、リリースノートを確認し、ユーザーが喜ぶ「自動有効」や「簡易有効」機能を発見できます。/ ユーザーにどのように新機能について知らせるつもりなのかをスーパーユーザーに伝え、フィードバックを求めます。」
- v: 要確認 / f: deploy
- 要確認の理由: 本文で「リリースノートの確認」は伝える前の準備として書かれており、伝え方のベストプラクティスに含めるかは選択肢の作りからの推定(B と C は C が明らかに誤り)。
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/sf_releases/sf_releases_strategy

### 162. Trailhead: システム管理者向けの Salesforce アンケート / ケースの開始時や終了時にアンケートへの招待を送信する Q1
- 問題: ケースがクローズされたときに送信するアンケートは、どのページで選択しますか?
- 正解: サポート設定(a=[2])
- 根拠(ユニット本文・日本語版): 「[サポート設定] ページで、Maria はケースのクローズ時に送信するアンケートを選択します。」
- v: Trailhead のユニット本文で確認 / f: cx / x: 「ケースのクローズ時のアンケートはサポート設定、作成時は自動レスポンスルールです。どちらもデフォルトの Experience Cloud サイトが必要です。」
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/salesforce-surveys-for-admins/surveys-case-scenario

### 163. Trailhead: システム管理者向けの Salesforce アンケート / ケースの開始時や終了時にアンケートへの招待を送信する Q2
- 問題: ケースに関連付けられているアンケートへの招待のお客様のフィードバックはどこで確認できますか?
- 正解: ケースレコードの [関連] タブにある [アンケートへの招待と回答] 関連リスト(a=[1])
- 根拠(ユニット本文・日本語版): 「ケースに関連付けられているアンケートへの招待のお客様のフィードバックは、[アンケートの招待と回答] 関連リストのケースレコードにある [関連] タブで確認できます。」
- v: Trailhead のユニット本文で確認 / f: cx
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/salesforce-surveys-for-admins/surveys-case-scenario

### 164. Trailhead: Salesforce でのスクラムと Kanban / スクラムについて Q1
- 問題: Salesforce でのスクラムの主要な属性の 1 つは何ですか?
- 正解: お客様への提供を整理するためのフレームワークである。(a=[0])
- 根拠(ユニット本文・日本語版): 「顧客に高品質な価値を提供するフレームワークです。」
- v: Trailhead のユニット本文で確認 / f: engage
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/scrum-and-kanban-at-salesforce/learn-about-scrum

### 165. Trailhead: Salesforce でのスクラムと Kanban / スクラムについて Q2
- 問題: 5 つのスクラム価値とは何ですか?
- 正解: 集中、勇気、率直さ、コミットメント、尊重(a=[3])
- 根拠(ユニット本文・日本語版): 「スクラムには 5 つの基本的価値があります。/ 1. 重点的に取り組む / 2. 勇気 / 3. 率直さ」
- v: Trailhead のユニット本文で確認 / f: engage
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/scrum-and-kanban-at-salesforce/learn-about-scrum

### 166. Trailhead: Salesforce でのスクラムと Kanban / スクラムについて Q3
- 問題: 主なスクラムチームの役割にはどのような特性がありますか?
- 正解: チームは作業を実行し、スクラムリーダーはプロセスの促進をサポートし、製品所有者はチームの方向性を定義する。(a=[2])
- 根拠(ユニット本文・日本語版): 「製品所有者はプロセスの内容と理由に責任を持ちます。/ そのために、製品のバックログに優先順位を付け、価値が最も高い作業を伝えます。」
- v: Trailhead のユニット本文で確認 / f: engage
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/scrum-and-kanban-at-salesforce/learn-about-scrum

### 167. Trailhead: Salesforce でのスクラムと Kanban / スクラムワークフローの要素 Q1
- 問題: 次のうち、スクラムの成果の要素について正しいのはどれですか?
- 正解: 製品バックログは、行う必要があると思われるすべてのことが含まれたリストである。(a=[0])
- 根拠(ユニット本文・日本語版): 「これは、必要となる可能性のある作業の順序付きリストです。」
- v: Trailhead のユニット本文で確認 / f: engage
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/scrum-and-kanban-at-salesforce/learn-the-elements-of-the-scrum-workflow

### 168. Trailhead: Salesforce でのスクラムと Kanban / スクラムワークフローの要素 Q2
- 問題: スプリントの作業を完了することが重要なのはなぜですか?
- 正解: Salesforce では無駄を排除することを重視していて、完了していない作業は、お客様に価値を提供するのに役立たない無駄の 1 つの形態であるため。(a=[0])
- 根拠(ユニット本文・日本語版): 「スクラムの世界では、作業が進行中のプロジェクトは無駄の 1 つの形態にすぎません。」
- v: Trailhead のユニット本文で確認 / f: engage
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/scrum-and-kanban-at-salesforce/learn-the-elements-of-the-scrum-workflow

### 169. Trailhead: Salesforce でのスクラムと Kanban / スクラムワークフローの要素 Q3
- 問題: 製品バックログとスプリントバックログの違いは何ですか?
- 正解: 製品バックログは必要になる可能性のあるすべてのことで、スプリントバックログは次の 2 週間でチームが責任を持つ作業である。(a=[3])
- 根拠(ユニット本文・日本語版): 「各スプリントの直前に、チームは製品バックログを参照し、優先順位の高い作業項目のうち、2 週間で取り組めるものはどれかを評価します。そして、それらのプロジェクトをスプリントバックログに入れます。」
- v: Trailhead のユニット本文で確認 / f: engage
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/scrum-and-kanban-at-salesforce/learn-the-elements-of-the-scrum-workflow

### 170. Trailhead: Salesforce でのスクラムと Kanban / スクラムの実装 Q1
- 問題: Salesforce で行われているスクラムミーティングの 2 つの主な種類は何ですか?
- 正解: 検査および適応ミーティングと計画ミーティング(a=[2])
- 根拠(ユニット本文・日本語版): 「Salesforce のスクラムミーティングには主に 2 種類のものがあります。/ 検査および適応ミーティング: チームが新しく学んだ内容を取り入れて、それらを次のスプリントに適用することがいかに重要かは詳しく説明しました。」
- v: Trailhead のユニット本文で確認 / f: engage
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/scrum-and-kanban-at-salesforce/implement-scrum

### 171. Trailhead: Salesforce でのスクラムと Kanban / スクラムの実装 Q2
- 問題: 計画で重要なのはどのミーティングですか?
- 正解: リリース計画、スプリント計画、バックログ調整、デイリースタンドアップ(a=[1])
- 根拠(ユニット本文・日本語版): 「2 週間ごとのバックログ調整計画 / 2 週間ごとのスプリント計画 / (ほぼ) 毎日のデイリー スタンドアップ」
- v: Trailhead のユニット本文で確認 / f: engage
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/scrum-and-kanban-at-salesforce/implement-scrum

### 172. Trailhead: Salesforce でのスクラムと Kanban / スクラムの実装 Q3
- 問題: 振り返りとデモ/レビューの主な違いは何ですか?
- 正解: 前者はチームの作業を検査し、後者は製品やサービスを検査して適応させる。(a=[3])
- 根拠(ユニット本文・日本語版): 「スプリントごとに、チームは作業がどれだけうまくいったか、またはいかなかったかを分析するための時間を取ります。このレビュー期間には、プロセスとチームの 2 つに重点を置きます。/ 成果物を検査し、学んだ内容をプロセスに適応させて、前進します。」
- v: Trailhead のユニット本文で確認 / f: engage
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/scrum-and-kanban-at-salesforce/implement-scrum

### 173. Trailhead: Salesforce でのスクラムと Kanban / Kanban について Q1
- 問題: Kanban チームが迅速に成果を出す要因は何ですか?
- 正解: フローの視覚化、ビジュアルインジケーターを使用した進行中の作業の制限、フローの管理、漸進的な変更への適応。(a=[1])
- 根拠(ユニット本文・日本語版): 「業務のフローをスムーズにする Kanban の 4 つの主要な特性は次のとおりです。/ ワークフローの視覚化: 作業は小さく分割され、それぞれがカードに記述されて壁 (物理的または仮想的) に貼られます。/ 進行中の作業 (WIP) の制限: チームは、各ワークフローフェーズで同時に進行中になる作業項目の数を制限します。」
- v: Trailhead のユニット本文で確認 / f: engage
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/scrum-and-kanban-at-salesforce/learn-about-kanban

### 174. Trailhead: Salesforce でのスクラムと Kanban / Kanban について Q2
- 問題: Kanban は計画されていない作業や変更にどのように対応しますか?
- 正解: 新しい要望に優先度を割り当て、それが準備完了列の最上部になったときに作業を開始する。(a=[2])
- 根拠(ユニット本文・日本語版): 「チームは、1 つの作業項目を完了すると、次に優先度が高い作業に取り組みます。」
- v: Trailhead のユニット本文で確認 / f: engage
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/scrum-and-kanban-at-salesforce/learn-about-kanban

### 175. Trailhead: Salesforce でのスクラムと Kanban / Kanban について Q3
- 問題: Kanban チームは、次のどのプラクティスを使用して進捗状況を追跡し、予測可能性を高めますか?
- 正解: サイクルタイム、リードタイム、小さいバッチサイズ、スループット(a=[3])
- 根拠(ユニット本文・日本語版): 「Kanban チームは、業務項目の小さいバッチを連続して処理します。Kanban ではいくつかの測定システムを使用します。/ スループットは、1 つの期間に完了した作業量として定義されます。/ Kanban メトリクスでは、平均リード時間を使用して結果を判断します。」
- v: Trailhead のユニット本文で確認 / f: engage
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/scrum-and-kanban-at-salesforce/learn-about-kanban

### 176. Trailhead: Salesforce でのスクラムと Kanban / 最適なワークフローの選択 Q1
- 問題: どのような場合にチームは作業の管理に Kanban を選択しますか?
- 正解: チームの作業が予測しにくい場合。(a=[1])
- 根拠(ユニット本文・日本語版): 「頻繁に指示を変更し、計画の中断を最小限に抑え、緊急の作業をすばやく開始する必要がある場合は、Kanban を使用します。」
- v: Trailhead のユニット本文で確認 / f: engage
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/scrum-and-kanban-at-salesforce/choose-the-best-workflow

### 177. Trailhead: Salesforce でのスクラムと Kanban / 最適なワークフローの選択 Q2
- 問題: 割り込み駆動型の作業とは何ですか?
- 正解: 事前に予測することは難しいが、発生した場合にはチームが対応する必要がある作業。(a=[2])
- 根拠(ユニット本文・日本語版): 「事前に通知されない新しい作業項目に対応する必要があるチームには、Kanban の方が適しています。これを割り込み駆動型の作業と呼んでいます。」
- v: Trailhead のユニット本文で確認 / f: engage
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/scrum-and-kanban-at-salesforce/choose-the-best-workflow

### 178. Trailhead: Salesforce でのスクラムと Kanban / 最適なワークフローの選択 Q3
- 問題: 一部のチームがスクラムプロセスと Kanban プロセスを組み合わせているのはなぜですか?
- 正解: チームがスクラムの構造と Kanban の WIP 制限を好むため。(a=[3])
- 根拠(ユニット本文・日本語版): 「チームは定期的な間隔で計画とレビューを行うスクラムの構造を好むことがよくあります。これによって、進行状況を管理しやすくなります。また、Kanban の進行中の作業の制限を使用して、Kanban による中断を最小限に抑えて緊急の作業に対応しています。」
- v: Trailhead のユニット本文で確認 / f: engage
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/scrum-and-kanban-at-salesforce/choose-the-best-workflow

### 179. Trailhead: Service 設定アシスタント: クイックルック / コンタクトセンターを設定する Q1
- 問題: Service 設定アシスタントの主なメリットの 1 つはどれですか?
- 正解: ユーザーが簡単な 2 ～ 3 の手順で Service Cloud を設定できる。(a=[2])
- 根拠(ユニット本文・日本語版): 「簡単な 2 ～ 3 の手順で Service Cloud をすぐに活用する。」
- v: Trailhead のユニット本文で確認 / f: deploy
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/service-setup-assistant-quick-look/set-up-your-contact-center-instantly

### 180. Trailhead: Service 設定アシスタント: クイックルック / コンタクトセンターを設定する Q2
- 問題: Service 設定アシスタントをチームに役立てる 1 つの方法はどれですか?
- 正解: 担当者向けのベストプラクティスや実証済みのワークフローを自動的に追加する。(a=[0])
- 根拠(ユニット本文・日本語版): 「チームは数回のクリック操作で、Service Cloud の便利な機能や Salesforce に組み込まれたベストプラクティスをすぐさま利用できます。」
- v: Trailhead のユニット本文で確認 / f: deploy
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/service-setup-assistant-quick-look/set-up-your-contact-center-instantly

### 181. Trailhead: Slack スウォーミング / スウォーミングでカスタマーサービスを変革する Q1
- 問題: 複雑なケースに関して、スウォーミングモデルが階層型モデルと異なる点は何ですか?
- 正解: 1 人のエージェントがずっとお客様と関与する。(a=[0])
- 根拠(ユニット本文・日本語版): 「チケットを指揮系統に沿ってエスカレーションするのではなく、ケース所有者が所有権を維持したまま、エキスパートのスウォームを招集して問題を解決し、助け合います。」
- v: Trailhead のユニット本文で確認 / f: slack
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/swarming-with-slack-basics/swarming-for-customer-success

### 182. Trailhead: Slack スウォーミング / スウォーミングでカスタマーサービスを変革する Q2
- 問題: Agentforce Service でのスウォーミングの利点は何ですか?
- 正解: ケースがより早く解決され、お客様の労力が少ない。(a=[1])
- 根拠(ユニット本文・日本語版): 「スウォーミングは、エキスパートをケースに集め、トラブルシューティングを加速します。/ 解決: 解決後、Agentforce はスウォームの会話を自動的に要約し、ケースを更新し、必要なナレッジ記事のドラフトを作成します。」
- v: Trailhead のユニット本文で確認 / f: slack
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/swarming-with-slack-basics/swarming-for-customer-success

### 183. Trailhead: Slack スウォーミング / Slack スウォームを管理する Q1
- 問題: スウォームにエキスパートを追加するにはどうすればよいですか?
- 正解: エキスパートファインダーを使用する。(a=[0])
- 根拠(ユニット本文・日本語版): 「適切なエキスパートがスウォームに追加されるようにエキスパートファインダーを設定する。」
- v: Trailhead のユニット本文で確認 / f: slack
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/swarming-with-slack-basics/manage-a-swarm

### 184. Trailhead: Slack スウォーミング / Slack スウォームを管理する Q2
- 問題: スウォームはどこで再オープンできますか?
- 正解: ケースレコードまたはスウォーム Slack チャンネルから(a=[0])
- 根拠(ユニット本文・日本語版): 「必要に応じて、Ada はいつでも Slack チャンネルまたはケースレコードからスウォームを再オープンできます。」
- v: Trailhead のユニット本文で確認 / f: slack
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/swarming-with-slack-basics/manage-a-swarm

### 185. Trailhead: サービス向け Slack / サービス向け Slack を知る Q1
- 問題: Slack はサービスチームがケースクローズまでの時間を短縮するためにどのように役立ちますか?
- 正解: B と C(a=[4])
- 根拠(ユニット本文・日本語版): 「Slack 内でサービスチームメンバーが重要な情報を見つけたり適切な人とつながったりするために専用の整理されたチャンネルを作成できます。/ Slack では協力者がサービスチャンネルに必要に応じて出入りできるため、適切なタイミングで参加できます。」
- v: Trailhead のユニット本文で確認 / f: slack
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/slack-first-service/discover-slack-first-service

### 186. Trailhead: サービス向け Slack / サービス向け Slack を知る Q2
- 問題: 効果的なカスタマーサービススウォームの主要なステップは何ですか?
- 正解: ケースを作成し、新しいスウォームチャンネルを作成し、メンバーを追加し、問題を解決し、スウォームチャンネルをアーカイブする。(a=[0])
- 根拠(ユニット本文・日本語版): 「一般的なスウォームは次のようなしくみになっています。/ Slack でスウォームチャンネルが作成される / スウォームチームメンバーがチャンネルに追加される / 目標を達成してサポートケースがクローズされ、顧客への連絡が行われ、Slack のスウォームチャンネルがアーカイブされる」
- v: Trailhead のユニット本文で確認 / f: slack
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/slack-first-service/discover-slack-first-service

### 187. Trailhead: サービス向け Slack / Slack ファーストな考え方をサービスチームに取り入れる計画を作成する Q1
- 問題: サービスチャンネルの命名規則のベストプラクティスはどれですか?
- 正解: 一貫したプレフィックスを使用することでチャンネルを論理的にグループ化する。(a=[1])
- 根拠(ユニット本文・日本語版): 「さらに一貫性のあるプレフィックス (カスタマーエクスペリエンスを表す #cx など) を付けることで、チャンネルが論理的な流れで自然にグループ化されます。」
- v: Trailhead のユニット本文で確認 / f: slack
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/slack-first-service/create-a-plan-to-bring-slack-first-thinking-to-your-service-team

### 188. Trailhead: サービス向け Slack / Slack ファーストな考え方をサービスチームに取り入れる計画を作成する Q2
- 問題: サービスでの Slack ワークフローの使用事例として適切なものはどれですか?
- 正解: A と B(a=[3])
- 根拠(ユニット本文・日本語版): 「たとえば、カスタマーサービス担当は Slack を使用して Salesforce ケースと特別な知識を持っているボランティアを表示したり、オープンになっている期間が長すぎるケースについてのメッセージを受け取ったり、重大度が高いケースが作成されたときに通知を受け取ったりします。」
- v: Trailhead のユニット本文で確認 / f: slack
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/slack-first-service/create-a-plan-to-bring-slack-first-thinking-to-your-service-team

### 189. Trailhead: Agentforce Service 向け WhatsApp / WhatsApp を使ってみる Q1
- 問題: サービス担当者がメッセージングセッション中にスーパーバイザーに質問するために使用可能なツールはどれですか?
- 正解: フラグ有効化と示唆(a=[3])
- 根拠(ユニット本文・日本語版): 「また、メッセージングセッション中に、フラグの有効化機能やスーパーバイザーの示唆機能を使用して、相手に気付かれることなくスーパーバイザーの指示を仰ぐことができる。」
- v: Trailhead のユニット本文で確認 / f: messaging
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/whatsapp-for-service-cloud/get-started-with-whatsapp

### 190. Trailhead: Agentforce Service 向け WhatsApp / WhatsApp を使ってみる Q2
- 問題: 正誤問題: メッセージを拡張ボットに転送できるようにしたい場合は、オムニチャネルフローを使用する必要がある。
- 正解: 正しい(a=[0])
- 根拠(ユニット本文・日本語版): 「オムニチャネルフローは、拡張ボットへのルーティングなど複雑なルーティングロジックをサポートし、便利なテンプレートも用意されています。」
- v: Trailhead のユニット本文で確認 / f: routing
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/whatsapp-for-service-cloud/get-started-with-whatsapp

### 191. Trailhead: Agentforce Service 向け WhatsApp / WhatsApp チャネルを細かく調整する Q1
- 問題: 正誤問題: オプトイン/オプトアウトのカスタムキーワードを複数の言語で設定できる。
- 正解: 正しい(a=[0])
- 根拠(ユニット本文・日本語版): 「Ursa Major Solar にはスペイン語を話すお客様やサービス担当者もいるため、Maria は [Add Language (言語を追加)] をクリックしてスペイン語のキーワードと応答を追加してから、変更内容を保存します。」
- v: Trailhead のユニット本文で確認 / f: messaging
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/whatsapp-for-service-cloud/fine-tune-your-whatsapp-channel

### 192. Trailhead: Agentforce Service 向け WhatsApp / WhatsApp チャネルを細かく調整する Q2
- 問題: ページコンポーネントのうち、拡張メッセージングセッションのリアルタイムのトランスクリプトが表示されるものはどれですか?
- 正解: 拡張会話(a=[2])
- 根拠(ユニット本文・日本語版): 「拡張会話: 拡張メッセージングセッションのリアルタイムのトランスクリプトが表示されます。」
- v: Trailhead のユニット本文で確認 / f: messaging
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/whatsapp-for-service-cloud/fine-tune-your-whatsapp-channel

### 193. Trailhead: Agentforce Service 向け WhatsApp / WhatsApp をメッセージングコンポーネントで拡張する Q1
- 問題: 次の種別のメッセージングコンポーネントのうち、直近の注文を設定したクリック可能なリストをお客様に表示できるものはどれですか?
- 正解: 動的オプションが含まれる質問(a=[2])
- 根拠(ユニット本文・日本語版): 「動的オプションが含まれる質問コンポーネントを作成して、お客様の直近の 3 件の注文を設定したクリック可能なリストを表示する。」
- v: Trailhead のユニット本文で確認 / f: messaging
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/whatsapp-for-service-cloud/extend-whatsapp-with-messaging-components

### 194. Trailhead: Agentforce Service 向け WhatsApp / WhatsApp をメッセージングコンポーネントで拡張する Q2
- 問題: 次の種別のメッセージングコンポーネントのうち、空いている時間枠を設定したクリック可能なリストをお客様に表示できるものはどれですか?
- 正解: 時間セレクター(a=[3])
- 根拠(ユニット本文・日本語版): 「時間セレクターコンポーネントを作成して、空いている時間枠を近い順に 4 つ表示する。」
- v: Trailhead のユニット本文で確認 / f: messaging
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/whatsapp-for-service-cloud/extend-whatsapp-with-messaging-components

### 195. Trailhead: Agentforce Service 向け WhatsApp / WhatsApp でお客様をサポートする Q1
- 問題: サービスコンソールで、メッセージングコンポーネントはどこに表示されますか?
- 正解: A と B(a=[3])
- 根拠(ユニット本文・日本語版): 「静的コンテンツが含まれるメッセージングコンポーネントを送信する場合は、担当者がサービスコンソールのメッセージングウィンドウでメッセージングコンポーネントアクションをクリックして、コンポーネントのリストの中から選択します。/ 他方、お客様ごとに異なる動的なコンテンツ (動的オプションが含まれる質問、時間セレクターなど) を伴なうメッセージングコンポーネントは、専用のスペースが必要なため、独自のフローコンポーネントとして表示されます。」
- v: Trailhead のユニット本文で確認 / f: messaging
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/whatsapp-for-service-cloud/help-customers-in-whatsapp

### 196. Trailhead: Agentforce Service 向け WhatsApp / WhatsApp でお客様をサポートする Q2
- 問題: サービス担当者は拡張 WhatsApp メッセージングセッションをどこに転送できますか?
- 正解: A、B、C のすべて(a=[4])
- 根拠(ユニット本文・日本語版): 「別の担当者、キュー、オムニチャネルルーティングフローに転送して、問題が解決されるようにします。」
- v: Trailhead のユニット本文で確認 / f: messaging
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/whatsapp-for-service-cloud/help-customers-in-whatsapp
