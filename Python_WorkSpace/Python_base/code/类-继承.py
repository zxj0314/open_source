# 类的继承
'''


'''


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + "正在吃饭")


class Student(Person):
    def __init__(self, name, age, clazz):
        super().__init__(name, age)
        self.clazz = clazz

    def study(self):
        print("{}正在学习{}".format(self.name, self.clazz))


class Employee(Person):
    def __init__(self, name, age, salary, compony):
        super().__init__(name, age)

    # 重写父类的方法,调用时，先找自己再找父类
    def eat(self):
        print("{}正在吃饭，喜欢吃红烧狮子头".format(self.name))


class Doctor(Person):
    def __init__(self, name, age, patients):
        super(Doctor, self).__init__(name, age)

    def eat(self, food):
        super().eat()  # 有需求先执行父类在执行子类
        print("{}正在吃饭，喜欢吃{}".format(self.name, food))


s = Student("小明", 8, "英语")
s.eat()
s.study()
e = Employee("肖恩", 22, 3000, "小米")
e.eat()
d = Doctor("肖恩", 23, ["a", "b", "c"])
d.eat("煎饼果子")
