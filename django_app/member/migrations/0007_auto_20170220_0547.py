# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 05:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0006_auto_20170220_0544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relationship',
            name='date_follow',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
