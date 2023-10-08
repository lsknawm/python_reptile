import requests,json
url = 'https://movie.douban.com/j/chart/top_list'
param = {
    'type': '24',
    'interval_id': '100:90',
    'action': '',
    'start': 0,
    'limit': 20,
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Connection": "close"
}
db = []
for i in range(20):
    req = requests.get(url=url, headers=headers, params=param)
    db.append(req.text)
    param["start"] += 20
    print(i+1)
with open('test.html',mode='w',encoding='utf-8') as f:
    for i in range(20):
        f.write(db[i+1])
        print(i+1)