from django.db import models


class Grade(models.Model):
    g_name = models.CharField(max_length=16)


class Students(models.Model):
    s_name = models.CharField(max_length=16)
    s_grade = models.ForeignKey(Grade, on_delete=models.DO_NOTHING)

    # 类函数，在模板中调用显示类属性值
    def get_name(self):
        return self.s_name


class Student(models.Model):
    s_name = models.CharField(max_length=16)
    s_age = models.IntegerField(default=1)


class Person(models.Model):
    p_name = models.CharField(max_length=16, unique=True)
    p_age = models.IntegerField(default=0, db_column='age')
    # 默认男True，女False
    p_sex = models.BooleanField(default=True, db_column='sex')

    # 修改数据库表名
    class Meta:
        db_table = 'People'

    @classmethod
    def create(cls, p_name, p_age=0, p_sex=True):
        return cls(p_name=p_name, p_age=p_age, p_sex=p_sex)


# 订单模型，时间查询测试
class Order(models.Model):
    o_num = models.CharField(max_length=16, unique=True)
    o_time = models.DateField(auto_now_add=True)


class Customer(models.Model):
    c_name = models.CharField(max_length=16)
    c_cost = models.IntegerField(default=0)


# F对象，属性内的值比较
class Company(models.Model):
    c_name = models.CharField(max_length=16)
    c_boy_num = models.IntegerField(default=4)
    c_girl_num = models.IntegerField(default=7)


# 重写Manager的 get_queryset 方法；添加默认查询过滤条件
class AnimalManager(models.Manager):
    def get_queryset(self):
        return super(AnimalManager, self).get_queryset().filter(is_delete=False)


class Animals(models.Model):
    a_name = models.CharField(max_length=32)
    a_weight = models.IntegerField(default=1)
    is_delete = models.BooleanField(default=False)
    objects = AnimalManager()  #
