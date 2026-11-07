"""用語カード(terms.json)を確かめる。
使い方: python3 check_terms.py <科目フォルダ(fe など)>
  <科目フォルダ>/terms.json と <科目フォルダ>/manuscript/out_ch*.json を読み、次を調べる。
  - 用語の項目(s)が原稿にあること
  - 用語の語句が、その項目の本文に文字どおりあること(用語カードの「テキストで見る」が探すのと同じく、
    図・見出し・ボタンを除いた1つのテキストの中で探す。括弧書きの用語は、括弧の前の語か括弧の中の別名でもよい)
  - 用語の重複がないこと
  - 説明が空でないこと、「: 」(コロンと空白)を使っていないこと
問題があれば一覧を出して終了コード1で終わる。
"""
import glob, html, json, os, re, sys
from html.parser import HTMLParser

SKIP = {"figure", "svg", "button", "h3", "script", "style"}
VOID = {"br", "img", "hr", "input", "meta", "link", "wbr", "col", "source", "path", "rect", "circle", "line", "polyline", "polygon", "ellipse"}


class Texts(HTMLParser):
    """本文のテキストを、タグで区切られた単位(ブラウザのテキストノード)ごとに集める"""
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.out = [], []

    def handle_starttag(self, tag, attrs):
        if tag not in VOID:
            self.stack.append(tag)

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        while self.stack:
            if self.stack.pop() == tag:
                break

    def handle_data(self, data):
        if data.strip() and not SKIP & set(self.stack):
            self.out.append(data)


def nodes(h):
    p = Texts(); p.feed(h); p.close()
    return [x.lower() for x in p.out]


def cands(t):
    """用語から、本文で探す語の候補を作る(括弧の前の語と、括弧の中の別名)"""
    out = []
    def add(x):
        x = x.strip()
        if len(x) >= 2 and x not in out:
            out.append(x)
    add(t)
    m = re.match(r"^(.*?)[(（]([^()（）]+)[)）]\s*$", t)
    if m:
        add(m[1])
        for x in re.split(r"[、,・/]|旧称?\s*|→", m[2]):
            add(x)
    return out


def main(d):
    terms = json.load(open(os.path.join(d, "terms.json"), encoding="utf-8"))
    secs = {}
    for f in sorted(glob.glob(os.path.join(d, "manuscript", "out_ch*.json")), key=lambda x: int(re.findall(r"\d+", x)[-1])):
        for s in json.load(open(f, encoding="utf-8"))["sections"]:
            secs[s["id"]] = nodes(s["html"])
    errs, seen, per = [], {}, {}
    for i, c in enumerate(terms, 1):
        s, t, dd = c.get("s"), c.get("t", ""), c.get("d", "")
        tag = f"#{i} [{s}] {t}"
        if set(c) != {"s", "t", "d"}:
            errs.append(f"{tag}: キーが s, t, d 以外")
        if s not in secs:
            errs.append(f"{tag}: 項目が原稿にない"); continue
        per[s] = per.get(s, 0) + 1
        if not any(k.lower() in n for k in cands(t) for n in secs[s]):
            errs.append(f"{tag}: 語句が項目の本文にない")
        if t in seen:
            errs.append(f"{tag}: 重複(#{seen[t]} と同じ用語)")
        seen.setdefault(t, i)
        if not dd.strip():
            errs.append(f"{tag}: 説明が空")
        if re.search(r"[:：] ", dd) or "：" in dd:
            errs.append(f"{tag}: 説明にコロンがある")
    empty = sorted(set(secs) - set(per))
    print(f"{d}: 用語 {len(terms)} 件、項目 {len(per)}/{len(secs)}")
    for s in sorted(per, key=lambda k: list(secs).index(k)):
        print(f"  {s}: {per[s]}")
    if empty:
        print("  用語のない項目:", ", ".join(empty))
    for e in errs:
        print("NG", e)
    print("問題なし" if not errs else f"問題 {len(errs)} 件")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(max(main(d.rstrip("/")) for d in sys.argv[1:]) if len(sys.argv) > 1 else print(__doc__) or 2)
