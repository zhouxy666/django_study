# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_banner_emailverifyrecord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(upload_to='image/banner/%Y-%m', verbose_name='轮播图'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='image/user/default.png', upload_to='image/user/%Y-%m', verbose_name='照片'),
        ),
    ]
