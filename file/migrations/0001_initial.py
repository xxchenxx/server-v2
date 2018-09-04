# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-04 11:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('report', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileRecord',
            fields=[
                ('file_id', models.AutoField(primary_key=True, serialize=False)),
                ('path', models.CharField(max_length=100)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.Report')),
            ],
        ),
    ]
