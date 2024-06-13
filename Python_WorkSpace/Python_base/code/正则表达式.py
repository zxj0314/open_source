import re

# 替换
phone = re.sub(r'-', "", '024-7513354')
print(phone)


def double(matched):
    # print(type(matched.group('value')))   # <class 'str'>
    value = int(matched.group('value'))
    return str(value * 2)


s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))

result = re.match(r'<([0-9a-zA-Z]+)>(.+)</\1>', "<html>hello</html>")
print(result)
print(result.group(0))
print(result.group(1))
print(result.group(2))

result = re.match(r'<([0-9a-zA-Z]+)><([0-9a-zA-Z]+)>(.+)</\2></\1>', "<html><h2>hello</h2></html>")
print(result)
print(result.group(0))
print(result.group(1))
print(result.group(2))
print(result.group(3))

# 起名字方式
result = re.match(r'<(?P<name1>\w+)><(?P<name2>\w+)>(.+)</(?P=name2)></(?P=name1)>', "<html><h2>hello</h2></html>")
print(result)
print(result.group(0))
print(result.group(1))
print(result.group(2))
print(result.group(3))

# re.compile 函数练习
'''
re.I 忽略大小写
re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
re.M 多行模式
re.S 即为 . 并且包括换行符在内的任意字符（. 不包括换行符）
re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
re.X 为了增加可读性，忽略空格和 # 后面的注释
'''
pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)  # re.I 表示忽略大小写
m = pattern.match('Hello World Wide Web')
print(m)
print(m.span(0))  # (0, 11),返回匹配成功的整个子串的索引
print(m.span(1))  # (0, 5), 返回第一个分组匹配成功的子串的索引
print(m.span(2))  # (6, 11),返回第二个分组匹配成功的子串
print(m.group(1))  # 'Hello',返回第一个分组匹配成功的子串
print(m.group(2))  # 'World',返回第二个分组匹配成功的子串
print(m.groups())  # ('Hello', 'World'),等价于 (m.group(1), m.group(2), ...)
# print(m.group(3))       # Traceback (most recent call last):报错

# findall
pattern = re.compile(r'\d+')  # 查找数字
result1 = pattern.findall('runoob 123 google 456')
print(result1)  # ['123', '456']

result = re.findall(r'(\w+)=(\d+)', 'set width=20 and height=10')
print(result)  # [('width', '20'), ('height', '10')]

iter = re.finditer(r"\d+", "12a32bc43jf3")
print(iter)  # <callable_iterator object at 0x0000021098DC2978>
for match in iter:
    print(match.group())  # 12 32 43 3

sp = re.split('\W+', 'runoob, runoob, runoob.') # 匹配非字母数字及下划线
print(sp)   # ['runoob', 'runoob', 'runoob', '']
sp1 = re.split('(\W+)', ' runoob, runoob, runoob.')
print(sp1)      # ['', ' ', 'runoob', ', ', 'runoob', ', ', 'runoob', '.', '']
re.split('a*', 'hello world')   # 对于一个找不到匹配的字符串而言，split 不会对其作出分割


