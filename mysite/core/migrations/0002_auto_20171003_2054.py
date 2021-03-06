# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-03 15:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hands',
            old_name='gender',
            new_name='age_group',
        ),
        migrations.AlterField(
            model_name='eye',
            name='location',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='hands',
            name='location',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='legs',
            name='location',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='teeth',
            name='location',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
