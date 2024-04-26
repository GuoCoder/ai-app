from typing import List

from paddlenlp import Taskflow

from RAG.Embeddings import BaseEmbeddings


class PostEmbedding(BaseEmbeddings):
    def __init__(
            self,model:str
    ) -> None:
        self.client = Taskflow("feature_extraction",model=model ,return_tensors='np')

    def get_embedding(self, text: str,model:str = "rocketqa-zh-base-query-encoder")  -> List[float]:
        text_embeds = self.client([text])
        result = text_embeds["features"]
        data = result[0]
        return data.tolist()

    def get_embeddings(self, text: List[str],model:str)  -> List[List[float]]:

        text_embeds = self.client(text)
        result = text_embeds["features"]
        data = result
        return data.tolist()

