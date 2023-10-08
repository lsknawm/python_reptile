import requests,json,time,aiohttp,asyncio,aiofiles
# https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4306063500"}   所有章节内容(名称，cid)

# https://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4306063500","cid":"4306063500|1569782244","need_bookinfo":1}    装载文章内容
'''
同步操作访问小说的ajax网页得到所以章节的名字和cid
异步操作分别访问每个章节对应的地址拿到章节内容
整合章节内容
'''
async def aiodownload(cid,book_id,title):
    data = {
    "book_id":book_id,
        "cid":f"{book_id}|{cid}",
        "need_bookinfo":1
    }
    data = json.dumps(data)
    url = f'https://dushu.baidu.com/api/pc/getChapterContent?data={data}'
    # print(url)
    async with aiohttp.ClientSession() as session:
        async with session.get(url,headers=headers) as resp:
            dic = await resp.json()

            async with aiofiles.open(f"./txt/{title}.txt",mode='w',encoding='utf-8') as f:
                await f.write(dic['data']['novel']['content'])
    pass
async def getCatalog(url):
    resp = requests.get(url,headers=headers)
    resp_data = json.loads(resp.text)
    tasks = []
    dic = resp_data['data']['novel']['items']
    for item in dic:
        title = item['title']
        cid = item['cid']
        tasks.append(asyncio.create_task(aiodownload(cid,bookid,title)))
    await asyncio.wait(tasks)

if __name__ == '__main__':
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    }
    bookid = '4306063500'
    url = 'https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":' + bookid +  '}'
    asyncio.run(getCatalog(url))