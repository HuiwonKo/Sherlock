from .common import *

DEBUG == False
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'room_thumbnail')

DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'hyuseoni.mysql.pythonanywhere-services.com',
        'NAME': 'hyuseoni$sherlock',
        'USER': 'hyuseoni',
        'PASSWORD': 'sherlock',
        'OPTIONS': {
            'sql_mode': 'traditional',  # strict mode
        },
    },
}
