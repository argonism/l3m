from openai import OpenAI

client = OpenAI(base_url="http://localhost:4000/v1", api_key="dummy")

r = client.chat.completions.create(
    model="gpt-oss-20b",  # litellm_config.yaml の論理名
    messages=[{"role":"user","content":"自己紹介して"}],
    temperature=0.7,
)
print(r.choices[0].message.content)
