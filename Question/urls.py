from django.conf.urls import url
from django.contrib import admin
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^question/(?P<question_id>[0-9]+)/$', views.question),
    url(r'^question/(?P<question_id>[0-9]+)/delete/$', views.delete),
    url(r'^question/admin/$', views.admin),
    url(r'^question/ask/$', views.ask),
    url(r'^question/$', views.index),
    url(r'^question/login/$', login, {'template_name' : 'question/login.html'}),
    url(r'^question/logout/$', logout, {'template_name' : 'question/logout.html'}),
    url(r'^question/adduser/$', views.addUser),

]
