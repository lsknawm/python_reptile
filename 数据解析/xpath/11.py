import requests


headers = {
    "authority": "svc.ncc.douxuedu.com",
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHBpcmUtYXQiOjE2OTQ5NTE4NDk2MDYsImV4cCI6MTY5NDk1MTg0OSwiaWF0IjoxNjk0OTQ4MjE5LCJhY2NvdW50IjoiZmp4eHMxMiJ9.mzD_tT9FyM4EwuEotRGwyxL3DRjo1yypGbadC9wwQIM",
    "origin": "https://ncc.douxuedu.com",
    "referer": "https://ncc.douxuedu.com/",
    "sec-ch-ua": "^\\^Microsoft",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "^\\^Windows^^",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "session_token": "1417543c1f532d7aa991bc6746acb804",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.31"
}
url = "https://svc.ncc.douxuedu.com/resource/api/v1/cloud/getPlatformTypes"
url_1 = 'https://ncc.douxuedu.com/classroom/resource'
response = requests.get(url_1, headers=headers)
response.encoding = 'utf-8'
with open('dxw.html',mode='w',encoding='utf-8') as f:
    f.write(response.text)
print(response.text)
# print(response)