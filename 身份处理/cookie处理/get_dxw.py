import requests
session = requests.session()
date = {
        'account':"fjxxs12",
        'loginType':"A_P",
        'password':"123456ok"
}
headers = {
    "Content-Type": "application/json"
}
url = 'https://svc.ncc.douxuedu.com/system/out-api/v1/login'
resp = session.post(url,date,headers=headers,verify=False)
resp.encoding='utf-8'
session.get(url='https://www.23qb.net/bookcase.php',)