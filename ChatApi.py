import openai

Key = input("请输入你的openai的key（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）：")


# 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
openai.api_key = Key


# 这个用GPT提问并返回答案
def gpt(question):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": question}]
    )
    answer = completion.choices[0].message["content"]
    return answer
