# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-14 11:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kred', '0007_auto_20170814_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='txn',
            name='merchant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='kred.Merchant'),
        ),
        migrations.AlterField(
            model_name='merchant',
            name='npwp',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='payer',
            name='addrMail',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='payer',
            name='imgVrf3',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
