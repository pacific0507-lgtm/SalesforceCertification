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

## 過去問の知識を本文に追記(2026-11-01)`add_pastq_text.py`

本文に論点がなかった過去問83問について、公式ドキュメントで調べ、各項目の「試験ポイント」の直前に「過去問で問われた関連知識」として73本の箇条書きを追記した(`d360/pastq_additions.json`)。これで過去問159問はすべて本文の該当箇所に結び付く。
- 公式で確認できた57問は「公式で確認済み」(参照URL付き)、公式と正解が食い違う12問は「要確認(矛盾あり)」、確認できなかった14問は本文を「〜とされます」と控えめに書いた。
- 調べた問題の入力は `d360/research/`。未対応(Trailhead のみ105問)は `d360/uncovered.md`。

## 科目 Marketing Cloud Administrator(mcadmin)

- `patch_multisubj.py`: エンジンの設定を科目ごとに切り替え、科目リスト(ホーム・科目一覧・学習記録・ルーター)に mcadmin を登録する。
- `build_mcadmin.py`: 章ごとの原稿 `mcadmin/manuscript/out_ch*.json` から `data/mcadmin/*.json` を組み立てる(選択肢は問題ごとに固定の乱数で並べ替え)。
- 構成: 5章21項目(デジタルマーケティングの基礎/セットアップ/サブスクライバーとデータの管理/チャネルの管理/メンテナンス)、オリジナル問題132問。すべて本文の該当箇所に結び付け済み。根拠は help.salesforce.com(各問題の参照ページ)。
- Trailhead のクイズはログインが必要で取得できなかったため、問題は Trailhead の資格対策モジュールの出題範囲と公式ヘルプをもとにしたオリジナル。
- 図: `mcadmin/figs.py` で21項目の図(SVG)を描き、各項目の「たとえるなら」の直後に入れる(Data 360 の図と同じクラスで、ライト/ダークに追従)。

## トレーニング(/practice/)
- `practice/patch_practice.py`: 社労士版と同じトレーニングのページを追加する。問題は各科目の4択をそのまま出す(出し方: 順番どおり・ランダム・今日の復習・間違えた問題・まだ解いていない)。カードは用語カード(数字カードはなし)
- 用語カードのデータ: `d360/data/terms.json`(120枚)、`mcadmin/data/terms.json`(178枚)。公開時は `data/<科目>/terms.json`
- 解いた結果は `ls-qpend-v1` に残り、科目の問題集を開いたときに回答履歴へ取り込む。学習の記録(act)にも数える

- `patch_subj_time.py`: 学習の記録「科目ごとの進み具合」に科目ごとの累計の勉強時間を常に表示。PCで行が崩れていた不具合(クラス名 x の衝突)も修正

- `patch_fig_fix.py`: スマホで図の説明の「問題 N」ボタンが横に伸びる不具合と、図の文字のはみ出し2か所を修正(d360 の chapters.json も更新)

## スマホ向けの図(figs_m/)
- `figs_m/lib.py` 作図の部品(幅340、横スクロールなし)、`spec_A〜D.py` 各図、`preview.py` 確認用PNG、`apply.py` で chapters.json と差し替え

- `patch_quiz_pos.py`: 問題集を開き直したとき、絞り込みを計算し直した並びの中で前回見ていた問題から再開する

- `patch_sync_keys.py`: お便りの既読・更新情報の既読・用語カードの覚えた・トレーニングの復習予定などもアカウント(fam-ls)に同期

- `rebuild.sh`: トレーニング追加前の版から、これまでのパッチを順に当てて作り直す

## 科目 Agentforce Sales コンサルタント(afsales)
- `afsales_SPEC.md` 原稿の仕様、`afsales/manuscript/` 章ごとの原稿、`build_afsales.py` で data を組み立て、`figs_m/spec_E〜G.py` と `figs_m/apply_afsales.py` で図を入れる、`patch_add_afsales.py` で科目を登録。公開データは `afsales/data/`

- AF Sales の過去問: Notion の4ページ(230問)から重複を除いた160問を、公式情報で検証・翻訳して `afsales/pastq/out_*.json` に。`merge_adds.py` で関連知識の重複をまとめ、`add_pastq_afsales.py` で問題集と本文に追加

- `patch_ask_form.py`: AI先生の質問欄の送信ボタンを入力欄の右に並べる

- `apply_jaui.py` + `afsales/jaui/glossary.json`: 英語のままの機能名を、公式の日本語UIの名称(日本語版 Trailhead などで確認)にそろえる。確かめられなかった名称(unconfirmed)は英語のまま
- Data 360 も同じ手順で `d360/jaui/glossary.json` を適用(公開データは `d360/data/`)

- `patch_news.py`: 更新情報(ホームの新着・更新情報ページ)に更新を追加

- `guide/patch_guide.py` + `guide/spec_guide.py`: 使い方ページ(/guide/、図入り・コメントのお願い)、ホームの紹介文を8パターンから切り替え、使い方を見ていない人への案内、メニューに「使い方」

- `patch_rotate_keep.py`: スマホを縦⇔横に回しても、画面上端の本文が同じ位置に来るようにする

- `patch_badge_toast.py`: バッジ獲得のお知らせを、アカウントの記録を読み終えてから、新しく獲得したものだけに

- `patch_home_wait.py`: ホームのお便り・更新情報の帯・使い方の案内の既読を、アカウントの記録を読み終えてから判定

- `patch_texts_order.py`: テキスト一覧の科目の並べ替えと合格の印(ユーザーごと、アカウントに同期)
