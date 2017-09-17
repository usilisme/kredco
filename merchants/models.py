# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import (
    Model, CharField, ImageField, IntegerField, DateField, ForeignKey
)

class CategoryMerchant(Model):
    parent = ForeignKey('self',null=True, blank=True)
    name = CharField(max_length=200)
    sortOrder = IntegerField()
    def __str__(self):
        return self.name

class Merchant (Model):
    name = CharField(max_length=200)
    npwp = CharField(max_length=20, blank=True)
    location = CharField(
        max_length=100,
        blank=True, default=''
    )
    owner = CharField(
        max_length=200,
        blank=True, default=''
    )
    logo = ImageField(
        upload_to='img/merchants/', blank=True
    )
    cat = ForeignKey(
        CategoryMerchant,
        blank = True, default=1
    )


    def __str__(self):
        return self.name
