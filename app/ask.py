"""第1回: 素のLLMに質問を続けられる対話スクリプト。

使い方:
    uv run python -m app.ask "LoRAとは何ですか？"
    uv run python -m app.ask            # 最初に講座固有の質問をして対話を開始する

会話履歴はユーザー発言とAIの回答の両方を含む。
"exit" または "quit" を入力すると終了する。
"""

import argparse

from google import genai
from google.genai import errors, types

from app.config import MODEL, api_error_message, get_api_key

# 講座に固有の質問。正しい答えは data/glossary.json の homework-levels にある
DEFAULT_QUESTION = "AIE2026の講座の宿題にある「3レベル」とは何ですか？"


def ask(
    question: str,
    history: list[types.Content] | None = None,
    client: genai.Client | None = None,
) -> str:
    if history is None:
        history = []
    if client is None:
        client = genai.Client(api_key=get_api_key())

    history.append(types.Content(role="user", parts=[types.Part(text=question)]))
    response = client.models.generate_content(model=MODEL, contents=history)
    answer = response.text

    history.append(types.Content(role="model", parts=[types.Part(text=answer)]))

    usage = response.usage_metadata
    if usage is not None:
        print(f"[入力トークン数] {usage.prompt_token_count}")
        print(f"[出力トークン数] {usage.candidates_token_count}")

    return answer


def main() -> None:
    parser = argparse.ArgumentParser(description="LLMと対話する")
    parser.add_argument("question", nargs="?", default=DEFAULT_QUESTION)
    args = parser.parse_args()

    print(f"[model] {MODEL}")
    history: list[types.Content] = []
    client = genai.Client(api_key=get_api_key())

    try:
        print(f"[質問] {args.question}\n")
        print(ask(args.question, history=history, client=client))

        while True:
            try:
                question = input("\n[質問] ").strip()
            except EOFError:
                break

            if question.lower() in {"exit", "quit"}:
                break
            if not question:
                continue

            print()
            print(ask(question, history=history, client=client))
    except errors.APIError as e:
        print(api_error_message(e.code, e.message))
        raise SystemExit(1)


if __name__ == "__main__":
    main()
