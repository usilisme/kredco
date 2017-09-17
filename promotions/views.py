# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import date

from django.shortcuts import render

from rest_framework.generics import (
    ListAPIView,
)
from rest_framework.permissions import(
    AllowAny,
)

from promotions.serializers import szPromotion
from promotions.models import Promotion

def promotion(request):
    promotions = Promotion.objects.order_by('-dateend')[:6]
    context = {'promotions': promotions}
    return render(request, 'promotion.html', context)

class vwListPromotion(ListAPIView):
    serializer_class = szPromotion
    permission_classes = (AllowAny,)
    def get_queryset(self):
        return Promotion.objects.filter(datestart__lte= date.today(), dateend__gte=date.today())
