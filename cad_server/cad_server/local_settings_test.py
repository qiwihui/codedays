# coding: utf-8
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '80l6h^-p@y1ghasdfc-n!ees4cg_lp95$)zgp9+gp%qe@!-n'

DEBUG = True

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'NAME': 'test',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'mysql',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8'
        }
    }
}

ANYMAIL = {
    "MAILGUN_API_KEY": 'fake-mailgun-api-key',
    "MAILGUN_SENDER_DOMAIN": "mail.codedays.app"
}


ENCRYPT_KEY = b'fake-key'

# redis
BROKER_URL = 'redis://codedays-redis:6379/6'
# store task results in redis
CELERY_RESULT_BACKEND = 'redis://codedays-redis:6379/6'
