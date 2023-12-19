import os
from dotenv import load_dotenv
from openai import OpenAI
import json


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set.")

client = OpenAI(api_key=api_key)

# completion = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
#         {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
#     ]
# )

# print(completion.choices[0].message)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a college level science professor with PHD"},
        {"role": "user", "content": "Why is the ocean and sky blue?"}
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

print(json_response)