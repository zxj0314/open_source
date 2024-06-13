# 装饰器
'''
1、函数作为参数传递
2、要有闭包的特点
    1、外部函数中定义了内部函数
    2、外部函数是有返回值的
    3、返回值是：内部函数名
    4、内部函数引用了外部函数的局部变量
3、
'''


# 地址引用
def func():
    print("地址引用")


f = func  # 把func的地址赋值给f，地址一样


# f()


# 定义装饰器；拥有闭包特点
def decorate(func):  # ②此时func=house，
    a = 100
    print("wapper 外层")  # 装饰器默认执行
    print(func)  # <function house at 0x0000022598BD0C80>

    # 内部函数
    def wapper():  # ③然后加载wapper
        func()
        print("wapper 内层")

    print("wapper 结束")  # 装饰器默认执行
    print(wapper)  # <function decorate.<locals>.wapper at 0x0000022598BD0D08>
    return wapper  # ④将wapper扔出


# 使用装饰器，①加了装饰器，就是将被装饰器函数house赋值给func
@decorate
def house():  # ⑤装饰后house就等于最终加载的wapper
    print(house)  # <function decorate.<locals>.wapper at 0x0000022598BD0D08>
    print("精简装修房")


house()
