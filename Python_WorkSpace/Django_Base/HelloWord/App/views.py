import random

from django.db.models import Max, Avg, F, Q
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from App.models import Student, Students, Grade, Person, Order, Customer, Company, Animals


def hello(request):
    return HttpResponse("<h1>Hello</h1>")


# HTML渲染
def index(request):
    index = loader.get_template('index.html')
    # 传参
    context = {
        "students": Student.objects.all(),
    }
    result = index.render(context=context)
    # print(result)
    return HttpResponse(result)


def add_student(request):
    student = Student()
    student.s_name = 'Suwei%d' % random.randint(0, 100)
    student.s_age = 8
    student.save()
    return HttpResponse("add Success%s" % student.s_name)


def get_students(request):
    students = Student.objects.all()
    # for student in students):
    #     print(student.s_name)
    # return HttpResponse("获取成功")
    context = {
        'title': "Student List",
        # 'students': Student.objects.all(),
        'students': students
    }
    return render(request, 'Studentlist.html', context=context)


def del_student(request):
    student = Student.objects.get(pk=1)
    student.delete()
    student.save()
    return HttpResponse("删除成功")


def update_student(request):
    student = Student.objects.get(pk=28)
    student.s_name = "Jack"
    student.save()
    return HttpResponse("update success")


# django shell 调试   > python manage.py shgell
'''
> python manage.py shgell
>>> from App.models import Student
>>> students = Student.objects.all()
>>> for st in students:
...     print(st.s_name)
'''


def get_student_grade(request):
    # 通过学生获取学生所在的班级
    student = Students.objects.get(pk=1)
    sgrade = student.s_grade
    # 通过班级找学生
    grade = Grade.objects.get(pk=1)
    gstudents = grade.students_set.all()
    studentlist = []
    for s in gstudents:
        print(s.s_name)
        studentlist.append(s.s_name)
    return HttpResponse("<h2>Student grade is: {}</h2>\n<h2>1班的学生有：{}</h2>".format(sgrade.g_name, studentlist))


def add_persons(request):
    for i in range(15):
        person = Person()
        flag = random.randrange(100)
        person.p_name = "Tom%d%i" % (flag, i)
        print(person.p_name)
        person.p_age = flag
        person.p_sex = flag % 2
        person.save()
    return HttpResponse("add Person success")


def get_persons(request):
    gtpersons = Person.objects.filter(p_age__gt=18)
    expersons = Person.objects.exclude(p_age__lt=30).order_by('p_age')  # 默认id
    # print(expersons.values())
    for person in expersons.values():
        print(person)
    context = {
        "gtperson": gtpersons,
        "expersons": expersons,
    }
    return render(request, 'person.html', context=context)


def add_person1(request):
    # 添加用户
    # person1 = Person.objects.create(p_name='Jack', p_age=18, p_sex=1)
    # person1.save()
    person = Person.create('skad')
    print("===============================", person.p_name)
    person.save()
    return HttpResponse("添加skad成功")


def get_person(request):
    # person = Person.objects.get(p_age=55)   # 找不到时会报错，DoesNotExist
    # person = Person.objects.get(p_age=40)   # 找到多个也报错，App.models.Person.MultipleObjectsReturned:
    person_first = Person.objects.all().first()
    print(person_first.p_name)
    person_last = Person.objects.all().last()
    print(person_last.p_name)
    # first和last 隐藏bug，会存在获取第一个和最后一个一样情况，解决显示或方法手动排序

    person = Person.objects.filter(p_age=40)
    if person.count():  # 判断用户个数
        print("用户存在")
    else:
        print("用户不存在")
    if person.exists():  # 判断用户是否存在
        print("用户存在")
    else:
        print("用户不存在")
    return HttpResponse("获取成功")


def get_orders(request):
    # Django 时区问题，解决方法1关闭Django中的自定义时区；解决方法2在数据库中创建对应的时区表
    # orders = Order.objects.filter(o_time__year=2024)  # 查询年没有问题
    # orders = Order.objects.filter(o_time__month=8)  # 查询月高版本也没问题
    # orders = Order.objects.filter(o_time__day=5)  # 查询日高版本也没问题
    # orders = Order.objects.filter(o_time__lte='2023-09-05')
    orders = Order.objects.filter(o_time__week_day=2)
    for order in orders:
        print(order.o_num)
    return HttpResponse("获取成功")


# 通过学生查班级
def get_grade(request):
    grades = Grade.objects.filter(students__s_name='luli')
    print(type(grades.values()))
    for grade in grades:
        print(grade.g_name)
    return HttpResponse("获取成功")


# aggregate()练习
# 'Avg 平均, Count 数量, Max 最大, Min 最小, StdDev, Sum 求和, 'Variance','Aggregate',
def get_customer(request):
    # result = Customer.objects.aggregate(Max('c_cost'))    # 获取最大值
    result = Customer.objects.aggregate(Avg('c_cost'))
    print(result)
    return HttpResponse("返回成功")


def get_company(request):
    # F对象
    # 直接比较模型AB两个属性
    # companies = Company.objects.filter(c_boy_num__lt=F('c_girl_num'))   # 获取男生比女生少的公司名称
    # companies = Company.objects.filter(c_boy_num__lt=F('c_girl_num')-1)   # 获取男生比女生少3个的公司名称
    # Q对象
    # 封装条件，支持逻辑条件 & and; | or; ~ 取反
    # companies = Company.objects.filter(c_boy_num__gt=1).filter(c_girl_num__gt=5)
    companies = Company.objects.filter(Q(c_boy_num__gt=1) & Q(c_girl_num__lt=6))
    for company in companies:
        print(company.c_name)
    return HttpResponse("获取成功")


def get_animal(request):
    animals = Animals.objects.all()
    for animal in animals:
        print(animal.a_name)
    return HttpResponse("获取动物成功")