from lib import Fig, fig


@fig("products")
def _():
    f = Fig("fproducts", 300, "スタジオとビルダー")
    f.text(10, 22, "スタジオ(チャネルや作業ごと)", "gta")
    st = [("Email Studio", "メール"), ("Mobile Studio", "SMS・プッシュ・LINE"),
          ("Advertising", "広告"), ("Automation Studio", "処理の自動化")]
    for i, (t, s) in enumerate(st):
        f.box(10 + (i % 2) * 165, 32 + (i // 2) * 60, 155, 52, "gba", t, [s])
    f.text(10, 170, "ビルダー(全体で共通に使う)", "gta")
    bd = [("Contact Builder", "連絡先データ"), ("Content Builder", "コンテンツ"),
          ("Journey Builder", "顧客の道筋"), ("Analytics Builder", "分析とレポート")]
    for i, (t, s) in enumerate(bd):
        f.box(10 + (i % 2) * 165, 180 + (i // 2) * 60, 155, 52, "gby", t, [s])
    return f.svg("チャネルや作業ごとの「スタジオ」と、データ・コンテンツ・分析を共通で扱う「ビルダー」を組み合わせて使います。足りない機能は拡張製品で足します。")


@fig("compliance")
def _():
    f = Fig("fcompliance", 296, "送信分類とCAN-SPAM区分")
    f.box(95, 10, 150, 50, "gby", "送信分類", ["CAN-SPAM区分を選ぶ"])
    f.box(26, 82, 288, 72, "gba", "Commercial(商用)",
          ["広告・宣伝が目的のメール", "送信時に配信停止リンクの有無をチェック"])
    f.box(26, 170, 288, 72, "gbo", "Transactional(トランザクション)",
          ["注文確認など、同意した取引のメール", "配信停止した人にも届く(オプションで除外できる)"])
    f.path([(95, 35), (14, 35), (14, 118), (22, 118)], "a")
    f.path([(245, 35), (326, 35), (326, 206), (318, 206)], "o")
    f.text(170, 266, "配信停止は10日以内に処理し、", "gts", "middle")
    f.text(170, 283, "仕組みは送信後30日以上動かす(CAN-SPAM)", "gts", "middle")
    return f.svg("商用メールは配信停止の仕組みが必須です。トランザクションメールは、配信停止した人にも届けられます。")


@fig("security-bp")
def _():
    f = Fig("fsecuritybp", 266, "セキュリティのベストプラクティス")
    f.text(170, 22, "人 → 入口 → 出口 → 保管、の順に守る", "gta", "middle")
    f.box(10, 36, 145, 76, "gba", "権限", ["必要最小限のロール", "Deny が許可より優先"])
    f.box(185, 36, 145, 76, "gby", "ログイン", ["MFA・IP許可リスト", "セッション20分"])
    f.box(185, 140, 145, 76, "gbo", "データの出口", ["持ち出し先の許可リスト", "Audit Trail で記録"])
    f.box(10, 140, 145, 76, "gbr", "保存するデータ", ["項目単位の暗号化", "データ保持ポリシー"])
    f.arrow(157, 74, 182, 74)
    f.arrow(257, 114, 257, 137)
    f.arrow(183, 178, 158, 178)
    f.text(170, 240, "そもそも保存しない機密データは", "gts", "middle")
    f.text(170, 257, "Tokenized Sending で送信時だけ渡す", "gts", "middle")
    return f.svg("権限を絞り、ログインを守り、データの出口を管理し、保存するデータは暗号化して期限を決めて持ちます。")


@fig("account")
def _():
    f = Fig("faccount", 320, "テナントとビジネスユニット")
    f.frame(6, 8, 328, 264)
    f.text(18, 28, "テナント", "gta")
    f.text(18, 46, "Enterprise 2.0 では最上位+全ビジネスユニット", "gts")
    f.box(55, 56, 230, 56, "gba", "最上位アカウント", ["EID / MID・購読者はここに保存"])
    f.arrow(170, 114, 170, 203)
    f.path([(170, 126), (90, 126), (90, 137)])
    f.path([(170, 126), (250, 126), (250, 137)])
    f.box(18, 140, 144, 52, "gby", "子ビジネスユニット", ["ブランドA(MID)"])
    f.box(178, 140, 144, 52, "gby", "子ビジネスユニット", ["ブランドB(MID)"])
    f.box(98, 206, 144, 52, "gby", "子ビジネスユニット", ["地域・店舗(MID)"])
    f.text(170, 293, "子が見られる購読者は、購読者フィルターで決まる。", "gts", "middle")
    f.text(170, 310, "共有したいものは共有フォルダーへ", "gts", "middle")
    return f.svg("Enterprise 2.0 では、購読者は最上位アカウントに保存され、ビジネスユニットごとに見られる範囲を分けます。")


@fig("users")
def _():
    f = Fig("fusers", 352, "ロールの組み合わせと権限の判定")
    f.box(110, 10, 120, 40, "gb", "ユーザー")
    roles = [("gba", "Marketing Cloud ロール", "標準ロールから1つ"),
             ("gba", "Email Studio ロール", "標準ロールから1つ"),
             ("gby", "カスタムロール・個別権限", "足りないときに追加")]
    ys = []
    for i, (c, t, s) in enumerate(roles):
        y = 66 + i * 58
        f.box(52, y, 236, 48, c, t, [s]); ys.append(y + 24)
    f.path([(110, 30), (26, 30), (26, ys[-1])], head=False)
    for yc in ys:
        f.arrow(26, yc, 49, yc)
        f.arrow(288, yc, 314, yc, head=False)
    f.path([(314, ys[0]), (314, 296), (258, 296)])
    f.box(85, 252, 170, 88, "gbr", "権限の判定",
          ["Deny があれば使えない", "未設定は拒否扱い", "許可だけなら使える"])
    return f.svg("ロールを組み合わせて権限を決めます。どこかに拒否(Deny)があれば、ほかで許可されていても使えません。")


@fig("security")
def _():
    f = Fig("fsecurity", 252, "ログインまでの守りと Audit Trail")
    steps = [("gby", "IP 許可リスト", "許可したIPのみ"), ("gby", "パスワード", "3回失敗でロック"),
             ("gba", "MFA", "もう1つの確認"), ("gbo", "ログイン後", "20分無操作で退出")]
    for i, (c, t, s) in enumerate(steps):
        y = 10 + i * 62
        f.box(10, y, 150, 46, c, t, [s])
        if i < 3: f.arrow(85, y + 47, 85, y + 59)
        f.arrow(162, y + 23, 186, y + 23, dash=True)
    f.box(190, 10, 140, 232, "gb", "Audit Trail",
          ["操作の記録", "(誰が何をしたか)", "", "Basic: 既定でオン", "30日保存", "Advanced: 60日"], step=19)
    return f.svg("ログインまでを何段階かで守り、操作は Audit Trail に記録します。SSO を使うときは、IdP 側で MFA をかけます。")


@fig("sending")
def _():
    f = Fig("fsending", 260, "送信分類・プロファイル・ドメインの関係")
    f.box(20, 10, 300, 52, "gba", "送信分類(Send Classification)", ["2つのプロファイル + CAN-SPAM区分"])
    f.box(10, 96, 155, 66, "gby", "送信者プロファイル", ["From名・Fromアドレス"])
    f.box(175, 96, 155, 66, "gby", "配信プロファイル", ["送信IP", "ヘッダーとフッター"])
    f.box(10, 196, 320, 52, "gbo", "検証済みドメイン", ["SAP・プライベートドメイン・登録ドメイン"])
    f.arrow(87, 94, 87, 65, "a")
    f.arrow(252, 94, 252, 65, "a")
    f.arrow(87, 194, 87, 165)
    f.arrow(252, 194, 252, 165)
    return f.svg("土台に検証済みドメインがあり、その上に2つのプロファイル、さらにそれをまとめた送信分類を重ねます。")


@fig("connect")
def _():
    f = Fig("fconnect", 304, "Marketing Cloud Connect")
    f.box(6, 10, 172, 80, "gba", "Sales / Service Cloud",
          ["管理パッケージを導入", "Salesforce", "システムユーザー"])
    f.box(188, 10, 146, 80, "gby", "Marketing Cloud",
          ["Engagement", "Marketing Cloud", "API ユーザー"])
    f.arrow(92, 92, 92, 254, dash=True, head=False)
    f.arrow(261, 92, 261, 254, dash=True, head=False)
    f.text(176, 112, "同期データソース", "gts", "middle")
    f.text(176, 128, "(Contact Builder)", "gts", "middle")
    f.arrow(94, 140, 258, 140, "a")
    f.text(176, 166, "メールの反応", "gts", "middle")
    f.text(176, 182, "(トラッキング)", "gts", "middle")
    f.arrow(259, 194, 95, 194, "o")
    f.text(176, 228, "CRMの画面からメール送信", "gts", "middle")
    f.arrow(94, 240, 258, 240)
    f.text(170, 278, "同期データエクステンションは、そのままでは", "gts", "middle")
    f.text(170, 295, "送信に使えない(クエリで移す)", "gts", "middle")
    return f.svg("CRM のデータを Engagement に同期して使い、メールの反応を CRM に戻します。両側にそれぞれ専用のユーザーを用意します。")


@fig("setup-home")
def _():
    f = Fig("fsetuphome", 308, "Setup の主な設定")
    f.box(122, 10, 120, 50, "gbr", "Setup", ["アカウント管理"])
    left = [("gba", "Account Settings", "住所・ヘッダー/フッター"), ("gba", "Security", "ログインとパスワード"),
            ("gby", "Installed Packages", "API 連携")]
    right = [("gba", "Business Units", "階層・ロール"), ("gby", "Key Management", "暗号化と署名のキー"),
             ("gby", "Mobile・ENS", "チャネル設定・通知")]
    for i in range(3):
        y = 76 + i * 64; yc = y + 26
        f.box(8, y, 154, 52, left[i][0], left[i][1], [left[i][2]])
        f.box(202, y, 130, 52, right[i][0], right[i][1], [right[i][2]])
        f.arrow(182, yc, 165, yc)
        f.arrow(182, yc, 199, yc)
    f.arrow(182, 62, 182, 230, head=False)
    f.text(170, 282, "購読者のプロファイル属性・プリファレンス属性は、", "gts", "middle")
    f.text(170, 299, "Setup ではなく Email Studio で作る", "gts", "middle")
    return f.svg("Setup にはアカウント全体の設定が集まっています。購読者の属性だけは Email Studio で作る点に注意します。")


@fig("subscribers")
def _():
    f = Fig("fsubscribers", 262, "購読者のステータス")
    f.box(10, 14, 120, 56, "gbo", "Active", ["送信できる"])
    f.box(200, 14, 130, 56, "gb", "Unsubscribed", ["配信停止・スパム報告"])
    f.box(10, 150, 120, 56, "gby", "Bounced", ["1回以上バウンス"])
    f.box(200, 150, 130, 56, "gbr", "Held", ["3回以上かつ15日超"])
    f.text(165, 34, "配信停止", "gts", "middle")
    f.arrow(132, 46, 197, 46, "r")
    f.arrow(40, 72, 40, 147)
    f.text(48, 114, "バウンス", "gts")
    f.arrow(132, 178, 197, 178)
    f.arrow(110, 148, 110, 73, dash=True)
    f.path([(265, 148), (265, 118), (110, 118)], dash=True, head=False)
    f.text(170, 234, "点線: Bounced や Held の人が", "gts", "middle")
    f.text(170, 251, "開封・クリックすると Active に戻る", "gts", "middle")
    return f.svg("購読者はサブスクライバーキーで見分け、ステータスで送信の可否が決まります。All Subscribers で配信停止になると、すべてのリストで停止です。")
