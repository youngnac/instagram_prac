# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 05:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_post_is_visible'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.CharField(max_length=45),
        ),
    ]
