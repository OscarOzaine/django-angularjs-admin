# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-12 04:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('internal', '0002_auto_20170111_1824'),
    ]

    operations = [
        migrations.CreateModel(
            name='RangeParameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('gpio', models.CharField(blank=True, default=b'', max_length=255)),
                ('max', models.FloatField()),
                ('max_value', models.FloatField()),
                ('min', models.FloatField()),
                ('min_value', models.FloatField()),
                ('range_id', models.IntegerField()),
                ('sensor_id', models.IntegerField()),
                ('highlighted', models.TextField()),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.AlterModelOptions(
            name='snippet',
            options={'ordering': ('owner', 'created')},
        ),
        migrations.AddField(
            model_name='snippet',
            name='highlighted',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='snippet',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='snippets', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]