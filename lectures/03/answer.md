# 第3回 解答

## 演習

- 第1回（素のLLM）とエージェントの回答の違い：素のLLMは「レベル1・2・3」など一般論を答えた。エージェントは用語集を検索して「基礎・実装・発展」と、どれか1つで完了というルールまで正しく答え、「関連する回：第1回」も示した。
- `--trace` で見えたツール呼び出し（ツール名と引数）：search_glossary({'query': 'LoRA'}) と search_glossary({'query': 'QLoRA'}) が別々に呼ばれた。
- 1つの質問での LLM 呼び出し回数（`requests`）：LoRAとQLoRAの質問で requests=2, tool_calls=2。確認問題の質問では requests=2, tool_calls=1。
- 追加したツールと、docstring に書いた説明：make_quiz(lecture: int) を追加。docstringに「復習用の確認問題を出したいときに使う（例：第2回の確認問題を出して）」と書いた。「モデルに見えているツール」は3個になり、make_quiz({'lecture': 2}) が呼ばれることを確認し、pytest は11 passed。

## 宿題

- 取り組んだレベル：基礎 / 実装 / 発展
- やったこと：
- 結果：
- 気づき・疑問：
