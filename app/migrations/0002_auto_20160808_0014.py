# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-07 15:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spot',
            name='lat',
            field=models.FloatField(blank=True, default=0, verbose_name='緯度'),
        ),
        migrations.AlterField(
            model_name='spot',
            name='long',
            field=models.FloatField(blank=True, default=0, verbose_name='経度'),
        ),
    ]
