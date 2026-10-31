# CommitStudy(Data 360)の作業用ファイル

公開中のアーティファクト: https://claude.ai/artifact/2GNXheR3Ki6gFeHyGtBNUV

- `d360/talks.json` … 各項目の「キャラの掛け合い」の原稿。`pattern` にその項目の型、`lines` に `[話者, セリフ, 表情(省略可)]` を並べる。
  - 話者: `pote`=まなびん / `rou`=クラウドちゃん / `pen`=コミットくん
  - 表情: normal / smile / eager / sad / surprise / sweat / think / wink(省略時は文面から自動判定)
- `apply_talks.py` … 公開中の `data/d360/chapters.json` の掛け合い部分を `talks.json` で差し替える。

```bash
python3 commitstudy/apply_talks.py chapters.json commitstudy/d360/talks.json chapters.new.json
```
