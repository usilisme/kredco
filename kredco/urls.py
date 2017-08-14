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

#router = routers.DefaultRouter()

urlpatterns = [
    #url(r'^$', views.index,name='index'),
    #url(r'^',include(router.urls)),
    url(r'^$', views.api_root),
    url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework')),

    url(r'^promo/$', views.PromoList.as_view()),
    url(r'^register/$', views.vwCrUser.as_view(), name='register'),
    url(r'^login/$', views.vwLoginUser.as_view(),name = 'login'),
    url(r'^admin/', admin.site.urls),
    url(r'^users/',include('users.urls', namespace='users')),
    url(r'^cards/',include('cards.urls', namespace='cards')),
    url(r'^transactions/', include('transactions.urls', namespace='transactions')),
]

