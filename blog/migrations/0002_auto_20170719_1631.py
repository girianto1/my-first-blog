# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-19 09:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 19, 9, 31, 32, 467425, tzinfo=utc)),
        ),
    ]
