# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-17 03:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Question', '0007_auto_20170917_0347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='user',
            field=models.CharField(default='Nothing', max_length=100),
        ),
    ]