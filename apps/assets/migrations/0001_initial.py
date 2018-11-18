# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-11-18 09:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(error_messages={'unique': '该主机名已存在，请不要重复添加'}, max_length=32, unique=True, verbose_name='主机名')),
                ('server_type', models.CharField(choices=[('physical', '物理机'), ('virtual', '虚拟机'), ('instance', '云主机')], default='instance', max_length=10, verbose_name='服务器类型')),
                ('wip', models.GenericIPAddressField(error_messages={'invalid': 'IP地址格式错误', 'required': 'IP不能为空', 'unique': '该IP已存在，请不要重复添加'}, unique=True, verbose_name='外网地址')),
                ('nip', models.GenericIPAddressField(error_messages={'invalid': 'IP地址格式错误', 'required': 'IP不能为空', 'unique': '该IP已存在，请不要重复添加'}, unique=True, verbose_name='内网地址')),
                ('status', models.CharField(choices=[('online', '上线'), ('offline', '下线')], default='offline', max_length=10, verbose_name='状态')),
                ('instance_id', models.CharField(blank=True, max_length=64, null=True, verbose_name='云服务器id')),
                ('sn', models.CharField(blank=True, max_length=64, null=True, verbose_name='SN编号')),
                ('cpu_info', models.CharField(blank=True, max_length=128, null=True, verbose_name='cpu信息')),
                ('os', models.CharField(blank=True, max_length=64, null=True, verbose_name='系统类型')),
                ('memory', models.SmallIntegerField(default=0, verbose_name='内存/GB')),
                ('disk', models.IntegerField(default=0, verbose_name='硬盘/GB')),
                ('ctime', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('utime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('desc', models.CharField(blank=True, max_length=200, null=True, verbose_name='描述')),
            ],
            options={
                'verbose_name': '主机',
                'verbose_name_plural': '主机',
            },
        ),
        migrations.CreateModel(
            name='BusinessUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(error_messages={'unique': '该业务线已存在，请不要重复添加'}, max_length=64, unique=True, verbose_name='业务线')),
                ('desc', models.CharField(blank=True, max_length=64, null=True, verbose_name='备注')),
                ('ctime', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('parent_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_level', to='assets.BusinessUnit')),
            ],
            options={
                'verbose_name': '业务线',
                'verbose_name_plural': '业务线',
            },
        ),
        migrations.CreateModel(
            name='IDC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(error_messages={'unique': '该机房已存在，请不要重复添加'}, max_length=64, unique=True, verbose_name='机房名')),
                ('ctime', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('desc', models.CharField(blank=True, max_length=128, null=True, verbose_name='描述')),
            ],
            options={
                'verbose_name': '机房',
                'verbose_name_plural': '机房',
            },
        ),
        migrations.CreateModel(
            name='RemoteUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(error_messages={'unique': '该名称已存在，请不要重复添加'}, max_length=24, unique=True, verbose_name='名称')),
                ('username', models.CharField(max_length=12, verbose_name='用户名')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
                ('businessunit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.BusinessUnit', verbose_name='业务线')),
            ],
            options={
                'verbose_name': '远程用户',
                'verbose_name_plural': '远程用户',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(error_messages={'unique': '该角色已存在，请不要重复添加'}, max_length=32, unique=True, verbose_name='角色')),
                ('ctime', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('desc', models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='描述')),
            ],
            options={
                'verbose_name': '类型',
                'verbose_name_plural': '类型',
            },
        ),
        migrations.AddField(
            model_name='assets',
            name='business_unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='businessunit', to='assets.BusinessUnit', verbose_name='业务线'),
        ),
        migrations.AddField(
            model_name='assets',
            name='idc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='idc', to='assets.IDC', verbose_name='机房'),
        ),
        migrations.AddField(
            model_name='assets',
            name='role',
            field=models.ManyToManyField(blank=True, null=True, related_name='tag', to='assets.Tag', verbose_name='标签'),
        ),
    ]
