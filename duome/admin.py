# -*- coding: utf-8 -*-
__author__ = 'Phoenix'

from django.contrib import admin
from duome.models import *

from django_summernote.admin import SummernoteModelAdmin

class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'simple_name', 'views')
    
class MumblerModelAdmin(SummernoteModelAdmin):
    fieldsets = [
        ('Basic Information',        {'fields': ['location', 'pub_date']}),
        ('Content',                  {'fields': ['content']}),
    ]
    list_display = ('uuid', 'location', 'pub_date')

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
admin.site.register(Mumbler, MumblerModelAdmin)
admin.site.register(Article, ArticleModelAdmin)
