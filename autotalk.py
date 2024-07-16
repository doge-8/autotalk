import requests
import time

while True:
    # 发送 HTTP 请求
    response = requests.post(
        "https://你的节点地址/v1/chat/completions",
        headers={"accept": "application/json", "Content-Type": "application/json"},
        data='{"messages":[{"role":"system", "content": "You are a helpful assistant."}, {"role":"user", "content": "Where is Paris?用中文回答我"}]}'
    )
    
    # 打印响应结果
    print(response.json())
    
    # 等待 1 秒钟
    time.sleep(1)
