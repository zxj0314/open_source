# python 格式化输出

## 1. f 转化的格式化输出方式(3.6以后版本)

f-string 是 Python3.6 新增的一种字符串格式方法，由于前面已经介绍了多种格式化方式，大同小异，此处用简单的案例对其用法进行演示。

```python
只需要在我们要格式化输出的内容开头引号的前面加上 f ，在字符串内要转义的内容用 {} 括起来即可
模板 ： print(f'xxx{aa}xxx')
1、使用 f-string 方法在字符串中嵌入变量和表达式
name = "Python" # 字符串
ver = 3.6 # 浮点数
# 输出：Python-3.6、Python-3.7、Python-3.8000000000000003
print(f"{name}-{ver}、{name}-{ver + 0.1}、{name}-{ver + 0.2}")

2、在示例 1 中，表达式计算浮点数时发生溢出，可以使用特殊格式化修饰符限定只显示 1 位小数
name = "Python" # 字符串
ver = 3.6 # 浮点数
# 输出：Python-3.6、Python-3.7、Python-3.8
print(f"{name}-{ver}、{name}-{ver + 0.1}、{name}-{ver + 0.2:.1f}")

3、把十六进制数字 10 分别转换为用十进制、十六进制、八进制和二进制表示。
n = 0x10 # 十六进制数字10
# 输出：dec:16, hex:10, oct:16, bin:10000
print(f"dec:{n:d}, hex:{n:x}, oct:{n:0}, bin:{n:b}")


4、如果要在多行中表示字符串，可以使用下面示例方式，在每一行子串前面都加上 f 修饰符
name = "Python" # 字符串
ver = 3.6 # 浮点数
s = f"{name}-" \
 f"{ver}"
print(s) # 输出：Python-3.6
```

## 2、% 格式化输出的方法

同理，在我们要输出的字符串内将要转义内容，根据其数据类型和应用，用下面的符号代替即可,在字符串外面添加我们想要转出的内容即可
模板：print('xxx%sxxx' % a)

```python
转换说明符（Conversion Specifier）只是一个占位符，它会被后面表达式（变量、常量、数字、字符串、加减乘除等各种形式）的值代替。
中间的%是一个分隔符，它前面是格式化字符串，后面是要输出的表达式。
1、指定最小输出宽度
    %10d 表示输出的整数宽度至少为 10；
    %20s 表示输出的字符串宽度至少为 20。
2、指定对齐方式
默认情况下，print() 输出的数据总是右对齐的
    -    指定左对齐
    +    表示输出的数字总要带着符号；正数带+，负数带-。
    0    表示宽度不足时补充 0，而不是补充空格。
    对于整数，指定左对齐时，在右边补 0 是没有效果的，因为这样会改变整数的值。
    对于小数，以上三个标志可以同时存在。
    对于字符串，只能使用
    -标志，因为符号对于字符串没有意义，而补 0 会改变字符串的值。
3、指定小数精度
对于小数（浮点数），print() 还允许指定小数点后的数字位数，也即指定小数的输出精度。
精度值需要放在最小宽度之后，中间用点号
.隔开；也可以不写最小宽度，只写精度。具体格式如下：
    %m.nf
    %.nf
    m 表示最小宽度，n 表示输出精度，.是必须存在的。  

4、%()元组可以包含一个或多个值，如变量或表达式，用来向字符串中%操作符传递值，元组包含元素数量、顺序都必须与字符串中%操作符一一对应，否则将抛出异常。%()元组必须位于字符串的后面，否则无效。如果字符串中只包含一个%操作符，那么也可以直接传递值。例如：
str1 = "AmoXiang.length = %d" % len("AmoXiang")
print(str1) # 输出AmoXiang.length = 8

5、使用 print() 函数把数字输出为十六进制、十进制、八进制格式的字符串
num = 123
# 输出：Hex = 7b Dec = 123 Oct=173
print("Hex = %x Dec = %d Oct=%o" % (num, num, num))

6、把数字输出为不同格式的浮点数字符串
PI = 3.141592653
print("pi1 = %10.3f" % PI) # 总宽度为10，小数位精度为3
print("pi2 = %.*f" % (3, PI)) # *表示从后面的元组中读取3，定义精度
print("pi3 = %010.3f" % PI) # 用0填充空白
print("pi4 = %-10.3f" % PI) # 左对齐，总宽度10个字符，小数位精度为3
print("pi5 = %+f" % PI) # 在浮点数前面显示正号
```

% 在字符串中表示格式化操作符，它后面必须附加一个格式化符号，具体说明如下表所示

Python 支持多种格式化符号，每一种都代表着不同的[数据](https://www.finclip.com/news/tags-80.html)类型：

| 格式化符号 | 描述                           |
| ----- | ---------------------------- |
| %d    | 有符号整数（十进制）                   |
| %i    | 有符号整数（十进制）                   |
| %o    | 无符号整数（八进制）                   |
| %u    | 无符号整数（十进制）                   |
| %x    | 无符号整数（十六进制 - 小写）             |
| %X    | 无符号整数（十六进制 - 大写）             |
| %e    | 浮点指数格式（小写）                   |
| %E    | 浮点指数格式（大写）                   |
| %f    | 浮点数（用小数点表示）                  |
| %F    | 同上                           |
| %g    | 浮点数字（根据大小采用 %e 或者 %f）        |
| %G    | 浮点数字（根据大小采用 %E 或者 %F）        |
| %c    | 字符及其 ASII 码                  |
| %r    | 字符串（用 repr() 转换任何 Python 对象） |
| %s    | 字符串（用 str() 转换任何 Python 对象）  |
| %%    | 字符 %                         |

## 3、str.format() 格式化输出的方法

在我们要输出的字符串内将要转义内容，用 {} 代替，然后用 .format() 方法在括号里面传递我们想要输出的内容即可

模板 ： print('xxx{}xxx'.format(x,x))

```python
print("...{索引}, ... , {索引}, ...".format(值1, 值2))
#索引{}为空，默认按照顺序取值
print("...{key1}, ... , {key2}, ...".format(key1=value,key2=value))

name='xiaoming'
age=12
print('My name is {}, My age is {}'.format(name,age))
print('My name is {0}, My age is {1}'.format(name,age))
print('My name is {name}, My age is {age}'.format(name='xiaoming',age=12))
#输出：My name is xiaoming,My age is 12

1、顺序填值
>   右对齐
<   左对齐
^   中间对齐   print('我叫:{:0^10},年龄是:{:0<5}'.format(name,age))
对齐方式【<,>】,数据宽度【{:<10}】,补齐方式【{：0<5}】
print('{:>8}'.format('1')) # 总宽度为8，右对齐，默认空格填充
print('{:0>8}'.format('1')) # 总宽度为8，右对齐，使用0填充
print('{:a<8}'.format('1')) # 总宽度为8，左对齐，使用a填充

2、下标填值
print('我叫:{1},年龄是:{0}'.format(name,age))
```

| 模板                            | 输出结果                                                                                             |
| ----------------------------- | ------------------------------------------------------------------------------------------------ |
| {\:a<3} <样式型>                 | 用a填充满长度为3的字符串且转义的内容靠左(<^>分别表示靠左上右)                                                               |
| {\:f}      <功能型>              | 将我们的[数据类型转换](https://so.csdn.net/so/search?q=数据类型转换\&spm=1001.2101.3001.7020)成浮点类型的数据（默认保留小数后6位） |
| {:.a}   <样式型>                 | 控制浮点数据保留a位小数                                                                                     |
| {:+}    <样式型>                 | 用于显示数据的正负号                                                                                       |
| {\:e}    <功能型>                | 将数字转化成科学计数法的形式                                                                                   |
| {:%}   <功能型>                  | 将我们的数据转换成百分制的形式输出                                                                                |
| {\:b} {\:d} {\:o} {\:x} <功能型> | b、d、o、x 分别是二进制、十进制、八进制、十六进制                                                                      |

```python
位数与进制转换
#保留2位有效数字
print("{:.2f}".format(3.1415926))
#转成二进制
print('{0:b}'.format(16))
#转成八进制
print('{0:o}'.format(10))
#转成十六进制
print('{0:x}'.format(15)) 
输出
3.14
10000
12
f
1、格式化十进制整数
print(format(81, '8d')) # 8位整数显示，不足部分整数前用空格填充
print(format(81, '+d')) # 格式化为带符号整数显示数据
print(format(-81, '8d')) # 格式化为8位带符号整数显示，补位空格放到符号前
print(format(81, '=8d')) # 格式化为8位正整数，用空格补位
print(format(-81, '=8d')) # 格式化为8位负整数，不足部分在负号后填充
print(format(81, '+8d')) # 格式化为8位正整数，不足部分在符号前填充
print(format(-81, '8d')) # 格式化为8位负整数，不足部分在符号前填充
 
print(format(81, '>10')) # 右对齐，宽度为10个字符
print(format(81, '<10')) # 左对齐，宽度为10个字符
print(format(81, '010')) # 用0填充空格，宽度为10个字符
print(format(81, '@<10')) # 用“@”填充空格，宽度为10个字符
print(format(81, '@>10')) # 用“@”填充空格，宽度为10个字符
print(format(+81, '=10')) # 右对齐，宽度为10个字符
print(format(81, '0^10')) # 用0填充空格，宽度为10个字符
 
s = 125
print(format(s, '0>10')) # 右对齐，不足指定宽度部分用0填充
print(format(s, '>04')) # 右对齐，不足指定宽度部分用0填充
print(format(s, '*>10')) # 右对齐，不足指定宽度部分用“*”填充
print(format(s, '>010')) # 右对齐，指定0标志位填充
print(format(s, '>10')) # 右对齐，没指定填充值，用默认值空格填充
print(format(s, '+^30')) # 居中对齐，用“+”填充不足部分
print(format(s, '*<8')) # 右对齐，不足指定宽度部分用“*”填充
print(format(s, '08')) # 右对齐，指定0标志位填充

2、式化浮点数
print(format(628, '.1f')) # 格式化为保留1位小数的浮点数，输出：628.0
print(format(628, '.2f')) # 格式化为保留2位小数的浮点数，输出：628.00
print(format(3.14159, '.1f')) # 格式化为保留1位小数的浮点数，输出：3.1
print(format(3.14159, '.2f')) # 格式化为保留2位小数的浮点数，输出：3.14
print(format(3.14159, '.5f')) # 格式化为保留5位小数的浮点数，输出：3.14159
print(format(-3.14159, '.3f')) # 格式化为保留3位小数的浮点数，输出：-3.142
print(format(3.1415926535898, 'f')) # 默认精度保留6位小数，输出：3.141593
# 默认精度保留6位小数，不足部分用空格填充，输出：3.141590
print(format(3.14159, 'f'))
 
print(format(3.14159, '+.3f')) # 格式化为保留3位小数带符号的浮点数
print(format(3.14159, '>8.2f')) # 右对齐，保留2位小数
print(format(3.14159, '<10.2f')) # 左对齐，宽度为10，保留2位小数，不足部分用空格填充
print(format(3.14159, '<.3f')) # 左对齐，保留3位小数
print(format(3.14159, '@>10.3f')) # 右对齐，用“@”填充不足位置
print(format(-3.14159, '=10.2f')) # 格式化为保留2位小数的10位数，默认用空格填充
print(format(-3.14159, '0=10.2f')) # 格式化为保留2位小数的10位数，空格用0填充
print(format(3.14159, '0^10.2f')) # 保留2位小数的10位数，居中显示，空格用0填充

3、格式化百分数
print(format(0.161896, '%')) # 将小数格式化成百分数，输出：16.189600%
print(format(0.161896, '.2%')) # 格式化为保留2位小数的百分数，输出：16.19%
print(format(0.0238912, '.6%')) # 格式化为保留6位小数的百分数，输出：2.389120%
print(format(2 / 16, '.2%')) # 格式化为保留2位小数的百分数，输出：12.50%
print(format(3.1415926, '.1%')) # 格式化为保留1位小数的百分数，输出：314.2%
print(format(0.161896, '.0%')) # 格式化为保留整数的百分数，输出：16%
print(format(0.0238912, '8.6%')) # 格式化为保留6位小数的八位百分数，输出：2.389120%
print(format(0.0238912, '>8.3%')) # 格式化为保留3位小数的八位百分数，输出：2.389%

4、格式化科学记数法
#####e和E
print(format(3141592653589, 'e')) # 科学记数法，默认保留6位小数，输出：3.141593e+12
print(format(3.14, 'e')) # 科学记数法，默认保留6位小数，输出：3.140000e+00
print(format(3.14, '0.4e')) # 科学记数法，默认保留4位小数，输出：3.1400e+00
print(format(3141592653589, '0.2e')) # 科学记数法，保留2位小数，输出：3.14e+12
print(format(3141592653589, '0.2E')) # 科学记数法，保留2位小数，采用大写E表示，输出：3.14E+12
#####g和G
print(format(3.14e+1000000, 'F')) # 无穷大转换成大写字母，输出：INF
print(format(3141592653589, 'g')) # 科学记数法，保留2位小数，输出：3.14159e+12
print(format(314, 'g')) # 科学记数法，保留2位小数，输出：314
print(format(3141592653589, '0.2g')) # 科学记数法，保留2位有效数字，采用小写e表示，输出：3.1e+12
print(format(3141592653589, 'G')) # 科学记数法，保留5位小数，采用大写E表示，输出：3.14159E+12
print(format(3.14e+1000000, 'g')) # 小数点计数法，无穷大转换成小写字母，输出：inf

5、格式化金额
print('$' + format(1201398.2315, '.2f')) # 添加美元符号，小数保留2位
print(chr(36) + format(1201398.2315, '.2f')) # ASCII码添加美元符号，小数保留2位
print('¥' + format(78088888, ',')) # 添加人民币符号，用千位分隔符区分金额
print('£' + format(7908.2315, '.2f')) # 添加英镑符号，用千位分隔符进行区分
print('€' + format(7908.2315, ',.2f')) # 添加欧元符号，保留两位小数，千位分隔
print(chr(0x20ac) + format(1201398.2315, ',f')) # 使用十六进制编码添加欧元符号
6、格式化字符
print(format('PYTHON', 'M^20.3')) # 截取3个字符，宽度为20居中，不足用M填充
print(format("PYTHON", '10')) # 默认居左显示，不足部分用空格填充
print(format('blog.csdn.net', '.3')) # 截取3个字符，默认居左显示
print(format("PYTHON", '>10')) # 居右显示，不足部分用空格填充
s = 'blog.csdn.net'
print(format(s, '0>20')) # 右对齐，不足指定宽度部分用0填充
print(format(s, '>4')) # 右对齐，因字符实际宽度大于指定宽度4，不用填充
print(format(s, '*>20')) # 右对齐，不足指定宽度部分用*填充
print(format(s, '>020')) # 右对齐，指定0标志位填充
print(format(s, '>20')) # 右对齐，没指定填充值，用默认值空格填充
print(format(s, '+^30')) # 居中对齐，用+填充不足部分

6、进制转换
b：二进制。将数字以 2 为基数进行输出。d：十进制整数。将数字以 10 为基数进行输出。o：八进制。将数字以 8 为基数进行输出。x：十六进制。将数字 以16 为基数进行输出，9 以上的数字用小写字母。
十进制、十六进制、八进制、二进制的转换代码如下：
print(format(77)) # 格式参数为空，默认为十进制
print(format(77, 'd')) # 原来是十进制数，转换后为原值
print(format(-77, 'd')) # 原来是十进制数，转换后为原值
print(format(77, '8d')) # 转换为8位十进制数，空余部分用空格填充
print(format(-77, '8d')) # 转换为8位十进制数，负数在负号前填充空余部分空格
print(format(77, '+8d')) # 转换为8位带符号十进制数，在符号前填充空余部分空格
print(format(-77, '08d')) # 转换为8位十进制数，负数在负号前填充空余部分空格
print(format(77, '+08d')) # 转换为8位带符号十进制数，在符号前填充空余部分空格
print(format(-77, '#8d')) # 转换为8位十进制数，加进制标志
print(format(-77, '=8d')) # 转换为8位十进制数，空余部分填充空格
print(format(+77, '=8d')) # 转换为8位十进制数，空余部分填充空格
print(format(+77, '*=8d')) # 转换为8位十进制数，空余部分填充*
print(format(+77, '*=+8d')) # 转换为8位带符号十进制数，符号与数据之间填充*
print(format(-77, '#=8d')) # 转换为8位十进制数，在符号与空余部分填充#
print(format(+77, '*<8d')) # 转换为8位十进制数，左对齐，空余部分填充*
print(format(-77, '#>8d')) # 转换为8位十进制数，右对齐，空余部分填充#
print(format(0X5A, 'd')) # 十六进制数5A转换成十进制数，0X代表十六进制数
print(format(0B011101, '+8d')) # 二进制数011101转换成十进制数，0B代表二进制数
print(format(0O34, 'd')) # 八进制数34转换成十进制数，0O代表八进制数
print(format(0O123456, '08d')) # 十六制数123456转换成十进制数，不足用0填充
print(format(+0X1234, '*>8d')) # 十六进制数1234转换成十进制数，右对齐，不足用*

对于带有进制前缀的数，如 0x、0o、0b，可以直接在后面加上 x、o、b 进行删除。

print(format(0X5A, 'x')) # 去除十六进制数的前缀，输出：5a
print(format(0B011101, 'b')) # 去除二进制数的前缀，输出：11101
print(format(0O34, 'o')) # 去除八进制数的前缀，输出：34
```

7、格式化日期

format() 函数也可以对日期和时间进行格式化，格式化时可以通过日期和时间格式符号进行设置，Python 中常用的时间日期格式化符号如表所示。

| %y | 两位数的年份表示（00-99）    | %B | 本地完整的月份名称               |
| -- | ------------------ | -- | ----------------------- |
| %Y | 四位数的年份表示（000-9999） | %c | 本地相应的日期表示和时间表示          |
| %m | 月份（01-12）          | %j | 年内的一天（001-366）          |
| %d | 月内中的一天（0-31）       | %p | 本地A.M.或P.M.的等价符         |
| %H | 24小时制小时数（0-23）     | %U | 一年中的星期数（00-53）星期天为星期的开始 |
| %I | 12小时制小时数（01-12）    | %w | 星期（0-6），星期天为星期的开始       |
| %M | 分钟数（00-59）         | %W | 一年中的星期数（00-53）星期一为星期的开始 |
| %S | 秒（00-59）           | %x | 本地相应的日期表示               |
| %a | 本地简化星期名称           | %X | 本地相应的时间表示               |
| %A | 本地完整星期名称           | %Z | 当前时区的名称                 |
| %b | 本地简化的月份名称          | %% | %号本身                    |

```python
import datetime
 
now = datetime.datetime.now()
print(format(now, '%Y-%m-%d %H:%M:%S %A')) # 当前时间格式化为年-月-日+完整英文星期
print(format(now, '%Y-%m-%d %H:%M:%S %a')) # 当前时间格式化为年-月-日+简写英文星期
# 中文年-月-日显示
print(format(now, '%Y'), '年', format(now, '%m'), '月', format(now, '%d'), '日')
# 中文时间显示
print(format(now, '%H'), '年', format(now, '%M'), '分', format(now, '%S'), '秒')
print(format(now, '%Y-%m-%d %H:%M:%S %a')) # 当前时间格式化为年-月-日+简写英文星期
print(format(now, '%Y-%m-%d')) # 当前时间格式化为标准年-月-日
print(format(now, '%y-%m-%d')) # 当前时间格式化为短日期年-月-日
print(format(now, '%Y<%m>%d')) # 当前时间格式化为长日期年-月-日，间隔符为“<”和“>”
print(format(now, '%c')) # 本地对应的年-月-日星期表示
 
print(format(now, '%B')) # 本地完整的月份表示，输出：May
print('现在是今年第', format(now, '%j'), '天') # 今天是一年中第几天，输出：现在是今年第 017 天
print('本周是今年第', format(now, '%U'), '周') # 本周是一年中第几周，输出：本周是今年第 02 周
print(format(now, '%y%m%d')) # 无间隔符短日期格式年月日，输出：210117
print(format(now, '%Y-%m')) # 长日期格式年-月，输出：2021-01
print(format(now, '%m-%d')) # 月-日显示，输出：01-17
print(format(now, '%m')) # 月份单独显示，输出：01
print(format(now, '%d')) # 日期单独显示，输出：17
 
print(format(now, '%H%M%S')) # 无间隔符，输出：133536
print(format(now, '%H:%M:%S')) # 标准时-分-秒，输出：13:35:36
print(format(now, '%I:%M:%S %I')) # 12小时制时-分-秒，输出：01:35:36 01
print(format(now, '%H:%M')) # 时+分，输出：13:35
print(format(now, '%M%S')) # 分+秒，输出：3536
print(format(now, '%H')) # 只显示小时，输出：13
print(format(now, '%H:%M:%S %p')) # 日期显示按AM，PM显示，输出：13:35:36 PM
print(format(now, '%a')) # 英文星期简写，输出：Sun
print(format(now, '%A')) # 英文星期完整显示，输出：Sunday
week = ['星期日', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六']
print(week[int(format(now, '%w'))]) # 中文星期，输出：星期日
 
dt = datetime.datetime(2020, 5, 9)
dm = datetime.datetime(2020, 5, 9, 12, 50, 20)
# 将输入的日期按年-月-日和时间格式化，因时间没有输入，按0时处理
print(format(dt, '%Y-%m-%d %H:%M:%S'))
print(format(dt, '%Y-%m-%d')) # 将输入的日期按年-月-日格式化
print(format(dm, '%Y-%m-%d %H:%M:%S')) # 将输入的日期按年-月-日和时间格式化
print(format(dm, '%Y-%m-%d')) # 将输入的日期按年-月-日格式化
 
wx = datetime.datetime.now()
print(str(wx), format(1, '0>3')) # 年-月-日 +3位编号
print(format(now, '%Y-%m-%d'), format(1, '0>3')) # 年-月-日 +3位编号
print(format(now, '%Y%m%d'), 'NO' + format(1, '0>3')) # 年-月-日 +NO+3位编号
print(format(now, '%d'), 'NO' + format(1, '0>3')) # 日期 +NO+3位编号
print(format(now, '%H%M'), 'NO' + format(1, '0>3')) # 时钟+分 +NO+3位编号
```

**填充对齐**

```python
# 先取到值,然后在冒号后设定填充格式：{索引:[填充字符][对齐方式][宽度]}
# *<20：左对齐，总共20个字符，不够的用*号填充
print('{0:*<20}'.format('hellopython'))
# *>20：右对齐，总共20个字符，不够的用*号填充
print('{0:*>20}'.format('hellopython'))
# *^20：居中显示，总共20个字符，不够的用*号填充
print('{0:*^20}'.format('hellopython'))
输出：
hellopython*********
*********hellopython
****hellopython*****

s = "PYTHON"
print(format(s, '10')) # 没有标志符，如果是字符串则默认左对齐，不足宽度部分默认用空格填充
print(format(13.14, '10')) # 没有标志符，如果是数字则默认右对齐，不足宽度部分默认用空格填充
print(format(s, '0>10')) # 右对齐，不足指定宽度部分用0填充
print(format(s, '>04')) # 右对齐，因字符实际宽度大于指定宽度4，不用填充
print(format(s, '*>10')) # 右对齐，不足部分用"*"填充
print(format(s, '>010')) # 右对齐，不足部分用0填充
print(format(s, '>10')) # 右对齐，默认用空格填充
print(format(s, '<10')) # 左对齐，默认用空格填充
print(format(s, '<010')) # 左对齐，不足部分用0填充
print(format(s, '@^10')) # 中间对齐，不足部分用'@'填充，宽度为10个空格
print(format(13.14, '0<10')) # 左对齐，不足部分用0填充
print(format(13.14, '@^10')) # 中间对齐，不足部分用@填充
print(format(13.14, '0>10')) # 右对齐，不足部分用0填充
print(format(-13.14, '0=10')) # 右对齐，符号后面不足部分用0填充
```

