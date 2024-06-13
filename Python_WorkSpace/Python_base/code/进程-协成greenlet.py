import time

from greenlet._greenlet import greenlet


def a():
    for i in range(10):
        print("A" + str(i))
        g2.switch()
        time.sleep(0.5)


def b():
    for i in range(10):
        print("B" + str(i))
        g3.switch()
        time.sleep(0.5)


def c():
    for i in range(10):
        print("C" + str(i))
        g1.switch()
        time.sleep(0.5)


if __name__ == '__main__':
    g1 = greenlet(a)
    g2 = greenlet(b)
    g3 = greenlet(c)
    g1.switch()
