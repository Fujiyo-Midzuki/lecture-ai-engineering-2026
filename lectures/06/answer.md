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

- 取り組んだレベル：基礎 / 実装 / 発展
- やったこと：
- 結果：
- 気づき・疑問：
