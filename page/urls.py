from django.conf.urls import  url
from page import views
urlpatterns = [

                       url(r'^(?P<cat_id>[0-9])+/$', views.index, name ='index'),
                       url(r'^good/(?P<good_id>\d+)/$', views.good, name = 'good'),
                       url(r'^categorys/$', views.categorys, name= 'categorys'),
                       ]
