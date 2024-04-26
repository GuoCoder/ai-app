大家好，我是程序锅。

github上的代码封装程度高，不利于小白学习入门。


常规的大模型RAG框架有langchain等，但是langchain等框架源码理解困难，debug源码上手难度大。

因此，写一个人人都能看懂、人人都能修改的大模型RAG框架代码。

主要分为4个章节，分别为：

**1. 如何调用大模型API**

2. RAG背景介绍

03. 依赖环境安装

04. 知识库构建

05. 基于知识库的大模型问答

本篇文章将介绍如何调用大模型API

## 一、大模型API介绍

大模型的使用可以分为本地调用和远程调用。由于本地硬件资源有限，我们一般选择远程调用大模型（后续小项目，也可自己本地部署大模型）。

目前市面上的大模型有ChatGPT、GPT4、GLM4、文心一言等等，OpenAI的产品由于有关原因被限制，在此我们采用智谱AI的**GLM4**作为实验对象。

1. 登录智谱AI开放平台获取获取API_key


(1) 注册账号

>https://maas.aminer.cn/

![image](https://files.mdnice.com/user/30915/740dbe02-f714-420e-85b6-04a274e19d37.png)


新注册账号有18元的额度，足够实验了。

(2) 获取API_KEY


![1](https://files.mdnice.com/user/30915/ebb45bef-f5b9-4e99-b89a-0340902fb249.png)



![2](https://files.mdnice.com/user/30915/f12c7022-35bc-421d-a695-fe297a791c7b.png)

注意，请不要泄露自己的API Keys！

2. API文档说明

请牢记上图的API key，现在我们看一看GLM4的API调用文档。

（1）查看接口文档
![image](https://files.mdnice.com/user/30915/776e4a61-1c36-40c2-83d8-07a4d2389a4d.png)

（2）查看调用示例
![image](https://files.mdnice.com/user/30915/d1a6f619-987d-4a7b-b79e-faed77d1e80a.png)

当然，我这里只讨论最简单的API调用形式，还有很多接口的参数没有利用到。

后续我们的小项目会根据实际需求，修改代码。

## 三、代码实现

接下来，代码实现它。

``` python
from zhipuai import ZhipuAI
client = ZhipuAI(api_key="") # 填写您自己的APIKey
response = client.chat.completions.create(
    model="glm-4",  # 填写需要调用的模型名称
    messages=[
        {"role": "user", "content": "作为一名营销专家，请为我的产品创作一个吸引人的slogan"},
        {"role": "assistant", "content": "当然，为了创作一个吸引人的slogan，请告诉我一些关于您产品的信息"},
        {"role": "user", "content": "智谱AI开放平台"},
        {"role": "assistant", "content": "智启未来，谱绘无限一智谱AI，让创新触手可及!"},
        {"role": "user", "content": "创造一个更精准、吸引人的slogan"}
    ],
)
print(response.choices[0].message)
```

这里修改API key即可
![image](https://files.mdnice.com/user/30915/1bfb2c48-3223-4430-9871-6c82d277c41b.png)

这样就完成了一个非常简单的大模型API调用，下一章我们将介绍RAG的思路。