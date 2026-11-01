"""Marketing Cloud Administrator の各項目の図(SVG)。Data 360 の図と同じクラス(.gb/.gba/.gby/.gbo/.gbr/.gtb/.gts/.gl…)を使い、テーマの配色に追従する。"""
import html, re

def tw(s, fs):  # 文字幅の目安
    w = 0
    for ch in s:
        w += fs * (0.58 if ord(ch) < 0x2000 else 1.0)
    return w

class Fig:
    def __init__(self, fid, h, aria):
        self.fid, self.h, self.aria, self.el, self.warn = fid, h, aria, [], []
    def box(self, x, y, w, h, cls, title, subs=(), fs=13.5):
        self.el.append(f'<rect class="{cls}" x="{x}" y="{y}" width="{w}" height="{h}" rx="10"/>')
        lines = [title] + list(subs); n = len(lines); step = 19.5
        y0 = y + h / 2 - (n - 1) * step / 2 + 4.6
        for i, t in enumerate(lines):
            f = fs if i == 0 else 12.0
            if tw(t, f) > w - 10: self.warn.append(f"{self.fid}: 「{t}」が箱({w})からはみ出す可能性")
            c = "gtb" if i == 0 else "gts"
            self.el.append(f'<text class="{c}" x="{x + w / 2:g}" y="{y0 + i * step:.1f}" text-anchor="middle" font-size="{f}">{html.escape(t)}</text>')
    def frame(self, x, y, w, h, cls="gbd"):
        self.el.append(f'<rect class="{cls}" x="{x}" y="{y}" width="{w}" height="{h}" rx="12"/>')
    def text(self, x, y, t, cls="gts", anchor="start", fs=12.0):
        self.el.append(f'<text class="{cls}" x="{x}" y="{y}" text-anchor="{anchor}" font-size="{fs}">{html.escape(t)}</text>')
    def arrow(self, x1, y1, x2, y2, c="n", dash=False):
        cls = {"n": "gl", "a": "gla", "r": "glr", "o": "glo"}[c] if not dash else "gld"
        mk = {"n": "mk_an", "a": "mk_aa", "r": "mk_ar", "o": "mk_ao"}[c]
        self.el.append(f'<line class="{cls}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" marker-end="url(#{self.fid}-{mk})"/>')
    def svg(self, caption):
        defs = "".join(f'<marker id="{self.fid}-{m}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" class="{m}"/></marker>' for m in ("mk_aa", "mk_an", "mk_ar", "mk_ao"))
        return (f'<figure class="fig wide"><svg viewBox="0 0 640 {self.h}" role="img" aria-label="{html.escape(self.aria)}" style="max-width:800px"><defs>{defs}</defs>'
                + "".join(self.el) + f'</svg><figcaption>{html.escape(caption)}</figcaption></figure>')

FIGS = {}
def fig(sec):
    def deco(fn): FIGS[sec] = fn; return fn
    return deco

@fig("products")
def _():
    f = Fig("fproducts", 236, "スタジオとビルダー")
    f.text(14, 22, "スタジオ(チャネルや作業ごと)", "gta")
    for i, (t, s) in enumerate([("Email Studio", "メール"), ("Mobile Studio", "SMS・プッシュ・LINE"), ("Advertising", "広告"), ("Automation Studio", "処理の自動化")]):
        f.box(14 + i * 154, 32, 146, 66, "gba", t, [s], fs=13)
    f.text(14, 134, "ビルダー(全体で共通に使う)", "gta")
    for i, (t, s) in enumerate([("Contact Builder", "連絡先データ"), ("Content Builder", "コンテンツ"), ("Journey Builder", "顧客の道筋"), ("Analytics Builder", "分析とレポート")]):
        f.box(14 + i * 154, 144, 146, 66, "gby", t, [s], fs=13)
    return f.svg("チャネルや作業ごとの「スタジオ」と、データ・コンテンツ・分析を共通で扱う「ビルダー」を組み合わせて使います。足りない機能は拡張製品で足します。")

@fig("compliance")
def _():
    f = Fig("fcompliance", 236, "送信分類のCAN-SPAM区分")
    f.box(14, 76, 170, 76, "gby", "送信分類", ["CAN-SPAM区分を選ぶ"])
    f.box(250, 18, 376, 88, "gba", "Commercial(商用)", ["広告・宣伝が目的のメール", "送信時に配信停止リンクの有無をチェック"])
    f.box(250, 122, 376, 88, "gbo", "Transactional(トランザクション)", ["注文確認など、同意した取引のメール", "配信停止した人にも届く(オプションで除外できる)"])
    f.arrow(186, 104, 246, 66, "a"); f.arrow(186, 126, 246, 164, "o")
    f.text(320, 228, "配信停止は10日以内に処理し、仕組みは送信後30日以上動かす(CAN-SPAM)", anchor="middle")
    return f.svg("商用メールは配信停止の仕組みが必須です。トランザクションメールは、配信停止した人にも届けられます。")

@fig("security-bp")
def _():
    f = Fig("fsecbp", 200, "データを守る4つの場所")
    items = [("権限", ["必要最小限のロール", "Deny が許可より優先"]), ("ログイン", ["MFA・IP許可リスト", "セッション20分"]),
             ("データの出口", ["持ち出し先の許可リスト", "Audit Trail で記録"]), ("保存するデータ", ["項目単位の暗号化", "データ保持ポリシー"])]
    for i, (t, s) in enumerate(items):
        f.box(14 + i * 154, 40, 146, 110, ["gba", "gby", "gbo", "gbr"][i], t, s, fs=13.5)
    f.text(320, 26, "人 → 入口 → 出口 → 保管、の順に守る", "gta", "middle")
    for i in range(3): f.arrow(160 + i * 154, 95, 166 + i * 154, 95, "n")
    f.text(320, 182, "そもそも保存しない機密データは Tokenized Sending で送信時だけ渡す", anchor="middle")
    return f.svg("権限を絞り、ログインを守り、データの出口を管理し、保存するデータは暗号化して期限を決めて持ちます。")

@fig("account")
def _():
    f = Fig("faccount", 252, "Enterprise 2.0 のアカウント構造")
    f.frame(6, 8, 628, 200); f.text(18, 28, "テナント(Enterprise 2.0 では最上位+全ビジネスユニット)", "gta")
    f.box(210, 40, 220, 64, "gba", "最上位アカウント", ["EID / MID・購読者はここに保存"])
    for i, t in enumerate(["ブランドA", "ブランドB", "地域・店舗"]):
        x = 18 + i * 206
        f.box(x, 136, 192, 60, "gby", f"子ビジネスユニット", [f"{t}(MID)"])
        f.arrow(320, 106, x + 96, 132, "n")
    f.text(320, 232, "子が見られる購読者は、購読者フィルターで決まる。共有したいものは共有フォルダーへ", anchor="middle")
    return f.svg("Enterprise 2.0 では、購読者は最上位アカウントに保存され、ビジネスユニットごとに見られる範囲を分けます。")

@fig("users")
def _():
    f = Fig("fusers", 236, "ロールで権限を決める")
    f.box(14, 88, 120, 60, "gb", "ユーザー")
    f.box(186, 14, 220, 60, "gba", "Marketing Cloud ロール", ["標準ロールから1つ"])
    f.box(186, 88, 220, 60, "gba", "Email Studio ロール", ["標準ロールから1つ"])
    f.box(186, 162, 220, 60, "gby", "カスタムロール・個別権限", ["足りないときに追加"])
    for y in (44, 118, 192): f.arrow(136, 118, 182, y, "n")
    f.box(462, 64, 164, 108, "gbr", "権限の判定", ["Deny があれば使えない", "未設定は拒否扱い", "許可だけなら使える"])
    for y in (44, 118, 192): f.arrow(408, y, 458, 118, "n")
    return f.svg("ロールを組み合わせて権限を決めます。どこかに拒否(Deny)があれば、ほかで許可されていても使えません。")

@fig("security")
def _():
    f = Fig("fsecurity", 230, "ログインまでの守り")
    steps = [("IP 許可リスト", "許可したIPのみ"), ("パスワード", "3回失敗でロック"), ("MFA", "もう1つの確認"), ("ログイン後", "20分無操作で退出")]
    for i, (t, s) in enumerate(steps):
        f.box(14 + i * 154, 30, 140, 66, ["gby", "gby", "gba", "gbo"][i], t, [s], fs=13.5)
        if i < 3: f.arrow(156 + i * 154, 63, 166 + i * 154, 63, "n")
    f.box(120, 146, 400, 66, "gb", "Audit Trail(誰が何をしたかの記録)", ["Basic は既定でオン・30日 / Advanced は60日"])
    for i in range(4): f.arrow(84 + i * 154, 100, 260 + i * 40, 142, "n", dash=True)
    return f.svg("ログインまでを何段階かで守り、操作は Audit Trail に記録します。SSO を使うときは、IdP 側で MFA をかけます。")

@fig("sending")
def _():
    f = Fig("fsending", 250, "送信設定の積み重ね")
    f.box(170, 12, 300, 62, "gba", "送信分類(Send Classification)", ["2つのプロファイル + CAN-SPAM区分"])
    f.box(40, 100, 270, 62, "gby", "送信者プロファイル", ["From名・Fromアドレス"])
    f.box(330, 100, 270, 62, "gby", "配信プロファイル", ["送信IP・ヘッダーとフッター"])
    f.box(40, 186, 560, 52, "gbo", "検証済みドメイン(SAP・プライベートドメイン・登録ドメイン)")
    f.arrow(175, 98, 260, 78, "a"); f.arrow(465, 98, 380, 78, "a")
    f.arrow(175, 184, 175, 166, "n"); f.arrow(465, 184, 465, 166, "n")
    return f.svg("土台に検証済みドメインがあり、その上に2つのプロファイル、さらにそれをまとめた送信分類を重ねます。")

@fig("connect")
def _():
    f = Fig("fconnect", 246, "Marketing Cloud Connect のデータの流れ")
    f.box(14, 40, 190, 150, "gba", "Sales / Service Cloud", ["管理パッケージを導入", "Salesforce", "システムユーザー"])
    f.box(436, 40, 190, 150, "gby", "Marketing Cloud", ["Engagement", "Marketing Cloud", "API ユーザー"])
    f.arrow(206, 70, 432, 70, "a"); f.text(320, 62, "同期データソース(Contact Builder)", anchor="middle")
    f.arrow(432, 118, 206, 118, "o"); f.text(320, 110, "メールの反応(トラッキング)", anchor="middle")
    f.arrow(206, 164, 432, 164, "n"); f.text(320, 156, "CRMの画面からメール送信", anchor="middle")
    f.text(320, 226, "同期データエクステンションは、そのままでは送信に使えない(クエリで移す)", anchor="middle")
    return f.svg("CRM のデータを Engagement に同期して使い、メールの反応を CRM に戻します。両側にそれぞれ専用のユーザーを用意します。")

@fig("setup-home")
def _():
    f = Fig("fsetuphome", 246, "Setup に集まる管理項目")
    f.box(250, 92, 140, 60, "gbr", "Setup", ["アカウント管理"])
    pos = [(14, 18, "Account Settings", "住所・ヘッダー/フッター"), (232, 18, "Business Units", "階層・ロール"), (450, 18, "Security", "ログインとパスワード"),
           (14, 168, "Installed Packages", "API 連携"), (232, 168, "Key Management", "暗号化と署名のキー"), (450, 168, "Mobile・ENS", "チャネル設定・通知")]
    for x, y, t, s in pos:
        f.box(x, y, 176, 60, "gba" if y < 100 else "gby", t, [s], fs=13)
        f.arrow(320, 92 if y < 100 else 152, x + 88, y + 62 if y < 100 else y - 4, "n")
    f.text(320, 240, "購読者のプロファイル属性・プリファレンス属性は、Setup ではなく Email Studio で作る", anchor="middle")
    return f.svg("Setup にはアカウント全体の設定が集まっています。購読者の属性だけは Email Studio で作る点に注意します。")

@fig("subscribers")
def _():
    f = Fig("fsubs", 256, "購読者のステータスの変わり方")
    f.box(240, 16, 160, 56, "gbo", "Active", ["送信できる"])
    f.box(14, 160, 180, 60, "gby", "Bounced", ["1回以上バウンス"])
    f.box(232, 160, 176, 60, "gbr", "Held", ["3回以上かつ15日超"])
    f.box(446, 160, 180, 60, "gb", "Unsubscribed", ["配信停止・スパム報告"])
    f.arrow(250, 74, 104, 156, "n"); f.text(120, 106, "バウンス", anchor="middle")
    f.arrow(196, 190, 228, 190, "n")
    f.arrow(390, 74, 536, 156, "r"); f.text(530, 106, "配信停止", anchor="middle")
    f.arrow(320, 156, 320, 76, "o", dash=True)
    f.text(320, 246, "点線: Bounced や Held の人が開封・クリックすると Active に戻る", anchor="middle")
    return f.svg("購読者はサブスクライバーキーで見分け、ステータスで送信の可否が決まります。All Subscribers で配信停止になると、すべてのリストで停止です。")

@fig("data-ext")
def _():
    f = Fig("fdataext", 236, "リストとデータエクステンション")
    f.box(14, 20, 290, 90, "gb", "リスト", ["50万人以下・属性は少なめ", "プロファイルセンターに対応"])
    f.box(336, 20, 290, 90, "gba", "データエクステンション", ["大規模・API・トリガー送信向け", "項目を自由に設計・保持ポリシーあり"])
    f.box(336, 150, 290, 66, "gby", "送信可能(Is Sendable)", ["Send Relationship でキーとつなぐ"])
    f.box(14, 150, 290, 66, "gbo", "All Subscribers", ["サブスクライバーキーで1人ずつ"])
    f.arrow(480, 112, 480, 146, "a"); f.arrow(334, 183, 308, 183, "o")
    f.arrow(160, 112, 160, 146, "n"); f.text(170, 134, "インポート時に追加")
    return f.svg("送信に使うデータエクステンションは「送信可能」にし、どの項目がサブスクライバーキーに当たるかを指定します。")

@fig("contacts")
def _():
    f = Fig("fcontacts", 240, "連絡先を中心にしたデータモデル")
    f.box(232, 86, 176, 70, "gbr", "連絡先", ["連絡先キーで1人を識別"])
    for i, (t, s) in enumerate([("Email Studio", "サブスクライバー"), ("MobileConnect", "SMS の購読"), ("MobilePush", "アプリの購読")]):
        y = 14 + i * 76
        f.box(14, y, 170, 60, "gba", t, [s], fs=13)
        f.arrow(186, y + 30, 228, 121, "n")
    f.box(456, 30, 170, 70, "gby", "属性グループ", ["データエクステンション"])
    f.box(456, 140, 170, 70, "gby", "注文データ", ["1人に複数行(1対多)"])
    f.arrow(410, 110, 452, 70, "a"); f.arrow(410, 132, 452, 172, "a")
    f.text(320, 232, "Data Designer で、連絡先キーを使って関係を定義する", anchor="middle")
    return f.svg("連絡先はチャネルをまたいだ1人です。データエクステンションは Data Designer で連絡先キーに結びつけます。")

@fig("profile-center")
def _():
    f = Fig("fprofile", 230, "2つのセンターの違い")
    f.box(14, 80, 150, 70, "gb", "メールのリンク")
    f.box(230, 14, 250, 84, "gba", "プロファイルセンター", ["「Update Profile」", "氏名などの属性を更新"])
    f.box(230, 132, 250, 84, "gby", "サブスクリプションセンター", ["「Manage Subscriptions」", "Public のリストを選ぶ"])
    f.arrow(166, 105, 226, 56, "a"); f.arrow(166, 125, 226, 174, "n")
    f.box(516, 80, 110, 70, "gbr", "全配信停止", ["どちらからも"])
    f.arrow(482, 56, 540, 76, "r"); f.arrow(482, 174, 540, 154, "r")
    return f.svg("個人情報の更新はプロファイルセンター、受け取るリストの選択はサブスクリプションセンターです。標準のセンターはリストに対応します。")

@fig("data-quality")
def _():
    f = Fig("fdq", 246, "リプライメール管理の仕分け")
    f.box(14, 88, 150, 70, "gb", "受信者の返信")
    f.box(196, 88, 150, 70, "gby", "reply.example.com", ["Reply Subdomain"])
    f.arrow(166, 123, 192, 123, "n")
    rules = [("不在通知・自動返信", "削除 または 転送", "gb"), ("配信停止の語句", "送信元を配信停止", "gbr"), ("それ以外", "転送先へ+自動応答", "gbo")]
    for i, (t, s, c) in enumerate(rules):
        y = 14 + i * 76
        f.box(400, y, 226, 64, c, t, [s])
        f.arrow(348, 123, 396, y + 32, "n")
    f.text(320, 240, "配信停止の語句は、件名か本文の最初の200文字にあれば処理される", anchor="middle")
    return f.svg("RMM は、返信用のサブドメインに届いた返信を、ルールに従って自動で仕分けます。")

@fig("email")
def _():
    f = Fig("femail", 214, "メールを送るまでの設定")
    steps = [("Fromアドレス", ["検証済みドメイン"]), ("送信分類", ["プロファイル+区分"]), ("テスト送信", ["送信数に数える"]), ("スロットリング", ["時間帯と1時間の上限"])]
    for i, (t, s) in enumerate(steps):
        f.box(14 + i * 154, 30, 140, 72, ["gby", "gba", "gb", "gbo"][i], t, s, fs=13.5)
        if i < 3: f.arrow(156 + i * 154, 66, 166 + i * 154, 66, "n")
    f.box(120, 136, 400, 60, "gb", "Send Logging", ["送信時の値をデータエクステンションに記録"])
    f.arrow(320, 106, 320, 132, "n", dash=True)
    return f.svg("検証済みの差出人で、送信分類のルールに沿って送ります。負荷を分けたいときはスロットリング、送信時の値を残したいときは Send Logging です。")

@fig("mobile")
def _():
    f = Fig("fmobile", 246, "MobileConnect と MobilePush")
    f.text(14, 22, "MobileConnect(SMS)", "gta")
    f.box(14, 32, 130, 64, "gb", "購読者", ["JOIN と送る"])
    f.box(176, 32, 200, 64, "gby", "コード", ["ショート / ロング"])
    f.box(408, 32, 218, 64, "gba", "オプトイン", ["シングル / ダブル"])
    f.arrow(146, 64, 172, 64, "n"); f.arrow(378, 64, 404, 64, "a")
    f.text(14, 136, "MobilePush(アプリ)", "gta")
    f.box(14, 146, 200, 64, "gby", "アプリ", ["SDK の組み込みが必須"])
    f.box(246, 146, 200, 64, "gba", "Setup でアプリ作成", ["APNs / Firebase の資格情報"])
    f.box(478, 146, 148, 64, "gbr", "送信ブラックアウト", ["送らない時間帯"])
    f.arrow(216, 178, 242, 178, "n")
    return f.svg("SMS はキーワードとコードで購読を受け付け、プッシュ通知はアプリへの SDK 組み込みが前提です。深夜などはブラックアウトで送信を止めます。")

@fig("advertising")
def _():
    f = Fig("fads", 236, "Advertising Audiences と Lead Capture")
    f.box(14, 20, 160, 70, "gby", "データエクステンション", ["または連絡先"])
    f.box(206, 20, 150, 70, "gb", "SHA-256 で", ["ハッシュ化"])
    f.box(388, 20, 238, 70, "gba", "広告ネットワーク(7つ)", ["Facebook・Google Ads など"])
    f.arrow(176, 55, 202, 55, "n"); f.arrow(358, 55, 384, 55, "a")
    f.box(388, 140, 238, 70, "gba", "リード広告フォーム", ["Facebook・Google"])
    f.box(14, 140, 342, 70, "gbo", "データエクステンション / Sales Cloud のリード", ["Lead Capture で自動同期"])
    f.arrow(386, 175, 360, 175, "o")
    return f.svg("顧客データはハッシュ化してから広告ネットワークに送ります。逆に、リード広告で集めた見込み客は Lead Capture で取り込みます。")

@fig("journey")
def _():
    f = Fig("fjourney", 246, "ジャーニーの組み立て")
    f.box(14, 30, 150, 80, "gby", "エントリーソース", ["DE・API など"])
    f.box(196, 30, 250, 80, "gba", "アクティビティ", ["メッセージ・分岐・待機", "レコードの更新"])
    f.box(478, 14, 148, 52, "gbo", "ゴール", ["成果を測る"])
    f.box(478, 76, 148, 52, "gbr", "終了条件", ["外すだけ"])
    f.arrow(166, 70, 192, 70, "n"); f.arrow(448, 60, 474, 40, "o"); f.arrow(448, 80, 474, 102, "r")
    f.box(14, 156, 250, 64, "gb", "Automation Studio", ["データを準備して1つにまとめる"])
    f.arrow(140, 154, 100, 114, "n", dash=True)
    f.text(300, 182, "再エントリー: なし / いつでも / 出たあとだけ")
    f.text(300, 204, "同じ人かどうかは連絡先キーで判断")
    return f.svg("エントリーソースから入った連絡先が、アクティビティを順に進みます。ゴールは成果を測り、終了条件は対象外の人を外します。")

@fig("automation")
def _():
    f = Fig("fauto", 240, "オートメーションの開始と実行")
    for i, (t, s) in enumerate([("スケジュール", "日時と間隔"), ("ファイルドロップ", "Enhanced FTP に到着"), ("トリガー", "S3 などに到着")]):
        f.box(14, 14 + i * 72, 170, 60, "gby", t, [s], fs=13)
        f.arrow(186, 44 + i * 72, 224, 116, "n")
    f.box(228, 60, 220, 112, "gba", "オートメーション", ["ステップ1: インポート", "ステップ2: SQL Query", "ステップ3: メール送信"])
    f.box(480, 76, 146, 80, "gbr", "通知", ["スキップ・エラー", "・完了"])
    f.arrow(450, 116, 476, 116, "r")
    f.text(338, 200, "同じステップは同時に、別のステップは順番に実行", anchor="middle")
    f.text(338, 222, "所要時間がスケジュールの間隔より長いと完了しない", anchor="middle")
    return f.svg("3種類のきっかけで始まり、ステップの順にアクティビティを実行します。通知は「Notification Settings」で受け取ります。")

@fig("reports")
def _():
    f = Fig("freports", 236, "データの抽出からFTPまで")
    steps = [("Data Extract", ["ステップ1", "ファイルを作る"], "gby"), ("Safehouse", ["一時置き場"], "gb"), ("File Transfer", ["ステップ2", "Move a File"], "gba"), ("FTP の場所", ["外部システムへ"], "gbo")]
    for i, (t, s, c) in enumerate(steps):
        f.box(14 + i * 154, 24, 140, 84, c, t, s, fs=13.5)
        if i < 3: f.arrow(156 + i * 154, 66, 166 + i * 154, 66, "n")
    f.box(14, 148, 296, 66, "gba", "画面で見る", ["標準レポート・Intelligence Reports"])
    f.box(330, 148, 296, 66, "gby", "SQL で見る", ["データビュー(最大6か月分)"])
    return f.svg("Data Extract はファイルを作るだけです。外に出すには、別のステップの File Transfer で FTP に移します。")

@fig("maintenance")
def _():
    f = Fig("fmaint", 246, "アカウントを健全に保つ作業")
    f.box(240, 92, 160, 62, "gbo", "健全なアカウント")
    items = [(14, 16, "データ保持ポリシー", "古いデータを自動で削除"), (446, 16, "ストレージの整理", "Download Storage Details"),
             (14, 168, "コンタクトの削除", "抑制期間は既定2日"), (446, 168, "稼働状況と記録", "Trust・Audit Trail")]
    for x, y, t, s in items:
        f.box(x, y, 180, 62, "gby" if x < 300 else "gba", t, [s], fs=13)
        f.arrow(x + 90 + (60 if x < 300 else -60), y + (64 if y < 100 else -2), 320 + (-60 if x < 300 else 60), 92 if y < 100 else 156, "n")
    return f.svg("データの持ちすぎを防ぎ、削除の依頼に応え、稼働状況と操作の記録を定期的に確認します。")

def insert_all(sections):
    """各項目の「たとえるなら」の直後に図を入れる(すでに図があれば差し替える)。"""
    warns = []
    for s in sections:
        fn = FIGS.get(s["id"])
        if not fn: continue
        h = re.sub(r'<figure class="fig wide">.*?</figure>', "", s["html"], flags=re.S)
        m = re.search(r'<div class="co tips">.*?</div>', h, re.S)
        figure = fn()
        h = h[:m.end()] + figure + h[m.end():]
        s["html"] = h
    for fn in FIGS.values():
        pass
    return warns
