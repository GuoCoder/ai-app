from RAG.Embeddings import ZhipuEmbedding
from RAG.FaissVectorBase import FaissVectorStore
from RAG.LLM import GLM4Chat

# 保存数据库之后
from RAG.PaddleEmbedding import PaddleEmbedding

vector = FaissVectorStore()

vector.load_vector('../../storage/history_24_1') # 加载本地的数据库

question = '介绍一下秦二世'

embedding = PaddleEmbedding() # 创建EmbeddingModel

content = vector.query(question, EmbeddingModel=embedding, k=3)[0]
print(f'知识库输出：{content}')

chat = GLM4Chat()

print(chat.chat(question, [], content))

