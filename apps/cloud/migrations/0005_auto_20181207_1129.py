# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-12-07 11:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0004_auto_20181207_1121'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='instancestype',
            unique_together=set([('family', 'type', 'zone')]),
        ),
    ]