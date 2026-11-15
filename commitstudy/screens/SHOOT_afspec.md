# 撮影指示: Agentforce スペシャリスト(afspec)

共通のルールは `commitstudy/screens/SHOOT_PROMPT.md` の「準備」「撮り方」「終わったら」に従う(読んでから始める)。違うのは次の点だけ。
- 保存先: `commitstudy/screens/raw/afspec/`、manifest も `commitstudy/screens/raw/afspec/manifest.json`
- 組織: Data 360 と同じ Developer Edition(Agentforce と Data Cloud 付き、日本語表示)
- コミットメッセージ: 「Salesforce の設定画面(Agentforce スペシャリスト)を撮る」
- エージェントの有効化・公開、プロンプトテンプレートの有効化はしない。編集画面は開いて見るだけ。新規作成はウィザードの途中まで進めてキャンセル(保存が必要なときは、ユーザーに許可をもらってから「CommitStudy撮影用」という名前で作る)

## 撮る画面(項目id: 内容)
1. `agents`: 設定 > Agentforce エージェント(エージェントの一覧)、Agentforce の有効化の設定ページ
2. `builder`: Agentforce Builder(エージェントを開いた画面。左のサブエージェント/トピックの一覧、中央の会話プレビュー)
3. `topics`: サブエージェント(トピック)の詳細: 分類の説明・範囲・指示が並ぶ画面
4. `actions`: アクションの追加画面(標準アクション・フロー・Apex・プロンプトテンプレートから選ぶ画面)、アクションの入力/出力の設定
5. `stdagents`: 新規エージェントの作成でテンプレート(Agentforce Service Agent・Sales Development Representative など)を選ぶ画面
6. `channels`: 設定 > メッセージング設定(Enhanced Messaging のチャネル)、エージェントの「接続」設定(あれば)
7. `promptbuilder`: Prompt Builder のテンプレート一覧、新規プロンプトテンプレートの種別の選択(営業メール・項目生成・レコードの要約・フレックスなど)
8. `grounding`: プロンプトテンプレートの編集画面で、差し込み項目(リソース)を選ぶメニュー(レコードの項目・関連リスト・フロー・Apex・Data Cloud)
9. `promptbp`: プロンプトテンプレートの「プレビュー」(応答の確認)画面
10. `models`: Einstein Studio(Model Builder)のモデル一覧、BYOLLM の追加画面(あれば)
11. `datalib`: Agentforce データライブラリの一覧と新規作成画面(ナレッジ/ファイルを選ぶ)
12. `retriever`: Data Cloud の検索インデックスの一覧と作成画面、リトリーバーの一覧(Einstein Studio)
13. `testing`: Agentforce Testing Center(テストの一覧・新規テストの作成)
14. `trust`: 設定 > Einstein Trust Layer(データマスキング・監査とフィードバックの設定)
15. `observe`: Agentforce の分析/エージェントの監視(Utterance Analysis・セッションの追跡)、監査証跡の設定
16. `access`: 権限セットの一覧で Agentforce 関連(Agentforce Service Agent User など)、エージェントのユーザー(エージェントユーザー)の設定
17. `deploy`: 変更セット/パッケージでエージェントを含める画面(あれば)。Sandbox がなければ missing
