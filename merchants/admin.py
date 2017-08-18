# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from merchants.models import (
    Merchant, CategoryMerchant
)

admin.site.register(Merchant)
admin.site.register(CategoryMerchant)
