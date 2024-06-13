from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from App.models import Students


def HelloTemplate(request):
    return HttpResponse("<h1/>Hello Template</h1>")


# 模版手动渲染
def index(request):
    # return render(request,'index.html')
    temp = loader.get_template('index.html')
    content = temp.render()
    return HttpResponse(content)


def get_students(request):
    students = Students.objects.all()
    # 当查询为空时，for循环显示为空，使用empty设置默认值
    # students = Students.objects.all().filter(s_name='Socker')
    # for循环中使用forloop.counter可以显示第几次循环
    # for 循环中forloop.first 判断第一个;forloop.last判断最后一个,对其进行操作
    # ifequal 等于比较  { % ifequal forloop.counter 5 %} < listyle = "color: #00ffff" > {{student.get_name}} </li> { % endifequal %}
    # 过滤器 |
    # 单行注释 {# 注释 #}
    # 多行注释 comment
    '''
    {% comment %}
        - 乘除
        {% widthratio 数 分母 分子 %}
        <h4>计算{{ count }}</h4>
        <h4>乘法：{% widthratio  count 1 5 %}</h4>
        <h4>除法：{% widthratio  count 5 1 %}</h4>
        <h4>整除：{% if forloop.counter|divisibleby:2 %} 
        # ifequal 等于比较  { % ifequal forloop.counter 5 %} < listyle = "color: #00ffff" > {{student.get_name}} </li> { % endifequal %}
        <h4>加法：{{ count | add:2  }}</h4>
        <h4>减法：{{ count | add:-2  }}</h4>
        <h3>转换成小写{{ students.0.s_name|lower }}</h3>
        <h3>转换成大写{{ students.0.s_name|upper }}</h3>
        拼接    {{student | join '='}}
        赋值    {{ var | default "cat" }}
        被整除    {% if forloop.counter|divisibleby:2 %}
        日期时间格式化 {{ datevalue | date'yy-mm-dd'}}
    {% endcomment %}
    '''
    context = {
        'students': students,
        'socks': 56,
        'link': "<a href='https://wwww.baidu.com'>百度</a>",
    }
    return render(request, 'Students.html', context=context)


# 模板继承
def home(request):
    return render(request, 'home.html', context={'title':'home'})
