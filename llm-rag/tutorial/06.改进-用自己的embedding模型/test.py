from RAG.FaissVectorBase import FaissVectorStore
from RAG.LLM import GLM4Chat

# 保存数据库之后
from RAG.PaddleEmbedding import PaddleEmbedding

vector = FaissVectorStore()

vector.load_vector('../../storage/history') # 加载本地的数据库

question = 'Git 中的文件有哪几种状态?'

embedding = PaddleEmbedding() # 创建EmbeddingModel

content = vector.query(question, EmbeddingModel=embedding, k=1)[0]

chat = GLM4Chat()

print(chat.chat(question, [], content))