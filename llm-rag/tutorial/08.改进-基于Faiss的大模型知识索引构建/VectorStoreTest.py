from RAG.Embeddings import ZhipuEmbedding
from RAG.FaissVectorBase import FaissVectorStore
from RAG.LLM import GLM4Chat

# 保存数据库之后
from RAG.PaddleEmbedding import PaddleEmbedding
from RAG.VectorBase import VectorStore

vector = VectorStore()

vector.load_vector('../../storage/history_24') # 加载本地的数据库

question = '关羽是被谁害死的？'

embedding = PaddleEmbedding() # 创建EmbeddingModel

content = vector.query(question, EmbeddingModel=embedding, k=1)[0]

chat = GLM4Chat()

print(chat.chat(question, [], content))

