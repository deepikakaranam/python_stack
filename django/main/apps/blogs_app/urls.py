from django.conf.urls import url
from . import views  


urlpatterns = [
    url(r'^$', views.index) ,
    url(r'^new/$', views.new),
    url(r'^new/(?P<number>\d+)/$', views.add_number),
    url(r'^new/(?P<number>\d+)/edit$', views.edit),
    url(r'^new/(?P<number>\d+)/delete$', views.destroy),
    url(r'^create/$', views.create)
    
    


]