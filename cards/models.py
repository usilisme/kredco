# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db.models import (
    Model,CharField,DateField,ImageField,ForeignKey,CASCADE
)

class Card (Model):
    CARD_TYPE = ( ('Visa','Visa'),('Master','Master'))
    owner = ForeignKey(User, related_name = 'cards', on_delete=CASCADE)
    type = CharField(max_length=6,choices=CARD_TYPE)
    number = CharField(max_length=4)
    dtExpiry = DateField()
    logo = ImageField(
        upload_to='img/promotions/'
        ,blank=True
    )


    addBill = CharField(max_length=100)
    def __str__(self):
        return self.number
