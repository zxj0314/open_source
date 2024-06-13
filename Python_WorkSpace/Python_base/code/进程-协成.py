# 协成交替完成
import time

def download():
    for i in range(10):
        print("A" + str(i))
        yield
        time.sleep(0.5)


def save():
    for i in range(10):
        print("B" + str(i))
        yield
        time.sleep(1)


if __name__ == '__main__':
    g1 = download()
    g2 = save()
    while True:
        try:
            next(g1)
            next(g2)
        except:
            break
