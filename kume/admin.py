# -*- coding: utf-8 -*-
__author__ = 'Phoenix'

from django.contrib import admin
from .models import *

from django_summernote.admin import SummernoteModelAdmin

class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'simple_name', 'views')

class ArticleModelAdmin(SummernoteModelAdmin):
    fieldsets = [
        ('Title',                    {'fields': ['title']}),
        ('Basic Information',        {'fields': ['views', 'category', 'pub_date', 'tags']}),
        ('Content',                  {'fields': ['content'], 'classes': ['collapse']}),
        ('Breviary',                 {'fields': ['breviary'], 'classes': ['collapse']}),
    ]
    list_display = ('title', 'pub_date', 'tags', 'views', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['title']

admin.site.register(Category, CategoryModelAdmin)
admin.site.register(Article, ArticleModelAdmin)
