from RAG.PaddleEmbedding import PaddleEmbedding
from RAG.VectorBase import VectorStore
from RAG.utils import ReadFiles

embedding_model = "rocketqa-zh-base-query-encoder"

docs = ReadFiles('../../data/history_24').get_content(min_token_len=1600,max_token_len=3200, cover_content=150) # 获得data目录下的所有文件内容并分割
vector = VectorStore(docs)
embedding = PaddleEmbedding(model=embedding_model) # 创建EmbeddingModel
vector.get_vector(EmbeddingModel=embedding)
vector.persist(path='../../storage_test/history_24') # 将向量和文档内容保存到storage目录下，下次再用就可以直接加载本地的数据库