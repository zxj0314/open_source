'''
生成器：
列表推导式：[表达式 for 迭代变量 in 可迭代对象 [if 条件表达式]]
generate：(表达式 for 迭代变量 in 可迭代对象 [if 条件表达式])

'''

# 生成器
g1 = (x * 3 for x in range(20))
print(g1)  # <generator object <genexpr> at 0x000001C14B53F4C0>
# print(g1.__next__())    # 3 打印第一个数
# print(next(g1))      # 6 打印第二个数

while True:
    try:
        n1 = next(g1)
        print(n1, end=",")
    except StopIteration:
        print("取完了")
        break


# 生成器
def func():
    n = 0
    while True:
        n += 1
        yield n  # return n + 暂停作用


g = func()
print(g)
print(next(g))
print(next(g))


def gen():
    i = 0
    while i < 5:
        temp = yield i
        print('temp:', temp)
        i += 1
    return "没有更多元素"


g = gen()

