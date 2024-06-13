# 类方法操作
'''
静态方法：
    静态方法不需要传递参数(cls，self)
    类方法和静态方法是在对象创建之前执行的
    只能访问类的属性和方法，对象无法访问


'''
class Person:
    __age = 1  # 私有变量

    # 类函数修改私有变量
    @classmethod
    def update_age(cls, age):
        cls.__age = cls.__age + age

    @classmethod
    def show_age(cls):  # 类方法显示私有变量
        print("修改后的年龄是", cls.__age)

    @staticmethod  # 静态方法
    def static_func():
        print("静态方法")
        # print(cls.__age)    # 语法错误
        print(Person.__age)


p1 = Person()
p1.update_age(2)    # 对象创建就已经执行了类方法
p1.show_age()
print("------------------>")
Person.update_age(3)
Person.show_age()
Person.static_func()
