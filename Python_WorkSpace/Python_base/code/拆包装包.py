# 拆包

tup1 = (1, 3, 7, 2, 4, 8)
a, b, *c = tup1  # *c 表示未知个数，[]
print(a, b, c)
print(a, b, *c)  # 拆包

list1 = [1, 2, 3, 4, 5, 6, 7, 8]
d, e, *f = list1
print(d, e, f)
print(d, e, *f)  # 拆包
