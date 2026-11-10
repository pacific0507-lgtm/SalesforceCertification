# MuleSoft Platform Architect(mulepa)Trailhead モジュールのクイズ

Trailhead のユニットのページ(英語版と /ja/ 版)の HTML に埋め込まれたクイズ(challenge.type = quiz)を取り出し、正解はユニット本文から判断した。取得日 2026-11-10。

## 公式の準備用 Trailmix について

- 認定資格のページ https://trailhead.salesforce.com/credentials/mulesoftplatformarchitecti (英語・日本語とも)の HTML には、準備用 Trailmix へのリンクもモジュールの一覧も含まれていなかった(内容は JavaScript で読み込まれる)。Trailhead Academy の試験ページ(exam-mule-plat-arch---Mule-Arch-201)にもリンクはなかった。推測した Trailmix の URL は 404、検索で見つかった Trailmix の URL はどれも MuleSoft の認定資格の概要ページへ転送された。
- そこで、試験範囲(API 主導の接続、Anypoint Platform、API の設計・ガバナンス、デプロイ、監視)に合う MuleSoft のモジュールを、モジュールページの HTML にあるトレイルのリンクからたどって選んだ。たどったトレイル: drive-success-with-mulesoft-anypoint-platform、great-integrations-mulesoft、mulesoft-integration-trailblazer。

## 使ったモジュール

| モジュール | 日本語名 | 日本語版 | 使ったユニット |
|---|---|---|---|
| anypoint-platform-basics | Anypoint Platform の基本 | あり | 4ユニット全部(8問) |
| application-networks-and-api-led-connectivity-in-mulesoft | (日本語版なし。名前は仮訳「MuleSoft のアプリケーションネットワークと API 主導の接続」) | なし | 4ユニット全部(8問) |
| api-design-with-mulesoft | MuleSoft を使用した API デザイン | あり | 5ユニット(10問中9問。1問は重複で除外) |
| anypoint-platform-deployment-and-management-of-apis | Anypoint Platform による API のデプロイメントと管理 | あり | 4ユニット全部(8問) |
| api-led-integration-for-business-reinvention | ビジネス変革のための API 主導の連携 | あり | imagine-the-potential-of-connected-data のみ(2問) |

## 見たが使わなかったもの

- api-led-integration-for-business-reinvention のほかの3ユニット: 第4次産業革命、PC と LAN、ポップコーンの選択肢など、ビジネス変革の一般論で試験範囲から外れるため。
- scanners-in-anypoint-exchange-quick-look: Agent Fabric の AI エージェントのスキャナーの話で、試験範囲外(日本語版もなし)。
- mulesoft-catalyst-knowledge-hub: ポータルの画面操作(検索バー、ダウンロードの可否)の問題で、試験範囲外(日本語版もなし)。
- mulesoft-anypoint-code-builder-quick-look、agentic-integration-with-mulesoft-vibes、pw-api-basics(Salesforce の一般的な API の基本)、mulesoft-community-quick-look: 試験範囲から外れるため対象外。
- プロジェクト govern-apis-using-anypoint-api-governance はハンズオンのチャレンジでクイズがないため対象外。
- Omni Gateway(旧 Flex Gateway)だけを扱う Trailhead モジュールは見つからなかった(推測した URL はすべて 404)。

## 重複として除外

- api-design-with-mulesoft/publish-and-share-apis Q1「What is a benefit of publishing an API to Anypoint Exchange?」: anypoint-platform-basics/explore-anypoint-exchange Q1 とほぼ同じ(Exchange で API を見つけて再利用できる)

## 日本語の扱い

- 日本語版があるユニットは公式の日本語のクイズ文をそのまま q / o に使い、英語を qe / oe に入れた。
- application-networks-and-api-led-connectivity-in-mulesoft は /ja/ の URL でも英語のまま表示される(日本語版なし)。q / o は自分で訳し、モジュール名・ユニット名も仮訳。u は /ja/ の URL(英語で表示される)。
- 「連携データの可能性を想像する Q2」は公式の選択肢が「A と B」「B と C」で、選択肢の並べ替えに弱いため、o では組み合わせを文字で書いた(oe は公式どおり "A and B" のまま)。

## 正解の根拠(ユニット本文からの引用)

v はすべて「Trailhead のユニット本文で確認」(要確認 0 問)。

### Trailhead: Anypoint Platform の基本 / Anypoint Platform について知る Q1
- 正解: A unified suite of tools for designing, building, and managing integrations  / 項目 f: platform
- 根拠: "Anypoint Platform is a complete suite of tools for designing, building, managing, and deploying APIs and integrations. … It provides all the resources you need to connect apps, data, and devices"

### Trailhead: Anypoint Platform の基本 / Anypoint Platform について知る Q2
- 正解: OAS  / 項目 f: spec
- 根拠: "At its core is the API Specification, typically written in OpenAPI Specification (OAS)."

### Trailhead: Anypoint Platform の基本 / Anypoint Platform を操作する Q1
- 正解: Helps align business goals with technical delivery and team enablement.  / 項目 f: c4e
- 根拠: "It’s built on three key pillars … Business outcomes: … align with stakeholders to measure success. Technology delivery: … Organization enablement: Entrust teams to use Anypoint Platform effectively by establishing best practices, training, and internal support."

### Trailhead: Anypoint Platform の基本 / Anypoint Platform を操作する Q2
- 正解: Monitor application performance.  / 項目 f: platform
- 根拠: "Use Anypoint Management Center to Monitor and Govern APIs … It’s a suite of tools that helps teams govern, deploy, and troubleshoot APIs throughout their lifecycle."

### Trailhead: Anypoint Platform の基本 / Anypoint Exchange を探索する Q1
- 正解: It enables teams to discover, share, and reuse APIs, templates, and connectors  / 項目 f: exchange
- 根拠: "Think of Anypoint Exchange as a central library where developers, integrators, and architects can discover APIs, connectors, and templates to speed up their work. Instead of starting from scratch, teams can reuse existing assets"

### Trailhead: Anypoint Platform の基本 / Anypoint Exchange を探索する Q2
- 正解: An API portal is automatically created, providing documentation, an API console, and a mocking service.  / 項目 f: c4e
- 根拠: "When a REST API is published to Anypoint Exchange, an API portal is automatically generated as part of the asset. These API portals include built-in documentation, an interactive console, and a mock service."

### Trailhead: Anypoint Platform の基本 / Anypoint コードビルダーを使って作業する Q1
- 正解: It’s an integrated development environment for API designs, implementations, and integration development.  / 項目 f: impl
- 根拠: "Anypoint Code Builder is MuleSoft’s integrated development environment (IDE), built on Visual Studio Code. It gives developers and integration teams a single, connected workspace where they can design and test APIs"

### Trailhead: Anypoint Platform の基本 / Anypoint コードビルダーを使って作業する Q2
- 正解: Defining the API’s structure and behavior  / 項目 f: spec
- 根拠: "“Design-first” development means defining what an API should do before building how it works. Rather than writing backend logic and adjusting it later, teams agree on the API’s structure and behavior upfront."

### Trailhead: MuleSoft のアプリケーションネットワークと API 主導の接続 / アプリケーションネットワークについて知る Q1
- 正解: They allow for reusable connections between systems, saving time and resources  / 項目 f: appnet
- 根拠: "Reusability: APIs are designed once and can be used across multiple projects and teams. / Instead of IT departments building single-use integrations for every system, application networks use APIs as standardized, reusable building blocks."

### Trailhead: MuleSoft のアプリケーションネットワークと API 主導の接続 / アプリケーションネットワークについて知る Q2
- 正解: Data silos that make it hard to share information across departments  / 項目 f: appnet
- 根拠: "Data silos: Systems and departments often operate independently, creating barriers to collaboration and efficient data sharing."

### Trailhead: MuleSoft のアプリケーションネットワークと API 主導の接続 / API 主導の接続について学ぶ Q1
- 正解: To create structured, reusable integrations that support agility and self-service  / 項目 f: appnet
- 根拠: "API-led connectivity transforms networks into structured, reusable frameworks … Enabling Reuse … Boosting Agility … Fostering Self-Service"

### Trailhead: MuleSoft のアプリケーションネットワークと API 主導の接続 / API 主導の接続について学ぶ Q2
- 正解: Experience API  / 項目 f: layers
- 根拠: "Experience APIs deliver data in formats optimized for user interfaces or devices."

### Trailhead: MuleSoft のアプリケーションネットワークと API 主導の接続 / API と Web サービスを調べる Q1
- 正解: PUT  / 項目 f: appnet
- 根拠: "PUT: Update an existing resource. / PUT: https://api.muleunited.com/flights/123 updates details for the flight with ID 123."

### Trailhead: MuleSoft のアプリケーションネットワークと API 主導の接続 / API と Web サービスを調べる Q2
- 正解: It uses encryption protocols like HTTPS to protect data in transit  / 項目 f: nfr
- 根拠: "Encryption: Use HTTPS to protect data as it travels between systems."

### Trailhead: MuleSoft のアプリケーションネットワークと API 主導の接続 / API コールを実行する Q1
- 正解: GET  / 項目 f: appnet
- 根拠: "GET: Retrieve data. (examine-apis-and-web-services ユニット) / In a real-world scenario, you'd use the GET method first to retrieve a list of flights"

### Trailhead: MuleSoft のアプリケーションネットワークと API 主導の接続 / API コールを実行する Q2
- 正解: The format of the response body, such as application/json.  / 項目 f: appnet
- 根拠: "Look at the response headers, such as Content-Type. … Content-Type: application/json; charset=UTF-8 (JSON の本文とともに表示される応答ヘッダーの例。定義文はないため、例から判断)"

### Trailhead: MuleSoft を使用した API デザイン / アプリケーションネットワークについて知る Q1
- 正解: /flights/{id}  / 項目 f: spec
- 根拠: "Use clear naming conventions: API endpoint names should be intuitive and self-explanatory instead of generic or arbitrary. Use: /flights/{id}"

### Trailhead: MuleSoft を使用した API デザイン / アプリケーションネットワークについて知る Q2
- 正解: It ensures APIs are easy to integrate, reuse, and scale.  / 項目 f: spec
- 根拠: "There are five proven API design principles that make APIs easy to use, scalable for future needs, and secure for data integrity. / Use Best Practices to Design Reusable and Scalable APIs"

### Trailhead: MuleSoft を使用した API デザイン / OAS を使用して API を定義する Q1
- 正解: They refine API requests to return specific data.  / 項目 f: spec
- 根拠: "To make an API useful, you also need to specify what actions it can perform and how clients can refine those actions. That’s where methods and parameters come in. / Query parameters follow a question mark (?) in the URL and filter or refine the request."

### Trailhead: MuleSoft を使用した API デザイン / OAS を使用して API を定義する Q2
- 正解: Use descriptive and consistent endpoint naming.  / 項目 f: spec
- 根拠: "Best Practices for Reusable APIs … Use consistent naming conventions. A predictable structure makes APIs easier to understand and navigate."

### Trailhead: MuleSoft を使用した API デザイン / モック対応 API について詳しく学ぶ Q1
- 正解: It defines the endpoints and the methods they expose.  / 項目 f: spec
- 根拠: "In OAS, resources are defined using URL paths that describe the type of data or functionality the API exposes. (define-apis-with-oas) / サンプル仕様: paths: /flights: get:"

### Trailhead: MuleSoft を使用した API デザイン / モック対応 API について詳しく学ぶ Q2
- 正解: They help consumers understand what to expect from the API.  / 項目 f: spec
- 根拠: "Response example: A sample JSON payload shows the data structure returned by the API. / Example responses show expected data structure"

### Trailhead: MuleSoft を使用した API デザイン / API をモックしてテストする Q1
- 正解: Example data for the response in the API definition  / 項目 f: spec
- 根拠: "The mocking service doesn’t create sample responses automatically. It uses the examples defined in the OAS file."

### Trailhead: MuleSoft を使用した API デザイン / API をモックしてテストする Q2
- 正解: Share the API asset in Anypoint Exchange.  / 項目 f: spec
- 根拠: "When a mocked API is published through a platform like Anypoint Exchange, a public portal is automatically created. This portal typically includes an API console where users can test endpoints using the example data defined in the specification. A single public link can be shared with stakeholders"

### Trailhead: MuleSoft を使用した API デザイン / API をパブリッシュして共有する Q2
- 正解: Create a customized API portal with examples and contact info.  / 項目 f: exchange
- 根拠: "Anypoint Exchange validates the specification and automatically creates an API portal based on its visibility settings. This portal includes: … Contact information and links for additional resources / Public (available to external developers)"

### Trailhead: Anypoint Platform による API のデプロイメントと管理 / Mule アプリケーションのデプロイメントモデルについて学ぶ Q1
- 正解: Runtime Fabric  / 項目 f: deployopts
- 根拠: "Runtime Fabric gives you full control over where and how applications run, including on-premises. / Unlike CloudHub and CloudHub 2.0, Runtime Fabric is customer-managed."

### Trailhead: Anypoint Platform による API のデプロイメントと管理 / Mule アプリケーションのデプロイメントモデルについて学ぶ Q2
- 正解: It monitors and manages deployed Mule applications across environments.  / 項目 f: platform
- 根拠: "Runtime Manager is the centralized tool for monitoring and operating deployed applications. It provides a single view across environments"

### Trailhead: Anypoint Platform による API のデプロイメントと管理 / API プロキシの役割を確認する Q1
- 正解: To route and manage requests between clients and backend services  / 項目 f: apimgr
- 根拠: "In Anypoint Platform, an API proxy receives requests from clients, evaluates those requests based on configured policies, and then forwards them to the backend service."

### Trailhead: Anypoint Platform による API のデプロイメントと管理 / API プロキシの役割を確認する Q2
- 正解: You can monitor API usage and apply policies without changing the backend.  / 項目 f: apimgr
- 根拠: "From API Manager, you can monitor usage, update policies, and publish new versions as the API evolves. This allows you to manage access and enforce governance without changing the underlying implementation."

### Trailhead: Anypoint Platform による API のデプロイメントと管理 / API ポリシーを使用してアクセスを管理する Q1
- 正解: Spike Control  / 項目 f: policies
- 根拠: "Spike Control: Focuses on preventing sudden bursts of traffic that could overwhelm backend services. It smooths out traffic by temporarily delaying or rejecting excessive requests during short time windows."

### Trailhead: Anypoint Platform による API のデプロイメントと管理 / API ポリシーを使用してアクセスを管理する Q2
- 正解: To allow enforcement without modifying backend code  / 項目 f: policies
- 根拠: "These policies are applied at the proxy level in Anypoint API Manager, so teams can manage access without modifying backend systems."

### Trailhead: Anypoint Platform による API のデプロイメントと管理 / 本番環境で API を監視して管理する Q1
- 正解: Response time  / 項目 f: monitoring
- 根拠: "Response time: How long it takes for the API to return a result."

### Trailhead: Anypoint Platform による API のデプロイメントと管理 / 本番環境で API を監視して管理する Q2
- 正解: To apply and enforce standards across teams  / 項目 f: governance
- 根拠: "Anypoint API Governance lets teams: Apply rulesets … Validate API specifications before they’re deployed. … Track conformance across teams and environments. Governance supports accurate, sustainable development. When teams work from shared standards …"

### Trailhead: ビジネス変革のための API 主導の連携 / 連携データの可能性を想像する Q1
- 正解: Ecosystems that involve a wide spectrum of stakeholders  / 項目 f: appnet
- 根拠: "Once that data is synchronized with a larger database in the cloud, an ecosystem involving other services starts to take shape. … More innovative opportunities present themselves, with gyms, financial institutions, and other stakeholders interested in finding ways to connect."

### Trailhead: ビジネス変革のための API 主導の連携 / 連携データの可能性を想像する Q2
- 正解: A and B  / 項目 f: appnet
- 根拠: "It’s repeatable, contextual, scalable, and the value of the data often improves with each new integration. / Connectivity-in-context: … there’s a specific context for connectivity … / Repeatable: … the value of the API-led connection is quickly and easily repeated across the ecosystem’s many stakeholders. / Purpose-built: The connectivity between devices and services is built with a set of agreed-upon and purpose-built standards."

## 補足

- 「API コールを実行する Q2」(Content-Type)は、本文に定義文はなく、JSON の応答本文とともに `Content-Type: application/json; charset=UTF-8` が応答ヘッダーとして示されているのが根拠。選択肢自体に application/json と書かれており、ほかの選択肢(メソッド、エンドポイント、状態コード)は明らかに違うので、確認済みとした。
- 「Anypoint Platform を操作する Q2」は、Management Center のツール一覧が画面のクリック操作で開く部分にあり HTML の本文に出てこないが、見出し「Use Anypoint Management Center to Monitor and Govern APIs」と説明文から判断した。
- 「Mule アプリケーションのデプロイメントモデルについて学ぶ Q1」は、試験の観点ではハイブリッド(顧客ホストの Mule)もインフラを自分で管理するが、選択肢にないため、本文どおり Runtime Fabric。

## 取得と解析

- 生の HTML: /tmp/claude-0/-home-user-SalesforceCertification/1fccc70c-a3a7-5e8a-825b-fb3720fd8239/scratchpad/th/mulepa/ (units/ にユニットごとの en / ja)
- 解析スクリプト: /tmp/claude-0/-home-user-SalesforceCertification/1fccc70c-a3a7-5e8a-825b-fb3720fd8239/scratchpad/thscripts/ (parse_mulepa.py、body_mulepa.py、spec_mulepa.py、build_mulepa_out.py。python3 -I で実行)
- add_trailhead.py を作業用のコピーで試し、35 問 / 警告 0(x はすべて本文と一致)を確認した。
