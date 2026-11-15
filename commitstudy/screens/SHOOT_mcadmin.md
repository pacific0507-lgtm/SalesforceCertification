# 撮影指示: Marketing Cloud Engagement Administrator(mcadmin)

共通のルールは `commitstudy/screens/SHOOT_PROMPT.md` の「準備」「撮り方」「終わったら」に従う(読んでから始める)。違うのは次の点だけ。
- 保存先: `commitstudy/screens/raw/mcadmin/`、manifest も `commitstudy/screens/raw/mcadmin/manifest.json`
- 環境: Marketing Cloud Engagement のアカウント(https://mc.exacttarget.com など)。**無料の開発用環境はないため、ユーザーが使えるアカウントがある場合だけ撮る**。なければ全部を missing にして、最初にユーザーに「Marketing Cloud のアカウントがない」と伝えて終える
- 表示言語: 日本語(ユーザー設定 > 言語)。日本語にできなければ英語
- コミットメッセージ: 「Marketing Cloud の画面を撮る」
- 送信・ジャーニーの有効化・オートメーションの実行・ユーザーの作成など、変更する操作はしない。作成画面は開いて見るだけ
- 実際の顧客データ(サブスクライバーのメールアドレスなど)が写る画面は撮らない。写ってしまったら撮り直す

## 撮る画面(項目id: 内容)
1. `account`: Setup > Business Units(ビジネスユニットの階層)
2. `users`: Setup > Users(ユーザーの一覧と、ロール・権限の設定画面)
3. `security`: Setup > Security Settings(セッションのタイムアウト・パスワード・ログイン IP の制限など)
4. `sending`: Setup > Sender Authentication Package / Send Classifications / Delivery Profiles / Sender Profiles の画面
5. `connect`: Setup > Salesforce Integration(Marketing Cloud Connect)の画面
6. `setup-home`: Setup のホームと Installed Packages(拡張機能)
7. `subscribers`: Email Studio > Subscribers > All Subscribers(一覧の列だけ。個人のアドレスは写さない)
8. `data-ext`: Contact Builder > Data Extensions の一覧と、新規データエクステンションの作成画面(送信可能・プライマリキーの設定)
9. `contacts`: Contact Builder > Data Designer(属性グループのつながり)
10. `profile-center`: Email Studio > Subscribers > Profile Management / Subscription Center の設定
11. `data-quality`: Email Studio > Admin > Reply Mail Management(RMM)の設定
12. `email`: Email Studio > Content Builder(コンテンツの一覧)、Email Studio の送信画面(Send Flow。送信はしない)
13. `journey`: Journey Builder のジャーニー一覧と、キャンバス(エントリーソース・アクティビティ)
14. `automation`: Automation Studio のオートメーション一覧と、キャンバス(スケジュール・アクティビティ)
15. `reports`: Analytics Builder > Reports、Data Extract のアクティビティ
16. `mobile`: Mobile Studio(MobileConnect / MobilePush)の画面(ライセンスがなければ missing)
17. `advertising`: Advertising Studio の画面(ライセンスがなければ missing)
