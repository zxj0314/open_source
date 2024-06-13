# 闭包

'''
闭包条件：
1、外部函数中定义了内部函数
2、外部函数是有返回值的
3、返回值是：内部函数名
4、内部函数引用了外部函数的局部变量
'''


def out_func():
    a = 10

    def inner_func():
        b = 99
        print(a, b)

    print(locals())
    return inner_func


# out_func()  # <function out_func at 0x00000136EB3D2EA0>
# result = out_func() # 将内部函数返回值赋值给result
# result()    # 调用内部函数inner_func()


def calculate(a, b):
    c = 0

    def add():
        c = a + b
        print(c)

    return add


result1 = calculate(4, 6)
result2 = calculate(3, 7)

result1()
result2()
