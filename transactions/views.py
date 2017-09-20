# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect

from rest_framework.generics import (
    CreateAPIView, RetrieveAPIView, UpdateAPIView, ListAPIView
)

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from transactions.models import Transaction

from transactions.serializers import (
    szListTransaction,szDtlTxn
)


User = get_user_model()


def transactions(request):
    context= {}
    transactions = Transaction.objects.all()
    context['transactions'] = transactions
    return render(request,'transactions/transactions.html', context)

def details_merchant(request):
    if (request.method == 'POST'):
        request.session['NameMerchant'] = request.POST.get('NameMerchant')
        request.session['MerchantPhone'] = request.POST.get('MerchantPhone')
        request.session['MerchantBank'] = request.POST.get('MerchantBank')
        request.session['MerchantAccountNo'] = request.POST.get('MerchantAccountNo')
        return render (request,'transactions/details_payment.html')
    else:
        context = {}
        if request.session.has_key('NameMerchant'):
            context['MerchantName'] = request.session['NameMerchant']
        if request.session.has_key('MerchantPhone'):
            context['MerchantPhone'] = request.session['MerchantPhone']
        if request.session.has_key('MerchantBank'):
            context['MerchantBank'] = request.session['MerchantBank']
        if request.session.has_key('MerchantAccountNo'):
            context['MerchantAccountNo'] = request.session['MerchantAccountNo']
        return render(request, 'transactions/details_merchant.html',context)

def details_payment(request):
    return render (request, 'transactions/details_payment.html')

def details_confirm(request):
    context = {}
    if request.session.has_key('NameMerchant'):
        context['MerchantName'] = request.session['NameMerchant']
    if request.session.has_key('MerchantPhone'):
        context['MerchantPhone'] = request.session['MerchantPhone']
    if request.session.has_key('MerchantBank'):
        context['MerchantBank'] = request.session['MerchantBank']
    if request.session.has_key('MerchantAccountNo'):
        context['MerchantAccountNo'] = request.session['MerchantAccountNo']
    return render (request, 'transactions/details_confirm.html', context)

### Start of the DRY Code ###
class vwListTransaction(ListAPIView):
    serializer_class = szListTransaction
    def get_queryset(self):
        user = self.request.user
        return Transaction.objects.filter(payer=user).order_by('-date')

class vwDtlTxn(RetrieveAPIView):
    serializer_class = szDtlTxn
    queryset = Transaction.objects.all()