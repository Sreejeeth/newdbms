# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-03 15:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20171003_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='hands',
            name='size',
            field=models.CharField(default=6, max_length=20),
            preserve_default=False,
        ),
    ]
