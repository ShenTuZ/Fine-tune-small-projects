from openai import OpenAI

client = OpenAI(
    api_key="sk-wzinqxnzpnngnwuxmlumohzwlxlofdncobyuwzjytofokewn",  # 从 `https://cloud.siliconflow.cn/account/ak获取`
    base_url="https://api.siliconflow.cn/v1"
)

messages = [
    {"role": "user", "content": "用当前语言解释微调模型流程"},
]

response = client.chat.completions.create(
    model="ft:LoRA/Qwen/Qwen2.5-72B-Instruct:eyyydwxlnn:JH1:qxoxkqzsreloevfarkma-ckpt_step_14",
    messages=messages,
    stream=True,
    max_tokens=4096
)

for chunk in response:
    print(chunk.choices[0].delta.content, end='')