# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-12 05:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('trans', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='slug',
            field=models.CharField(default='a', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contentversion',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 12, 5, 29, 40, 745421, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='uploaded_file',
            field=models.FileField(blank=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='versionparticle',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 12, 5, 29, 40, 752308, tzinfo=utc)),
        ),
    ]