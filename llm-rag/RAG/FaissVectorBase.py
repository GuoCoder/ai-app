#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import time
from typing import Dict, List, Optional, Tuple, Union
import json

import faiss

from RAG.Embeddings import BaseEmbeddings, OpenAIEmbedding, JinaEmbedding, ZhipuEmbedding
import numpy as np
from tqdm import tqdm

from RAG.VectorBase import VectorStore


class FaissVectorStore(VectorStore):

    def __init__(self, document: List[str] = ['']) -> None:
        super().__init__(document)
        self.document = document

    def get_vector(self, EmbeddingModel: BaseEmbeddings) -> List[List[float]]:
        self.vectors = []
        for doc in tqdm(self.document, desc="Calculating embeddings"):
            self.vectors.append(EmbeddingModel.get_embedding(doc))
        return self.vectors

    def persist(self, path: str = 'storage'):
        if not os.path.exists(path):
            os.makedirs(path)
        with open(f"{path}/doecment.json", 'w', encoding='utf-8') as f:
            json.dump(self.document, f, ensure_ascii=False)
        if self.vectors:
            with open(f"{path}/vectors.json", 'w', encoding='utf-8') as f:
                json.dump(self.vectors, f)

    def load_vector(self, path: str = 'storage'):
        with open(f"{path}/vectors.json", 'r', encoding='utf-8') as f:
            self.vectors = json.load(f)
        with open(f"{path}/doecment.json", 'r', encoding='utf-8') as f:
            self.document = json.load(f)

    def get_similarity(self, vector1: List[float], vector2: List[float]) -> float:
        return BaseEmbeddings.cosine_similarity(vector1, vector2)

    def generateIndexFlatL2(self):
        dim, measure = 768, faiss.METRIC_L2
        param = 'Flat'
        vectors = np.array([vector for vector in self.vectors]).astype('float32')
        index = faiss.index_factory(dim, param, measure)
        index.add(vectors)  # 将向量库中的向量加入到index中
        return index


    def query(self, query: str, EmbeddingModel: BaseEmbeddings, k: int = 1) -> List[str]:

        start_time = time.time()
        index = self.generateIndexFlatL2()
        end_time = time.time()
        print(' 构建索引 cost %f second' % (end_time - start_time))
        query_vector = np.array([EmbeddingModel.get_embedding(query)]).astype("float32")

        end_time = time.time()
        D, I = index.search(query_vector, k)  # xq为待检索向量，返回的I为每个待检索query最相似TopK的索引list，D为其对应的距离
        print(' 检索 cost %f second' % (time.time() - end_time))
        return np.array(self.document)[I[0,:]].tolist()


