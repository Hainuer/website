# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256)),
                ('tags', models.CharField(help_text=b'\xe8\xaf\xb7\xe4\xbd\xbf\xe7\x94\xa8\xe7\xa9\xba\xe6\xa0\xbc\xe5\xb0\x86\xe6\xa0\x87\xe7\xad\xbe\xe5\x88\x86\xe9\x9a\x94\xe5\xbc\x80', max_length=128, blank=True)),
                ('content', models.TextField(verbose_name=b'')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('views', models.IntegerField(default=0)),
                ('breviary', models.TextField(max_length=256, verbose_name=b'', blank=True)),
                ('uuid', models.CharField(max_length=36)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('simple_name', models.CharField(unique=True, max_length=128, blank=True)),
                ('views', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(to='kume.Category'),
        ),
    ]
