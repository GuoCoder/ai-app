import os

from zhipuai import ZhipuAI
client = ZhipuAI(api_key=os.getenv("ZHIPUAI_API_KEY")) # 填写您自己的APIKey
response = client.chat.completions.create(
    model="glm-4",  # 填写需要调用的模型名称
    messages=[
        {"role": "user", "content": "作为一名自媒体工作者，请为我的产品创作一个吸引人的slogan"},
        {"role": "assistant", "content": "当然，为了创作一个吸引人的slogan，请告诉我一些关于您产品的信息"},
        {"role": "user", "content": "程序锅讲大模型"}
    ]

)
print(response.choices[0].message)