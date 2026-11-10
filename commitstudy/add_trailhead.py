"""Trailhead のモジュールのクイズ(<科目>/trailhead/out.json)を、その科目の問題集(<科目>/data)に足す。
  - 出典 s は「Trailhead: モジュール / ユニット Qn」。アプリの出典の絞り込みでは「Trailhead のクイズ」になる(patch_trailhead_src.py)
  - 問題の番号(id)は出典 s ごとに <科目>/trailhead/ids.json で固定する。原稿・過去問の番号と重ならないよう 5001 から振る
  - 何度実行しても同じ結果になるよう、先に data から「Trailhead:」の問題を取り除いてから足し直す
  - 項目 f がない・正解の位置が不正なら止める。該当箇所 x が本文にないときは警告して x を外す
使い方: python3 add_trailhead.py <科目id>   (例: python3 add_trailhead.py mcadmin)
"""
import html, json, os, re, sys
subj = sys.argv[1]
here = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(here, subj, "data"); T = os.path.join(here, subj, "trailhead")
L = lambda n: json.load(open(os.path.join(D, n), encoding="utf-8"))
CH, Q, R = L("chapters.json"), L("questions.json"), L("qrows.json")
items = json.load(open(os.path.join(T, "out.json"), encoding="utf-8"))
warn = []
def plain(x): return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", x))).strip()
secch, units = {}, {}
for c in CH:
    for m in re.finditer(r'<article class="feat" data-sec="([^"]+)".*?</article>', c["data"]["html"], re.S):
        secch[m.group(1)] = c["data"]["n"]
        a = re.sub(r"<svg.*?</svg>", "", m.group(0), flags=re.S)
        units[m.group(1)] = {plain(x[1]) for x in re.findall(r"<(li|p)(?:\s[^>]*)?>(.*?)</\1>", a, re.S)} | {plain(x) for x in re.findall(r"<tr[^>]*>(.*?)</tr>", a, re.S)}
# 前回足した分を取り除く
Q = [q for q in Q if not str(q["data"].get("s", "")).startswith("Trailhead:")]
R = [r for r in R if r.get("source") != "th"]
idp = os.path.join(T, "ids.json")
IDS = json.load(open(idp, encoding="utf-8")) if os.path.exists(idp) else {}
nid = max([5000] + list(IDS.values()))
seen = set(); added = 0
for it in items:
    s = it["s"]
    if not s.startswith("Trailhead:"): sys.exit("出典が Trailhead: で始まらない: " + s)
    if s in seen: warn.append("出典の重複: " + s); continue
    seen.add(s)
    f = re.sub(r"^f-", "", it["f"]).split(":")[-1]
    if f not in secch: sys.exit(f"項目がない: {s} {f}")
    if not (len(it["o"]) >= 2 and it["a"] and all(0 <= a < len(it["o"]) for a in it["a"])): sys.exit("正解の位置が不正: " + s)
    x = it.get("x") or ""
    if x and x not in units.get(f, set()): warn.append(f"該当箇所が本文にない(外す): {s} {x[:30]}"); x = ""
    if s not in IDS: nid += 1; IDS[s] = nid
    qid = IDS[s]; added += 1
    d = {"a": sorted(it["a"]), "c": secch[f] - 1, "ex": it["ex"], "f": "f-" + f, "id": qid, "n": None, "o": it["o"],
         "q": it["q"], "s": s, "u": it.get("u"), "v": it.get("v") or "Trailhead のユニット本文で確認", "x": x}
    if it.get("qe"): d["qe"] = it["qe"]
    if it.get("oe"): d["oe"] = it["oe"]
    Q.append({"id": f"q{qid:04d}", "data": d})
    R.append({"id": f"{subj}:q{qid}", "subject_id": subj, "n": qid, "kind": "mc", "source": "th", "exam": s, "text": it["q"],
              "section_id": f"{subj}:{f}", "kq": [], "law": None})
json.dump(dict(sorted(IDS.items(), key=lambda kv: kv[1])), open(idp, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
for n, obj in (("questions.json", Q), ("qrows.json", R)):
    json.dump(obj, open(os.path.join(D, n), "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
for w in warn: print("警告:", w)
print(f"{subj}: Trailhead のクイズ {added} 問 / 警告 {len(warn)}")
