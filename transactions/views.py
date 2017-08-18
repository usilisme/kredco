# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import (
    CreateAPIView, RetrieveAPIView, UpdateAPIView, ListAPIView
)

from django.contrib.auth import get_user_model

from transactions.models import Transaction

from transactions.serializers import (
    szListTransaction,szDtlTxn
)


User = get_user_model()

### Start of the DRY Code ###
class vwListTransaction(ListAPIView):
    serializer_class = szListTransaction
    def get_queryset(self):
        user = self.request.user
        return Transaction.objects.filter(payer=user).order_by('-date')

class vwDtlTxn(RetrieveAPIView):
    serializer_class = szDtlTxn
    queryset = Transaction.objects.all()