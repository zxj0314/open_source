# 字符串格式化
'''
python字符串格式化符号:
%c	 格式化字符及其ASCII码
%s	 格式化字符串
%d	 格式化整数
%u	 格式化无符号整型
%o	 格式化无符号八进制数
%x	 格式化无符号十六进制数
%X	 格式化无符号十六进制数（大写）
%f	 格式化浮点数字，可指定小数点后的精度
%e	 用科学计数法格式化浮点数
%E	 作用同%e，用科学计数法格式化浮点数
%g	 %f和%e的简写
%G	 %f 和 %E 的简写
%p	 用十六进制数格式化变量的地址
--------------------------------------
格式化操作符辅助指令:
*	    定义宽度或者小数点精度
-	    用做左对齐
+	    在正数前面显示加号( + )
<sp>	在正数前面显示空格
#	    在八进制数前面显示零('0')，在十六进制前面显示'0x'或者'0X'(取决于用的是'x'还是'X')
0	    显示的数字前面填充'0'而不是默认的空格
%	    '%%'输出一个单一的'%'
(var)	映射变量(字典参数)
m.n.	m 是显示的最小总宽度,n 是小数点后的位数(如果可用的话)
'''
# 例1
print("我叫 %s 今年 %d 岁!" % ('小明', 10))

# 例2
# f-string 是 python3.6 之后版本添加的，称之为字面量格式化字符串，是新的格式化字符串的语法。
# f-string 格式化字符串以 f 开头，后面跟着字符串，字符串中的表达式用大括号 {} 包起来，它会将变量或表达式计算后的值替换进
name = 'Runoob'
str1 = f'Hello {name}'  # 替换变量
print(str1)
print(f'{1 + 2}')  # 使用表达式
w = {'name': 'Runoob', 'url': 'www.runoob.com'}
print(f'{w["name"]}: {w["url"]}')  # 用了这种方式明显更简单了，不用再去判断使用 %s，还是 %d。

# 例3
name = '乔治'
age = 18
money = '1亿'
print('{}今年{}了，拥有{}压岁钱'.format(name, age, money))
print('{name}今年{age}了，拥有{money}压岁钱'.format(age=10, name='乔恩', money='1万'))
print("我叫{1}，来自{2}，今年{0}岁".format(15,"小王","天津"))
print("我来自{0}，我今年{1}岁了,我来自{0}".format("东北",'15'))

'''
{:b}	将数字用二进制表示
{:c}	将整数转换为对应的Unicode字符串
{:d}	将数字用十进制整数表示（format中相应内容应是整数）
{: o}	将数字用八进制表示
{:x}	将数字用十六进制表示
{:f}	将数字用浮点数表示
{:e}	将数字用科学计数法表示
{:%}	将数字用百分数表示
{:，}	用逗号分隔数字
{:.3f}	保留三位小数
{:.2%}	将数字用百分数表示，且小数点后保留两位小数
'''
print("我{:>5d}岁了".format(32))  # 5个数字，右对齐，缺失用空格填充
## 我   32岁了
print("我{:0>5d}岁了".format(32))  # 5个数字，右对齐，缺失用0填充
## 我00032岁了
print("我的存款为{:.2f}元".format(12345))  # 保留两位小数
## 我的存款为12345.00元
print("本季度利润为{:.3f}元".format(1456.265897))  # 保留三位小数
## 本季度利润为1456.266元
print("你排名前{:.2%}".format(0.354))  # 百分比形式，保留两位小数
## 你排名前35.40%
print("我的存款为{:.2e}元".format(12345))  # 科学计数法并保留两位小数
## 我的存款为1.23e+04元
print("本季度利润为{:,}元".format(1456265.897))  # 用逗号分隔数字
## 本季度利润为1,456,265.897元



# 对其方式
print("我是{0:>5}，来自{1:*^6}".format("小王","天津"))       # 我是   小王，来自**天津**