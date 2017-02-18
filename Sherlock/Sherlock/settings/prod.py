import os
from .common import *

DEBUG == False
ALLOWED_HOSTS = ['*']

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'room_thumbnail')

DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': '127.0.0.1',
        'NAME': 'ubuntu',
        'USER': 'ubuntu',
        'PASSWORD': 'sherlock.',
    },
}
