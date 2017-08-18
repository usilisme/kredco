from django.contrib.auth import get_user_model

from rest_framework.serializers import (
    ModelSerializer,HyperlinkedModelSerializer, CharField, EmailField, ValidationError,
    PrimaryKeyRelatedField,
)

from transactions.models import Transaction

User = get_user_model()

class szListTransaction (ModelSerializer):
    #payer = szGetUser()
    class Meta:
        model = Transaction
        fields = ('id','date','amount','merchant',)

class szDtlTxn (ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'date', 'amount', 'merchant','remarks','flow','status',)