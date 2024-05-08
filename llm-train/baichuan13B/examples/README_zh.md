我们提供了多样化的大模型微调示例脚本。

```
│  README_zh.md
│  run_baichuan13B_merge_lora.sh  #用于合并lora权重
│  run_baichuan13B_sft_lora.sh    #用于基于baichuan13B通过lora微调
└─inference # 服务构建
        api_demo.sh  # API推理服务构建
        cli_demo.sh  # 交互式推理服务构建
        vllm_demo.sh # vllm推理服务构建
        web_demo.sh  # web推理服务构建
```
