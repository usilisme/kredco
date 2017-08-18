from .base import *

DEBUG = False

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'kredco',
        'USER': 'usilisme',
        'PASSWORD':'Gab0lehtahu',
        'HOST':'localhost',
        'POST':'',
    }
}

STATIC_URL = '/static/'