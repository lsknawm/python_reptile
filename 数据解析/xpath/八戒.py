import csv

import requests
from lxml import etree
f = open('BJ.html',mode='r',encoding='utf-8')
htm_l = f.read()
f.close()
htm = etree.HTML(htm_l)
divs = htm.xpath('//*[@id="__layout"]/div/div[3]/div/div[4]/div/div[2]/div[1]/div')
f = open('date.csv',mode='w',encoding='utf-8')
csvwrite = csv.writer(f)
csvwrite.writerow('价格,商品名称,商家,省份\n')
for div in divs:
    price = div.xpath('./div/div[3]/div[1]/span[1]/text()')[0].strip('¥')
    print(price)
    title = 'saas'.join(div.xpath('./div/div[3]/div[2]/a/text()'))
    print(title)
    com_name = div.xpath('./div/a/div[2]/div[1]/div/text()')[0]
    print(com_name)
    location = div.xpath('./div/div[@class="card-box"]/a/div[2]/div[@class="tabstwo"]/span[2]/text()')[0]
    print(location)
    # csvwrite.writerow(price,title)