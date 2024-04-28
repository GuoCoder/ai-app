



## 1.环境准备


```bash
git clone https://github.com/hiyouga/LLaMA-Factory.git
conda create -n llama_factory python=3.10
conda activate llama_factory
cd LLaMA-Factory
pip install -e .[metrics]
```


## 2.百川13B下载

```
#模型下载
from modelscope import snapshot_download
model_dir = snapshot_download('baichuan-inc/Baichuan2-13B-Chat')
```

默认模型会下载到```~/.cache/modelscope/hub```中，如果需要修改下载目录，可以手动指定环境变量：```MODELSCOPE_CACHE```，modelscope会将模型和数据集下载到该环境变量指定的目录中

更改默认位置：
```
 export MODELSCOPE_CACHE=./models
```

下载完成目录结构：
```
./models/
├── ast_indexer
├── baichuan-inc
│   └── Baichuan2-13B-Chat
│       ├── config.json
│       ├── configuration_baichuan.py
│       ├── configuration.json
│       ├── generation_config.json
│       ├── generation_utils.py
│       ├── model-00001-of-00006.safetensors
│       ├── model-00002-of-00006.safetensors
│       ├── model-00003-of-00006.safetensors
│       ├── model-00004-of-00006.safetensors
│       ├── model-00005-of-00006.safetensors
│       ├── model-00006-of-00006.safetensors
│       ├── modeling_baichuan.py
│       ├── model.safetensors.index.json
│       ├── ms_wrapper.py
│       ├── quantizer.py
│       ├── README.md
│       ├── special_tokens_map.json
│       ├── tokenization_baichuan.py
│       ├── tokenizer_config.json
│       └── tokenizer.model
└── temp
```



 ## 3.训练



### 可视化页面训练

```python
export CUDA_VISIBLE_DEVICES=0 # Windows 使用 `set CUDA_VISIBLE_DEVICES=0`
export GRADIO_SERVER_PORT=10099 # Windows 使用 `set GRADIO_SERVER_PORT=7860`
python src/train_web.py # 或 python -m llmtuner.webui.interface
```
截图如下：

![可视化页面训练截图](assets/%E5%8F%AF%E8%A7%86%E5%8C%96%E9%A1%B5%E9%9D%A2%E8%AE%AD%E7%BB%83%E6%88%AA%E5%9B%BE.png)



### 命令行训练

