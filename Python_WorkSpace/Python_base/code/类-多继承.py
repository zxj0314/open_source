# 类的多继承
class Base:
    def test(self):
        print("----------Base-------------")


class A(Base):
    def test(self):
        print("---------------AAAAAAAAAA")


class B(Base):
    def test(self):
        print("---------------BBBBBBBBBB")


class C(Base):
    def test(self):
        print("---------------CCCCCCCCCC")


class D(A, B, C):
    pass


# c = C()
# c.test()

d = D()
d.test()  # ---------------AAAAAAAAAA
# 查看继承顺序,根据继承时填写的顺序一直
import inspect

print(inspect.getmro(D))  # (<class '__main__.D'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.Base'>, <class 'object'>)
print(D.__mro__)

# 多继承搜索顺序
# py2 经典类是按深度优先来继承的，新式类是按广度优先来继承的。
# py3 经典类和新式类都是统一按广度优先来继承的。
# 深度优先遍历是从 D 开始往上搜索到 B，若 B 没有数据，则继续往上搜索到 A；
# 广度优先遍历是从 D 开始往上搜索到 B，若 B 没有数据，则搜索和 B 同级的 C 里的数据，若同级的 C 里还是没有数据，再继续往上搜索到 A 。
