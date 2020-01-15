from .common import *
import socket
DEBUG = True

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'foundation',
        'USER': 'foundation',
        'PASSWORD': 'f0und4t10n01',
        'HOST': 'db',
        'PORT': '5432',
    }
}
INSTALLED_APPS = INSTALLED_APPS + ('debug_toolbar',)

MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')

# Fix when works on docker
INTERNAL_IPS = [
    '127.0.0.1',
    'localhost',
]

ip = socket.gethostbyname(socket.gethostname())
INTERNAL_IPS += [ip[:-1] + '1']
