from multiprocessing import Process
import os
from time import sleep

'''
# 主进程运行完后，在运行子进程

'''
# 全局变量不可共用
n = 1  # 不可变
list1 = []  # 可变


def task1():
    global n
    while True:
        sleep(1)
        list1.append(str(n) + 'task1')
        print(list1)
        n = n + 1
        print("任务一------------》", n, os.getpid(), os.getppid())  # os.getpid()打印当前进程；os.getppid()打印父进程


def task2():
    global n
    while True:
        n = n + 1
        list1.append(str(n) + 'task2')
        print(list1)
        sleep(2)
        print("任务二-----------》", n, os.getpid(), os.getppid())


if __name__ == '__main__':
    print(os.getpid())  # 打印当前进程
    print("开始执行任务")
    p1 = Process(target=task1, name="任务一")
    p1.start()
    print(p1.name)
    p2 = Process(target=task2, name="任务二")
    p2.start()
    print(p2.name)
    print("任务在主进程执行完后再执行子进程")

    while True:
        sleep(1)
        n = n + 1
        print("主进程的", n)
        list1.append(str(1) + 'mian')
        print(list1)
        # 终止进程
        if n == 100:
            p1.terminate()
            p2.terminate()
