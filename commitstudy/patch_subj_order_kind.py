"""科目の並び(csOrd)を、資格の種類(Salesforce → 情報処理 → その他)ごとにまとめてから、ユーザーの並べ替え(cs-subj-order)の順にする。
  テキスト一覧はグループごとに分かれているので、トレーニング・ホーム・学習計画などほかの科目の並びもこれと同じ順になる。
  種類の分け方は patch_texts_groups.py / patch_practice_kind.py と同じ(載っていない科目は「その他」)。
使い方: python3 patch_subj_order_kind.py <index.html> <出力>
"""
import sys
src, out = sys.argv[1:3]
s = open(src, encoding="utf-8").read()
old = 'return function(a,b){var x=p[a.id!=null?a.id:a],y=p[b.id!=null?b.id:b];return (x==null?999:x)-(y==null?999:y)}};'
new = ('var K={d360:0,mcadmin:0,afsales:0,afsvc:0,afspec:0,mulepa:0,fe:1,sg:1},kd=function(id){return K[id]!=null?K[id]:2};'
       'return function(a,b){var ia=a.id!=null?a.id:a,ib=b.id!=null?b.id:b,k=kd(ia)-kd(ib);if(k)return k;var x=p[ia],y=p[ib];return (x==null?999:x)-(y==null?999:y)}};')
if s.count(old) != 1: sys.exit(f"{s.count(old)} 件")
s = s.replace(old, new)
open(out, "w", encoding="utf-8").write(s); print("ok")
