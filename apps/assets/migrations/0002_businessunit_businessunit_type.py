# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-11-19 09:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessunit',
            name='businessunit_type',
            field=models.IntegerField(choices=[(1, '一级业务线'), (2, '二级业务线'), (3, '三级业务线')], default=1, verbose_name='业务线级别'),
        ),
    ]
