#!/bin/bash
# DO NOT use quantized model or quantization_bit when merging lora weights

CUDA_VISIBLE_DEVICES=2 python ../../src/export_model.py \
    --model_name_or_path ~/models/baichuan-inc/Baichuan2-13B-Chat \
    --adapter_name_or_path saves/Baichuan2-13B-Chat/lora/train_2024-04-30-13-10-46 \
    --template baichuan2 \
    --finetuning_type lora \
    --export_dir ../../models/Baichuan2-13B-Chat-sft-0430 \
    --export_size 2 \
    --export_device cuda \
    --export_legacy_format False
