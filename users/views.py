# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
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
from cards.forms import CardCreateForm
from cards.models import Card
from transactions.models import Transaction

User = get_user_model()

#SITE
@login_required
def myprofile(request):
    context = {}
    u = request.user
    cards = Card.objects.filter(owner=u)

    if request.method == 'POST':
        uf = UserEditForm(request.POST,instance=u)
        pf = EditProfileForm(request.POST,instance=u)
        cf = CardCreateForm(request.POST,initial={'owner':u})
        cf.owner = u
        if uf.is_valid():
            uf.save()
        if pf.is_valid():
            pf.save()
        if cf.is_valid():
            cf.save()
        else:
            print cf.errors
        context['u'] = u
        context['uf'] = uf
        context['pf'] = pf
        context['cf'] = cf
        context['cards'] = cards
        return redirect('/users/myprofile/')
    else:
        uf = UserEditForm(instance=u)
        pf = EditProfileForm(instance=u)
        cf = CardCreateForm(initial={'owner':u})
    context['u'] = u
    context['uf'] = uf
    context['pf'] = pf
    context['cf'] = cf
    context['cards'] = cards
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
            login(request,user)
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
            user = authenticate(username=username, password=password)
            if user is not None:
                if remember:
                    request.session.set_expiry(3600)
                else:
                    request.session.set_expiry(0)
                login(request, user)
                return render(request, 'transactions/tour.html',context)
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
    request.session.flush()
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