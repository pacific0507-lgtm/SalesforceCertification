# CommitStudy(Data 360)の作業用ファイル

公開中のアーティファクト: https://claude.ai/artifact/2GNXheR3Ki6gFeHyGtBNUV

- `d360/talks.json` … 各項目の「キャラの掛け合い」の原稿。`pattern` にその項目の型、`lines` に `[話者, セリフ, 表情(省略可)]` を並べる。
  - 話者: `pote`=まなびん / `rou`=クラウドちゃん / `pen`=コミットくん
  - 表情: normal / smile / eager / sad / surprise / sweat / think / wink(省略時は文面から自動判定)
- `apply_talks.py` … 公開中の `data/d360/chapters.json` の掛け合い部分を `talks.json` で差し替える。

```bash
python3 commitstudy/apply_talks.py chapters.json commitstudy/d360/talks.json chapters.new.json
```

## 問題集を社労士版(LaughStudy 家族版)の仕様に合わせるパッチ

`patch_quiz_like_sharoushi.py` を公開中の `index.html` に当てる。

- 問題の並びをテキストの項目順にし、表示番号(問N)を1からの通し番号にする(記録は元の番号のまま。前回の位置も同じ問題に戻る)
- PC幅(980px以上)では問題集の左に問題一覧を常に表示(折りたたみ可)。本文は最大860pxで中央、前へ/答え/次へを中央にまとめる
- しおり・回答履歴・ノート・AI先生の保存回答などの「問N」も通し番号にそろえる
- 4択・検証状況・試験セクションなど Data 360 独自の部分はそのまま(選択式・5肢択一は入れない)

```bash
python3 commitstudy/patch_quiz_like_sharoushi.py index.html index.new.html
```
