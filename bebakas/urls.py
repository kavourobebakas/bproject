from django.conf.urls import url, include
from bebakas import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^bproject/whoisthat/$', views.slide1),
    url(r'^bproject/me/$', views.slide2),
    url(r'^bproject/emmanuela/$', views.nope),
    url(r'^bproject/code2/$', views.code2),
    url(r'^bproject/macube/$', views.slide3),
    url(r'^bproject/code3/$', views.code3),
    url(r'^bproject/damnwerehot/$', views.slide4),
    url(r'^bproject/code4/$', views.code4),
    url(r'^bproject/hero/$', views.slide5),
    url(r'^bproject/code5/$', views.code5),
    url(r'^bproject/almost/$', views.slide6),
    url(r'^bproject/code6/$', views.code6),
    ]
