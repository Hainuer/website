# -*- coding: utf-8 -*-
__author__ = 'Phoenix'

from django.conf.urls import patterns, url
from duome import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^category/(?P<simple_name>[\w\-]+)/$', views.category, name='category'),
    url(r'^post/(?P<uuid>[\w\d\-]+)/$', views.post, name='post'),
    url(r'^tag/(?P<tag>(.)+)/$', views.tag, name='tag'),
    url(r'^mumbler/$', views.mumbler, name='mumbler'),
    url(r'^archive/$', views.archive, name='archive'),
    url(r'^about/$', views.about, name='about'),
)