"""4グループで別々に作った「過去問で問われた関連知識」の重複をまとめる(out_*.json を上書き)。"""
import json, glob, os
d = os.path.dirname(os.path.abspath(__file__))
C2MA = "Contacts to Multiple Accounts を有効にすると、1人の取引先責任者を主取引先以外の複数の取引先にも関連付けられます。「取引先名」の取引先が主取引先(直接の関係)で、それ以外の取引先とは間接の関係になります。"
C2MA_PA = "Contacts to Multiple Accounts は個人取引先にも使えます。個人取引先どうし、または個人取引先と法人取引先・取引先責任者を関連付けた関係は、常に間接的な関係として記録されます。"
FC = "Pipeline Forecasting のロールアップには単一分類と累積の2方式があり、設定で選びます。累積ロールアップ(既定)では、Open Pipeline、Best Case Forecast、Commit Forecast のように複数の売上予測分類の商談を合算して表示します。"
ROLE = "ロールでは、そのロールのユーザーが所有する取引先に関連する商談・取引先責任者・ケースへのアクセス(参照のみ、参照・更新など)を、子レコードの所有者に関係なく指定できます。商談の組織の共有設定が公開/参照・更新可能のときは、商談のアクセスは指定できません。"
FIX = {("v2026-08-04", 6): ("opps", C2MA), ("v2026-03-03", 11): ("opps", C2MA), ("Sales-Con-201", 67): ("opps", C2MA),
       ("Sales-Con-201", 77): ("opps", C2MA), ("Sales-Con-201", 4): ("opps", C2MA), ("v2026-03-03", 67): ("opps", C2MA_PA),
       ("v2026-03-03", 1): ("forecast", FC), ("Sales-Con-201", 35): ("forecast", FC),
       ("v2026-03-03", 69): ("security", ROLE), ("Sales-Con-201", 93): ("security", ROLE)}
n = 0
for f in sorted(glob.glob(os.path.join(d, "out_*.json"))):
    L = json.load(open(f, encoding="utf-8"))
    for it in L:
        k = (it["label"], it["no"])
        if k in FIX:
            assert it.get("add"), k
            it["f"], it["add"]["text"] = FIX[k]; n += 1
    json.dump(L, open(f, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("まとめた", n)
