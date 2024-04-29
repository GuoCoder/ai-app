## LLM可用训练数据整理

其中：

- en表示英文数据
- zh表示中文数据

- SFT表示指令微调数据集

- 多模态SFT表示输入为图像和语言的多模态指令微调数据集

- RAG-SFT表示输入为question、references和answers的指令微调数据集




### SFT


| 训练类型    | 数据集                                                       |                             介绍                             |
| ----------- | ------------------------------------------------------------ | :----------------------------------------------------------: |
| SFT         | [firefly-train-1.1M](https://huggingface.co/datasets/YeungNLP/firefly-train-1.1M) | 包含了23种常见的中文NLP任务的数据，并且构造了许多与中华文化相关的数据，如对联、作诗、文言文翻译、散文、金庸小说等。对于每个任务，由人工书写若干种指令模板，保证数据的高质量与丰富度，数据量为115万。 |
| SFT         | [shareAI/CodeChat](https://huggingface.co/datasets/shareAI/CodeChat) |      主要包含逻辑推理、代码问答、代码生成相关语料样本。      |
| SFT         | [shareAI/ShareGPT-Chinese-English-90k](https://huggingface.co/datasets/shareAI/ShareGPT-Chinese-English-90k) | 中英文平行双语优质人机问答数据集，覆盖真实复杂场景下的用户提问。（包含大量多轮对话） |
| SFT         | [ruozhiba](https://huggingface.co/datasets/LooksJuicy/ruozhiba) |         弱智吧数据问答，据说比较锻炼模型的心智能力。         |
| SFT         | [DPO-EN-ZH-20k](https://huggingface.co/datasets/hiyouga/DPO-En-Zh-20k) | 包含大量偏好对齐的问答对数据<好，差>，有助于进一步提升chat模型的对话质量，使其生成内容更加详细、适合人类偏好。 |
| SFT         | [glaive-function-calling-v2-sharegpt](https://huggingface.co/datasets/hiyouga/glaive-function-calling-v2-sharegpt) | 包含大量工具函数选择、调用和具体参数数据，有助于提升模型的自主工具选择与使用能力。 |
| SFT         | [Agent-FLAN](https://huggingface.co/datasets/internlm/Agent-FLAN) | (纯英文)类型同上， 包含大量工具使用数据，有助于提升模型的工具使用能力。 |
| SFT         | [Agent-Instruct](https://huggingface.co/datasets/THUDM/AgentInstruct) | (纯英文)类型同上， 包含大量agent演示数据，有助于提升模型的工具使用、模拟能力。 |
| 多模态SFT   | [CogVLM-sft-311K](https://huggingface.co/datasets/THUDM/CogVLM-SFT-311K) | (中文) 包含带图片问答数据，可以训练模型看图问答、看图生成代码能力。 |
| 多模态SFT   | [ShareGPT4-V ](https://huggingface.co/datasets/Lin-Chen/ShareGPT4V) | (英文) 类型同上，包含带图片问答数据，可以训练模型看图问答、看图生成代码能力。 |
| RAG-    SFT | [web-QA](https://huggingface.co/datasets/THUDM/webglm-qa)    | (纯英文) 包含大量（网页文章 -> 问题 -> 答案)数据，可以提升模型在RAG、文档问答、网页问答等垂直场景表现能力。欢迎翻译成中文进行开源 |
| SFT         | [Humaneval-x](https://huggingface.co/datasets/THUDM/humaneval-x) | (纯英文) 包含cpp、java、go、js等代码的测试数据，可以评测模型生成代码能力。 |
| RAG-SFT     | [longBench](https://huggingface.co/datasets/THUDM/LongBench) | (中、英文) 包含长样本问答数据，可以评测模型在输入内容比较长时候的任务能力。（长上下文） |
| SFT         | [Llama3 中文化数据集](https://modelscope.cn/datasets/baicai003/Llama3-Chinese-dataset/summary) | 该数据集已统一处理为firefly格式，可以配合firefly工具直接训练llama3中文模型。 |
| SFT         | [Stanford Alpaca (en)](https://github.com/tatsu-lab/stanford_alpaca) | alpaca_data.json 包含我们用于微调 Alpaca 模型的 52K 指令跟踪数据 |
| SFT         | [Stanford Alpaca (zh)](https://github.com/ymcui/Chinese-LLaMA-Alpaca) | 中文Alpaca数据，包含51k个从ChatGPT (gpt-3.5-turbo)爬取的指令数据。 |
| SFT         | [Alpaca GPT4 (en&zh)](https://github.com/Instruction-Tuning-with-GPT-4/GPT-4-LLM) | 包含 GPT-4 生成的 52K 指令微调数据，并由 ChatGPT 翻译成中文。 |
| SFT         | [Alpaca-CoT(zh)](https://github.com/PhoebusSi/Alpaca-CoT/blob/main/CN_README.md) | Alpaca-CoT项目的存储库，该项目旨在构建一个多接口统一的轻量级指令微调（IFT）平台，该平台具有广泛的指令集合(尤其是CoT数据集) |
| SFT         | 持续更新。。。                                               |                              /                               |




### <details><summary>预训练数据集</summary>
| 训练类型 | 数据集名称                                                   | 介绍 |
| -------- | ------------------------------------------------------------ | ---- |
| 预训练   | [StarCoder (en)](https://huggingface.co/datasets/bigcode/starcoderdata) |      |
| 预训练   | [Wiki Demo (en)](data/wiki_demo.txt)                         |      |
| 预训练   | [RefinedWeb (en)](https://huggingface.co/datasets/tiiuae/falcon-refinedweb) |      |
| 预训练   | [RedPajama V2 (en)](https://huggingface.co/datasets/togethercomputer/RedPajama-Data-V2) |      |
| 预训练   | [Wikipedia (en)](https://huggingface.co/datasets/olm/olm-wikipedia-20221220) |      |
| 预训练   | [Wikipedia (zh)](https://huggingface.co/datasets/pleisto/wikipedia-cn-20230720-filtered) |      |
| 预训练   | [Pile (en)](https://huggingface.co/datasets/EleutherAI/pile) |      |
| 预训练   | [SkyPile (zh)](https://huggingface.co/datasets/Skywork/SkyPile-150B) |      |
| 预训练   | [The Stack (en)](https://huggingface.co/datasets/bigcode/the-stack) |      |

</details>



### <details><summary>偏好数据集</summary>

- [HH-RLHF (en)](https://huggingface.co/datasets/Anthropic/hh-rlhf)
- [Open Assistant (multilingual)](https://huggingface.co/datasets/OpenAssistant/oasst1)
- [GPT-4 Generated Data (en&zh)](https://github.com/Instruction-Tuning-with-GPT-4/GPT-4-LLM)
- [Orca DPO (en)](https://huggingface.co/datasets/Intel/orca_dpo_pairs)
- [Nectar (en)](https://huggingface.co/datasets/berkeley-nest/Nectar)
- [DPO mixed (en&zh)](https://huggingface.co/datasets/hiyouga/DPO-En-Zh-20k)
- [Orca DPO (de)](https://huggingface.co/datasets/mayflowergmbh/intel_orca_dpo_pairs_de)

</details>

