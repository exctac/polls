# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-23 08:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20170923_0846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='state',
            field=models.IntegerField(choices=[(1, 'Новый'), (2, 'Активный'), (3, 'Завершен')], default=1, max_length=255, verbose_name='Status'),
        ),
    ]
