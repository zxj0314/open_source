import time

import gevent
from gevent import monkey

monkey.patch_all()


def a():
    for i in range(10):
        print("A" + str(i))
        time.sleep(0.5)


def b():
    for i in range(10):
        print("B" + str(i))
        time.sleep(0.5)


def c():
    for i in range(10):
        print("C" + str(i))
        time.sleep(0.5)


if __name__ == '__main__':
    g1 = gevent.spawn(a)
    g2 = gevent.spawn(b)
    g3 = gevent.spawn(c)
    g1.join()
    g2.join()
    g3.join()
