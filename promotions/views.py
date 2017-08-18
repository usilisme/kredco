# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import date

from rest_framework.generics import (
    ListAPIView,
)
from rest_framework.permissions import(
    AllowAny,
)

from promotions.serializers import szPromotion
from promotions.models import Promotion

class vwListPromotion(ListAPIView):
    serializer_class = szPromotion
    permission_classes = (AllowAny,)
    def get_queryset(self):
        return Promotion.objects.filter(datestart__lte= date.today(), dateend__gte=date.today())
