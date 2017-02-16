from .common import *

DEBUG == False
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'room_thumbnail')

DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'yeonjunpark.mysql.pythonanywhere-services.com',
        'NAME': 'yeonjunpark$sherlock',
        'USER': 'yeonjunpark',
        'PASSWORD': 'sherlock1',
        'OPTIONS': {
            'sql_mode': 'traditional',  # strict mode
        },
    },
}
