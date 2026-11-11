"""仕様書ページの図(figs_m/lib.py を使う。幅340)"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figs_m"))
from lib import Fig, fig

@fig("arch")
def _():
    f = Fig("sarch", 330, "全体の構成")
    f.frame(6, 6, 328, 196, "gbd")
    f.text(16, 26, "claude.ai のアーティファクト(公開先)", "gta")
    f.box(16, 38, 150, 70, "gba", "index.html", ["約1MBの1ファイル", "画面・処理・CSS"])
    f.box(176, 38, 148, 70, "gb", "data/<科目>/", ["テキスト・問題", "用語カード(JSON)"])
    f.box(16, 120, 150, 70, "gb", "brand/", ["キャラ・使い方の", "画面写真(webp)"])
    f.box(176, 120, 148, 70, "gb", "data/catalog.json", ["科目ごとの", "問題数・枚数"])
    f.box(16, 236, 150, 84, "gby", "ブラウザ", ["localStorage", "(端末の控え)"])
    f.box(176, 236, 148, 84, "gbo", "window.claude", ["db: 記録の保存", "user: 本人のID", "sample: AI先生"])
    f.arrow(91, 204, 91, 232, "a")
    f.arrow(166, 278, 172, 278, "n")
    return f.svg("ページはサーバーを持たず、アーティファクトに置いたファイルと、claude.ai が用意する window.claude の機能だけで動きます。")

@fig("boot")
def _():
    f = Fig("sboot", 360, "ページを開いてから表示するまで")
    f.box(20, 8, 300, 50, "gb", "① body に index.html が入る", ["head はホスト側。CSS はスクリプトで head へ"])
    f.box(20, 82, 300, 50, "gba", "② ルーター: パス → ページ名", ["/texts/ → texts、/d360/ → subject など"])
    f.box(20, 156, 300, 50, "gba", "③ FAMP.<ページ名>() を実行", ["画面の HTML を組み立てる"])
    f.box(20, 230, 300, 50, "gb", "④ 必要なデータを fetch", ["famURL() で公開先のURLに直す"])
    f.box(20, 304, 300, 50, "gbo", "⑤ 記録を読み込んで描く", ["端末の控え → アカウントの記録で更新"])
    for y in (60, 134, 208, 282): f.arrow(170, y, 170, y + 18, "n")
    return f.svg("科目を開くと body が作り直されるため、画面ごとの CSS は head に入れ直します。")

@fig("sync")
def _():
    f = Fig("ssync", 300, "記録の保存と同期")
    f.box(10, 10, 140, 70, "gby", "iPhone", ["localStorage", "+ 端末ID"])
    f.box(190, 10, 140, 70, "gby", "PC", ["localStorage", "+ 端末ID"])
    f.box(70, 120, 200, 64, "gba", "合わせる(CSQ)", ["読む → 合わせる → 保存"])
    f.box(40, 220, 260, 70, "gbo", "アカウント(window.claude db)", ["data/users/<ID>/…", "quiz・study・act・fam-ls"])
    f.arrow(80, 82, 130, 116, "n"); f.arrow(260, 82, 210, 116, "n")
    f.arrow(160, 186, 160, 216, "a"); f.arrow(184, 216, 184, 190, "a")
    return f.svg("保存の前に必ずアカウントの記録を読み直し、項目ごとの更新時刻で合わせてから書きます。")

@fig("quiz")
def _():
    f = Fig("squiz", 380, "問題集の処理の流れ")
    f.box(20, 8, 300, 48, "gb", "questions.json", ["科目の全問題(本文・選択肢・正解・解説)"])
    f.box(20, 78, 300, 48, "gba", "normQ: 画面用の形に直す", ["出典 s → src、項目 f → s など"])
    f.box(20, 148, 300, 62, "gba", "絞り込み(baseOk / buildDeck)", ["Chapter・項目・出題回・出典・状態", "検証状況・出題範囲・科目A/B"])
    f.box(20, 232, 300, 48, "gb", "deck: 解く順の番号の並び", ["項目順、またはランダム"])
    f.box(20, 302, 300, 64, "gbo", "答え合わせ → 記録", ["hist(集計)・log(履歴)", "<科目>-quiz と学習量(act)に保存"])
    for y in (58, 128, 212, 282): f.arrow(170, y, 170, y + 16, "n")
    return f.svg("絞り込み中の件数と、実際に解く並びは同じ判定を使います。")

@fig("train")
def _():
    f = Fig("strain", 250, "トレーニングの結果の受け渡し")
    f.box(10, 10, 140, 64, "gba", "トレーニング", ["/practice/", "1問ずつ解く"])
    f.box(190, 10, 140, 64, "gbo", "<科目>-quiz", ["アカウントの", "回答履歴"])
    f.box(10, 120, 140, 64, "gby", "ls-qpend-v1", ["書けなかった分の", "控え(端末)"])
    f.box(190, 120, 140, 64, "gb", "科目の問題集", ["開いたときに", "控えを取り込む"])
    f.arrow(152, 42, 186, 42, "a")
    f.arrow(80, 76, 80, 116, "n", dash=True)
    f.arrow(152, 152, 186, 152, "n", dash=True)
    f.text(170, 222, "取り込み済みの印で、二重には数えない", "gts", "middle")
    return f.svg("その場でアカウントに書き、書けなかったときだけ端末の控えから後で取り込みます。")

@fig("build")
def _():
    f = Fig("sbuild", 420, "作り方・確かめ方・公開")
    f.text(10, 20, "画面(index.html)", "gta")
    f.box(10, 30, 150, 56, "gb", "index.v21.html", ["トレーニング追加前"])
    f.box(180, 30, 150, 56, "gba", "rebuild.sh", ["パッチを順に当てる"])
    f.arrow(162, 58, 176, 58, "a")
    f.text(10, 124, "データ(data/<科目>/)", "gta")
    f.box(10, 134, 150, 56, "gb", "原稿・過去問", ["<科目>/manuscript など"])
    f.box(180, 134, 150, 56, "gba", "build・add 系の", ["スクリプトで JSON に"])
    f.arrow(162, 162, 176, 162, "a")
    f.box(10, 236, 320, 60, "gby", "確かめる", ["wrap.sh で公開先と同じく body に包む", "スモークテスト(Playwright・18項目)"])
    f.box(10, 336, 320, 60, "gbo", "公開", ["アーティファクトに index.html と data を出す"])
    f.arrow(255, 192, 255, 232, "n"); f.path([(331, 58), (337, 58), (337, 266), (333, 266)], "n"); 
    f.arrow(170, 298, 170, 332, "n")
    return f.svg("index.html は手で直さず、必ずパッチを足して作り直します。")
