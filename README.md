<img src="./assets\sologan.png" alt="sologan"  />


<p> 
<a href="https://github.com//llm-action/blob/main/pic/wx.jpg"> <img src="https://img.shields.io/badge/程序锅锅-1AAD19.svg?style=plastic&logo=wechat&logoColor=white" > </a>
<a href="https://www.zhihu.com/people/echo-liu-32"> <img src="https://img.shields.io/badge/程序锅-0079FF.svg?style=plastic&logo=zhihu&logoColor=white"> </a>
<a href="https://blog.csdn.net/qq_35054222"> <img src="https://img.shields.io/badge/CSDN-程序锅锅-FC5531.svg""> </a>
</p> 
**持续更新中ing，点star不迷路** 。


## 目录

- 🔥 [服务器基础环境安装及常用工具](#服务器基础环境安装及常用工具) 
  - 🐫[PyCharm安装](#pycharm安装)
  - 🐼[Anaconda安装及原理介绍](#Anaconda安装)
  - 🐰[关于SSH那些事](#关于ssh那些事)
  - 💪[实战：用VSCode远程服务器开发](https://zhuanlan.zhihu.com/p/693420628)
- 🐎 [大模型介绍](#大模型训练)
  - 🐎[主流大模型API调用总结](#主流大模型API调用总结)
  - 🍚[大模型本地部署技术](#大模型本地部署)
- 🍄[检索增强生成（RAG）](#检索增强生成（RAG）)
  - 🌼 [ragflow](#ragflow)
  - 🌴 [QAnything](#QAnything)
  - 🐫 [LLamaIndex](#LLamaIndex)
  - 🌼 [FastGPT](#FastGPT)
  - 💪 [实战：自己手写一个最简单的RAG](#实战-手写一个最简单的RAG)
  - 💪 [实战：基于ragflow做了款初中历史辅导工具](#实战：基于ragflow做一款初中历史辅导工具)
- 🎪[向量数据库技术](#向量数据库)
  - 🐮 [Faiss](#Faiss)
  - 🌲 [Milvus](#Milvus)
  - 🌞 [Elasticsearch](#Elasticsearch)
  - 💪 [实战-自己手写一个最简单的向量数据库](#实战-自己手写一个最简单的向量数据库)
- 🚅 [大模型训练](#大模型训练)
  - ❄️[预训练（PT）](#预训练)
  - ⛄️[指令微调（SFT）](#指令微调)
  - ✈️[基于人工反馈的强化学习（RLHF）](#基于人工反馈的强化学习)
  - 🚀 [大模型训练神器LLaMAFactory](#LLaMAFactory大模型训练)
  - 💪 [实战-基于LLaMA Factory微调数百种大模型](#实战-基于LLaMA Factory微调)
- 🚀 [大模型Agent框架](#Agent)
  - 🏠 [langchain](#langchain)
  - 🗼 [AutoGPT](#AutoGPT)
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

PyCharm是一种Python IDE（集成开发环境），相比标准python，它的开发效率要更高，同时引入第三方库也更加容易。

这里可以理解为我用记事本也可以写python代码，不过用pycharm去写python代码比较方便。

Pycharm最常用的版本有**社区版（community）**和 **专业版(professional)**, 其中专业版是需要收费的，相比于社区版，其增加了远程开发等功能。

详细介绍如下：

[最新版pycharm专业版（2023.3.4）环境安装以及永久使用方法](https://zhuanlan.zhihu.com/p/689191237)

### Anaconda

Anaconda是Python依赖管理工具，支持Linux,Mac,Windows系统，提供了包管理与环境管理的功能，可以很方便地解决多版本python并存、切换以及各种第三方包安装问题。

Anaconda解决了官方Python的两大痛点。

一是提供了包管理功能，不再需要人为管理众多的python依赖；

二是提供环境管理的功能，解决了多版本Python并存、切换的问题。比如我现在有两个项目，分别用到了python2.7和python3.10，用官方python执行器，由于环境变量混乱，很容易造成不知名的BUG。

详细介绍如下：

[Anaconda安装与原理介绍](https://mp.weixin.qq.com/s?__biz=MzkwNzY3ODU5MA==&mid=2247483956&idx=1&sn=efdb4783a00cb10349f80ab2f818dbcf&chksm=c1defe6805c5fc674158167fec0cde2a6152137cfa3e0f0b836414b4314cb03ea013b75511bc&scene=126&sessionid=1714101698#rd)





## 大模型训练

### 预训练



- [OpenAI首次揭秘GPT训练细节](https://zhuanlan.zhihu.com/p/633202668)

### 指令微调



- [OpenAI首次揭秘GPT训练细节](https://zhuanlan.zhihu.com/p/633202668)



### 基于人工反馈的强化学习

- [OpenAI首次揭秘GPT训练细节](https://zhuanlan.zhihu.com/p/633202668)





### LLaMAFactory大模型训练

 - LLaMAFactory能干啥？

   用一种极简方式支持数百种大模型训练

- 为什么要用LLaMAFactory?

  比如对chatglm3微调，不再需要去chatglm3官网查看微调代码。在LLaMAFactory中，更换一个参数直接搞定。

- 如何使用？
  项目地址：[LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory/blob/main/README_zh.md)

  


### 实战-基于LLaMA Factory微调

- 只需两个脚本，单机单卡微调BaiChuan2-13B并发布服务

- 只需两个脚本，单机多卡微调BaiChuan2-13B并发布服务

- 只需两个脚本，多机多卡微调BaiChuan2-13B并发布服务

- 只需两个脚本，使用vllm部署BaiChuan2-13B

- 使用Ollama

  



## 检索增强生成（RAG）

- 为什么要用检索增强生成？

  大模型（LLM）会产生误导性的 “幻觉”，训练数据会过时，处理特定知识时效率不高，缺乏专业领域的深度洞察，同时在推理能力上也有所欠缺。

  正是在这样的背景下，检索增强生成技术（Retrieval-Augmented Generation,RAG）应时而生，成为大模型时代的一大趋势。

- 检索增强生成是什么？

  RAG通过在语言模型生成答案之前，先从广泛的专业文档数据库中检索相关信息，然后利用这些专业信息来引导大模型生成的结果，极大地提升了内容的准确性和相关性。

  RAG有效地缓解了幻觉问题，提高了知识更新的速度（大模型+搜索引擎），并增强了内容生成的可追溯性，使得大型语言模型在实际应用中变得更加实用和可信。

  

RAG整体技术路线可分为3大块8个小点见下图，其中包含知识库构建、知识检索和知识问答。其中核心在于**知识库构建**

![rag-技术路线](assets/rag-%E6%8A%80%E6%9C%AF%E8%B7%AF%E7%BA%BF.png)

详细介绍见：

[自己手写了一个大模型RAG项目-02.RAG原理介绍](https://mp.weixin.qq.com/s/zlkYMkBgz4MuRW5dmOP73g)



### ragflow

- 常规rag存在的问题：

  **一是**如何应对复杂多变的数据，这些数据包含各种格式，更复杂的还包含各类图表、pdf、excel循环嵌套等。如果在没有理解这些数据的基础之上直接简单粗暴地做RAG ，就会导致知识检索失败，从而导致rag失败。

  **二是**如何查询和排序。假设知识库中有10W条数据，你的问题需要和10W数据匹配检索并且找到最适合的几条，无疑于大海捞针。



- ragflow是如何改善这些问题的？

  **一是**基于深度文档理解**deepdoc模块**，能够从各类复杂格式的非结构化数据中提取真知灼见。

  **二是**引入**多路召回**和**重排序**，才能保证数据检索召回的准确度

项目地址：[ragflow](https://github.com/infiniflow/ragflow)

**[⬆ 一键返回目录](#目录)**



### QAnything

与ragflow类似，也是解决常规rag的数据问题和检索问题。

不过整体效果不如ragflow

项目地址：[QAnything](https://github.com/netease-youdao/QAnything)

**[⬆ 一键返回目录](#目录)**



### 实战：基于ragflow做一款初中历史辅导工具

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
|         01.如何调用大模型API          | [手把手教你完成大模型RAG知识问答应用构建-01.如何调用大模型API](https://zhuanlan.zhihu.com/p/687087842) | [配套代码](./llm-rag/README.md) |
|              02.RAG介绍               | [手把手教你完成大模型RAG知识问答应用构建-02.RAG介绍](https://zhuanlan.zhihu.com/p/687216989) | [配套代码](./llm-rag/README.md) |
|            03.部署环境准备            | [手把手教你完成大模型RAG知识问答应用构建-03.项目依赖环境准备](https://zhuanlan.zhihu.com/p/690248249) | [配套代码](./llm-rag/README.md) |
|             04.知识库构建             | [手把手教你完成大模型RAG知识问答应用构建-04.知识库构建](https://zhuanlan.zhihu.com/p/694699663) | [配套代码](./llm-rag/README.md) |
|       05.基于知识库的大模型问答       | [手把手教你完成大模型RAG知识问答应用构建-05.基于知识库的大模型问答](https://zhuanlan.zhihu.com/p/695336978) | [配套代码](./llm-rag/README.md) |
|     06.改进-用自己的embedding模型     |                            更新中                            | [配套代码](./llm-rag/README.md) |
|        07.封装镜像对外提供服务        |                            更新中                            | [配套代码](./llm-rag/README.md) |
| 08.改进-基于Faiss的大模型知识索引构建 |                            更新中                            | [配套代码](./llm-rag/README.md) |
|        09.改进-使用向量数据库         |                            更新中                            | [配套代码](./llm-rag/README.md) |
|              10.前端构建              |                            更新中                            | 更新中                          |

**[⬆ 一键返回目录](#目录)**






## 向量数据库


## Agent
Agent的构成要素包括LLM（Language Model），记忆（Memory），规划技能（Planning skills），工具使用能力（Tool use），使用这些不同的环节，完成构建AGI。

**Agent = LLM+Planning+Feedback+Tool use**


如下为AI Agent云服务商E2B整理的目前市面上不同领域里知名的 AI Agent 项目，共计81个开源+58个闭源Agent项目

![landscape-latest](assets/landscape-latest.png)



### 自己手写一个最简单的Agent

论文：[ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)





## AI图像生成

## AI语音合成

## AI音乐合成

## AI技术应用交流群

<img src="C:\Users\LiuJing\Desktop\ai-app\assets\guo.jpg" alt="guo" style="zoom: 25%;" />

图片挂掉，可加微信:Code-GUO

## 微信公众号

![程序锅锅公众号](C:\Users\LiuJing\Desktop\ai-app\assets\程序锅锅公众号-1714486122128.jpg)

图片挂掉，可加微信:Code-GUO

## 免责声明

如有疑问请提交**issue**，有**违规侵权**，请联系本人 **[coderguo@foxmail.com](coderguo@foxmail.com)** ，本人立马删除相应链接，感谢！

本仓库仅作学习交流分享使用，任何子环节不作任何商用。