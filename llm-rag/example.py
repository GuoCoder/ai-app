from RAG.VectorBase import VectorStore
from RAG.utils import ReadFiles
from RAG.LLM import OpenAIChat, InternLMChat, GLM4Chat
from RAG.Embeddings import JinaEmbedding, ZhipuEmbedding


# 保存数据库之后
vector = VectorStore()

vector.load_vector('./storage') # 加载本地的数据库

question = 'git如何申请个人访问令牌？'

embedding = ZhipuEmbedding() # 创建EmbeddingModel

content = vector.query(question, EmbeddingModel=embedding, k=1)[0]
#chat = OpenAIChat(model='gpt-3.5-turbo-1106')
chat = GLM4Chat()
print(chat.chat(question, [], content))

