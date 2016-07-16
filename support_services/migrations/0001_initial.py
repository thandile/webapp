# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-16 13:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name="service's name")),
                ('description', models.TextField(verbose_name="service's description")),
                ('slug', models.SlugField(max_length=120, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
