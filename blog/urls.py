from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    #url(r'^$', views.home, name='home'),
    url(r'^pet_ask/$', views.pet_ask, name='pet_ask'),
    url(r'^pet_search/$', views.pet_search, name='pet_search'),
    url(r'^pet_sitter/$', views.pet_sitter, name='pet_sitter'),
    #url(r'^js/$', views.script, name='script'),
    #url(r'^js2/$', views.script2, name='script2'),
    #url(r'^ajax/$', views.ajax, name='ajax'),
    #url(r'^$', views.main, name='main'),
    #url(r'^log/$', views.log, name='log'),
]
