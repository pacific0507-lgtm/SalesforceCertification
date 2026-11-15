# 撮影指示: Agentforce Sales コンサルタント(afsales)

共通のルールは `commitstudy/screens/SHOOT_PROMPT.md` の「準備」「撮り方」「終わったら」に従う(読んでから始める)。違うのは次の点だけ。
- 保存先: `commitstudy/screens/raw/afsales/`、manifest も `commitstudy/screens/raw/afsales/manifest.json`
- 組織: Data 360 と同じ Developer Edition(日本語表示)でよい。営業の機能(Sales Cloud)が入っている組織
- コミットメッセージ: 「Salesforce の設定画面(Agentforce Sales)を撮る」
- 組織のデータを変える操作はしない(テリトリーモデルの有効化・売上予測の有効化など、元に戻しにくい設定は特に)。設定ページは開いて見るだけ。新規作成画面は開いて「キャンセル」

## 撮る画面(項目id: 内容。見つからない・ライセンスがないものは manifest に missing で)
1. `territory`: 設定 > テリトリー設定(エンタープライズテリトリー管理)。テリトリーモデルの一覧、テリトリー種別の一覧
2. `forecast`: 設定 > 売上予測の設定(売上予測種別・売上予測期間・調整の設定が並ぶ画面)。売上予測タブ(あれば)
3. `forecast`: パイプラインインスペクション(商談タブのリストビュー切り替え、または設定 > パイプラインインスペクション)
4. `reports`: レポートの新規作成(レポートタイプの選択)、ダッシュボードの新規作成(コンポーネントの追加画面)
5. `leads`: 設定 > リード > リード割り当てルール、Web-to-リード の設定画面、リードの取引開始の画面(取引開始ボタンで開くダイアログ。開いたらキャンセル)
6. `opps`: 設定 > 商談 > セールスプロセス、パス(パスの設定)、商談チームの設定
7. `quotes`: 設定 > 見積の設定、価格表(標準価格表)の画面、商品の新規作成画面
8. `security`: 設定 > 共有設定(組織の共有設定のデフォルトの表)、ロール階層、権限セットの一覧
9. `quality`: 設定 > 重複管理 > 一致ルール・重複ルール、入力規則の新規作成画面(オブジェクトマネージャーから)
10. `predictive`: 設定 > Einstein リードスコアリング、Einstein 商談スコアリング(有効化はしない)
11. `generative`: 設定 > Agentforce エージェント(営業向けのエージェント・Sales Development Representative など)、Einstein 営業メール/通話の要約の設定(あれば)
12. `trust`: 設定 > Einstein Trust Layer(またはデータマスキングの設定)
13. `extend`: 設定 > Einstein 活動キャプチャ、Slack 連携(Sales Cloud for Slack)の設定ページ(あれば)
14. `products`: Sales Engagement(リズム/ケイデンス)の画面(ライセンスがなければ missing)
