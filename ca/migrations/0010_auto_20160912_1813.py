# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-12 12:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ca', '0009_task_taskinstance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caprofile',
            name='year',
            field=models.IntegerField(blank=True, choices=[(1, 'First'), (2, 'Second'), (3, 'Third'), (4, 'Fourth'), (5, 'Fifth')], null=True),
        ),
    ]
