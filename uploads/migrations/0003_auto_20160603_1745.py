# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-03 17:45
from __future__ import unicode_literals

from django.db import migrations, models
import uploads.models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0002_auto_20160602_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='contents_file',
            field=models.FileField(default='media/surveys/1/hello.xlsx', upload_to=uploads.models._get_upload_to),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='survey',
            name='file',
            field=models.FileField(upload_to=uploads.models._get_upload_to),
        ),
    ]
