# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-22 09:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('places', '0005_category_pin_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
