import requests,json,re
from lxml import etree
url = 'https://www.pearvideo.com/popular'
url_start = f'https://www.pearvideo.com/popular_loading.jsp?reqType=41&categoryId=&start={70}&sort={70}'

def get_url(url_top:str):
    url_top = url_top
    official_url = 'https://www.pearvideo.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    }
    req_li = requests.get(url_top,headers).text
    tree = etree.HTML(req_li)
    url_list = []
    mp4_name = []
    li = tree.xpath('//*[@id="popularList"]/li[@class="popularem clearfix"]')
    for item in li:
        url = item.xpath('./a/@href')
        url_list.append(url[0])
        name = item.xpath('./div[@class="popularem-ath"]/a/h2/text()')
        name[0] = re.sub(r'[\\/*?:"<>|]', "", name[0])
        mp4_name.append(name[0])
    for it in range(len(url_list)):
        url_list[it-1] = official_url + url_list[it-1]
    return url_list,mp4_name
def get_mp4(url,mp4_name):
    #拿到需要的contId
    url = url
    name = mp4_name
    contId = url.split('_')[1]
    videoStatus = f'https://www.pearvideo.com/videoStatus.jsp?contId={contId}'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        "Referer": f"https://www.pearvideo.com/video_{contId}"
    }
    dic = requests.get(videoStatus,headers=headers).json()
    systemTime = dic['systemTime']
    srcUrl = dic['videoInfo']['videos']['srcUrl']
    srcUrl = srcUrl.replace(systemTime,f'cont-{contId}')
    print(srcUrl)
    with open(f'./mp4/{name}.mp4',mode='wb') as f:
        f.write(requests.get(srcUrl).content)
url_list,url_name = get_url(url)
# get_mp4('https://www.pearvideo.com/video_1437657',url_name[7])
for item in range(len(url_list)):
    get_mp4(url_list[item-1],url_name[item-1])