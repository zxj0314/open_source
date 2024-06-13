'''
列表推导式是 Python 语言特有的一种语法结构，也可以看成是 Python 中一种独特的数据处理方式。所谓的列表推导式，就是指的轻量级循环创建列表。
列表推导式的两大作用: 转换 和 过滤 数据
列表推导式的语法格式:
    [表达式 for 迭代变量 in 可迭代对象 [if 条件表达式]]
列表表达式由四个部分组成：
    输入的列表
    列表循环变量
    可选的约束条件
    输出表达式
'''
# 取出列表中的数字，然后得到平方值放入新的列表中
a = [1, 2, 3, 'a', 'b', 'c']
b = [i ** 2 for i in a if isinstance(i, int)]
print(b)

# 支持两层for循环
a = [1, 2, 3, 4, 5, 6, 7]
b = [1, 2, 3, 4, 7, 7, 7]
c = [(x, y) for x in a for y in b if (x == y)]
print(c)  # [(1, 1), (2, 2), (3, 3), (4, 4), (7, 7), (7, 7), (7, 7)]
# 如果想要得到 a、b 两个列表中对应索引相同的元素对
d = [(a[x], b[y]) for x in range(7) for y in range(7) if a[x] == b[y] and (x == y)]
print(d)  # [(1, 1), (2, 2), (3, 3), (4, 4), (7, 7)]

# 多层嵌套
nn_list = [(x, y, z, m) for x in range(3) for y in range(3) for z in range(3) for m in range(3)]
print(nn_list)

nn_list = [(x, y, z, m) for x in range(3) if x > 1 for y in range(3) if y > 1 for z in range(3) for m in range(3)]
print(nn_list)
nn_list = [(x, y, z, m) for x in range(3) for y in range(3) for z in range(3) for m in range(3) if x > 1 and y > 1]
print(nn_list)
# 矩阵转至
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [[row[i] for row in a] for i in range(3)]
print(b)
# 矩阵平铺
y = [j for i in a for j in i]
print(y)

# 生成100以内的素数
'''
试除法：通过尝试将n除以2到sqrt(n)之间的所有整数，如果都无法整除，则n是素数。具体步骤如下：
- 从2开始，遍历2到sqrt(n)的所有整数，尝试将n除以当前整数。
- 如果n能够被当前整数整除，则n不是素数。
- 如果遍历完所有整数后都没有找到能够整除n的数，则n是素数。
'''
import numpy as np

a = [x for x in range(2, 101) if 0 not in [x % i for i in range(2, int(x / 2))]]
print(a)

# # 100以内的质数
# num = []
# i = 2
# for i in range(2, 101):
#     j = 2
#     for j in range(2, i):
#         if (i % j == 0):
#             break
#     else:
#         num.append(i)
# print(num)

# 集合推导式
l1 = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
s1 = {x for x in l1}
print(s1)
s2 = {x for x in l1 if x > 50}
print(s2)
