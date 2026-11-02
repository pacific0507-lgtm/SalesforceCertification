"""スマホ(iPhone)前提の図を作るための部品。CommitStudy の図クラス(.gba/.gby/.gbo/.gbr/.gb/.gbd/.gtb/.gts/.gta/.gtr/.gto/.gl/.gla/.glr/.glo/.gld)を使い、テーマの配色に追従する。
  - 横幅は W=340(iPhone の本文幅 約320px で 0.94倍。文字 .gts=11.5 → 約10.8px、.gtb=13 → 約12.2px)
  - 高さは 160〜520 を目安(縦に長すぎると見づらい)。横スクロールはしない(figure class="fig m")
  - 文字の大きさは CSS のクラスで決まる(font-size 属性は効かない): gtb/gta/gtr/gto/gt/gtm=13, gts=11.5
使い方: f = Fig("fsi", 300, "aria の説明"); f.box(...); ...; html = f.svg("キャプション")
"""
import html as _h

W = 340
FS = {"gtb": 13, "gta": 13, "gtr": 13, "gto": 13, "gt": 13, "gtm": 13, "gts": 11.5, "gtw": 13}

def tw(s, fs):
    """文字幅の目安(全角=1.0em、半角=0.58em)"""
    return sum(fs * (0.58 if ord(ch) < 0x2000 else 1.0) for ch in s)

class Fig:
    def __init__(self, fid, h, aria, w=W):
        self.fid, self.h, self.w, self.aria = fid, h, w, aria
        self.el, self.warn, self.boxes = [], [], []

    def _chk_text(self, x, t, cls, anchor, limit_l=None, limit_r=None):
        wd = tw(t, FS.get(cls, 13))
        l = x if anchor == "start" else x - wd / 2 if anchor == "middle" else x - wd
        r = l + wd
        lo = 2 if limit_l is None else limit_l
        hi = self.w - 2 if limit_r is None else limit_r
        if l < lo - 0.5 or r > hi + 0.5:
            self.warn.append(f"{self.fid}: 「{t}」がはみ出す(左{l:.0f} 右{r:.0f} / 範囲{lo:.0f}〜{hi:.0f})")

    def box(self, x, y, w, h, cls, title, subs=(), tcls="gtb", scls="gts", step=17):
        """角丸の箱。1行目は太字、2行目以降は小さい灰色の字。中央そろえ"""
        self.el.append(f'<rect class="{cls}" x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}" rx="9"/>')
        self.boxes.append((x, y, w, h, title))
        lines = [(title, tcls)] + [(s, scls) for s in subs]
        n = len(lines); y0 = y + h / 2 - (n - 1) * step / 2 + 4.4
        if (n - 1) * step + 16 > h: self.warn.append(f"{self.fid}: 箱「{title}」の高さ{h}に{n}行は窮屈")
        for i, (t, c) in enumerate(lines):
            if not t: continue
            self._chk_text(x + w / 2, t, c, "middle", x + 4, x + w - 4)
            self.el.append(f'<text class="{c}" x="{x + w / 2:g}" y="{y0 + i * step:.1f}" text-anchor="middle">{_h.escape(t)}</text>')
        return (x, y, w, h)

    def frame(self, x, y, w, h, cls="gbd"):
        """点線などの囲み(グループ)"""
        self.el.append(f'<rect class="{cls}" x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}" rx="11"/>')

    def text(self, x, y, t, cls="gts", anchor="start"):
        self._chk_text(x, t, cls, anchor)
        self.el.append(f'<text class="{cls}" x="{x:g}" y="{y:g}" text-anchor="{anchor}">{_h.escape(t)}</text>')

    def _mk(self, c):
        return {"n": "mk_an", "a": "mk_aa", "r": "mk_ar", "o": "mk_ao", "d": "mk_an"}[c]

    def arrow(self, x1, y1, x2, y2, c="n", dash=False, head=True):
        """直線の矢印。c: n=黒 a=アクセント r=赤 o=緑。dash=True で点線"""
        cls = {"n": "gl", "a": "gla", "r": "glr", "o": "glo"}[c]
        st = ' stroke-dasharray="5 4"' if dash else ""
        mk = f' marker-end="url(#{self.fid}-{self._mk(c)})"' if head else ""
        self.el.append(f'<line class="{cls}" x1="{x1:g}" y1="{y1:g}" x2="{x2:g}" y2="{y2:g}"{st}{mk}/>')

    def path(self, pts, c="n", dash=False, head=True):
        """折れ線の矢印。pts=[(x,y),...]"""
        cls = {"n": "gl", "a": "gla", "r": "glr", "o": "glo"}[c]
        d = "M" + " L".join(f"{x:g} {y:g}" for x, y in pts)
        st = ' stroke-dasharray="5 4"' if dash else ""
        mk = f' marker-end="url(#{self.fid}-{self._mk(c)})"' if head else ""
        self.el.append(f'<path class="{cls}" d="{d}"{st}{mk}/>')

    def cross(self, x, y, r=6):
        """赤い ✕ 印(つなげない・使えない を表す。赤い点線の途中や先に置く)"""
        self.el.append(f'<circle cx="{x:g}" cy="{y:g}" r="{r + 3:g}" class="gbr"/>'
                       f'<path class="glr" d="M{x - r * .6:g} {y - r * .6:g} L{x + r * .6:g} {y + r * .6:g} M{x + r * .6:g} {y - r * .6:g} L{x - r * .6:g} {y + r * .6:g}"/>')

    def check(self):
        """箱どうしの重なりも調べる"""
        b = self.boxes
        for i in range(len(b)):
            for j in range(i + 1, len(b)):
                x1, y1, w1, h1, t1 = b[i]; x2, y2, w2, h2, t2 = b[j]
                if x1 < x2 + w2 - 1 and x2 < x1 + w1 - 1 and y1 < y2 + h2 - 1 and y2 < y1 + h1 - 1:
                    self.warn.append(f"{self.fid}: 箱「{t1}」と「{t2}」が重なっている")
        for x, y, w, h, t in b:
            if x < 0 or y < 0 or x + w > self.w or y + h > self.h:
                self.warn.append(f"{self.fid}: 箱「{t}」が図の外にはみ出す")
        return self.warn

    def svg(self, caption):
        self.check(); WARN.extend(self.warn)
        defs = "".join(f'<marker id="{self.fid}-{m}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" class="{m}"/></marker>' for m in ("mk_aa", "mk_an", "mk_ar", "mk_ao"))
        return (f'<figure class="fig m"><svg viewBox="0 0 {self.w} {self.h}" role="img" aria-label="{_h.escape(self.aria)}"><defs>{defs}</defs>'
                + "".join(self.el) + f'</svg><figcaption>{_h.escape(caption)}</figcaption></figure>')

WARN = []
FIGS = {}
def fig(sec):
    """@fig("項目のdata-sec") を付けた関数が、その項目の図(figure の HTML)を返す"""
    def deco(fn): FIGS[sec] = fn; return fn
    return deco
