# d360 オリジナル問題 (out.json) メモ

- 150問。intro 8 / stream 8 / category 8 / refresh 8 / dlo 8 / zerocopy 8 / mapping 8 / transform 8 / space 8 / idr 12 / ci 10 / si 8 / graph 8 / search 8 / segment 8 / activation 8 / action 8 / share 8
- 4択が基本。5択・2つ選択は7問(category-06, mapping-04, space-08, si-06, graph-08 など。q に「2つ選択」と明記)
- 選択肢の並びは key をシードに決定的にシャッフル済み(正解位置の偏りなし)。ex は選択肢の記号を使わない書き方
- x は d360 のビルドと同じ抽出(svg除去 → `<li>`/`<p>`/`<tr>` → html.unescape・タグ除去・空白詰め)で照合し、不一致 0
- u は Salesforce Help(data.c360_a_*)。Salesforce-Docs MCP(release 264)で内容を確認した
- 既存の過去問・Trailhead の問題文と完全一致するものはなし。論点が近い既存問題がある項目(データストリームの電話番号型・先頭ゼロ、Party 主題領域、提案値、公開履歴、Audience DMO など)は避けた

## 本文と Help の食い違い・注意

1. si「6つ以上作成できますが、実行されるのは最初の5つだけ」: これは Help の「Customer Data Platform Limits and Guidelines」(旧CDPライセンス)の記載。現行の「Data 360 Limits and Guidelines」ではストリーミングインサイトの総数は 20(ハードリミット)で、元DMOのソースに Amazon Kinesis、Apache Kafka、CRM Streaming、Ingestion API (Batch) も含まれ、メジャーは Count と Sum のみ。問題ではこの論点を使っていない。本文の見直しを推奨
2. space「標準の権限セットが付与されるのは、既定のデータスペースだけです」: Help では「既定のデータスペースは標準権限セットに関連づけられる(Data Cloud Architect を除く)」。問題(space-02)は既定以外のデータスペースへの手動関連づけだけを問うので矛盾しない
3. space「Data Aware Specialist」: 現行の標準権限セット一覧(c360_a_userpermissions)には Architect / Activation Manager / Activation Specialist / User が載り、Data Aware Specialist は CDP ライセンス側のページにある。問題では使っていない
4. segment の標準公開「12時間または24時間ごと」: Help では Daily(12/24時間)に加えて Weekly / Monthly も選べる。問題(segment-03)は同時実行の上限による遅延を問うだけ
5. idr の照合方法: Help ではあいまい一致は高・中・低の3精度があり、Account の項目ではあいまい一致を使えない。本文の例(太郎/タロウ)は問題に使わず、Jon/John の綴りの揺れにした
6. stream の CRM コネクタ「通常10分ごとの増分」は Help で確認しきれなかったため問題にしていない

## 確認の弱いもの

- intro-02/03(5段階の呼び名): 段階名は本文独自の整理。u は Data 360 の機能概要ページで、名前そのものは Help にない
- ci-10(取り込み → ID解決 → 計算済みインサイトの順): u はフロー連携のページ(処理を順番につなげる例)。順序そのものは本文にもとづく
- transform-02(電話番号の表記ゆれを変換で揃える): Help はストリーミング変換を「取り込んだデータのクレンジング」に使うと説明。電話番号の例は本文にもとづく
