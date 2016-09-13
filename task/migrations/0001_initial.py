# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-12 14:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ca', '0012_auto_20160912_1938'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('directorDetail', models.TextField()),
                ('dd', models.BooleanField(default=False)),
                ('studentBodyDetail', models.TextField()),
                ('sbd', models.BooleanField(default=False)),
                ('ca', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ca.CAProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('taskId', models.AutoField(primary_key=True, serialize=False)),
                ('taskName', models.CharField(max_length=50)),
                ('taskDescription', models.TextField()),
                ('deadLine', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='TaskInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.SmallIntegerField(default=0)),
                ('ca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ca.CAProfile')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.Task')),
            ],
        ),
    ]