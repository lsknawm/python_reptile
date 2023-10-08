# from multiprocessing import Process
# def func():
#     for item in range(1000):
#         print('子进程',item)
# if __name__ == '__main__':
#     p = Process(target=func())
#     p.start()
#     for item in range(1000):
#         print('进程',item)
#
from multiprocessing import Process

def print_func():
    for item in range(10000000):
        print(f"Hello, {item}")

if __name__ == "__main__":
    t1 = Process(target=print_func)
    t1.start()
    for item in range(10000000):
        print('主',item)