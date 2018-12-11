# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-12-11 17:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0007_auto_20181208_1624'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='pid',
            new_name='proid',
        ),
        migrations.RemoveField(
            model_name='project',
            name='name',
        ),
        migrations.AddField(
            model_name='project',
            name='ctime',
            field=models.CharField(default='', max_length=32, verbose_name='项目创建时间'),
        ),
        migrations.AddField(
            model_name='project',
            name='desc',
            field=models.TextField(blank=True, null=True, verbose_name='项目描述'),
        ),
        migrations.AddField(
            model_name='project',
            name='proname',
            field=models.CharField(default='', max_length=32, verbose_name='项目名称'),
        ),
    ]