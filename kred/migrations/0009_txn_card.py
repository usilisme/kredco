# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-14 11:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kred', '0008_auto_20170814_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='txn',
            name='card',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='kred.Card'),
        ),
    ]
