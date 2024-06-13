'''
魔术方法：
所有以双下划线__包起来的方法，统称为Magic Method（魔术方法），它是一种的特殊方法，普通方法需要调用，而魔术方法不需要显示调用就可以执行。
__init__(self)  初始化方法
    触发机制：实例化对象之后立即触发
    参数：至少有一个self，接收当前对象，其他参数根据需要进行定义
    返回值：无
    作用：初始化对象的成员

__new__(cls) 构造方法
    触发时机： 实例化对象时自动触发（在__init__之前触发）
    参数：至少一个cls 接收当前类，其他参数根据初始化方法参数决定
    返回值：必须返回一个对象实例，没有返回值，则实例化对象的结果为None
    作用：实例化对象
    注意：实例化对象是Object类底层实现，其他类继承了Object的__new__才能够实现实例化对象。
__call__(self)  可调用对象魔术方法
    触发时机:将对象当作函数调用时触发,方式： 对象()
    参数:至少一个self接收对象，其余根据调用时参数决定
    返回值：根据情况而定
    作用：可以将复杂的步骤进行合并操作，减少调用的步骤，方便使用
    注意：无
__del__(self)   析构方法
    触发时机：当该类对象被销毁时，自动触发
    参数：一个self，接受当前对象
    返回值：无
    作用：关闭或释放对象创建时资源
    注意：del不一定会触发当前方法，只有当前对象没有任何变量引用时才会触发
    sys.getrefcount(p) 查看地址引用
    不建议手动修改，垃圾回收机制可能回收失败
__str__(self)
    需要对象转换为string时，python都会默认调用该魔法方法
    如print的时候，与字符串进行＋运算的时候，凡是需要进行隐示类型转换为字符串的地方，都会自动调用该方法。该方法返回一个字符串：
'''
import sys


class Person:
    def __init__(self, name):  # self接收__new__返回的结果 ret
        self.name = name
        print("我是init", self)  # 我是init <__main__.Person object at 0x0000018CDB4CFD30>

    def __new__(cls, *args, **kwargs):
        print("我是new()", cls)  # 我是new() <class '__main__.Person'>
        # 如果不在__new__方法里面调object的__new__方法就不会创建对象，__init__不会被执行；
        ret = super().__new__(cls)  # 调用父类object的__new__方法创建对象
        print(ret)  # <__main__.Person object at 0x0000018CDB4CFD30>
        # 如果不在__new__方法里面return创建好的对象，__init__不会被执行；
        return ret  # __new__魔术方法返回的就是self的内存地址

    # 将对象当作函数调用时重写此方法
    def __call__(self, name):
        print("我是call", self)  # <__main__.Person object at 0x0000018CDB4CFD30>
        print("我是call", name)

    def __del__(self):
        print("ohohoh，对象被销毁了")
        print("只要还有对象引用这个地址，执行结束就会自动出发销毁,否则全部执行结束调用")


p = Person("Jack")
print(p)  # <__main__.Person object at 0x0000018CDB4CFD30>
p("Jack")  # 将对象当作函数调用,自动调用__call__()
p1 = p
print("当前有几个对象引用", sys.getrefcount(p))
del p1
print("当前有几个对象引用", sys.getrefcount(p))
# del p
print("当前有几个对象引用", sys.getrefcount(p))  # NameError: name 'p' is not defined


class Dog(object):
    def __init__(self, name):  # self 是对象
        # 对象.属性名 = 属性值
        self.name = name

    def __str__(self):
        # 必须返回一个字符串
        return f"小狗的名字是{self.name}"


dog1 = Dog('aha')
print(dog1)
# str = 'Hello!' + dog1; #会提示TypeError
str = 'Hello!' + str(dog1)
print(f'{str}')