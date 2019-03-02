from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^signin/$', views.signin, name="signin"),

    url(r'^login/$', views.login, name="login"),
    url(r'^register/$', views.register, name="register"),
    url(r'^process/$', views.process, name="process"),
    url(r'^success/$', views.success, name="success"),

   
]