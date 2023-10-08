import json, requests
url = 'https://fanyi.baidu.com/sug'
dat = {
    'kw': 'dog'
}
req = requests.post(url=url,data=dat)
with open('translate.html',mode='w',encoding='utf-8') as f:
    f.write(json.dumps(req.json()))
print(req.json())

