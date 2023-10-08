import re,requests,csv
cod = 0
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}
obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?<br>.*?(?P<date>\d+)&nbsp.*?<span class="rating_num" property="v:average">(?P<scode>.*?)</span>.*?<span>(?P<per>\d+)人评价</span>',re.S)
while (cod * 25 <= 250):
    url = f'https://movie.douban.com/top250?start={cod}&filter='
    req = requests.get(url=url, headers=headers).text
    resp = obj.finditer(req)
    f = open('test.csv', mode='w', encoding='utf-8', newline='')
    csvwrite = csv.writer(f)
    for item in resp:
        dic = item.groupdict()
        csvwrite.writerow(dic.values())
    f.close()
    print(f'[{cod}]over!!!')
    cod += 1




#匹配需要内容的正则公式








# with open('test.csv',mode='w',encoding='utf-8') as f:
#     csvwrite = csv.writer(f)
#     for item in resp:
#         dic = item.groupdict()
#         dic['per'] = dic['per'].strip()
#         csvwrite.writerow(dic.values())