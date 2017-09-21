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
from kred import views
from users import views

router = routers.DefaultRouter()

urlpatterns = [
    #SITE
    url(r'^myprofile/$'
        ,views.myprofile, name='myprofile'
    ),
    url(
      r'signup/$'
        ,views.signup, name='signup'
    ),
    url(r'^signin/$'
        , views.signin, name='signin'
    ),
    url(r'^signout/$'
        , views.signout, name='signout'
    ),
    url(r'^resetpassword/$'
        , views.resetpassword, name='resetpassword'
    ),
    #API
    url(r'^api/register/$', views.vwCrUser.as_view(), name='register'),
    url(r'^api/login/$', views.vwLoginUser.as_view(),name = 'login'),
    url(r'^api/(?P<username>[\w-]+)/$'
        , views.vwGetUser.as_view()
        , name='user-profiles'),
    url(r'^(?P<username>[\w-]+)/reset-password/$', views.vwResetPass.as_view(), name='reset-password'),
]


