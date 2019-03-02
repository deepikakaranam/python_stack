from django.conf.urls import url
from . import views 


urlpatterns = [
    url(r'^$', views.index,name="index"),
    url(r'^process/$', views.process,name="process"),
    url(r'^login/$', views.login,name="login"),
    url(r'^dashboard/$', views.dashboard,name="dashboard"),
    url(r'^(?P<id>\d+)/add/$', views.add,name="add"),
    url(r'^add_job/$', views.add_job,name="add_job"),
    url(r'^create_job/$', views.create_job,name="create_job"),
    url(r'^(?P<id>\d+)/view_job/$', views.view_job,name="view_job"),
    url(r'^(?P<id>\d+)/edit_job/$', views.edit_job,name="edit_job"),
    url(r'^(?P<id>\d+)/delete_job/$', views.delete_job,name="delete_job"),
    url(r'^(?P<id>\d+)/update/$', views.update,name="update"),
    url(r'^logout/$', views.logout,name="logout"),
]