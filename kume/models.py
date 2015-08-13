# -*- coding: utf-8 -*-
__author__ = 'Phoenix'

import uuid
import datetime
from pypinyin import lazy_pinyin
from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    simple_name = models.CharField(max_length=128, blank=True, unique=True)
    views = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        # 输入中文
        if self.simple_name == '' or self.simple_name == None:
            self.simple_name = '-'.join(lazy_pinyin(self.name))
        # 输入英文
        if self.simple_name == '' or self.simple_name == None:
            self.simple_name = self.name
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class Article(models.Model):
    category = models.ForeignKey(Category)
    title    = models.CharField(max_length=256)
    tags     = models.CharField(max_length=128, blank=True, help_text='请使用空格将标签分隔开')
    content  = models.TextField(verbose_name = '')
    pub_date = models.DateTimeField(default=timezone.now)
    views    = models.IntegerField(default=0)
    breviary = models.TextField(max_length=256, blank=True, verbose_name='')
    uuid = models.CharField(max_length=36)

    def save(self, *args, **kwargs):
        if self.breviary == '' or self.breviary == None:
            self.breviary = self.content[0:256]
        else:
            self.breviary = self.breviary
        if self.uuid == '' or self.uuid == None:
            self.uuid = str(uuid.uuid1())
        if not self.tags == '':
            self.tags = ' '.join(self.tags.split(' '))
        super(Article, self).save(*args, **kwargs)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently ?'    

    def __unicode__(self):
        return self.title