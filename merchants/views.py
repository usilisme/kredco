# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework.generics import (
    ListAPIView, RetrieveAPIView,
)
from rest_framework.permissions import(
    AllowAny,
)
from rest_framework.filters import(
    SearchFilter
)

from merchants.serializers import szListMerchant
from merchants.models import Merchant

#SITE
def merchants(request):
    merchants = Merchant.objects.order_by('name')[:12]
    context = {'merchants': merchants}


    filter = request.GET.get("filter")
    if filter:
        filter = filter
    else :
        filter = ""
    results = Merchant.objects.filter(name__icontains=filter)
    context = {'results':results}
    return render(request,'merchant.html', context)

#API
class vwListMerchant(ListAPIView):
    serializer_class = szListMerchant
    permission_classes = (AllowAny,)
    def get_queryset(self):
        return Merchant.objects.all()
    filter_backends = (SearchFilter,)
    search_fields = ('name',)

class vwGetMerchant(RetrieveAPIView):
    queryset = Merchant.objects.all()
    serializer_class = szListMerchant

