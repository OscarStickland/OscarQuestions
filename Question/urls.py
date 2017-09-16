from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^question/(?P<question_id>[0-9]+)/$', views.question),
    url(r'^question/(?P<question_id>[0-9]+)/delete/$', views.delete),
    url(r'^question/admin/$', views.admin),
    url(r'^question/ask/$', views.ask),
    url(r'^question/login/$', views.login),
    url(r'^question/$', views.index)

]
