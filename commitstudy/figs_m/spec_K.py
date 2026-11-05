from lib import Fig, fig


# ---- 第5章 デプロイ ----

@fig("deployopts")
def _():
    f = Fig("mpdeployopts", 400, "5つのデプロイ先ごとに、ランタイムをホストする側と管理機能(コントロールプレーン)をホストする側を比べる")
    f.text(75, 20, "デプロイ先", "gts", "middle")
    f.text(195, 20, "ランタイム", "gts", "middle")
    f.text(290, 20, "管理機能", "gts", "middle")
    rows = [
        ("CloudHub 2.0", "コンテナ型", "MuleSoft", "MuleSoft"),
        ("CloudHub", "(CloudHub 1.0)", "MuleSoft", "MuleSoft"),
        ("ハイブリッド", "自社の Mule サーバー", "顧客", "MuleSoft"),
        ("Runtime Fabric", "顧客の Kubernetes", "顧客", "MuleSoft"),
        ("PCE", "オンプレミスなど", "顧客", "顧客"),
    ]
    for i, (t, s, r, c) in enumerate(rows):
        y = 30 + i * 56
        f.box(10, y, 135, 48, "gb", t, [s])
        f.box(153, y, 84, 48, "gba" if r == "MuleSoft" else "gby", r)
        f.box(245, y, 85, 48, "gba" if c == "MuleSoft" else "gbr" if i == 4 else "gby", c)
    f.text(10, 324, "ハイブリッド: エージェントで登録", "gts")
    f.text(10, 344, "クラウドへはメタデータだけ(アプリのデータは出ない)", "gts")
    f.text(10, 368, "Runtime Fabric: イングレスと LB は顧客の責任", "gts")
    f.text(10, 390, "管理機能まで自社でホストするのは PCE だけ", "gtr")
    return f.svg("CloudHub 2.0 と CloudHub は MuleSoft がランタイムをホストし、ハイブリッド、Runtime Fabric、PCE は顧客がホストします。管理機能(コントロールプレーン)まで自社に置くのは PCE だけです。")


@fig("cloudhub")
def _():
    f = Fig("mpcloudhub", 470, "CloudHub(1.0)と CloudHub 2.0 の、実行単位、サイズ、数、ネットワーク、キュー、クラスタリングの違い")
    f.box(10, 8, 155, 36, "gby", "CloudHub(1.0)")
    f.box(175, 8, 155, 36, "gba", "CloudHub 2.0")
    rows = [
        ("実行単位", ("ワーカー", []), ("レプリカ", []), None),
        ("1つの最大サイズ", ("16 vCore", []), ("4 vCore", []), None),
        ("数の上限(1アプリ)", ("最大8ワーカー", ["合計128 vCore まで"]), ("最大8レプリカ", ["上位の契約なら16"]), None),
        ("分離されたネットワーク", ("Anypoint VPC", ["DLB の前提"]), ("プライベートスペース", ["シングルテナント"]), None),
        ("永続的な VM キュー", ("対応", []), ("非対応", ["Anypoint MQ を使う"]), (1, 0)),
        ("Mule クラスタリング", ("非対応", []), ("対応", ["2レプリカ以上"]), (0, 1)),
    ]
    y = 54
    for lab, (lt, ls), (rt, rs), ok in rows:
        f.text(170, y + 13, lab, "gts", "middle")
        h = 44 if (ls or rs) else 34
        lc = "gb" if ok is None else ("gbo" if ok[0] else "gbr")
        rc = "gb" if ok is None else ("gbo" if ok[1] else "gbr")
        f.box(10, y + 19, 155, h, lc, lt, ls)
        f.box(175, y + 19, 155, h, rc, rt, rs)
        y += 19 + h + 8
    return f.svg("ワーカーは1.0で最大16 vCore、レプリカは2.0で最大4 vCore です。永続的な VM キューと Mule クラスタリングの対応は、1.0と2.0で逆になります。")


@fig("cicd")
def _():
    f = Fig("mpcicd", 486, "Mule Maven プラグインで、テスト、パッケージ化、-DmuleDeploy の有無によるデプロイとアップロードの分かれ道")
    f.box(10, 10, 320, 50, "gb", "MUnit Maven プラグイン", ["カバレッジ基準に届かなければ failBuild"])
    f.arrow(170, 62, 170, 79, "a")
    f.box(10, 82, 320, 50, "gb", "package ゴール", ["アプリの JAR ファイルを作る"])
    f.arrow(170, 134, 170, 151, "a")
    f.box(10, 154, 320, 36, "gba", "mvn clean deploy")
    f.arrow(80, 192, 80, 213, "a")
    f.arrow(245, 192, 245, 213, "r", dash=True)
    f.box(10, 216, 140, 56, "gbo", "-DmuleDeploy あり", ["デプロイ先へ"])
    f.box(160, 216, 170, 56, "gby", "-DmuleDeploy なし", ["distributionManagement", "へアップロードだけ"])
    f.arrow(80, 274, 80, 307, "o")
    f.frame(10, 310, 320, 120)
    f.text(22, 330, "設定要素", "gta")
    f.box(20, 338, 145, 50, "gb", "CloudHub(1.0)", ["cloudHubDeployment"])
    f.box(175, 338, 145, 50, "gb", "CloudHub 2.0", ["cloudhub2Deployment"])
    f.text(247, 410, "先に Exchange に公開", "gtr", "middle")
    f.text(92, 410, "Runtime Fabric なども", "gts", "middle")
    f.text(10, 454, "優先: デプロイメント > システム > 環境", "gts")
    f.text(10, 474, "> アプリケーション > グローバル", "gts")
    return f.svg("パイプラインからは mvn clean deploy -DmuleDeploy でデプロイします。muleDeploy を付けないと distributionManagement のリポジトリへアップロードするだけです。")


# ---- 第6章 API の管理 ----

@fig("apimgr")
def _():
    f = Fig("mpapimgr", 470, "API Manager がポリシーを配る3つのゲートウェイの形:自動検出、プロキシ、Omni Gateway")
    f.box(10, 10, 320, 50, "gba", "API Manager", ["ポリシー・契約・分析"])
    f.path([(22, 62), (22, 314)], "a", head=False)
    f.frame(10, 84, 320, 176)
    f.text(320, 100, "Mule Gateway", "gta", "end")
    rows = [
        (112, "自動検出", ["apiId・flowRef"], "Mule アプリ", ["HTTP Listener が必要"]),
        (190, "プロキシ", ["アプリを前に置く"], "守る相手", ["Mule 以外のアプリ", "自動検出なしの Mule"]),
    ]
    for y, lt, ls, rt, rs in rows:
        f.arrow(22, y + 28, 37, y + 28, "a")
        f.box(40, y, 120, 56, "gba", lt, ls)
        f.arrow(162, y + 28, 177, y + 28)
        f.box(180, y, 140, 56, "gb", rt, rs)
    f.arrow(22, 314, 37, 314, "a")
    f.box(40, 280, 290, 68, "gby", "Omni Gateway(旧 Flex Gateway)", ["Envoy ベースで軽量・高速", "Mule 以外の API もどこでも"])
    f.box(40, 362, 140, 50, "gb", "接続モード", ["UI で集中管理"])
    f.box(190, 362, 140, 50, "gb", "ローカルモード", ["設定ファイル・CI/CD"])
    f.path([(110, 350), (110, 359)], head=False)
    f.path([(260, 350), (260, 359)], head=False)
    f.text(170, 438, "ゲートキーパー: ポリシー適用まで 503", "gtr", "middle")
    f.text(170, 460, "1つの Mule アプリに API インスタンスは1つ", "gts", "middle")
    return f.svg("Mule アプリは自動検出(apiId と flowRef)で、Mule 以外や自動検出のないアプリはプロキシで守ります。Omni Gateway(旧 Flex Gateway)のローカルモードは設定ファイルでポリシーを適用し、CI/CD に向きます。")


@fig("policies")
def _():
    f = Fig("mppolicies", 480, "Rate Limiting の共有の枠と SLA-based のクライアントごとの枠、Spike Control、ポリシーの実行順")
    f.text(87, 20, "Rate Limiting", "gta", "middle")
    f.text(252, 20, "SLA-based", "gta", "middle")
    for x, cx in ((10, 87), (175, 252)):
        f.box(x, 30, 72, 36, "gb", "アプリ A")
        f.box(x + 83, 30, 72, 36, "gb", "アプリ B")
    f.path([(46, 68), (46, 84), (87, 84), (87, 101)])
    f.path([(129, 68), (129, 84), (87, 84)], head=False)
    f.box(10, 104, 155, 50, "gby", "1つの枠", ["API 全体で共有"])
    f.arrow(211, 68, 211, 101)
    f.arrow(294, 68, 294, 101)
    f.box(175, 104, 72, 50, "gba", "A の枠", ["SLA 層"])
    f.box(258, 104, 72, 50, "gba", "B の枠", ["SLA 層"])
    f.text(87, 176, "識別子でグループ分けも", "gts", "middle")
    f.text(252, 176, "契約がないと拒否", "gtr", "middle")
    f.text(170, 202, "上限を超えると 429", "gtb", "middle")
    f.box(10, 216, 320, 56, "gb", "Spike Control", ["急な波をならす(待たせて再試行)", "クォータは強制しない"])
    f.text(10, 300, "実行順", "gta")
    f.box(10, 308, 74, 40, "gb", "リクエスト")
    f.arrow(86, 328, 101, 328, "a")
    f.box(104, 308, 102, 40, "gba", "自動ポリシー")
    f.arrow(208, 328, 223, 328, "a")
    f.box(226, 308, 104, 40, "gb", "API 個別")
    f.text(170, 370, "自動ポリシーは環境のすべての API に適用", "gts", "middle")
    f.text(170, 390, "API 個別は自動ポリシーより先にできない", "gts", "middle")
    f.text(10, 422, "主な拒否コード", "gta")
    f.text(10, 444, "Client ID Enforcement 401 / IP Allowlist 403", "gts")
    f.text(10, 466, "Rate Limiting・SLA-based・Spike Control 429", "gts")
    return f.svg("Rate Limiting は API 全体で1つの枠を分け合い、Rate Limiting: SLA-based は契約したクライアントごとに SLA 層の上限で数えます。Spike Control は波をならすだけで、クォータは強制しません。")


@fig("governance")
def _():
    f = Fig("mpgovernance", 508, "クライアントアプリケーションの契約の流れと、ガバナンスプロファイルで準拠状況を検証する API Governance の流れ")
    f.text(10, 20, "クライアントアプリケーションと契約", "gta")
    f.box(10, 28, 92, 50, "gb", "リクエスト", ["Exchange で"])
    f.arrow(104, 53, 121, 53)
    f.box(124, 28, 92, 50, "gby", "承認", ["自動か手動"])
    f.arrow(218, 53, 235, 53, "o")
    f.box(238, 28, 92, 50, "gbo", "契約", ["1組に1つ"])
    f.text(170, 98, "SLA 層がなければ自動承認", "gts", "middle")
    f.text(170, 116, "手動は API Manager の「契約」で承認", "gts", "middle")
    f.text(10, 146, "API Governance", "gta")
    f.box(10, 154, 320, 40, "gb", "Exchange でタグとカテゴリー")
    f.arrow(170, 196, 170, 211, "a")
    f.box(10, 214, 320, 50, "gba", "ガバナンスプロファイル", ["どのルールセットをどの API に"])
    f.arrow(80, 266, 80, 281, "a")
    f.box(10, 284, 140, 50, "gby", "下書き(Draft)", ["通知なしで試す"])
    f.arrow(152, 309, 177, 309, "a")
    f.box(180, 284, 150, 50, "gbo", "有効(Active)", ["結果を全体に表示"])
    f.arrow(255, 336, 255, 351, "a")
    f.box(10, 354, 320, 50, "gb", "準拠状況", ["準拠・非準拠・未検証"])
    f.arrow(80, 406, 80, 421)
    f.arrow(255, 406, 255, 421)
    f.box(10, 424, 140, 50, "gb", "通知メール", ["発行者・連絡先など"])
    f.box(180, 424, 150, 50, "gb", "直す", ["設計時・デプロイ時"])
    f.text(170, 498, "検証だけ。ポリシーの適用は自動ポリシー", "gtr", "middle")
    return f.svg("契約は1つのインスタンスと1つのアプリの間に1つだけです。ガバナンスプロファイルはルールセットで API を検証するだけで、ポリシーは適用しません。")


# ---- 第7章 非機能要件と監視 ----

@fig("nfr")
def _():
    f = Fig("mpnfr", 500, "AZ をまたぐ高可用性、利用者が組むリージョンをまたぐ DR、垂直・水平スケールと HPA")
    f.box(10, 10, 320, 50, "gby", "グローバルロードバランサー", ["利用者が用意する(DR は利用者の責任)"])
    f.arrow(98, 62, 98, 85)
    f.arrow(262, 62, 262, 85, dash=True)
    f.frame(10, 88, 176, 216)
    f.text(22, 108, "リージョン A", "gta")
    f.box(20, 116, 156, 48, "gb", "HTTP ロードバランサー", ["ラウンドロビン"])
    f.arrow(56, 166, 56, 189)
    f.arrow(140, 166, 140, 189)
    f.box(20, 192, 73, 56, "gba", "AZ 1", ["レプリカ"])
    f.box(103, 192, 73, 56, "gba", "AZ 2", ["レプリカ"])
    f.text(98, 272, "AZ 障害は別の AZ で", "gts", "middle")
    f.text(98, 290, "自動で再起動", "gts", "middle")
    f.box(194, 88, 136, 216, "gb", "リージョン B", ["自動では", "複製されない", "", "アクティブ-アクティブ", "か", "ウォームスタンバイ"], step=20)
    f.text(10, 330, "スケーラビリティ", "gta")
    rows = [
        ("垂直スケール", "vCore を大きく(0.1〜4)"),
        ("水平スケール", "レプリカを増やす(最大8)"),
        ("HPA", "CPU 70% を目標に自動増減"),
    ]
    for i, (t, s) in enumerate(rows):
        y = 338 + i * 46
        f.box(10, y, 110, 40, "gba" if i == 2 else "gb", t)
        f.box(128, y, 202, 40, "gb", s, tcls="gt")
    f.text(170, 490, "バッチジョブは1つのレプリカだけで動く", "gtr", "middle")
    return f.svg("レプリカを2つ以上にすると別々の AZ に置かれ、AZ 障害に耐えます。リージョン障害への備えは利用者がグローバルロードバランサーで組み、バッチジョブは台数を増やしても分散されません。")


@fig("monitoring")
def _():
    f = Fig("mpmonitoring", 438, "デプロイ先ごとの監視の準備、2系統のアラート、API Visualizer")
    f.text(10, 20, "監視を始める準備", "gta")
    rows = [
        ("CloudHub 2.0", ["Runtime Fabric"], "gbo", "準備不要", ["既定で使える"]),
        ("CloudHub(1.0)", [], "gb", "アプリごとに有効化", []),
        ("ハイブリッド", [], "gby", "エージェント", ["サーバーにインストール"]),
    ]
    for i, (lt, ls, c, rt, rs) in enumerate(rows):
        y = 28 + i * 56
        f.box(10, y, 145, 48, "gb", lt, ls)
        f.arrow(157, y + 24, 172, y + 24)
        f.box(175, y, 155, 48, c, rt, rs)
    f.text(10, 210, "アラートは2系統", "gta")
    f.box(10, 218, 320, 56, "gba", "Anypoint Monitoring のアラート", ["指標がしきい値の条件を N 分連続で満たす"])
    f.box(10, 282, 320, 56, "gby", "Runtime Manager のアラート", ["デプロイの完了・ワーカーの異常・サーバーの切断"])
    f.box(10, 360, 320, 68, "gbo", "API Visualizer", ["アプリケーションネットワークを図に", "線は過去7日間の通信・レイヤーで分類"])
    return f.svg("CloudHub 2.0 と Runtime Fabric は準備不要、CloudHub(1.0)はアプリごとの有効化、ハイブリッドはエージェントのインストールが必要です。指標のしきい値は Anypoint Monitoring、デプロイやワーカーの出来事は Runtime Manager のアラートです。")
