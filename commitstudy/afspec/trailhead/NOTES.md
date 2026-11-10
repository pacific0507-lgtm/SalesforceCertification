# Trailhead モジュールのクイズ: Agentforce スペシャリスト (afspec)

出題元: 資格ページ https://trailhead.salesforce.com/credentials/agentforcespecialist の「Study & Prepare」は Agentblazer ステータス(https://trailhead.salesforce.com/agentblazer)を案内している。そこから Become an Agentblazer Champion / Innovator / Legend 2026 の3トレイルのモジュールのうち、出題範囲(エージェント、Builder、サブエージェント/アクション、プロンプト、グラウンディング、Data 360/RAG、テスト、デプロイ、Trust Layer、監視)に関係するものを使った。AI 一般の入門(AI の基礎、LLM、NLP など)、Headless 360、Claude 連携、業種別などは範囲外として除外。営業向けエージェントの3モジュールは afsales に回した。

- 問題数: 178(うち 要確認 5)
- 問題文と選択肢は公式の日本語版(/ja/)を使い、英語を qe/oe に入れた。日本語版がない(英語のまま表示される)ユニットは、日本語を自分で訳した(下の表で「訳」と表示)。
- 正解は Trailhead の HTML に含まれないので、各ユニットの本文から判断した。根拠の文を下に引用した。
- ハンズオン(Challenge/assessment)のユニットとプロジェクト・スーパーバッジは対象外。
- 近い内容の重複クイズは見つからなかった(英語の問題文と選択肢で比較)。
- f はモジュール(一部はユニット)ごとに manuscript の最も近い節を割り当てた。x は節の本文に明確に対応する文がある場合だけ入れ、ほかは空にした。

## 使ったモジュールとユニット

### Agentforce の概要(Introduction to Agentforce)
https://trailhead.salesforce.com/ja/content/learn/modules/introduction-to-agentforce

- Agentforce の機能について知る (get-to-know-agentforce-functionality): クイズ 2問

### 自律型エージェント(Autonomous Agents)
https://trailhead.salesforce.com/ja/content/learn/modules/autonomous-agents

- 自律型エージェントについて知る (get-to-know-autonomous-agents): クイズ 2問
- 自律型エージェントと信頼関係を確立する (establish-trust-with-autonomous-agents): クイズ 2問
- 自律型エージェントでビジネストランスフォーメーションを実現する (transform-your-business-with-autonomous-agents): クイズ 2問

### Agentforce の基本(Agentforce Basics)
https://trailhead.salesforce.com/ja/content/learn/modules/einstein-copilot-basics

- はじめての Agentforce (get-started-with-einstein-copilot): クイズ 2問
- Agentforce を試す (explore-einstein-copilot): クイズ 2問
- 推論エンジンの概要 (enable-customize-copilot): クイズ 2問

### 新しい Agentforce Builder: クイックルック(New Agentforce Builder: Quick Look)
https://trailhead.salesforce.com/ja/content/learn/modules/new-agentforce-builder-quick-look

- 新しいエージェントビルダーについて知る (explore-the-new-agentforce-builder): クイズ 2問

### Agentforce Builder の概要(Introduction to Agentforce Builder)
https://trailhead.salesforce.com/ja/content/learn/modules/introduction-to-agent-builder

- Agentforce Builder について知る (get-to-know-agent-builder): クイズ 2問

### Agentforce を使用した設定: クイックルック(Setup with Agentforce: Quick Look)
https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-for-setup-quick-look

- Agentforce を使用した設定について知る (get-to-know-setup-with-agentforce): クイズ 2問

### サービス向け Agentforce(Agentforce for Service)
https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-service-agent-quick-look

- サービス向け Agentforce 入門 (get-started-with-agentforce-service-agent): クイズ 2問
- サービス向け Agentforce のユースケースを確認する (explore-use-cases-for-agentforce-for-service): クイズ 2問
- サービス向け Agentforce でナレッジを使用する (use-knowledge-in-agentforce-for-service): クイズ 2問

### Salesforce モバイルアプリケーションの Agentforce: クイックルック(Agentforce on the Salesforce Mobile App: Quick Look)
https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-on-the-salesforce-mobile-app-quick-look

- Salesforce モバイルアプリケーションで Agentforce を使用して時間を節約する (save-time-with-agentforce-on-the-salesforce-mobile-app): クイズ 2問

### AgentExchange: クイックルック(AgentExchange: Quick Look)
https://trailhead.salesforce.com/ja/content/learn/modules/agentexchange-quick-look

- 新しい AgentExchange を体験する (experience-the-new-agentexchange): クイズ 2問

### クイックスタート: Agentforce Builder でサービスエージェントを構築する(Quick Start: Assemble a Service Agent with Agentforce Builder)
https://trailhead.salesforce.com/ja/content/learn/modules/quick-start-assemble-a-service-agent-with-agentforce-builder

- Agentforce Builder について学ぶ (learn-about-agentforce-builder): ハンズオンのため対象外
- Agentforce Builder を使って構築する (build-with-agentforce-builder): ハンズオンのため対象外

### Agentforce でのプログラムによる指示(Programmatic Instructions in Agentforce)
https://trailhead.salesforce.com/ja/content/learn/modules/programmatic-instructions-in-agentforce

- フロー、アクション、権限を使用してエージェントに追加情報を提供する (give-your-agent-more-information-with-flows-actions-and-permissions): クイズ 2問
- 条件ロジックを使用して各コンテキストに適したプロンプトを送信する (use-conditional-logic-to-send-the-right-prompt-for-each-context): クイズ 2問
- 変数とアクションの絞り込みを使用してビジネスルールエンジンを適応する (enforce-business-rules-with-variables-and-action-filters): クイズ 2問

### 従業員エージェントを使って業務を進める(Use Employee Agents to Get Work Done)
https://trailhead.salesforce.com/ja/content/learn/modules/use-employee-agents-to-get-work-done

- Coral Cloud Resorts へようこそ (welcome-to-coral-cloud-resorts): ハンズオンのため対象外
- 水漏れトラブルに対応する (help-a-guest-out-of-a-soggy-situation): ハンズオンのため対象外
- 紛失したマザーズバッグを探す (solve-the-case-of-the-missing-diaper-bag): ハンズオンのため対象外
- ゲストの体験予約を変更する (navigate-guest-experience-bookings): ハンズオンのため対象外

### プロンプトの基本事項(Prompt Fundamentals)
https://trailhead.salesforce.com/ja/content/learn/modules/prompt-fundamentals

- プロンプト入門 (get-started-with-prompts): クイズ 2問
- より良いプロンプトを書く (write-better-prompts): クイズ 2問
- プロンプト設計パターンを確認する (explore-prompt-design-patterns): クイズ 2問
- モデルの適合性が重要な理由を学ぶ (learn-why-model-fit-matters): クイズ 2問
- プロンプトのテストと改善 (test-and-improve-prompts): クイズ 2問

### プロンプトビルダーの基本(Prompt Builder Basics)
https://trailhead.salesforce.com/ja/content/learn/modules/prompt-builder-basics

- プロンプトビルダーについて知る (get-to-know-prompt-builder): クイズ 2問
- プロンプトテンプレートを作成してグラウンディングする (create-and-ground-prompt-templates): クイズ 2問
- 項目生成プロンプトテンプレートを構築する (build-a-field-generation-prompt-template): クイズ 2問
- プロンプトテンプレートを確認して修正し、保存する (review-revise-and-repeat-testing-prompt-templates): クイズ 2問

### Agentforce Trust Layer(The Agentforce Trust Layer)
https://trailhead.salesforce.com/ja/content/learn/modules/the-einstein-trust-layer

- Agentforce Trust Layer の概要 (meet-the-einstein-trust-layer): クイズ 2問
- プロンプトジャーニーをたどる (follow-the-prompt-journey): クイズ 2問
- 応答ジャーニーをたどる (follow-the-response-journey): クイズ 2問

### データ + AI + CRM: クイックルック(Data + AI + CRM: Quick Look)
https://trailhead.salesforce.com/ja/content/learn/modules/ai-data-crm-quick-look

- データ + AI + CRM が連携するしくみを学習する (learn-how-ai-data-crm-work-together): クイズ 2問

### Agentforce: エージェントプランニング(Agentforce: Agent Planning)
https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-agent-planning

- エージェントのユースケースを特定する (identify-the-agent-use-case): クイズ 2問
- 適切なソリューションを設計する (architect-the-right-solution): クイズ 2問
- エージェントのガードレールを定義する (define-the-agent-guardrails): クイズ 2問
- エージェントの作業の概要を定める (outline-the-agents-work): クイズ 2問
- エージェントのプロトタイプを作成する (prototype-the-agent): クイズ 2問

### エージェントの動作の基本(Agent Behavior Basics)
https://trailhead.salesforce.com/ja/content/learn/modules/agent-behavior-basics

- エージェントの動作と会話デザインを検討する (explore-agent-behavior-and-conversation-design): クイズ 2問
- 信頼できる動作をデザインする (design-trusted-behavior): クイズ 2問

### エージェントの動作の評価(Agent Behavior Evaluation)
https://trailhead.salesforce.com/ja/content/learn/modules/agent-behavior-evaluation

- AI エージェントの価値を評価する (evaluate-ai-agent-value): クイズ 2問
- エージェント応答をトリアージする (triage-agent-responses): クイズ 2問

### 信頼できるエージェント型 AI(Trusted Agentic AI)
https://trailhead.salesforce.com/ja/content/learn/modules/trusted-agentic-ai

- Salesforce が信頼できるエージェント型 AI を構築する方法を確認する (discover-how-salesforce-builds-trusted-agentic-ai): クイズ 2問
- Agentforce のガードレールと信頼パターンを検討する (explore-agentforce-guardrails-and-trust-patterns): クイズ 2問
- 責任ある倫理的なエージェントを推進する (promote-responsible-and-ethical-agents): クイズ 2問

### AI エージェントの脅威モデリング(Threat Modeling for AI Agents)
https://trailhead.salesforce.com/ja/content/learn/modules/threat-modeling-for-ai-agents

- AI エージェントの使用に伴うリスクを認識する (know-the-risks-when-using-ai-agents): クイズ 2問
- AI エージェントのリスクを特定して管理する (identify-and-manage-ai-agent-risks): クイズ 2問

### サービスエージェントのための Agentforce リリース(Agentforce Deployment for Service Agents)
https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-deployment-quick-look

- リリースプロセスについて学ぶ (learn-about-the-deployment-process): クイズ 2問
- メッセージング接続を設定する (set-up-the-messaging-connection): クイズ 2問
- メッセージング接続を Web サイトにリリースする (deploy-the-messaging-connection-to-a-website): クイズ 2問
- 音声接続のセットアップ (set-up-the-voice-connection): クイズ 2問
- エージェントを本番環境にリリースする (deploy-an-ai-agent-with-agentforce): クイズ 2問

### Agentforce Voice
https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-voice-quick-look

- Agentforce Voice の概要 (meet-agentforce-voice): クイズ 2問
- 音声対応エージェントを作成する (build-your-voice-enabled-agent): クイズ 2問
- 着信通話ルーティングを管理する (manage-inbound-call-routing-agenforce-voice): クイズ 2問

### Agentforce サービスアシスタント(Agentforce Service Assistant)
https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-service-assistant

- サービスアシスタントを準備する (plan-for-service-assistant): クイズ 2問
- サービスアシスタントを設定する (set-up-service-assistant): ハンズオンのため対象外
- サービスアシスタントをテストする (test-service-assistant): クイズ 2問

### エージェントのカスタマイズ: クイックルック(Agent Customization: Quick Look)
https://trailhead.salesforce.com/ja/content/learn/modules/agent-customization-quick-look

- エージェントをカスタマイズする (customize-your-agents): クイズ 2問

### プロンプトビルダーを使用したサービスエージェントのカスタマイズ(Service Agent Customization with Prompt Builder)
https://trailhead.salesforce.com/ja/content/learn/modules/custom-service-agents-with-prompt-builder-and-agentforce

- 効果的なプロンプトテンプレートを作成する (craft-an-effective-prompt-template): ハンズオンのため対象外
- エージェントアクションを活用してプロンプトを実用化する (bring-your-prompt-to-life-with-agent-actions): ハンズオンのため対象外
- プロンプトテンプレートを調整してエージェントの応答精度を高める (refine-your-prompt-template-for-accurate-agent-replies): ハンズオンのため対象外

### プロンプトエンジニアリングのテクニック(Prompt Engineering Techniques)
https://trailhead.salesforce.com/ja/content/learn/modules/prompt-engineering-techniques

- いろいろなプロンプト手法を利用してプロンプトを改善しましょう。 (improve-prompts-using-different-prompt-techniques): クイズ 2問
- プロンプトを実際に使ってみる (get-hands-on-with-prompts): ハンズオンのため対象外

### フローを使用したエージェントのカスタマイズ(Agent Customization with Flows)
https://trailhead.salesforce.com/ja/content/learn/modules/agent-customization-with-flows

- フローをエージェント対応にする (learn-how-to-make-agent-ready-flows): クイズ 2問
- エージェント対応フローを作成する (create-an-agent-ready-flow): ハンズオンのため対象外
- エージェントアクションとしてフローを追加する (add-a-flow-as-an-agent-action): ハンズオンのため対象外

### Apex を使用したエージェントのカスタマイズ(Agent Customization with Apex)
https://trailhead.salesforce.com/ja/content/learn/modules/agent-customization-with-apex

- Apex アクションを作成する準備をしましょう。 (get-ready-to-create-an-apex-action): ハンズオンのため対象外
- Apex エージェントアクションを作成する (create-an-apex-agent-action): ハンズオンのため対象外

### エージェントをデータでグラウンディングする(Grounding an Agent with Data)
https://trailhead.salesforce.com/ja/content/learn/modules/grounding-an-agent-with-data

- グラウンディングの基本を学ぶ (learn-the-basics-of-grounding): クイズ 2問
- エージェントをデータでグラウンディングするためのオプションを確認する (review-options-to-ground-an-agent-with-data): クイズ 2問

### 検索拡張生成: クイックルック(Retrieval Augmented Generation: Quick Look)
https://trailhead.salesforce.com/ja/content/learn/modules/retrieval-augmented-generation-quick-look

- 関連ビジネスナレッジを使用したエージェントとプロンプトの拡張 (augment-prompts-with-relevant-knowledge): クイズ 2問

### Agentforce データライブラリの基礎(Agentforce Data Library Basics)
https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-data-library-basics

- 実世界のデータで AI をアップグレードする (upgrade-ai-with-real-world-data): クイズ 2問
- エージェントのファイルベースライブラリを構築する (build-a-file-based-data-library-for-an-agent): クイズ 2問

### Data 360 を駆使したエクスペリエンス(Data 360-Powered Experiences)
https://trailhead.salesforce.com/ja/content/learn/modules/data-cloud-powered-experiences

- Data 360 のしくみを学習する (learn-how-data-cloud-works): クイズ 2問
- Data 360 の活用例を見る (see-data-cloud-in-action): クイズ 2問

### Data 360 を活用した Agentforce(Data 360-Powered Agentforce)
https://trailhead.salesforce.com/ja/content/learn/modules/data-cloud-powered-agentforce

- Data 360 と Agentforce について検討する (explore-data-cloud-and-agentforce): クイズ 2問
- Data 360 を使用して信頼できるエージェントを実現する (enable-trusted-agents-with-data-cloud): クイズ 2問
- Agentforce に Data 360 を実装する (implement-data-cloud-for-agentforce): クイズ 2問

### Data 360 の検索インデックス種別: クイックルック(Search Index Types in Data 360: Quick Look)
https://trailhead.salesforce.com/ja/content/learn/modules/search-index-types-data-cloud-quick-look

- Data 360 の 検索インデックス種別について知る (get-to-know-search-index-types-in-data-cloud): クイズ 2問

### Data 360 Sandbox(Data 360 Sandboxes)
https://trailhead.salesforce.com/ja/content/learn/modules/data-360-sandboxes

- Data 360 Sandbox を設定する (set-up-your-data-360-sandbox): クイズ 2問
- Data 360 Sandbox を更新して同期する (refresh-and-synchronize-your-data-360-sandbox): クイズ 2問
- Data 360 の設定を DevOps データキットにバンドルする (bundle-data-360-configurations-into-a-devops-data-kit): クイズ 2問
- Data 360 設定を展開して検証する (deploy-and-validate-your-data-360-configurations): クイズ 2問

### Agentforce のテストツールと計画(Agentforce Testing Tools and Strategies)
https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-testing-tools-and-strategies

- エージェントのテストツールと考慮事項を確認する (explore-agent-testing-tools-and-considerations): クイズ 2問
- 5 ステップのテスト計画を使用してエージェントを調整する (refine-your-agents-using-a-five-step-testing-strategy): クイズ 2問

### Agentforce テストセンター(Agentforce Testing Center)
https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-agent-testing

- エージェントを信頼する (trust-your-agents): クイズ 2問
- テスト条件を設定する (set-up-testing-criteria): ハンズオンのため対象外
- AI を使用してテストを生成する (use-ai-to-generate-tests): ハンズオンのため対象外
- テスト結果を確認する (view-test-results): クイズ 2問

### エージェントの分析と監視(Agent Analytics and Monitoring)
https://trailhead.salesforce.com/ja/content/learn/modules/agent-analytics-and-monitoring

- エージェントモニタリングを使ってみる (get-started-with-agent-monitoring): クイズ 2問
- エージェントのメトリクスとスコアを監視する (monitor-agent-metrics-and-scores): クイズ 2問
- エージェントのセッションとインテントを調査する (investigate-agent-sessions-and-intents): クイズ 2問
- エージェント健全性を監視する (monitor-agent-health): クイズ 2問

### Agentforce のエージェント動作のトラブルシューティング(Agent Behavior Troubleshooting in Agentforce)
https://trailhead.salesforce.com/ja/content/learn/modules/agent-behavior-troubleshooting-in-agentforce

- Agentforce のトラブルシューティング入門 (get-started-with-agentforce-troubleshooting): クイズ 2問
- 設定とデータの問題を修正する (fix-configuration-and-data-issues): クイズ 2問
- ルーティング、アクション、プロンプト作文の問題を解決する (resolve-routing-action-and-prompting-issues): クイズ 2問
- グラウンディング、制限、一般的なエラーをトラブルシューティングする (troubleshoot-grounding-limits-and-common-errors): クイズ 2問
- インテグレーションエラーとランタイムエラーを解決する (resolve-integration-and-runtime-errors): クイズ 2問

### Slack にリリースする Agentforce の設定(Agentforce Configuration for Slack Deployment)
https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-configuration-for-slack-deployment

- Agentforce と Slack が連携するしくみ (learn-how-agentforce-and-slack-work-together): クイズ 2問
- Salesforce で Slack エージェントを設定する (configure-a-slack-agent-in-salesforce): ハンズオンのため対象外
- エージェントを Slack にリリースする (deploy-an-agent-in-slack): ハンズオンのため対象外

### エージェント API: クイックルック(Agent API: Quick Look)
https://trailhead.salesforce.com/ja/content/learn/modules/agent-api-quick-look

- エージェント API を使用してカスタム AI エージェントを作成する (build-custom-ai-agents-with-agent-api): クイズ 2問

### Models API 入門(Get Started with the Models API)
https://trailhead.salesforce.com/ja/content/learn/modules/get-started-with-einstein-models-api

- Models API の基本を学ぶ (learn-the-basics-of-models-api): クイズ 2問
- 組織で Models API にアクセスする準備をする (prepare-your-org-to-access-the-models-api): ハンズオンのため対象外
- Models API の Lightning Web コンポーネントを作成する (create-a-models-api-lightning-web-component): ハンズオンのため対象外

## 正解と根拠

### 1. Trailhead: エージェントの分析と監視 / エージェントモニタリングを使ってみる Q1
- 問題: エージェントのオブザーバビリティに付属する機能のうち、継続的な改善を直接サポートするものはどれですか?
- 正解: エージェントの実際の動作に基づいて、期待を下回る結果を特定し、重点的な改善策を実施する機能(a=[0])
- 根拠(ユニット本文・日本語版): 「エージェントのオブザーバビリティを活用した継続的な改善」
- v: Trailhead のユニット本文で確認 / f: observe
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agent-analytics-and-monitoring/get-started-with-agent-monitoring

### 2. Trailhead: エージェントの分析と監視 / エージェントモニタリングを使ってみる Q2
- 問題: エージェントのデフレクション率、エスカレーション率、放棄率を測定するときは、どのようなメトリクスを使用しますか?
- 正解: エージェントの有効性(a=[2])
- 根拠(ユニット本文・日本語版): 「有効性 : ケースデフレクション率 (%) など」
- v: Trailhead のユニット本文で確認 / f: observe
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agent-analytics-and-monitoring/get-started-with-agent-monitoring

### 3. Trailhead: エージェントの分析と監視 / エージェントのメトリクスとスコアを監視する Q1
- 問題: エージェント分析で、エージェントのパフォーマンスのインテント別の内訳はどこで検討できますか?
- 正解: パフォーマンスのインサイト(a=[2])
- 根拠(ユニット本文・日本語版): 「[Performance Insights (パフォーマンスのインサイト)] タブでは、セグメント間のパフォーマンスを比較できます。どのサブエージェント、インテント、アクションが良い結果または悪い結果をもたらしているのかを確認できます。このタブを使用して、パフォーマンスが不振なセグメントを調査します。」
- v: Trailhead のユニット本文で確認 / f: observe
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agent-analytics-and-monitoring/monitor-agent-metrics-and-scores

### 4. Trailhead: エージェントの分析と監視 / エージェントのメトリクスとスコアを監視する Q2
- 問題: ユーザー数は 2 日間同じであると仮定します。2 日目にデフレクション率が上昇した場合、どのようなことを意味しますか?
- 正解: エージェントが解決することができるユーザーリクエストが増えた。(a=[3])
- 根拠(ユニット本文・日本語版): 「Deflection Rate (デフレクション率) : サポート担当者または別のエージェントへのエスカレーションなしで終了したセッションの割合」
- v: Trailhead のユニット本文で確認 / f: observe / x: 「Effectiveness タブでは、Deflection Rate(エスカレーションなしで終わったセッションの割合)、Escalation Rate、Abandonment Rate などを見ます。」
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agent-analytics-and-monitoring/monitor-agent-metrics-and-scores

### 5. Trailhead: エージェントの分析と監視 / エージェントのセッションとインテントを調査する Q1
- 問題: [Sessions & Intents (セッションとインテント)] ページに移動したところ、一部のセッションが [Unprocessed (未処理)] と表示されていることに気がつきました。これはどういう意味でしょうか?
- 正解: これらのセッションは現在進行中か、終了したばかりで、インテントパイプラインやクラスタリングパイプラインによる処理が完了していない。(a=[1])
- 根拠(ユニット本文・日本語版): 「[Processed Sessions (処理済みセッション)] にセッションが見つからない場合は、[Unprocessed Sessions (未処理セッション)] を確認してください。まだ処理中の可能性があります。」
- v: Trailhead のユニット本文で確認 / f: observe
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agent-analytics-and-monitoring/investigate-agent-sessions-and-intents

### 6. Trailhead: エージェントの分析と監視 / エージェントのセッションとインテントを調査する Q2
- 問題: エージェントがオプショナルツアーの予約に失敗した理由を理解したいと思い、セッションの [Trace (トレース)] タブを確認しています。トレースではどのような情報を確認できますか?
- 正解: エージェントが試行した一連のアクション、各アクションへの入力、返された出力(a=[0])
- 根拠(ユニット本文・日本語版): 「[Trace (トレース)] タブには、エージェントが実行したすべての処理のステップと各ステップの所要時間が時系列で表示されます。」
- v: Trailhead のユニット本文で確認 / f: observe / x: 「Agentforce セッショントレース(Session Tracing)セッションごとのターン、推論の手順、アクション、メッセージ、エラーエージェントが何を判断し、何をしたか」
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agent-analytics-and-monitoring/investigate-agent-sessions-and-intents

### 7. Trailhead: エージェントの分析と監視 / エージェント健全性を監視する Q1
- 問題: プロアクティブなエージェント健全性監視によって可能になることは何ですか?
- 正解: 影響が広がる前に、エラーや遅延の急増をいち早く検知する。(a=[1])
- 根拠(ユニット本文・日本語版): 「エージェント健全性監視があれば、チームがこうした人目につかない障害をほぼリアルタイムで検知して、迅速に対応できるようになります。」
- v: Trailhead のユニット本文で確認 / f: observe / x: 「Agent Health Monitoring のアラートは、1つのエージェントの1つの指標を監視します。毎分、直近15分のデータで評価し、通知したあと30分は同じアラートから再通知しません。」
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agent-analytics-and-monitoring/monitor-agent-health

### 8. Trailhead: エージェントの分析と監視 / エージェント健全性を監視する Q2
- 問題: 通知に基づいて関連するセッションを詳しく調べる最大の目的は何ですか?
- 正解: アラート違反の発生期間に関連するインタラクションを特定するため(a=[1])
- 根拠(ユニット本文・日本語版): 「するとすぐ、アラート条件に関連するインタラクションに絞り込まれます。」
- v: Trailhead のユニット本文で確認 / f: observe
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agent-analytics-and-monitoring/monitor-agent-health

### 9. Trailhead: エージェント API: クイックルック / エージェント API を使用してカスタム AI エージェントを作成する Q1
- 問題: エージェント API へのコールを実行するには何が必要ですか?
- 正解: A と B と C(a=[4])
- 根拠(ユニット本文・日本語版): 「ステップ 2: 外部クライアントアプリケーションを作成して、OAuth 設定を有効にする」
- v: Trailhead のユニット本文で確認 / f: channels
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agent-api-quick-look/build-custom-ai-agents-with-agent-api

### 10. Trailhead: エージェント API: クイックルック / エージェント API を使用してカスタム AI エージェントを作成する Q2
- 問題: 正誤問題: エージェント API では、同期メッセージ処理とストリーミングメッセージ処理の両方がサポートされている。
- 正解: 正しい(a=[0])
- 根拠(ユニット本文・日本語版): 「エージェント API では、同期メッセージ処理とストリーミングメッセージ処理の両方がサポートされています。」
- v: Trailhead のユニット本文で確認 / f: channels
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agent-api-quick-look/build-custom-ai-agents-with-agent-api

### 11. Trailhead: エージェントの動作の基本 / エージェントの動作と会話デザインを検討する Q1
- 問題: 次のうち、従来の電話自動応答システムや基本的なチャットボットなど、ルールベースのスクリプト型対話システムの主な制限事項はどれですか?
- 正解: 事前定義されたパスを忠実にたどり、ユーザーがスクリプトから逸脱すると行き詰まる。(a=[3])
- 根拠(ユニット本文・日本語版): 「従来の電話自動応答システムや基本的なチャットボットを思い浮かべてみてください。こうしたシステムは確定的でした。つまり、事前に定義された厳格なパスをたどっていました。お客様がスクリプトから外れると、そこで行き止まりになります。」
- v: Trailhead のユニット本文で確認 / f: topics
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agent-behavior-basics/explore-agent-behavior-and-conversation-design

### 12. Trailhead: エージェントの動作の基本 / エージェントの動作と会話デザインを検討する Q2
- 問題: 次のうち、インテントの失敗の例に該当するものはどれですか?
- 正解: ユーザーが注文をキャンセルしたいときに、代わりにキャンセルポリシーに関する情報を提示する。(a=[1])
- 根拠(ユニット本文・日本語版): 「もう 1 つはインテントの失敗で、エージェントがきちんと指示に従っているにもかかわらず、ユーザーの問題が解決されない状況です。」
- v: Trailhead のユニット本文で確認 / f: topics
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agent-behavior-basics/explore-agent-behavior-and-conversation-design

### 13. Trailhead: エージェントの動作の基本 / 信頼できる動作をデザインする Q1
- 問題: ユーザーがエージェントとやり取りするときに、正しい答えが示されますが、その結論に至った経緯や参照した情報源が説明されません。信頼できる動作を支える領域のうち、ユーザーの不安を軽減するために改善が必要なものはどれですか?
- 正解: 明確性(a=[2])
- 根拠(ユニット本文・日本語版): 「根拠を説明する: エージェントは回答を提示するだけでなく、その根拠となる情報源も簡潔に示します。たとえば、「会社の保証ポリシーに基づいて…」と説明します。」
- v: Trailhead のユニット本文で確認 / f: topics
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agent-behavior-basics/design-trusted-behavior

### 14. Trailhead: エージェントの動作の基本 / 信頼できる動作をデザインする Q2
- 問題: スムーズで敬意あるユーザーエクスペリエンスを維持するために、エージェントから人間への引き継ぎを優先すべきタイミングはいつですか?
- 正解: ユーザーのセンチメントが著しく否定的になった場合、またはタスクに人間レベルの権限が必要な場合。(a=[1])
- 根拠(ユニット本文・日本語版): 「エスカレーションすべき状況を把握する: エージェントは機密性の高い極めて複雑なシナリオを特定し、ユーザーのセンチメントが著しく否定的になった場合や、タスクに人間レベルの権限が必要な場合に、人間の担当者に丁重に引き継ぎます。」
- v: Trailhead のユニット本文で確認 / f: topics
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agent-behavior-basics/design-trusted-behavior

### 15. Trailhead: エージェントの動作の評価 / AI エージェントの価値を評価する Q1
- 問題: エージェントは特定のデータベースにアクセスできないことを正確に認識し、ユーザーが手動で情報を確認できるダッシュボードへのリンクを提供しました。ユーザーはエージェントが機能しないと報告します。システム管理者はこのフィードバックをどのように分類すべきですか?
- 正解: ユーザーエクスペリエンスの失敗をもたらした技術的に成功したインタラクション(a=[1])
- 根拠(ユニット本文・日本語版): 「技術的に言えば、 これは成功したインタラクションです。エージェントはハルシネーションを起こさず、自身の制限を正確に特定してユーザーを適切に誘導しました。ただし、ユーザーにとっては、 これは失敗と言えます。タスクを完了するために必要な回答が得られませんでした。ユーザーにとって、エージェントは機能しなかったのです。」
- v: Trailhead のユニット本文で確認 / f: testing
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agent-behavior-evaluation/evaluate-ai-agent-value

### 16. Trailhead: エージェントの動作の評価 / AI エージェントの価値を評価する Q2
- 問題: セールス業務エージェントは機能していて正確ですが、単純なデータ要求に対して 500 語の説明を提供するため、ユーザーはスクロールして実際の数値を探さなければなりません。失敗ポイント分類によると、この問題の優先度レベルまたはランクは何ですか?
- 正解: P2: 価値が限られている(a=[2])
- 根拠(ユニット本文・日本語版): 「エージェントは機能しており、正確ですが、出力の品質が低い、冗長すぎる、または実際の回答を得るためにユーザーがさらに作業する必要があります。」
- v: Trailhead のユニット本文で確認 / f: testing
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agent-behavior-evaluation/evaluate-ai-agent-value

### 17. Trailhead: エージェントの動作の評価 / エージェント応答をトリアージする Q1
- 問題: エージェントの動作の設計において、評価はどのような役割を果たしますか?
- 正解: 的を絞った評価により、設計担当者はユーザーインテントを達成するための介入をトリアージし、優先度を付けることができる。(a=[0])
- 根拠(ユニット本文・日本語版): 「これらのログにより、設計担当者は会話の流れを確認でき、エージェントが異なる動作ができた可能性のある、不満や失敗のポイントも把握できます。」
- v: Trailhead のユニット本文で確認 / f: testing
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agent-behavior-evaluation/triage-agent-responses

### 18. Trailhead: エージェントの動作の評価 / エージェント応答をトリアージする Q2
- 問題: ヒューリスティックが評価された後、設計担当者はエージェントの会話ログ全体にどのようにスコアを付けるべきですか?
- 正解: 最終的な優先度は、ほかのヒューリスティックにかかわらず、最も重大な失敗に基づいて評価される。(a=[3])
- 根拠(ユニット本文・日本語版): 「この最終スコアは平均に基づくものではありません。1 つの重大な失敗がユーザーエクスペリエンスに大きな影響を与える可能性があるためです。代わりに、観察された最も高い重大度ランクに基づいて会話のスコアが付けられます。」
- v: Trailhead のユニット本文で確認 / f: testing
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agent-behavior-evaluation/triage-agent-responses

### 19. Trailhead: Agentforce のエージェント動作のトラブルシューティング / Agentforce のトラブルシューティング入門 Q1
- 問題: エージェントルーターではどのようなことができますか?
- 正解: サブエージェントの選択を確認する。(a=[0])
- 根拠(ユニット本文・日本語版): 「ルーティング: エージェントルーター は、想定どおりのサブエージェントを選択しましたか?」
- v: Trailhead のユニット本文で確認 / f: testing
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agent-behavior-troubleshooting-in-agentforce/get-started-with-agentforce-troubleshooting

### 20. Trailhead: Agentforce のエージェント動作のトラブルシューティング / Agentforce のトラブルシューティング入門 Q2
- 問題: Agentforce の予期しない動作の一般的な根本原因はどれですか?
- 正解: 範囲が不明確で、重複しているサブエージェント(a=[2])
- 根拠(ユニット本文・日本語版): 「ほかのサブエージェントとの重複、汎用的な名前、あいまいな説明や範囲が広すぎる説明がないか」
- v: Trailhead のユニット本文で確認 / f: testing
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agent-behavior-troubleshooting-in-agentforce/get-started-with-agentforce-troubleshooting

### 21. Trailhead: Agentforce のエージェント動作のトラブルシューティング / 設定とデータの問題を修正する Q1
- 問題: データエラーではなく設定エラーを最も直接的に示す症状はどれですか?
- 正解: エージェントがワークフローを実行すると、「Access Denied (アクセスが拒否されました)」または「Insufficient Privileges (アクセス権がありません)」と表示される。(a=[3])
- 根拠(ユニット本文・日本語版): 「症状としては、設定されたワークフローをエージェントが実行しない、「Access Denied (アクセスが拒否されました)」または「Insufficient Privileges (アクセス権がありません)」といったエラーが発生する、UI に AI アクションが表示されない、などが挙げられます。」
- v: Trailhead のユニット本文で確認 / f: testing
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agent-behavior-troubleshooting-in-agentforce/fix-configuration-and-data-issues

### 22. Trailhead: Agentforce のエージェント動作のトラブルシューティング / 設定とデータの問題を修正する Q2
- 問題: Data Cloud を基盤とした応答が古いまたは不完全に見える場合、最初に何を確認すべきですか?
- 正解: データストリームの同期状況と項目の対応付け(a=[1])
- 根拠(ユニット本文・日本語版): 「次に、ソースシステムと Data 360 データモデル間の項目の対応付けを確認します。」
- v: Trailhead のユニット本文で確認 / f: testing
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agent-behavior-troubleshooting-in-agentforce/fix-configuration-and-data-issues

### 23. Trailhead: Agentforce のエージェント動作のトラブルシューティング / ルーティング、アクション、プロンプト作文の問題を解決する Q1
- 問題: エージェントが確実に使用できるようにコンテキスト変数を設定するには、どうすればよいですか?
- 正解: アクション出力の対応付け、変数の対応付け、またはフローロジックを使用して設定する。(a=[3])
- 根拠(ユニット本文・日本語版): 「コンテキスト変数は、アクション出力の対応付け、設定での変数の対応付け、またはフローや構造化された割り当てロジックを通じて直接設定してください。」
- v: Trailhead のユニット本文で確認 / f: testing
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agent-behavior-troubleshooting-in-agentforce/resolve-routing-action-and-prompting-issues

### 24. Trailhead: Agentforce のエージェント動作のトラブルシューティング / ルーティング、アクション、プロンプト作文の問題を解決する Q2
- 問題: プロンプト作文の問題による予測不能な動作を軽減するプラクティスはどれですか?
- 正解: アクションを使用すべき状況と使用すべきでない状況を明確に定義する。(a=[1])
- 根拠(ユニット本文・日本語版): 「アクションを実行すべき状況と実行すべきでない状況を明確に定義します。」
- v: Trailhead のユニット本文で確認 / f: testing
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agent-behavior-troubleshooting-in-agentforce/resolve-routing-action-and-prompting-issues

### 25. Trailhead: Agentforce のエージェント動作のトラブルシューティング / グラウンディング、制限、一般的なエラーをトラブルシューティングする Q1
- 問題: Agentforce の応答に引用を表示するために必要な条件は何ですか?
- 正解: ナレッジアクションが引用を返し、そのアクションで引用が有効になっている。(a=[2])
- 根拠(ユニット本文・日本語版): 「引用は、 ナレッジアクション が引用を返し、そのアクションで引用が有効になっている場合にのみ表示されます。」
- v: Trailhead のユニット本文で確認 / f: testing
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agent-behavior-troubleshooting-in-agentforce/troubleshoot-grounding-limits-and-common-errors

### 26. Trailhead: Agentforce のエージェント動作のトラブルシューティング / グラウンディング、制限、一般的なエラーをトラブルシューティングする Q2
- 問題: Agentforce の応答が途中で切れないようにするための推奨方法は何ですか?
- 正解: 大きな出力を埋め込む代わりに、[Show in Conversation (会話に表示)] を使用する。(a=[1])
- 根拠(ユニット本文・日本語版): 「大きな出力を直接埋め込む代わりに、[Show in Conversation (会話に表示)] を使用します。」
- v: Trailhead のユニット本文で確認 / f: testing
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agent-behavior-troubleshooting-in-agentforce/troubleshoot-grounding-limits-and-common-errors

### 27. Trailhead: Agentforce のエージェント動作のトラブルシューティング / インテグレーションエラーとランタイムエラーを解決する Q1
- 問題: エージェントが外部 API を呼び出すときに、「401 Unauthorized」エラーが発生します。最初に何を確認すべきですか?
- 正解: 指定ログイン情報と OAuth トークンの状況(a=[2])
- 根拠(ユニット本文・日本語版): 「よくある原因としては、期限切れの OAuth トークンや無効な API キー、Salesforce 側で更新されていないエンドポイント URL の変更、または正しく設定されていない指定ログイン情報などが挙げられます。」
- v: Trailhead のユニット本文で確認 / f: testing
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agent-behavior-troubleshooting-in-agentforce/resolve-integration-and-runtime-errors

### 28. Trailhead: Agentforce のエージェント動作のトラブルシューティング / インテグレーションエラーとランタイムエラーを解決する Q2
- 問題: インテグレーションエラーではなく、ランタイムエラーであることを示すものはどれですか?
- 正解: 再帰的なトリガーによる、自動化処理の予期しないループ(a=[1])
- 根拠(ユニット本文・日本語版): 「よくある原因としては、フローロジックの誤りや初期化されていない変数、再帰的なトリガーや循環依存 (互いに繰り返しトリガーし合うステップ)、またはガバナ制限 (Salesforce が 1 つのトランザクションに許可するリソースの上限) の超過などが挙げられます。」
- v: Trailhead のユニット本文で確認 / f: testing
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agent-behavior-troubleshooting-in-agentforce/resolve-integration-and-runtime-errors

### 29. Trailhead: エージェントのカスタマイズ: クイックルック / エージェントをカスタマイズする Q1
- 問題: 複雑な自動化 (プロンプトの一部として外部サービスからデータを取得するなど) に最適なカスタマイズの種別はどれですか?
- 正解: Apex(a=[2])
- 根拠(ユニット本文・日本語版): 「フローやプロンプトによって、エージェントの操作性は大きく向上しますが、それらは自然言語による指示や従来のフローで自動化できる業務に限られます。一方で、大規模言語モデル (LLM) はコードの読み取りと処理も可能であるため、エージェントは Apex の強力な機能も活用できます。」
- v: Trailhead のユニット本文で確認 / f: actions
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agent-customization-quick-look/customize-your-agents

### 30. Trailhead: エージェントのカスタマイズ: クイックルック / エージェントをカスタマイズする Q2
- 問題: フローを使用すると、AI エージェントは何を実行できますか?
- 正解: Salesforce データを変更する(a=[0])
- 根拠(ユニット本文・日本語版): 「Agentforce の真の強みは、エージェントがフローを実行できる点にあります。フローは、顧客レコードの変更などの複雑なビジネス業務をユーザーがローコードで実行できるようにするツールです。」
- v: Trailhead のユニット本文で確認 / f: actions
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agent-customization-quick-look/customize-your-agents

### 31. Trailhead: フローを使用したエージェントのカスタマイズ / フローをエージェント対応にする Q1
- 問題: エージェントアクションで必要なフロー変数の種類はどれですか?
- 正解: 入力変数と出力変数(a=[3])
- 根拠(ユニット本文・日本語版): 「フローベースのエージェントアクションでは、必ずフロー内に 1 つ以上の入力変数と 1 つ以上の出力変数が必要です。」
- v: Trailhead のユニット本文で確認 / f: actions
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agent-customization-with-flows/learn-how-to-make-agent-ready-flows

### 32. Trailhead: フローを使用したエージェントのカスタマイズ / フローをエージェント対応にする Q2
- 問題: エージェントに送信されるデータを制限する場合に選択するべき [Get Records (レコードを取得)] オプションはどれですか?
- 正解: Choose fields and assign variables (項目を選択して変数を割り当てる)(a=[2])
- 根拠(ユニット本文・日本語版): 「このオプションの代わりに、[Choose fields and assign variables (項目を選択して変数を割り当てる)] 設定を選択し、個別のレコード変数を使用して、エージェントが必要な項目のみを選択します。」
- v: Trailhead のユニット本文で確認 / f: actions
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agent-customization-with-flows/learn-how-to-make-agent-ready-flows

### 33. Trailhead: AgentExchange: クイックルック / 新しい AgentExchange を体験する Q1
- 問題: 新しいブラウザータブを開いたり、新しい URL を入力したりせずに、AgentExchange で見つけたエージェントとの互換性のある Slack ツールを見つけるには、Slack アプリケーションでどのように操作しますか?
- 正解: 画面上部のナビゲーションバーにある Slack タブをクリックする。(a=[0])
- 根拠(ユニット本文・日本語版): 「URL を切り替えずにコンテキストを維持: 同じタブ、同じ ID で作業フローを維持しながら、必要なものをすべて見つけます。Agentforce ソリューションを参照していて、それらのエージェントをトリガーする Slack アプリケーションが必要だと気付いた場合は、Slack タブをクリックします。」
- v: Trailhead のユニット本文で確認 / f: stdagents
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agentexchange-quick-look/experience-the-new-agentexchange

### 34. Trailhead: AgentExchange: クイックルック / 新しい AgentExchange を体験する Q2
- 問題: Agentforce Builder から離れずに、カスタムエージェント用に AgentExchange の事前構築済みスキルを見つけて統合するにはどうすればよいですか?
- 正解: AgentExchange は Agentforce Builder に直接組み込まれているため、作業フロー内で事前構築済みのエージェントスキルを簡単に見つけて統合できる。マーケットプレイスはコンテキストを理解し、適切なソリューションをプロアクティブにマッチングする。(a=[0])
- 根拠(ユニット本文・日本語版): 「作業フローの中で必要なものを見つける: AgentExchange は Agentforce Builder に組み込まれているため、作成中のエージェントに応じて、事前構築済みソリューションのパーソナライズされたおすすめが表示されます。」
- v: Trailhead のユニット本文で確認 / f: stdagents
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agentexchange-quick-look/experience-the-new-agentexchange

### 35. Trailhead: Agentforce: エージェントプランニング / エージェントのユースケースを特定する Q1
- 問題: 次の要因のうち、自律型 AI のユースケースの成功に貢献するものはどれですか?
- 正解: ポリシー、ルール、制約が明確に定義され、AI エージェントが独力で従うことができる作業(a=[0])
- 根拠(ユニット本文・日本語版): 「ポリシー、ルール、制約が明確に定義され、AI エージェントが独力で従うことができるか?」
- v: Trailhead のユニット本文で確認 / f: agents
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-agent-planning/identify-the-agent-use-case

### 36. Trailhead: Agentforce: エージェントプランニング / エージェントのユースケースを特定する Q2
- 問題: 自律型 AI のユースケースのうち、範囲が限定的なものから始めることが推奨されるのはなぜですか?
- 正解: 仮説を検証し、価値を実証して、リスクレベルを管理し、計画を立てることができるため(a=[3])
- 根拠(ユニット本文・日本語版): 「範囲を定めれば、仮説を検証して、価値を実証し、リスクのレベルを管理して、AI ソリューションの拡張計画を立てることができます。」
- v: Trailhead のユニット本文で確認 / f: agents
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-agent-planning/identify-the-agent-use-case

### 37. Trailhead: Agentforce: エージェントプランニング / 適切なソリューションを設計する Q1
- 問題: 組織で会話が AI エージェントから人間のサービス担当にエスカレーションされる可能性があるのはなぜですか?
- 正解: 規制や会社のポリシーを遵守するため(a=[1])
- 根拠(ユニット本文・日本語版): 「サービス担当にエスカレーションする理由として、会社のポリシー、ブランド要件、セキュリティ対策、リスク管理、規制遵守などが挙げられます。」
- v: Trailhead のユニット本文で確認 / f: agents
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-agent-planning/architect-the-right-solution

### 38. Trailhead: Agentforce: エージェントプランニング / 適切なソリューションを設計する Q2
- 問題: Salesforce 組織における AI エージェントのデフォルトのアクセスと権限に関する次の文のうち、正しいものはどれですか?
- 正解: AI エージェントのデフォルトの権限はごく限られているため、ジョブの実行に必要なデータへのアクセス権を明示的に付与する必要がある。(a=[2])
- 根拠(ユニット本文・日本語版): 「デフォルトでは、エージェントユーザーに限定的な権限セットが付与されます。セキュリティの観点から言えば、これは最小権限の原則に従っているため好ましいことです。」
- v: Trailhead のユニット本文で確認 / f: agents
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-agent-planning/architect-the-right-solution

### 39. Trailhead: Agentforce: エージェントプランニング / エージェントのガードレールを定義する Q1
- 問題: 正誤問題: AI エージェントの安全性を確保する場合、テクノロジー面のガードレールだけで十分である。
- 正解: 誤り(a=[1])
- 根拠(ユニット本文・日本語版): 「AI 評議会は Coral Cloud の AI ガバナンスの一環として、新しい AI プロジェクトのすべてに安全性レビューの実施を義務付けています。この規定は、組織を AI のリスクから守るためのビジネスプロセスで、テクノロジー機能ではありません。」
- v: Trailhead のユニット本文で確認 / f: agents
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-agent-planning/define-the-agent-guardrails

### 40. Trailhead: Agentforce: エージェントプランニング / エージェントのガードレールを定義する Q2
- 問題: 自律型 AI のユースケースに付随するリスクと懸念事項を評価する際に役立つフレームワークはどれですか?
- 正解: 人、ビジネス、テクノロジー、データ(a=[3])
- 根拠(ユニット本文・日本語版): 「おそらく多くの組織でお馴染みの「人、ビジネス、テクノロジー、データ」フレームワークを使用することをお勧めします。」
- v: Trailhead のユニット本文で確認 / f: agents
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-agent-planning/define-the-agent-guardrails

### 41. Trailhead: Agentforce: エージェントプランニング / エージェントの作業の概要を定める Q1
- 問題: プロセスマッピングとは何ですか?
- 正解: ビジネスプロセスの手順の視覚表現で、開始から終了までの流れを示す(a=[0])
- 根拠(ユニット本文・日本語版): 「プロセスマッピング はビジネスプロセスの手順の視覚表現で、開始から終了までの流れを示します。」
- v: Trailhead のユニット本文で確認 / f: agents
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-agent-planning/outline-the-agents-work

### 42. Trailhead: Agentforce: エージェントプランニング / エージェントの作業の概要を定める Q2
- 問題: AI エージェントのビジネスプロセスの定義に関する次の文のうち、正しいものはどれですか?
- 正解: ビジネスプロセスを定義できなければ、作業を実行するように AI を設定することは難しい。(a=[2])
- 根拠(ユニット本文・日本語版): 「ご想像のとおり、組織がその作業の進め方を説明できなければ、その作業を実行するように AI エージェントを設定することはほぼ不可能です。」
- v: Trailhead のユニット本文で確認 / f: agents
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-agent-planning/outline-the-agents-work

### 43. Trailhead: Agentforce: エージェントプランニング / エージェントのプロトタイプを作成する Q1
- 問題: 自然言語プロンプトとプログラムロジックの両方が含まれるサブエージェントの要素はどれですか?
- 正解: 指示(a=[2])
- 根拠(ユニット本文・日本語版): 「指示には、プログラムロジック ( Agent Script で記述) と自然言語プロンプトの組み合わせが含まれます。」
- v: Trailhead のユニット本文で確認 / f: agents / x: 「Agent Script(エージェントを作るための言語)で、全体の業務の流れと会話の柔軟さを分けます。決定的なルールとLLMの推論を同じエンジンで組み合わせることを、ハイブリッド推論と呼びます。」
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-agent-planning/prototype-the-agent

### 44. Trailhead: Agentforce: エージェントプランニング / エージェントのプロトタイプを作成する Q2
- 問題: 毎回実行時に一貫した出力を生成する参照アクションはどのように説明されますか?
- 正解: 確定的(a=[1])
- 根拠(ユニット本文・日本語版): 「フローまたは Apex に基づくアクションは確定的で、ビジネスロジックとルールを使用して一貫した結果を生成します。」
- v: Trailhead のユニット本文で確認 / f: agents
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-agent-planning/prototype-the-agent

### 45. Trailhead: Agentforce テストセンター / エージェントを信頼する Q1
- 問題: パフォーマンステストについて最も適切な説明はどれですか?
- 正解: 多数のテストを同時に実行する。(a=[2])
- 根拠(ユニット本文・日本語版): 「Agentforce テストセンターでは、テスト環境で大量のテストを同時に実行することで、パフォーマンステストを行うこともできます。」
- v: Trailhead のユニット本文で確認 / f: testing / x: 「Agentforce Testing Center(テストセンター)は、エージェントに多数のテストケースを一括で投げ、回答や選んだサブエージェント、アクションを自動で評価する機能です。」
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-agent-testing/trust-your-agents

### 46. Trailhead: Agentforce テストセンター / エージェントを信頼する Q2
- 問題: 手動でエージェントのテストとトラブルシューティングを行うのに最適なツールはどれですか?
- 正解: Agentforce Builder(a=[0])
- 根拠(ユニット本文・日本語版): 「Agentforce Builder では、エージェントの作成中や更新中に手動でテストとトラブルシューティングを行うことができます。」
- v: Trailhead のユニット本文で確認 / f: testing / x: 「不合格の発話はAgentforce Builderで手動で再テストし、推論の流れを確認してから、サブエージェントの指示、アクション、ナレッジを直します。」
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-agent-testing/trust-your-agents

### 47. Trailhead: Agentforce テストセンター / テスト結果を確認する Q1
- 問題: [Actual Actions (実際のアクション)] はテスト結果のどの部分を表していますか?
- 正解: エージェントが実行したアクション(a=[2])
- 根拠(ユニット本文・日本語版): 「[Actual Actions (実際のアクション)] にはエージェントがサブエージェントから実行したアクションが表示されます。」
- v: Trailhead のユニット本文で確認 / f: testing
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-agent-testing/view-test-results

### 48. Trailhead: Agentforce テストセンター / テスト結果を確認する Q2
- 問題: Agentforce Builder ではどの種類のテストを実施できますか?
- 正解: 手動テスト(a=[0])
- 根拠(ユニット本文・日本語版): 「このような方法で Agentforce Builder を使用することは手動テストの一種であり、発言を詳しく調べてエージェントが選択したサブエージェント、アクション、応答を確認することができます。」
- v: Trailhead のユニット本文で確認 / f: testing / x: 「不合格の発話はAgentforce Builderで手動で再テストし、推論の流れを確認してから、サブエージェントの指示、アクション、ナレッジを直します。」
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-agent-testing/view-test-results

### 49. Trailhead: Slack にリリースする Agentforce の設定 / Agentforce と Slack が連携するしくみ Q1
- 問題: Slack ユーザーは使用可能なエージェントをどこで参照できますか?
- 正解: Slack の Agentforce ハブ(a=[2])
- 根拠(ユニット本文・日本語版): 「従業員は、Slack の Agentforce ハブでエージェントを見つけたり、自分に関連するエージェントがどのように役立つかを理解したり、より直感的に操作できる提案されたプロンプトを確認したりします。」
- v: Trailhead のユニット本文で確認 / f: channels
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-configuration-for-slack-deployment/learn-how-agentforce-and-slack-work-together

### 50. Trailhead: Slack にリリースする Agentforce の設定 / Agentforce と Slack が連携するしくみ Q2
- 問題: 従業員が Slack の人事エージェントに今年の福利厚生について問い合わせます。エージェントが従業員とやり取りするのに必要なアクションはどれですか?
- 正解: ダイレクトメッセージ (DM) を送信する。(a=[0])
- 根拠(ユニット本文・日本語版): 「エージェントから特定の Slack ユーザーにダイレクトメッセージで通知やメッセージを送信します。」
- v: 要確認 / f: channels
- 要確認の理由: 本文にSlackアクション「Slack ダイレクトメッセージを送信」はあるが、問題の「必要なアクション」を直接示す記述はない。
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-configuration-for-slack-deployment/learn-how-agentforce-and-slack-work-together

### 51. Trailhead: Agentforce データライブラリの基礎 / 実世界のデータで AI をアップグレードする Q1
- 問題: 非構造化データを AI 機能に統合するうえでの主な課題は何ですか?
- 正解: 非構造化データは、検索が容易ではないが、貴重なインサイトが含まれている。(a=[1])
- 根拠(ユニット本文・日本語版): 「エンタープライズデータデータの 90% 近くを占めるこうしたデータは、検索が容易ではありませんが、お客様のフィードバック、認識、意見、口調、センチメントなどの貴重なインサイトが詰まっています。」
- v: Trailhead のユニット本文で確認 / f: datalib
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-data-library-basics/upgrade-ai-with-real-world-data

### 52. Trailhead: Agentforce データライブラリの基礎 / 実世界のデータで AI をアップグレードする Q2
- 問題: ユーザーが Agentforce データライブラリに接続されたエージェントに質問すると、実行時にどのような処理が行われますか?
- 正解: ユーザーのクエリがプロンプトテンプレートに追加され、レトリーバーが最も関連性の高いデータを取得する。(a=[1])
- 根拠(ユニット本文・日本語版): 「実行時には、ユーザーのクエリがプロンプトテンプレートに追加され、関連するデータに接続するレトリーバーを参照します。」
- v: Trailhead のユニット本文で確認 / f: datalib
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-data-library-basics/upgrade-ai-with-real-world-data

### 53. Trailhead: Agentforce データライブラリの基礎 / エージェントのファイルベースライブラリを構築する Q1
- 問題: Agentforce Builder ワークフローでデータライブラリに加えた変更をテストするには、どうしたらよいですか?
- 正解: 会話プレビューを再起動し、エージェントとチャットする。(a=[1])
- 根拠(ユニット本文・日本語版): 「変更をテストするために、まず検索インデックスとデータライブラリの準備が完了したことを確認してから、会話プレビューを再起動します。」
- v: Trailhead のユニット本文で確認 / f: datalib
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-data-library-basics/build-a-file-based-data-library-for-an-agent

### 54. Trailhead: Agentforce データライブラリの基礎 / エージェントのファイルベースライブラリを構築する Q2
- 問題: テスト中にエージェントが応答で使用した情報源を調べたい場合、 どこで見つけることができますか?
- 正解: エージェントの推論ウィンドウ(a=[1])
- 根拠(ユニット本文・日本語版): 「Becca がエージェントの推論を確認すると、データライブラリにアップロードしたファイルが引用されています。」
- v: Trailhead のユニット本文で確認 / f: datalib
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-data-library-basics/build-a-file-based-data-library-for-an-agent

### 55. Trailhead: サービスエージェントのための Agentforce リリース / リリースプロセスについて学ぶ Q1
- 問題: エージェント開発ライフサイクルにおいて、リリースフェーズの主な目標は何ですか?
- 正解: ユーザーがやり取りするチャネルにエージェントを接続する(a=[2])
- 根拠(ユニット本文・日本語版): 「リリース: ユーザーがエージェントとやり取りするチャネルにエージェントを接続します。」
- v: Trailhead のユニット本文で確認 / f: channels
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-deployment-quick-look/learn-about-the-deployment-process

### 56. Trailhead: サービスエージェントのための Agentforce リリース / リリースプロセスについて学ぶ Q2
- 問題: エージェントのリリース戦略を定義する際、どのコンポーネントを含める必要がありますか?
- 正解: ロールアウトプラン、変更管理、ガバナンス(a=[0])
- 根拠(ユニット本文・日本語版): 「変更管理とガバナンスを管理する」
- v: Trailhead のユニット本文で確認 / f: channels
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-deployment-quick-look/learn-about-the-deployment-process

### 57. Trailhead: サービスエージェントのための Agentforce リリース / メッセージング接続を設定する Q1
- 問題: メッセージング接続において、インバウンドのオムニチャネルフローはどのような役割を果たしますか?
- 正解: 新しい会話を AI エージェントに転送する(a=[1])
- 根拠(ユニット本文・日本語版): 「インバウンドフロー: 新しい会話が開始されると、このフローが会話を AI エージェントにルーティングします。」
- v: Trailhead のユニット本文で確認 / f: channels
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-deployment-quick-look/set-up-the-messaging-connection

### 58. Trailhead: サービスエージェントのための Agentforce リリース / メッセージング接続を設定する Q2
- 問題: Escalation (エスカレーション) サブエージェントはいつ AI エージェントからサービス担当者へのハンドオフをトリガーしますか?
- 正解: エージェントの範囲外の要求など、顧客にサービス担当者が必要だと指示が判断したとき(a=[2])
- 根拠(ユニット本文・日本語版): 「Agentforce サービスエージェントは、 エスカレーションサブエージェントとアウトバウンドのオムニチャネルフロー を使用して、会話をサービス担当者やキューなどの宛先にエスカレーションします。」
- v: 要確認 / f: channels
- 要確認の理由: 本文のEscalationサブエージェントの説明から推定。
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-deployment-quick-look/set-up-the-messaging-connection

### 59. Trailhead: サービスエージェントのための Agentforce リリース / メッセージング接続を Web サイトにリリースする Q1
- 問題: 事前チャットフォームでできることは何ですか?
- 正解: 会話が始まる前に顧客の詳細を収集し、既存の Salesforce レコードを見つけようと試みる(a=[3])
- 根拠(ユニット本文・日本語版): 「事前チャットフォームは、会話が始まる前に顧客の名前やメールアドレスなどの詳細情報をいくつか収集するため、エージェントはある程度のコンテキストを持った状態で対応を開始できます。」
- v: Trailhead のユニット本文で確認 / f: channels
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-deployment-quick-look/deploy-the-messaging-connection-to-a-website

### 60. Trailhead: サービスエージェントのための Agentforce リリース / メッセージング接続を Web サイトにリリースする Q2
- 問題: Experience Cloud サイトのドメインを CORS 許可リストに追加する必要があるのはなぜですか?
- 正解: Salesforce がサイトのドメインを信頼して呼び出せるようにするため(a=[2])
- 根拠(ユニット本文・日本語版): 「また、Salesforce がヘルプサイトからの呼び出しを信頼できるように、サイトを CORS 許可リストに追加する作業も忘れずに行います。」
- v: Trailhead のユニット本文で確認 / f: channels
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-deployment-quick-look/deploy-the-messaging-connection-to-a-website

### 61. Trailhead: サービスエージェントのための Agentforce リリース / 音声接続のセットアップ Q1
- 問題: Agentforce Voice は何をしますか?
- 正解: サービスエージェント向けの音声ベースの会話型 AI を有効にする(a=[0])
- 根拠(ユニット本文・日本語版): 「Agentforce Voice は、顧客とサービスエージェントの間で自然な音声ベースの会話型 AI を実現します。」
- v: Trailhead のユニット本文で確認 / f: channels
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-deployment-quick-look/set-up-the-voice-connection

### 62. Trailhead: サービスエージェントのための Agentforce リリース / 音声接続のセットアップ Q2
- 問題: PSTN 音声チャネルを設定する場合、関連付けられる電話番号はどれですか?
- 正解: [Live (ライブ)] の状況の番号のみ。各番号は 1 つのチャネルにのみ使用できる(a=[2])
- 根拠(ユニット本文・日本語版): 「[Live (ライブ)] の状況の番号のみドロップダウンに表示され、各番号は 1 つのチャネルにのみ関連付けることができます。」
- v: Trailhead のユニット本文で確認 / f: channels
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-deployment-quick-look/set-up-the-voice-connection

### 63. Trailhead: サービスエージェントのための Agentforce リリース / エージェントを本番環境にリリースする Q1
- 問題: サービスエージェントを本番組織にリリースする前の前提条件として正しいものはどれですか?
- 正解: 適切なプロファイルと権限を持つ専用のエージェントユーザー(a=[1])
- 根拠(ユニット本文・日本語版): 「エージェントユーザー: サービスエージェントは専用のエージェントユーザーとして動作します。これは Salesforce インテグレーションユーザーであり、そのプロファイルと権限によって、エージェントが顧客チャネルでアクセスできる内容が制御されます。」
- v: Trailhead のユニット本文で確認 / f: deploy
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-deployment-quick-look/deploy-an-ai-agent-with-agentforce

### 64. Trailhead: サービスエージェントのための Agentforce リリース / エージェントを本番環境にリリースする Q2
- 問題: Sandbox からエージェントのメタデータを取得して対象組織にリリースするには、何を使用しますか?
- 正解: Salesforce CLI(a=[3])
- 根拠(ユニット本文・日本語版): 「Salesforce CLI を使用して Sandbox 組織から 最新のメタデータを取得 し、エージェント用のパッケージファイルを生成します。」
- v: Trailhead のユニット本文で確認 / f: deploy / x: 「メタデータでの移行(API v68以降)Winter ’27 からの AiAgentDefinition と AiAgentDefinitionVersion を使うと、Salesforce CLI がエージェントと依存関係をまとめて取得する。移行元と移行先の両方が v68 であることが条件」
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-deployment-quick-look/deploy-an-ai-agent-with-agentforce

### 65. Trailhead: Agentforce を使用した設定: クイックルック / Agentforce を使用した設定について知る Q1
- 問題: 「Agentforce を使用した設定」をシステム管理者が利用する主なメリットは何ですか?
- 正解: タスクが簡潔になり、反復作業が減るため、生産性が向上する。(a=[3])
- 根拠(ユニット本文・日本語版): 「エージェントドリブンのこのエクスペリエンスでは、タスクが簡潔になり、反復作業が減るため、システム管理者の生産性が向上します。」
- v: Trailhead のユニット本文で確認 / f: stdagents
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-for-setup-quick-look/get-to-know-setup-with-agentforce

### 66. Trailhead: Agentforce を使用した設定: クイックルック / Agentforce を使用した設定について知る Q2
- 問題: [Setup (設定)] のタスクのうち、Agentforce がその実行をサポートできるものはどれですか?
- 正解: ユーザーがレコードにアクセスできない原因をトラブルシューティングする。(a=[0])
- 根拠(ユニット本文・日本語版): 「オブジェクト、項目、レコードへのユーザーアクセスの問題のトラブルシューティング」
- v: Trailhead のユニット本文で確認 / f: stdagents
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-for-setup-quick-look/get-to-know-setup-with-agentforce

### 67. Trailhead: Salesforce モバイルアプリケーションの Agentforce: クイックルック / Salesforce モバイルアプリケーションで Agentforce を使用して時間を節約する Q1
- 問題: Agentforce が Salesforce モバイルアプリケーションで動作するには、どのようなステップを追加で実行する必要がありますか?
- 正解: 何も行わない。Agentforce の設定時にすべて完了している。(a=[1])
- 根拠(ユニット本文・日本語版): 「Salesforce モバイルアプリケーションのために追加で行う必要のある Agentforce 設定はありません。」
- v: Trailhead のユニット本文で確認 / f: channels
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-on-the-salesforce-mobile-app-quick-look/save-time-with-agentforce-on-the-salesforce-mobile-app

### 68. Trailhead: Salesforce モバイルアプリケーションの Agentforce: クイックルック / Salesforce モバイルアプリケーションで Agentforce を使用して時間を節約する Q2
- 問題: iOS デバイス上の Agentforce で音声制御を有効化するにはどうすればよいですか?
- 正解: 音声認識とマイクロフォンへのアクセス権を付与する。(a=[2])
- 根拠(ユニット本文・日本語版): 「入力するのが面倒な場合は、 マイクロフォンのアイコンをタップして (アプリケーションに音声認識とマイクロフォンへのアクセス権を付与していない場合は付与してください)、Agentforce に実行して欲しいことを伝えることもできます。」
- v: Trailhead のユニット本文で確認 / f: channels
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-on-the-salesforce-mobile-app-quick-look/save-time-with-agentforce-on-the-salesforce-mobile-app

### 69. Trailhead: サービス向け Agentforce / サービス向け Agentforce 入門 Q1
- 問題: 正誤問題: Agentforce for Service は、カスタマーチャネルで自律的に動作するが、断定的なダイアログになりがちである。
- 正解: 誤り(a=[1])
- 根拠(ユニット本文・日本語版): 「硬直かつ断定的なダイアログになりがちな従来のチャットボットとは異なり、こうした自律型エージェントは生成 AI を使用して、セルフサービスポータルやメッセージングチャネルの全域で 24 時間稼働し、タスクを処理して判断を下し、ブランド設定を反映した自然な応答で対応します。」
- v: Trailhead のユニット本文で確認 / f: stdagents
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-service-agent-quick-look/get-started-with-agentforce-service-agent

### 70. Trailhead: サービス向け Agentforce / サービス向け Agentforce 入門 Q2
- 問題: 次のうち、自律型エージェントと従来のボットとの違いについての最も適切な説明はどれですか?
- 正解: 自律型エージェントは判断を下し、生成 AI を使用してコンテキストを理解したうえで応答を作成する。(a=[2])
- 根拠(ユニット本文・日本語版): 「自然な会話で返答: 生成 AI を使用してコンテキストを理解し、ブランドのボイスを反映した会話形式の応答を作成します。」
- v: Trailhead のユニット本文で確認 / f: stdagents
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-service-agent-quick-look/get-started-with-agentforce-service-agent

### 71. Trailhead: サービス向け Agentforce / サービス向け Agentforce のユースケースを確認する Q1
- 問題: エージェントのカスタムサブエージェントとアクションを作成する主なメリットは何ですか?
- 正解: エージェントが操作の精度を高めて効率的に作業を完了したり、会社のブランドやボイスに合致する応答を提示したりできるようになる。(a=[1])
- 根拠(ユニット本文・日本語版): 「標準サブエージェントやアクションは有用で編集可能ですが、お客様にエンゲージしたり、タスクを完了したり、ブランドやトーンに合致する応答を提示したりするために、さらにパーソナライズされたアプローチが必要な場合にはどうすればよいのでしょうか? このような場合には、カスタムサブエージェントやアクションを作成することが極めて重要です。」
- v: Trailhead のユニット本文で確認 / f: stdagents
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-service-agent-quick-look/explore-use-cases-for-agentforce-for-service

### 72. Trailhead: サービス向け Agentforce / サービス向け Agentforce のユースケースを確認する Q2
- 問題: 正誤問題: サービス向け Agentforce は、カスタムと標準の両方のサブエージェントやアクションを同時にサポートできる。
- 正解: 正しい(a=[0])
- 根拠(ユニット本文・日本語版): 「Agentforce ではサブエージェント、アクション、指示が連携して、どのやり取りでも最適な応答を提示できるようにします。」
- v: Trailhead のユニット本文で確認 / f: stdagents
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-service-agent-quick-look/explore-use-cases-for-agentforce-for-service

### 73. Trailhead: サービス向け Agentforce / サービス向け Agentforce でナレッジを使用する Q1
- 問題: Agentforce データライブラリは、どのようなデータソースをサポートしていますか?
- 正解: A と C(a=[3])
- 根拠(ユニット本文・日本語版): 「データライブラリでは、ナレッジ記事 (レコードと項目)、アップロードされたファイル、ウェブ検索、カスタムリトリーバーがすべてサポートされています。」
- v: Trailhead のユニット本文で確認 / f: stdagents
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-service-agent-quick-look/use-knowledge-in-agentforce-for-service

### 74. Trailhead: サービス向け Agentforce / サービス向け Agentforce でナレッジを使用する Q2
- 問題: 非構造化データの処理に Agentforce データライブラリを統合する主なメリットは何ですか?
- 正解: 非構造化データと構造化データの自動インデックス付けが可能になり、迅速で正確な応答が実現する。(a=[1])
- 根拠(ユニット本文・日本語版): 「Agentforce にデータライブラリを追加すると、Salesforce が RAG を利用したソリューションを自動的に構築し、ナレッジ記事や PDF から非構造化データ (と構造化データ) を取得します。」
- v: Trailhead のユニット本文で確認 / f: stdagents
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-service-agent-quick-look/use-knowledge-in-agentforce-for-service

### 75. Trailhead: Agentforce サービスアシスタント / サービスアシスタントを準備する Q1
- 問題: サービス担当者が作業負荷をより効果的に管理するのに役立つ、サービスアシスタントの主要な機能はどれですか?
- 正解: ケースに対して迅速なサマリーとステップバイステップの解決ガイダンスを提供する。(a=[2])
- 根拠(ユニット本文・日本語版): 「Lightning Web コンポーネントとして、サービス担当者にケースサマリーと、サービスプランと呼ばれるステップバイステップの解決ガイダンスを迅速に提供します。」
- v: Trailhead のユニット本文で確認 / f: stdagents / x: 「Service Assistantサービス担当者に、ケースの要約と解決までの手順を示す」
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-service-assistant/plan-for-service-assistant

### 76. Trailhead: Agentforce サービスアシスタント / サービスアシスタントを準備する Q2
- 問題: サービスアシスタントのグラウンディングが重要なのはなぜですか?
- 正解: サービスアシスタントが会社のサービスポリシーとプラクティスに準拠するようにするから。(a=[2])
- 根拠(ユニット本文・日本語版): 「なぜなら、サービスアシスタントは Coral Cloud 独自のデータを使用して、サービスポリシーと基準に完全に一致するサービスプランを作成するからです。」
- v: Trailhead のユニット本文で確認 / f: stdagents
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-service-assistant/plan-for-service-assistant

### 77. Trailhead: Agentforce サービスアシスタント / サービスアシスタントをテストする Q1
- 問題: ケースを最初に開くと、サービスアシスタントはサービス担当者に何を提供しますか?
- 正解: ケースサマリーとサマリー手順(a=[3])
- 根拠(ユニット本文・日本語版): 「変更が保存されると、サービスアシスタントが動作を開始し、ケースサマリーとサマリー手順を作成します。」
- v: Trailhead のユニット本文で確認 / f: stdagents / x: 「Service Assistantサービス担当者に、ケースの要約と解決までの手順を示す」
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-service-assistant/test-service-assistant

### 78. Trailhead: Agentforce サービスアシスタント / サービスアシスタントをテストする Q2
- 問題: [Help with Travel Documentation (渡航書類の支援)] ケースページを開くと、サービスアシスタントがサマリーとサマリー手順を生成していることに気付きました。このケースについて、より詳細なステップバイステップの解決ガイドを表示するにはどうすればよいですか?
- 正解: サービスアシスタントコンポーネントで [Draft Plan (プランのドラフトを作成)] ボタンをクリックする。(a=[2])
- 根拠(ユニット本文・日本語版): 「サービスアシスタントコンポーネントで、 [Draft Plan (プランのドラフトを作成)] をクリックし、サービスプランを確認します。」
- v: Trailhead のユニット本文で確認 / f: stdagents
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-service-assistant/test-service-assistant

### 79. Trailhead: Agentforce のテストツールと計画 / エージェントのテストツールと考慮事項を確認する Q1
- 問題: エージェントのテストが「確率的」と考えられ、従来のアプリケーションのテストよりも予測しにくいのはなぜですか?
- 正解: 生成 AI にはルールに基づくロジックが欠けているため、さまざまな、ときには驚くような応答を返すことがあるから。(a=[2])
- 根拠(ユニット本文・日本語版): 「つまり、生成 AI にはルールに基づくロジックが欠けているため、予測しにくく、ユニークで、ときには驚くような結果になることがあります。」
- v: Trailhead のユニット本文で確認 / f: testing
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-testing-tools-and-strategies/explore-agent-testing-tools-and-considerations

### 80. Trailhead: Agentforce のテストツールと計画 / エージェントのテストツールと考慮事項を確認する Q2
- 問題: エージェントが応答を生成するために通ったサブエージェント、アクション、指示のパスは、Agentforce Builder のどこで確認できますか?
- 正解: プランキャンバス(a=[2])
- 根拠(ユニット本文・日本語版): 「一括テストを実行すると、結果にはテストされた入力内容のほかに、予期されるサブエージェントとアクション、実際にコールされたトピックとアクション、予期される応答、各入力が合格か不合格かが表示されます。テスト入力が不合格となった理由を詳しく知りたい場合は、Agentforce Builder の [Preview (プレビュー)] パネルに入力内容をコピーして貼り付けると、プランキャンバスでエージェントが不合格の応答に至るまでに通ったパスを確認できます。」
- v: Trailhead のユニット本文で確認 / f: testing
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-testing-tools-and-strategies/explore-agent-testing-tools-and-considerations

### 81. Trailhead: Agentforce のテストツールと計画 / 5 ステップのテスト計画を使用してエージェントを調整する Q1
- 問題: テストのシナリオに基づいて、Maria が本格稼働前に包括的なテスト計画を採用する最も重要な理由は何ですか?
- 正解: ユーザーがエージェントとやり取りする予測可能なさまざまな方法に対応するため。(a=[2])
- 根拠(ユニット本文・日本語版): 「エージェントを徹底的にテストするには、あらゆる種類の入力に対応できるよう、多数のシナリオを用意する必要があります。」
- v: Trailhead のユニット本文で確認 / f: testing
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-testing-tools-and-strategies/refine-your-agents-using-a-five-step-testing-strategy

### 82. Trailhead: Agentforce のテストツールと計画 / 5 ステップのテスト計画を使用してエージェントを調整する Q2
- 問題: テストスイート (ベータ) で Global Stay Resorts エージェントの一括テストを実行したところ、Maria はいくつかのテストが失敗しているのを確認しました。5 ステップ計画によれば、失敗したテストに対処し、エージェントをさらに改善するために Maria が取るべき次の論理的なステップは何ですか?
- 正解: テスト結果を確認し、テストが失敗した原因を理解するために人間による検証を行う。(a=[2])
- 根拠(ユニット本文・日本語版): 「生成されたテストは多くのシナリオに対応し、合格か不合格かを判定しますが、ユーザーがエージェントとどのようにやり取りするか、エージェントが期待どおりに応答しているか、有害または望ましくない結果を生み出していないかを確認するために、人間によるレビューを行うことが重要です。」
- v: Trailhead のユニット本文で確認 / f: testing
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-testing-tools-and-strategies/refine-your-agents-using-a-five-step-testing-strategy

### 83. Trailhead: Agentforce Voice / Agentforce Voice の概要 Q1
- 問題: Agentforce Voice の主な機能は何ですか?
- 正解: AI エージェントが顧客を理解し、会話できるようにする(a=[1])
- 根拠(ユニット本文・日本語版): 「Agentforce Voice は、お客様とサービスエージェントの間の音声ベースの自然なやり取りを可能にする会話型 AI 機能です。」
- v: Trailhead のユニット本文で確認 / f: channels
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-voice-quick-look/meet-agentforce-voice

### 84. Trailhead: Agentforce Voice / Agentforce Voice の概要 Q2
- 問題: テレフォニーオプションを比較する場合、コンテキストの保持に関して Salesforce Voice (ネイティブテレフォニー) の主な利点は何ですか?
- 正解: 最初から最後までの会話全体のトランスクリプトが含まれた 1 つの完全なレコードが維持される。(a=[2])
- 根拠(ユニット本文・日本語版): 「コンテキストの保持: 転送時も含め、やり取り全体で、完全な通話トランスクリプトやセッションコンテキストが保持されます。」
- v: Trailhead のユニット本文で確認 / f: channels
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-voice-quick-look/meet-agentforce-voice

### 85. Trailhead: Agentforce Voice / 音声対応エージェントを作成する Q1
- 問題: カスタマーサービスの着信通話を処理するための新しいエージェントを作成する場合、どのテンプレートを選択しますか?
- 正解: Agentforce Service エージェント(a=[0])
- 根拠(ユニット本文・日本語版): 「[Agentforce Service Agent (Agentforce Service エージェント)] テンプレートを選択します。」
- v: Trailhead のユニット本文で確認 / f: channels
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-voice-quick-look/build-your-voice-enabled-agent

### 86. Trailhead: Agentforce Voice / 音声対応エージェントを作成する Q2
- 問題: 会社独自の用語をエージェントが正しく発音するようにするには、どのツールを使用できますか?
- 正解: 発音辞書(a=[3])
- 根拠(ユニット本文・日本語版): 「また、エージェントがキーワードやキーフレーズをどのように発音するかを正確に指定するために、発音辞書を定義することもできます。」
- v: Trailhead のユニット本文で確認 / f: channels
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-voice-quick-look/build-your-voice-enabled-agent

### 87. Trailhead: Agentforce Voice / 着信通話ルーティングを管理する Q1
- 問題: 音声通話を転送する新しいオムニチャネルフローを作成する場合、音声通話レコード ID を保存するためにどのリソースを作成する必要がありますか?
- 正解: API 参照名が recordId で、データ型がテキストの変数(a=[1])
- 根拠(ユニット本文・日本語版): 「API 参照名: recordId」
- v: Trailhead のユニット本文で確認 / f: channels
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-voice-quick-look/manage-inbound-call-routing-agenforce-voice

### 88. Trailhead: Agentforce Voice / 着信通話ルーティングを管理する Q2
- 問題: 着信音声ルーティングフローを実装中の顧客が、通話が Agentforce Service エージェントに転送されていないことに気付きました。フローを電話番号にリンクする前に [Setup (設定)] メニューで完了する必要がある一般的な前提条件は何ですか?
- 正解: [Communication Channels (コミュニケーションチャネル)] の下の特定の音声チャネル内でフローを対応付ける必要がある。(a=[3])
- 根拠(ユニット本文・日本語版): 「[Setup (設定)] の [Quick Find (クイック検索)] ボックスで [Communication Channels (コミュニケーションチャネル)] を検索して選択します。」
- v: Trailhead のユニット本文で確認 / f: channels
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/agentforce-voice-quick-look/manage-inbound-call-routing-agenforce-voice

### 89. Trailhead: データ + AI + CRM: クイックルック / データ + AI + CRM が連携するしくみを学習する Q1
- 問題: 次のうち、マーケティングでの AI の活用法の一例はどれですか?
- 正解: 顧客用のカスタムランディングページを作成する。(a=[3])
- 根拠(ユニット本文・日本語版): 「過去の購入履歴や閲覧履歴など CRM の e コマースデータを AI で分析して、顧客の興味に基づいたカスタムランディングページを生成できます。」
- v: Trailhead のユニット本文で確認 / f: d360ai
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/ai-data-crm-quick-look/learn-how-ai-data-crm-work-together

### 90. Trailhead: データ + AI + CRM: クイックルック / データ + AI + CRM が連携するしくみを学習する Q2
- 問題: 成功する AI 戦略の基盤を築くのは何ですか?
- 正解: 信頼(a=[1])
- 根拠(ユニット本文・日本語版): 「信頼を築く: 信頼は成功する AI 戦略の基盤となります。」
- v: Trailhead のユニット本文で確認 / f: d360ai
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/ai-data-crm-quick-look/learn-how-ai-data-crm-work-together

### 91. Trailhead: 自律型エージェント / 自律型エージェントについて知る Q1
- 問題: 自律型エージェントの主な機能は何ですか?
- 正解: 時間とリソースを節約し、カスタマーエクスペリエンスを向上させること(a=[1])
- 根拠(ユニット本文・日本語版): 「この結果、カスタマーエクスペリエンスが向上するだけでなく、ビジネスが膨大な時間を節約し、カスタマーサービスを一層充実させるための極めて重要なタスクに注力できます。」
- v: Trailhead のユニット本文で確認 / f: agents
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/autonomous-agents/get-to-know-autonomous-agents

### 92. Trailhead: 自律型エージェント / 自律型エージェントについて知る Q2
- 問題: 次の機能のうち、自律型エージェントとチャットボットを区別するものはどれですか?
- 正解: 自律型エージェントはタスクを独立して実行できる。(a=[3])
- 根拠(ユニット本文・日本語版): 「自律型エージェントがタスクを遂行するのに人間の助けは必要ありませんが、達成してもらいたい目標と主な目的を説明する必要があります。」
- v: Trailhead のユニット本文で確認 / f: agents
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/autonomous-agents/get-to-know-autonomous-agents

### 93. Trailhead: 自律型エージェント / 自律型エージェントと信頼関係を確立する Q1
- 問題: 次のうち、自律型エージェントを構築して統合する際に検討すべき重要なガードレールはどれですか?
- 正解: 複雑なやり取りや機密性の高い取引には人間による監視を実施する。(a=[1])
- 根拠(ユニット本文・日本語版): 「自律型エージェントはさまざまなタスクを独立して処理しますが、複雑なやり取りや機密性の高い取引については人間の監視を実施することが重要です。」
- v: Trailhead のユニット本文で確認 / f: agents
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/autonomous-agents/establish-trust-with-autonomous-agents

### 94. Trailhead: 自律型エージェント / 自律型エージェントと信頼関係を確立する Q2
- 問題: お客様とやり取りする自律型エージェントをリリースするときは、何に対して透明性を確保することが重要ですか?
- 正解: 顧客が自律型エージェントとどのように、いつやり取りしているか(a=[0])
- 根拠(ユニット本文・日本語版): 「お客様が自律型エージェントとやり取りしているときはそのことを伝え、必要に応じて人間の担当者と話すことを選択できるようにします。」
- v: Trailhead のユニット本文で確認 / f: agents
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/autonomous-agents/establish-trust-with-autonomous-agents

### 95. Trailhead: 自律型エージェント / 自律型エージェントでビジネストランスフォーメーションを実現する Q1
- 問題: カスタマーサポートで自律型エージェントを使用する主なメリットは何ですか?
- 正解: 人間の担当者が複雑な問題に集中して取り組める。(a=[1])
- 根拠(ユニット本文・日本語版): 「カスタマーサポート: シンプルな FAQ から、複雑ながら人間の監視は必要としない問題まで、お客様からの幅広い問い合わせに対応できます。このため、担当者は人間ならではの対応が必要となる厄介な事案に専念できます。」
- v: Trailhead のユニット本文で確認 / f: agents
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/autonomous-agents/transform-your-business-with-autonomous-agents

### 96. Trailhead: 自律型エージェント / 自律型エージェントでビジネストランスフォーメーションを実現する Q2
- 問題: Agentforce が会社のデータを保護し、有害性を検出することを保証するものは何ですか?
- 正解: Einstein Trust Layer(a=[1])
- 根拠(ユニット本文・日本語版): 「Einstein Trust Layer は、セキュアなゲートウェイを使用し、データ保持ゼロ協定に従って会社のデータを保護します。」
- v: Trailhead のユニット本文で確認 / f: agents
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/autonomous-agents/transform-your-business-with-autonomous-agents

### 97. Trailhead: Data 360 Sandbox / Data 360 Sandbox を設定する Q1
- 問題: Jamal が Cloud Kicks の本番組織で直接テストするのではなく、Data 360 Sandbox を使用するのはなぜですか?
- 正解: ライブ本番データに影響を与えることなく、安全に設定を構築およびテストするため(a=[1])
- 根拠(ユニット本文・日本語版): 「ライブ環境で Data 360 の設定をテストすることは、特に何百万件もの顧客データを管理している場合、リスクを伴います。」
- v: Trailhead のユニット本文で確認 / f: deploy
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/data-360-sandboxes/set-up-your-data-360-sandbox

### 98. Trailhead: Data 360 Sandbox / Data 360 Sandbox を設定する Q2
- 問題: Data 360 Sandbox を作成する最初のプロセスはどこから始まりますか?
- 正解: 本番環境の [Setup (設定)] メニュー(a=[0])
- 根拠(ユニット本文・日本語版): 「本番環境から Data 360 Sandbox インスタンスをプロビジョニングする。」
- v: Trailhead のユニット本文で確認 / f: deploy
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/data-360-sandboxes/set-up-your-data-360-sandbox

### 99. Trailhead: Data 360 Sandbox / Data 360 Sandbox を更新して同期する Q1
- 問題: Data 360 Sandbox を更新した場合の主な結果は何ですか?
- 正解: Sandbox のメタデータが本番組織の現在の状態と一致するように更新される。(a=[1])
- 根拠(ユニット本文・日本語版): 「メタデータの同期: Sandbox を更新すると、データストリーム、計算済みインサイト、セグメントを含むすべての Data 360 設定がコピーされます。」
- v: Trailhead のユニット本文で確認 / f: deploy / x: 「Data 360 の Sandboxメタデータだけが複製され、データはコピーされない(Partial Copy や Full Copy でも同じ)。接続の認証情報も複製されないので、Sandbox で設定し直す」
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/data-360-sandboxes/refresh-and-synchronize-your-data-360-sandbox

### 100. Trailhead: Data 360 Sandbox / Data 360 Sandbox を更新して同期する Q2
- 問題: Vijay が更新後に不要になった孤立したメタデータを削除するには、どのツールを使用すればよいですか?
- 正解: Data 360 設定のクリーンアッププロセス(a=[1])
- 根拠(ユニット本文・日本語版): 「古いメタデータをクリーンアップする: [Data Cloud Setup (Data Cloud 設定)] メニューを使用して、同期中に発生した孤立したデータストリームやマッピングエラーを特定し、削除します。」
- v: Trailhead のユニット本文で確認 / f: deploy
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/data-360-sandboxes/refresh-and-synchronize-your-data-360-sandbox

### 101. Trailhead: Data 360 Sandbox / Data 360 の設定を DevOps データキットにバンドルする Q1
- 問題: Data 360 の展開ライフサイクルにおける DevOps データキットの主な機能は何ですか?
- 正解: 複数の Data 360 設定を 1 つの移植可能なリリース成果物にバンドルする。(a=[1])
- 根拠(ユニット本文・日本語版): 「DevOps データキットを使用すると、Data 360 コンポーネントを 1 つのユニットにバンドルし、環境間で繰り返し可能で、監査可能かつ安全な昇格を実現できます。」
- v: Trailhead のユニット本文で確認 / f: deploy
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/data-360-sandboxes/bundle-data-360-configurations-into-a-devops-data-kit

### 102. Trailhead: Data 360 Sandbox / Data 360 の設定を DevOps データキットにバンドルする Q2
- 問題: DevOps データキットにバンドルできる 3 つの Data 360 コアコンポーネントはどれですか?
- 正解: データストリーム、計算済みインサイト、ID 解決ルール(a=[3])
- 根拠(ユニット本文・日本語版): 「Data 360 の Sandbox で作業する場合、いくつかのコアメタデータコンポーネントをデータキットにバンドルできます。」
- v: Trailhead のユニット本文で確認 / f: deploy
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/data-360-sandboxes/bundle-data-360-configurations-into-a-devops-data-kit

### 103. Trailhead: Data 360 Sandbox / Data 360 設定を展開して検証する Q1
- 問題: データキットを展開した後、CRM データストリームの展開に失敗した場合、何をする必要がありますか?
- 正解: 対象の組織でコネクタを有効化してから、データキットを再度展開する。(a=[1])
- 根拠(ユニット本文・日本語版): 「CRM データストリームが失敗した場合は、まず対象組織でコネクタを手動で有効化し、その後データキットを再度展開する必要があります。」
- v: Trailhead のユニット本文で確認 / f: deploy
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/data-360-sandboxes/deploy-and-validate-your-data-360-configurations

### 104. Trailhead: Data 360 Sandbox / Data 360 設定を展開して検証する Q2
- 問題: Sandbox から移行した ID 解決ルールが本番環境で意図したとおりに機能していることを、アーキテクトはどのように確認できますか?
- 正解: ルールセットを手動で実行した後にメトリクスをレビューし、サンプルテストプロファイルを監査する。(a=[3])
- 根拠(ユニット本文・日本語版): 「[Metrics (メトリクス)] セクションを監視します。処理された入力レコードの数と、結果として生成された統合プロファイルが、想定される許容範囲内であることを確認します。」
- v: Trailhead のユニット本文で確認 / f: deploy
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/data-360-sandboxes/deploy-and-validate-your-data-360-configurations

### 105. Trailhead: Data 360 を活用した Agentforce / Data 360 と Agentforce について検討する Q1
- 問題: Data 360 の堅牢なデータ基盤にアクセスするためには、どの手順に従う必要がありますか?
- 正解: Data 360 を実装するためにプロビジョニングして有効にしてから、データを接続して変換し、マッピングする。(a=[3])
- 根拠(ユニット本文・日本語版): 「実装 は、組織で Data 360 を有効にして、データを接続し、データモデルにマッピングしているということです。さらに、ID 解決ルールセットを実行してデータをハーモナイズし、Data 360 のその他の機能を設定している場合もあります。」
- v: Trailhead のユニット本文で確認 / f: d360ai
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/data-cloud-powered-agentforce/explore-data-cloud-and-agentforce

### 106. Trailhead: Data 360 を活用した Agentforce / Data 360 と Agentforce について検討する Q2
- 問題: Data 360 の一元化された Customer 360 データがエージェントにとって有益なのはなぜですか?
- 正解: エージェントが、お客様のアクションとコンテキスト全体を考慮してパーソナライズした応答を示すことができるため(a=[1])
- 根拠(ユニット本文・日本語版): 「エージェントは、一般的あるいは断片的な応答ではなく、会社全体に対するお客様の行動を考慮してパーソナライズされた応答を示すことができます。」
- v: Trailhead のユニット本文で確認 / f: d360ai
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/data-cloud-powered-agentforce/explore-data-cloud-and-agentforce

### 107. Trailhead: Data 360 を活用した Agentforce / Data 360 を使用して信頼できるエージェントを実現する Q1
- 問題: 検索拡張生成 (RAG) に Agentforce データライブラリ (ADL) を使用する場合と、フルカスタマイズが可能な Data 360 設定を使用する場合の主な違いは何ですか?
- 正解: ADL が事前構成されたクイックスタートソリューションであるのに対し、カスタマイズ可能な設定ではデータの取り込みや処理を細かく管理できる。(a=[0])
- 根拠(ユニット本文・日本語版): 「Agentforce データライブラリ (ADL) は、事前構成された RAG のクイックスタートソリューションで、 エージェントが個人的に使用する整理されたデータソースです。」
- v: Trailhead のユニット本文で確認 / f: d360ai
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/data-cloud-powered-agentforce/enable-trusted-agents-with-data-cloud

### 108. Trailhead: Data 360 を活用した Agentforce / Data 360 を使用して信頼できるエージェントを実現する Q2
- 問題: 次のうち、Data 360 を活用した生成 AI 監査とフィードバック履歴の主な機能はどれですか?
- 正解: 各応答に対する上向き親指と下向き親指の反応や安全スコアなどのフィードバックデータをログに記録する。(a=[1])
- 根拠(ユニット本文・日本語版): 「フィードバック API を使用して、エージェントの応答に関するフィードバックをログに記録できます。」
- v: Trailhead のユニット本文で確認 / f: d360ai
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/data-cloud-powered-agentforce/enable-trusted-agents-with-data-cloud

### 109. Trailhead: Data 360 を活用した Agentforce / Agentforce に Data 360 を実装する Q1
- 問題: NTO の例を参考に、Agentforce プロジェクトのデータを準備する正しい手順はどれですか?
- 正解: データストリームを作成し、一括処理データ変換を使用してから、ID 解決ルールセットを実行する。(a=[3])
- 根拠(ユニット本文・日本語版): 「Pia は一括処理データ変換を使用して、名前や形式の不一致といったデータの問題を解決します。変換されたデータは、クリーンアップ済みケース DLO に保存されます。」
- v: Trailhead のユニット本文で確認 / f: d360ai
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/data-cloud-powered-agentforce/implement-data-cloud-for-agentforce

### 110. Trailhead: Data 360 を活用した Agentforce / Agentforce に Data 360 を実装する Q2
- 問題: データを準備した後で、Data 360 で一元化されたデータや変換されたデータを基盤にエージェントを作成する正しい手順はどれですか?
- 正解: 検索インデックスを作成し、レトリーバーをコールするプロンプトテンプレートを作成してから、そのプロンプトテンプレートを使用するエージェントアクションを作成する。(a=[2])
- 根拠(ユニット本文・日本語版): 「この 2 つのインデックスは、エージェントの RAG に活用します。Data 360 で自動的に各インデックスのレトリーバーが作成されます。このレトリーバーは、検索インデックスとプロンプトテンプレート間のブリッジとして機能します。」
- v: Trailhead のユニット本文で確認 / f: d360ai
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/data-cloud-powered-agentforce/implement-data-cloud-for-agentforce

### 111. Trailhead: Data 360 を駆使したエクスペリエンス / Data 360 のしくみを学習する Q1
- 問題: Data 360 は、データを統合して個人の統合プロファイルを作成する際に、どれを使用しますか?
- 正解: ID 解決ルールセット(a=[2])
- 根拠(ユニット本文・日本語版): 「ID 解決ルールセットでデータを統合します。」
- v: Trailhead のユニット本文で確認 / f: d360ai
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/data-cloud-powered-experiences/learn-how-data-cloud-works

### 112. Trailhead: Data 360 を駆使したエクスペリエンス / Data 360 のしくみを学習する Q2
- 問題: 顧客は Customer 360 アプリケーションで Data 360 のデータをどのように活用できますか?
- 正解: B と C(a=[4])
- 根拠(ユニット本文・日本語版): 「そして、これらのデータアクションは、イベント、ストリーミングインサイト、あるいはデータの変更によってフローをトリガーします。」
- v: Trailhead のユニット本文で確認 / f: d360ai
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/data-cloud-powered-experiences/learn-how-data-cloud-works

### 113. Trailhead: Data 360 を駆使したエクスペリエンス / Data 360 の活用例を見る Q1
- 問題: 次の回答のうち、優れた倫理的ベストプラクティスの例ではないものはどれですか?
- 正解: 全ユーザーに機密データへのアクセスを付与する(a=[2])
- 根拠(ユニット本文・日本語版): 「提供されるデータに見合う価値提供を約束すること、本当に必要なデータのみを収集すること、そして機密データを慎重に取り扱うことなど、Data 360 の使用を開始する前に倫理的なベストプラクティスを理解しておくことが重要です。」
- v: Trailhead のユニット本文で確認 / f: d360ai
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/data-cloud-powered-experiences/see-data-cloud-in-action

### 114. Trailhead: Data 360 を駆使したエクスペリエンス / Data 360 の活用例を見る Q2
- 問題: 営業担当が連絡しようとしている顧客について詳しく知るために役立つユースケースはどれですか?
- 正解: データ強化(a=[3])
- 根拠(ユニット本文・日本語版): 「データを使用して取引先責任者レイアウトを強化する」
- v: 要確認 / f: d360ai
- 要確認の理由: 本文の「データを使用して取引先責任者レイアウトを強化する」節から推定。選択肢「一括インサイト」との区別が本文だけでは明確でない。
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/data-cloud-powered-experiences/see-data-cloud-in-action

### 115. Trailhead: Agentforce の基本 / はじめての Agentforce Q1
- 問題: Agentforce とは何ですか?
- 正解: AI エージェントを構築およびリリースするための、完全で拡張可能なオープンプラットフォーム(a=[1])
- 根拠(ユニット本文・日本語版): 「Agentforce は、既存のワークフロー、データ、インテグレーションを使用して AI エージェントを構築およびリリースできる、完全で拡張可能なオープンプラットフォームです。」
- v: Trailhead のユニット本文で確認 / f: agents
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/einstein-copilot-basics/get-started-with-einstein-copilot

### 116. Trailhead: Agentforce の基本 / はじめての Agentforce Q2
- 問題: Agentforce を Trust Layer と統合するメリットはどれですか?
- 正解: サードパーティ LLM プロバイダーがデータを保持することがない。(a=[0])
- 根拠(ユニット本文・日本語版): 「ユーザーのデータがサードパーティの大規模言語モデル (LLM) プロバイダーに保持されることがありません。」
- v: Trailhead のユニット本文で確認 / f: agents
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/einstein-copilot-basics/get-started-with-einstein-copilot

### 117. Trailhead: Agentforce の基本 / Agentforce を試す Q1
- 問題: Agentforce における標準アクションとカスタムアクションの主な違いは何ですか?
- 正解: 標準アクションは Salesforce によって作成されるのに対し、カスタムアクションはお客様によって特定のビジネスニーズに合わせて作成される。(a=[0])
- 根拠(ユニット本文・日本語版): 「ビジネスに固有のプロセスやワークフローに合わせてエージェントをカスタマイズする必要がある場合は、各自のサブエージェント用のカスタムアクションを作成します。」
- v: Trailhead のユニット本文で確認 / f: agents
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/einstein-copilot-basics/explore-einstein-copilot

### 118. Trailhead: Agentforce の基本 / Agentforce を試す Q2
- 問題: Agentforce におけるサブエージェントの役割の最も適切な説明はどれですか?
- 正解: サブエージェントは、特定のタスクを実行するための一連のアクションと指示をエージェントに示す。(a=[1])
- 根拠(ユニット本文・日本語版): 「他方、カスタムのサブエージェントやアクションを作成して、AI エージェントに各自のビジネスに固有のタスクを実行させることも可能です。」
- v: Trailhead のユニット本文で確認 / f: agents
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/einstein-copilot-basics/explore-einstein-copilot

### 119. Trailhead: Agentforce の基本 / 推論エンジンの概要 Q1
- 問題: Agentforce における推論エンジンの主な役割は何ですか?
- 正解: ユーザーリクエストを解釈し、適切なサブエージェントとアクションを選択する(a=[1])
- 根拠(ユニット本文・日本語版): 「指揮者が拍子をとって演奏者を率いるように、推論エンジンはサブエージェントとアクションがユーザーのリクエストをどのように処理するかを調整します。」
- v: Trailhead のユニット本文で確認 / f: agents
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/einstein-copilot-basics/enable-customize-copilot

### 120. Trailhead: Agentforce の基本 / 推論エンジンの概要 Q2
- 問題: Agentforce Builder のエクスプローラーではどのようなことができますか?
- 正解: AI エージェントのすべてのアセットを表示して操作する。(a=[3])
- 根拠(ユニット本文・日本語版): 「Explorer (エクスプローラー) (1): エージェントのすべてのアセットやコンポーネントを 1 か所に表示してアクセスできます。」
- v: Trailhead のユニット本文で確認 / f: agents
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/einstein-copilot-basics/enable-customize-copilot

### 121. Trailhead: Models API 入門 / Models API の基本を学ぶ Q1
- 問題: 次のうち、Models API に最適なユースケースはどれですか?
- 正解: カスタム UI と外部 API インテグレーションを備えた AI ダッシュボード(a=[2])
- 根拠(ユニット本文・日本語版): 「彼女は、Models API を使用して外部の住宅市場 API からのデータを分析し、要約したものを DreamHouse Realty の従業員に提供する社内向けダッシュボードを作成しています。」
- v: Trailhead のユニット本文で確認 / f: models
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/get-started-with-einstein-models-api/learn-the-basics-of-models-api

### 122. Trailhead: Models API 入門 / Models API の基本を学ぶ Q2
- 問題: Models API は LLM に加えてエンベディングモデルもサポートしている。
- 正解: 正しい(a=[0])
- 根拠(ユニット本文・日本語版): 「Models API ではエンベディングや履歴を使用したチャット生成などの追加機能が提供され、それによって開発者はカスタム AI アプリケーションを設計できます。」
- v: Trailhead のユニット本文で確認 / f: models
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/get-started-with-einstein-models-api/learn-the-basics-of-models-api

### 123. Trailhead: エージェントをデータでグラウンディングする / グラウンディングの基本を学ぶ Q1
- 問題: LLM プロンプトをグラウンディングする目的は何ですか?
- 正解: LLM の応答の関連性と正確性を高めるため(a=[1])
- 根拠(ユニット本文・日本語版): 「グラウンディングの目的は、LLM の応答の正確性と関連性を高めることです。」
- v: Trailhead のユニット本文で確認 / f: grounding / x: 「グラウンディングは、プロンプトに組織の正確で最新のデータを加えて、LLM に文脈を与えることです。Prompt Template Workspace の「Insert Resource」ボタンから、差し込み項目として追加します。」
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/grounding-an-agent-with-data/learn-the-basics-of-grounding

### 124. Trailhead: エージェントをデータでグラウンディングする / グラウンディングの基本を学ぶ Q2
- 問題: AI エージェントに RAG を使用するのはどのような場合ですか?
- 正解: 非構造化データに保存されている知識で AI エージェントをグラウンディングする場合(a=[0])
- 根拠(ユニット本文・日本語版): 「RAG は、非構造化データソースから知識を取得するグラウンディングの一種です。このアプローチでは、ドキュメントのコレクションなど、信頼できるソースからの関連性の高い最新情報で LLM プロンプトを強化します。」
- v: Trailhead のユニット本文で確認 / f: grounding
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/grounding-an-agent-with-data/learn-the-basics-of-grounding

### 125. Trailhead: エージェントをデータでグラウンディングする / エージェントをデータでグラウンディングするためのオプションを確認する Q1
- 問題: 形式があらかじめ定義されているため、Agentforce と統合しやすいデータの種類はどれですか?
- 正解: 構造化データ(a=[0])
- 根拠(ユニット本文・日本語版): 「標準オブジェクト: エージェントアクションは、取引先、取引先責任者、ケース、商談などの標準 Salesforce オブジェクトの構造化データにアクセスできます。」
- v: Trailhead のユニット本文で確認 / f: grounding
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/grounding-an-agent-with-data/review-options-to-ground-an-agent-with-data

### 126. Trailhead: エージェントをデータでグラウンディングする / エージェントをデータでグラウンディングするためのオプションを確認する Q2
- 問題: Agentforce アクションを Salesforce データに接続するために使用される方法はどれですか?
- 正解: Flow Builder(a=[2])
- 根拠(ユニット本文・日本語版): 「エージェントアクションにローコードやノーコードアプローチを使用したい場合は、Flow Builder を使用してエージェントアクションを構築できます。」
- v: Trailhead のユニット本文で確認 / f: grounding
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/grounding-an-agent-with-data/review-options-to-ground-an-agent-with-data

### 127. Trailhead: Agentforce Builder の概要 / Agentforce Builder について知る Q1
- 問題: エージェントに関連付けられているサブエージェントやアクションに影響するものは何ですか?
- 正解: 選択したテンプレートまたは記述したエージェントの説明(a=[1])
- 根拠(ユニット本文・日本語版): 「選択したテンプレートや記述したエージェントの説明によって、エージェントに関連付けられるサブエージェントやアクションが決まります。」
- v: Trailhead のユニット本文で確認 / f: builder
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/introduction-to-agent-builder/get-to-know-agent-builder

### 128. Trailhead: Agentforce Builder の概要 / Agentforce Builder について知る Q2
- 問題: エージェントのパフォーマンスはどこでテストできますか?
- 正解: [Preview (プレビュー)] モード(a=[2])
- 根拠(ユニット本文・日本語版): 「[Preview (プレビュー)] モードでエージェントをテストし、会話の背後にある詳細を表示して、エージェントがプレビューの問い合わせに応答するために使用したサブエージェント、アクション、指示、推論を確認する。」
- v: Trailhead のユニット本文で確認 / f: builder / x: 「Preview発話を入力してテストし、どのサブエージェントやアクションが選ばれたかを確認する」
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/introduction-to-agent-builder/get-to-know-agent-builder

### 129. Trailhead: Agentforce の概要 / Agentforce の機能について知る Q1
- 問題: Agentforce が会話の変化に応じて異なるサブエージェントやアクションをコールできるようにするものはどれですか?
- 正解: Atlas 推論エンジン(a=[1])
- 根拠(ユニット本文・日本語版): 「推論エンジンにより、エージェントが人間の意図を処理して理解し、会話の流れの中でアクションを実行して、会話の変化に応じて異なるサブエージェントやアクションをコールできます。」
- v: Trailhead のユニット本文で確認 / f: agents / x: 「推論エンジン会話をサブエージェントへ振り分け、LLMと推論して次の手を決める」
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/introduction-to-agentforce/get-to-know-agentforce-functionality

### 130. Trailhead: Agentforce の概要 / Agentforce の機能について知る Q2
- 問題: エージェントが実行するように設定されている個々のタスクを何と言いますか?
- 正解: アクション(a=[2])
- 根拠(ユニット本文・日本語版): 「アクションは、エージェントがジョブを実行するときに行う個々のタスク (ユーザーに取引先番号を尋ねるなど) です。」
- v: Trailhead のユニット本文で確認 / f: agents
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/introduction-to-agentforce/get-to-know-agentforce-functionality

### 131. Trailhead: 新しい Agentforce Builder: クイックルック / 新しいエージェントビルダーについて知る Q1
- 問題: Agentforce エージェントを管理するための新しい場所は何ですか?
- 正解: Agentforce スタジオ(a=[2])
- 根拠(ユニット本文・日本語版): 「Agentforce スタジオは、AI エージェントを作成して管理するための中央ハブです。」
- v: Trailhead のユニット本文で確認 / f: builder
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/new-agentforce-builder-quick-look/explore-the-new-agentforce-builder

### 132. Trailhead: 新しい Agentforce Builder: クイックルック / 新しいエージェントビルダーについて知る Q2
- 問題: 次のうち、キャンバスビューの正しい定義はどれですか?
- 正解: エージェントを作成するためのドキュメントスタイルのエディター。(a=[1])
- 根拠(ユニット本文・日本語版): 「キャンバス (2): このドキュメントスタイルのエディターを使用して、エージェントを変更したり、その詳細を表示したりできます。」
- v: Trailhead のユニット本文で確認 / f: builder
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/new-agentforce-builder-quick-look/explore-the-new-agentforce-builder

### 133. Trailhead: Agentforce でのプログラムによる指示 / フロー、アクション、権限を使用してエージェントに追加情報を提供する Q1
- 問題: お客様の誕生日を返すように [Get Customer Details (顧客の詳細を取得)] フローを更新するには、どうすればよいですか?
- 正解: [Get Contact by Email and Member Number (メールとメンバー番号で取引先責任者を取得)] 要素で、[Add Field (項目を追加)] をクリックし、[Birthdate (誕生日)] を選択する。(a=[1])
- 根拠(ユニット本文・日本語版): 「[Get Contact by Email and Member Number (メールとメンバー番号で取引先責任者を取得)] 要素をダブルクリックして開きます。」
- v: Trailhead のユニット本文で確認 / f: topics
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/programmatic-instructions-in-agentforce/give-your-agent-more-information-with-flows-actions-and-permissions

### 134. Trailhead: Agentforce でのプログラムによる指示 / フロー、アクション、権限を使用してエージェントに追加情報を提供する Q2
- 問題: あなたは取引先責任者オブジェクトに新しい項目 Preferred_Name__c を追加しました。お客様にプリファードネームで挨拶するようにエージェントを更新したいと思います。エージェントが新しい項目にアクセスできるようにするには、どうすればよいですか?
- 正解: エージェントに取引先責任者オブジェクトの Preferred_Name__c に対する参照アクセス権を付与する。(a=[1])
- 根拠(ユニット本文・日本語版): 「ユーザーがオブジェクトのカスタム項目に対するアクセス権を自動的に得ることはありません。」
- v: Trailhead のユニット本文で確認 / f: topics
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/programmatic-instructions-in-agentforce/give-your-agent-more-information-with-flows-actions-and-permissions

### 135. Trailhead: Agentforce でのプログラムによる指示 / 条件ロジックを使用して各コンテキストに適したプロンプトを送信する Q1
- 問題: テストのシナリオに記載されている推論指示について考えます。お客様のロイヤルティランクが Premium (プラチナ) の場合、どのプロンプトが LLM に送信されますか?
- 正解: If the user wants to make a return, confirm with them which order they want to return. (ユーザーが返品を希望する場合、どの注文の返品を希望するかを確認してください。) Once confirmed, process the return with {!@actions.create_return}. (確認したら、{!@actions.create_return} で返品を処理してください。)(a=[1])
- 根拠(ユニット本文・日本語版): 「| If the user wants to make a return, confirm with them which order they want to return.」
- v: Trailhead のユニット本文で確認 / f: topics
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/programmatic-instructions-in-agentforce/use-conditional-logic-to-send-the-right-prompt-for-each-context

### 136. Trailhead: Agentforce でのプログラムによる指示 / 条件ロジックを使用して各コンテキストに適したプロンプトを送信する Q2
- 問題: エージェント変数の現在の値を確認する最も簡単な方法はどれですか?
- 正解: [Preview (プレビュー)] で [Variables (変数)] を選択すると、すべての変数のリストが表示される。(a=[3])
- 根拠(ユニット本文・日本語版): 「[Preview (プレビュー)] で、 [Variables (変数)] タブをクリックします。」
- v: Trailhead のユニット本文で確認 / f: topics
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/programmatic-instructions-in-agentforce/use-conditional-logic-to-send-the-right-prompt-for-each-context

### 137. Trailhead: Agentforce でのプログラムによる指示 / 変数とアクションの絞り込みを使用してビジネスルールエンジンを適応する Q1
- 問題: テストシナリオで、エスカレーションサブエージェントが LLM に送信されるのはどの条件の場合ですか?
- 正解: ユーザーが検証済みで、サポートデスクの受付時間内である場合(a=[1])
- 根拠(ユニット本文・日本語版): 「available when @variables.customerVerified == True and @variables.officeOpen == True」
- v: Trailhead のユニット本文で確認 / f: topics
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/programmatic-instructions-in-agentforce/enforce-business-rules-with-variables-and-action-filters

### 138. Trailhead: Agentforce でのプログラムによる指示 / 変数とアクションの絞り込みを使用してビジネスルールエンジンを適応する Q2
- 問題: 条件付きチェックを行うために変数を使用している場合に変数のデフォルト値を設定すべきなのはなぜですか?
- 正解: 条件付きステートメントが正しく機能し、エージェントを更新するほかのユーザーがロジックを理解しやすくするため。(a=[0])
- 根拠(ユニット本文・日本語版): 「Agentforce では Boolean 変数のデフォルト値が指定されていない場合、自動的に False に設定されますが、 明確にデフォルト値を指定することで、同僚がエージェントを更新する必要が生じた場合に条件ロジックを理解しやすくなります。」
- v: Trailhead のユニット本文で確認 / f: topics
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/programmatic-instructions-in-agentforce/enforce-business-rules-with-variables-and-action-filters

### 139. Trailhead: プロンプトビルダーの基本 / プロンプトビルダーについて知る Q1
- 問題: プロンプトに具体的な要件とコンテキストを指示すると、応答にどのような影響がありますか?
- 正解: 指定した要件に合わせて出力が調整され強化される。(a=[2])
- 根拠(ユニット本文・日本語版): 「具体的な要件とコンテキストを指示した場合と指示しない場合とでは、生成される出力が大きく異なります。」
- v: Trailhead のユニット本文で確認 / f: promptbuilder
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/prompt-builder-basics/get-to-know-prompt-builder

### 140. Trailhead: プロンプトビルダーの基本 / プロンプトビルダーについて知る Q2
- 問題: 顧客向けにパーソナライズされたメールの生成を支援するプロンプトテンプレート種別はどれですか?
- 正解: セールスメールプロンプトテンプレート(a=[1])
- 根拠(ユニット本文・日本語版): 「セールスメールプロンプトテンプレート : チームがレコードデータに基づいて、顧客、商品、イベントなどに関する真の意味でパーソナライズされたメールのドラフトを作成できます。」
- v: Trailhead のユニット本文で確認 / f: promptbuilder
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/prompt-builder-basics/get-to-know-prompt-builder

### 141. Trailhead: プロンプトビルダーの基本 / プロンプトテンプレートを作成してグラウンディングする Q1
- 問題: 正誤問題: グラウンディングは、プロンプトの応答にコンテキストや具体的な情報を示すために使用する手法である。
- 正解: 正しい(a=[0])
- 根拠(ユニット本文・日本語版): 「テンプレートを 具体的 にすれば効果が高まります。「具体的」とは、テンプレートが グラウンディング されているということです。」
- v: Trailhead のユニット本文で確認 / f: promptbuilder
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/prompt-builder-basics/create-and-ground-prompt-templates

### 142. Trailhead: プロンプトビルダーの基本 / プロンプトテンプレートを作成してグラウンディングする Q2
- 問題: セールスメールプロンプトテンプレートで、顧客ごとにメールをパーソナライズするための Name、Title、MailingCity などの差し込み項目を提供するリソースはどれですか?
- 正解: 受信者(a=[2])
- 根拠(ユニット本文・日本語版): 「Linda は [Resources (リソース)] 選択リストから [Sender (送信者)] と [Recipient (受信者)] を選択し、さらにプロンプトテンプレートをグラウンディングするために役職、名前、会社などの具体的な情報を選択します。」
- v: Trailhead のユニット本文で確認 / f: promptbuilder
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/prompt-builder-basics/create-and-ground-prompt-templates

### 143. Trailhead: プロンプトビルダーの基本 / 項目生成プロンプトテンプレートを構築する Q1
- 問題: プロンプトビルダーを使用して項目生成プロンプトテンプレートを作成するために必要なものはどれですか?
- 正解: A と C(a=[4])
- 根拠(ユニット本文・日本語版): 「Object (オブジェクト): Case (ケース)」
- v: Trailhead のユニット本文で確認 / f: promptbuilder
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/prompt-builder-basics/build-a-field-generation-prompt-template

### 144. Trailhead: プロンプトビルダーの基本 / 項目生成プロンプトテンプレートを構築する Q2
- 問題: 項目生成プロンプトテンプレートはどの種別のフローを使用しますか?
- 正解: テンプレートトリガープロンプトフロー(a=[1])
- 根拠(ユニット本文・日本語版): 「[Template-Triggered Prompt Flow (テンプレートトリガープロンプトフロー)] 種別のフローはプロンプトテンプレートからのみ実行されます。」
- v: Trailhead のユニット本文で確認 / f: promptbuilder
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/prompt-builder-basics/build-a-field-generation-prompt-template

### 145. Trailhead: プロンプトビルダーの基本 / プロンプトテンプレートを確認して修正し、保存する Q1
- 問題: プロンプトの応答を確認するときに、正確性を確保し、意図しない情報が含まれないようにするために検討すべき点はどれですか?
- 正解: 事実の正確度(a=[3])
- 根拠(ユニット本文・日本語版): 「プロンプトの応答の正確度を高め、有害性を抑える方法を復習する。」
- v: 要確認 / f: promptbuilder
- 要確認の理由: 本文に「事実の正確度」という語での直接の記述を確認できず、ユニット目標の記述から推定。
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/prompt-builder-basics/review-revise-and-repeat-testing-prompt-templates

### 146. Trailhead: プロンプトビルダーの基本 / プロンプトテンプレートを確認して修正し、保存する Q2
- 問題: ユーザーがプロンプトの応答をプレビューできるプロンプトビルダーの 2 つの機能はどれですか?
- 正解: 解決済みプロンプトと応答(a=[1])
- 根拠(ユニット本文・日本語版): 「テンプレートを修正して、プレビューを生成し直すたびに、Einstein によって解決済みプロンプトと LLM 応答が更新されます。」
- v: Trailhead のユニット本文で確認 / f: promptbuilder
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/prompt-builder-basics/review-revise-and-repeat-testing-prompt-templates

### 147. Trailhead: プロンプトエンジニアリングのテクニック / いろいろなプロンプト手法を利用してプロンプトを改善しましょう。 Q1
- 問題: クイズのシナリオに基づき、Janina が使用する高度なプロンプトエンジニアリング手法はどれですか?
- 正解: CoT プロンプト(a=[1])
- 根拠(ユニット本文・日本語版): 「CoT (Chain-of-thought: 思考の連鎖) プロンプトは、AI が回答を出す前に「考えを言語化しながら進める」ように促す手法です。」
- v: Trailhead のユニット本文で確認 / f: promptbp
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/prompt-engineering-techniques/improve-prompts-using-different-prompt-techniques

### 148. Trailhead: プロンプトエンジニアリングのテクニック / いろいろなプロンプト手法を利用してプロンプトを改善しましょう。 Q2
- 問題: プロンプトのライフサイクルにおいて、レポート機能や信頼機能を使用してプロンプトのパフォーマンスを追跡することに焦点を当てるフェーズはどれですか?
- 正解: 監視(a=[2])
- 根拠(ユニット本文・日本語版): 「監視: プロンプトが使用可能な状態になったら、Data 360 の AI レポートや Einstein Trust Layer などのソースから得られるセキュリティと分析情報を活用して、プロンプトがビジネスに与える影響を包括的に把握します。」
- v: Trailhead のユニット本文で確認 / f: promptbp
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/prompt-engineering-techniques/improve-prompts-using-different-prompt-techniques

### 149. Trailhead: プロンプトの基本事項 / プロンプト入門 Q1
- 問題: プロンプトの品質は、AI モデルの応答にどのような影響を与えますか?
- 正解: より明確で具体的なプロンプトほど、より良い応答が得られる(a=[1])
- 根拠(ユニット本文・日本語版): 「プロンプトが明確で具体的であるほど、AI モデルの回答の質が高まります。」
- v: Trailhead のユニット本文で確認 / f: promptbp
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/prompt-fundamentals/get-started-with-prompts

### 150. Trailhead: プロンプトの基本事項 / プロンプト入門 Q2
- 問題: 次のうち、効果的なプロンプトの 6 つの主要な構成要素の 1 つはどれですか?
- 正解: ロール(a=[2])
- 根拠(ユニット本文・日本語版): 「Role (ロール) : AI にどのような役割を担わせるか。」
- v: Trailhead のユニット本文で確認 / f: promptbp
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/prompt-fundamentals/get-started-with-prompts

### 151. Trailhead: プロンプトの基本事項 / より良いプロンプトを書く Q1
- 問題: プロンプトでトリプルクォート (""") を使用する主な目的は何ですか?
- 正解: 指示とデータを明確に区別すること(a=[0])
- 根拠(ユニット本文・日本語版): 「データを囲む区切りとしてトリプルクォート ( """ ) を使用します。」
- v: Trailhead のユニット本文で確認 / f: promptbp
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/prompt-fundamentals/write-better-prompts

### 152. Trailhead: プロンプトの基本事項 / より良いプロンプトを書く Q2
- 問題: 「一度だけ参照する」原則によると、プロンプトで避けるべきことは何ですか?
- 正解: 同じデータを 1 つのプロンプトで複数回繰り返すこと(a=[3])
- 根拠(ユニット本文・日本語版): 「1 つのプロンプトで同じデータを繰り返すと、予期しない結果や一貫性のない結果につながる可能性があります。」
- v: Trailhead のユニット本文で確認 / f: promptbp
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/prompt-fundamentals/write-better-prompts

### 153. Trailhead: プロンプトの基本事項 / プロンプト設計パターンを確認する Q1
- 問題: 長いメールスレッドを要点にまとめるには、どのプロンプト設計パターンを使用しますか?
- 正解: 要約(a=[2])
- 根拠(ユニット本文・日本語版): 「要約: レシピ全体を大まかな手順に絞り込みます。」
- v: Trailhead のユニット本文で確認 / f: promptbp
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/prompt-fundamentals/explore-prompt-design-patterns

### 154. Trailhead: プロンプトの基本事項 / プロンプト設計パターンを確認する Q2
- 問題: マーケティングチームが、1 つの商品説明をもとに、新商品に関するソーシャルメディア投稿を 10 種類作成する必要があります。どのパターンを使用すべきですか?
- 正解: 変換(a=[1])
- 根拠(ユニット本文・日本語版): 「プラットフォーム (ソーシャルメディア、ブログなど) に合わせてコンテンツを変更する。」
- v: 要確認 / f: promptbp
- 要確認の理由: 本文の変換パターンの例「プラットフォーム(ソーシャルメディア、ブログなど)に合わせてコンテンツを変更する」から推定。コンテンツ生成とする解釈もあり得る。
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/prompt-fundamentals/explore-prompt-design-patterns

### 155. Trailhead: プロンプトの基本事項 / モデルの適合性が重要な理由を学ぶ Q1
- 問題: ユースケースに合わせて AI モデルを選択する際に最も重要な要素は何ですか?
- 正解: 特定のタスクでどの程度のパフォーマンスを発揮するか(a=[3])
- 根拠(ユニット本文・日本語版): 「重要なのは、特定のタスクでモデルがどの程度のパフォーマンスを発揮するかという点です。」
- v: Trailhead のユニット本文で確認 / f: promptbp
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/prompt-fundamentals/learn-why-model-fit-matters

### 156. Trailhead: プロンプトの基本事項 / モデルの適合性が重要な理由を学ぶ Q2
- 問題: コストと精度のトレードオフの原則に基づくと、モデルを選択する際に何を考慮すべきですか?
- 正解: テストして、ニーズに合ったコストと品質のバランスを見つける(a=[1])
- 根拠(ユニット本文・日本語版): 「原則 3: コストと精度のトレードオフ: 高性能なモデルほどコストが高いことがよくあります。」
- v: Trailhead のユニット本文で確認 / f: promptbp
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/prompt-fundamentals/learn-why-model-fit-matters

### 157. Trailhead: プロンプトの基本事項 / プロンプトのテストと改善 Q1
- 問題: プロンプトが汎用的で役に立たない出力を生成する場合、推奨される修正方法は何ですか?
- 正解: タスクと指示にさらに具体的な内容を追加する(a=[3])
- 根拠(ユニット本文・日本語版): 「タスクと指示をもっと具体的にする」
- v: Trailhead のユニット本文で確認 / f: promptbp
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/prompt-fundamentals/test-and-improve-prompts

### 158. Trailhead: プロンプトの基本事項 / プロンプトのテストと改善 Q2
- 問題: 7 ステップの反復サイクルにおいて、プロンプトをテストした直後に行うべきことは何ですか?
- 正解: 成功基準に照らして結果を評価する(a=[0])
- 根拠(ユニット本文・日本語版): 「成功基準に照らして結果を評価します。」
- v: Trailhead のユニット本文で確認 / f: promptbp
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/prompt-fundamentals/test-and-improve-prompts

### 159. Trailhead: 検索拡張生成: クイックルック / 関連ビジネスナレッジを使用したエージェントとプロンプトの拡張 Q1
- 問題: プロンプトで RAG を使用する理由はどれですか?
- 正解: RAG によって LLM 応答の正確性と関連性が高まるため。(a=[0])
- 根拠(ユニット本文・日本語版): 「RAG を使用すると、ドメイン固有の情報が追加され、LLM がユーザーのプロンプトに対してより適切に応答できるようになります。」
- v: Trailhead のユニット本文で確認 / f: datalib
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/retrieval-augmented-generation-quick-look/augment-prompts-with-relevant-knowledge

### 160. Trailhead: 検索拡張生成: クイックルック / 関連ビジネスナレッジを使用したエージェントとプロンプトの拡張 Q2
- 問題: プロンプトテンプレートで、特定の情報を検索するために RAG をトリガーするには何を追加しますか?
- 正解: レトリーバー(a=[1])
- 根拠(ユニット本文・日本語版): 「レトリーバーとは、ナレッジストアの関連情報を検索して返すためにプロンプトテンプレートに組み込むリソースです。」
- v: Trailhead のユニット本文で確認 / f: datalib
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/retrieval-augmented-generation-quick-look/augment-prompts-with-relevant-knowledge

### 161. Trailhead: Data 360 の検索インデックス種別: クイックルック / Data 360 の 検索インデックス種別について知る Q1
- 問題: ハイブリッド検索インデックスの主なコンポーネントは何ですか?
- 正解: ベクトル検索インデックス、キーワード検索インデックス、融合ランカーサービス(a=[1])
- 根拠(ユニット本文・日本語版): 「ハイブリッド検索では、両タイプの検索から取得した情報をマージした後に、融合ランカー機能を使用し」
- v: Trailhead のユニット本文で確認 / f: retriever / x: 「ハイブリッド検索(Hybrid Search)ベクトル検索とキーワード検索の両方で探し、結果をまとめて順位をつける「LaserPrinter TX 400」と「TX 440」のような型番の違いにも強い」
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/search-index-types-data-cloud-quick-look/get-to-know-search-index-types-in-data-cloud

### 162. Trailhead: Data 360 の検索インデックス種別: クイックルック / Data 360 の 検索インデックス種別について知る Q2
- 問題: 検索クエリで意味一致とキーワード一致の両方の長所を生かすのに最も効率的な検索種別はどれですか?
- 正解: ハイブリッド検索(a=[1])
- 根拠(ユニット本文・日本語版): 「ハイブリッド検索は、意味を認識するベクトル検索の強みとドメインの用語を処理するキーワード検索の機能を組み合わせたものです。」
- v: Trailhead のユニット本文で確認 / f: retriever / x: 「ハイブリッド検索(Hybrid Search)ベクトル検索とキーワード検索の両方で探し、結果をまとめて順位をつける「LaserPrinter TX 400」と「TX 440」のような型番の違いにも強い」
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/search-index-types-data-cloud-quick-look/get-to-know-search-index-types-in-data-cloud

### 163. Trailhead: Agentforce Trust Layer / Agentforce Trust Layer の概要 Q1
- 問題: Salesforce が Einstein Trust Layer を作成した理由は何ですか?
- 正解: データセキュリティとプライバシーコントロールを実装するため(a=[1])
- 根拠(ユニット本文・日本語版): 「Einstein Trust Layer を使用すると、お客様がデータのセキュリティコントロールやプライバシーコントロールを阻害することなく、生成 AI のメリットを活用できます。」
- v: Trailhead のユニット本文で確認 / f: trust / x: 「Einstein Trust Layer は、生成AIとAgentforceの機能に組み込まれた、データのプライバシーを守り、AIを安全に使うための機能・プロセス・ポリシーの集まりです。」
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/the-einstein-trust-layer/meet-the-einstein-trust-layer

### 164. Trailhead: Agentforce Trust Layer / Agentforce Trust Layer の概要 Q2
- 問題: Salesforce の最大の価値は何ですか?
- 正解: 信頼(a=[2])
- 根拠(ユニット本文・日本語版): 「Salesforce の最大の価値である信頼について話し合う。」
- v: Trailhead のユニット本文で確認 / f: trust
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/the-einstein-trust-layer/meet-the-einstein-trust-layer

### 165. Trailhead: Agentforce Trust Layer / プロンプトジャーニーをたどる Q1
- 問題: 動的グラウンディングによってプロンプトのコンテキストがどのように改善されますか?
- 正解: 組織から直接、承認済みの安全な関連データが取り込まれ、プロンプトテンプレートに追加される。(a=[3])
- 根拠(ユニット本文・日本語版): 「プロンプトテンプレートがどのようなもので、どのような方法でテンプレートに顧客データや関連リソースが入力され、Einstein Trust La」
- v: Trailhead のユニット本文で確認 / f: trust
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/the-einstein-trust-layer/follow-the-prompt-journey

### 166. Trailhead: Agentforce Trust Layer / プロンプトジャーニーをたどる Q2
- 問題: Trust Layer のプロンプト防御ガードレールは、何から保護する場合に役立ちますか?
- 正解: プロンプトインジェクション攻撃(a=[1])
- 根拠(ユニット本文・日本語版): 「生成 AI では、こうした攻撃の一種を プロンプトインジェクション と呼んでいます。」
- v: Trailhead のユニット本文で確認 / f: trust
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/the-einstein-trust-layer/follow-the-prompt-journey

### 167. Trailhead: Agentforce Trust Layer / 応答ジャーニーをたどる Q1
- 問題: データ保持ゼロとはどういう意味ですか?
- 正解: プロンプト、その応答、すべての関連データを LLM が忘れ去る。(a=[3])
- 根拠(ユニット本文・日本語版): 「けれども、Salesforce のデータ保持ゼロポリシーにより、LLM のパートナーは対話のデータを一切保持できません。」
- v: Trailhead のユニット本文で確認 / f: trust / x: 「ゼロデータ保持により、外部のLLMはデータを保存せず、学習にも使いません。」
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/the-einstein-trust-layer/follow-the-response-journey

### 168. Trailhead: Agentforce Trust Layer / 応答ジャーニーをたどる Q2
- 問題: 応答の有害な言葉はどのようにスキャンされますか?
- 正解: 機械学習モデルは有害なコンテンツの識別に使用される。(a=[2])
- 根拠(ユニット本文・日本語版): 「Trust Layer は機械学習モデルを使用して、プロンプトや応答の有害なコンテンツを、暴力的、性的、冒涜的、憎悪的、身体的という 5 つのカテゴリで識別してフラグを立てます。」
- v: Trailhead のユニット本文で確認 / f: trust
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/the-einstein-trust-layer/follow-the-response-journey

### 169. Trailhead: AI エージェントの脅威モデリング / AI エージェントの使用に伴うリスクを認識する Q1
- 問題: 次のうち、AI エージェントの動作に影響を及ぼす一般的なリスクを説明しているものはどれですか?
- 正解: メモリ汚染により、エージェントが誤ったコンテキストに基づいてアクションを実行する。(a=[1])
- 根拠(ユニット本文・日本語版): 「攻撃者がエージェントの短期/長期メモリに偽のコンテキストを仕込み、エージェントが長期にわたって安全でないアクションを繰り返し実行するようにする。」
- v: Trailhead のユニット本文で確認 / f: access
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/threat-modeling-for-ai-agents/know-the-risks-when-using-ai-agents

### 170. Trailhead: AI エージェントの脅威モデリング / AI エージェントの使用に伴うリスクを認識する Q2
- 問題: 次のリスクのうち、意図していたものより広範なアクセス権限がエージェントに付与され、リスクの高いアクションの実行が可能になるものはどれですか?
- 正解: 権限の侵害(a=[0])
- 根拠(ユニット本文・日本語版): 「設定ミスにより、エージェントに意図したものより広範なアクセス権限が付与され、エージェントがリスクの高いアクション (承認、変更、削除など) を実行可能になる。」
- v: Trailhead のユニット本文で確認 / f: access
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/threat-modeling-for-ai-agents/know-the-risks-when-using-ai-agents

### 171. Trailhead: AI エージェントの脅威モデリング / AI エージェントのリスクを特定して管理する Q1
- 問題: あるビジネスワークフローでは、エージェントが API に接続します。これはどの種類の関与ですか?
- 正解: システム(a=[2])
- 根拠(ユニット本文・日本語版): 「例: お客様がリクエスト ( データ入力 ) → エージェントがデータをレビュー ( API 接続 ) → エージェントが応答 → 人間が承認 ( 人間のレビュー ) → システム更新」
- v: Trailhead のユニット本文で確認 / f: access
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/threat-modeling-for-ai-agents/identify-and-manage-ai-agent-risks

### 172. Trailhead: AI エージェントの脅威モデリング / AI エージェントのリスクを特定して管理する Q2
- 問題: 次のシナリオのうち、脅威モデリングを使用して AI エージェントのリスクを軽減するものはどれですか?
- 正解: エージェントが許可されていないデータにアクセス可能になる過剰なアクセス権限を特定して、不必要な権限を削除する。(a=[2])
- 根拠(ユニット本文・日本語版): 「AI エージェントのリスクを軽減するために脅威モデリングを実践する。」
- v: Trailhead のユニット本文で確認 / f: access
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/threat-modeling-for-ai-agents/identify-and-manage-ai-agent-risks

### 173. Trailhead: 信頼できるエージェント型 AI / Salesforce が信頼できるエージェント型 AI を構築する方法を確認する Q1
- 問題: エージェント型 AI に付随する主なリスクは何ですか?
- 正解: 予期しない動作や意図しない結果(a=[1])
- 根拠(ユニット本文・日本語版): 「AI エージェントの自律的なアクションが、予期しない、潜在的に有害な結果につながるおそれがあります。」
- v: Trailhead のユニット本文で確認 / f: access
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/trusted-agentic-ai/discover-how-salesforce-builds-trusted-agentic-ai

### 174. Trailhead: 信頼できるエージェント型 AI / Salesforce が信頼できるエージェント型 AI を構築する方法を確認する Q2
- 問題: 次の原則のうち、責任あるエージェント型 AI の基本原則の一部であるものはどれですか?
- 正解: A と B(a=[3])
- 根拠(ユニット本文・日本語版): 「正確さ」
- v: Trailhead のユニット本文で確認 / f: access
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/trusted-agentic-ai/discover-how-salesforce-builds-trusted-agentic-ai

### 175. Trailhead: 信頼できるエージェント型 AI / Agentforce のガードレールと信頼パターンを検討する Q1
- 問題: Agentforce でエージェントの動作を調整するにはどうすればよいですか?
- 正解: トピックの指示とアクションを調整する。(a=[2])
- 根拠(ユニット本文・日本語版): 「エージェントの標準トピックの指示を変更することや、カスタムトピックをゼロから作成することができます。」
- v: Trailhead のユニット本文で確認 / f: topics / x: 「サブエージェント(旧称 トピック)は、エージェントができる「1つの仕事」です。会話の進め方を決める指示(インストラクション)と、仕事に使うアクションをまとめて持ちます。」
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/trusted-agentic-ai/explore-agentforce-guardrails-and-trust-patterns

### 176. Trailhead: 信頼できるエージェント型 AI / Agentforce のガードレールと信頼パターンを検討する Q2
- 問題: 正誤問題: トピック分類は、ユーザー入力を特定のトピックにマッピングするために使用する。
- 正解: 正しい(a=[0])
- 根拠(ユニット本文・日本語版): 「トピック分類を使用して、ユーザー入力を特定のトピックにマッピングします。」
- v: Trailhead のユニット本文で確認 / f: topics
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/trusted-agentic-ai/explore-agentforce-guardrails-and-trust-patterns

### 177. Trailhead: 信頼できるエージェント型 AI / 責任ある倫理的なエージェントを推進する Q1
- 問題: Salesforce は AI 製品のレッドチーミングに対してどのようなアプローチを採用していますか?
- 正解: レッドチーミングの手動と自動の両方の手法を使用する。(a=[1])
- 根拠(ユニット本文・日本語版): 「Salesforce では、AI 製品の安全性を高める目的で、手動と自動の両方のレッドチーミング手法を採用しています。」
- v: Trailhead のユニット本文で確認 / f: access
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/trusted-agentic-ai/promote-responsible-and-ethical-agents

### 178. Trailhead: 信頼できるエージェント型 AI / 責任ある倫理的なエージェントを推進する Q2
- 問題: 正誤問題: AI システムの整合性を維持するためには、継続的な改善とイノベーションが不可欠である。
- 正解: 正しい(a=[0])
- 根拠(ユニット本文・日本語版): 「継続的な改善とイノベーションの文化を育み、お客様に信頼してもらえる AI ソリューションの提供に取り組んでいます。」
- v: Trailhead のユニット本文で確認 / f: access
- URL: https://trailhead.salesforce.com/ja/content/learn/modules/trusted-agentic-ai/promote-responsible-and-ethical-agents
