# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-15 13:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0010_donorprofileinfo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donorprofileinfo',
            old_name='profile_pic',
            new_name='mobile',
        ),
    ]
