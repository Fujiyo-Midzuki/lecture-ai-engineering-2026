# 第6回 解答

## 演習

<!-- [tool call] の行は、表示された行をそのまま貼り付けてください。終わらなかった STEP は、空欄のままでかまいません。 -->

- STEP 1 のツールの名前：glossary_search_glossary
- STEP 2 の [tool call]：glossary_search_glossary({'query': '3レベル'})
- STEP 3 の [tool call]：fetch_fetch({'url': 'https://modelcontextprotocol.io/'})
- STEP 4 の [tool call]：aws_aws___search_documentation({'search_phrase': 'Amazon S3 バージョニング 概要', 'topics': ['general']}) の後、aws_aws___search_documentation({'search_phrase': 'What is versioning in Amazon S3', 'topics': ['general']})
- 気づき・疑問：STEP 4 では、同じ aws の検索ツールが日本語、英語の順に2回呼ばれ、モデル応答は3回、入力は11,339 tokens だった。STEP 2（715 tokens）、STEP 3（2,179 tokens）よりかなり多かった。AIがなぜ2回目に英語で検索し直したのかは分からない。また、STEP 4 は質問の内容がAWSに送られると知り、外部のサーバーに何を渡すかを考えて使う必要があると思った。

## 宿題

<!-- 基礎・実装・発展のどれか1つに取り組めば完了です。 -->

- 取り組んだレベル：基礎 
- やったこと：app/mcp_server.py の TODO の行の下に、`server.tool()(tools.get_lecture_summary)` の1行を書き足した。エージェント側（app/mcp_agent.py と app/mcp_servers.json）は変えていない。また、テストが失敗したため、第5回の宿題で 1 に変えていた app/config.py の RAG_TOP_K を、元の 5 に戻した。
- 結果：`uv run python -m app.mcp_agent --list-tools` の一覧に、[glossary_get_lecture_summary] が増えた。「第2回では何を学びますか？」と質問すると、`[tool call]` の行に glossary_get_lecture_summary({'lecture': 2}) が出て、`[tool return]` に第2回の要点が返り、回答に使われた（入力 5,942 tokens／出力 294 tokens、モデル応答 2回）。`uv run pytest -q` は、1回目は 1 failed, 20 passed だった。失敗したのは test_built_index_can_be_searched で、検索結果が2件の想定なのに1件だった。RAG_TOP_K を 5 に戻して再実行すると、21 passed になった。
- 気づき・疑問：エージェント側を変えなくても、サーバー側に1行足すだけで、AIが使える道具が増えて呼ばれたことに驚いた。また、第5回の宿題で変えた設定が、第6回のテストの失敗につながったことに気づいた。設定を変えたあとは、テストを実行して確かめる必要があると思った。なぜ検索件数が1件だと、このテストが失敗するのか、詳しい仕組みはまだよく分からない。
