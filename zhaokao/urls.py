# -*- coding: utf-8 -*-
__author__ = 'Phoenix'

from django.conf.urls import patterns, url
from zhaokao import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^want/$', views.want, name='want'),
    url(r'^notice/$', views.notice, name='notice'),
    url(r'^view/(?P<link>[\w\=\?\-\.]+)/$', views.view, name='view'),
    url(r'^category/(?P<city_code>[\w]+)/$', views.category, name='category'),
)