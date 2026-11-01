# 仕様: Marketing Cloud Engagement Administrator のテキスト+問題集(日本語)

CommitStudy(Salesforce認定資格の学習アプリ)に、Marketing Cloud Engagement Administrator 試験の科目を追加します。
あなたは1つの章を担当し、各項目(節)の本文HTMLと、その本文にひも付いた4択問題を作ります。

## 試験の範囲(公式)
Digital marketing proficiency 13% / Subscriber data management 18% / Setup 38% / Channel management 16% / Maintenance 15%
資料: Trailhead のモジュール「Prep: Marketing Cloud Engagement Admin: Setup and Data」「Cert Prep: Marketing Cloud Engagement Admin: Marketing, Channels, & Maintenance」と、各単元で挙がっている Salesforce ヘルプ。

## 調べ方(必須)
- 事実はすべて公式情報で確認する。`mcp__Salesforce-Docs-MCP__salesforce_docs_search`(ToolSearch で "select:mcp__Salesforce-Docs-MCP__salesforce_docs_search" を読み込む。`salesforce_docs_fetch` もあれば使う)で help.salesforce.com の Marketing Cloud Engagement のページを探す。必要なら WebFetch で trailhead.salesforce.com の単元本文も読んでよい。
- 推測で書かない。確認できなかったことは本文に書かない。製品名は現在の公式名(Marketing Cloud Engagement、Email Studio、Journey Builder など)。画面名は英語のまま「 」で書いてよい。

## 本文HTMLの書き方
見本: reference_sections.html(Data 360 の2項目。構造と文体を合わせる。図(figure)は不要)
各項目の `html` は、<article> と <h3> を除いた中身。次の順で並べる:
1. `<div class="co talk">…</div>` キャラの掛け合い(4〜6行)。
   - 話者: `<p class="tk pote"><b class="who">まなびん</b>…</p>`(学習者・くだけた口調)、`<p class="tk rou"><b class="who">クラウドちゃん</b>…</p>`(先生・です/ます)、`<p class="tk pen"><b class="who">コミットくん</b>…</p>`(ロボット・「〜だ」、短く、ときどきプログラミングのたとえ)。
   - 表情は任意で `data-f="smile|eager|sad|surprise|sweat|think|wink"` を p に付ける。
   - **項目ごとに掛け合いの型を変える**(出題して間違える/ボケとツッコミ/学習者が先に説明する/なぞなぞ/2人だけ/たとえ話のリレー/専門用語をかみ砕く など)。毎回「質問→説明→補足→なるほど」にしない。
2. `<p class="one">` その機能を一言で説明する1〜2文。
3. `<div class="co tips"><p><b class="lab">たとえるなら</b>…</p></div>` 身近なたとえ。
4. 本体: `<h4>見出し</h4>` と `<ul>`/`<ol class="steps">`/表 `<div class="tw"><table><thead><tr><th>…</th></tr></thead><tr><td>…</td></tr></table></div>` を組み合わせる。知識は1つの <li> に1つ。
5. 必要なら2つ目の掛け合い `<div class="co talk t2">…</div>`(2〜3行、補足)。
6. `<div class="co memo"><p><b class="lab">試験ポイント</b></p><ul><li>…</li></ul></div>` 試験に出やすい点を3〜5個。
- 文体: です/ます。1文は短く。専門用語は初出で一言説明。Markdown記号は使わない。<b> は強調に少しだけ。
- 1項目の本文はおよそ 900〜1600 字(掛け合いを除く)。

## 問題の書き方
- 各項目につき指定の問題数。4択(正解1つ。「2つ選択」の問題は全体の1〜2割まで、そのときは問題文末に「(2つ選択)」)。
- 試験と同じく、シナリオ型(「ある会社は…したい。管理者は何をすべきですか?」)を半分以上に。
- 誤りの選択肢も、もっともらしいMarketing Cloudの用語にする。
- `ex`(解説): 2〜4文。正解の理由と、紛らわしい選択肢がなぜ違うか。
- `u`: 根拠にした公式ページのURL(help.salesforce.com か trailhead.salesforce.com)。
- `x`: **その問題の論点が書かれている本文の1要素の文字列そのもの**。同じ項目の html の中の <li> 1つ、<p> 1つ、または表の1行(<tr> の各セルの文字をつなげたもの)の、タグを除いた全文と完全一致させる。本文に論点がない問題は作らない(先に本文に書く)。
- 問題文・選択肢・解説はすべて日本語。

## 出力
ファイル `out_<担当>.json` に次の形で書く(UTF-8、JSON):
{"chapter": <章番号>, "chapter_title": "...", "chapter_sub": "章の説明1文", "sections": [
  {"id": "<指定のID>", "no": "Ch<章>·<連番>", "title": "日本語の見出し", "tag": "英語名(短く)", "html": "...",
   "questions": [{"q": "...", "o": ["...","...","...","..."], "a": [正解のindex(0始まり)], "ex": "...", "u": "https://...", "x": "..."}]}
]}
書いたら自分で検証する: すべての x が、その項目の html からタグを除いた <li>/<p>/<tr> の文字列のどれかと完全一致すること、a が範囲内であること。
