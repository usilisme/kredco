# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-17 15:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('merchants', '0002_auto_20170817_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorymerchant',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='merchants.CategoryMerchant'),
        ),
    ]
