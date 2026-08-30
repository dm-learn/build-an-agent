import json
import os
import sys
import argparse
from dotenv import load_dotenv

from openai import OpenAI

from prompts import system_prompt
from call_function import available_functions, call_function


def main():
    
    parser = argparse.ArgumentParser(description="Chat bot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    
    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")

    if api_key is None:
        raise RuntimeError("OPENROUTER_API_KEY environmnet variable not set")

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": args.user_prompt},
    ]

    if args.verbose:
        print(f"User prompt: {args.user_prompt}\n")

    for _ in range(20):
        response = client.chat.completions.create(
            model="openrouter/free",
            messages=messages,
            tools=available_functions,
        )

        if args.verbose:
            print("Prompt tokens:", response.usage.prompt_tokens)
            print("Response tokens:", response.usage.completion_tokens)

        message = response.choices[0].message
        messages.append(message)

        if not message.tool_calls:
            print(f"Final message:")
            print(message.content)
            return

        for tool_call in message.tool_calls:
            if tool_call.type != "function":
                continue
            function_args = json.loads(tool_call.function.arguments or "{}")
            print(f"Calling function: {tool_call.function.name}({function_args})")

            result_message = call_function(tool_call, args.verbose)

            if not result_message.get("content"):
                raise RuntimeError(f"Empty function response for {tool_call.function.name}")
            if args.verbose:
                print(f"-> {result_message['content']}")
            messages.append(result_message)
    
    print("Maximum iterations reached before final response")
    sys.exit(1)


if __name__ == "__main__":
    main()

