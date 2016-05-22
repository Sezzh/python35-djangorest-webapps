# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-22 20:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('colors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColorPalette',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category_name', models.CharField(max_length=100)),
                ('color', models.ManyToManyField(to='colors.Color')),
                ('owner', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
