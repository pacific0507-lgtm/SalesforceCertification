"""節の重要度(★★★ 頻出 / ★★ よく出る / ★ 出題少なめ)を、科目の過去問から計算して <科目>/data/imp.json に書く(社労士版から移植)。
  公開先は data/<科目>/imp.json。アプリはテキストを開いたときにこれを読み、節の見出しと目次に星を出す(patch_imp.py)。
  過去問(出典が「オリジナル」「Trailhead」で始まらない問題)だけを数える。問題の節は f(f-<節のid>)。

  数え方(科目ごと):
  - 回で数える科目(round): 1回の試験でたくさん出た節が強くなりすぎないよう、問題の数ではなく「出題された回の数」で比べる。
      eisei1 : 公表の回(令和N年M月公表)。同じ問題をまとめたもの(s2)は、ほかの回にも出たものとして数える。第二種の科目の問題も同じ回に数える
      fe     : 試験の回(修了認定試験の各回・各年度の公開問題・サンプル問題。公開問題とサンプル問題は科目A・Bで1回)
      sg     : 試験の回(各年度の公開問題・サンプル問題)
  - 問題の数で数える科目(count): d360・mcadmin・afsales・afspec・mulepa の過去問の出典(v2026-02-28 など)は、
      試験の年度ではなく問題集の版で、1問は1つの版にしか入っていない(afspec は版が1つだけ)。版の数を数えても意味がないので、問題の数で比べる。
  - afsvc は過去問がない(Trailhead とオリジナルだけ)ので、星を出さない(secs が空の imp.json を書く)。

  ★の決め方(相対): 科目の中で、過去問が1問以上ある節を(出題された回の数、同じなら問題の数)の多い順に並べ、
  上位30%を★★★、次の35%を★★、残りを★にする。並べたときに同じ数の節は同じ★にする(その節たちの順位のまんなかで決める)。
  1回(問題の数で数える科目は1問)だけの出題は、順位にかかわらず★。
  過去問のない節は★(「過去問での出題なし」)。問題が1問もない節(試験の概要など)は星を出さない。

  使い方: python3 make_imp.py                  … 全科目(<科目>/data/questions.json → <科目>/data/imp.json)
          python3 make_imp.py <科目> [<data>]   … 1科目(<data>/questions.json → <data>/imp.json。<data> の既定は <科目>/data)
          python3 make_imp.py --check          … 全科目の imp.json が questions.json と合っているかだけ確かめる(違えば知らせる。書き換えない)
  過去問を足した・まとめた・節を付け替えたら、作り直して data/<科目>/imp.json を公開する。
"""
import json, math, os, re, sys

BASE = os.path.dirname(os.path.abspath(__file__))
SUBJ = ["d360", "mcadmin", "afsales", "afspec", "afsvc", "mulepa", "fe", "sg", "eisei1"]
MODE = {"eisei1": "round", "fe": "round", "sg": "round"}
NOTPAST = re.compile(r"^(オリジナル|Trailhead)")
Z2H = str.maketrans("０１２３４５６７８９", "0123456789")

def era_n(e, n):
    return (2018 if e == "令和" else 1988) + (1 if n == "元" else int(n))

def round_of(sid, src):
    """出典の文字から、その回の (並べ替えの鍵, 表示名)。回がわからなければ None"""
    t = str(src).translate(Z2H)
    if sid == "eisei1":
        m = re.match(r"(令和|平成)(元|\d+)年(\d+)月公表", t)
        if not m: return None
        return ((era_n(m[1], m[2]), int(m[3])), f"{m[1]}{m[2]}年{m[3]}月")
    if "サンプル問題" in t:
        return ((0, 0), "サンプル問題")
    m = re.search(r"(令和|平成)(元|\d+)年度\s*(\d+)月実施分", t)
    if m:
        mo = int(m[3]); return ((era_n(m[1], m[2]), (mo - 4) % 12 + 1), f"{m[1]}{m[2]}年度 {mo}月(修了認定)")
    m = re.search(r"(令和|平成)(元|\d+)年度", t)
    if m:
        return ((era_n(m[1], m[2]), 13), f"{m[1]}{m[2]}年度 公開問題")
    return None

def ver_of(src):
    m = re.match(r"(v\d{4}(?:-\d\d-\d\d)?|Sales-Con-201)(?=\s|$)", str(src))
    return m[1] if m else str(src).split(" ")[0]

def compute(sid, Q, sections):
    mode = MODE.get(sid, "count")
    allsec = [str(x["id"]).split(":")[-1] for x in sorted(sections, key=lambda x: x.get("sort_order", 0))]
    withq, st = set(), {}
    units = {}
    npast = 0
    for it in Q:
        d = it["data"]; sec = str(d.get("f", "")).removeprefix("f-")
        if not sec: continue
        withq.add(sec)
        if NOTPAST.match(str(d.get("s", ""))): continue
        npast += 1
        o = st.setdefault(sec, {"n": 0, "u": {}})
        o["n"] += 1
        if mode == "round":
            for src in [d.get("s", "")] + list(d.get("s2") or []):
                r = round_of(sid, src)
                if not r: continue
                units[r[1]] = r[0]
                o["u"][r[1]] = o["u"].get(r[1], 0) + 1
        else:
            v = ver_of(d.get("s", "")); units[v] = v
            o["u"][v] = o["u"].get(v, 0) + 1
    out = {"v": 1, "sid": sid, "mode": mode, "past": npast, "units": [], "secs": {}}
    if not npast:
        out["none"] = "過去問がないため、節の重要度は出さない"
        return out
    order = sorted(units, key=lambda k: units[k])
    out["units"] = order
    def key(sec):
        o = st[sec]
        return (len(o["u"]), o["n"]) if mode == "round" else (o["n"],)
    ranked = sorted(st, key=lambda s: (tuple(-x for x in key(s)), allsec.index(s) if s in allsec else 999))
    N = len(ranked); n3 = round(N * 0.30); n2 = round(N * 0.65)
    gpos = {}
    for i, s in enumerate(ranked):
        gpos.setdefault(key(s), []).append(i)
    for i, s in enumerate(ranked):
        o = st[s]; ix = gpos[key(s)]; g = (ix[0] + ix[-1]) / 2
        lv = 3 if g < n3 - 0.5 else 2 if g < n2 - 0.5 else 1
        once = (len(o["u"]) if mode == "round" else o["n"]) <= 1
        if once: lv = 1
        u = sorted(o["u"], key=lambda k: units[k], reverse=True)
        out["secs"][s] = {"lv": lv, "rk": i + 1, "r": len(o["u"]), "n": o["n"], "u": [[k, o["u"][k]] for k in u]}
    for s in allsec:
        if s in withq and s not in st:
            out["secs"][s] = {"lv": 1, "rk": 0, "r": 0, "n": 0, "u": []}
    out["ranked"] = N
    out["head"], out["rule"] = texts(sid, mode, order, npast)
    return out

def texts(sid, mode, units, npast):
    """押したときの枠に出す文(科目ごとの数え方の説明)"""
    if mode == "round":
        dated = [u for u in units if u != "サンプル問題"]
        rng = f"{dated[0]}〜{dated[-1]}" if len(dated) > 1 else (dated[0] if dated else "")
        if sid == "eisei1":
            head = f"過去{len(units)}回({rng})の公表問題"
            extra = "同じ問題がほかの回にも出ているときは、その回も数えます(第二種の科目の問題も同じ回に数えます)。"
        else:
            kinds = "修了認定試験・公開問題" if sid == "fe" else "公開問題"
            ys = [u.split(" ")[0] for u in dated]
            rng = f"{ys[0]}〜{ys[-1]}" if ys and ys[0] != ys[-1] else (ys[0] if ys else "")
            head = f"過去{len(units)}回({rng}の{kinds}" + ("とサンプル問題" if "サンプル問題" in units else "") + ")"
            extra = "公開問題とサンプル問題は、科目A・科目Bを合わせて1回と数えます。"
        rule = ("★の決め方: この科目の過去問のある節を、出題された回の数(同じなら問題の数)の多い順に並べ、上位30%を★★★ 頻出、"
                "次の35%を★★ よく出る、残りを★ 出題少なめにしています。1回の試験で何問も出た節が強くなりすぎないよう、問題の数ではなく回の数で比べます。"
                "1回だけの出題と、過去問での出題がない節は★です。" + extra + "オリジナル問題は数えません。")
    else:
        vs = "・".join(units)
        head = f"過去問{npast}問(問題集の版: {vs})"
        rule = ("★の決め方: この科目の過去問は、試験の年度ではなく問題集の版ごとに集められていて、1問は1つの版にしか入っていないため、"
                "回の数ではなく問題の数で比べます。過去問のある節を問題の数の多い順に並べ、上位30%を★★★ 頻出、次の35%を★★ よく出る、"
                "残りを★ 出題少なめにしています。1問だけの出題と、過去問での出題がない節は★です。オリジナル問題と Trailhead のクイズは数えません。")
    return head, rule

def load(p):
    with open(p, encoding="utf-8") as f: return json.load(f)

def build(sid, data):
    Q = load(os.path.join(data, "questions.json"))
    sp = os.path.join(data, "sections.json")
    secs = load(sp) if os.path.exists(sp) else []
    return compute(sid, Q, secs)

def dump(o):
    return json.dumps(o, ensure_ascii=False, separators=(",", ":")) + "\n"

def summary(o):
    c = {1: 0, 2: 0, 3: 0}; z = 0
    for v in o["secs"].values():
        if v["r"] or v["n"]: c[v["lv"]] += 1
        else: z += 1
    return f'{o["sid"]}: {o["mode"]} 過去問{o["past"]}問 回/版{len(o["units"])} ★★★{c[3]} ★★{c[2]} ★{c[1]} 出題なし★{z}'

def main(a):
    if a and a[0] == "--check":
        bad = 0
        for sid in SUBJ:
            d = os.path.join(BASE, sid, "data"); p = os.path.join(d, "imp.json")
            if not os.path.exists(os.path.join(d, "questions.json")): continue
            new = dump(build(sid, d))
            if not os.path.exists(p) or open(p, encoding="utf-8").read() != new:
                print(f"注意: {sid}/data/imp.json が過去問と合っていません。python3 make_imp.py で作り直してください", file=sys.stderr); bad += 1
        return
    todo = [(a[0], a[1] if len(a) > 1 else os.path.join(BASE, a[0], "data"))] if a else [(s, os.path.join(BASE, s, "data")) for s in SUBJ]
    for sid, d in todo:
        o = build(sid, d)
        with open(os.path.join(d, "imp.json"), "w", encoding="utf-8") as f: f.write(dump(o))
        print(summary(o))

if __name__ == "__main__":
    main(sys.argv[1:])
