# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.shortcuts import render,redirect

from django.db.models import(
    Sum,Count,
)
from rest_framework.generics import (
    CreateAPIView, RetrieveAPIView, UpdateAPIView, ListAPIView
)



from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from cards.models import Card
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
    u = request.user

    #Summary Statistics
    context = Transaction.objects.filter(payer=u).aggregate(Sum('amount'),Count('id'))

    d = Transaction.objects.values('status').annotate(Sum('amount'))
    context['piedata'] = d

    #Recent Transactions
    transactions = Transaction.objects.filter(payer=u).order_by('-date')
    context['transactions'] = transactions

    print(context)
    return render (request, 'transactions/dashboard.html', context)

@login_required
def history(request):
    context = {}
    u = request.user
    q = Transaction.objects.filter(payer=u)
    transactions = q.filter(status='scheduled')
    completeds = q.filter(status='completed')
    cancelleds = q.filter(status='cancelled')

    context['transactions'] = transactions
    context['completeds'] = completeds
    context['cancelleds'] = cancelleds
    print(context)
    return render(request, 'transactions/history.html', context)

def cancel_transaction(request,pk):
    context = {}
    u = request.user
    t = Transaction.objects.get(pk=pk)
    t.status = 'cancelled'
    t.save()
    return redirect('history')


def payment(request):
    context = {}
    u = request.user
    try:
        cards = Card.objects.filter(owner=u)
    except:
        cards = None
    completed = False
    src = 'web' #request.META.get('HTTP_USER_AGENT')
    dttm = datetime.today().strftime('-%Y%m%d-%H%M%S')
    TransactionKey = src+dttm

    if (request.method == 'POST'):
        f = PaymentForm(request.POST, request.FILES, payer=u)
        if f.is_valid():
            t = f.save()
            t.payer = u
            t.save()
            completed = True
        else:
            print(f.errors)
            print()
            print(f)

    else:
        f = PaymentForm(initial={'TransactionKey':TransactionKey}, payer=u)
    context['form'] = f
    context['completed'] = completed
    context['cards'] = cards
    return render(request, 'transactions/payment.html',context)


### Start of the DRY Code ###
class vwListTransaction(ListAPIView):
    serializer_class = szListTransaction
    def get_queryset(self):
        user = self.request.user
        return Transaction.objects.filter(payer=user).order_by('-date')

class vwDtlTxn(RetrieveAPIView):
    serializer_class = szDtlTxn
    queryset = Transaction.objects.all()