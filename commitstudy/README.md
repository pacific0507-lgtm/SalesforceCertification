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

## 修正パッチ(2026-11-01) `patch_fix_20261101.py`

- 絞り込み中(例: 出典=過去問)は、絞り込んだ問題だけで1から番号を振り直し、一覧にも絞り込み中の問題だけを出す
- テーマを `sr-theme` にも保存し、起動部分からの復元(`window.__srThemeSync`)を受け取る(iPhone で開き直すと「自動」に戻る不具合)
- 960幅の横長の図3枚(全体の流れ・カテゴリ・ID解決)がスマホで小さくならないよう、`figure` の余白をなくして横スクロールにする

```bash
python3 commitstudy/patch_fix_20261101.py index.html chapters.json index.new.html chapters.new.json
```

## 旧「Data360 AI先生テキスト問題集」からの記録の引き継ぎ(2026-11-01 実施)

旧アーティファクト(JAJpRpzNWPU4rRBRuyqbDL)の `data/users/<自分>/quiz`・`study` を、CommitStudy の `d360-quiz`・`d360-study` へ合算した。
問題288問は番号・問題文・選択肢・正解がすべて一致していたので、番号はそのまま。
回答の集計(hist)・回答履歴(log)・しおり(bm)・読了済みの項目(done)を合算し、CommitStudy 側の絞り込み・位置などの設定はそのまま残した。

## 保存状態の帯 `patch_syncbar.py`(社労士版と同じ)

アカウントに記録が保存されていないときだけ、メニューバーの一番上に帯を出す。
- 赤「アカウントに保存されていません(この端末のみ)」+ 再読み込み … クラウドにつながっていない
- 赤「クラウドへの保存に失敗しています」+ 再試行 … 学習の記録・問題集の記録の保存に失敗
- 黄「クラウドに接続しています…」… 3秒経っても未接続(15秒で赤に切り替え)

`syncbar.js` / `syncbar.css` は社労士版から写した部分。

## 過去問の追加 `add_questions.py`

Notion の過去問原本(英語)から、問題集に入っていない問題を追加する。英語の問題文・選択肢は原本から取り、日本語訳・解説・テキストの項目・出題範囲は追加分の JSON に書く。

- 2026-11-01: v2025-03-20 から15問を追加(`d360/add_v20250320.json`、問題ID 289〜303)。
  公式ドキュメントで確認できた3問(Q8・Q43・Q54)は「公式で確認済み」、新しい版と正解が食い違う Q41 は「要確認(矛盾あり)」、ほかは「原本どおり」。

```bash
python3 commitstudy/add_questions.py notion.txt commitstudy/d360/add_v20250320.json v2025-03-20 questions.json qrows.json
```

## 問題とテキストを「該当箇所」で結ぶ `patch_qx.py`

- 問題データに `x`(本文中の該当する段落・表の行の文字列)、別の項目なら `xs` を持たせる。対応表は `d360/anchors.json`(115問・64箇所)。
- 問題の「テキストの該当箇所で復習する」→ その箇所までスクロールして黄色で光らせる。本文を直して文字列が見つからなくなったときは項目の先頭へ。
- 本文の該当箇所の末尾に「問題 N」の印。押すとその箇所の問題を一覧し、押した問題へ飛ぶ(全問正解済みの箇所は緑)。
- 本文に論点がない188問は `d360/uncovered.md`(本文へ追記するときの候補)。
