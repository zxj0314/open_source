# 可迭代对象：生成器，列表、元组、集合、字典、字符串
from collections import Iterable

# 可迭代判断
list1 = [1, 2, 3, 4, 6, 7]
print(isinstance(list1, Iterable))  # 列表 True
print(isinstance('waedda', Iterable))  # 字符串 True
g = (x for x in range(10))  # 生成器 True
print(isinstance(g, Iterable))

'''
迭代器：迭代器是可以迭代的对象，这意味着您可以遍历所有值。
可被next()函数调用不断返回下一个值的对象成为迭代器：Iterator
迭代器的作用：
1、遍历容器中的元素：迭代器提供了一种逐个访问容器中元素的方法，可以遍历一个容器，访问其中的每个元素。
2、节省内存消耗：使用迭代器可以节省内存消耗，因为它只保存当前迭代的元素和迭代状态，而不是保存整个容器的数据。
3、实现惰性求值：迭代器采用的是延迟计算的方式，只有在需要时才会计算下一个元素，可以在处理大量数据时减少计算量。
4、处理无限序列：使用迭代器可以处理无限序列，因为它只需要在需要时生成下一个元素，而不需要一次性生成整个序列。
5、支持for循环：Python中for循环底层基于迭代器实现，因此，任何支持迭代的对象都可以用于 for 循环语句中。
6、处理流式数据：迭代器可以处理流式数据，比如网络数据、文件数据等，可以逐次读取大文件中的数据，或者逐次处理流式数据，而不必一次性将所有数据读入内存。
7、更加简洁的代码：使用迭代器可以减少代码的复杂度，提高代码的可读性和可维护性。因为迭代器提供了一种逐个访问元素的方法，可以避免使用复杂的控制流语句等。
迭代器机制的优点主要包括：
1、节省内存，提高效率。迭代器是一种惰性求值策略，只有在遍历过程中才返回真正需要的数据，避免了一次性读取全部数据带来的内存消耗和时间开销。
2、持无限序列处理。由于迭代器可以一次返回一个元素，因此对于很多无限序列（比如自然数序列）的遍历，使用迭代器可以实现简单高效的处理。
3、利于数据流处理。迭代器可以接受输入流的数据，逐一处理每一份数据，并适时输出处理结果，符合数据流“拉取式”处理的特点。

迭代器>可迭代的>生成器
'''

# 将可遍历的编程可迭代的:iter()
list1 = [1, 2, 3, 4, 6, 7]
list1 = iter(list1)
print(type(list1))  # <class 'list_iterator'>
print(next(list1))
print(next(list1))

# 使用内置函数： Python提供了一些内置函数，如 map()、filter()、zip() 等，它们返回的结果是迭代器。

# 使用 map() 创建迭代器
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x ** 2, numbers)

# 使用 filter() 创建迭代器
even_numbers = filter(lambda x: x % 2 == 0, numbers)

# 使用 zip() 创建迭代器
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
zipped_data = zip(names, ages)
# 文件迭代器： 文件对象本身也是一种迭代器，可以逐行读取文件内容。
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())
