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

from merchants import views

urlpatterns = [
    #SITE
    url(r'^$'
        ,views.merchants, name='merchant'
    ),
    url(r'^signup/$'
        ,views.signup, name='signup'
    ),
    url(r'^myshops/$'
        ,views.myshops, name='myshops'
    ),
    url(r'detail/(?P<pk>\d+)/$',
        views.detail_merchant
        ,name='detail_merchant'
    ),

    #API
    url(r'^api/$'
        , views.vwListMerchant.as_view()
        , name='merchant-list'),
    url(r'^api/(?P<pk>[0-9]+)/$'
        , views.vwGetMerchant.as_view()
        , name='merchant-detail'),
]


