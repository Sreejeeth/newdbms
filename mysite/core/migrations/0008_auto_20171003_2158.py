# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-03 16:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_teeth_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teeth',
            name='description',
            field=models.CharField(max_length=1000),
        ),
    ]
