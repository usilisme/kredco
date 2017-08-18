# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import (
    Model, CharField, DateField, ImageField, DecimalField,
    OneToOneField, ForeignKey,
    SET_NULL,
)
from django.contrib.auth.models import User
from merchants.models import Merchant

class Transaction (Model):
    id = CharField(
        max_length = 19 # <sourceID>-yyyyMMdd-hhmmss ios-201708-130500
        ,primary_key=True
    )
    date = DateField()
    status = CharField(
        max_length=200 #completed scheduled cancelled
        , default='scheduled'
    )
    FLOW_TYPE = (('in', 'in'), ('out', 'out'))
    flow = CharField(
        max_length=200, choices=FLOW_TYPE,
        default='out'
    )
    remarks = CharField(
        max_length=200, blank=True
    )
    amount = DecimalField(
        max_digits=12
        ,decimal_places=2
    )
    category = CharField(
        max_length = 200
    )
    invoice = ImageField(blank=True)
    merchant = ForeignKey(
        Merchant, on_delete = SET_NULL, blank=True, null = True
    )
    payer = ForeignKey(
        User, on_delete=SET_NULL, blank=True, null=True
    )
    tmpMchntName = CharField(max_length = 200,blank=True)
    tmpMchntPhon = CharField(max_length = 50,blank=True)
    tmpMchntAcctNo = CharField(max_length = 50,blank=True)
    tmpMchntAcctNm = CharField(max_length = 200,blank=True)
    def __str__(self):
        return self.id
