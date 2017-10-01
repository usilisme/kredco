# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
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

from users.forms import (
    UserEditForm ,EditProfileForm
)
from merchants.serializers import szListMerchant

from merchants.models import Merchant

#SITE
def signup(request):
    context = {}
    u = request.user
    if request.method == 'POST':
        uf = UserEditForm(request.POST, instance=u)
        pf = BeMerchantForm(request.POST,instance=u)
        sf = CreateShopForm(request.POST)
        if uf.is_valid():
            uf.save()
        if pf.is_valid():
            pf.save()
        if sf.is_valid():
            sf.save()
    else:
        uf = UserEditForm(instance=u)
        pf = EditProfileForm(instance=u)
        sf = CreateShopForm()

    context['uf'] = uf
    context['pf'] = pf
    context['sf'] = sf
    return render(request, 'merchants/signup.html',context)

def myshops(request):
    context = {}
    return render(request, 'construction.html', context)

def merchants(request):
    filter = request.GET.get("q")
    if filter:
        filter = filter
    else :
        filter = ""
    results = Merchant.objects.filter(name__icontains=filter)
    context = {'merchants':results}
    return render(request,'merchant.html', context)

def detail_merchant(request,pk):
    context = {}
    return render (request, 'construction.html', context)

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

