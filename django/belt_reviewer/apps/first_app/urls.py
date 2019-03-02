from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index,name="index"),
    url(r'^process/$', views.process,name="process"),
    url(r'^login/$', views.login,name="login"),
    url(r'^books/$', views.books,name="books"),
    url(r'^create/$', views.create,name="create"),
    url(r'^create_book/$', views.create_book,name="create_book"),
    url(r'^show/$', views.show,name="show"),
    
    # url(r'^create_review/$', views.create_review,name="create_review"),
    url(r'^logout/$', views.logout,name="logout"),
   

   
]