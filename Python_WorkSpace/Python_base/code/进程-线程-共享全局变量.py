import threading
from time import sleep

ticketnum = 1000


def ticket(name):
    global ticketnum
    for i in range(100):
        ticketnum -= 1
        # sleep(0.1)
    print('{}卖了100张票！'.format(name))


if __name__ == '__main__':
    t1 = threading.Thread(target=ticket, name='ticket1', args=('ticket1',))
    t2 = threading.Thread(target=ticket, name='ticket2', args=('ticket2',))
    t3 = threading.Thread(target=ticket, name='ticket3', args=('ticket3',))
    t1.setName('tark')  # 更改name
    print(t1.name)
    t1.start()
    t1.join()
    t2.start()
    t2.join()
    t3.start()
    t3.join()
    print('还剩余车票：', ticketnum)
