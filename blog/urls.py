from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^pet_ask/$', views.pet_ask, name='pet_ask'),
    # url(r'^pet_search/$', views.pet_search, name='pet_search'),
    # url(r'^pet_sitter/$', views.pet_sitter, name='pet_sitter'),
    #url(r'^js/$', views.script, name='script'),
    url(r'^$', views.home, name='home'),
    url(r'^home2/$', views.home2, name='home2'),
    url(r'^ab/$', views.ab, name='about'),
    url(r'^ab2/$', views.ab, name='about2'),
    url(r'^join/$', views.join, name='join'),
    url(r'^log/$', views.log, name='log'),
    url(r'^mem_check/$', views.mem_check, name='mem_check'),
    url(r'^mem_join/$', views.mem_join, name='mem_join')
]
