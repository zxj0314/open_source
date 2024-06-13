# 带参数的装饰器
'''
带参数的装饰器，装3层
最外层是装饰器的参数
第二层是被装饰函数的参数
第三层是修饰做的内容
三层必须带参数，不带参数会失败
'''


def outer(a):
    def decorate(func):
        def wapper(*args, **kwargs):
            func(*args, **kwargs)
            print("开始装修")
            print("装修工期是{}天".format(a))

        return wapper

    return decorate


@outer(10)  # 带参数的装饰器
def house():
    print("毛坯房")


@outer(100)
def street():
    print("修路")


house()
print("*" * 30)
street()
