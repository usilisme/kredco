# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db.models import (
    Model,
    CharField,
    PositiveSmallIntegerField,
    DateField,ImageField,ForeignKey,CASCADE
)

class Card (Model):
    CARD_TYPE = ( ('Visa','Visa'),('Master','Master'))

    owner = ForeignKey(User, related_name = 'cards', on_delete=CASCADE)
    type = CharField(max_length=6,choices=CARD_TYPE)
    number = CharField(max_length=16)

    @property
    def number4(self):
        return '**** **** **** %s' % (self.number[-4:])

    ExpiryMonth = PositiveSmallIntegerField(default=12)
    ExpiryYear = PositiveSmallIntegerField(default=2050)

    dtExpiry = DateField(blank=True, null=True, default='2050-12-31'

    )
    logo = ImageField(
        upload_to='img/promotions/'
        ,blank=True
    )


    addBill = CharField( blank=True, null=True, default=''
        ,max_length=100
    )
    def __str__(self):
        return self.number4
