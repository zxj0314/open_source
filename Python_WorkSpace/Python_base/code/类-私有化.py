# 类变量私有化
'''
私有化属性
    私有化属性只需要以双下划线开头，声明该属性为私有属性即可，声明之后就不能在类外部使用或直接访问。
    不能在类外面访问
    可以在类里面访问，修改
    子类不能继承私有化属性
set和get
    set是为了赋值，给私有化属性赋值。
    get是为了取值，把私有化属性的值取出来
私有化好处：
    隐藏属性不被外界随意修改(在set里面加一些判断，防止被随意修改)
    也可以修改，通过函数完成
    如果想获取具体的某一个属性，使用get函数来完成
    通过装饰器，就可以让私有属性当作属性一样去调用。
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,age):
        self.__age = age

'''


class Student:
    def __init__(self):
        self.__age = 18
        self.__name = "无名氏"
        self.__score = 0

    def __str__(self):
        return "姓名：" + self.__name + "，年龄：" + str(self.__age) + "，分数" + str(self.__score)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def setAge(self, age):
        # 私有化可以增加判断
        if age > 0 and age < 120:
            self.__age = age
        else:
            print("年龄不在范围内")
            # return "复制失败"

    def getAge(self):
        print(self.__age)


if __name__ == '__main__':
    s = Student()
    print(s)
    s.setAge(20)
    print(dir(s))  # 打印对象可调用的属性
    print(s.__dir__())
    s.name="小黑"
    print(s)
    print(s._Student__name)