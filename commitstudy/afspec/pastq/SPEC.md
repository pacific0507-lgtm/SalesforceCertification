# 過去問の検証・翻訳・テキストへのひも付け(Agentforce スペシャリスト)

CommitStudy の科目「Agentforce スペシャリスト」(afspec)に、Notion の過去問を取り込みます。進め方と出力の形は Marketing Cloud Engagement Administrator(`mcadmin/pastq/SPEC.md`、元は `mulepa/pastq/SPEC.md`)と同じです。

## 原本(Notion「Agentforce Specialist」の子ページ)
- `v2026-08-19`: 英語164問(すべて3択・1つ選択)→ `in_A.json`(ラベル A)。子ページはこの1つだけで、日付のない回はない。
- 原本では「Question 122/164」が2回続けて入っていて(中身も同じ)、本来の Q123 はない。2つ目を Q123 として扱い、Q122 の重複にした。
- 重複は同じ回の中で番号の小さいほうを残す。164問 → 159問。重複の対応は `dups.json`([残した回, 番号, 重複の回, 番号, 正解が同じか])。Q102 と Q114 は正解が食い違う(`note`)。
- 問題文の先頭の「Choose 1 option.」は取り除いた。

## 1問ごとの作業
- 正解を help.salesforce.com・developer.salesforce.com・architect.salesforce.com(Salesforce-Docs MCP)で確かめ、判定 `v` を次から1つ: `公式で確認済み` / `解答を修正(公式にもとづく)`(ex の最後に「原本の解答は X でしたが、…のため Y が正解です。」) / `要確認(矛盾あり)`(最も妥当な方を a にし、食い違いを ex に書く) / `原本どおり`
- 製品名が変わったもの(Einstein Copilot → Agentforce、Agent Builder → Agentforce Builder、トピック → サブエージェント、Einstein Studio → AI Models、Data Cloud → Data 360 など)は問題を残し、ex に改名を書く。
- q/o/ex は日本語(製品名・画面名は公式の英語名。テキスト本文の表記に合わせる)。u は根拠のURL(確かめられないときは null)。
- f は afspec の項目ID、x は本文の1要素(`<li>`/`<p>`/表の行)の文字列そのまま。本文に論点がなければ x を null にして add(公式で確かめた事実だけ。60〜140字程度)。確かめられないときは x も add も入れない。

## 出力
`out_<ラベル>.json`: {label, no, f, a, q, o, ex, u, v, x, add(任意)}。`python3 add_pastq_afspec.py afspec/pastq afspec/pastq afspec/data <出力>` で問題集と本文に追加する。出典 s は「v2026-08-19 Q12」の形で、問題の番号は `ids.json` で固定(オリジナル117問の後ろ、118〜)。
