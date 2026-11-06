# 過去問の検証・翻訳・テキストへのひも付け(MuleSoft Platform Architect)

CommitStudy(Salesforce認定資格の学習アプリ)の科目「MuleSoft Platform Architect」(Salesforce Certified MuleSoft Platform Architect、旧 MuleSoft Certified Platform Architect - Level 1)に、Notion にある過去問(英語)を取り込みます。原本の解答には誤りが混じっていることがあるので、**1問ずつ公式情報で検証**してから日本語にします。

## 入力
- 担当分: `in_<担当>.json`。各問 {label, no, qe(英語の問題文), oe(英語の選択肢), ans(原本の正解 index。複数正解の問題もある), ans_raw, expl(原本の解説。誤りも多いので鵜呑みにしない), also(同じ問題がほかの回にも出たときの [label,no])}
- テキストの各項目の本文: `sections_units.json` = {項目ID: {chapter, title, units: [本文の <li>/<p>/表の行 の文字列]}}

## 1問ごとの作業
1. **検証**: 正解を公式情報で確かめる。主な情報源は MuleSoft の公式ドキュメント docs.mulesoft.com(WebFetch で読む)。`mcp__Salesforce-Docs-MCP__salesforce_docs_search`(ToolSearch で "select:mcp__Salesforce-Docs-MCP__salesforce_docs_search,mcp__Salesforce-Docs-MCP__salesforce_docs_fetch" を読み込む。collection は "mulesoft/...")も使える。API 主導の接続・C4E などの考え方は trailhead.salesforce.com の MuleSoft のモジュールでも確かめてよい。製品名は今の公式名(Omni Gateway(旧 Flex Gateway)、API Visualizer(旧 Anypoint Visualizer)など)。古い製品・機能(CloudHub 1.0、Mule 3 など)が前提の問題は、どの前提の話かを ex に明記する。
2. **判定 `v`**(次のどれか1つ、文字列そのまま):
   - `公式で確認済み` … 原本の正解が公式情報で裏づけられた
   - `解答を修正(公式にもとづく)` … 原本の正解が誤り。`a` を正しい選択肢にし、`ex` の最後に「原本の解答は X でしたが、…のため Y が正解です。」と書く
   - `要確認(矛盾あり)` … 公式情報どうし、または原本と公式で食い違い、決めきれない。最も妥当な方を `a` にし、`ex` に食い違いを一言書く
   - `原本どおり` … 公式情報で確かめられなかったが、原本の解答に明らかな誤りはない
3. **翻訳**: `q`(問題文)、`o`(選択肢。oe と同じ順・同じ数)を自然な日本語に。製品名・機能名は公式の英語名のまま(テキスト本文と同じ表記に合わせる。本文は sections_units.json で確認できる)。会社名などの固有名詞はそのまま。
4. **解説 `ex`**: 日本語2〜4文。正解の理由と、ほかの選択肢がなぜ違うか。です/ます。
5. **根拠 `u`**: 根拠にした公式ページのURL(docs.mulesoft.com / trailhead.salesforce.com)。確認できなかったときは null。
6. **項目 `f`**: その問題がいちばん合う項目ID(sections_units.json のキー。例 "policies")。
7. **該当箇所 `x`**: その問題の論点が書かれている本文の1要素を、`sections_units.json` の units から**1つ選び、文字列そのまま**入れる(項目 f の中から。どうしても別の項目にしかないときは `xs` にその項目IDを入れる)。
   - 本文に論点がないときは、`x` を null にして `add` を入れる: `{"text": "本文に足す1文(です/ます、事実のみ、60〜140字)", "source_url": "根拠URL", "note": "根拠の要約"}`。この text は項目 f の末尾近くの「過去問で問われた関連知識」に箇条書きで追加される。**公式で確かめた事実だけ**を書く(確かめられないなら add は作らず、x も null でよい)。
   - 1つの add を複数問で共有したいときは、同じ text を使う(完全一致させる)。

## 出力
`out_<担当>.json` に JSON 配列で、入力と同じ順に:
{"label", "no", "f", "a": [正解index], "q", "o": [...], "ex", "u", "v", "x", "xs"(任意), "add"(任意)}
書いたら検証: 件数が入力と同じ、o の数が oe と同じ、a が範囲内、f が実在、x がある場合は units に完全一致。

- 複数正解の問題は a に正解の index をすべて入れる(問題文の「2つ選択」などはそのまま訳す)。
- 画像が前提で文章だけでは解けない問題は、v を `要確認(矛盾あり)` にせず、ex の冒頭に「(原本は図つき)」と書き、文章からわかる範囲で答える。どうしても解けない問題は配列に入れたうえで "skip": true を付け、理由を ex に書く。
- `"lang":"ja"` の問題は原本が日本語(機械翻訳調のことが多い)。英語の原文はないので、q・o は原本の意味を保ったまま自然な日本語に整える(英語の製品名・機能名は公式の英語名に直す)。`qj`/`oj` がある問題は日本語の原本、`qe`/`oe` はほかの回の英語の同じ問題。
- `note` に、原本どうしの解答の食い違い・原本の解説との矛盾・選択肢の崩れなどが書いてある。必ず読み、公式情報で正解を決める。選択肢が崩れていて意味がとれないものは、ほかの回の同じ問題(also)や図の説明から復元し、復元したことを ex に一言書く。
- `[FIGURE: url]` は原本の図。図がないと解けない問題は上の skip の扱い。
