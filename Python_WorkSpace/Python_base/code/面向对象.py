'''
面向对象（OOP）是一种对现实世界理解和抽象的方法，对象的含义是指在现实生活中能够看得见摸得着的具体事物，一句比较经典的描述是一切皆对象，Python 是一门面向对象的语言，面向对象编程简单来说就是一种封装代码的方式。
面向对象相关概念
    类：描述具有相同属性和方法的集合，简单来说就是一个模板，通它来创建对象。
    对象：类的实例。
    方法：类中定义的函数。
    类变量：定义在类中且在函数之外的变量，在所有实例化对象中公用。
    局部变量：方法中定义的变量，只作用于当前实例。
面向对象三大特性
    封装：隐藏对象的属性和实现细节，仅对外提供公共访问方式，提高复用性和安全性。
    继承：一个类继承一个基类便可拥有基类的属性和方法，可提高代码的复用性。
    多态：父类定义的引用变量可以指向子类的实例对象，提高了程序的拓展性。

类
Python 中类的定义使用 class 关键字，语法如下所示：
class Cat:
    属性
    ...
    def __init__(self, name):
        self.name = name
    方法
    ...
对象
创建对象也称类的实例化，比如我们通过 Cat 类创建对象，如下所示：
 # 创建对象
c = Cat('Tom')
# 访问属性
print('name-->', c.name)
# 调用方法
c.eat('鱼')

继承
Python 支持类的继承，而且支持多继承，语法格式为：
class 基类(子类1, 子类2 ...):
    ...
'''


class Cat():
    # 类属性
    name = "花花"
    age = "3"

    # 类方法
    @classmethod
    def test(cls):
        print(cls)
        print(cls.name)  # 可以访问类属性
        # print(cls.color)    # 类方法不能访问对象的属性

    # 类初始化特征
    def __init__(self, name, color):
        self.name = name
        self.color = color

    #
    def eat(self, food):
        print(self)  # <__main__.Cat object at 0x000002C7C377FCC0>，self代表当前对象本身
        print(self.name, "正在吃", food)
        self.show()  # 调用类的同级方法

    def show(self):
        print(self.name, self.color)


# 创建对象
c1 = Cat('小黑', 'black')
print(c1)  # <__main__.Cat object at 0x000002C7C377FCC0>
print(c1.name)  # 调用类属性
c1.eat("老鼠")  # 给类方法传参
c1.show()
c1.test()
