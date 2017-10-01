# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render,redirect

from django.contrib.auth import get_user_model

from rest_framework.generics import (
    CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
)

from cards.serializers import (
    szListCard,szGetCard
)
from cards.models import Card

User = get_user_model()

def delete_card(request,pk):
    card = Card.objects.get(pk = pk)
    card.delete()
    return redirect('/users/myprofile/')

### Start of the DRY Code ###
class vwListCard(ListAPIView):
    serializer_class = szListCard
    def get_queryset(self):
        user = self.request.user
        return Card.objects.filter(owner=user)

class vwGetCard(RetrieveAPIView):
    serializer_class = szGetCard
    queryset = Card.objects.all()

class vwUpdCard(UpdateAPIView):
    serializer_class = szGetCard
    queryset = Card.objects.all()

class vwDelCard(DestroyAPIView):
    serializer_class = szGetCard
    queryset = Card.objects.all()