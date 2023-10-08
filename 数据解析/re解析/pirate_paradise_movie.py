import re

import requests
domain = 'https://www.dyttcn.com/'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}
req = requests.get(url=domain,headers=headers,verify=False)
req.encoding = 'gb2312'
# print(req.text)
#第一次匹配到需要的li标签
obj1 = re.compile(r'最新更新.*?<ul>(?P<ul>.*?)</ul>',re.S)
obj2 = re.compile(r'''<li><a href='(?P<url>.*?)' title="(?P<mode_name>.*?)">.*?</a><span><font color=.*?</font></span></li>''',re.S)

obj3 = re.compile(r'''◎片　　名(?P<movie>.*?)</p>.*?<table bgcolor="#0099cc" border="0" cellpadding="5" cellspacing="1" width="100%">.*?<tr>.*?<td bgcolor=.*width=".*?">.*?<a href="(?P<download>.*?)">.*?</a></td>''',re.S)

resp1 = obj1.finditer(req.text)
child_herf_list = []
#拿到ul里面的li标签
for item in resp1:
    ul = item.group("ul")
    # print(ul)
    resp2 = obj2.finditer(ul)
    for it in resp2:
        child_herf = domain + it.group("url").strip('/')
        child_herf_list.append(child_herf)
        print(it.group("mode_name"))
        print(child_herf)
print(child_herf_list)

for href in child_herf_list:
    child_resp = requests.get(href,verify=False,headers=headers)
    child_resp.encoding = 'gb2312'
    print('-'*50)
    resp3 = obj3.search(child_resp.text)
    print(resp3.group("movie"))
    print(resp3.group("download"))
