from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$', views.post_list, name='post_list'),
    url(r'^css/ex1$', views.ex_css_1, name='ex_css_1'),
    url(r'^css/ex2$', views.ex_css_2, name='ex_css_2'),
    url(r'^css/ex3$', views.ex_css_3, name='ex_css_3'),
    url(r'^$', views.index, name='index'),
    url(r'^page_html/$', views.page_html, name='page_html'),
    url(r'^page_vc/$', views.page_vc, name='page_vc'),
    url(r'^page_op/$', views.page_op, name='page_op'),
]
