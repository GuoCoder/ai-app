# -*- coding: utf-8 -*-  
import os
import sys
from typing import List

from pydantic import BaseModel

from RAG.PaddleEmbedding import PaddleEmbedding

base_dir = os.path.dirname(__file__)
sys.path.append(base_dir) 
from fastapi import APIRouter

router = APIRouter()
API_SUMMARY = 'API'
# -------------------- Business --------------------
from loguru import logger

AVAIL_MODELS = ["PaddlePaddle/ernie_vil-2.0-base-zh","rocketqa-zh-base-query-encoder","rocketqa-zh-dureader-query-encoder"]


class Parameters(BaseModel):
    input: List[str]
    model: str

@router.get("/v1/models")
async def v1_models():
    output =    {
            "object": "list",
            "data": [
                {
                    "model_name": "PaddlePaddle/ernie_vil-2.0-base-zh",
                    "embedding_dim": 768,
                    "describle": "",
                },
                {
                    "model_name": "rocketqa-zh-base-query-encoder",
                    "embedding_dim": 768,
                    "describle": "",
                },
                {
                    "model_name": "rocketqa-zh-dureader-query-encoder",
                    "embedding_dim": 768,
                    "describle": "",
                }
            ]
        }
    return output


@router.post("/v1/embeddings")
async def v1_completions(param: Parameters) -> List[List[float]]:
    if param.model in AVAIL_MODELS:
        return PaddleEmbedding(model=param.model).get_embeddings(param.input)
    else:
        from response import fail
        return fail()


