# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-19 18:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('ing', models.TextField()),
                ('price', models.FloatField()),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_talabat.MenuCategory')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.TextField()),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='menucategory',
            name='res',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_talabat.Restaurant'),
        ),
    ]
