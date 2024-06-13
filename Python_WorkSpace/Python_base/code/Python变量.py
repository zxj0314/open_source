# Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
# 可变不可变
'''
不可变：整数，字符串，元祖
可变类型：列表，字典，集合
'''


# 1、Number（数字）
a = 111
print(type(a))  # type()不会认为子类是一种父类类型。
print(isinstance(a, int))  # isinstance()会认为子类是一种父类类型。
del a  # 删除对象引用
# print(a)    # NameError: name 'a' is not defined

x, y = 1, 2  # 多个变量赋值，如

# 2、String（字符串）
'''
# Python中的字符串用单引号 ' 或双引号 " 括起来，同时使用反斜杠 \ 转义特殊字符；字符串不能被改变
1、反斜杠可以用来转义，使用r可以让反斜杠不发生转义。
2、字符串可以用+运算符连接在一起，用*运算符重复。
3、Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
4、Python中的字符串不能改变。
'''
string = 'Runoob'
print(string[0])  # 输出字符串第一个字符
print(string[2:])  # 输出从第三个开始的后的所有字符
print(string[2:5])  # 输出从第三个开始到第五个的字符
print(string * 2)  # 输出字符串两次，也可以写成 print (2 * str)
print(string + "TEST")  # 连接字符串
# 反斜杠 \ 转义特殊字符
print('Ru\noob')

# 3、 bool(布尔类型)
'''
在 Python 中，True 和 False 都是关键字，表示布尔值。
布尔类型只有两个值：True 和 False。
布尔类型可以和其他数据类型进行比较，比如数字、字符串等。在比较时，Python 会将 True 视为 1，False 视为 0
布尔类型可以和逻辑运算符一起使用，包括 and、or 和 not。这些运算符可以用来组合多个布尔表达式，生成一个新的布尔值。
布尔类型也可以被转换成其他数据类型，比如整数、浮点数和字符串。在转换时，True 会被转换成 1，False 会被转换成 0。
在 Python 中，所有非零的数字和非空的字符串、列表、元组等数据类型都被视为 True，只有 0、空字符串、空列表、空元组等被视为 False。
'''
a = True
b = False

# 比较运算符
print(2 < 3)  # True
print(2 == 3)  # False

# 逻辑运算符
print(a and b)  # False
print(a or b)  # True
print(not a)  # False

# 类型转换
print(int(a))  # 1
print(float(b))  # 0.0
print(str(a))  # "True"

# 4、List（列表）
'''
列表是写在方括号 [] 之间、用逗号分隔开的元素列表。
列表同样可以被索引和截取,列表截取的语法格式如下：变量[头下标:尾下标]
加号 + 是列表连接运算符，星号 * 是重复操作
列表中的元素是可以改变的
'''
list1 = ['abcd', 786, 2.23, 'runoob', 70.2]
tinylist = [123, 'runoob']
print(list1)  # 输出完整列表,['abcd', 786, 2.23, 'runoob', 70.2]
print(list1[0])  # 输出列表第一个元素,abcd
print(list1[1:3])  # 从第二个开始输出到第三个元素,[786, 2.23]
print(list1[2:])  # 输出从第三个元素开始的所有元素,[2.23, 'runoob', 70.2]
print(tinylist * 2)  # 输出两次列表,[123, 'runoob', 123, 'runoob']
print(list1 + tinylist)  # 连接列表,['abcd', 786, 2.23, 'runoob', 70.2, 123, 'runoob']
print(list1[-1::-1])  # 翻转列表，第一个参数 -1 表示最后一个元素，第二个参数为空，表示移动到列表末尾，第三个参数为步长，-1 表示逆向

# 5、Tuple（元组）
'''
元组（tuple）与列表类似，不同之处在于元组的元素不能修改,元组写在小括号 () 里，元素之间用逗号隔开。
元组也可以被索引和切片，方法一样
元组也可以使用+操作符进行拼接。
'''
tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
tinytuple = (123, 'runoob')

print(tuple)  # 输出完整元组
print(tuple[0])  # 输出元组的第一个元素
print(tuple[1:3])  # 输出从第二个元素开始到第三个元素
print(tuple[2:])  # 输出从第三个元素开始的所有元素
print(tinytuple * 2)  # 输出两次元组
print(tuple + tinytuple)  # 连接元组
print(tuple.index(786))
# 6、Set（集合）,不能重复
'''
Python 中的集合（Set）是一种无序、可变的数据类型，用于存储唯一的元素。
集合中的元素不会重复，并且可以进行交集、并集、差集等常见的集合操作
在 Python 中，集合使用大括号 {} 表示，元素之间用逗号 , 分隔
也可以使用 set() 函数创建集合

'''
set1 = set()
print("空集合%s" % type(set1))
sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}
print(sites)  # 输出集合，重复的元素被自动去掉
# 成员测试
if 'Runoob' in sites:
    print('Runoob 在集合中')
else:
    print('Runoob 不在集合中')
# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
print("a,b中相同的元素%s" % a.intersection(b))
print("a与b的集合%s" % a.union(b))
print("a有b没有的%s" % a.difference(b))
print(a - b)  # a 和 b 的差集
print(a | b)  # a 和 b 的并集
print(a & b)  # a 和 b 的交集
print(a ^ b)  # a 和 b 中不同时存在的元素

s1 = {'1', 'b', 'c'}
l1 = [1, 2, 3, 4]
t1 = ('z', 'x', 'c', 'v', 'b')
s1.add('123')
print(s1)
s1.update(l1)
print(s1)
s1.update(t1)
print(s1)
s1.remove('123')
print(s1)
s1.pop()  # 随机删除，默认删除集合第一个元素
s1.discard('v')
print('*' * 30)
# 7、Dictionary（字典）
'''
字典（dictionary）是Python中另一个非常有用的内置数据类型。
列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
键(key)必须使用不可变类型,在同一个字典中，键(key)必须是唯一的。
'''
# 字典复制方式
dict1 = {}  # 定义空字典
dict1["one"] = '菜鸟'
dict1['two'] = '学习'
dict1['three'] = 'Python'
tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}

print(dict1)
print(tinydict)  # 输出完整的字典
print(tinydict.items())  #
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值
# print(tinydict[111])    # KeyError:报错
print(tinydict.get('name'))
del tinydict['name']  # key 不存在会报错
result = tinydict.pop('name', '不存在')
print(result)
dict2 = dict([(1, 2), (3, 4), (5, 6)])  # 列表转换为字典
print("dict2:{}".format(dict2))
for key in dict2:
    print(key)
for li in dict2.items():
    print(li)
for key, value in enumerate(dict2):
    print(key, value)

# 8、bytes 类型
'''
与字符串类型不同的是，bytes 类型中的元素是整数值（0 到 255 之间的整数），而不是 Unicode 字符。
bytes 类型通常用于处理二进制数据，比如图像文件、音频文件、视频文件等等。在网络编程中，也经常使用 bytes 类型来传输二进制数据。
此外，也可以使用 bytes() 函数将其他类型的对象转换为 bytes 类型。bytes() 函数的第一个参数是要转换的对象，第二个参数是编码方式，如果省略第二个参数，则默认使用 UTF-8 编码：
x = bytes("hello", encoding="utf-8")
bytes 类型也支持许多操作和方法，如切片、拼接、查找、替换等等
其中 ord() 函数用于将字符转换为相应的整数值
'''

b1 = b'hello'
print(b1)
print(type(b1))
