import time
import timeit
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
for item in range(1000):
    print(item)
start = time.time()
for item in range(1000*1000):
    print(item)
# def fn(name):
#     for item in range(1000):
#         print(name,item)
# if __name__ == '__main__':
#     with ThreadPoolExecutor(50) as t:
#         for item in range(1000):
#             t.submit(fn,name=f'线程{item}')
#     print('结束')
stop = time.time()
print(stop - start)
