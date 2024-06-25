import configparser
import json
import os
import time
import random
from typing import List

import numpy as np
from datasets import tqdm
from pymilvus import connections, utility
from pymilvus import Collection, DataType, FieldSchema, CollectionSchema

from RAG.Embeddings import BaseEmbeddings
from RAG.PaddleEmbedding import PaddleEmbedding
from RAG.VectorBase import VectorStore

class ZillizVectorStore(VectorStore):

    ## document 为分段后的文本,用List保存

    def __init__(self, document: List[str] = ['']) -> None:
        cfp =  configparser.RawConfigParser()
        self.cfp = cfp.read('config.ini')
        self.milvus_uri = cfp.get('example', 'uri')
        self.user = cfp.get('example', 'user')
        self.password = cfp.get('example', 'password')
        self.collection_name =  cfp.get('example', 'collection_name')
        self.dim = int(cfp.get('example', 'dim'))
        self.connections = connections.connect("default",
                            uri=self.milvus_uri,
                            user=self.user,
                            password=self.password)
        # # Please check your connection guide in Zilliz Cloud console, if the cluster provides a token, you can use it to authenticate your cluster
        # # token based cluster
        # token = cfp.get('example', 'token')
        # connections.connect("default",
        #                     uri=milvus_uri,
        #                     token=token)
        print(f"Connecting to DB: {self.milvus_uri}")
        self.document = document
        self.entities = []
        self.create_collection()

    def drop_collection(self):
        utility.drop_collection(self.collection_name)

    def create_collection(self):
        check_collection = utility.has_collection(self.collection_name)

        book_id_field = FieldSchema(name="history_id", dtype=DataType.INT64, is_primary=True,
                                    description="customized primary id")
        word_count_field = FieldSchema(name="hitory_content", dtype=DataType.VARCHAR, max_length=8196)
        book_intro_field = FieldSchema(name="history_intro", dtype=DataType.FLOAT_VECTOR, dim=self.dim)
        schema = CollectionSchema(fields=[book_id_field, word_count_field, book_intro_field],
                                  auto_id=False,
                                  description="my first collection")
        self.collection = Collection(name=self.collection_name, schema=schema)

    def get_vector(self, EmbeddingModel: BaseEmbeddings) -> List[List[float]]:
        self.vectors = []
        for doc in tqdm(self.document, desc="Calculating embeddings"):
            self.vectors.append(EmbeddingModel.get_embedding(doc))
        return self.vectors

    def batch_split_list(self, lst, batch_size):
        return [lst[i:i + batch_size] for i in range(0, len(lst), batch_size)]

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

    def prepare_entity(self):
        nb = len(self.vectors)
        book_ids = [i for i in range(0, nb)]
        word_contents = self.document
        entities = [book_ids, word_contents, self.vectors]
        self.entities = entities

    def insert(self):
        t0 = time.time()
        start = 0
        nb = 1000
        nrounds = int(len(self.vectors)/nb)+1
        if(self.entities):
            for i in range(nrounds):
                temp = [self.entities[0][start:start+nb],self.entities[1][start:start+nb],self.entities[2][start:start+nb]]
                ins_resp = self.collection.insert(temp)
                start += nb
                print(f"Round stage {i} insert success!")
            ins_rt = time.time() - t0
            print(f"Succeed insert {len(self.entities)} data in {round(ins_rt, 4)} seconds!")
        else:
            raise RuntimeError

    def flush(self):
                # flush
        print("Flushing...")
        start_flush = time.time()
        self.collection.flush()
        end_flush = time.time()
        print(f"Succeed in {round(end_flush - start_flush, 4)} seconds!")
        # build index
        index_params = {"index_type": "AUTOINDEX", "metric_type": "L2", "params": {}}
        t0 = time.time()
        print("Building AutoIndex...")
        self.collection.create_index(field_name="history_intro", index_params=index_params)
        t1 = time.time()
        print(f"Succeed in {round(t1 - t0, 4)} seconds!")

        # load collection
        t0 = time.time()
        print("Loading collection...")
        self.collection.load()
        t1 = time.time()
        print(f"Succeed in {round(t1 - t0, 4)} seconds!")

    def get_similarity(self, vector1: List[float], vector2: List[float]) -> float:
        return BaseEmbeddings.cosine_similarity(vector1, vector2)

    def query(self, query: str, EmbeddingModel: BaseEmbeddings, k: int = 1) -> List[str]:
        search_params = {"metric_type": "L2"}
        topk = k
        search_vec = [EmbeddingModel.get_embedding(query)]
        print(f"Searching vector: {search_vec}")
        t0 = time.time()
        results = self.collection.search(search_vec,
                                    anns_field="history_intro",
                                    param=search_params,
                                    limit=topk,
                                    guarantee_timestamp=1)
        t1 = time.time()
        print(f"Result:{results}")

        print(f"ZillizVectorStore search 耗时: {round(t1 - t0, 4)} seconds!")
        return np.array(self.document)[results[0].ids].tolist()



if __name__ == '__main__':
    # connect to milvus
    storage = "../../storage/history_24"
    # zillizVectorStore = ZillizVectorStore()
    # zillizVectorStore.load_vector(storage)
    # zillizVectorStore.query(EmbeddingModel = PaddleEmbedding(),query = "秦始皇的妻子和嫪毐有什么关系？",k = 3)
    # zillizVectorStore.load_vector(storage)
    # zillizVectorStore.prepare_entity()
    # zillizVectorStore.insert()
    # zillizVectorStore.flush()

