# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-23 08:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='state',
            field=models.CharField(choices=[('n', 'Новый'), ('a', 'Активный'), ('f', 'Завершен')], default='n', max_length=255, verbose_name='Status'),
        ),
    ]
