# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-22 09:24
from __future__ import unicode_literals

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20171022_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdb',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, keep_meta=True, quality=0, size=[500, 300], upload_to='products/%Y/%m/%d'),
        ),
    ]
