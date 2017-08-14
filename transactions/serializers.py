from django.contrib.auth import get_user_model
from django.db.models import Q

from rest_framework.serializers import (
    ModelSerializer,HyperlinkedModelSerializer, CharField, EmailField, ValidationError,
    PrimaryKeyRelatedField,
)
from rest_framework import serializers
from django.contrib.auth.models import User
from kred.models import UserProfile,Payer,Payee,Card,Txn,Promo
from users.serializers import (
    szGetUser
)

User = get_user_model()

class szGetTxn (ModelSerializer):
    payer = szGetUser()
    class Meta:
        model = Txn
        fields = ('id','TxnKey','dateTxn','amount','merchant','payer','card',)

class szDtlTxn (ModelSerializer):
    class Meta:
        model = Txn
        fields = ('id','TxnKey', 'dateTxn', 'amount', 'merchant', 'payer', 'card',)