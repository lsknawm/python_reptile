import requests
from bs4 import BeautifulSoup
import urllib3
import time
import re
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
url = 'https://www.umei.cc/katongdongman/dongmanbizhi/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}
def get_page_url():
    req = requests.get(url=url, headers=headers, verify=False)
    req.encoding = 'utf-8'
    page = BeautifulSoup(req.text, "html.parser")
    alist = page.find('div', attrs={"class": "item_list infinite_scroll"}).find_all('a',attrs={"class": "img_album_btn"})
    self_list = []
    for i in alist:
        self_list.append('https://www.umei.cc/' + i.get("href")[1:])
    req.close()
    return self_list
url_list = get_page_url()

def get_image(image_url):
    self_list = []
    self_name = []
    for item in url_list:
        req = requests.get(item,headers=headers,verify=False)
        req.encoding = 'utf-8'
        page = BeautifulSoup(req.text, "html.parser")
        image_list = page.find('div',{'class': 'big-pic'}).find('img').get('src')
        name_list = page.find('div',{'class': 'big-pic'}).find('img').get("title")
        self_name.append(name_list)
        self_list.append(image_list)
        req.close()
    return self_list,self_name
image_list,name_list = get_image(url_list)
print(image_list)
print(name_list)
for i in range(len(image_list)):
    img_resp = requests.get(image_list[i-1])
    # img_resp.content
    img_name = name_list[i-1].replace('，','_').replace(' ','').replace('<','_').replace('>','_').replace('/','')
    with open((img_name+'.jpg'),mode='wb') as f:
        f.write(img_resp.content)
    print(f'{[img_name]} download success ! ! !')
    time.sleep(1)
print('all_ovler')
