import json
import time
from lxml import etree
f = open('acg.html',mode='r',encoding='utf-8')
html_date = f.read()
html = etree.HTML(html_date)
table = html.xpath('//*[@id="content"]/div[3]/div/div/div[4]/div')
my_dic = {}
for item in range(len(table)):
    print('-' * 250)
    url_name = table[item-1].xpath('./div/a[1]/@data-original-title')
    print(url_name)
    description = table[item-1].xpath('./div/a[1]/div/div[1]/img/@alt')
    print(description)
    url = table[item-1].xpath('./div/a[1]/@data-url')
    print(url)
    my_dic[url_name[0]] = (description[0],url[0])
print(my_dic)