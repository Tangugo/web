# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-06 01:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20160506_0106'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='shirt_size',
            field=models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], default=datetime.datetime(2016, 5, 6, 1, 14, 52, 1991, tzinfo=utc), max_length=1),
            preserve_default=False,
        ),
    ]
