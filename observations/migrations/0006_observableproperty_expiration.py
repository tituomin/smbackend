# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-20 11:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('observations', '0005_translate_observable_properties'),
    ]

    operations = [
        migrations.AddField(
            model_name='observableproperty',
            name='expiration',
            field=models.DurationField(blank=True, null=True),
        ),
    ]
