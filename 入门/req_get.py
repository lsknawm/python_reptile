import requests,webbrowser
query = input('请输入想搜索的内容:\n')
url = f'https://www.sogou.com/web?query={query}'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}
resp =  requests.get(url,headers=headers)   #此处返回内容会显示不正常，因为这个访问并不是真的由浏览器请求的，是由python发起的一个请求
with open('mybaidu.html',mode="r+",encoding='utf-8') as f:
    f.write(resp.text)