# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from kred.models import Txn,UserProfile, Merchant ,Payee,Payer,Card, Promo

admin.site.register(Txn)
admin.site.register(UserProfile)
admin.site.register(Merchant)
admin.site.register(Payee)
admin.site.register(Payer)
admin.site.register(Card)
admin.site.register(Promo)
