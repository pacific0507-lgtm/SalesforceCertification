"""Agentforce Specialist の図(spec_H.py と、あれば spec_I.py)を、科目 afspec の chapters.json に入れる。
  図のない項目には、本文の最初の <p class="one">(一言説明)の直後に図を入れる。
使い方: python3 apply_afspec.py <chapters.json> <出力>
"""
import sys, os, re, json, importlib.util
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, here)
import lib
figs = {}
for name in ("spec_H", "spec_I"):
    if not os.path.exists(os.path.join(here, name + ".py")): continue
    lib.FIGS.clear(); m = importlib.util.spec_from_file_location(name, os.path.join(here, name + ".py")); mod = importlib.util.module_from_spec(m); m.loader.exec_module(mod)
    figs.update({k: v() for k, v in lib.FIGS.items()})
if lib.WARN: sys.exit("警告:\n" + "\n".join(lib.WARN))
src, out = sys.argv[1:3]
ch = json.load(open(src, encoding="utf-8")); done = set()
for c in ch:
    h = c["data"]["html"]
    for sec, fh in figs.items():
        i = h.find(f'data-sec="{sec}"')
        if i < 0: continue
        j = h.find("<article", i + 10); j = len(h) if j < 0 else j
        m = re.compile(r'<figure class="fig[^"]*"[^>]*>.*?</figure>', re.S).search(h, i, j)
        if m: h = h[:m.start()] + fh + h[m.end():]
        else:
            k = h.find('<p class="one">', i, j)
            if k < 0: sys.exit("一言説明が見つからない: " + sec)
            k = h.find("</p>", k) + 4
            h = h[:k] + fh + h[k:]
        done.add(sec)
    c["data"]["html"] = h
print("図", len(done), "/ spec", len(figs))
json.dump(ch, open(out, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
