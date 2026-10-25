import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("LLM_API_KEY"),
    base_url=os.getenv("LLM_BASE_URL"),
)

resp = client.chat.completions.create(
    model=os.getenv("LLM_MODEL"),
    messages=[
        {"role": "system", "content": "你是一个简洁的技术助手"},
        {"role": "user", "content": "用一句话解释什么是 FDE"},
    ],
    temperature=0.7,
    timeout=60,
)

print("模型:", resp.model)
print("回答:", resp.choices[0].message.content)
print("本次消耗 token:", resp.usage.total_tokens)