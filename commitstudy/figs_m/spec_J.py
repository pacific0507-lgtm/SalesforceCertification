from lib import Fig, fig


# ---- 第1章 アプリケーションネットワークと API 主導の接続 ----

@fig("appnet")
def _():
    f = Fig("mpappnet", 442, "ポイントツーポイント連携と、再利用できる API でつなぐアプリケーションネットワークの比較")
    f.frame(6, 8, 328, 166)
    f.text(18, 28, "ポイントツーポイント", "gta")
    pos = [(20, 42), (120, 42), (20, 122), (120, 122)]
    for x, y in pos:
        f.box(x, y, 60, 36, "gb", "システム", tcls="gts")
    c = [(x + 30, y + 18) for x, y in pos]
    for i in range(4):
        for j in range(i + 1, 4):
            (x1, y1), (x2, y2) = c[i], c[j]
            if y1 == y2: f.path([(x1 + 31, y1), (x2 - 31, y2)], "r", head=False)
            elif x1 == x2: f.path([(x1, y1 + 19), (x2, y2 - 19)], "r", head=False)
            else:
                sx = 1 if x2 > x1 else -1
                f.path([(x1 + sx * 22, y1 + 19), (x2 - sx * 22, y2 - 19)], "r", head=False)
    f.text(196, 70, "1対1で直接つなぐ", "gts")
    f.text(196, 98, "10個なら45本", "gtr")
    f.text(196, 126, "つなぐたびに", "gts")
    f.text(196, 144, "専用の連携を作る", "gts")
    f.frame(6, 186, 328, 246)
    f.text(18, 206, "アプリケーションネットワーク", "gta")
    for i, t in enumerate(["アプリケーション", "データ", "デバイス"]):
        x = 16 + i * 104
        f.box(x, 216, 100, 38, "gb", t, tcls="gts")
        f.arrow(x + 50, 256, x + 50, 279, "a")
    f.box(16, 282, 308, 50, "gba", "再利用できる API", ["役割ごとの層に整理(API 主導の接続)"])
    for i, t in enumerate(["再利用性", "拡張性", "ガバナンス"]):
        f.box(16 + i * 104, 344, 100, 36, "gbo", t)
    f.text(170, 404, "API Visualizer で全体をグラフ表示", "gts", "middle")
    f.text(170, 422, "直近7日間のトラフィックから描く", "gts", "middle")
    return f.svg("ポイントツーポイント連携はつなぐたびに専用の連携が必要です。再利用できる API でつなぐと、再利用性、拡張性、ガバナンスが得られます。")


@fig("layers")
def _():
    f = Fig("mplayers", 444, "API 主導の接続の3層。Experience API、Process API、System API と、それぞれの役割")
    for i, t in enumerate(["モバイルアプリ", "Web", "キオスク"]):
        x = 10 + i * 110
        f.box(x, 10, 100, 36, "gb", t, tcls="gts")
        f.arrow(x + 50, 48, x + 50, 69)
    f.box(10, 72, 320, 56, "gba", "Experience API", ["画面やデバイスに合った形式で届ける"])
    f.arrow(170, 130, 170, 151, "a")
    f.box(10, 154, 320, 56, "gba", "Process API", ["複数の System API を組み合わせる(業務ロジック)"])
    f.arrow(170, 212, 170, 233, "a")
    f.box(10, 236, 320, 56, "gbo", "System API", ["基幹システムのデータを公開し、守る"])
    for i, t in enumerate(["CRM", "ERP", "データベース"]):
        x = 10 + i * 110
        f.arrow(x + 50, 294, x + 50, 315)
        f.box(x, 318, 100, 36, "gb", t, tcls="gts")
    f.text(170, 380, "再利用性が特に高いのは System API", "gto", "middle")
    f.text(170, 404, "素通りするだけの Process API は作らない", "gtr", "middle")
    f.text(170, 428, "チャネルごとに作る前に共通化を考える", "gts", "middle")
    return f.svg("System は基幹システムの近く、Experience は利用者の近く、Process はその間で業務ロジックを組み立てます。変換、検証、集約をしない素通りの層は作りません。")


@fig("c4e")
def _():
    f = Fig("mpc4e", 470, "C4E が Exchange にアセットをパブリッシュし、各チームがセルフサービスで再利用し、指標で再利用を測る")
    f.box(10, 10, 190, 66, "gba", "C4E", ["Center for Enablement", "COE の考え方を改良"])
    f.arrow(105, 78, 105, 117, "a")
    f.text(113, 102, "パブリッシュ", "gta")
    f.box(10, 120, 190, 54, "gbo", "Anypoint Exchange", ["承認済みのアセット"])
    f.arrow(105, 176, 105, 215, "a")
    f.text(113, 200, "見つけて再利用", "gta")
    f.box(10, 218, 190, 54, "gb", "各チームの開発者", ["セルフサービス"])
    f.box(220, 120, 110, 92, "gby", "指標", ["ダウンロード", "依存アセット", "契約"])
    f.arrow(202, 147, 217, 147)
    f.path([(275, 118), (275, 43), (203, 43)], dash=True)
    f.text(283, 80, "再利用", "gts")
    f.text(283, 98, "を測る", "gts")
    f.frame(6, 292, 328, 168)
    f.text(18, 312, "MuleSoft Catalyst の3つの柱", "gta")
    f.box(18, 322, 304, 36, "gb", "ビジネス成果の特定")
    f.box(18, 366, 304, 44, "gba", "組織のイネーブルメント", ["C4E はここに入る"], step=16)
    f.box(18, 418, 304, 36, "gb", "テクノロジーの提供")
    return f.svg("C4E はベストプラクティス、再利用、セルフサービスを広めるチームです。承認済みのアセットを Exchange にパブリッシュし、使用状況とエンゲージメントの指標で再利用を確かめます。")


# ---- 第2章 Anypoint Platform の構成 ----

@fig("platform")
def _():
    f = Fig("mpplatform", 480, "コントロールプレーンとランタイムプレーンの構成と、ランタイムからのアウトバウンド接続")
    f.frame(6, 8, 328, 172)
    f.text(18, 28, "コントロールプレーン", "gta")
    f.text(18, 46, "組織・ID・設計時のメタデータ", "gts")
    for i, t in enumerate(["Design Center", "Anypoint Exchange", "API Manager", "Runtime Manager"]):
        f.box(18 + (i % 2) * 156, 56 + (i // 2) * 44, 148, 36, "gba", t)
    f.text(170, 166, "MuleSoft 管理(US・EU・Japan など)か PCE", "gts", "middle")
    f.arrow(60, 182, 60, 223, "a")
    f.text(68, 207, "デプロイ・管理", "gts")
    f.arrow(300, 223, 300, 182, "o")
    f.text(292, 207, "アウトバウンド接続", "gto", "end")
    f.frame(6, 226, 328, 172)
    f.text(18, 246, "ランタイムプレーン", "gta")
    f.text(18, 264, "Mule ランタイムエンジンが動く", "gts")
    f.box(18, 274, 148, 52, "gbo", "CloudHub 2.0", ["MuleSoft が管理"])
    f.box(174, 274, 148, 52, "gbo", "CloudHub(1.0)", ["MuleSoft が管理"])
    f.box(18, 336, 114, 52, "gby", "Runtime Fabric", ["インフラは顧客"])
    f.box(140, 336, 182, 52, "gby", "ハイブリッドスタンドアロン", ["インフラは顧客"])
    f.text(170, 422, "顧客ホストは Runtime Manager エージェントが接続", "gts", "middle")
    f.text(170, 446, "自社ネットワークへの内向きの接続は不要", "gtr", "middle")
    f.text(170, 470, "PCE で使えるのはハイブリッドスタンドアロンだけ", "gts", "middle")
    return f.svg("管理はコントロールプレーン、アプリを動かすのはランタイムプレーンで、別々の場所に置けます。顧客ホストのランタイムからはエージェントが外向きに接続します。")


@fig("orgs")
def _():
    f = Fig("mporgs", 480, "ルート組織の下のビジネスグループの入れ子、環境の種類、チームの階層")
    f.box(70, 10, 200, 50, "gba", "ルート組織", ["ID 管理(SSO)はここで設定"])
    f.path([(170, 62), (170, 74), (87, 74), (87, 93)])
    f.path([(170, 74), (252, 74), (252, 93)])
    f.box(10, 96, 155, 50, "gb", "ビジネスグループ", ["既定で無効・最大100個"])
    f.box(175, 96, 155, 50, "gb", "ビジネスグループ", ["親は1つ"])
    f.arrow(87, 148, 87, 169)
    f.box(10, 172, 155, 50, "gb", "子ビジネスグループ", ["オーナーは1人"])
    f.text(87, 244, "親の設定・シークレットは", "gtr", "middle")
    f.text(87, 262, "見られない", "gtr", "middle")
    f.arrow(252, 148, 252, 169)
    f.frame(175, 172, 155, 196)
    f.text(187, 190, "環境", "gta")
    f.box(185, 198, 135, 48, "gbo", "本番", ["公開して運用"])
    f.box(185, 254, 135, 48, "gb", "サンドボックス", ["開発とテスト"])
    f.box(185, 310, 135, 48, "gby", "デザイン", ["Design Center だけ"])
    f.box(10, 280, 155, 50, "gb", "Everyone at 組織名", ["ルートチーム"])
    f.arrow(87, 332, 87, 353)
    f.box(10, 356, 155, 50, "gb", "子チーム", ["親の権限を引き継ぐ"])
    f.text(170, 430, "環境の種類はあとから変えられない", "gtr", "middle")
    f.text(170, 452, "ロールはビジネスグループごと", "gts", "middle")
    f.text(170, 470, "チームはビジネスグループをまたげる", "gts", "middle")
    return f.svg("ビジネスグループは既定で無効で、使うには MuleSoft の担当者に有効にしてもらいます。環境へのアクセスはユーザーに直接与えず、ロールなどの権限を通じて与えます。")


# ---- 第3章 API の設計と Exchange ----

@fig("spec")
def _():
    f = Fig("mpspec", 476, "API Designer で仕様を書き、モックサービスと動作ヘッダーで実装前に試す流れ")
    f.box(10, 10, 155, 50, "gb", "API フラグメント", ["Exchange 依存関係"])
    f.box(175, 10, 155, 50, "gb", "ルールセット", ["ガバナンスの検証"])
    f.arrow(87, 62, 87, 87)
    f.arrow(252, 62, 252, 87)
    f.box(10, 90, 320, 76, "gba", "API Designer", ["RAML 0.8 / 1.0・OAS 2.0 / 3.0", "AsyncAPI 2.0 / 2.6(イベント駆動)"])
    f.arrow(170, 168, 170, 199, "a")
    f.text(178, 188, "実装する前に", "gts")
    f.box(10, 202, 320, 52, "gbo", "モックサービス", ["仕様のステータスコードと例を返す"])
    f.frame(6, 268, 328, 146)
    f.text(18, 288, "動作ヘッダーでまねる", "gta")
    rows = [("MS2-Delay", "遅延(タイムアウト)"), ("MS2-Error-Rate", "エラーの確率 0〜1"),
            ("MS2-Error-Level", "4XX・5XX・ALL"), ("MS2-Status-Code", "ステータスを絞る")]
    for i, (h, d) in enumerate(rows):
        y = 314 + i * 26
        f.text(18, y, h, "gt")
        f.text(150, y, d, "gts")
    f.text(170, 438, "内部 URL には認可ヘッダーが必要", "gts", "middle")
    f.text(170, 462, "社外と共有するなら Make Public", "gta", "middle")
    return f.svg("共通のデータ型やセキュリティスキームは API フラグメントとして取り込みます。モックサービスに動作ヘッダーを付けると、遅延やエラーの場面を再現できます。")


@fig("exchange")
def _():
    f = Fig("mpexchange", 424, "Exchange のライフサイクル状態の移行と、Exchange の権限")
    f.box(10, 10, 320, 66, "gby", "開発(development)", ["同じ GAV で再公開すると上書き", "Studio や API Manager からは使われない"])
    f.arrow(45, 78, 45, 121, "a")
    f.text(53, 104, "昇格", "gta")
    f.path([(125, 121), (125, 80)], "r", dash=True)
    f.cross(125, 100)
    f.text(140, 104, "戻せない", "gtr")
    f.box(10, 124, 150, 88, "gbo", "安定(stable)", ["作成時の既定", "上書きできない", "7日後は論理削除"])
    f.box(180, 124, 150, 88, "gb", "非推奨(deprecated)", ["status だけが違う", "管理者だけが設定"])
    f.arrow(162, 156, 177, 156, "a")
    f.arrow(177, 182, 162, 182, "a")
    f.text(170, 236, "依存先が development なら昇格できない", "gtr", "middle")
    f.frame(6, 254, 328, 162)
    f.text(18, 274, "Exchange の権限", "gta")
    rows = [("Viewers", "表示・ダウンロード"), ("Contributors", "+ アセットの作成"),
            ("Administrators", "+ 共有・非推奨化・削除"), ("Creator", "作成だけ(自分のアセット)")]
    for i, (h, d) in enumerate(rows):
        y = 302 + i * 34
        f.text(18, y, h, "gtb")
        f.text(130, y, d, "gts")
    return f.svg("状態の移行は development から stable、stable と deprecated の行き来だけです。stable は上書きできないので、直すときは新しいバージョンを出します。")


@fig("versioning")
def _():
    f = Fig("mpversioning", 446, "セマンティックバージョニングで上げる番号と、API バージョンや API インスタンスとの関係")
    f.text(170, 20, "アセットバージョン 2.4.6", "gta", "middle")
    cols = [("メジャー 2", "gbr", ["後方互換を壊す", "必須の引数の追加"]),
            ("マイナー 4", "gby", ["後方互換", "任意の要素の追加"]),
            ("パッチ 6", "gbo", ["バグ修正", "ドキュメント更新"])]
    for i, (t, c, s) in enumerate(cols):
        f.box(8 + i * 110, 30, 104, 78, c, t, s)
    f.text(10, 140, "API バージョンとメジャーをそろえる", "gta")
    f.box(10, 150, 100, 44, "gba", "v1")
    f.arrow(112, 172, 147, 172, "o")
    f.box(150, 150, 180, 44, "gbo", "1.0.0・1.0.1・1.1.1")
    f.box(10, 202, 100, 44, "gba", "v2")
    f.path([(112, 224), (147, 224)], "r", dash=True)
    f.cross(130, 224, 5)
    f.box(150, 202, 180, 44, "gbr", "1.0.1", ["認められない"], step=15)
    f.text(10, 280, "API Manager の API インスタンス", "gta")
    f.box(10, 290, 155, 56, "gbo", "1.3.0 → 1.4.0", ["同じメジャーなら変更可"])
    f.box(175, 290, 155, 56, "gbr", "1.3.0 → 2.0.0", ["新しい API インスタンス"])
    f.text(170, 376, "URL にはメジャーだけを v1 のように入れる", "gts", "middle")
    f.text(170, 400, "v1.2 のようなドット表記は避ける", "gtr", "middle")
    f.text(170, 424, "stable で使った番号は再利用できない", "gts", "middle")
    return f.svg("後方互換を壊す変更だけメジャーを上げます。メジャーが変わるときは、API Manager でも新しい API インスタンスを作ります。")


# ---- 第4章 実装と連携のパターン ----

@fig("impl")
def _():
    f = Fig("mpimpl", 470, "APIkit が API 仕様から生成するメインフローとリソースごとのフロー、要求の流れ")
    f.box(10, 10, 130, 46, "gb", "API 仕様", ["RAML・OAS"], step=16)
    f.arrow(142, 33, 197, 33, "a")
    f.text(170, 26, "生成", "gts", "middle")
    f.box(200, 10, 130, 46, "gba", "APIkit", ["ひな形を作る"], step=16)
    f.box(10, 76, 320, 48, "gby", "API ゲートウェイのポリシー", ["認証などのセキュリティ"])
    f.arrow(87, 126, 87, 169)
    f.frame(6, 144, 328, 178)
    f.text(322, 162, "メインフロー", "gta", "end")
    f.box(18, 172, 140, 40, "gb", "HTTP リスナー")
    f.arrow(88, 214, 88, 235)
    f.box(18, 238, 140, 72, "gba", "APIkit Router", ["仕様と照らして検証", "フローへ振り分け"])
    f.box(176, 238, 146, 72, "gbr", "エラーハンドラー", ["400 BAD_REQUEST", "501 NOT_IMPLEMENTED"])
    f.arrow(160, 274, 173, 274, "r")
    f.arrow(88, 312, 88, 349, "a")
    f.box(10, 352, 320, 66, "gb", "リソースごとのフロー", ["操作・リソース・コンテンツタイプごと", "ソースなし・中身はモック実装"])
    f.text(170, 446, "Router は認証などのセキュリティを検証しない", "gtr", "middle")
    return f.svg("APIkit Router は要求を仕様と照らして検証し、リソースごとのフローへ振り分けます。認証などのセキュリティは、Router の手前で API ゲートウェイのポリシーが受け持ちます。")


@fig("events")
def _():
    f = Fig("mpevents", 470, "Anypoint MQ のメッセージエクスチェンジ、標準キューと FIFO キュー、デッドレターキューへの流れ")
    f.box(95, 10, 150, 36, "gb", "送る側のアプリ")
    f.arrow(170, 48, 170, 65, "a")
    f.box(10, 68, 320, 52, "gba", "メッセージエクスチェンジ", ["1つのメッセージを複数のキューへ"])
    f.arrow(62, 122, 62, 143, "a")
    f.arrow(177, 122, 177, 143, "a")
    f.path([(282, 122), (282, 143)], "r", dash=True)
    f.cross(282, 131, 5)
    f.box(10, 146, 105, 52, "gb", "標準キュー", ["少なくとも1回"])
    f.box(125, 146, 105, 52, "gb", "標準キュー", ["少なくとも1回"])
    f.box(240, 146, 90, 52, "gby", "FIFO キュー", ["正確に1回"])
    f.text(285, 218, "バインド", "gtr", "middle")
    f.text(285, 236, "できない", "gtr", "middle")
    f.arrow(70, 200, 70, 233, "a")
    f.arrow(177, 200, 177, 233, "a")
    f.box(40, 236, 190, 52, "gbo", "受ける側のアプリ", ["AUTO なら失敗で NACK"])
    f.path([(24, 200), (24, 337)], "r")
    f.text(32, 314, "配信試行の既定10回", "gtr")
    f.box(10, 340, 220, 52, "gbr", "デッドレターキュー", ["同じ種類・リージョン・環境"])
    f.text(170, 420, "メッセージは最大 10 MB・TTL は最大2週間", "gts", "middle")
    f.text(170, 446, "IMMEDIATE は処理前に ACK(再配信されない)", "gtr", "middle")
    return f.svg("1つのイベントを複数の受け手に配るなら標準キューとメッセージエクスチェンジです。FIFO キューはエクスチェンジにバインドできず、配信できなかったメッセージは DLQ に回ります。")


@fig("resilience")
def _():
    f = Fig("mpresilience", 412, "On Error Propagate と On Error Continue の違い、再試行の3つの仕組み、冪等性")
    f.text(10, 20, "エラー処理", "gta")
    f.box(10, 28, 155, 66, "gbr", "On Error Propagate", ["上位に伝える・失敗扱い", "ロールバック"])
    f.box(175, 28, 155, 66, "gbo", "On Error Continue", ["成功として扱う", "コミット"])
    f.text(170, 114, "何も設定しないと Propagate と同じ", "gts", "middle")
    f.text(10, 144, "再試行", "gta")
    f.box(10, 152, 320, 58, "gb", "Until Successful スコープ", ["成功するまで再試行(既定の間隔1分)", "使い切ると MULE:RETRY_EXHAUSTED"], step=16)
    f.box(10, 216, 320, 42, "gb", "再接続戦略", ["コネクタの接続失敗(既定は None)"], step=16)
    f.box(10, 264, 320, 42, "gb", "再配信ポリシー", ["既定5回で MULE:REDELIVERY_EXHAUSTED"], step=16)
    f.text(10, 332, "冪等性", "gta")
    f.box(10, 340, 320, 62, "gba", "Idempotent Message Validator", ["ID の既定は #[correlationId]", "重複は MULE:DUPLICATE_MESSAGE"], step=16)
    return f.svg("失敗を呼び出し元に伝えるなら On Error Propagate、成功として返すなら On Error Continue です。再試行するなら、二重処理を防ぐ冪等性もセットで考えます。")
