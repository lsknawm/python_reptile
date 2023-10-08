import requests
session = requests.session()
date = {
        'loginName': '17859530620',
        'password': 'lsknawm@'
}
url = 'https://passport.17k.com/ck/user/login'
session.post(url,date)
# print(req.text)
resp = session.get('https://user.17k.com/ck/user/myInfo/101706934?bindInfo=1&appKey=2406394919')
resp.encoding = 'utf-8'
with open('text.html',mode='w',encoding='utf-8') as f:
        f.write(resp.text)
print(resp.text)
