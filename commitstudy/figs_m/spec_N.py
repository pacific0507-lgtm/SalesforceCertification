"""Agentforce Service コンサルタント(afsvc)の図。1項目に1枚。figs_m/apply_afsvc.py で chapters.json に入れる。"""
from lib import Fig, fig


# ---- 第1章 業界知識と導入戦略 ----
@fig("kpi")
def _():
    f = Fig("svkpi", 330, "主なKPIと、その数字を動かす機能・見る場所")
    f.text(71, 20, "指標", "gts", "middle")
    f.text(245, 20, "効く機能", "gts", "middle")
    rows = [
        ("処理時間 AHT", "Omni-Channel", "スキルで配る"),
        ("初回解決率 FCR", "Knowledge", "記事の推奨"),
        ("回避率", "Agentforce", "Service Agent"),
        ("待ち時間 ASA", "キューの変更", "空いた人を回す"),
    ]
    y = 30
    for l, r, sub in rows:
        f.box(10, y, 122, 44, "gb", l)
        f.box(160, y, 170, 44, "gba", r, [sub])
        f.arrow(134, y + 22, 157, y + 22, "a")
        y += 52
    f.text(18, 254, "見る場所", "gts")
    f.box(10, 262, 155, 56, "gby", "人の成績", ["Service Intelligence"])
    f.box(175, 262, 155, 56, "gbo", "AIの効果", ["Agent Analytics"])
    return f.svg("数字ごとに効く機能が違います。人の成績は Service Intelligence、AIエージェントの回避率などは Service Agent Analytics で見ます。")


@fig("outcome")
def _():
    f = Fig("svoutcome", 300, "Agentforce Service の全体像と、人とAIの分担")
    f.box(10, 10, 320, 44, "gba", "Agentforce Service(旧 Service Cloud)")
    cols = [(10, "顧客向け", ["Service Agent", "ポータル"]), (118, "担当者向け", ["Console", "スウォーミング"]), (226, "責任者向け", ["Command", "Center"])]
    for x, t, subs in cols:
        f.box(x, 84, 104, 70, "gb", t, subs)
        f.arrow(x + 52, 56, x + 52, 81)
    f.text(18, 186, "人とAIの分担", "gts")
    f.box(10, 196, 130, 68, "gby", "AIエージェント", ["定型業務を", "自律で処理"])
    f.box(200, 196, 130, 68, "gbo", "サービス担当者", ["複雑な案件と", "関係づくり"])
    f.arrow(142, 230, 197, 230, "a")
    f.text(170, 222, "要約つき", "gta", "middle")
    f.text(170, 288, "AIの回答の品質 = Knowledge の品質", "gtr", "middle")
    return f.svg("AIは定型業務、人は複雑な案件と関係づくりを担います。AIの回答の正確さは、根拠にする Knowledge の品質で決まります。")


@fig("engage")
def _():
    f = Fig("svengage", 318, "要件をニーズ・ウォンツ・期待に分け、三重の制約の中でスコープを決める")
    f.frame(10, 10, 320, 160)
    f.text(22, 30, "スコープ(荷台の大きさは決まっている)", "gts")
    f.box(22, 40, 140, 56, "gba", "ニーズ", ["必須・最初のスコープ"])
    f.box(178, 40, 140, 56, "gb", "ウォンツ", ["交渉・先送りの対象"])
    f.box(22, 104, 296, 52, "gby", "期待", ["使い方のイメージ・価値が出る時期"])
    f.text(18, 196, "三重の制約(1つを固定すると他が動く)", "gts")
    f.box(10, 206, 100, 44, "gb", "スコープ")
    f.box(120, 206, 100, 44, "gb", "スケジュール")
    f.box(230, 206, 100, 44, "gb", "コスト")
    f.arrow(112, 228, 117, 228)
    f.arrow(222, 228, 227, 228)
    f.text(170, 278, "承認のない変更の積み重ね = スコープクリープ", "gtr", "middle")
    f.text(170, 302, "まず宣言型の標準機能、足りない所だけ開発", "gta", "middle")
    return f.svg("ニーズを最初のスコープにし、ウォンツは先送りや交渉の対象にします。承認のない変更(スコープクリープ)は失敗の大きな原因です。")


@fig("deploy")
def _():
    f = Fig("svdeploy", 330, "Sandbox の4種類と更新間隔、変革管理の5段階")
    f.box(10, 10, 155, 52, "gb", "Developer", ["1日・メタデータのみ"])
    f.box(175, 10, 155, 52, "gb", "Developer Pro", ["1日・メタデータ 1GB"])
    f.box(10, 70, 155, 52, "gba", "Partial Copy", ["5日・テンプレート必須"])
    f.box(175, 70, 155, 52, "gbo", "Full", ["29日・すべてのデータ"])
    f.text(88, 142, "UAT・トレーニング", "gta", "middle")
    f.text(252, 142, "性能・負荷・ステージング", "gto", "middle")
    f.box(10, 156, 320, 44, "gby", "Sandbox プレビュー", ["本番のリリースの4〜6週間前"])
    f.text(18, 230, "変革管理の5段階", "gts")
    xs = ["準備", "計画", "実施", "定着", "分析"]
    for i, t in enumerate(xs):
        x = 10 + i * 66
        f.box(x, 240, 56, 40, "gba" if t == "定着" else "gb", t)
        if i < 4: f.arrow(x + 58, 260, x + 64, 260)
    f.text(170, 312, "定着では評価や手順書に組み込み、元に戻さない", "gts", "middle")
    return f.svg("性能テストやステージングは Full Sandbox だけです。Partial Copy は Sandbox テンプレートで決めたサンプルデータを持ちます。")


@fig("datamig")
def _():
    f = Fig("svdatamig", 330, "移行は所有者・親・子の順。ケースはデータローダ。重複管理は一致ルールと重複ルール")
    f.text(18, 20, "読み込む順番", "gts")
    f.box(10, 30, 96, 56, "gb", "所有者", ["ユーザー"])
    f.box(122, 30, 96, 56, "gb", "親", ["取引先"])
    f.box(234, 30, 96, 56, "gba", "子", ["ケースなど"])
    f.arrow(108, 58, 119, 58, "a")
    f.arrow(220, 58, 231, 58, "a")
    f.box(10, 100, 155, 56, "gby", "インポートウィザード", ["5万件まで・ケース不可"])
    f.box(175, 100, 155, 56, "gbo", "データローダ", ["大量・ケースもこちら"])
    f.text(18, 186, "重複管理", "gts")
    f.box(10, 196, 140, 56, "gba", "一致ルール", ["何を重複とみなすか"])
    f.box(190, 196, 140, 56, "gba", "重複ルール", ["警告 / ブロック"])
    f.arrow(152, 224, 187, 224, "a")
    f.text(170, 280, "1つの親に子が1万件超 = データスキュー", "gtr", "middle")
    f.text(170, 304, "削除はごみ箱に15日、大量ならハードデリート", "gts", "middle")
    return f.svg("親と所有者を先に読み込みます。ケースはデータインポートウィザードの対象外なので、データローダを使います。")


# ---- 第2章 ソリューション設計 ----
@fig("console")
def _():
    f = Fig("svconsole", 300, "Service Console の画面構成")
    f.frame(10, 10, 320, 264)
    f.box(20, 20, 150, 32, "gba", "ワークスペースタブ")
    f.box(178, 20, 82, 32, "gb", "別のタブ")
    f.box(28, 60, 90, 28, "gby", "サブタブ")
    f.box(124, 60, 90, 28, "gby", "サブタブ")
    f.box(20, 96, 216, 118, "gb", "レコードページ", ["強調表示パネル", "= コンパクトレイアウト", "Dynamic Forms"])
    f.box(244, 96, 76, 118, "gbo", "Omni", ["サイド", "バー"])
    f.box(20, 222, 300, 42, "gb", "ユーティリティバー", ["履歴・メモ・ソフトフォン"])
    return f.svg("関連レコードはサブタブで開きます。強調表示パネルの項目はコンパクトレイアウトから来ます。Omni-Channel はサイドバーに置くのが推奨です。")


@fig("cx")
def _():
    f = Fig("svcx", 316, "セルフサービスからAIエージェント、サービス担当者へ段階的に進む顧客体験")
    f.box(10, 10, 320, 52, "gb", "ヘルプセンター(Experience Cloud)", ["まず自分で記事を調べる"])
    f.box(10, 96, 320, 52, "gba", "Agentforce Service Agent", ["Enhanced Chat で24時間対応"])
    f.box(10, 188, 320, 52, "gbo", "サービス担当者", ["送信用の Omni-Channel フローで転送"])
    f.arrow(170, 64, 170, 93)
    f.text(178, 84, "分からなければ", "gts")
    f.arrow(170, 150, 170, 185, "a")
    f.text(178, 172, "会話履歴も渡る", "gta")
    f.text(18, 270, "アンケート: 作成時 = 自動レスポンスルール", "gts")
    f.text(18, 292, "クローズ時 = サポート設定(サイトが必要)", "gts")
    return f.svg("引き継ぎにはエスカレーションのサブエージェントと送信用の Omni-Channel フローを使い、会話履歴も一緒に渡ります。")


@fig("security")
def _():
    f = Fig("svsecurity", 344, "組織の共有設定で閉じ、ロール階層・共有ルール・チームで広げる")
    f.box(10, 10, 220, 40, "gb", "ケースチーム")
    f.box(10, 58, 220, 40, "gb", "共有ルール")
    f.box(10, 106, 220, 40, "gb", "ロール階層")
    f.box(10, 154, 220, 48, "gba", "組織の共有設定", ["最も厳しくする"])
    f.arrow(262, 196, 262, 16, "o")
    f.text(272, 100, "広げる", "gto")
    f.text(272, 120, "だけ", "gto")
    f.text(18, 230, "外部ユーザー: 外部の共有設定(社内以下)", "gts")
    f.text(18, 250, "+共有セット(上位ロールに広がらない)", "gts")
    f.box(10, 266, 76, 60, "gby", "暗号化", ["Shield"])
    f.box(91, 266, 76, 60, "gby", "監査", ["Field", "Audit Trail"])
    f.box(172, 266, 76, 60, "gby", "AI", ["Trust", "Layer"])
    f.box(253, 266, 77, 60, "gby", "本人確認", ["顧客確認"])
    return f.svg("共有ルールでアクセスを制限することはできません。基準を最も厳しくし、ほかの機能で広げます。")


# ---- 第3章 ナレッジ管理と受付・対話チャネル ----
@fig("knowledge")
def _():
    f = Fig("svknowledge", 318, "記事の版のライフサイクルと公開チャネル")
    f.box(10, 10, 96, 56, "gb", "下書き", ["Draft"])
    f.box(122, 10, 96, 56, "gba", "公開済み", ["Published"])
    f.box(234, 10, 96, 56, "gby", "アーカイブ", ["Archived"])
    f.arrow(108, 30, 119, 30, "a")
    f.arrow(220, 30, 231, 30, "a")
    f.path([(170, 68), (170, 96), (58, 96), (58, 69)])
    f.text(114, 112, "Edit as Draft(公開版はそのまま)", "gts", "middle")
    f.path([(282, 68), (282, 140), (40, 140), (40, 69)], dash=True)
    f.text(282, 158, "Restore", "gts", "end")
    f.text(18, 186, "記事の削除はアーカイブ済みだけ", "gtr")
    f.text(18, 214, "公開チャネル(誰に見せるか)", "gts")
    f.box(10, 224, 155, 40, "gb", "内部アプリ")
    f.box(175, 224, 155, 40, "gb", "顧客")
    f.box(10, 270, 155, 40, "gb", "パートナー")
    f.box(175, 270, 155, 40, "gb", "公開ナレッジベース")
    return f.svg("公開中の記事を直すときは Edit as Draft で下書きを作ります。公開中の版は公開されたままです。Lightning Knowledge は一度有効にすると戻せません。")


@fig("kcs")
def _():
    f = Fig("svkcs", 300, "KCS の Solve Loop(ケース対応の中)と Evolve Loop(継続的改善)")
    f.text(18, 20, "ケース対応の中で(Solve Loop)", "gts")
    f.box(10, 30, 96, 48, "gb", "把握")
    f.box(122, 30, 96, 48, "gb", "検索")
    f.box(234, 30, 96, 48, "gb", "活用")
    f.box(122, 110, 96, 48, "gba", "作成")
    f.box(234, 110, 96, 48, "gba", "修正/フラグ")
    f.arrow(108, 54, 119, 54)
    f.arrow(220, 54, 231, 54)
    f.path([(170, 80), (170, 107)], "a")
    f.text(162, 98, "なければ", "gts", "end")
    f.path([(282, 80), (282, 107)], "a")
    f.box(10, 190, 320, 56, "gbo", "Evolve Loop(継続的改善)", ["検索のギャップ・リンク率を見る"])
    f.arrow(170, 160, 170, 187)
    f.text(170, 280, "記事の作成数は良い指標ではない", "gtr", "middle")
    return f.svg("担当者が対応しながら記事を作り、直します。マネージャーは検索のギャップやリンク率を見てプロセスを改善します。")


@fig("intake")
def _():
    f = Fig("svintake", 334, "受付チャネルからケースを作り、自動レスポンスと割り当てルールで振り分ける")
    f.box(10, 10, 155, 52, "gb", "Email-to-Case", ["25 MB 未満"])
    f.box(175, 10, 155, 52, "gb", "Web-to-Case", ["24時間で5,000件"])
    f.box(10, 96, 320, 44, "gba", "ケース")
    f.arrow(87, 64, 87, 93)
    f.arrow(252, 64, 252, 93)
    f.box(10, 176, 155, 56, "gby", "自動レスポンス", ["受付確認メール"])
    f.box(175, 176, 155, 56, "gbo", "割り当てルール", ["ユーザー / キュー"])
    f.arrow(87, 142, 87, 173, "a")
    f.arrow(252, 142, 252, 173, "a")
    f.text(170, 262, "どちらもケース用に有効は1つだけ", "gtr", "middle")
    f.text(170, 286, "エントリは上から評価・最初の一致で止まる", "gts", "middle")
    f.text(170, 310, "最後に条件なしのエントリを置く", "gta", "middle")
    return f.svg("Web-to-Case の上限を超えた分は保留キューに入ります。ルールエントリは上から評価され、最初に一致したところで止まります。")


@fig("routing")
def _():
    f = Fig("svrouting", 334, "Omni-Channel のルーティングと、ルーティングモデルの違い")
    f.box(10, 10, 100, 52, "gb", "作業項目", ["ケース・会話"])
    f.box(130, 10, 200, 52, "gba", "Omni-Channel フロー", ["Route Work で振り分け"])
    f.arrow(112, 36, 127, 36, "a")
    f.box(10, 96, 155, 52, "gb", "キュー", ["キューのメンバーへ"])
    f.box(175, 96, 155, 52, "gb", "スキル", ["全スキルを持つ人へ"])
    f.arrow(200, 64, 87, 93)
    f.arrow(260, 64, 252, 93)
    f.box(10, 182, 320, 44, "gbo", "空きキャパシティのある担当者")
    f.arrow(87, 150, 87, 179)
    f.arrow(252, 150, 252, 179)
    f.box(10, 248, 155, 52, "gby", "Least Active", ["使用中が最も少ない人"])
    f.box(175, 248, 155, 52, "gby", "Most Available", ["空きが最も多い人"])
    f.text(170, 322, "同点なら最も長く作業を受けていない人", "gts", "middle")
    return f.svg("ルーティングの優先度は数字が小さいほど先です。言語と製品など複数の条件を満たす人に配るならスキルベースです。")


@fig("messaging")
def _():
    f = Fig("svmessaging", 316, "WhatsApp の24時間のカスタマーケアウィンドウと、音声の2つの選択肢")
    f.text(18, 20, "WhatsApp", "gts")
    f.box(10, 30, 96, 52, "gb", "顧客の", ["メッセージ"])
    f.box(116, 30, 104, 52, "gbo", "24時間", ["自由に返信"])
    f.box(230, 30, 100, 52, "gbr", "過ぎたら", ["承認済みのみ"])
    f.arrow(108, 56, 113, 56)
    f.arrow(222, 56, 227, 56)
    f.text(170, 104, "テンプレートは Meta の承認(最大1日)", "gts", "middle")
    f.text(18, 140, "音声", "gts")
    f.box(10, 150, 155, 92, "gba", "Partner", ["Contact Center", "Amazon Connect", "など外部と連携"])
    f.box(175, 150, 155, 92, "gby", "Agentforce", ["Contact Center", "Voice", "Salesforce 組み込み"])
    f.text(170, 270, "Legacy Chat は2026年2月14日に終了", "gtr", "middle")
    f.text(170, 294, "移行先は Enhanced Chat(非同期)", "gta", "middle")
    return f.svg("WhatsApp は24時間を過ぎると承認済みテンプレートでしか送れません。既存のコンタクトセンターを生かすなら Partner Contact Center です。")


@fig("agents")
def _():
    f = Fig("svagents", 340, "Agentforce Service Agent の受信、サブエージェント、本人確認、人への引き継ぎ")
    f.box(10, 10, 110, 52, "gb", "受信用フロー", ["inbound"])
    f.box(140, 10, 190, 52, "gba", "Service Agent", ["受信の会話だけ・72時間"])
    f.arrow(122, 36, 137, 36, "a")
    f.frame(140, 76, 190, 150)
    f.text(152, 96, "サブエージェント(旧称トピック)", "gts")
    f.box(150, 104, 170, 52, "gby", "顧客確認", ["コードは5分有効"])
    f.box(150, 164, 170, 52, "gb", "個人データのアクション")
    f.arrow(235, 158, 235, 161)
    f.box(10, 104, 120, 112, "gbr", "Escalation", ["人へ引き継ぐ", "サブエージェント", "試行は1回"])
    f.box(10, 252, 155, 52, "gb", "送信用フロー", ["outbound"])
    f.box(175, 252, 155, 52, "gbo", "サービス担当者", ["会話履歴も渡る"])
    f.arrow(70, 218, 70, 249, "r")
    f.arrow(167, 278, 172, 278, "a")
    f.text(170, 328, "Einstein Bots は2026年8月17日から保守モード", "gts", "middle")
    return f.svg("本人確認ができるまで個人データを扱うアクションを使えないようにします。Escalation サブエージェントがないと人へ引き継げません。")


# ---- 第4章 ケース管理 ----
@fig("caseproc")
def _():
    f = Fig("svcaseproc", 330, "レコードタイプとサポートプロセス、ケースの作成からクローズまで")
    f.box(10, 10, 155, 52, "gb", "レコードタイプ", ["問い合わせの種類"])
    f.box(175, 10, 155, 52, "gba", "サポートプロセス", ["使う状況の値"])
    f.arrow(167, 36, 172, 36, "a")
    f.box(10, 96, 96, 48, "gb", "新規")
    f.box(122, 96, 96, 48, "gb", "対応中")
    f.box(234, 96, 96, 48, "gbo", "クローズ")
    f.arrow(108, 120, 119, 120)
    f.arrow(220, 120, 231, 120)
    f.box(10, 176, 155, 56, "gby", "割り当てルール", ["作成時にキューへ"])
    f.box(175, 176, 155, 56, "gbr", "エスカレーション", ["時間が経っても未解決"])
    f.arrow(58, 174, 58, 147)
    f.arrow(252, 174, 170, 147)
    f.text(170, 262, "マージは最大3件・元に戻せない", "gts", "middle")
    f.text(170, 286, "Close Case アクションでクローズの値を選ぶ", "gts", "middle")
    f.text(170, 310, "大規模な障害はインシデントで(Ch5·4)", "gta", "middle")
    return f.svg("問い合わせの種類ごとに状況の値を変えるなら、サポートプロセスを作ってレコードタイプに割り当てます。")


@fig("deflect")
def _():
    f = Fig("svdeflect", 320, "Contact Support Form と Case Deflection コンポーネントでケースを回避する流れ")
    f.box(10, 10, 320, 52, "gb", "Contact Support Form", ["件名と説明を入力"])
    f.box(10, 96, 320, 52, "gba", "Case Deflection", ["入力中の文字で記事を表示(既定6件)"])
    f.arrow(170, 64, 170, 93, "a")
    f.box(10, 184, 155, 52, "gbo", "解決した", ["ケース作成をやめる"])
    f.box(175, 184, 155, 52, "gb", "解決しない", ["ケースを作成"])
    f.arrow(87, 150, 87, 181, "o")
    f.arrow(252, 150, 252, 181)
    f.text(170, 266, "ゲストの検索は記事のタイトルだけ", "gtr", "middle")
    f.text(170, 292, "効果は Case Deflection Dashboard", "gta", "middle")
    return f.svg("フォームに入力中に記事を出すのが Case Deflection コンポーネントです。効果は Case Deflection Dashboard などで測ります。")


@fig("entitle")
def _():
    f = Fig("sventitle", 336, "エンタイトルメント・プロセス・マイルストンの関係と営業時間の優先順位")
    f.box(10, 10, 96, 52, "gb", "取引先")
    f.box(122, 10, 208, 52, "gba", "エンタイトルメント", ["サポートを受ける権利"])
    f.arrow(108, 36, 119, 36)
    f.box(122, 90, 208, 52, "gba", "エンタイトルメント", ["プロセス(時間割)"])
    f.arrow(226, 64, 226, 87)
    f.box(122, 170, 98, 52, "gby", "初回応答", ["マイルストン"])
    f.box(232, 170, 98, 52, "gby", "解決", ["マイルストン"])
    f.arrow(170, 144, 170, 167)
    f.arrow(282, 144, 282, 167)
    f.box(10, 90, 96, 132, "gb", "アクション", ["成功", "警告", "違反"])
    f.text(18, 254, "営業時間の優先順位", "gts")
    f.box(10, 264, 100, 40, "gba", "マイルストン")
    f.box(120, 264, 100, 40, "gb", "プロセス")
    f.box(230, 264, 100, 40, "gb", "ケース")
    f.arrow(112, 284, 117, 284)
    f.arrow(222, 284, 227, 284)
    f.text(170, 326, "マイルストンは自動では完了しない", "gtr", "middle")
    return f.svg("サポートを受ける権利がエンタイトルメント、約束の時間がマイルストン、その時間割がエンタイトルメントプロセスです。")


@fig("automation")
def _():
    f = Fig("svautomation", 322, "誰が動かすか・何を自動にするかで選ぶ自動化の道具")
    f.text(18, 20, "サービス担当者が動かす", "gts")
    f.box(10, 30, 100, 56, "gba", "マクロ", ["複数の操作"])
    f.box(120, 30, 100, 56, "gba", "クイック", ["テキスト・文章"])
    f.box(230, 30, 100, 56, "gba", "画面フロー", ["手順の案内"])
    f.text(18, 116, "システムが動かす", "gts")
    f.box(10, 126, 320, 48, "gb", "レコードトリガフロー", ["作成・更新で自動"])
    f.text(18, 204, "AI(Einstein for Service)", "gts")
    f.box(10, 214, 100, 70, "gby", "入力", ["Case", "Classifi-", "cation"])
    f.box(120, 214, 100, 70, "gby", "要約", ["Work", "Summaries"])
    f.box(230, 214, 100, 70, "gby", "返信", ["Service", "Replies"])
    f.text(170, 310, "確認なしで保存できるのは Case Classification", "gts", "middle")
    return f.svg("担当者のワンクリックならマクロ、人の操作なしならレコードトリガフローです。要約は Work Summaries、返信の下書きは Service Replies です。")


# ---- 第5章 分析とインテグレーション ----
@fig("reports")
def _():
    f = Fig("svreports", 324, "ダッシュボードの実行ユーザーと、関係者ごとの見せ方")
    f.text(18, 20, "View Dashboard As", "gts")
    f.box(10, 30, 155, 60, "gb", "自分 / 別の人", ["全員に同じデータ"])
    f.box(175, 30, 155, 60, "gba", "閲覧者", ["各自の権限で表示"])
    f.box(10, 124, 155, 52, "gby", "経営層", ["全体の数字"])
    f.box(175, 124, 155, 52, "gbo", "担当者・SV", ["動的ダッシュボード"])
    f.arrow(87, 92, 87, 121)
    f.arrow(252, 92, 252, 121, "a")
    f.text(252, 200, "購読・スケジュール不可", "gtr", "middle")
    f.text(18, 236, "サポート向けのレポートタイプ", "gts")
    f.box(10, 246, 100, 56, "gb", "変更前後", ["Case History"])
    f.box(120, 246, 100, 56, "gb", "経過時間", ["Lifecycle"])
    f.box(230, 246, 100, 56, "gb", "時間の変化", ["Historical", "Trending"])
    return f.svg("実行ユーザーを閲覧者にしたものが動的ダッシュボードです。実行ユーザーを管理者に固定すると、見えすぎに注意が必要です。")


@fig("analytics")
def _():
    f = Fig("svanalytics", 330, "今・過去・AIエージェントで見る場所を分ける")
    f.box(10, 10, 96, 56, "gba", "今", ["リアルタイム"])
    f.box(122, 10, 208, 56, "gba", "Command Center", ["for Service", "旧称 Omni Supervisor"])
    f.box(10, 80, 96, 56, "gb", "過去", ["実績"])
    f.box(122, 80, 208, 56, "gb", "レポート", ["AgentWork・CRM Analytics"])
    f.box(10, 150, 96, 56, "gby", "AI", ["エージェント"])
    f.box(122, 150, 208, 56, "gby", "Agent Analytics", ["回避率・エスカレーション率"])
    for y in (38, 108, 178):
        f.arrow(108, y, 119, y)
    f.text(18, 236, "表示されるタブ", "gts")
    f.box(10, 246, 155, 56, "gb", "Queues Backlog", ["キューベース"])
    f.box(175, 246, 155, 56, "gb", "Skills Backlog", ["スキルベースのみ"])
    return f.svg("今どうなっているかは Command Center for Service、先月どうだったかはレポート、AIエージェントの効果は Agent Analytics で見ます。")


@fig("integ")
def _():
    f = Fig("svinteg", 330, "外部データはコピーせず参照するか、Data 360 のゼロコピーか。電話はどの Amazon Connect か")
    f.text(18, 20, "外部データ(コピーしない)", "gts")
    f.box(10, 30, 155, 70, "gba", "Salesforce", ["Connect", "外部オブジェクト"])
    f.box(175, 30, 155, 70, "gba", "Data 360", ["ゼロコピー", "Snowflake など"])
    f.text(88, 122, "大量・少量ずつ・最新", "gts", "middle")
    f.text(252, 122, "複製せずにクエリ", "gts", "middle")
    f.text(18, 158, "電話(Partner Contact Center)", "gts")
    f.box(10, 168, 155, 56, "gb", "構築を任せる", ["with Amazon Connect"])
    f.box(175, 168, 155, 56, "gb", "既存を使う", ["Bring Your Own"])
    f.box(10, 248, 320, 56, "gby", "通話のルーティングはプロバイダー側", ["Salesforce のキューを対応付ける"])
    return f.svg("コピーしたくない大量のデータを少しずつリアルタイムで使うなら Salesforce Connect です。既存の Amazon Connect を使うなら Bring Your Own です。")


@fig("slack")
def _():
    f = Fig("svslack", 334, "階層型サポートとスウォーミング、ケースとインシデントの関係")
    f.box(10, 10, 155, 60, "gb", "階層型", ["1次→2次→3次", "説明し直し"])
    f.box(175, 10, 155, 60, "gba", "スウォーミング", ["専門家を集める", "Slack で協業"])
    f.arrow(167, 40, 172, 40, "a")
    f.text(330, 92, "Expert Finder で専門家を探す", "gts", "end")
    f.text(18, 128, "Customer Service Incident Management", "gts")
    f.box(10, 138, 96, 52, "gb", "ケース", ["多数"])
    f.box(122, 138, 208, 52, "gbr", "インシデント", ["多くの顧客に及ぶ障害"])
    f.arrow(108, 164, 119, 164)
    f.box(122, 214, 208, 44, "gby", "問題", ["根本原因の分析"])
    f.box(122, 276, 208, 44, "gbo", "変更要求", ["修正を実施"])
    f.arrow(226, 192, 226, 211)
    f.arrow(226, 260, 226, 273)
    return f.svg("1件の問い合わせはケース、多くの顧客に及ぶ障害はインシデントです。原因分析は問題、修正の実施は変更要求で行います。")
