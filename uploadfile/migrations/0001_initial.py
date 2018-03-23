# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-09 10:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('file_title', models.CharField(max_length=500)),
                ('company', models.CharField(max_length=100)),
                ('file_url', models.CharField(max_length=1000)),
                ('file_type', models.CharField(max_length=100)),
            ],
        ),
    ]