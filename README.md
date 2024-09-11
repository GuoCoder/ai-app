<p><img src="./assets/sologan.png" alt="sologan" style="zoom:50%;" /></p>

<p> 
<a href="https://github.com//llm-action/blob/main/pic/wx.jpg"> <img src="https://img.shields.io/badge/程序锅锅-1AAD19.svg?style=plastic&logo=wechat&logoColor=white" > </a>
<a href="https://www.zhihu.com/people/echo-liu-32"> <img src="https://img.shields.io/badge/程序锅-0079FF.svg?style=plastic&logo=zhihu&logoColor=white"> </a>
<a href="https://blog.csdn.net/qq_35054222"> <img src="https://img.shields.io/badge/CSDN-程序锅锅-FC5531.svg"> </a>
</p> 


## 目录

- 🔥 [服务器基础环境安装及常用工具](#服务器基础环境安装及常用工具)
  - 🐫[PyCharm安装](#pycharm安装)
  - 🐼[Anaconda安装及原理介绍](#Anaconda安装)
  - 💪[实战：用VSCode远程服务器开发](https://zhuanlan.zhihu.com/p/693420628)
- 🐎 [大模型调用总结](#大模型调用)
  - 🐎[主流大模型API调用总结](#主流大模型API调用总结)
  - 🍚[大模型部署推理](#大模型部署推理)
- [大模型原理介绍](#大模型原理介绍)
  - [Transformer原理介绍](#Transformer原理介绍)
  - [实战：从零实现llama3](#从零实现llama3)
- 🍄[检索增强生成(RAG)](#检索增强生成)
  - 🗼[RAG原理介绍](#检索增强生成)
  - 🌼 [ragflow介绍](#ragflow)
  - 💪 [实战：自己手写一个最简单的RAG](#实战-手写一个最简单的RAG)
  - 💪 [实战：基于ragflow做了款初中历史辅导工具](#实战-基于ragflow做一款初中历史辅导工具)
- 🎪[向量数据库技术](#向量数据库)
  - 🐮 [向量数据库原理介绍](#向量数据库原理介绍)
  - 💪 [实战-自己手写一个最简单的向量数据库](#实战-自己手写一个最简单的向量数据库)
- 🚅 [大模型训练](#大模型训练)
  - ❄️[模型训练基础知识](#模型训练基础知识)
  - 🚀 [LoRA微调](#LoRA微调)
  - 💪[实战-用LLaMAFactory微调数百种大模型](#实战-基于LLaMAFactory微调)
  - 💪[实战-微调大模型实现商品评价情感预测](#实战-大模型做情感预测)
- 🚀 [大模型Agent框架](#Agent)
  - 🏠 [Agent原理介绍](#Agent原理介绍)
  - 💪 [实战-自己手写一个最简单的Agent](#自己手写一个最简单的Agent)
- ♻️ [AI图像生成](#AI图像生成)
  - 📐 [StableDiffusion1.5](#StableDiffusion1.5)
  - 💎 [SDXL](#SDXL)
  - 🍦 [ControlNet](#ControlNet)
  - 💪 [实战-基于easyphoto实现AI换脸](#实战-基于easyphoto实现AI换脸)
- :house_with_garden:  [AI语音合成](#AI语音合成)
  - ♻️ [VITS-fast-fine-tuning](#VITS-fast-fine-tuning)
  - 📐 [GPT-SoVITS](#GPT-SoVITS)
  - 💪 [实战-克隆自己的声音](#克隆自己的声音)
- 🎵 [AI音乐合成](#AI音乐合成)
  - 📐 [Suno](#Suno)
- 📞 [我用AI技术做了一个虚拟女友](#我用AI技术做了一个虚拟女友)
- 💬 [AI技术应用交流群](#AI技术应用交流群)
- 👥 [微信公众号](#微信公众号)



## 服务器基础环境安装及常用工具

### pycharm安装

- [最新版pycharm专业版（2023.3.4）环境安装以及永久使用方法](https://zhuanlan.zhihu.com/p/689191237)

### Anaconda

- [Anaconda安装与原理介绍](https://mp.weixin.qq.com/s?__biz=MzkwNzY3ODU5MA==&mid=2247483956&idx=1&sn=efdb4783a00cb10349f80ab2f818dbcf&chksm=c1defe6805c5fc674158167fec0cde2a6152137cfa3e0f0b836414b4314cb03ea013b75511bc&scene=126&sessionid=1714101698#rd)

## 大模型调用

### 主流大模型API调用总结

采用语言python

| 大模型     | 厂商名称 | API调用文档                                                  | 支持模型(闭源)                                    | 依赖下载                                    |
| ---------- | -------- | ------------------------------------------------------------ | ------------------------------------------------- | ------------------------------------------- |
| chatglm    | 智谱     | [链接](https://open.bigmodel.cn/dev/api#glm-4)               | GLM-4、GLM-4V、GLM-3-Turbo                        | ```pip install zhipuai```                   |
| 星火大模型 | 科大讯飞 | [链接](https://www.xfyun.cn/doc/spark/Web.html)              | V1.5、V2.0、V3.0和V3.5四个版本                    | ```pip install --upgrade spark_ai_python``` |
| 通义千问   | 阿里     | [链接](https://help.aliyun.com/zh/dashscope/developer-reference/model-introduction) | qwen-turbo、qwen-plus、qwen-max等                 | ```pip install dashscope```                 |
| 文心一言   | 百度     | [链接](https://cloud.baidu.com/doc/WENXINWORKSHOP/s/xlmokikxe) | ERNIE-4.0、ERNIE-3.5、ERNIE-Lite等                | ```pip install qianfan```                   |
| kimi       | 月之暗面 | [链接](https://platform.moonshot.cn/docs/api/chat#%E5%9F%BA%E6%9C%AC%E4%BF%A1%E6%81%AF) | moonshot-v1-8k、moonshot-v1-32k、moonshot-v1-128k | ```pip install openai```                    |
| chatgpt    | OpenAI   | [链接](https://platform.openai.com/docs/introduction)        | gpt4、gpt3.5                                      | ```pip install openai```                    |



### 大模型部署推理

- [千亿级开源大模型Qwen1.5-110B-Chat部署实测](https://zhuanlan.zhihu.com/p/696929885)
- [目前有什么可以本地部署的大模型推荐?](https://www.zhihu.com/question/648879790/answer/3504152602)
- [为什么vllm消耗显存那么大？](#为什么vllm消耗显存那么大？)
- [大模型本地部署这么麻烦，为什么不直接调用API？](https://www.zhihu.com/question/653448544/answer/3512063454)
- vllm
- 8bit量化、4bit量化技术原理介绍

## 大模型原理介绍

### Transformer原理介绍

- [一文讲明白初学者怎么入门大语言模型（LLM）？](https://www.zhihu.com/question/644285055/answer/3455086230)
- [从矩阵运算角度理解反向传播](https://www.zhihu.com/question/663495727/answer/3613784579)
- 图解Transformer中的Attention机制

### 从零实现llama3

- llama3整体架构图介绍
- llama3原始权重与HuggingFace权重的区别
- llama3归一化方法RMSNorm实现
- llama3分组查询注意力（Grouped Query Attention，GQA）实现
- llama3 掩码注意力机制（Masked Grouped Query Attention）实现
- llama3前馈网络SwiGLU实现
- llama3整体推理实现



## 大模型训练

### 模型训练基础知识

- [一文带你了解预训练、指令微调和人类反馈强化学习](https://zhuanlan.zhihu.com/p/633202668)
- [初学者如何快速入门大模型微调](https://www.zhihu.com/question/638803488/answer/3521367223)
- [介绍部分微调中的Prompt-Tuning](https://www.zhihu.com/question/646632163/answer/3584882298)
- [从原理到实战讲明白大模型微调方法LoRA](https://zhuanlan.zhihu.com/p/714762638)
- 如何从零开始训练一个llm模型？

### LoRA微调

| 项目                            | 教程 | 代码                         |
| ------------------------------- | ---- | ---------------------------- |
| 不依赖微调框架，从0实现LoRA微调 |      | [配套代码](./llm-train/lora) |



### 实战-基于LLaMAFactory微调

- [只需三个脚本，单机单卡微调BaiChuan2-13B并发布服务](https://zhuanlan.zhihu.com/p/696631776) 代码：[配套代码](./llm-train/baichuan13B)

- 只需三个脚本，单机多卡微调BaiChuan2-13B并发布服务

- 只需三个脚本，多机多卡微调BaiChuan2-13B并发布服务

- 只需三个脚本，使用vllm部署BaiChuan2-13B

### 实战-大模型做情感预测

| 项目                   | 微调方式 | 教程                                                         | 视频教程                                                | 相关依赖                        |
| ---------------------- | -------- | ------------------------------------------------------------ | ------------------------------------------------------- | ------------------------------- |
| 微调大模型实现情感预测 | Lora     | [我用LLaMA-Factory微调大模型来实现商品评论情感分析，准确率高达91.70%](https://zhuanlan.zhihu.com/p/699510751) | [视频链接](https://www.bilibili.com/video/BV1siuietEYX) | [配套代码](./llm-train/comment) |




## 检索增强生成


RAG整体技术路线可分为3大块8个小点见下图，其中包含知识库构建、知识检索和知识问答。其中核心在于**知识库构建**

![rag-技术路线](assets/rag-%E6%8A%80%E6%9C%AF%E8%B7%AF%E7%BA%BF.png)

详细介绍见：

- [RAG原理介绍](https://mp.weixin.qq.com/s/zlkYMkBgz4MuRW5dmOP73g)



### ragflow

- 常规rag存在的问题：

  **一是**如何应对复杂多变的数据，这些数据包含各种格式，更复杂的还包含各类图表、pdf、excel循环嵌套等。如果在没有理解这些数据的基础之上直接简单粗暴地做RAG ，就会导致知识检索失败，从而导致rag失败。

  **二是**如何查询和排序。假设知识库中有10W条数据，你的问题需要和10W数据匹配检索并且找到最适合的几条，无疑于大海捞针。



- ragflow是如何改善这些问题的？

  **一是**基于深度文档理解**deepdoc模块**，能够从各类复杂格式的非结构化数据中提取真知灼见。

  **二是**引入**多路召回**和**重排序**，才能保证数据检索召回的准确度

项目地址：[ragflow](https://github.com/infiniflow/ragflow)

**[⬆ 一键返回目录](#目录)**



### 实战-基于ragflow做一款初中历史辅导工具

| 向量数据库                                                | 数据处理                                                     | 语义召回             | 教程                                                         | 视频地址                                     |
| --------------------------------------------------------- | ------------------------------------------------------------ | -------------------- | ------------------------------------------------------------ | -------------------------------------------- |
| [Elasticsearch](https://github.com/elastic/elasticsearch) | [deepdoc模块](https://github.com/infiniflow/ragflow/blob/main/deepdoc/README_zh.md) | 多路召回、融合重排序 | [我用ragflow做了一款初中历史辅导助手](https://zhuanlan.zhihu.com/p/694358392) | https://www.bilibili.com/video/BV1yw4m1y7yA/ |

**[⬆ 一键返回目录](#目录)**

### 实战-手写一个最简单的RAG

github上的代码封装程度高，不利于小白学习入门。

常规的大模型RAG框架有langchain等，但是langchain等框架源码理解困难，debug源码上手难度大。

因此，我写了一个人人都能看懂、人人都能修改的大模型RAG框架代码。

整体项目结构如下图所示：手把手教你大模型RAG框架架构。

![手把手教你大模型RAG框架架构](assets/%E6%89%8B%E6%8A%8A%E6%89%8B%E6%95%99%E4%BD%A0%E5%A4%A7%E6%A8%A1%E5%9E%8BRAG%E6%A1%86%E6%9E%B6%E6%9E%B6%E6%9E%84%20.jpg)



代码与教程如下：

|                 章节                  |                             教程                             | 代码                            |
| :-----------------------------------: | :----------------------------------------------------------: | ------------------------------- |
|         01.如何调用大模型API          | [手把手教你完成大模型RAG知识问答应用构建-01.如何调用大模型API](https://zhuanlan.zhihu.com/p/687087842) | [配套代码](./llm-rag) |
|              02.RAG介绍               | [手把手教你完成大模型RAG知识问答应用构建-02.RAG介绍](https://zhuanlan.zhihu.com/p/687216989) | / |
|            03.部署环境准备            | [手把手教你完成大模型RAG知识问答应用构建-03.项目依赖环境准备](https://zhuanlan.zhihu.com/p/690248249) | / |
|             04.知识库构建             | [手把手教你完成大模型RAG知识问答应用构建-04.知识库构建](https://zhuanlan.zhihu.com/p/694699663) | / |
|       05.基于知识库的大模型问答       | [手把手教你完成大模型RAG知识问答应用构建-05.基于知识库的大模型问答](https://zhuanlan.zhihu.com/p/695336978) | [配套代码](./llm-rag/tutorial/05.基于知识库的大模型问答) |
|     06.改进-用自己的embedding模型     | [手把手教你完成大模型RAG知识问答应用构建-06.用自己的embedding模型](https://zhuanlan.zhihu.com/p/696868834) | [配套代码](./llm-rag/tutorial/06.改进-用自己的embedding模型) |
|        07.封装镜像对外提供服务        |                            更新中                            | 更新中 |
| 08.改进-基于Faiss的大模型知识索引构建 |                            更新中                            | [配套代码](./llm-rag/tutorial/08.改进-基于Faiss的大模型知识索引构建) |
|        09.改进-使用向量数据库         |                            更新中                            | [配套代码](./llm-rag/tutorial/09.改进-使用Milvus向量数据库) |
|              10.前端构建              |                            更新中                            | 更新中                          |

**[⬆ 一键返回目录](#目录)**





## 向量数据库

### 向量数据库原理介绍



### 实战-自己手写一个最简单的向量数据





## Agent


### Agent原理介绍



Agent的构成要素包括LLM（Language Model），记忆（Memory），规划技能（Planning skills），工具使用能力（Tool use），使用这些不同的环节，完成构建AGI。

**Agent = LLM+Planning+Feedback+Tool use**


如下为AI Agent云服务商E2B整理的目前市面上不同领域里知名的 AI Agent 项目，共计81个开源+58个闭源Agent项目

![landscape-latest](assets/landscape-latest.png)



Agent相关文章：

- [什么是 AI 智能体，和大模型有什么关系？](https://www.zhihu.com/question/663495727/answer/3613784579)
- 



### 自己手写一个最简单的Agent

论文：[ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)





## AI图像生成

## AI语音合成

## AI音乐合成

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=GuoCoder/ai-app&type=Date)](https://star-history.com/#GuoCoder/ai-app&Date)




## AI技术应用交流群

<img src="assets/image-20240430221857315.png" alt="image-20240430221857315" style="zoom: 33%;" />

图片挂掉，可加微信:Code-GUO

## 微信公众号

<img src="assets/程序锅锅公众号-1714486122128.jpg" alt="程序锅锅公众号" style="zoom: 67%;" />

图片挂掉，可加微信:Code-GUO

## 免责声明

如有疑问请提交**issue**，有**违规侵权**，请联系本人 **[coderguo@foxmail.com](coderguo@foxmail.com)** ，本人立马删除相应链接，感谢！

本仓库仅作学习交流分享使用，任何子环节不作任何商用。