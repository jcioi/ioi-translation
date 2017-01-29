# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-29 18:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.FileField(upload_to='uploads/')),
                ('title', models.CharField(max_length=100)),
                ('create_time', models.DateTimeField(verbose_name='Date Created')),
            ],
        ),
        migrations.AlterField(
            model_name='version',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 29, 18, 32, 33, 479033)),
        ),
        migrations.AlterField(
            model_name='versionparticle',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 29, 18, 32, 33, 479596)),
        ),
    ]