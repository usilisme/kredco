from kredco.settings.base import *

DEBUG = True

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

STATICFILES_DIRS = [STATIC_DIR,]

MEDIA_DIR = os.path.join(BASE_DIR,'media')
MEDIA_ROOT = MEDIA_DIR

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # During development only