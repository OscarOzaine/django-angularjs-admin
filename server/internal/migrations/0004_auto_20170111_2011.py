# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-12 04:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internal', '0003_auto_20170111_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rangeparameter',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
