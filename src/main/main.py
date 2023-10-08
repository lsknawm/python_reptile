import requests
url = 'https://www.baidu.com/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}
req = requests.get(url,headers=headers,verify=False)
with open('test.html',mode='w',encoding='utf-8') as f:
    f.write(req.text)
print('hello-git')
print('hello-git')
print('hello-git')
print('hello-git')
print('hello-git')
print('hello-git')
print('hello-git')
print('hello-git')
print('hello-git')
print('lsknawm')
print('第三个')