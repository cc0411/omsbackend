# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-11-18 12:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0003_auto_20181118_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assets',
            name='nip',
            field=models.GenericIPAddressField(error_messages={'invalid': 'IP地址格式错误', 'null': 'NIP不能为空', 'unique': '该IP已存在，请不要重复添加'}, unique=True, verbose_name='内网地址'),
        ),
        migrations.AlterField(
            model_name='assets',
            name='wip',
            field=models.GenericIPAddressField(error_messages={'invalid': 'IP地址格式错误', 'null': 'WIP不能为空', 'unique': '该IP已存在，请不要重复添加'}, unique=True, verbose_name='外网地址'),
        ),
    ]
