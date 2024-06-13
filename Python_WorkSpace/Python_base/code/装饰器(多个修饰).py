# 多个装饰器同时装饰一个函数
# 离得近的装饰器优先执行


def decorate1(func):
    print("装饰器1开始装修")

    def wapper(*args, **kwargs):
        func(*args, **kwargs)
        print("刷墙")

    return wapper


def decorate2(func):
    print("装饰器2开始装修")

    def wapper(*args, **kwargs):
        func(*args, **kwargs)
        print("铺地板")

    return wapper


@decorate2
@decorate1  # 装饰器里的近的优先执行
def house():
    print("毛坯房")


house()
