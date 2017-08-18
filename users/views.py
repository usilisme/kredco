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

from rest_framework.permissions import(
    AllowAny,
)

from kred.serializers import (
    szCrUser, szLoginUser
)
from users.serializers import (
    szGetUser,szGetUserProfile,szResetPass
)

User = get_user_model()

### Start of the DRY Code ###
class vwCrUser(CreateAPIView):
    serializer_class = szCrUser
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

class vwLoginUser(APIView):
    permission_classes = (AllowAny,)
    serializer_class = szLoginUser
    def post(self, request, *args, **kwargs):
        data = request.data
        sz = szLoginUser(data = data)
        if sz.is_valid(raise_exception=True):
            new_data = sz.data
            return Response (new_data,status=HTTP_200_OK)
        return Response(sz.errors,status=HTTP_400_BAD_REQUEST)

class vwGetUser (RetrieveAPIView):
    serializer_class = szGetUser
    queryset = User.objects.all()
    lookup_field = 'username'

class vwResetPass(UpdateAPIView):
    serializer_class = szResetPass
    queryset = User.objects.all()
    lookup_field = 'username'