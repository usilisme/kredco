# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import (
    Model, CharField, ImageField, DateField
)

class Promotion (Model):
    name = CharField(max_length = 500)
    description = CharField(
        max_length= 1000, default=''
    )
    CategoryPromotion = CharField(
        max_length=50, default='Uncategorized'
    )
    imagebanner = ImageField(upload_to='img/promotions/')
    datestart = DateField()
    dateend = DateField()
    def __str__(self):
        return self.name
