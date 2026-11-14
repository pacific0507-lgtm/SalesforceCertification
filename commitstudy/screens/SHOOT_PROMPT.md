# Salesforce の設定画面を撮るセッションへの指示(Mac 上で動かす)

あなたは Mac 上で動く Claude Code のセッションです。CommitStudy(Salesforce 資格の学習アプリ)のテキストに入れる、
Salesforce の実際の設定画面のスクリーンショットを撮ってください。撮った画像はリポジトリにプッシュするだけで、加工や差し込みはクラウドのセッションが行います。

## 準備
- リポジトリ: `pacific0507-lgtm/SalesforceCertification`、ブランチ `claude/dazzling-dijkstra-qyjlwm`(なければ clone して checkout。作業前に `git pull`)
- ブラウザ: Mac のブラウザで、ユーザーがログイン済みの Salesforce 組織(Trailhead Playground / Developer Edition)を使う。
  ブラウザの操作は、使えるツール(Claude in Chrome、組み込みブラウザ、computer use のどれか)で行う。ログインや多要素認証が必要になったら、ユーザーに頼む。
- 表示言語: 日本語。日本語にできない画面は英語のままでよい(ファイル名の末尾に `_en` を付ける)
- 組織のデータを変更する操作(保存・有効化・削除など)はしない。作成画面は開いて入力欄が見える状態で撮り、「キャンセル」で閉じる。

## 撮り方
- ブラウザの幅は 1280px 前後、拡大率 100%。画面全体ではなく、説明したい部分(設定のフォームや一覧)が入る範囲で撮る
- 撮影は PNG。保存先: `commitstudy/screens/raw/d360/`(科目ごとのフォルダ)
- ファイル名: `<項目id>_<連番2桁>.png`(例: `stream_01.png`)
- 個人情報(ユーザー名・メールアドレス・組織名・組織 ID)は写ったままでよい。クラウド側で隠す。ただしパスワードやトークンが写る画面は撮らない
- 撮った画像ごとに `commitstudy/screens/raw/d360/manifest.json` に1件ずつ足す:
  `{"file":"stream_01.png","sec":"stream","title":"新規データストリームの作成(コネクタの選択)","where":"Data Cloud アプリ > データストリーム > 新規","lang":"ja","note":"気づいたこと(画面が見つからない・名前が違う など)"}`
- 画面が見つからない・ライセンスがなくて開けないものは、撮らずに manifest に `{"sec":"…","title":"…","missing":"理由"}` を書く

## まず試しに撮る画面(Data 360 / Data Cloud。Data Cloud アプリ、または「設定」から)
1. `stream`: データストリームの一覧と、「新規」で開くコネクタ(データソース)の選択画面
2. `dlo`: データレイクオブジェクトの一覧と、1つを開いた詳細(項目の一覧)
3. `mapping`: データストリームの「データマッピング」画面(DLO の項目から DMO の項目へ線で結ぶ画面)
4. `space`: 設定 > Data Cloud のデータスペースの一覧
5. `idr`: ID 解決のルールセットの一覧と、一致ルール(マッチルール)の設定画面
6. `ci`: 計算済みインサイトの一覧と、作成画面(ビジュアルビルダーまたは SQL)
7. `segment`: セグメントの一覧と、セグメントビルダー(属性を条件にドラッグする画面)
8. `activation`: 有効化対象の一覧と、有効化の作成画面

## 終わったら
- `git add commitstudy/screens/raw && git commit -m "Salesforce の設定画面(Data 360)を撮る"`(メッセージ末尾に、このリポジトリのいつもの Co-Authored-By 行があれば付ける) → `git push origin claude/dazzling-dijkstra-qyjlwm`
- プッシュする前に `git pull --rebase origin claude/dazzling-dijkstra-qyjlwm` をする
- 最後に、撮れた画面・撮れなかった画面と理由を日本語で短くまとめて、ユーザーに伝える
