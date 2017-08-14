from django.contrib.auth import get_user_model
from django.db.models import Q

from rest_framework.serializers import (
    ModelSerializer,HyperlinkedModelSerializer, CharField, EmailField, ValidationError,
    PrimaryKeyRelatedField,
)
from rest_framework import serializers
from django.contrib.auth.models import User
from kred.models import UserProfile,Payer,Payee,Card,Txn,Promo

User = get_user_model()

class szListCard(ModelSerializer):
    class Meta:
        model = Card
        fields = ('number',)

class szGetCard (ModelSerializer):
    class Meta:
        model = Card
        fields = ('number',)