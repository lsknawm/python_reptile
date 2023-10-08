import aiohttp,asyncio
urls = [
    'http://kr.shanghai-jiuxin.com/file/bizhi/20220927/nuxizveelbg.jpg',
    'http://kr.shanghai-jiuxin.com/file/bizhi/20220927/r1fflxqp20p.jpg',
    'http://kr.shanghai-jiuxin.com/file/bizhi/20220927/kjjg5atrnkl.jpg'
]
async def aiodownload(url):
    name = url.rsplit("/",1 )[1] #拿到名字，从右边切，切一次得到[1]位置内容
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            with open(name,mode='wb') as f:
                f.write(await resp.content.read())
    print(name,'搞定')










async def main():
    tasks = []
    for item in urls:
        tasks.append(asyncio.create_task(aiodownload(item)))
    await asyncio.wait(tasks)

if __name__ == '__main__':
    asyncio.run(main())