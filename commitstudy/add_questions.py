"""Notion の過去問原本から、CommitStudy の data/d360/questions.json と qrows.json に問題を追加する。
使い方: python3 add_questions.py <notion本文.txt> <追加分.json> <版の名前> <questions.json> <qrows.json>
追加分.json: [{no, f, c, a, q, o, ex, (v, u, n)}]  英語の問題文と選択肢は Notion 本文から取る
"""
import json, re, sys
notion, addp, ver, qp, rp = sys.argv[1:6]
t = open(notion, encoding="utf-8").read()
heads = re.findall(r"#### <b>Question (\d+)/\d+</b>", t)
blocks = re.split(r"#### <b>Question \d+/\d+</b>", t)[1:]
B = dict(zip(map(int, heads), blocks))
Q = json.load(open(qp, encoding="utf-8")); R = json.load(open(rp, encoding="utf-8"))
have = {r["data"].get("s") for r in Q}
nid = max(r["data"]["id"] for r in Q)
LET = "ABCDE"
for it in json.load(open(addp, encoding="utf-8")):
    s = f"{ver} Q{it['no']}"
    if s in have: print("skip(既にあり)", s); continue
    b = re.sub(r"<[^>]+>", "", B[it["no"]]); body = b[:b.find("Correct Answer")]
    ans = re.search(r"Correct Answer:\s*([A-E][A-E, ]*)", b).group(1)
    corr = sorted(LET.index(x) for x in re.findall(r"[A-E]", ans))
    assert corr == sorted(it["a"]), (it["no"], corr, it["a"])
    m = re.search(r"\n\s*(?:- \[ \] )?A\.", body)
    qe = re.sub(r"\s+", " ", body[:m.start()]).strip()
    qe = re.sub(r"([.?])(?=[A-Z])", r"\1 ", qe)
    oe = [re.sub(r"\s+", " ", x).strip() for x in re.findall(r"(?:^|\n)\s*(?:- \[ \] )?[A-E]\.\s*(.+)", body)]
    assert len(oe) == len(it["o"]), (it["no"], oe)
    nid += 1
    d = {"a": it["a"], "c": it["c"], "ex": it["ex"], "f": it["f"], "id": nid, "n": it.get("n"), "o": it["o"], "oe": oe,
         "q": it["q"], "qe": qe, "s": s, "u": it.get("u"), "v": it.get("v", "原本どおり")}
    Q.append({"id": f"q{nid:04d}", "data": d})
    R.append({"id": f"d360:q{nid}", "subject_id": "d360", "n": nid, "kind": "mc", "source": "past", "exam": s,
              "text": it["q"], "section_id": "d360:" + it["f"][2:], "kq": [], "law": None})
    print("add", nid, s, it["f"], corr)
json.dump(Q, open(qp, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
json.dump(R, open(rp, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
