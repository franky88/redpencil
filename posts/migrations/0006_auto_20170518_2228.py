# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-18 14:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_post_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='art_title',
        ),
    ]