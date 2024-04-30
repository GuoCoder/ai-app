CUDA_VISIBLE_DEVICES=2,3 API_PORT=10099 python ../../src/api_demo.py \
    --model_name_or_path /home/test/LLaMA-Factory/models/Baichuan2-13B-Chat-sft-0430 \
    --template baichuan2 \
    --infer_backend vllm \
    --vllm_enforce_eager \
