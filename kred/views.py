# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect

from rest_framework.decorators import api_view
from rest_framework.response import Response

from promotions.models import Promotion
from kred.forms import SignUpForm

#SITE
def index(request):
    promotion_list = Promotion.objects.order_by('name')[:3]
    context_dict = {'promotions': promotion_list}
    return render (request, 'index.html', context_dict)

def about(request):
    return render(request, 'about.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

#API
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'Welcome To kred.co'
    })

