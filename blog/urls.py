from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^home2/$', views.home2, name='home2'),
    url(r'^ab/$', views.ab, name='about'),
    url(r'^home2/ab2/$', views.ab2, name='about2'),
    url(r'^join/$', views.join, name='join'),
    url(r'^log/$', views.log, name='log'),
    url(r'^home2/infor$', views.infor, name='infor'),
    url(r'^mem_check/$', views.mem_check, name='mem_check'),
    url(r'^mem_join/$', views.mem_join, name='mem_join')
]
