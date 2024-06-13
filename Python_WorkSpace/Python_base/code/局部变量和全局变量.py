# global 变量范围
# 局部变量  全局变量
'''
global 修饰必须放在调用前
不可变变量在局部修改，需要用global修饰
可变变量不需要修饰
'''
name = '蛋炒饭'
list1 = ['a', 'd', 's', 'f']


def func():
    global name  # 在局部变量修改全局变量
    s = 'zxcsidau'  # 局部变量
    s += 'X'
    name += "吃"
    print(s, name)
    # global name  # 不能再使用后再用global修饰；SyntaxError: name 'name' is used prior to global declaration
    list1.append(9)
    # print(list1)


func()
# print(s)    # 局部变量不能再函数外部调用
print(name)  # 全局变量在函数中用global修改后，全局变量也会被修改
print(list1)
