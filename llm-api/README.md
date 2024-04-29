### 可用训练数据整理


| 数据集                                                       | 介绍                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [firefly-train-1.1M](https://huggingface.co/datasets/YeungNLP/firefly-train-1.1M) | 包含了23种常见的中文NLP任务的数据，并且构造了许多与中华文化相关的数据，如对联、作诗、文言文翻译、散文、金庸小说等。对于每个任务，由人工书写若干种指令模板，保证数据的高质量与丰富度，数据量为115万。 |
| [shareAI/CodeChat](https://huggingface.co/datasets/shareAI/CodeChat) | 主要包含逻辑推理、代码问答、代码生成相关语料样本。           |
| [shareAI/ShareGPT-Chinese-English-90k](https://huggingface.co/datasets/shareAI/ShareGPT-Chinese-English-90k) | 中英文平行双语优质人机问答数据集，覆盖真实复杂场景下的用户提问。（包含大量多轮对话） |
| [ruozhiba](https://huggingface.co/datasets/LooksJuicy/ruozhiba) | 弱智吧数据问答，据说比较锻炼模型的心智能力。                 |
| [DPO-EN-ZH-20k](https://huggingface.co/datasets/hiyouga/DPO-En-Zh-20k) | 包含大量偏好对齐的问答对数据<好，差>，有助于进一步提升chat模型的对话质量，使其生成内容更加详细、适合人类偏好。 |
| [glaive-function-calling-v2-sharegpt](https://huggingface.co/datasets/hiyouga/glaive-function-calling-v2-sharegpt) | 包含大量工具函数选择、调用和具体参数数据，有助于提升模型的自主工具选择与使用能力。 |
| [Agent-FLAN](https://huggingface.co/datasets/internlm/Agent-FLAN) | (纯英文)类型同上， 包含大量工具使用数据，有助于提升模型的工具使用能力。 |
| [Agent-Instruct](https://huggingface.co/datasets/THUDM/AgentInstruct) | (纯英文)类型同上， 包含大量agent演示数据，有助于提升模型的工具使用、模拟能力。 |
| [CogVLM-sft-311K](https://huggingface.co/datasets/THUDM/CogVLM-SFT-311K) | (中文) 包含带图片问答数据，可以训练模型看图问答、看图生成代码能力。 |
| [ShareGPT4-V ](https://huggingface.co/datasets/Lin-Chen/ShareGPT4V) | (英文) 类型同上，包含带图片问答数据，可以训练模型看图问答、看图生成代码能力。 |
| [web-QA](https://huggingface.co/datasets/THUDM/webglm-qa)    | (纯英文) 包含大量（网页文章 -> 问题 -> 答案)数据，可以提升模型在RAG、文档问答、网页问答等垂直场景表现能力。欢迎翻译成中文进行开源 |
| [Humaneval-x](https://huggingface.co/datasets/THUDM/humaneval-x) | (纯英文) 包含cpp、java、go、js等代码的测试数据，可以评测模型生成代码能力。 |
| [longBench](https://huggingface.co/datasets/THUDM/LongBench) | (中、英文) 包含长样本问答数据，可以评测模型在输入内容比较长时候的任务能力。（长上下文） |
| [Llama3 中文化数据集](https://modelscope.cn/datasets/baicai003/Llama3-Chinese-dataset/summary) | 该数据集已统一处理为firefly格式，可以配合firefly工具直接训练llama3中文模型。 |







欢迎提issue补充，要求中文且一问一答形式，适合用于提升llama3任务能力的数据集