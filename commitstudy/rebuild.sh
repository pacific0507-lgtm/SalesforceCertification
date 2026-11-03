#!/bin/bash
# 基準(v21 = トレーニング追加前)から、これまでのパッチを順に当てて index.html を作り直す
# 使い方: bash rebuild.sh <基準 index.html> <作業フォルダ> <出力 index.html> <practice_extra.css> <d360 chapters(図修正前)> <mcadmin chapters>
set -e
C=$(cd "$(dirname "$0")" && pwd); B=$1; T=$2; OUT=$3; EX=$4; D=$5; M=$6
python3 $C/practice/patch_practice.py $B $T/p1.html $EX
python3 $C/patch_subj_time.py $T/p1.html $T/p2.html
python3 $C/patch_fig_fix.py $T/p2.html $T/p3.html $D $T/d1.json
python3 $C/figs_m/apply.py $T/d1.json $T/d2.json $M $T/m2.json $T/p3.html $T/p4.html
python3 $C/patch_quiz_pos.py $T/p4.html $T/p5.html
python3 $C/patch_sync_keys.py $T/p5.html $T/p6.html
python3 $C/patch_add_afsales.py $T/p6.html $OUT
python3 $C/patch_ask_form.py $OUT $OUT.tmp && mv $OUT.tmp $OUT
