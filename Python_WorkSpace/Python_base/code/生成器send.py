'''
生成器传参
获取下一个元素 g.__next__(),next(g)
send(value) 像生成器传递参数，注意第一次必须先传第一个None
'''


def gen():
    i = 0
    while i < 5:
        temp = yield i  # temp接收send传入的值,
        print('temp', temp, i)
        i += 1
    return "没有更多值了"


g = gen()

# g.send(None)
print(g.send(None))
print(g.send("哈哈"))
print(g.send("呵呵"))
