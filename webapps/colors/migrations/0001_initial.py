# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-22 20:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hexa', models.CharField(max_length=15)),
                ('opacity', models.DecimalField(decimal_places=2, max_digits=4)),
                ('rgb', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
