"""kredco URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from transactions import views


urlpatterns = [
    url(
        r'^$'
        ,views.transactions, name='transactions'
    ),
    url(r'dashboard/$'
        ,views.dashboard, name='dashboard'
    ),
    url(
        r'history/$'
        ,views.history, name='history'
    ),
    url(r'delete/(?P<pk>\d+)/'
        ,views.cancel_transaction, name='cancel_transaction'
    ),
    url(
        r'payment/$'
        ,views.payment, name='payment'
    ),
    url(r'^api/$'
        , views.vwListTransaction.as_view()
        , name='transaction-list'
        ),
    url(r'^api/(?P<pk>[\w-]+)/$'
        , views.vwDtlTxn.as_view()
        , name='transaction-detail'),
]


