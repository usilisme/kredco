# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import date
from rest_framework import viewsets, status, generics, permissions
from rest_framework.generics import (
    CreateAPIView, RetrieveAPIView, UpdateAPIView, ListAPIView
)
from rest_framework.decorators import api_view, list_route
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from kred.forms import FormUser,FormPayer
from kred.models import Card,Promo,UserProfile,Txn
from rest_framework.permissions import AllowAny
from kred.permissions import (IsOwnerOrReadOnly)
from kred.serializers import (
    szCrUser, szLoginUser,  szCard, szPromo
)
from transactions.serializers import (
    szGetTxn,szDtlTxn
)


User = get_user_model()

### Start of the DRY Code ###
class vwGetTxn(ListAPIView):
    serializer_class = szGetTxn
    def get_queryset(self):
        user = self.request.user
        return Txn.objects.filter(payer=user).order_by('-dateTxn')

class vwDtlTxn(RetrieveAPIView):
    serializer_class = szDtlTxn
    queryset = Txn.objects.all()