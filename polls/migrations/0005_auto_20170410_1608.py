# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-10 16:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20170410_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
