# import json
# import requests
# headers = {
#     "Accept": "*/*",
#     "Accept-Language": "zh-CN,zh;q=0.9",
#     "Connection": "keep-alive",
#     "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
#     "Origin": "http://www.xinfadi.com.cn",
#     "Referer": "http://www.xinfadi.com.cn/priceDetail.html",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
#     "X-Requested-With": "XMLHttpRequest"
# }
# url = "http://www.xinfadi.com.cn/getPriceData.html"
# data = {
#     "limit": "20",
#     "current": "1",
#     "pubDateStartTime": "",
#     "pubDateEndTime": "",
#     "prodPcatid": "",
#     "prodCatid": "",
#     "prodName": ""
# }
# response = requests.post(url, headers=headers, data=data, verify=False)
# data = json.loads(response.text)['list']
# print(data[6])
# f = open('test.csv',mode='w',encoding='utf-8')
# f.write('一级分类,二级分类,品名,最低价,平均价,最高价,规格,产地,单位,发布日期\n')
# for item in data:
#     f.write(f'''{item["prodCat"]},{item["prodPcat"]},{item["prodName"]},{item["lowPrice"]},{item["avgPrice"]},{item["highPrice"]},{item['specInfo']},{item["place"]},{item['unitInfo']},{item['pubDate']}\n''')

import json
import time

import requests
from concurrent.futures import ThreadPoolExecutor



