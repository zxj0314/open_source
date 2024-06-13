# 定义带参数的装饰器

def decorate(func):
    print("wapper start-------")

    def wapper(*args, **kwargs):
        print("正在打印")
        func(*args, **kwargs)

    print("wapper end--------------")
    return wapper


@decorate
def f1(n):
    print("-----f1---------", n)


@decorate
def f2(list1):
    print("-----f1---------", list1)


@decorate
def f3(dict):
    print("-----f1---------", dict)


dict1 = {"a": "11", "b": "22"}
f1(2)
f2([1, 2, 3, 4, 5])
f3(dict1)
