# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-15 07:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0002_auto_20180615_0756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='keywords',
            field=models.TextField(help_text='Separete each by comma'),
        ),
    ]
