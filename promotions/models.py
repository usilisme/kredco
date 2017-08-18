# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import (
    Model, CharField, ImageField, DateField
)

class Promotion (Model):
    name = CharField(max_length = 500)
    imagebanner = ImageField(upload_to='media/images/promotions/')
    datestart = DateField()
    dateend = DateField()
    def __str__(self):
        return self.name
