# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.db.models import (
    Model, CharField, DateField, ImageField, FileField, DecimalField,
    OneToOneField, ForeignKey,
    SET_NULL,
)
from django.contrib.auth.models import User
from merchants.models import Merchant

class Transaction (Model):
    TRANSACTION_STATUS = (
        ('scheduled', 'scheduled')
        , ('completed', 'completed')
        , ('cancelled', 'cancelled')
    )
    TransactionKey = CharField(
        blank=True,null=True,
        max_length = 19 # <sourceID>-yyyyMMdd-hhmmss ios-201708-130500

    )

    date = DateField(
        blank=True ,null = True
        ,default= datetime.now
    )

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
    amount = DecimalField(blank=True,null=True,
        max_digits=12
        ,decimal_places=2
    )
    category = CharField(
        max_length = 200,
        default='Unknown'
    )
    invoice = FileField(blank=True,null=True,
        upload_to = 'invoices/'
    )
    merchant = ForeignKey(
        Merchant, on_delete = SET_NULL, blank=True, null = True
    )
    payer = ForeignKey(
        User, on_delete=SET_NULL, blank=True, null=True
    )
    tempMerchantName = CharField(max_length = 200,blank=True)
    tempMerchantPhone = CharField(max_length = 50,blank=True)
    tempMerchantBankAccount = CharField(max_length = 50,blank=True)
    tmpMerchantBankName = CharField(max_length = 200,blank=True)

    tempCardNumber = CharField(max_length=50,blank=True)
    tempCardOwnerName = CharField(max_length=50,blank=True)
    tempCardExpiryDate = CharField(max_length=50,blank=True)
    tempCardCVV = CharField(max_length=50,blank=True)

    def __str__(self):
        return self.TransactionKey
