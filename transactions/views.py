# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

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
    transactions = Transaction.objects.filter(status='scheduled')
    context['transactions'] = transactions
    return render(request,'transactions/tour.html', context)

def dashboard(request):
    context = {}
    return render (request, 'dashboard.html', context)

def history(request):
    context = {}

    transactions = Transaction.objects.filter(status='scheduled')
    completeds = Transaction.objects.filter(status='completed')
    cancelleds = Transaction.objects.filter(status='cancelled')

    context['transactions'] = transactions
    context['completeds'] = completeds
    context['cancelleds'] = cancelleds
    return render(request, 'transactions/history.html', context)

def payment(request):
    context = {}
    completed = False
    src = 'web' #request.META.get('HTTP_USER_AGENT')
    dttm = datetime.today().strftime('-%Y%m%d-%H%M%S')
    TransactionKey = src+dttm

    if (request.method == 'POST'):
        f = PaymentForm(request.POST, request.FILES)
        if f.is_valid():
            t = f.save()
            t.save()
            completed = True
        else:
            print(f.errors)

    else:
        f = PaymentForm(initial={'TransactionKey':TransactionKey})
    context['form'] = f
    context['completed'] = completed
    return render(request, 'transactions/payment.html',context)

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