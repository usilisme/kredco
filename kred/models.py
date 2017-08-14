# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models import Model
from django.db import models
from django.db.models import(
    ForeignKey,CASCADE
)
from django.contrib.auth.models import User

class UserProfile(Model):
    user = models.OneToOneField(User, related_name='profiles')
    nameFull = models.CharField(max_length=200)
    nik = models.CharField(max_length=20) # Identification Number / Nomor Induk KTP
    avatar = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.user.username

class Payer (Model):
    user = models.OneToOneField(User, on_delete=CASCADE,)
    addrMail = models.CharField(max_length=10, null=True, blank=True)
    imgVrf3 = models.ImageField(upload_to='images/',blank=True)
    def __str__(self):
        return self.user.username

class Payee (Model):
    user = models.OneToOneField(User)
    def __str__(self):
        return self.user.username

class Merchant (Model):
    payee = ForeignKey(Payee, on_delete=models.CASCADE)
    nameMerchant = models.CharField(max_length=200)
    npwp = models.CharField(max_length=20, blank=True)
    def __str__(self):
        return self.nameMerchant

class Card (Model):
    CARD_TYPE = ( ('4','Visa'),('5','Master'))
    owner = models.ForeignKey('auth.User', related_name = 'cards', on_delete=models.CASCADE)
    type = models.CharField(max_length=6,choices=CARD_TYPE)
    number = models.CharField(max_length=20)
    dtExpiry = models.DateField()
    addBill = models.CharField(max_length=100)
    def __str__(self):
        return self.number

class Txn (Model):
    TxnKey = models.CharField(max_length = 15) # <sourceID>-yyyyMMdd-hhmm ios-201708-1305
    dateTxn = models.DateField()
    amount = models.DecimalField(max_digits=5,decimal_places=2)
    catTxn = models.CharField(max_length = 200)
    invoiceImg = models.ImageField()
    card = ForeignKey(Card, on_delete=models.SET_NULL, blank=True, null=True)
    merchant = ForeignKey(Merchant, on_delete = models.SET_NULL, blank=True, null = True)
    payer = ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    tmpMchntName = models.CharField(max_length = 200)
    tmpMchntPhon = models.CharField(max_length = 50)
    tmpMchntAcctNo = models.CharField(max_length = 50)
    tmpMchntAcctNm = models.CharField(max_length = 200)
    def __str__(self):
        return self.TxnKey

class Promo (models.Model):
    name = models.CharField(max_length = 500)
    imgBanner = models.ImageField(upload_to='images/promo/')
    dateFr = models.DateField()
    dateTo = models.DateField()
