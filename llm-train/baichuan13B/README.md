我们提供了多样化的大模型微调示例脚本。

1.examples文件夹

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

2.src文件夹

提供了训练微调核心代码



以上代码运行，请务必下载和安装好[LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory)，如安装环境有问题，可联系我要代码conda env环境。