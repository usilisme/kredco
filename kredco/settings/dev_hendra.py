from kredco.settings.base import *

DEBUG = True



# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATICFILES_DIRS = [STATIC_DIR,]

MEDIA_DIR = os.path.join(BASE_DIR,'media')
MEDIA_ROOT = MEDIA_DIR

LOGIN_URL = '/users/login/'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # During development only