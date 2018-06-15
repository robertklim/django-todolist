# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-15 07:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('todos', '0002_auto_20180613_0631'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords', models.TextField(help_text='Separete each bo comma')),
                ('description', models.TextField(blank=True, help_text='Separete each bo comma', null=True)),
                ('public', models.BooleanField(default=True)),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('todo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todos.Todos')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-updated', '-timestamp'],
            },
        ),
    ]
