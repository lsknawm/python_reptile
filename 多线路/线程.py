# from threading import Thread
# def func():
#     for item in range(1000):
#         print('func',item)
# if __name__ == '__main__':
#     t = Thread(target=func)
#     t.start()
#     for item in range(1000):
#         print('main',item)
# from threading import Thread
#
#第二种方法
# class MyThreadd(Thread):
#     def run(self):
#         for item in range(1000):
#             print('子线程',item)
# if __name__ == '__main__':
#     t = MyThreadd()
#     t.start()
#     for item in range(1000):
#         print('主线程',item)
from threading import Thread
def func(name):
    for item in range(1000):
        print(name,item)
if __name__ == '__main__':
    t1 = Thread(target=func,args=('周杰伦',))
    t1.start()
    t2 = Thread(target=func,args=('王力宏',))
    t2.start()