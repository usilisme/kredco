# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import date
from rest_framework.reverse import reverse
from rest_framework import viewsets, status, generics, permissions
from rest_framework.generics import (
    CreateAPIView
)
from rest_framework.decorators import api_view, list_route
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from kred.forms import FormUser,FormPayer
from kred.models import Card,Promo
from rest_framework.permissions import AllowAny
from kred.permissions import (IsOwnerOrReadOnly)
from kred.serializers import (
    szCrUser, szLoginUser, szCard, szPromo
)

User = get_user_model()

class vwCrUser(CreateAPIView):
    serializer_class = szCrUser
    queryset = User.objects.all()

class vwLoginUser(APIView):
    permission_classes = [AllowAny]
    serializer_class = szLoginUser
    def post(self, request, *args, **kwargs):
        data = request.data
        sz = szLoginUser(data = data)
        if sz.is_valid(raise_exception=True):
            new_data = sz.data
            return Response (new_data,status=HTTP_200_OK)
        return Response(sz.errors,status=HTTP_400_BAD_REQUEST)

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = szCard

class CardList (generics.ListAPIView):
    queryset = Card.objects.all()
    serializer_class = szCard

class CardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = szCard
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

class PromoList(generics.ListAPIView):
    serializer_class = szPromo
    def get_queryset(self):
        return Promo.objects.filter(dateFr__lte= date.today(), dateTo__gte=date.today())

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'Welcome To kred.co'
    })

