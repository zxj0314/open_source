from django.conf.urls import url

from Template import views

urlpatterns=[
    url(r'HelloTemplate/',views.HelloTemplate),
    url(r'index/',views.index),
    url(r'getstudents/',views.get_students),
    # 模板继承
    url(r'home/',views.home),
]