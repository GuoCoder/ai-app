#!/bin/bash

CUDA_VISIBLE_DEVICES=2 python ../../src/cli_demo.py \
    --model_name_or_path /home/test/models/baichuan-inc/Baichuan2-13B-Chat \
    --adapter_name_or_path ../../saves/Baichuan2-13B-Chat/lora/train_2024-04-30-13-10-46 \
    --template baichuan2 \
    --finetuning_type lora
