# CommitStudy の作業メモ

- 機能を追加・変更したら、使い方ページ(`guide/patch_guide.py` の本文と `guide/spec_guide.py` の図)も合わせて直す。画面名・ボタン名・科目の一覧などが変わったら必ず見直す。
- 目立つ更新は `patch_news.py` の更新情報にも足す(新しい順に先頭へ)。
- index.html は `rebuild.sh` で、トレーニング追加前の版(v21)からパッチを順に当てて作り直せる。新しいパッチは rebuild.sh の末尾に足す。
- 図はスマホ(iPhone)前提。`figs_m/lib.py` で幅340、`figs_m/preview.py` ではみ出し・重なりを確かめる。
