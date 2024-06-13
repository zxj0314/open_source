# 阻赛式进程
import os
import random
import time
from multiprocessing import Process, Pool

def task(task_name):
    print("开始做任务：", task_name)
    start_time = time.time()
    time.sleep(random.random() * 2)
    end_time = time.time()
    print('完成任务:{}！用时{}，进程ID{}'.format(task_name, (start_time - end_time), os.getpid()))

if __name__ == '__main__':
    pool = Pool(5)
    tasks = ['听歌', '打游戏', '做饭', '洗衣服', '拖地', '扔垃圾', '遛狗']
    for c in tasks:
        pool.apply(task, args=(c,))
    pool.close()
    pool.join()
    print('cev.')
