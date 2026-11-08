# 過去問の検証・翻訳・テキストへのひも付け(Marketing Cloud Engagement Administrator)

CommitStudy の科目「Marketing Cloud Engagement Administrator」(mcadmin)に、Notion の過去問を取り込みます。進め方と出力の形は MuleSoft Platform Architect(`mulepa/pastq/SPEC.md`)と同じです。

## 原本(Notion「Marketing Cloud Engagement Administrator」の子ページ)
- `v2026-03-24`: 日本語(機械翻訳調)106問 → `in_A.json`(ラベル A)
- `v2026-02-19`: 英語81問 → `in_B.json`(ラベル B)
- `v2025-09-22`: 英語34問。2つの問題集(MCE-Admn-201 の NO.1〜17 と、旧 Marketing Cloud Administrator の NO.1〜17)が1ページに入っている。番号が重ならないよう、2つ目は Q18〜Q34 と続き番号にした(`src` に元の番号) → `in_C.json`(ラベル C)
- 重複は「日付のある回どうしは新しいほう」を残す。同じ回の中の重複は番号の小さいほうを残す。221問 → 129問。重複の対応は `dups.json`([残した回, 番号, 重複の回, 番号, 正解が同じか])。
- 日本語の原本(`lang: "ja"`)で英語の重複がある問題は、`qj`/`oj` が日本語の原本、`qe`/`oe` が英語の重複(選択肢はこの回の順に並べ替え。`text_from` が元)。英語の重複がない日本語の問題は `qe`/`oe` に日本語を入れ、問題集には英語の原文を持たせない。

## 1問ごとの作業
- 正解を help.salesforce.com(Salesforce-Docs MCP の `admin/mktg`)で確かめ、判定 `v` を次から1つ: `公式で確認済み` / `解答を修正(公式にもとづく)`(ex の最後に「原本の解答は X でしたが、…のため Y が正解です。」) / `要確認(矛盾あり)`(最も妥当な方を a にし、食い違いを ex に書く) / `原本どおり`
- q/o/ex は日本語(製品名・画面名は公式の英語名。テキスト本文の表記に合わせる)。u は根拠のURL(確かめられないときは null)。
- f は mcadmin の項目ID、x は本文の1要素(`<li>`/`<p>`/表の行)の文字列そのまま。本文に論点がなければ x を null にして add(公式で確かめた事実だけ。60〜140字程度)。add は項目の「過去問で問われた関連知識」に入る。同じ add を複数の問題で共有するときは text を完全一致させる。

## 出力
`out_<ラベル>.json`: {label, no, f, a, q, o, ex, u, v, x, add(任意)}。`python3 add_pastq_mcadmin.py mcadmin/pastq mcadmin/pastq mcadmin/data <出力>` で問題集と本文に追加する。出典 s は「v2026-03-24 Q12」の形で、問題の番号は `ids.json` で固定(オリジナル132問の後ろ、133〜)。
