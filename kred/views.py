# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from promotions.models import Promotion

#SITE
def index(request):
    promotion_list = Promotion.objects.order_by('name')[:3]
    context_dict = {'promotions': promotion_list}
    return render (request, 'index.html', context_dict)

def about(request):
    return render(request, 'about.html')

def login(request):
    return render (request, 'login.html')

#API
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'Welcome To kred.co'
    })

