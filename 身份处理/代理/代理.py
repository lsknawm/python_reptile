import requests,urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxy = '43.138.20.156:80'      #此处用的代理是有可能用不了的，得多尝试
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}
proxies = {
    'http': f'http://{proxy}',
    # 'https': f"https://{proxy}"
}
resp = requests.get('https://www.baidu.com/',proxies=proxies,headers=headers,verify=False)
resp.encoding='utf-8'
print(resp.text)