
from RAG.VectorBase import VectorStore
from RAG.utils import ReadFiles
from RAG.LLM import OpenAIChat, InternLMChat, GLM4Chat
from RAG.Embeddings import JinaEmbedding, ZhipuEmbedding

docs = ReadFiles('../../data/github_data').get_content(min_token_len=600, max_token_len=1800, cover_content=150) # 获得data目录下的所有文件内容并分割
vector = VectorStore(docs)
embedding = ZhipuEmbedding() # 创建Zhipu EmbeddingModel
vector.get_vector(EmbeddingModel=embedding)
vector.persist(path='../../storage/github_data') # 将向量和文档内容保存到storage目录下，下次再用就可以直接加载本地的数据库