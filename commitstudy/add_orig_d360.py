"""Data 360 のオリジナル問題(d360/orig/out.json)を問題集(d360/data)に足す。
  - 出典 s は「オリジナル(公式ヘルプにもとづく) <key>」。出典の絞り込みでは「オリジナル問題」になる(patch_d360_orig.py)
  - 番号(id)は key ごとに d360/orig/ids.json で固定し、3001 から振る
  - 何度実行しても同じ結果になるよう、先に「オリジナル」の問題を取り除いてから足し直す
  - 出題範囲(c)は、同じ項目 f の既存の問題で一番多い範囲に合わせる
使い方: python3 add_orig_d360.py
"""
import collections, json, os, sys
here = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(here, "d360", "data"); T = os.path.join(here, "d360", "orig")
L = lambda n: json.load(open(os.path.join(D, n), encoding="utf-8"))
Q, R = L("questions.json"), L("qrows.json")
items = json.load(open(os.path.join(T, "out.json"), encoding="utf-8"))
Q = [q for q in Q if not str(q["data"].get("s", "")).startswith("オリジナル")]
R = [r for r in R if r.get("source") != "orig"]
cnt = collections.defaultdict(collections.Counter)
for q in Q: cnt[q["data"]["f"]][q["data"]["c"]] += 1
secs = {s["id"].split(":")[-1] for s in L("sections.json")} if os.path.exists(os.path.join(D, "sections.json")) else set()
idp = os.path.join(T, "ids.json")
IDS = json.load(open(idp, encoding="utf-8")) if os.path.exists(idp) else {}
nid = max([3000] + list(IDS.values())); seen = set(); n = 0
for it in items:
    k = it["key"]
    if k in seen: sys.exit("key の重複: " + k)
    seen.add(k)
    f = "f-" + it["f"].removeprefix("f-")
    if f not in cnt and f[2:] not in secs: sys.exit(f"項目がない: {k} {f}")
    if not (len(it["o"]) >= 2 and it["a"] and all(0 <= a < len(it["o"]) for a in it["a"])): sys.exit("正解の位置が不正: " + k)
    c = it.get("c")
    if c is None: c = cnt[f].most_common(1)[0][0] if cnt[f] else 0
    if k not in IDS: nid += 1; IDS[k] = nid
    qid = IDS[k]; n += 1
    s = "オリジナル(公式ヘルプにもとづく) " + k
    d = {"a": sorted(it["a"]), "c": c, "ex": it["ex"], "f": f, "id": qid, "n": None, "o": it["o"], "q": it["q"], "s": s,
         "u": it.get("u"), "v": "公式ヘルプにもとづく", "x": it.get("x") or ""}
    Q.append({"id": f"q{qid:04d}", "data": d})
    R.append({"id": f"d360:q{qid}", "subject_id": "d360", "n": qid, "kind": "mc", "source": "orig", "exam": s, "text": it["q"],
              "section_id": "d360:" + f[2:], "kq": [], "law": None})
json.dump(dict(sorted(IDS.items(), key=lambda kv: kv[1])), open(idp, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
for nm, obj in (("questions.json", Q), ("qrows.json", R)):
    json.dump(obj, open(os.path.join(D, nm), "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print(f"d360: オリジナル問題 {n} 問")
