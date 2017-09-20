# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
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
from users.forms import UserForm
from users.serializers import (
    szGetUser,szGetUserProfile,szResetPass
)

from cards.models import Card
from transactions.models import Transaction

User = get_user_model()

#SITE
def myprofile(request):
    context = {}
    context['profile'] = request.user
    context['cards'] = Card.objects.all()
    transactions =  Transaction.objects.all()
    context['mytransactions'] = transactions
    return render(request, 'users/myprofile.html', context)

def register (request):
    context = {}
    registered = False
    if request.method=='POST':
        uf = UserForm(data=request.POST)
        if uf.is_valid():
            user = uf.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(uf.errors)
    else:
        uf = UserForm()
        context['UserForm'] = UserForm
    context['registered'] = registered
    return render (request, 'users/register.html',context)

def log_in(request):
    context = {}
    if(request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            return render(request, 'transactions/transactions.html')
        else:
            return HttpResponse("Invalid Login")
    else:
        return render(request, 'users/login.html', context)

def log_out(request):
    context = {}
    logout(request)
    return render(request,'users/logout.html',context)

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