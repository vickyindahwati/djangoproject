# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-11 04:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_do', models.TextField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]