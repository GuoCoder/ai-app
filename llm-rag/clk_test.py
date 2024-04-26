import tiktoken_ext.openai_public
import inspect

print(dir(tiktoken_ext.openai_public))
# The encoder we want is cl100k_base, we see this as a possible function

print(inspect.getsource(tiktoken_ext.openai_public.cl100k_base))
# The URL should be in the 'load_tiktoken_bpe function call'

import hashlib

# 我的blobpath是https://openaipublic.blob.core.windows.net/encodings/cl100k_base.tiktoken
blobpath = "https://openaipublic.blob.core.windows.net/encodings/cl100k_base.tiktoken"
cache_key = hashlib.sha1(blobpath.encode()).hexdigest()
print(cache_key)

import os
print(os.getenv("ZHIPUAI_API_KEY"))
