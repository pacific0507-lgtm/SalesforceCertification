"""過去問で問われたのに本文にない知識を、各項目の「試験ポイント」の直前に箇条書きで追記する。
使い方: python3 add_pastq_text.py <chapters.json> <追記分.json> <出力 chapters.json>
追記分.json: [{section, ids, text, status, source_url, note}]
見出し「過去問で問われた関連知識」の下に <ul class="pq"> で並べる(既にあれば中身を差し替える)。
"""
import html, json, re, sys
chs, addp, out = sys.argv[1:4]
D = json.load(open(chs, encoding="utf-8")); A = json.load(open(addp, encoding="utf-8"))
by = {}
for e in A: by.setdefault(e["section"], []).append(e)
HEAD = '<h4 class="pq-h">過去問で問われた関連知識</h4>'
done = set()
for c in D:
    h = c["data"]["html"]
    def rep(m):
        art, sec = m.group(0), m.group(1)
        if sec not in by: return art
        art = re.sub(re.escape(HEAD) + r'<ul class="pq">.*?</ul>\n?', "", art, flags=re.S)
        block = HEAD + '<ul class="pq">\n' + "".join(f"<li>{html.escape(e['text'], quote=False)}</li>\n" for e in by[sec]) + "</ul>\n"
        for anchor in ('<div class="co memo">', '<div class="done-row">'):
            i = art.rfind(anchor)
            if i >= 0:
                done.add(sec); return art[:i] + block + art[i:]
        sys.exit(f"挿入位置なし: {sec}")
    c["data"]["html"] = re.sub(r'<article class="feat" data-sec="([^"]+)".*?</article>', rep, h, flags=re.S)
miss = set(by) - done
if miss: sys.exit(f"項目が見つからない: {miss}")
json.dump(D, open(out, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print("ok", {k: len(v) for k, v in by.items()})
