# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-21 09:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160420_1359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='website',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='contactNo',
            field=models.CharField(default=b'', max_length=11),
        ),
    ]
