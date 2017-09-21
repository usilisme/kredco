# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect

from rest_framework.generics import (
    CreateAPIView, RetrieveAPIView, UpdateAPIView, ListAPIView
)

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from transactions.models import Transaction
from transactions.forms import PaymentForm

from transactions.serializers import (
    szListTransaction,szDtlTxn
)


User = get_user_model()

def transactions(request):
    context= {}
    transactions = Transaction.objects.all()
    context['transactions'] = transactions
    return render(request,'transactions/tour.html', context)

def history(request):
    context = {}
    transactions = Transaction.objects.all()
    context['transactions'] = transactions
    return render(request, 'transactions/history.html', context)

def payment(request):
    context = {}
    if (request.method == 'POST'):
        f = PaymentForm(data=request.POST)
        if f.is_valid():
            request.session['NameMerchant'] = f.cleaned_data('tempNameMerchant')
            request.session['MerchantPhone'] = f.cleaned_data('tempMerchantPhone')
            request.session['MerchantBank'] = f.cleaned_data('tempMerchantBankName')
            request.session['MerchantAccountNo'] = f.cleaned_data('tempMerchantBankAccount')
    else:
        f = PaymentForm()
        if request.session.has_key('NameMerchant'):
            context['MerchantName'] = request.session['NameMerchant']
        if request.session.has_key('MerchantPhone'):
            context['MerchantPhone'] = request.session['MerchantPhone']
        if request.session.has_key('MerchantBank'):
            context['MerchantBank'] = request.session['MerchantBank']
        if request.session.has_key('MerchantAccountNo'):
            context['MerchantAccountNo'] = request.session['MerchantAccountNo']
    context['form'] = f
    return render(request, 'transactions/payment.html',context)

def details_payment(request):
    return render (request, 'transactions/payment.html')

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