"""テキスト(<科目>/data/chapters.json)の各章の更新時刻 ts を上げる。
  アプリは本文を端末に控え(chcache)として持ち、章の ts が変わったときだけ描き直す。
  本文(html など)を変えたのに ts を上げないと、一度開いたことのある端末には古い本文が出続ける。
  - 引数なし: 全科目。<科目> を並べるとその科目だけ
  - --changed <公開中の chapters.json>: その科目で、公開中と中身が違う章だけ上げる
使い方: python3 bump_chapters_ts.py [科目 ...]   /   python3 bump_chapters_ts.py d360 --changed 公開中/d360/chapters.json
"""
import json, os, sys, time
here = os.path.dirname(os.path.abspath(__file__))
args = sys.argv[1:]
old = None
if "--changed" in args:
    i = args.index("--changed"); old = json.load(open(args[i + 1], encoding="utf-8")); args = args[:i] + args[i + 2:]
subs = args or ["d360", "mcadmin", "afsales", "afsvc", "afspec", "mulepa", "fe", "sg"]
now = int(time.time())
for sj in subs:
    p = os.path.join(here, sj, "data", "chapters.json")
    C = json.load(open(p, encoding="utf-8")); n = 0
    O = {c["data"]["n"]: c["data"] for c in old} if old else {}
    for c in C:
        d = c["data"]
        if old is not None:
            o = dict(O.get(d["n"]) or {}); o.pop("ts", None); x = dict(d); x.pop("ts", None)
            if o == x: continue
        d["ts"] = max(now, int(d.get("ts") or 0) + 1); n += 1
    json.dump(C, open(p, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
    print(f"{sj}: {n} 章の ts を上げた")
