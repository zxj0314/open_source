from django.conf.urls import url

from App import views

urlpatterns = [
    url('^hello/', views.hello),
    url(r'^index/',views.index),
    url(r'^addstudent/',views.add_student),
    url(r'getstudents/',views.get_students),
    url(r'^delstudent/',views.del_student),
    url(r'^updatestudent/',views.update_student),
    url(r'^getstudentgrade/',views.get_student_grade),
    url(r'addpersons/',views.add_persons),
    url(r'addperson1/',views.add_person1),
    url(r'getpersons/',views.get_persons),
    url(r'getperson/',views.get_person),
    url(r'getorders/',views.get_orders),
    url(r'getgrade/',views.get_grade),
    url(r'getcustomer/',views.get_customer),
    url(r'getcompany/',views.get_company),
    url(r'getanimal/',views.get_animal),
]
