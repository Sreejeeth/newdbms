# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-19 17:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20171019_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='legs1',
            name='slug',
            field=models.SlugField(max_length=200),
        ),
    ]
