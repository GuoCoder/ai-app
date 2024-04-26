#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import time
from typing import Dict, List, Optional, Tuple, Union
import json
from RAG.Embeddings import BaseEmbeddings, OpenAIEmbedding, JinaEmbedding, ZhipuEmbedding
import numpy as np
from tqdm import tqdm


class VectorStore():
    def __init__(self, document: List[str] = ['']) -> None:
        self.document = document

    def get_vector(self, EmbeddingModel: BaseEmbeddings) -> List[List[float]]:
        
        self.vectors = []
        for doc in tqdm(self.document, desc="Calculating embeddings"):
            self.vectors.append(EmbeddingModel.get_embedding(doc))
        return self.vectors

    def batch_split_list(self, lst,batch_size):
        return [lst[i:i + batch_size] for i in range(0, len(lst), batch_size)]

    def get_vector_batch(self, EmbeddingModel: BaseEmbeddings, batch:int) -> List[List[float]]:

        self.vectors = []
        self.document = self.batch_split_list(self.document, batch)
        for doc in tqdm(self.document, desc="Calculating embeddings"):
            self.vectors.extend(EmbeddingModel.get_embeddings(doc))
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

    def query(self, query: str, EmbeddingModel: BaseEmbeddings, k: int = 1) -> List[str]:
        query_vector = EmbeddingModel.get_embedding(query)

        end_time = time.time()

        result = np.array([self.get_similarity(query_vector, vector)
                          for vector in self.vectors])
        print(' 检索 cost %f second' % (time.time() - end_time))
        return np.array(self.document)[result.argsort()[-k:][::-1]].tolist()
