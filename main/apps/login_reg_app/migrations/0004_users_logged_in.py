# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-06-20 16:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_reg_app', '0003_auto_20190620_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='logged_in',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
