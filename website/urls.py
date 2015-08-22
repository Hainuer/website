# -*- coding: utf-8 -*-
__author__ = 'Phoenix'

"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from home.views import index

urlpatterns = [
    url(r'^$', index),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^zhaokao/', include('zhaokao.urls', namespace='zhaokao')),
    url(r'^kume/', include('kume.urls', namespace='kume')),
    url(r'^duome/', include('duome.urls', namespace='duome')),
    url(r'^summernote/', include('django_summernote.urls')),
]

# 取消调试时调整static文件路径
if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_PATH)
    