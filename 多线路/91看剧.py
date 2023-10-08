import requests,re

# m3u8_url = 'https://v6.1080pzy.co/20220806/RXTYqmTO/hls/index.m3u8'
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
# }
# resp = requests.get(url=m3u8_url,headers=headers)
# with open('./mp4/哲仁皇后.m3u8',mode='w',encoding='utf-8') as f:
#     f.write(resp.text)
# resp.close()
# print('下载完毕!!!')


# 解析m3u8
n = 1
with open('./mp4/哲仁皇后.m3u8',mode='r',encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line.startswith("#"):
            continue
        resp = requests.get(line)
        f = open(f'./mp4/{n}.ts',mode='wb')
        f.write(resp.content)
        print(n)
        n += 1