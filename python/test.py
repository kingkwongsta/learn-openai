import os
from dotenv import load_dotenv
from openai import OpenAI
import json


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set.")

client = OpenAI(api_key=api_key)

user_request = input("What can I help you with today? ")

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You have every PHD available and read ever book known"},
        {"role": "user", "content": user_request}
    ]
)

choices_info = [
    {
        "finish_reason": choice.finish_reason,
        "message": {
            "content": choice.message.content,
            "role": choice.message.role,
            "function_call": choice.message.function_call,
            "tool_calls": choice.message.tool_calls,
        },
    }
    for choice in completion.choices
]
result_dict = {
    "id": completion.id,
    "choices": choices_info,
    "created": completion.created,
    "model": completion.model,
    "object": completion.object,
    "usage": {
        "completion_tokens": completion.usage.completion_tokens,
        "prompt_tokens": completion.usage.prompt_tokens,
        "total_tokens": completion.usage.total_tokens,
    },
}
json_response = json.dumps(result_dict, indent=2)

print(result_dict['choices'][0]['message']['content'])