# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-09 12:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import pytz
UTC_TIMEZONE = pytz.timezone('UTC')


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0029_order_units_by_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unit',
            name='modified_time',
        ),
        migrations.AddField(
            model_name='unit',
            name='origin_last_modified_time',
            field=models.DateTimeField(
                db_index=True,
                default=datetime.datetime.now(UTC_TIMEZONE),
                help_text='Time of last modification'),
            preserve_default=False,
        ),
    ]
