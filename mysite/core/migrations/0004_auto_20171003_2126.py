# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-03 15:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_hands_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='legs',
            name='heel_height',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='legs',
            name='warrenty',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='legs',
            name='weight',
            field=models.CharField(max_length=11),
        ),
    ]
