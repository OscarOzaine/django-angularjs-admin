# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-12 02:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, default=b'', max_length=100)),
                ('code', models.TextField()),
                ('linenos', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.RemoveField(
            model_name='employee',
            name='store',
        ),
        migrations.RemoveField(
            model_name='store',
            name='chain',
        ),
        migrations.DeleteModel(
            name='Chain',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.DeleteModel(
            name='Store',
        ),
    ]
