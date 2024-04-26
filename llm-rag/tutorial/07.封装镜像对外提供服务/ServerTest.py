import json

import numpy as np
import requests

req = {"input": "你好我想了解一下大模型","model":"rocketqa-zh-base-query-encoder"}
emb_url = "http://127.0.0.1:5000"
response_raw = requests.post(emb_url+"/v1/embedding", json=req)

if response_raw.status_code >= 400 and response_raw.status_code != 503:
    raise Exception(f"{vars(response_raw)}")

response = response_raw.json()
if "errors" in response:
    raise Exception(", ".join(response["errors"]))

if response:
    # print("result",response)
    data = np.asarray(json.loads(response).tolist())
    print(data)

