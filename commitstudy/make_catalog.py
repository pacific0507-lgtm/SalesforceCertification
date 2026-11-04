"""科目ごとの収録内容(問題の種類ごとの数・用語カードの枚数)を data/catalog.json にまとめる。
  テキスト一覧のカードのタグ(patch_texts_tags.py)が読む。問題や用語カードを足したら作り直して公開する。
使い方: python3 make_catalog.py <data フォルダ> <出力 catalog.json>
"""
import collections, json, os, sys
src, out = sys.argv[1:3]
cat = {}
for sj in sorted(os.listdir(src)):
    d = os.path.join(src, sj); qp = os.path.join(d, "qrows.json")
    if not os.path.exists(qp): continue
    rows = json.load(open(qp, encoding="utf-8"))
    n = collections.Counter(r.get("source") or "orig" for r in rows)
    tp = os.path.join(d, "terms.json")
    cat[sj] = {"n": dict(n), "terms": len(json.load(open(tp, encoding="utf-8"))) if os.path.exists(tp) else 0}
json.dump(cat, open(out, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print(json.dumps(cat, ensure_ascii=False))
