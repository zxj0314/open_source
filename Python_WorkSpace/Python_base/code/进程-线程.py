# 线程
import threading
from time import sleep


def download(n):
    imgs = ['girl.jpg', 'boy.jpg', 'man.jpg']
    for img in imgs:
        print('正在下载图片:', img)
        sleep(0.5)
        print('下载{}成功'.format(img))


def listenMusic():
    musics = ['as', 'ad', 'af', 'ag', 'ah']
    for muc in musics:
        print('正在听{}:'.format(muc))
        sleep(0.5)


if __name__ == '__main__':
    # 创建线程对象
    t = threading.Thread(target=download, args=(1,))
    t.start()
    t1 = threading.Thread(target=listenMusic, name='listen')
    t1.start()
