
import os
from typing import Dict, List, Optional, Tuple, Union

import PyPDF2
import markdown
import html2text
import json
from tqdm import tqdm
import tiktoken
from bs4 import BeautifulSoup
import re

enc = tiktoken.get_encoding("cl100k_base")


file_path = "./data/history_24/baihuabeishi.txt"

with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()



curr_len = 0
curr_chunk = ''
min_token_len = 600
max_token_len = 1600
cover_content = 150
lines = content.split('\n')  # 假设以换行符分割文本为行
chunk_text = []
chunk_lenth = []

for line in lines:
    line = line.replace(' ', '')
    line_len = len(enc.encode(line))
    if curr_len > max_token_len:
        while (curr_len > max_token_len):
            split_a = enc.encode(curr_chunk)[:max_token_len]
            split_b = enc.encode(curr_chunk)[max_token_len:]
            curr_chunk = enc.decode(split_a)
            chunk_text.append(curr_chunk)
            chunk_lenth.append(max_token_len)
            curr_chunk = curr_chunk[-cover_content:] + enc.decode(split_b)
            curr_len = cover_content + curr_len - max_token_len
    else:

        if(curr_len <= min_token_len):
            curr_chunk += line
            curr_chunk += '\n'
            curr_len += line_len
            curr_len += 1
        else:
            chunk_text.append(curr_chunk)
            chunk_lenth.append(curr_len)
            curr_chunk = curr_chunk[-cover_content:] + line
            curr_len = line_len + cover_content

if curr_chunk:
    chunk_text.append(curr_chunk)
    chunk_lenth.append(curr_len)

chunk_str =json.dumps(chunk_text,indent=4,sort_keys=True,ensure_ascii=False)#设置缩进级别为4# 排序键sort keys=True


with open(f"./docement.json", 'w', encoding='utf-8') as f:
    json.dump(chunk_str, f,ensure_ascii=False)

print(chunk_text)

print(chunk_lenth)

print(max(chunk_lenth))
print(f"chunk_lenth中最大为：{max(chunk_lenth)};\nchunk_lenth中最小为：{min(chunk_lenth)};\nchunk_text中有{len(chunk_text)}个\n")
