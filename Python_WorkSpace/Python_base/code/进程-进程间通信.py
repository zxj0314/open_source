from multiprocessing import Queue, Process
from time import sleep


# que = Queue(5)
# print(que.full())  # 布尔值
# print(que.empty())  # 布尔值
# for i in range(10):
#     if not que.full():
#         que.put(i, timeout=3)  # 相队列中存
#     else:
#         print("队列已满")
#         break
# print(que.get(timeout=2))
# print(que.get(timeout=2))


# que.get_nowait()
# que.get_nowait()

# 进程间通信应用
def download(que):
    imgs = ['girl.jpg', 'boy.jpg', 'man.jpg']
    for img in imgs:
        print('正在下载图片:', img)
        que.put(img)
        sleep(0.5)


def save(que):
    while True:
        try:
            file = que.get(timeout=5)
            print('保存成功:', file)
        except:
            break


if __name__ == '__main__':
    que = Queue(5)
    p1 = Process(target=download, args=(que,))
    p1.start()
    p1.join()
    p2 = Process(target=save, args=(que,))
    p2.start()
    p2.join()
