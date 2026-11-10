"""Data 360 のテキストを現行の公式ヘルプに合わせて直す(2026-11-10)。
  - ストリーミングインサイトの数: 旧 Customer Data Platform ライセンスの「最初の5つだけ」→ 現行は組織で最大20。メジャーは Count と Sum のみ。元にできるソースを現行の一覧に
  - Data Aware Specialist: 旧ライセンスの権限セットで、現行の標準権限セットの一覧にはないことを書き足す
  - ID解決のあいまい一致: 例を「Jon/John」の綴りのゆれにし、精度(高・中・低)と、取引先の項目には使えないことを書き足す
  問題の「該当箇所(x)」や用語カードも同じ文に合わせる。何度実行しても同じ結果になる。
使い方: python3 d360/fix_text_20261110.py
"""
import os
here = os.path.dirname(os.path.abspath(__file__))
R = [
 ("<li>ディメンションは最大10、メジャーは最大5</li>", "<li>ディメンションは最大10、メジャーは最大5(集計の関数は Count と Sum だけ)</li>"),
 ("<li>6つ以上作成できますが、実行されるのは最初の5つだけ</li>", "<li>ストリーミングインサイトは、組織全体で最大20まで(旧 Customer Data Platform ライセンスでは、6つ以上作っても実行されるのは最初の5つだけ)</li>"),
 ("<li>元になるDMOは、Web SDK、モバイルSDK、Marketing Cloud Personalization、Ingestion APIなど、ストリーミング系のソースから作られたもの</li>",
  "<li>元になるDMOは、Web SDK、モバイルSDK、Marketing Cloud Personalization、Ingestion API(ストリーミング・バッチ)、Amazon Kinesis、Apache Kafka、CRM ストリーミングなど、ストリーミング系のソースから作られたエンゲージメント型のもの</li>"),
 ("6つ以上作れますが、実行されるのは最初の5つだけです。元になるDMOは", "いまの Data 360 では、組織全体で20個までです。旧ライセンスでは、6つ以上作っても実行されるのは最初の5つだけでした。元になるDMOは"),
 ("ディメンションは最大10、メジャーは最大5です。6つ以上作成できますが、実行されるのは最初の5つだけです。", "ディメンションは最大10、メジャーは最大5(関数は Count と Sum だけ)、ストリーミングインサイトは組織全体で最大20です。旧 Customer Data Platform ライセンスでは、6つ以上作っても実行されるのは最初の5つだけでした。"),
 ("最小の権限セットは、Data Aware Specialistです。</li>\n</ul>",
  "最小の権限セットは、Data Aware Specialistです。</li>\n<li>Data Aware Specialist は、旧 Customer Data Platform ライセンスの標準権限セットです。いまの Data 360 の標準権限セットの一覧(Data Cloud Architect〔旧 Data Cloud Admin〕、Activation Manager、Activation Specialist、User など)には載っていません。過去問では選択肢として出ます。</li>\n</ul>"),
 ("より広い権限セットではなく、最小の権限という条件で問われる点を押さえます。\"}", "より広い権限セットではなく、最小の権限という条件で問われる点を押さえます。旧 Customer Data Platform ライセンスの権限セットで、いまの標準権限セットの一覧にはありません。\"}"),
 ('"x":"ディメンションは最大10、メジャーは最大5"', '"x":"ディメンションは最大10、メジャーは最大5(集計の関数は Count と Sum だけ)"'),
 ('"x":"元になるDMOは、Web SDK、モバイルSDK、Marketing Cloud Personalization、Ingestion APIなど、ストリーミング系のソースから作られたもの"',
  '"x":"元になるDMOは、Web SDK、モバイルSDK、Marketing Cloud Personalization、Ingestion API(ストリーミング・バッチ)、Amazon Kinesis、Apache Kafka、CRM ストリーミングなど、ストリーミング系のソースから作られたエンゲージメント型のもの"'),
 ("あいまい一致(Fuzzy。「太郎」と「タロウ」のような表記ゆれを許す)", "あいまい一致(Fuzzy。「Jon」と「John」のような綴りのゆれを許す。精度は高・中・低から選べ、取引先〔Account〕の項目には使えない)"),
]
files = ["data/chapters.json", "data/questions.json", "data/terms.json", "anchors.json", "orig/out.json", "research/input_C.json"]
tot = {o: 0 for o, _ in R}
for f in files:
    p = os.path.join(here, f)
    s = open(p, encoding="utf-8").read(); t = s
    for o, n in R:
        for oo, nn in ((o, n), (o.replace("\n", "\\n"), n.replace("\n", "\\n"))):
            c = t.count(oo); tot[o] += c; t = t.replace(oo, nn)
    if t != s: open(p, "w", encoding="utf-8").write(t); print("更新:", f)
for o, c in tot.items(): print(c, o[:40])
