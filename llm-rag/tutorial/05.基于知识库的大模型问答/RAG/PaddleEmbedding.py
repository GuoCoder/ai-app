from typing import List

from paddlenlp import Taskflow

from RAG.Embeddings import BaseEmbeddings


class PaddleEmbedding(BaseEmbeddings):
    def __init__(
            self,
            model:str="rocketqa-zh-base-query-encoder",
            batch_size:int =1,
            **kwargs

    ) -> None:
        self.client = Taskflow("feature_extraction",model=model ,batch_size = batch_size,return_tensors='np',**kwargs)

    def get_embedding(self, text: str)  -> List[float]:
        text_embeds = self.client([text])
        result = text_embeds["features"]
        data = result[0]
        return data.tolist()

    def get_embeddings(self, text: List[str])  -> List[List[float]]:
        text_embeds = self.client(text)
        result = text_embeds["features"]
        data = result
        return data.tolist()

