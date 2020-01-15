from .common import *

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'foundation',
        'USER': 'foundation',
        'PASSWORD': 'f0und4t10n01',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

