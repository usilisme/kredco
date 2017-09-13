from kredco.settings.base import *

DEBUG = True

MEDIA_DIR = os.path.join(BASE_DIR,'media')

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

MEDIA_ROOT = MEDIA_DIR
MEDIA_URL = '/media/'
