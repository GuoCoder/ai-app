from RAG.Embeddings import ZhipuEmbedding
from RAG.FaissVectorBase import FaissVectorStore
from RAG.LLM import GLM4Chat

# 保存数据库之后
from RAG.PaddleEmbedding import PaddleEmbedding
from RAG.VectorBase import VectorStore

vector = VectorStore()

vector.load_vector('../../storage/github_data') # 加载本地的数据库

question = 'Git中的文件有哪几种状态?'

embedding = ZhipuEmbedding()

content = vector.query(question, EmbeddingModel=embedding, k=1)[0]

chat = GLM4Chat()

print(chat.chat(question, [], content))


## 基于Faiss检索耗时：0.570064s
