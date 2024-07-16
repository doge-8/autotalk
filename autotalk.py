import requests
import time

##url换成自己的
url = "https://gaianet.network/v1/chat/completions"
headers = {
    "accept": "application/json",
    "Content-Type": "application/json"
}
data = {
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Where is Paris?"}
    ]
}

while True:
    response = requests.post(url, headers=headers, json=data)
    print(response.json())
    time.sleep(1)
