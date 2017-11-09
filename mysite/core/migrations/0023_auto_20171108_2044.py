# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-08 15:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_about_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productdb',
            name='stock',
        ),
        migrations.AlterField(
            model_name='about',
            name='description',
            field=models.CharField(db_index=True, max_length=2000),
        ),
    ]