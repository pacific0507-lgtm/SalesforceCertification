# 撮影指示: MuleSoft Platform Architect(mulepa)

共通のルールは `commitstudy/screens/SHOOT_PROMPT.md` の「準備」「撮り方」「終わったら」に従う(読んでから始める)。違うのは次の点だけ。
- 保存先: `commitstudy/screens/raw/mulepa/`、manifest も `commitstudy/screens/raw/mulepa/manifest.json`
- 環境: Anypoint Platform(https://anypoint.mulesoft.com)。ユーザーのアカウント(無料トライアルでよい)にログインしてもらう。画面は英語のままでよい(lang は "en"、ファイル名の末尾 `_en` は付けなくてよい)
- コミットメッセージ: 「Anypoint Platform の画面(MuleSoft)を撮る」
- アプリのデプロイ・削除、ポリシーの適用、ユーザーの招待など、変更する操作はしない。作成画面は開いて見るだけ(保存が必要なときはユーザーに許可をもらい「commitstudy-demo」という名前で作る)
- トライアルで使えない機能(Runtime Fabric・Anypoint MQ など)は missing でよい

## 撮る画面(項目id: 内容)
1. `platform`: Anypoint Platform のホーム(左メニューに Design Center・Exchange・Management Center の各製品が並ぶ画面)
2. `orgs`: Access Management(ビジネスグループの一覧、環境の一覧 Sandbox/Production、チーム・ユーザー)
3. `spec`: Design Center の新規 API 仕様の作成画面(RAML / OAS の選択)、API 仕様のエディターとモッキングサービスの切り替え
4. `exchange`: Anypoint Exchange(アセットの一覧、1つのアセットの詳細: バージョン・API ノートブック・公開)
5. `versioning`: Exchange のアセットのバージョン一覧(メジャー/マイナー/パッチ)
6. `cloudhub`: Runtime Manager のアプリの一覧と、Deploy Application(CloudHub 2.0: レプリカ数・vCore・ランタイムのバージョンの選択)画面
7. `deployopts`: Runtime Manager のデプロイ先の選択(CloudHub 2.0・Runtime Fabric・ハイブリッドのサーバー)。プライベートスペースの一覧(あれば)
8. `apimgr`: API Manager の API インスタンスの一覧と「Add API」(自動検出・プロキシ・Flex Gateway/Omni Gateway の選択)
9. `policies`: API Manager の API インスタンス > Policies(ポリシーの追加画面: Client ID Enforcement・Rate Limiting・SLA ベースのレート制限・OAuth 2.0・JWT・IP Allowlist)
10. `governance`: API Governance(ルールセット・プロファイルの画面)、Exchange のクライアントアプリケーションと契約(Contracts)の画面
11. `monitoring`: Anypoint Monitoring(組み込みダッシュボード・アラートの作成画面)、API Manager の API 分析(Analytics)
12. `cicd`: Runtime Manager のアプリの Properties(プロパティ・安全なプロパティ)画面
13. `events`: Anypoint MQ のキューの一覧(トライアルで使えなければ missing)
