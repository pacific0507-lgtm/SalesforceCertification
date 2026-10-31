"""CommitStudy の chapters.json にある「キャラの掛け合い」(.co.talk) を talks.json の内容に差し替える。
使い方: python3 apply_talks.py <chapters.json> <talks.json> <出力先>
"""
import html, json, re, sys

NAMES = {"pote": "まなびん", "rou": "クラウドちゃん", "pen": "コミットくん"}

def block(lines):
    ps = ""
    for line in lines:
        k, t = line[0], line[1]
        face = f' data-f="{line[2]}"' if len(line) > 2 else ""
        ps += f'<p class="tk {k}"{face}><b class="who">{NAMES[k]}</b>{html.escape(t, quote=False)}</p>'

    return f'<div class="co talk">{ps}</div>'

src, talks_path, out = sys.argv[1:4]
chs = json.load(open(src, encoding="utf-8"))
talks = json.load(open(talks_path, encoding="utf-8"))
done = set()
for c in chs:
    h = c["data"]["html"]
    def rep(m):
        art = m.group(0)
        sec = m.group(1)
        if sec not in talks:
            return art
        new, n = re.subn(r'<div class="co talk">.*?</div>', lambda _: block(talks[sec]["lines"]), art, count=1, flags=re.S)
        if n:
            done.add(sec)
        return new
    c["data"]["html"] = re.sub(r'<article class="feat"[^>]*id="f-([^"]+)".*?</article>', rep, h, flags=re.S)
missing = [k for k in talks if not k.startswith("_") and k not in done]
if missing:
    sys.exit(f"差し替えできなかった項目: {missing}")
json.dump(chs, open(out, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print(f"{len(done)} 項目を差し替えました")
