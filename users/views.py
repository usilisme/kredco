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

from users.serializers import (
    szGetUser,szGetUserProfile,szResetPass
)
from users.forms import (
    SignupForm, UserEditForm, EditProfileForm
)
from users.models import (
    User, UserProfile,
)
from cards.models import Card
from transactions.models import Transaction

User = get_user_model()

#SITE
def myprofile(request):
    context = {}
    u = request.user
    if request.method == 'POST':
        uf = UserEditForm(request.POST,instance=u)
        pf = EditProfileForm(request.POST,instance=u)
        if uf.is_valid():
            uf.save()
        if pf.is_valid():
            pf.save()
    else:
        uf = UserEditForm(instance=u)
        pf = EditProfileForm(instance=u)

    context['u'] = u
    context['uf'] = uf
    context['pf'] = pf
    return render(request, 'users/myprofile.html', context)

def signup (request):
    context = {}
    registered = False
    if request.method=='POST':
        uf = SignupForm(data=request.POST)
        if uf.is_valid():
            user = uf.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            context['errors'] = uf.errors.as_data()
    else:
        uf = SignupForm()
    context['form'] = uf
    context['registered'] = registered
    return render (request, 'users/signup.html',context)

def signin(request):
    context = {}

    if(request.method == 'POST'):
        print('init')
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = request.POST.get('remember')

        if User.objects.filter(username = username).exists():
            print('check username')
            user = authenticate(username=username, password=password)
            if user is not None:
                print('pass betul')
                #if (remember):
                 #   request.session.set_expiry(60)
                #else:
                 #   request.session.set_expiry(0)
                return render(request, 'transactions/tour.html')
            else:
                print ('pass salah')
                context['errorpassword'] = 'Wrong Password Entered.'
        else:
            print('usernmae ga ada')
            context['errorusername'] = 'Username entered does not exist.'

    return render(request, 'users/login.html', context)

def signout(request):
    context = {}
    logout(request)
    return render(request,'users/signout.html',context)

def resetpassword(request):
    context={}
    resetted = False
    if(request.method=='POST'):
        username = request.POST.get('username')
        password = request.POST.get('newpassword')
        try:
            user = User.objects.get(username__iexact=username)
            user.set_password(password)
            user.save()
            resetted = True
        except:
            context ['error'] = 'Username does not exist.'
    context['resetted'] = resetted
    return render(request,'users/resetpassword.html',context)

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