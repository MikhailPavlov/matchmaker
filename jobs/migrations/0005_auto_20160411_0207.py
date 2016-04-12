# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-11 02:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20160410_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='employer',
            name='slug',
            field=models.SlugField(default='abc-123'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='slug',
            field=models.SlugField(default='abs-123'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='slug',
            field=models.SlugField(default='abc-123'),
            preserve_default=False,
        ),
    ]