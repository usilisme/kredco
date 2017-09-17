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
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views

from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from kred import views
from rest_framework_jwt.views import obtain_jwt_token
#router = routers.DefaultRouter()

urlpatterns = [
    #url(r'^$', views.index,name='index'),
    #url(r'^',include(router.urls)),
    url(r'^admin/', admin.site.urls),

    #SITE
    url(r'^$'
        , views.index, name='index'),
    url(r'^about/$'
        , views.about, name='about'
    ),
    url(
        r'^signup/$'
        ,views.signup, name='signup'
    ),
    url(r'^login/$'
        , auth_views.login, name='login'
        ),
    url(r'^myprofile/$'
        ,views.myprofile, name='myprofile'
    ),
    url(r'^logout/$'
        , auth_views.logout
        ,{'template_name':'registration/logout.html'}
        , name='logout'
        ),
  url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
  url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
  url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
      auth_views.password_reset_confirm, name='password_reset_confirm'),
  url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'^merchant/$'
        ,views.merchant, name='merchant'
    ),

    url(r'^payment/$'
        ,views.payment, name='payment'
    ),
    #API
    url(r'^api-auth/'
        ,include('rest_framework.urls',namespace='rest_framework')
        ),
    url(r'^api/$', views.api_root),
    url(r'^users/api/login/$'
        , obtain_jwt_token
        ),
    url(r'^promotions/'
        , include('promotions.urls',namespace='promotions'),
        ),
    url(r'^merchants/'
        , include('merchants.urls',namespace='merchants'),
        ),
    url(r'^users/'
        ,include('users.urls', namespace='users')
        ),
    url(r'^cards/'
        ,include('cards.urls', namespace='cards')
        ),
    url(r'^transactions/'
        , include('transactions.urls', namespace='transactions')
        ),
]
urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


