# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-05 13:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0006_auto_20160405_1318'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useranswer',
            old_name='their_answer_importance',
            new_name='their_importance',
        ),
    ]
