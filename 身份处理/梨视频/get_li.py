#1. 拿到contid
#2. 拿到videostatus返回的json -> srcurl
#3. srcurl里面的内容进行休整
#4. 下载视频
import requests
url = 'https://www.pearvideo.com/video_1437657'
def returon_video(url):
    url = url
    contId = url.split('_')[1]
    print(contId)
    videoStatus = f'https://www.pearvideo.com/videoStatus.jsp?contId={contId}'

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        #防盗链，本次请求的上一级
        "Referer": f'https://www.pearvideo.com/video_{contId}'
    }
    resp = requests.get(videoStatus,headers=headers)
    dic = resp.json()

    srcUrl = dic['videoInfo']['videos']['srcUrl']
    systemTime = dic['systemTime']
    srcUrl = srcUrl.replace(systemTime,f'cont-{contId}')
    print(srcUrl)
    with open(f'{contId}.mp4',mode='wb') as f:
        f.write(requests.get(srcUrl).content)
returon_video(url)