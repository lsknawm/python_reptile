# import asyncio
# import time
#
#
# async def func1():
#     print('你好啊，我叫潘金莲')
#     await asyncio.sleep(3)
#     print('你好啊，我叫潘金莲')
#
#
# async def func2():
#     print('你好啊，我叫王建国')
#     await asyncio.sleep(2)
#     print('你好啊，我叫王建国')
#
#
# async def func3():
#     print('你好啊，我叫李雪晴')
#     await asyncio.sleep(4)
#     print('你好啊，我叫李雪晴')
#
#
# async def main():
#     f1 = asyncio.create_task(func1())
#     f2 = asyncio.create_task(func2())
#     f3 = asyncio.create_task(func3())
#     tasks = [f1, f2, f3]
#
#     t1 = time.time()
#     await asyncio.wait(tasks)
#     t2 = time.time()
#     print(t2 - t1)
#
#
# if __name__ == '__main__':
#     asyncio.run(main())

import asyncio
import time


async def download(url):
    print('准备开始下载')
    await asyncio.sleep(2)
    print('下载完成')
async def main():
    url = [
        'www.baidu.com',
        'www.sougou.com',
        'www.bing.com'
    ]
    takes = []
    for item in url:
        items = asyncio.create_task(download(item))
        takes.append(items)
    await asyncio.wait(takes)
if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    stop = time.time()
    print(stop-start)