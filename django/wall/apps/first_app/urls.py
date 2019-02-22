from django.conf.urls import url
from . import views 


urlpatterns = [
    url(r'^$', views.index),
    url(r'process/$', views.process),
    url(r'login/$', views.login),
    url(r'wall/$',views.wall),
    url(r'message/$', views.message),
    url(r'(?P<id>\d+)/comment/$', views.comment),
    url(r'logout/$', views.logout)


]