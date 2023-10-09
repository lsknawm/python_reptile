import json
import time

import requests

time.sleep(5)
print('sleep 5s')
time.sleep(5)
time.sleep(15)
print('sleep 45s')
time.sleep(30)
dog = input('输入')
data = {
    'from': 'en',
    'to': 'zh',
    'query': dog
}
req = requests.post(url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh',data=json.dumps(data),headers=aaaaa)
print(req.text)