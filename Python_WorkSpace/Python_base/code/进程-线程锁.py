import threading
import time

lock = threading.Lock()
list1 = [0] * 10
print(list1)


def task1():
    lock.acquire()
    for i in range(len(list1)):
        list1[i] = 1
        time.sleep(0.3)
    lock.release()


def task2():
    lock.acquire()
    for i in range(len(list1)):
        print('------------>',i, list1[i])
        time.sleep(0.3)
    lock.release()


if __name__ == '__main__':
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)
    t1.start()
    t2.start()
