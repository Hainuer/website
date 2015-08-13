# -*- coding: utf-8 -*-
__author__ = 'Phoenix'

from django.conf.urls import patterns, url
from kume import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<uuid>[\w\d\-]+)/$', views.post, name='post'),
    url(r'^about/$', views.about, name='about'),
    url(r'^archive/$', views.archive, name='archive'),
    url(r'^category/(?P<simple_name>[\w\-]+)/$', views.category, name='category'),
)