# -*- coding: utf-8 -*-
__author__ = 'Phoenix'

from django.shortcuts import render
from kume.models import *

def index(request):
    articles = Article.objects.all().order_by('-pub_date')[:4]
    return render(request, 'index.html', {'articles': articles })
