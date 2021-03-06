# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-19 17:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20171019_2116'),
    ]

    operations = [
        migrations.CreateModel(
            name='Legs1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(default='', editable=False, max_length=200)),
                ('weight', models.CharField(max_length=60)),
                ('warrenty', models.CharField(max_length=60)),
                ('heel_height', models.CharField(max_length=60)),
                ('activity', models.CharField(max_length=60)),
                ('location', models.CharField(blank=True, max_length=300)),
                ('cost', models.FloatField()),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.DeleteModel(
            name='Legs',
        ),
        migrations.AlterIndexTogether(
            name='legs1',
            index_together=set([('id', 'slug')]),
        ),
    ]
