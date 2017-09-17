from .base import *

DEBUG = False

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

STATIC_ROOT = '/home/hendra/static/'
STATICFILES_DIRS = [STATIC_ROOT,STATIC_DIR, ]

MEDIA_DIR = '/home/hendra/media/'
MEDIA_ROOT = MEDIA_DIR