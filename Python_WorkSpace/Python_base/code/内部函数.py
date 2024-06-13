# 内部函数

a = 10

print(globals())    # 查看全局变量
def func():
    b = 100
    list1 = [1, 8, 5, 6, 2]

    def inner_func():
        # 对list1元素＋5
        global a  # 对全局变量a修改
        nonlocal b  # 对内部局部变量b进行修改
        for index, i in enumerate(list1):
            list1[index] = i + 5
        print(list1)
        a = a + 10
        b = b + 100
        print(a, b)
        print(locals())     # 查看当前函数中声明的内容

    inner_func()


# 调用函数
func()
